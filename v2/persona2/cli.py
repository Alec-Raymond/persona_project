"""CLI: `persona2 chat <persona_dir>` and `persona2 inspect <trace.json>`.

chat runs the per-turn pipeline and renders the full firing trace by default
(the whole point of the skeleton is to see what the machinery did). Pass
`--quiet` to show only the response.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from rich.console import Console

from .config import CHEAP, MID, TOP, Config
from .persona import load_persona
from .runtime import Runtime

console = Console()

_TIERS = {"haiku": CHEAP, "sonnet": MID, "opus": TOP}


def _load_env() -> None:
    """Find an ANTHROPIC_API_KEY from common .env locations (incl. the V1 dir)."""
    here = Path(__file__).resolve().parent.parent  # v2/
    for p in (Path.cwd() / ".env", here / ".env", here.parent / "persona" / ".env"):
        if p.exists():
            load_dotenv(p, override=False)


def _default_persona() -> Path:
    return Path(__file__).resolve().parent.parent / "personas" / "testbed"


async def _chat(args: argparse.Namespace) -> None:
    persona = load_persona(args.persona)
    cfg = Config()
    if args.all:
        tier = _TIERS[args.all]
        cfg.model_selector = cfg.model_machine = cfg.model_synth = cfg.model_final = tier
    if args.final:
        cfg.model_final = _TIERS[args.final]
    if args.concurrency:
        cfg.concurrency = args.concurrency

    rt = Runtime.new(persona, cfg=cfg, seed=args.seed)
    console.print(
        f"[bold]{persona.name}[/bold] — {len(persona.always_on)} always-on, "
        f"{len(persona.pool)} in pool\n[dim]models: sel={cfg.model_selector} · "
        f"machine={cfg.model_machine} · synth={cfg.model_synth} · final={cfg.model_final}[/dim]"
    )

    save_dir = None
    if not args.no_save:
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        save_dir = Path(args.persona).resolve().parent.parent / "traces" / f"{persona.name}-{stamp}"

    messages = list(args.message or [])
    interactive = not messages
    n = 0
    while True:
        if messages:
            msg = messages.pop(0)
            console.print(f"\n[bold blue]you[/bold blue] › {msg}")
        elif interactive:
            try:
                msg = console.input("\n[bold blue]you[/bold blue] › ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if msg.lower() in {"exit", "quit", ":q"}:
                break
            if not msg:
                continue
        else:
            break

        trace = await rt.turn(msg)
        n += 1
        if args.quiet:
            console.print(f"\n[bold green]{persona.name}[/bold green] › {trace.response}")
        else:
            trace.render(console)
        if save_dir:
            path = trace.save(save_dir / f"turn-{n:03d}.json")
            console.print(f"[dim]trace → {path}[/dim]")


def _inspect(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.trace).read_text())
    # rebuild a minimal render from the saved dict
    from .trace import GroupTrace, TurnTrace

    t = TurnTrace(
        input_text=data["input_text"],
        response=data["response"],
        bwo_before=data["bwo_before"],
        bwo_after=data["bwo_after"],
        draft_response=data.get("draft_response", ""),
        justification=data.get("justification", ""),
        fit_reviews=data.get("fit_reviews", []),
        fired=[tuple(x) for x in data["fired"]],
        machine_outputs=data["machine_outputs"],
        edits=data.get("edits", []),
        relevance_picks=[tuple(x) for x in data["relevance_picks"]],
        random_picks=data["random_picks"],
        selection_scores=data["selection_scores"],
        groups=[GroupTrace(**g) for g in data["groups"]],
        calls=[],
        elapsed_s=data.get("totals", {}).get("elapsed_s", 0.0),
    )
    t.render(console)


def main(argv: list[str] | None = None) -> int:
    _load_env()
    parser = argparse.ArgumentParser(prog="persona2")
    sub = parser.add_subparsers(dest="cmd", required=True)

    pc = sub.add_parser("chat", help="run the per-turn pipeline interactively")
    pc.add_argument("persona", nargs="?", default=str(_default_persona()))
    pc.add_argument("-m", "--message", action="append", help="run this message (repeatable, non-interactive)")
    pc.add_argument("--all", choices=list(_TIERS), help="set ALL stage models to this tier")
    pc.add_argument("--final", choices=list(_TIERS), help="final-machine model tier (overrides --all for the final)")
    pc.add_argument("--seed", type=int, default=None)
    pc.add_argument("--concurrency", type=int, default=None)
    pc.add_argument("--quiet", action="store_true", help="show only the response")
    pc.add_argument("--no-save", action="store_true", help="don't save traces")

    pi = sub.add_parser("inspect", help="render a saved trace JSON")
    pi.add_argument("trace")

    pl = sub.add_parser("live", help="serve the live frontend (chat in the browser)")
    pl.add_argument("persona", nargs="?", default=str(_default_persona()))
    pl.add_argument("--all", choices=list(_TIERS), help="set ALL stage models to this tier")
    pl.add_argument("--final", choices=list(_TIERS), help="final-stage model tier")
    pl.add_argument("--port", type=int, default=8765)
    pl.add_argument("--concurrency", type=int, default=None)
    pl.add_argument("--no-browser", action="store_true")

    args = parser.parse_args(argv)
    if args.cmd == "chat":
        asyncio.run(_chat(args))
    elif args.cmd == "inspect":
        _inspect(args)
    elif args.cmd == "live":
        from .live import serve

        cfg = Config()
        if args.all:
            tier = _TIERS[args.all]
            cfg.model_selector = cfg.model_machine = cfg.model_synth = cfg.model_final = tier
        if args.final:
            cfg.model_final = _TIERS[args.final]
        if args.concurrency:
            cfg.concurrency = args.concurrency
        serve(args.persona, cfg, port=args.port, open_browser=not args.no_browser)
    return 0


if __name__ == "__main__":
    sys.exit(main())
