"""Event bus for the live frontend.

The pipeline and LLM layer emit structured events (turn/stage lifecycle,
per-call streaming deltas) into a process-wide sink. When no sink is set —
normal CLI runs — emission is a no-op. The live server installs a sink that
fans events out to browser SSE connections.

A plain module global (not a contextvar): one live session per process, and
events must cross the server-thread / asyncio-loop boundary.
"""

from __future__ import annotations

import threading
import time
from typing import Any, Callable

_sink: Callable[[dict], None] | None = None
_lock = threading.Lock()


def set_sink(fn: Callable[[dict], None] | None) -> None:
    global _sink
    with _lock:
        _sink = fn


def enabled() -> bool:
    return _sink is not None


def emit(type_: str, **data: Any) -> None:
    fn = _sink
    if fn is None:
        return
    try:
        fn({"type": type_, "ts": round(time.time(), 3), **data})
    except Exception:
        pass  # the visualization must never break a run
