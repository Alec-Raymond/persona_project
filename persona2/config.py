"""Tunable parameters and model tiers for the per-turn pipeline.

Model defaults depend on the backend. Codex uses Astra; Anthropic and the
Claude CLI use Sonnet. Haiku is available as an explicit override.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field

# --- Model tiers (exact API IDs) ---
CHEAP = "claude-haiku-4-5-20251001"  # selectors, per-machine calls — narrow work
MID = "claude-sonnet-5"         # group synthesizers — mode-choice + synthesis
TOP = "claude-opus-4-8"         # final machine — most context, the response
ASTRA = "gpt-6-astra"
BACKENDS = ("anthropic", "claude", "codex")
REASONING_EFFORTS = ("low", "medium", "high", "xhigh", "max")


def default_backend() -> str:
    """Preserve the older Claude CLI setting unless a backend is explicit."""
    return os.environ.get("PERSONA2_BACKEND") or (
        "claude" if os.environ.get("PERSONA2_CLAUDE_CLI") else "anthropic"
    )

# The four group-synthesis modes. Transcendent function is pairs-only.
MODES = ("connective", "disjunctive", "conjunctive", "transcendent")


@dataclass
class Config:
    """Per-run configuration, including the model transport."""

    backend: str = field(default_factory=default_backend)
    reasoning_effort: str = "medium"  # Codex only
    call_timeout: float = 300.0       # seconds per Codex call

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
    model_selector: str | None = None
    model_machine: str | None = None
    model_synth: str | None = None
    model_final: str | None = None

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

    def __post_init__(self) -> None:
        if self.backend not in BACKENDS:
            raise ValueError(f"Unknown backend: {self.backend}. Choose from {', '.join(BACKENDS)}.")
        if self.reasoning_effort not in REASONING_EFFORTS:
            raise ValueError(f"Unknown reasoning effort: {self.reasoning_effort}")
        if self.call_timeout <= 0:
            raise ValueError("Call timeout must be positive.")
        default_model = ASTRA if self.backend == "codex" else MID
        for name in ("model_selector", "model_machine", "model_synth", "model_final"):
            if getattr(self, name) is None:
                setattr(self, name, default_model)
