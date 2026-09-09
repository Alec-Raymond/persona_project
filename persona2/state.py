"""State that carries across turns within a conversation.

Per the redesign sketch, three things carry within a conversation: the BwO
text, `fire_count` per machine, and `mode_history` (last turn's mode choices).
Between-conversation state (machine set edits, memory corpus, ...) is the
ghostwriter's job and is out of scope for the skeleton.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .bwo import BwO


@dataclass
class ConvState:
    bwo: BwO
    fire_count: dict[str, int] = field(default_factory=dict)
    mode_history: list[str] = field(default_factory=list)  # modes used last turn
    history: list[dict[str, str]] = field(default_factory=list)  # {role, content}

    def record_firing(self, names: list[str]) -> None:
        for n in names:
            self.fire_count[n] = self.fire_count.get(n, 0) + 1

    # Prompt-facing speaker labels. "user"/"assistant" vocabulary is banned
    # here — it pulls the models into the assistant frame and blurs who is
    # speaking. The other person is exactly that; the persona is the persona.
    _LABELS = {"user": "the other person", "persona": "the persona"}

    def history_text(self, window: int) -> str:
        if not self.history:
            return "(Start of conversation. The other person is a stranger; no one has spoken yet.)"
        recent = self.history[-window * 2 :]
        return "\n".join(
            f"[{self._LABELS.get(m['role'], m['role'])}] {m['content']}" for m in recent
        )
