"""Grouping — randomly partition the firing set into groups of 2–4.

The synthesis mode is NOT assigned here; each group's synthesizer chooses its
own mode (see synthesis.py). Grouping only decides membership. We avoid
size-1 groups (nothing to synthesize) by merging a leftover singleton.
"""

from __future__ import annotations

import random

from .config import Config
from .machine import Machine


def partition(
    machines: list[Machine], cfg: Config, rng: random.Random
) -> list[list[Machine]]:
    items = machines[:]
    rng.shuffle(items)

    if len(items) <= cfg.max_group:
        return [items] if items else []

    groups: list[list[Machine]] = []
    i = 0
    n = len(items)
    while i < n:
        remaining = n - i
        # keep group sizes in [min_group, max_group]; don't strand a singleton
        hi = min(cfg.max_group, remaining)
        lo = cfg.min_group
        if remaining - hi == 1:  # would leave a singleton next round
            hi -= 1
        size = rng.randint(lo, max(lo, hi))
        groups.append(items[i : i + size])
        i += size

    # safety: fold any singleton into the previous group
    if len(groups) >= 2 and len(groups[-1]) == 1:
        groups[-2].extend(groups.pop())
    return groups


def allowed_modes(group_size: int, cfg: Config) -> list[str]:
    """Transcendent function is pairs-only; everything else always available."""
    modes = ["connective", "disjunctive", "conjunctive"]
    if group_size == 2:
        modes.append("transcendent")
    return modes
