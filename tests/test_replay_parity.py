"""The hosted replay must reproduce the tuned Python event sequence and timing."""

import json
import shutil
import subprocess
from dataclasses import asdict
from pathlib import Path
from types import SimpleNamespace

import pytest

from persona2.cli import _default_persona
from persona2.live import Session
from persona2.persona import load_persona


def capture_local(turn, persona, monkeypatch):
    elapsed = 0.0
    events = []

    def advance(seconds):
        nonlocal elapsed
        elapsed += seconds

    session = object.__new__(Session)
    session.persona = persona
    session.hub = SimpleNamespace(emit=lambda event: events.append({
        "at_ms": round(elapsed * 1000), "event": event,
    }))
    monkeypatch.setattr("persona2.live.time.sleep", advance)
    session._replay_turn(turn)
    return events


def capture_hosted(turn, persona):
    script = Path(__file__).resolve().parent.parent / "replay-site/lib/replay-events.mjs"
    program = f"""
import {{ replayTurn }} from {json.dumps(script.as_uri())};
let input = ''; for await (const chunk of process.stdin) input += chunk;
const {{ turn, roster }} = JSON.parse(input);
let elapsed = 0; const events = [];
await replayTurn(turn, roster, {{
  emit: event => events.push({{ at_ms: elapsed, event }}),
  sleep: async ms => {{ elapsed += ms; }},
}});
process.stdout.write(JSON.stringify(events));
"""
    result = subprocess.run(
        ["node", "--input-type=module", "-e", program],
        input=json.dumps({"turn": turn, "roster": [asdict(machine) for machine in persona.machines]}),
        capture_output=True, text=True, check=True,
    )
    return json.loads(result.stdout)


@pytest.mark.skipif(shutil.which("node") is None, reason="Node is needed for the hosted replay check")
def test_hosted_replay_matches_every_local_event_and_delay(monkeypatch):
    turn = {
        "input_text": "Replay fixture", "bwo_before": "before", "bwo_after": "after",
        "response": "Final response", "draft_response": "First draft", "justification": "A reason",
        "fired": [["Compensator", "analysis", "always-on"], ["Shame", "modulation", "selected"]],
        "machine_outputs": {"Compensator": "ANALYSIS\nOne, two, three.\nPRODUCT\nA small change.",
                            "Shame": "ANALYSIS\nA café — with \"quotes\".\nPRODUCT\nA pause."},
        "groups": [{"members": ["Compensator", "Shame"], "mode": "conjunctive",
                    "thinking": "Two outputs — one group.", "result": "Keep the pause."}],
        "calls": [{"label": "interior-editor", "output": {
            "thinking": "Quoted \"words\" and an emoji 🙂", "bwo": "after", "response": "First draft",
        }}],
        "edits": [{"change": "A detail", "driven_by": ["Shame"]}],
        "fit_reviews": [
            {"round": 1, "response": "First reply", "fits": False, "explanation": "Too much."},
            {"round": 2, "response": "Final response", "fits": True, "explanation": "Fits."},
        ],
    }
    persona = load_persona(_default_persona())
    assert capture_hosted(turn, persona) == capture_local(turn, persona, monkeypatch)
