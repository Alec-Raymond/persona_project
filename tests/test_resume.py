"""Resume keeps conversation state without generating replacement turns."""

import json

import pytest

from persona2 import events
from persona2.cli import _default_persona
from persona2.config import Config
from persona2.live import Session
from persona2.persona import load_persona
from persona2.runtime import Runtime


def saved_turns():
    return [{"input_text": f"Question {index}", "response": f"Reply {index}",
             "bwo_before": f"State {index}", "bwo_after": f"State {index + 1}",
             "fired": [["Compensator", "analysis", "always-on"]],
             "groups": [{"members": ["Compensator"], "mode": "disjunctive",
                         "thinking": "Analysis", "result": "Result"}],
             "machine_outputs": {"Compensator": "ANALYSIS\nAnalysis\nPRODUCT\nProduct"}}
            for index in range(2)]


def test_resume_restores_state_history_firing_counts_and_modes():
    runtime = Runtime.resume(load_persona(_default_persona()), saved_turns(), Config(backend="codex"))
    assert runtime.state.bwo.text == "State 2"
    assert runtime.state.fire_count == {"Compensator": 2}
    assert runtime.state.mode_history == ["disjunctive"]
    assert runtime.state.history == [
        {"role": "user", "content": "Question 0"}, {"role": "persona", "content": "Reply 0"},
        {"role": "user", "content": "Question 1"}, {"role": "persona", "content": "Reply 1"},
    ]
    assert "[the other person] Question 1" in runtime.state.history_text(12)


@pytest.mark.parametrize("failure", ["empty", "missing_text", "discontinuous"])
def test_resume_rejects_incomplete_conversations(failure):
    turns = saved_turns()
    if failure == "empty":
        turns = []
    elif failure == "missing_text":
        del turns[1]["response"]
    else:
        turns[1]["bwo_before"] = "Another conversation"
    with pytest.raises(ValueError):
        Runtime.resume(load_persona(_default_persona()), turns)


def test_live_resume_restores_replay_and_save_position_without_sleeping_or_model_calls(tmp_path, monkeypatch):
    for index, turn in enumerate(saved_turns(), 1):
        (tmp_path / f"turn-{index:03d}.json").write_text(json.dumps(turn))
    def forbidden(*args, **kwargs):
        raise AssertionError("Resuming must not generate outputs or wait through a replay")
    monkeypatch.setattr("persona2.live.time.sleep", forbidden)
    monkeypatch.setattr("persona2.pipeline.call_llm", forbidden)
    session = Session(str(_default_persona()), Config(backend="codex"), resume_dir=str(tmp_path))
    try:
        assert session.turn_n == 2
        assert session.save_dir == tmp_path
        assert session.rt.state.bwo.text == "State 2"
        assert not session.busy
        history = session.hub._history
        assert history[0] == {"type": "session_reset"}
        assert [event["response"] for event in history if event["type"] == "turn_done"] == ["Reply 0", "Reply 1"]
        assert session.reset()
        assert session.turn_n == 0
        assert session.rt.state.history == []
        assert session.save_dir != tmp_path
    finally:
        events.set_sink(None)
        session.loop.call_soon_threadsafe(session.loop.stop)


def test_live_resume_rejects_a_missing_turn_file(tmp_path):
    (tmp_path / "turn-002.json").write_text(json.dumps(saved_turns()[1]))
    with pytest.raises(ValueError, match="consecutive"):
        Session(str(_default_persona()), Config(backend="codex"), resume_dir=str(tmp_path))
