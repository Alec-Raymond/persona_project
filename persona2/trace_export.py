"""Export a selected, multi-turn Astra run for the replay website.

    python -m persona2.trace_export traces/<run> conversation.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .machine import load_machines


def export_run(directory: Path, *, title: str | None = None) -> dict:
    files = sorted(directory.glob("turn-*.json"))
    if len(files) < 2:
        raise ValueError("Record at least two turns before exporting a conversation.")
    turns = [json.loads(path.read_text()) for path in files]
    for index, turn in enumerate(turns):
        calls = turn.get("calls", [])
        if not calls or any(call.get("model") != "gpt-6-astra" for call in calls):
            raise ValueError(f"Turn {index + 1} must use gpt-6-astra for every recorded call.")
        if index and turn["bwo_before"] != turns[index - 1]["bwo_after"]:
            raise ValueError(f"Turn {index + 1} does not continue the previous turn's state.")
    opening = " ".join(turns[0]["input_text"].split())
    default_title = opening[:72] + ("…" if len(opening) > 72 else "")
    persona = directory.name.rsplit("-", 2)[0].removesuffix("-live")
    root = Path(__file__).resolve().parent.parent
    roster = []
    for base in (root / "personas", root / "wiki" / "archive" / "personas"):
        manifest = base / persona / "manifest.yaml"
        if manifest.is_file():
            roster = [{"name": machine.name, "category": machine.category,
                       "sensitivity": machine.sensitivity.strip()}
                      for machine in load_machines(manifest)]
            break
    return {
        "format": "persona-trace-run-v1",
        "id": directory.name,
        "title": title or default_title or "Conversation",
        "persona": persona,
        "roster": roster,
        "model": "gpt-6-astra",
        "turns": turns,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--title")
    args = parser.parse_args()
    try:
        result = export_run(args.directory, title=args.title)
    except ValueError as exc:
        parser.error(str(exc))
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Exported {len(result['turns'])} Astra turns to {args.output}")


if __name__ == "__main__":
    main()
