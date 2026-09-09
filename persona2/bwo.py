"""The Body without Organs — the persona's interior surface.

For the skeleton this is deliberately thin: a text buffer the machines write
through the pipeline, rewritten by the final machine each turn. Its form and
content emerge from those operations; we don't pre-impose structure (per the
redesign sketch — "there is no iceberg below the text").

The final machine is instructed to keep the surface bounded (letting old
content contract), so we don't need a separate compression mechanism yet.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BwO:
    text: str
    seed: str

    @classmethod
    def from_seed(cls, seed: str) -> "BwO":
        return cls(text=seed.strip(), seed=seed.strip())

    def reset(self) -> None:
        """Reset to seed at the start of each conversation."""
        self.text = self.seed

    @property
    def word_count(self) -> int:
        return len(self.text.split())
