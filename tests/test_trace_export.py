import json

import pytest

from persona2.trace_export import export_run


def write_turns(directory, models=("gpt-6-astra", "gpt-6-astra")):
    for index, model in enumerate(models):
        turn = {"input_text": f"message {index}", "response": f"reply {index}",
                "bwo_before": str(index), "bwo_after": str(index + 1),
                "calls": [{"model": model}]}
        (directory / f"turn-{index + 1:03d}.json").write_text(json.dumps(turn))


def test_export_keeps_full_conversation_and_exact_model(tmp_path):
    write_turns(tmp_path)
    result = export_run(tmp_path, title="My conversation")
    assert result["title"] == "My conversation"
    assert len(result["turns"]) == 2
    assert result["turns"][1]["input_text"] == "message 1"


def test_export_rejects_single_turn(tmp_path):
    write_turns(tmp_path, models=("gpt-6-astra",))
    with pytest.raises(ValueError, match="at least two"):
        export_run(tmp_path)


def test_export_rejects_mixed_models(tmp_path):
    write_turns(tmp_path, models=("gpt-6-astra", "claude-sonnet-5"))
    with pytest.raises(ValueError, match="Turn 2 must use"):
        export_run(tmp_path)


def test_export_rejects_unrelated_turns(tmp_path):
    write_turns(tmp_path)
    path = tmp_path / "turn-002.json"
    turn = json.loads(path.read_text())
    turn["bwo_before"] = "another conversation"
    path.write_text(json.dumps(turn))
    with pytest.raises(ValueError, match="does not continue"):
        export_run(tmp_path)
