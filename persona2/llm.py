"""The single LLM chokepoint.

Every model call in the system goes through `call_llm`. That buys us, in one
place: tiered models, structured output (Pydantic via tool-forcing), prompt
caching on the shared system prefix, retries, and — most importantly —
automatic capture of every call into the current turn's firing trace.

The trace capture uses a contextvar so the pipeline can wrap a turn with
`capture()` and collect every nested call without threading a logger through
every function.
"""

from __future__ import annotations

import asyncio
import contextvars
import json
import os
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any, TypeVar

from anthropic import (
    APIConnectionError,
    APIStatusError,
    AsyncAnthropic,
    RateLimitError,
)
from pydantic import BaseModel
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from . import events

_client: AsyncAnthropic | None = None


def client() -> AsyncAnthropic:
    """Lazily-created shared async client (reads ANTHROPIC_API_KEY from env)."""
    global _client
    if _client is None:
        _client = AsyncAnthropic()
    return _client


# --- trace capture -----------------------------------------------------------


@dataclass
class LLMCall:
    """One model call, captured for the firing trace."""

    stage: str
    label: str
    model: str
    system: str
    user: str
    output: Any
    input_tokens: int = 0
    output_tokens: int = 0
    cache_read_tokens: int = 0
    latency_s: float = 0.0


_calls: contextvars.ContextVar[list[LLMCall] | None] = contextvars.ContextVar(
    "_calls", default=None
)


@contextmanager
def capture():
    """Collect every `call_llm` made inside this block into a fresh list."""
    calls: list[LLMCall] = []
    token = _calls.set(calls)
    try:
        yield calls
    finally:
        _calls.reset(token)


def _record(call: LLMCall) -> None:
    calls = _calls.get()
    if calls is not None:
        calls.append(call)


# --- the call ----------------------------------------------------------------

T = TypeVar("T", bound=BaseModel)

_RETRYABLE = (RateLimitError, APIConnectionError, APIStatusError)

# Some models (Opus 4.8+, the Claude 5 family) reject a non-default
# `temperature` with a 400 — omit the param entirely for them.
_NO_TEMPERATURE = ("claude-opus-4-8", "claude-opus-5", "claude-sonnet-5")

# Models that run adaptive thinking when `thinking` is omitted. Our calls use
# small max_tokens budgets that cap thinking + text together, so thinking
# would eat the budget and truncate the actual output — disable it explicitly
# (accepted on these models; NOT on claude-fable-5, which rejects disabled).
_DISABLE_THINKING = ("claude-opus-5", "claude-sonnet-5")


def _supports_temperature(model: str) -> bool:
    return not any(model.startswith(p) for p in _NO_TEMPERATURE)


def _needs_thinking_disabled(model: str) -> bool:
    return any(model.startswith(p) for p in _DISABLE_THINKING)


@retry(
    retry=retry_if_exception_type(_RETRYABLE),
    wait=wait_exponential_jitter(initial=1, max=30),
    stop=stop_after_attempt(5),
    reraise=True,
)
async def _create(**kwargs):
    return await client().messages.create(**kwargs)


@retry(
    retry=retry_if_exception_type(_RETRYABLE),
    wait=wait_exponential_jitter(initial=1, max=30),
    stop=stop_after_attempt(5),
    reraise=True,
)
async def _create_streaming(call_key: str, **kwargs):
    """SDK call with live deltas emitted to the event bus.

    Text deltas stream text; tool-forced (schema) calls stream the tool
    input's partial JSON — the frontend extracts fields incrementally.
    """
    async with client().messages.stream(**kwargs) as s:
        async for event in s:
            if getattr(event, "type", "") == "content_block_delta":
                d = event.delta
                chunk = getattr(d, "text", None) or getattr(d, "partial_json", None)
                if chunk:
                    events.emit("call_delta", id=call_key, text=chunk)
        return await s.get_final_message()


# --- claude-CLI backend (runs on the user's Claude subscription) -------------
#
# Set PERSONA2_CLAUDE_CLI=1 to route every call through `claude -p` instead of
# the SDK. Same prompts, same trace capture; the CLI inherits the user's
# Claude login, so usage bills to the subscription, not API credits.
# Structured outputs are enforced by instruction + pydantic validation with
# one retry (the CLI has no tool-forcing).

_SCHEMA_INSTR = """

---
Respond with ONLY a single JSON object — no prose, no code fences — that \
validates against this JSON Schema:
{schema}"""


def _extract_json(text: str) -> str:
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else t
        t = t.rsplit("```", 1)[0]
    if not t.lstrip().startswith("{"):
        s, e = t.find("{"), t.rfind("}")
        if s != -1 and e > s:
            t = t[s : e + 1]
    return t.strip()


def _cli_env() -> dict:
    return {
        k: v
        for k, v in os.environ.items()
        if k not in {"ANTHROPIC_API_KEY", "CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT"}
    }


async def _cli_once(
    *, model: str, system: str, user: str, call_key: str | None = None
) -> tuple[str, dict]:
    """One `claude -p` invocation. Returns (result_text, usage_dict).

    With an event sink installed and a call_key given, runs in stream-json
    mode and emits live text deltas; otherwise a single json result.
    """
    if events.enabled() and call_key is not None:
        return await _cli_once_streaming(
            model=model, system=system, user=user, call_key=call_key
        )
    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", user,
        "--system-prompt", system,
        "--model", model,
        "--output-format", "json",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_cli_env(),
    )
    out, err = await proc.communicate()
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude CLI failed (rc={proc.returncode}): {err.decode()[:500]}"
        )
    data = json.loads(out.decode())
    if data.get("is_error"):
        raise RuntimeError(f"claude CLI error result: {data.get('result', '')[:500]}")
    return data.get("result", ""), data.get("usage") or {}


async def _cli_once_streaming(
    *, model: str, system: str, user: str, call_key: str
) -> tuple[str, dict]:
    """`claude -p` in stream-json mode, emitting call_delta events live."""
    proc = await asyncio.create_subprocess_exec(
        "claude", "-p", user,
        "--system-prompt", system,
        "--model", model,
        "--output-format", "stream-json",
        "--include-partial-messages",
        "--verbose",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_cli_env(),
    )
    assert proc.stdout is not None and proc.stderr is not None
    stderr_task = asyncio.create_task(proc.stderr.read())
    parts: list[str] = []
    final_text = ""
    usage: dict = {}
    is_error = False
    async for raw in proc.stdout:
        line = raw.decode(errors="replace").strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        t = obj.get("type")
        if t == "stream_event":
            ev = obj.get("event") or {}
            if ev.get("type") == "content_block_delta":
                d = ev.get("delta") or {}
                chunk = d.get("text") or d.get("partial_json") or ""
                if chunk:
                    parts.append(chunk)
                    events.emit("call_delta", id=call_key, text=chunk)
        elif t == "result":
            final_text = obj.get("result", "")
            usage = obj.get("usage") or {}
            is_error = bool(obj.get("is_error"))
    err = await stderr_task
    await proc.wait()
    if proc.returncode != 0:
        raise RuntimeError(
            f"claude CLI failed (rc={proc.returncode}): {err.decode()[:500]}"
        )
    if is_error:
        raise RuntimeError(f"claude CLI error result: {final_text[:500]}")
    return final_text or "".join(parts), usage


async def _cli_call(
    *, model: str, system: str, user: str, schema: type[T] | None,
    call_key: str | None = None
) -> tuple[Any, Any, dict]:
    """CLI-backed call. Returns (result, output_repr, usage_dict)."""
    if schema is None:
        text, usage = await _cli_once(
            model=model, system=system, user=user, call_key=call_key
        )
        return text.strip(), text.strip(), usage

    schema_json = json.dumps(schema.model_json_schema())
    prompt = user + _SCHEMA_INSTR.format(schema=schema_json)
    text, usage = await _cli_once(
        model=model, system=system, user=prompt, call_key=call_key
    )
    try:
        # strict=False: long prose fields routinely carry literal newlines,
        # which strict JSON rejects as control characters.
        parsed = json.loads(_extract_json(text), strict=False)
        return schema.model_validate(parsed), parsed, usage
    except Exception as exc:  # one correction retry
        retry_prompt = (
            prompt
            + f"\n\nYour previous output was:\n{text[:2000]}\n\nIt failed "
            f"validation: {exc}. Output ONLY the corrected JSON object."
        )
        text2, usage2 = await _cli_once(
            model=model, system=system, user=retry_prompt, call_key=call_key
        )
        parsed = json.loads(_extract_json(text2), strict=False)
        for k in ("input_tokens", "output_tokens", "cache_read_input_tokens"):
            usage[k] = (usage.get(k) or 0) + (usage2.get(k) or 0)
        return schema.model_validate(parsed), parsed, usage


async def call_llm(
    *,
    stage: str,
    label: str,
    model: str,
    system: str,
    user: str,
    schema: type[T] | None = None,
    max_tokens: int = 1024,
    temperature: float = 1.0,
    cache: bool = True,
):
    """Make one model call.

    If `schema` is given, the model is forced to emit an instance of that
    Pydantic model (returned validated). Otherwise the joined text is returned.
    `stage`/`label` tag the call in the trace.

    With PERSONA2_CLAUDE_CLI=1 the call routes through the `claude` CLI
    (subscription-billed) instead of the SDK; `max_tokens`, `temperature`,
    and `cache` do not apply on that path.
    """
    call_key = f"{stage}/{label}"
    events.emit(
        "call_started", id=call_key, stage=stage, label=label, model=model,
        schema=bool(schema),
    )

    if os.environ.get("PERSONA2_CLAUDE_CLI"):
        t0 = time.monotonic()
        result, output_repr, usage_d = await _cli_call(
            model=model, system=system, user=user, schema=schema,
            call_key=call_key,
        )
        _record(
            LLMCall(
                stage=stage,
                label=label,
                model=model,
                system=system,
                user=user,
                output=output_repr,
                input_tokens=usage_d.get("input_tokens") or 0,
                output_tokens=usage_d.get("output_tokens") or 0,
                cache_read_tokens=usage_d.get("cache_read_input_tokens") or 0,
                latency_s=round(time.monotonic() - t0, 2),
            )
        )
        events.emit("call_done", id=call_key, output=output_repr)
        return result

    system_param: Any
    if cache:
        system_param = [
            {"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}
        ]
    else:
        system_param = system

    kwargs: dict[str, Any] = dict(
        model=model,
        max_tokens=max_tokens,
        system=system_param,
        messages=[{"role": "user", "content": user}],
    )
    if temperature is not None and _supports_temperature(model):
        kwargs["temperature"] = temperature
    if _needs_thinking_disabled(model):
        kwargs["thinking"] = {"type": "disabled"}

    if schema is not None:
        tool_name = "emit_" + schema.__name__.lower()
        kwargs["tools"] = [
            {
                "name": tool_name,
                "description": (schema.__doc__ or "Emit the structured result.").strip(),
                "input_schema": schema.model_json_schema(),
            }
        ]
        kwargs["tool_choice"] = {"type": "tool", "name": tool_name}

    t0 = time.monotonic()
    if events.enabled():
        resp = await _create_streaming(call_key, **kwargs)
    else:
        resp = await _create(**kwargs)
    latency = time.monotonic() - t0

    if schema is not None:
        block = next(b for b in resp.content if b.type == "tool_use")
        result: Any = schema.model_validate(block.input)
        output_repr: Any = block.input
    else:
        result = "".join(b.text for b in resp.content if b.type == "text").strip()
        output_repr = result

    usage = resp.usage
    _record(
        LLMCall(
            stage=stage,
            label=label,
            model=model,
            system=system,
            user=user,
            output=output_repr,
            input_tokens=getattr(usage, "input_tokens", 0) or 0,
            output_tokens=getattr(usage, "output_tokens", 0) or 0,
            cache_read_tokens=getattr(usage, "cache_read_input_tokens", 0) or 0,
            latency_s=round(latency, 2),
        )
    )
    events.emit("call_done", id=call_key, output=output_repr)
    return result
