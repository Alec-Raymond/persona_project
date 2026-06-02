"""Selection — which machines fire this turn.

Skeleton voter set: always-on (deterministic) + relevance (LLM) + random
(deterministic), combined by a Gaussian-jittered weighted sum, top-N fires.
The compensation and habit/variation voters from the full design are deferred
(additive — they slot into the same combine step).
"""

from __future__ import annotations

import random
from dataclasses import dataclass, field

from .config import Config
from .llm import call_llm
from .machine import Machine, roster_text
from .models import RelevanceVotes
from .prompts import SELECTION_SYSTEM, format_selection_user


@dataclass
class SelectionResult:
    fired: list[tuple[Machine, str]]  # (machine, resonance) for the variable pool
    relevance: RelevanceVotes | None = None
    random_picks: list[str] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)


async def select(
    *,
    cfg: Config,
    pool: list[Machine],
    bwo_text: str,
    input_text: str,
    history: str,
    rng: random.Random,
) -> SelectionResult:
    """Pick top-N machines from the variable pool (always-on handled by caller)."""
    if not pool:
        return SelectionResult(fired=[])

    by_name = {m.name: m for m in pool}

    votes: RelevanceVotes = await call_llm(
        stage="selection",
        label="relevance",
        model=cfg.model_selector,
        system=SELECTION_SYSTEM,
        user=format_selection_user(
            roster=roster_text(pool),
            bwo_text=bwo_text,
            input_text=input_text,
            history=history,
            k=cfg.relevance_k,
        ),
        schema=RelevanceVotes,
        max_tokens=cfg.selector_max_tokens,
        temperature=cfg.temp_selector,
    )

    # relevance contributions (only valid roster names)
    rel: dict[str, tuple[float, str]] = {}
    for p in votes.picks:
        if p.name in by_name:
            rel[p.name] = (max(0.0, min(1.0, p.score)), p.reason)

    # random voter
    random_picks = rng.sample(list(by_name), k=min(cfg.random_k, len(by_name)))

    # Gaussian-jittered weights so the same voter doesn't always dominate
    w_rel = max(0.0, cfg.w_relevance + rng.gauss(0, cfg.weight_noise))
    w_rand = max(0.0, cfg.w_random + rng.gauss(0, cfg.weight_noise))

    scores: dict[str, float] = {}
    for name, (score, _) in rel.items():
        scores[name] = scores.get(name, 0.0) + w_rel * score
    for name in random_picks:
        scores[name] = scores.get(name, 0.0) + w_rand * 1.0

    ranked = sorted(scores, key=lambda n: scores[n], reverse=True)[: cfg.top_n]

    fired: list[tuple[Machine, str]] = []
    for name in ranked:
        resonance = rel[name][1] if name in rel else "surfaced by variation"
        fired.append((by_name[name], resonance))

    return SelectionResult(
        fired=fired, relevance=votes, random_picks=random_picks, scores=scores
    )
