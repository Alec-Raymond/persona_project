"""Backend routing, CLI configuration, and subscription transport failures."""

import argparse
import asyncio
import json
from pathlib import Path
from unittest.mock import AsyncMock

import pytest

from persona2 import codex, events, llm
from persona2.cli import _config_from_args, _model_arguments
from persona2.config import ASTRA, MID, Config
from persona2.models import BwoEdit, FitCheck
from persona2.machine import Machine
from persona2.persona import load_persona
from persona2.runtime import Runtime
from persona2.selection import relevance_schema, select
from persona2.trace import TurnTrace


@pytest.fixture(autouse=True)
def clean_backend_environment(monkeypatch):
    monkeypatch.delenv("PERSONA2_BACKEND", raising=False)
    monkeypatch.delenv("PERSONA2_CLAUDE_CLI", raising=False)
    events.set_sink(None)
    yield
    events.set_sink(None)


def cli_config(*options):
    parser = argparse.ArgumentParser()
    _model_arguments(parser)
    return _config_from_args(parser.parse_args(options))


@pytest.mark.parametrize("backend,expected", [("anthropic", MID), ("claude", MID), ("codex", ASTRA)])
def test_backend_defaults_do_not_use_haiku(backend, expected):
    cfg = cli_config("--backend", backend)
    assert (cfg.model_selector, cfg.model_machine, cfg.model_synth, cfg.model_final) == (expected,) * 4


def test_explicit_models_and_final_override():
    cfg = cli_config("--backend", "codex", "--model", "gpt-6-astra", "--final", "gpt-5.6-sol")
    assert cfg.model_selector == ASTRA
    assert cfg.model_final == "gpt-5.6-sol"
    assert cli_config("--backend", "anthropic", "--all", "haiku").model_selector.startswith("claude-haiku")
    assert Config(backend="codex", model_selector="gpt-5.6-sol").model_selector == "gpt-5.6-sol"


def test_environment_backend_and_legacy_setting(monkeypatch):
    monkeypatch.setenv("PERSONA2_CLAUDE_CLI", "1")
    assert cli_config().backend == "claude"
    monkeypatch.setenv("PERSONA2_BACKEND", "codex")
    assert cli_config().model_final == ASTRA
    assert cli_config("--backend", "anthropic").backend == "anthropic"


@pytest.mark.parametrize("options", [
    ("--backend", "codex", "--all", "haiku"),
    ("--backend", "anthropic", "--model", "astra"),
    ("--backend", "claude", "--final", "gpt-6-astra"),
    ("--concurrency", "0"),
    ("--call-timeout", "0"),
])
def test_invalid_configuration_fails_before_calls(options):
    with pytest.raises(ValueError):
        cli_config(*options)


def test_structured_output_closes_nested_objects_and_preserves_original():
    original = BwoEdit.model_json_schema()
    converted = codex.strict_schema(original)
    assert "default" in original["properties"]["justification"]
    assert "default" not in converted["properties"]["justification"]
    assert converted["required"] == list(converted["properties"])
    assert converted["additionalProperties"] is False
    assert converted["$defs"]["EditNote"]["additionalProperties"] is False


@pytest.mark.asyncio
async def test_relevance_votes_use_bare_roster_names(monkeypatch):
    import random

    pool = [Machine(name=name, category="affect", shape="modulation", sensitivity="s", flow="f")
            for name in ("Hope", "Tristitia", "Cupiditas")]
    schema = relevance_schema(pool)
    # This is the malformed vote returned in the first live Astra run.
    with pytest.raises(ValueError):
        schema.model_validate({"picks": [{"name": "Hope [affect/modulation]", "score": 0.9, "reason": "r"}]})

    async def vote(**kwargs):
        allowed = kwargs["schema"].model_json_schema()["$defs"]["RosterMachinePick"]["properties"]["name"]["enum"]
        assert allowed == ["Hope", "Tristitia", "Cupiditas"]
        return kwargs["schema"].model_validate({"picks": [{"name": "Hope", "score": 0.9, "reason": "a specific concern"}]})

    monkeypatch.setattr("persona2.selection.call_llm", vote)
    result = await select(
        cfg=Config(backend="codex", random_k=0), pool=pool,
        bwo_text="state", input_text="hello", history="", rng=random.Random(7),
    )
    assert [(machine.name, reason) for machine, reason in result.fired] == [("Hope", "a specific concern")]
    assert result.scores["Hope"] > 0


def event_output(text="hello"):
    return "\n".join(json.dumps(event) for event in [
        {"type": "thread.started", "thread_id": "test"},
        {"type": "item.completed", "item": {"type": "agent_message", "text": text}},
        {"type": "turn.completed", "usage": {"input_tokens": 100, "output_tokens": 8, "cached_input_tokens": 60}},
    ]).encode()


@pytest.mark.parametrize("payload,message", [
    ({"type": "turn.failed", "error": {"message": "Model unavailable"}}, "Model unavailable"),
    ({"type": "turn.completed", "usage": {}}, "empty final message"),
])
def test_incomplete_or_empty_codex_result_is_an_error(payload, message):
    with pytest.raises(RuntimeError, match=message):
        codex.parse_events(json.dumps(payload))


@pytest.mark.asyncio
async def test_subscription_call_uses_stdin_and_native_schema(monkeypatch):
    monkeypatch.setattr(codex.shutil, "which", lambda _: "/usr/bin/codex")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key-do-not-forward")
    monkeypatch.setenv("CODEX_API_KEY", "test-key-do-not-forward")
    reply = {"explanation": "Fits the setting.", "fits": True}
    process = AsyncMock()
    process.returncode = 0
    process.communicate.return_value = (event_output(json.dumps(reply)), b"")
    paths = []

    async def launch(*command, **kwargs):
        assert "--ignore-user-config" in command and "--ephemeral" in command
        assert command[command.index("--sandbox") + 1] == "read-only"
        assert 'forced_login_method="chatgpt"' in command
        assert "--dangerously-bypass-approvals-and-sandbox" not in command
        assert "OPENAI_API_KEY" not in kwargs["env"] and "CODEX_API_KEY" not in kwargs["env"]
        assert "stage input" not in command
        schema_path = Path(command[command.index("--output-schema") + 1])
        paths.append(schema_path.parent)
        assert json.loads(schema_path.read_text())["additionalProperties"] is False
        assert (schema_path.parent / "instructions.txt").read_text() == "stage instructions"
        return process

    monkeypatch.setattr(codex.asyncio, "create_subprocess_exec", launch)
    result, output, usage = await codex.generate(
        model=ASTRA, system="stage instructions", user="stage input", schema=FitCheck,
    )
    assert result.fits and output == reply
    assert usage == {"input_tokens": 100, "output_tokens": 8, "cache_read_input_tokens": 60}
    process.communicate.assert_awaited_once_with(b"stage input")
    assert not paths[0].exists()


@pytest.mark.asyncio
async def test_codex_process_error_reports_service_failure(monkeypatch):
    monkeypatch.setattr(codex.shutil, "which", lambda _: "/usr/bin/codex")
    process = AsyncMock()
    process.returncode = 1
    process.communicate.return_value = (json.dumps({"type": "error", "message": "Usage limit reached"}).encode(), b"")
    monkeypatch.setattr(codex.asyncio, "create_subprocess_exec", AsyncMock(return_value=process))
    with pytest.raises(RuntimeError, match="Usage limit reached"):
        await codex.generate(model=ASTRA, system="s", user="u", schema=None)


@pytest.mark.asyncio
async def test_codex_timeout_kills_and_reaps_process(monkeypatch):
    from unittest.mock import Mock

    monkeypatch.setattr(codex.shutil, "which", lambda _: "/usr/bin/codex")
    process = AsyncMock()
    process.returncode = None
    process.kill = Mock()

    async def hanging_call(_):
        await asyncio.sleep(60)

    process.communicate.side_effect = hanging_call
    monkeypatch.setattr(codex.asyncio, "create_subprocess_exec", AsyncMock(return_value=process))
    with pytest.raises(RuntimeError, match="exceeded"):
        await codex.generate(model=ASTRA, system="s", user="u", schema=None, timeout=0.01)
    process.kill.assert_called_once()
    process.wait.assert_awaited_once()


@pytest.mark.asyncio
async def test_cancelled_codex_call_kills_and_reaps_process(monkeypatch):
    from unittest.mock import Mock

    monkeypatch.setattr(codex.shutil, "which", lambda _: "/usr/bin/codex")
    started = asyncio.Event()
    process = AsyncMock()
    process.returncode = None
    process.kill = Mock()

    async def hanging_call(_):
        started.set()
        await asyncio.sleep(60)

    process.communicate.side_effect = hanging_call
    monkeypatch.setattr(codex.asyncio, "create_subprocess_exec", AsyncMock(return_value=process))
    task = asyncio.create_task(codex.generate(model=ASTRA, system="s", user="u", schema=None))
    await started.wait()
    task.cancel()
    with pytest.raises(asyncio.CancelledError):
        await task
    process.kill.assert_called_once()
    process.wait.assert_awaited_once()


@pytest.mark.asyncio
async def test_missing_codex_cli_explains_login_setup(monkeypatch):
    monkeypatch.setattr(codex.shutil, "which", lambda _: None)
    with pytest.raises(RuntimeError, match="Install it and run `codex login`"):
        await codex.generate(model=ASTRA, system="s", user="u", schema=None)


@pytest.mark.asyncio
async def test_codex_failure_does_not_fall_back_to_anthropic(monkeypatch):
    monkeypatch.setattr(codex, "generate", AsyncMock(side_effect=RuntimeError("not signed in")))
    anthropic_call = AsyncMock()
    monkeypatch.setattr(llm, "_create", anthropic_call)
    with llm.model_backend(Config(backend="codex")):
        with pytest.raises(RuntimeError, match="not signed in"):
            await llm.call_llm(stage="machine", label="m", model=ASTRA, system="s", user="u")
    anthropic_call.assert_not_awaited()


@pytest.mark.asyncio
async def test_concurrent_runtimes_keep_backend_and_trace_separate(monkeypatch):
    async def fake_codex(**kwargs):
        await asyncio.sleep(0)
        return "codex reply", "codex reply", {"input_tokens": 4, "output_tokens": 2}

    async def fake_claude(**kwargs):
        await asyncio.sleep(0)
        return "claude reply", "claude reply", {"input_tokens": 3, "output_tokens": 1}

    async def fake_turn(**kwargs):
        with llm.capture() as calls:
            response = await llm.call_llm(
                stage="machine", label="test", model=kwargs["cfg"].model_final, system="s", user="u",
            )
        return TurnTrace(input_text=kwargs["input_text"], response=response, bwo_before="a", bwo_after="b", calls=calls)

    monkeypatch.setattr(codex, "generate", fake_codex)
    monkeypatch.setattr(llm, "_cli_call", fake_claude)
    monkeypatch.setattr("persona2.runtime.run_turn", fake_turn)
    persona = load_persona(Path(__file__).resolve().parent.parent / "personas/testbed")
    captured = []
    events.set_sink(captured.append)
    runtimes = [Runtime.new(persona, Config(backend=name)) for name in ("codex", "claude")]
    traces = await asyncio.gather(*(runtime.turn("hello") for runtime in runtimes))
    assert [trace.response for trace in traces] == ["codex reply", "claude reply"]
    assert [trace.calls[0].model for trace in traces] == [ASTRA, MID]
    assert [trace.totals()["input_tokens"] for trace in traces] == [4, 3]
    assert any(event["type"] == "call_delta" and event["text"] == "codex reply" for event in captured)
    assert llm._run_config.get() is None
