"""Conversation runtime — holds state across turns and runs the pipeline."""

from __future__ import annotations

import random
from dataclasses import dataclass

from .bwo import BwO
from .config import Config
from .llm import model_backend
from .persona import Persona
from .pipeline import run_turn
from .state import ConvState
from .trace import TurnTrace


@dataclass
class Runtime:
    cfg: Config
    persona: Persona
    state: ConvState
    rng: random.Random

    @classmethod
    def new(
        cls, persona: Persona, cfg: Config | None = None, seed: int | None = None
    ) -> "Runtime":
        cfg = cfg or Config()
        state = ConvState(bwo=BwO.from_seed(persona.bwo_seed))
        rng = random.Random(seed if seed is not None else cfg.seed)
        return cls(cfg=cfg, persona=persona, state=state, rng=rng)

    @classmethod
    def resume(cls, persona: Persona, traces: list[dict], cfg: Config | None = None) -> "Runtime":
        """Restore saved conversation state without replaying model calls."""
        if not traces:
            raise ValueError("The saved conversation has no turns.")
        runtime = cls.new(persona, cfg=cfg)
        previous = None
        for index, trace in enumerate(traces, 1):
            if any(not isinstance(trace.get(key), str) for key in
                   ("input_text", "response", "bwo_before", "bwo_after")):
                raise ValueError(f"Saved turn {index} is missing conversation or state text.")
            if previous is not None and trace["bwo_before"] != previous:
                raise ValueError(f"Saved turn {index} does not continue the previous state.")
            runtime.state.history.extend([
                {"role": "user", "content": trace["input_text"]},
                {"role": "persona", "content": trace["response"]},
            ])
            runtime.state.record_firing([firing[0] for firing in trace.get("fired", [])])
            previous = trace["bwo_after"]
        runtime.state.bwo.text = previous
        runtime.state.mode_history = [group["mode"] for group in traces[-1].get("groups", [])]
        return runtime

    async def turn(self, input_text: str) -> TurnTrace:
        with model_backend(self.cfg):
            trace = await run_turn(
                cfg=self.cfg,
                persona=self.persona,
                state=self.state,
                input_text=input_text,
                rng=self.rng,
            )
        # append AFTER the turn (the pipeline reads prior history)
        self.state.history.append({"role": "user", "content": input_text})
        self.state.history.append({"role": "persona", "content": trace.response})
        return trace

    def new_conversation(self) -> None:
        """Reset BwO + within-conversation state for a fresh conversation."""
        self.state = ConvState(bwo=BwO.from_seed(self.persona.bwo_seed))
