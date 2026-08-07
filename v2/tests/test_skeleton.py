"""Non-API tests for the deterministic skeleton pieces.

The full pipeline wiring is validated by a real one-turn run (it needs the API
and producing real output is the point). These cover everything that doesn't."""

from __future__ import annotations

import random
from pathlib import Path

import pytest

from persona2.config import Config
from persona2.grouping import allowed_modes, partition
from persona2.machine import Machine, load_machines
from persona2.models import BwoEdit, GroupSynthesis, RelevanceVotes
from persona2.persona import load_persona
from persona2.trace import GroupTrace, TurnTrace

PERSONA = Path(__file__).resolve().parent.parent / "personas" / "testbed"


def test_persona_loads():
    p = load_persona(PERSONA)
    assert len(p.machines) >= 8
    assert len(p.always_on) == 3
    assert {m.name for m in p.always_on} == {"Compensator", "Situation", "Pulsation"}
    assert p.voice_sketch and p.bwo_seed
    # all three shapes represented
    shapes = {m.shape for m in p.machines}
    assert shapes == {"analysis", "proposal", "modulation"}


def test_machine_shape_validation():
    with pytest.raises(ValueError):
        Machine(name="x", category="c", shape="bogus", sensitivity="s", flow="f")


@pytest.mark.parametrize("n", list(range(2, 13)))
def test_partition_no_singletons_and_covers_all(n):
    cfg = Config()
    machines = [
        Machine(name=f"m{i}", category="c", shape="analysis", sensitivity="s", flow="f")
        for i in range(n)
    ]
    groups = partition(machines, cfg, random.Random(0))
    # every machine appears exactly once
    flat = [m.name for g in groups for m in g]
    assert sorted(flat) == sorted(m.name for m in machines)
    # no singleton groups, none larger than max (allow the safety-merge up to max+1)
    for g in groups:
        assert len(g) >= 2
        assert len(g) <= cfg.max_group + 1


def test_allowed_modes_pair_constraint():
    cfg = Config()
    assert "transcendent" in allowed_modes(2, cfg)
    assert "transcendent" not in allowed_modes(3, cfg)
    assert "transcendent" not in allowed_modes(4, cfg)


def test_structured_schemas_build():
    # tool input_schema generation must not blow up
    for model in (RelevanceVotes, GroupSynthesis, BwoEdit):
        schema = model.model_json_schema()
        assert schema["type"] == "object"


def test_trace_roundtrip(tmp_path):
    t = TurnTrace(
        input_text="hi",
        response="hello",
        bwo_before="a",
        bwo_after="b",
        fired=[("Compensator", "analysis", "(always-on)")],
        machine_outputs={"Compensator": "a small flow"},
        groups=[GroupTrace(members=["Compensator"], mode="conjunctive", summaries=[("Compensator", "s")], result="r")],
    )
    p = t.save(tmp_path / "t.json")
    assert p.exists()
    import json

    data = json.loads(p.read_text())
    assert data["response"] == "hello"
    assert data["totals"]["calls"] == 0
    # render must not crash (write to a throwaway console)
    from rich.console import Console

    t.render(Console(file=open(tmp_path / "out.txt", "w"), force_terminal=False))


def test_manifest_machines_have_required_fields():
    machines = load_machines(PERSONA / "manifest.yaml")
    for m in machines:
        assert m.name and m.sensitivity.strip() and m.flow.strip()
