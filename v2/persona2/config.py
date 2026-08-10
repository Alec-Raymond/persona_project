"""Tunable parameters and model tiers for the per-turn pipeline.

Everything here is meant to be swept empirically (see the redesign sketch's
"Tunable parameters" section). Defaults are skeleton-scale: small N, cheap
models, so a turn is fast and cheap to inspect.
"""

from __future__ import annotations

from dataclasses import dataclass

# --- Model tiers (exact API IDs) ---
CHEAP = "claude-haiku-4-5-20251001"  # selectors, per-machine calls — narrow work
MID = "claude-sonnet-5"         # group synthesizers — mode-choice + synthesis
TOP = "claude-opus-4-8"         # final machine — most context, the response

# The four group-synthesis modes. Transcendent function is pairs-only.
MODES = ("connective", "disjunctive", "conjunctive", "transcendent")


@dataclass
class Config:
    """Per-run configuration. Skeleton defaults; tune freely."""

    # --- selection ---
    top_n: int = 5              # variable machines that fire per turn (+ always-on set)
    relevance_k: int = 6       # the relevance voter nominates up to k machines
    random_k: int = 3          # the random voter draws k machines
    # weights for combining voters (Gaussian noise added at runtime)
    w_relevance: float = 1.0
    w_random: float = 0.4
    weight_noise: float = 0.15

    # --- grouping ---
    min_group: int = 2
    max_group: int = 4

    # --- models per stage ---
    model_selector: str = CHEAP
    model_machine: str = CHEAP
    model_synth: str = MID
    model_final: str = MID     # bump to TOP once wiring is proven

    # --- llm call shape ---
    selector_max_tokens: int = 700
    machine_max_tokens: int = 1000   # ANALYSIS (~100w) + PRODUCT (~250w)
    synth_max_tokens: int = 1600     # thinking (~100w) + result (250w+), JSON
    final_max_tokens: int = 4200     # thinking (500w) + surface (500w) + edits + reply + justification
    response_max_tokens: int = 600   # armor + redraft calls (the spoken reply)
    fit_max_tokens: int = 700        # blind fit-check verdicts
    fit_max_rounds: int = 2          # max redraft rounds after a failed fit
    concurrency: int = 8       # max simultaneous LLM calls (semaphore)

    # temperatures
    temp_selector: float = 0.4
    temp_machine: float = 1.0
    temp_synth: float = 1.0
    temp_final: float = 1.0

    # --- bookkeeping ---
    history_window: int = 12   # conversation turns shown to selectors/final
    seed: int | None = None    # set for reproducible grouping/random selection
