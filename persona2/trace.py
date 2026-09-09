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
    result: str = ""
    # The synthesizer's free-association phase (new traces).
    thinking: str = ""
    # One-line-per-machine summaries (legacy traces only).
    summaries: list[tuple[str, str]] = field(default_factory=list)


@dataclass
class TurnTrace:
    input_text: str
    response: str
    bwo_before: str
    bwo_after: str
    # What the persona was about to say before the armoring pass bent it.
    draft_response: str = ""
    # The interior editor's own account of why the reply speaks from the
    # surface. Instrumentation; never fed back into the run.
    justification: str = ""
    # Blind-reader verdicts per armor round: {round, response, fits, explanation}.
    fit_reviews: list[dict] = field(default_factory=list)
    fired: list[tuple[str, str, str]] = field(default_factory=list)  # name, shape, resonance
    machine_outputs: dict[str, str] = field(default_factory=dict)
    # Why the surface changed: {change, driven_by[], why} per substantive edit.
    # Written by the final machine as instrumentation; never fed back into the run.
    edits: list[dict] = field(default_factory=list)
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

        if self.edits:
            c.print(Rule("[bold]WHY THE SURFACE CHANGED[/bold]"))
            etbl = Table(show_header=True, header_style="bold", box=None)
            etbl.add_column("change", overflow="fold")
            etbl.add_column("driven by")
            etbl.add_column("why", overflow="fold")
            for e in self.edits:
                etbl.add_row(e.get("change", ""), ", ".join(e.get("driven_by", [])), e.get("why", ""))
            c.print(etbl)

        if self.draft_response and self.draft_response != self.response:
            c.print(Rule("[bold]DRAFT (before armoring)[/bold]"))
            c.print(Panel(self.draft_response, border_style="dim"))

        if self.justification:
            c.print(Rule("[bold]WHY THE REPLY (editor's justification)[/bold]"))
            c.print(Panel(self.justification, border_style="dim"))

        if self.fit_reviews:
            c.print(Rule("[bold]FIT CHECKS (blind reader)[/bold]"))
            for r in self.fit_reviews:
                verdict = "[green]FITS[/green]" if r.get("fits") else "[red]DOES NOT FIT[/red]"
                c.print(f"round {r.get('round')}: {verdict} — {r.get('explanation', '')}")

        c.print(Rule("[bold green]RESPONSE[/bold green]"))
        c.print(Panel(self.response, border_style="green"))

        t = self.totals()
        c.print(
            f"[dim]{t['calls']} calls · in {t['input_tokens']} "
            f"(cache {t['cache_read_tokens']}) · out {t['output_tokens']} "
            f"· {t['elapsed_s']}s[/dim]"
        )
