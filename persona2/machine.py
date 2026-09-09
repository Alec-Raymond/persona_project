"""Desiring machines — the narrow analytical agents.

A machine is specified by what it latches onto (sensitivity), what it produces
(flow), and persona-specific tuning (calibration). Its `shape` says what kind
of work it does:

- analysis    — reads the situation/BwO, produces an analytical flow
- proposal    — contributes its own content (a memory, a fantasy) without
                reading state in detail
- modulation  — shapes tone/tempo/intensity rather than adding content

`always_on` machines bypass voting and fire every turn (the constitutive set).
The rest are nominated by the selection voters.

Deep-end discipline: a finished machine is specified in concrete surface terms;
the theory that inspired it is provenance, not operating instructions.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

SHAPES = ("analysis", "proposal", "modulation")


@dataclass
class Machine:
    name: str
    category: str
    shape: str
    sensitivity: str
    flow: str
    always_on: bool = False
    calibration: str = ""

    def __post_init__(self) -> None:
        if self.shape not in SHAPES:
            raise ValueError(
                f"Machine {self.name!r}: shape {self.shape!r} not in {SHAPES}"
            )

    def brief(self) -> str:
        """One line for the selection roster."""
        tag = "always-on" if self.always_on else self.shape
        return f"- {self.name} [{self.category}/{tag}]: {self.sensitivity.strip()}"

    def spec(self) -> str:
        """Full spec for the machine's own firing prompt.

        Category and shape are deliberately absent: the category enters the
        prompt as its guidance block (prompts.CATEGORY_GUIDANCE), and shape is
        pipeline metadata a firing machine has no use for.
        """
        parts = [
            f"Machine: {self.name}",
            f"Sensitivity (what you latch onto): {self.sensitivity.strip()}",
            f"Flow (what you produce when you fire): {self.flow.strip()}",
        ]
        if self.calibration.strip():
            parts.append(f"Calibration (this persona's tuning): {self.calibration.strip()}")
        return "\n".join(parts)


def load_machines(path: str | Path) -> list[Machine]:
    """Load a machine manifest (YAML list under key `machines`)."""
    data = yaml.safe_load(Path(path).read_text())
    return [Machine(**m) for m in data["machines"]]


def roster_text(machines: list[Machine]) -> str:
    """The variable-pool roster shown to the selection voters."""
    return "\n".join(m.brief() for m in machines)
