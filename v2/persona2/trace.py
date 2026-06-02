"""The firing trace — the full per-turn record.

This is both the debugging view (read what every stage did) and the artifact
the between-conversation ghostwriter will eventually consume. Building it now
is not throwaway work.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path

from .llm import LLMCall


@dataclass
class GroupTrace:
    members: list[str]
    mode: str
    summaries: list[tuple[str, str]]
    result: str


@dataclass
class TurnTrace:
    input_text: str
    response: str
    bwo_before: str
    bwo_after: str
    fired: list[tuple[str, str, str]] = field(default_factory=list)  # name, shape, resonance
    machine_outputs: dict[str, str] = field(default_factory=dict)
    relevance_picks: list[tuple[str, float, str]] = field(default_factory=list)
    random_picks: list[str] = field(default_factory=list)
    selection_scores: dict[str, float] = field(default_factory=dict)
    groups: list[GroupTrace] = field(default_factory=list)
    calls: list[LLMCall] = field(default_factory=list)
    elapsed_s: float = 0.0

    # --- totals ---
    def totals(self) -> dict[str, int | float]:
        return {
            "calls": len(self.calls),
            "input_tokens": sum(c.input_tokens for c in self.calls),
            "output_tokens": sum(c.output_tokens for c in self.calls),
            "cache_read_tokens": sum(c.cache_read_tokens for c in self.calls),
            "elapsed_s": round(self.elapsed_s, 2),
        }

    # --- persistence ---
    def to_dict(self) -> dict:
        d = asdict(self)
        d["totals"] = self.totals()
        return d

    def save(self, path: str | Path) -> Path:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(self.to_dict(), indent=2))
        return p

    # --- pretty render ---
    def render(self, console=None) -> None:
        from rich.console import Console
        from rich.panel import Panel
        from rich.rule import Rule
        from rich.table import Table

        c = console or Console()

        c.print(Rule("[bold]SELECTION[/bold]"))
        tbl = Table(show_header=True, header_style="bold", box=None)
        tbl.add_column("machine")
        tbl.add_column("shape")
        tbl.add_column("score", justify="right")
        tbl.add_column("why it fired", overflow="fold")
        for name, shape, reson in self.fired:
            score = self.selection_scores.get(name)
            tbl.add_row(name, shape, f"{score:.2f}" if score is not None else "—", reson)
        c.print(tbl)

        c.print(Rule("[bold]MACHINE OUTPUTS[/bold]"))
        for name, _, _ in self.fired:
            out = self.machine_outputs.get(name, "")
            c.print(Panel(out, title=name, title_align="left", border_style="dim"))

        c.print(Rule("[bold]GROUP SYNTHESES[/bold]"))
        for i, g in enumerate(self.groups):
            head = f"Group {i + 1}  [{g.mode}]  ·  {', '.join(g.members)}"
            c.print(Panel(g.result, title=head, title_align="left", border_style="cyan"))

        c.print(Rule("[bold]BwO (after)[/bold]"))
        c.print(Panel(self.bwo_after, border_style="magenta"))

        c.print(Rule("[bold green]RESPONSE[/bold green]"))
        c.print(Panel(self.response, border_style="green"))

        t = self.totals()
        c.print(
            f"[dim]{t['calls']} calls · in {t['input_tokens']} "
            f"(cache {t['cache_read_tokens']}) · out {t['output_tokens']} "
            f"· {t['elapsed_s']}s[/dim]"
        )
