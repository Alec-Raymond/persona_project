"""Group synthesis — one LLM call per group; the synthesizer picks its mode."""

from __future__ import annotations

from .config import Config
from .grouping import allowed_modes
from .llm import call_llm
from .machine import Machine
from .models import GroupSynthesis
from .prompts import SYNTHESIS_SYSTEM, format_synthesis_user


async def synthesize_group(
    *,
    cfg: Config,
    group: list[Machine],
    out_by_name: dict[str, str],
    last_modes: list[str],
    bwo_text: str,
) -> GroupSynthesis:
    outputs = [(m.name, out_by_name.get(m.name, "")) for m in group]
    allowed = allowed_modes(len(group), cfg)

    res: GroupSynthesis = await call_llm(
        stage="synthesis",
        label=" + ".join(m.name for m in group),
        model=cfg.model_synth,
        system=SYNTHESIS_SYSTEM,
        user=format_synthesis_user(
            outputs=outputs,
            allowed_modes=allowed,
            last_modes=last_modes,
            bwo_text=bwo_text,
        ),
        schema=GroupSynthesis,
        max_tokens=cfg.synth_max_tokens,
        temperature=cfg.temp_synth,
    )

    # enforce the pair-constraint even if the model ignores it
    if res.mode not in allowed:
        res.mode = "disjunctive" if "disjunctive" in allowed else allowed[0]
    return res
