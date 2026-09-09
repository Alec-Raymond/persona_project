"""Conversation runtime — holds state across turns and runs the pipeline."""

from __future__ import annotations

import random
from dataclasses import dataclass

from .bwo import BwO
from .config import Config
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

    async def turn(self, input_text: str) -> TurnTrace:
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
