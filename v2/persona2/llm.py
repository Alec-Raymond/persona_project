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

import contextvars
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

# Some models (Opus 4.8+) deprecate the `temperature` param and 400 if it's sent.
_NO_TEMPERATURE = ("claude-opus-4-8",)


def _supports_temperature(model: str) -> bool:
    return not any(model.startswith(p) for p in _NO_TEMPERATURE)


@retry(
    retry=retry_if_exception_type(_RETRYABLE),
    wait=wait_exponential_jitter(initial=1, max=30),
    stop=stop_after_attempt(5),
    reraise=True,
)
async def _create(**kwargs):
    return await client().messages.create(**kwargs)


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
    """
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
    return result
