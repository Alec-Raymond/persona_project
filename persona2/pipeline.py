"""The per-turn pipeline.

selection → per-machine (parallel) → grouping → group synthesis (parallel)
→ interior editor → armor. Returns a full TurnTrace (which carries the
response).

Every generative stage is two-phase — a free-association thinking part and
a product part — and every output stands alone: each stage's text carries
its own referents because its reader never sees its inputs. The interior
editor thinks (500w), rewrites the surface, logs edits, and writes the
initial reply; the armor selects the spark from that reply, sized by the
Pulsation machine's rhythm read and tuned by the new surface. Stages
1 → (2,3) → 4 → 5 are sequential; fan-out within stages 2 and 4 is bounded
by a semaphore (cfg.concurrency).
"""

from __future__ import annotations

import asyncio
import random
import re
import time

from . import events
from .config import Config
from .llm import call_llm, capture
from .machine import Machine
from .models import BwoEdit, FitCheck
from .persona import Persona
from .prompts import (
    ARMOR_SYSTEM,
    BWO_EDIT_SYSTEM,
    FIT_SYSTEM,
    MACHINE_SYSTEM,
    REDRAFT_SYSTEM,
    format_armor_user,
    format_bwo_edit_user,
    format_fit_user,
    format_machine_user,
    format_redraft_user,
)
from .grouping import partition
from .selection import select
from .state import ConvState
from .synthesis import synthesize_group
from .trace import GroupTrace, TurnTrace


# The PRODUCT heading of a machine's two-part output (tolerates ## or **).
_PRODUCT_RE = re.compile(r"(?m)^\s*#{0,3}\s*\**PRODUCT\**\s*:?\s*$")


def _product_only(text: str) -> str:
    """The part of a machine's output that travels downstream.

    The ANALYSIS is instrumentation (trace-only); only the PRODUCT reaches
    the synthesizers. Falls back to the whole text if the heading is absent.
    """
    parts = _PRODUCT_RE.split(text)
    return parts[-1].strip() if len(parts) > 1 else text.strip()


async def _fire_machine(
    sem: asyncio.Semaphore,
    cfg: Config,
    m: Machine,
    resonance: str,
    bwo_text: str,
    input_text: str,
    history: str,
) -> str:
    async with sem:
        return await call_llm(
            stage="machine",
            label=m.name,
            model=cfg.model_machine,
            system=MACHINE_SYSTEM,
            user=format_machine_user(
                machine=m,
                resonance=resonance,
                bwo_text=bwo_text,
                input_text=input_text,
                history=history,
            ),
            max_tokens=cfg.machine_max_tokens,
            temperature=cfg.temp_machine,
        )


async def run_turn(
    *,
    cfg: Config,
    persona: Persona,
    state: ConvState,
    input_text: str,
    rng: random.Random | None = None,
) -> TurnTrace:
    rng = rng or random.Random(cfg.seed)
    history = state.history_text(cfg.history_window)
    bwo_before = state.bwo.text
    sem = asyncio.Semaphore(cfg.concurrency)

    with capture() as calls:
        t0 = time.monotonic()
        events.emit("turn_started", input=input_text, bwo=bwo_before)

        # 1. selection (always-on bypass the vote)
        events.emit("stage_started", stage="selection")
        sel = await select(
            cfg=cfg,
            pool=persona.pool,
            bwo_text=bwo_before,
            input_text=input_text,
            history=history,
            rng=rng,
        )
        fired: list[tuple[Machine, str]] = [
            (m, "(always-on)") for m in persona.always_on
        ] + sel.fired
        events.emit(
            "selection_done",
            fired=[
                {
                    "name": m.name,
                    "category": m.category,
                    "sensitivity": m.sensitivity.strip(),
                    "resonance": res,
                }
                for m, res in fired
            ],
        )

        # 2. per-machine, in parallel
        events.emit("stage_started", stage="machines")
        outputs = await asyncio.gather(
            *(
                _fire_machine(sem, cfg, m, res, bwo_before, input_text, history)
                for m, res in fired
            )
        )
        out_by_name = {m.name: o for (m, _), o in zip(fired, outputs)}
        product_by_name = {n: _product_only(o) for n, o in out_by_name.items()}
        fired_machines = [m for m, _ in fired]

        # 3. grouping (random partition into 2–4)
        groups = partition(fired_machines, cfg, rng)
        events.emit(
            "groups_assigned", groups=[[m.name for m in g] for g in groups]
        )

        # 4. group synthesis, in parallel
        events.emit("stage_started", stage="synthesis")
        async def _syn(group: list[Machine]):
            async with sem:
                return await synthesize_group(
                    cfg=cfg,
                    group=group,
                    out_by_name=product_by_name,
                    last_modes=state.mode_history,
                    bwo_text=bwo_before,
                )

        syntheses = await asyncio.gather(*(_syn(g) for g in groups))
        for gi, (g, s) in enumerate(zip(groups, syntheses)):
            events.emit(
                "synthesis_done",
                group=gi + 1,
                members=[m.name for m in g],
                mode=s.mode,
                thinking=s.thinking,
                result=s.result,
            )

        # 5a. interior editor — thinks (500w), rewrites the surface, logs
        # the edits, and writes the initial (pre-armor) reply. The voice
        # governs only the reply.
        events.emit("stage_started", stage="editor")
        bwo_edit: BwoEdit = await call_llm(
            stage="final",
            label="interior-editor",
            model=cfg.model_final,
            system=BWO_EDIT_SYSTEM,
            user=format_bwo_edit_user(
                bwo_text=bwo_before,
                groups=[(s.thinking, s.result) for s in syntheses],
                input_text=input_text,
                history=history,
                voice_sketch=persona.voice_sketch,
            ),
            schema=BwoEdit,
            max_tokens=cfg.final_max_tokens,
            temperature=cfg.temp_final,
        )

        # 5b-5d. armor → blind fit-check → redraft loop. The armor selects
        # the spark from the current draft; a blind reader (situation +
        # conversation only, no interior) judges fit; on failure its
        # explanation goes back to a redraft, and the loop re-armors.
        initial_reply = (bwo_edit.revised_response or bwo_edit.response).strip()
        bwo_after_text = bwo_edit.bwo.strip()
        events.emit(
            "editor_done",
            bwo=bwo_after_text,
            edits=[e.model_dump() for e in bwo_edit.edits],
            response=initial_reply,
            justification=bwo_edit.justification.strip(),
            revised=bool(bwo_edit.revised_response.strip()),
        )
        events.emit("stage_started", stage="armor")
        draft_current = initial_reply
        fit_reviews: list[dict] = []
        response = ""
        for round_i in range(cfg.fit_max_rounds + 1):
            response = await call_llm(
                stage="final",
                label="armor" if round_i == 0 else f"armor-{round_i + 1}",
                model=cfg.model_final,
                system=ARMOR_SYSTEM,
                user=format_armor_user(
                    draft=draft_current,
                    bwo_text=bwo_after_text,
                    voice_sketch=persona.voice_sketch,
                    input_text=input_text,
                    history=history,
                ),
                max_tokens=cfg.response_max_tokens,
                temperature=cfg.temp_final,
            )
            fit: FitCheck = await call_llm(
                stage="final",
                label=f"fit-check-{round_i + 1}",
                model=cfg.model_synth,
                system=FIT_SYSTEM,
                user=format_fit_user(
                    situation=persona.situation,
                    history=history,
                    input_text=input_text,
                    response=response,
                ),
                schema=FitCheck,
                max_tokens=cfg.fit_max_tokens,
                temperature=cfg.temp_synth,
            )
            fit_reviews.append(
                {
                    "round": round_i + 1,
                    "response": response.strip(),
                    "fits": fit.fits,
                    "explanation": fit.explanation.strip(),
                }
            )
            events.emit("fit_round", **fit_reviews[-1])
            if fit.fits or round_i == cfg.fit_max_rounds:
                break
            draft_current = await call_llm(
                stage="final",
                label=f"redraft-{round_i + 1}",
                model=cfg.model_final,
                system=REDRAFT_SYSTEM,
                user=format_redraft_user(
                    situation=persona.situation,
                    history=history,
                    input_text=input_text,
                    failed_reply=response,
                    explanation=fit.explanation,
                    bwo_text=bwo_after_text,
                    voice_sketch=persona.voice_sketch,
                ),
                max_tokens=cfg.response_max_tokens,
                temperature=cfg.temp_final,
            )
        elapsed = time.monotonic() - t0
        events.emit(
            "turn_done", response=response.strip(), bwo_after=bwo_after_text
        )

    # --- commit state ---
    state.bwo.text = bwo_edit.bwo.strip()
    state.record_firing([m.name for m in fired_machines])
    state.mode_history = [s.mode for s in syntheses]

    # --- build trace ---
    group_traces = [
        GroupTrace(
            members=[m.name for m in g],
            mode=s.mode,
            thinking=s.thinking,
            result=s.result,
        )
        for g, s in zip(groups, syntheses)
    ]

    return TurnTrace(
        input_text=input_text,
        response=response.strip(),
        bwo_before=bwo_before,
        bwo_after=state.bwo.text,
        draft_response=initial_reply,
        justification=bwo_edit.justification.strip(),
        fit_reviews=fit_reviews,
        fired=[(m.name, m.shape, res) for m, res in fired],
        machine_outputs=out_by_name,
        edits=[e.model_dump() for e in bwo_edit.edits],
        relevance_picks=(
            [(p.name, p.score, p.reason) for p in sel.relevance.picks]
            if sel.relevance
            else []
        ),
        random_picks=sel.random_picks,
        selection_scores=sel.scores,
        groups=group_traces,
        calls=list(calls),
        elapsed_s=elapsed,
    )
