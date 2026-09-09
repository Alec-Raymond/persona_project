"""The wire audit must reject hidden instructions and nested tool definitions."""

import pytest

from persona2.codex import strict_schema
from persona2.models import FitCheck
from scripts.audit_codex_prompt import SYSTEM, USER, inspect_request


@pytest.fixture
def request_body():
    return {"model": "gpt-6-astra", "input": [
        {"type": "additional_tools", "role": "developer", "tools": [], "id": "ignored"},
        {"type": "message", "role": "developer", "content": [{"type": "input_text", "text": SYSTEM}]},
        {"type": "message", "role": "user", "content": [{"type": "input_text", "text": USER}]},
    ]}


def test_accepts_only_caller_messages_and_empty_tool_envelope(request_body):
    assert inspect_request(request_body)["clean"]


@pytest.mark.parametrize("contamination", ["global", "tools", "top_level_tools", "instructions", "model", "unknown"])
def test_rejects_extra_context_and_tools(request_body, contamination):
    if contamination == "global":
        request_body["input"].insert(1, {"type": "message", "role": "user", "content": "AGENTS.md"})
    elif contamination == "tools":
        request_body["input"][0]["tools"] = [{"type": "namespace", "name": "functions", "tools": [{"name": "exec"}]}]
    elif contamination == "top_level_tools":
        request_body["tools"] = [{"type": "function", "name": "apply_patch"}]
    elif contamination == "instructions":
        request_body["instructions"] = "You are a coding agent."
    elif contamination == "model":
        request_body["model"] = "other-model"
    else:
        request_body["input"].append({"type": "unknown", "content": "extra context"})
    assert not inspect_request(request_body)["clean"]


def test_structured_audit_requires_exact_schema(request_body):
    assert not inspect_request(request_body, FitCheck)["clean"]
    request_body["text"] = {"format": {"type": "json_schema", "strict": True,
                                       "schema": strict_schema(FitCheck.model_json_schema())}}
    assert inspect_request(request_body, FitCheck)["clean"]
    request_body["text"]["format"]["strict"] = False
    assert not inspect_request(request_body, FitCheck)["clean"]
