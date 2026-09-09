"""A persona = a machine set + a voice sketch + a BwO seed.

For the skeleton these are loaded from a persona directory:

    <persona>/
      manifest.yaml   # machines (always-on + variable pool)
      voice.md        # six-dimensional Bakhtinian voice sketch (free text ok)
      bwo_seed.txt    # the intensive surface the BwO resets to each conversation
      situation.txt   # the scenario the conversation happens in (optional)
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .machine import Machine, load_machines

DEFAULT_SITUATION = (
    "Two strangers, seated near each other in a public waiting place. They "
    "have never met and know nothing about each other. Either may speak; "
    "nothing obliges them to."
)


@dataclass
class Persona:
    name: str
    machines: list[Machine]
    voice_sketch: str
    bwo_seed: str
    situation: str = DEFAULT_SITUATION

    @property
    def always_on(self) -> list[Machine]:
        return [m for m in self.machines if m.always_on]

    @property
    def pool(self) -> list[Machine]:
        return [m for m in self.machines if not m.always_on]


def load_persona(path: str | Path) -> Persona:
    d = Path(path)
    machines = load_machines(d / "manifest.yaml")
    voice = ""
    for fn in ("voice.md", "voice.txt"):
        p = d / fn
        if p.exists():
            voice = p.read_text().strip()
            break
    seed = (d / "bwo_seed.txt").read_text().strip()
    sit_path = d / "situation.txt"
    situation = sit_path.read_text().strip() if sit_path.exists() else DEFAULT_SITUATION
    return Persona(
        name=d.name,
        machines=machines,
        voice_sketch=voice,
        bwo_seed=seed,
        situation=situation,
    )
