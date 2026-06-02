"""The per-turn pipeline.

selection → per-machine (parallel) → grouping → group synthesis (parallel)
→ final machine. Returns a full TurnTrace (which carries the response).

Stages 1 → (2,3) → 4 → 5 are sequential; the fan-out within stages 2 and 4 is
bounded by a semaphore (cfg.concurrency).
"""

from __future__ import annotations

import asyncio
import random
import time

from .config import Config
from .llm import call_llm, capture
from .machine import Machine
from .models import FinalOutput
from .persona import Persona
from .prompts import (
    FINAL_SYSTEM,
    MACHINE_SYSTEM,
    format_final_user,
    format_machine_user,
)
from .grouping import partition
from .selection import select
from .state import ConvState
from .synthesis import synthesize_group
from .trace import GroupTrace, TurnTrace


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

        # 1. selection (always-on bypass the vote)
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

        # 2. per-machine, in parallel
        outputs = await asyncio.gather(
            *(
                _fire_machine(sem, cfg, m, res, bwo_before, input_text, history)
                for m, res in fired
            )
        )
        out_by_name = {m.name: o for (m, _), o in zip(fired, outputs)}
        fired_machines = [m for m, _ in fired]

        # 3. grouping (random partition into 2–4)
        groups = partition(fired_machines, cfg, rng)

        # 4. group synthesis, in parallel
        async def _syn(group: list[Machine]):
            async with sem:
                return await synthesize_group(
                    cfg=cfg,
                    group=group,
                    out_by_name=out_by_name,
                    last_modes=state.mode_history,
                    bwo_text=bwo_before,
                )

        syntheses = await asyncio.gather(*(_syn(g) for g in groups))

        # 5. final machine — edits BwO + speaks
        final: FinalOutput = await call_llm(
            stage="final",
            label="final",
            model=cfg.model_final,
            system=FINAL_SYSTEM,
            user=format_final_user(
                voice_sketch=persona.voice_sketch,
                bwo_text=bwo_before,
                group_results=[s.result for s in syntheses],
                input_text=input_text,
                history=history,
            ),
            schema=FinalOutput,
            max_tokens=cfg.final_max_tokens,
            temperature=cfg.temp_final,
        )
        elapsed = time.monotonic() - t0

    # --- commit state ---
    state.bwo.text = final.bwo.strip()
    state.record_firing([m.name for m in fired_machines])
    state.mode_history = [s.mode for s in syntheses]

    # --- build trace ---
    group_traces = [
        GroupTrace(
            members=[m.name for m in g],
            mode=s.mode,
            summaries=[(ms.machine, ms.summary) for ms in s.summaries],
            result=s.result,
        )
        for g, s in zip(groups, syntheses)
    ]

    return TurnTrace(
        input_text=input_text,
        response=final.response.strip(),
        bwo_before=bwo_before,
        bwo_after=state.bwo.text,
        fired=[(m.name, m.shape, res) for m, res in fired],
        machine_outputs=out_by_name,
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
