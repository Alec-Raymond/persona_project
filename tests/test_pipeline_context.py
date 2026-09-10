"""Reply revisions keep the synthesis inputs; the fit reader stays independent."""

from types import SimpleNamespace

import pytest

from persona2 import pipeline
from persona2.cli import _default_persona
from persona2.config import Config
from persona2.models import BwoEdit, FitCheck, GroupSynthesis
from persona2.persona import load_persona
from persona2.prompts import format_synthesis_context
from persona2.runtime import Runtime


@pytest.mark.asyncio
@pytest.mark.parametrize("failed_rounds", [0, 2])
async def test_every_revision_retains_all_syntheses_without_exposing_them_to_fit_reader(monkeypatch, failed_rounds):
    captured = {}
    persona = load_persona(_default_persona())

    async def select(**kwargs):
        return SimpleNamespace(fired=[], relevance=None, random_picks=[], scores={})

    async def synthesize(**kwargs):
        members = [machine.name for machine in kwargs["group"]]
        for product in kwargs["out_by_name"].values():
            assert "PRIVATE_MACHINE_ANALYSIS" not in product
        return GroupSynthesis(
            mode="disjunctive", thinking=f"SYNTHESIS_ANALYSIS_{members[0]}",
            result=(f"SYNTHESIS_RESULT_{members[0]} " * 200) + "KEEP_THE_END",
        )

    async def call(**kwargs):
        label = kwargs["label"]
        captured[label] = kwargs["user"]
        if kwargs["stage"] == "machine":
            return f"ANALYSIS\nPRIVATE_MACHINE_ANALYSIS\nPRODUCT\nMeaning from {label}"
        if label == "interior-editor":
            return BwoEdit(thinking="PRIVATE_EDITOR_ANALYSIS", bwo="UPDATED_STATE",
                           response="Initial reply", justification="PRIVATE_EDIT_JUSTIFICATION")
        if label.startswith("fit-check-"):
            round_number = int(label.rsplit("-", 1)[1])
            return FitCheck(explanation=f"Feedback {round_number}", fits=round_number > failed_rounds)
        if label.startswith("redraft-"):
            return f"Rewritten reply {label}"
        if label.startswith("armor"):
            return f"Candidate {label}"
        raise AssertionError(f"Unexpected call: {label}")

    monkeypatch.setattr(pipeline, "select", select)
    monkeypatch.setattr(pipeline, "partition", lambda machines, *_: [machines[:2], machines[2:]])
    monkeypatch.setattr(pipeline, "synthesize_group", synthesize)
    monkeypatch.setattr(pipeline, "call_llm", call)
    runtime = Runtime.new(persona, Config(backend="codex"))
    trace = await runtime.turn("THE_OTHER_PERSONS_MESSAGE")
    context = format_synthesis_context(trace.groups)
    writers = ["interior-editor", "armor"]
    for round_number in range(1, failed_rounds + 1):
        writers.extend([f"redraft-{round_number}", f"armor-{round_number + 1}"])
        assert f"Feedback {round_number}" in captured[f"redraft-{round_number}"]
        assert f"Rewritten reply redraft-{round_number}" in captured[f"armor-{round_number + 1}"]
    for label in writers:
        assert context in captured[label], label
        for group in trace.groups:
            assert group.thinking in captured[label]
            assert group.result in captured[label]
            assert ", ".join(group.members) in captured[label]
        assert "THE_OTHER_PERSONS_MESSAGE" in captured[label]
        if label != "interior-editor":
            assert "UPDATED_STATE" in captured[label]
            assert "PRIVATE_EDITOR_ANALYSIS" not in captured[label]
            assert "PRIVATE_EDIT_JUSTIFICATION" not in captured[label]
    for round_number in range(1, failed_rounds + 2):
        reader = captured[f"fit-check-{round_number}"]
        assert "THE_OTHER_PERSONS_MESSAGE" in reader
        assert "Candidate armor" in reader
        assert "SYNTHESIS_" not in reader
        assert "UPDATED_STATE" not in reader
    assert len(trace.fit_reviews) == failed_rounds + 1
    assert runtime.state.bwo.text == "UPDATED_STATE"
    assert runtime.state.history[-1]["content"] == trace.response
