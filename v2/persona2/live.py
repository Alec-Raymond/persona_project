"""The live frontend server.

Stdlib-only: a ThreadingHTTPServer serves the page, an SSE event stream, a
message endpoint, and trace replay. The pipeline runs on an asyncio loop in
a background thread; persona2.events fans its events out to every connected
browser. One conversation per server run.

    python -m persona2.cli live personas/effusive --all sonnet
"""

from __future__ import annotations

import asyncio
import json
import queue
import threading
import time
import webbrowser
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import events
from .config import Config
from .persona import load_persona
from .runtime import Runtime

_ROOT = Path(__file__).resolve().parent.parent  # v2/
_PAGE = _ROOT / "viewer" / "live.html"
_TRACES = _ROOT / "traces"


class Hub:
    """Thread-safe fanout of events to SSE clients, with history replay."""

    def __init__(self) -> None:
        self._clients: list[queue.Queue] = []
        self._history: list[dict] = []
        self._lock = threading.Lock()

    def emit(self, ev: dict) -> None:
        with self._lock:
            self._history.append(ev)
            clients = list(self._clients)
        for q in clients:
            q.put(ev)

    def subscribe(self) -> queue.Queue:
        q: queue.Queue = queue.Queue()
        with self._lock:
            for ev in self._history:
                q.put(ev)
            self._clients.append(q)
        return q

    def unsubscribe(self, q: queue.Queue) -> None:
        with self._lock:
            if q in self._clients:
                self._clients.remove(q)

    def clear(self) -> None:
        with self._lock:
            self._history = []


class Session:
    """The conversation: a Runtime on its own asyncio loop thread."""

    def __init__(self, persona_dir: str, cfg: Config) -> None:
        self.persona_dir = persona_dir
        self.cfg = cfg
        self.persona = load_persona(persona_dir)
        self.hub = Hub()
        self.busy = False
        self.turn_n = 0
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.save_dir = _TRACES / f"{self.persona.name}-live-{stamp}"
        self.loop = asyncio.new_event_loop()
        threading.Thread(target=self.loop.run_forever, daemon=True).start()
        fut = asyncio.run_coroutine_threadsafe(self._make_runtime(), self.loop)
        self.rt = fut.result()
        events.set_sink(self.hub.emit)

    async def _make_runtime(self) -> Runtime:
        return Runtime.new(self.persona, cfg=self.cfg)

    def reset(self) -> bool:
        """Start a fresh conversation: new runtime, new trace dir, clean slate."""
        if self.busy:
            return False
        fut = asyncio.run_coroutine_threadsafe(self._make_runtime(), self.loop)
        self.rt = fut.result()
        self.turn_n = 0
        stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        self.save_dir = _TRACES / f"{self.persona.name}-live-{stamp}"
        self.hub.clear()
        self.hub.emit({"type": "session_reset"})
        return True

    def send_message(self, text: str) -> bool:
        if self.busy:
            return False
        self.busy = True

        async def _run() -> None:
            try:
                trace = await self.rt.turn(text)
                self.turn_n += 1
                path = trace.save(self.save_dir / f"turn-{self.turn_n:03d}.json")
                self.hub.emit({"type": "trace_saved", "path": str(path)})
            except Exception as exc:  # surface errors to the page
                self.hub.emit({"type": "turn_error", "error": str(exc)[:800]})
            finally:
                self.busy = False

        asyncio.run_coroutine_threadsafe(_run(), self.loop)
        return True

    # --- replay ---------------------------------------------------------

    def replay(self, trace_dir: str) -> bool:
        if self.busy:
            return False
        self.busy = True
        threading.Thread(
            target=self._replay_worker, args=(trace_dir,), daemon=True
        ).start()
        return True

    def _sensitivity(self, name: str) -> str:
        for m in self.persona.machines:
            if m.name == name:
                return m.sensitivity.strip()
        return ""

    def _category(self, name: str) -> str:
        for m in self.persona.machines:
            if m.name == name:
                return m.category
        return "?"

    @staticmethod
    def _tokens(text: str) -> list[str]:
        import re
        return re.findall(r"\S+\s*", text)

    def _stream_parallel(
        self, streams: list[tuple[str, str]], words_per_tick: int = 2,
        delay: float = 0.03,
    ) -> None:
        """Type several call streams at once, a few words per tick each —
        replayed machines write in parallel, at reading speed."""
        toks = {cid: self._tokens(t) for cid, t in streams}
        pos = {cid: 0 for cid, _ in streams}
        while True:
            alive = False
            for cid, tk in toks.items():
                p = pos[cid]
                if p >= len(tk):
                    continue
                alive = True
                chunk = "".join(tk[p : p + words_per_tick])
                pos[cid] = p + words_per_tick
                self.hub.emit({"type": "call_delta", "id": cid, "text": chunk})
            if not alive:
                break
            time.sleep(delay)

    def _type_out(self, call_id: str, text: str) -> None:
        self._stream_parallel([(call_id, text)], words_per_tick=3, delay=0.03)

    def _replay_worker(self, trace_dir: str) -> None:
        try:
            d = _TRACES / trace_dir
            for turn_file in sorted(d.glob("turn-*.json")):
                t = json.loads(turn_file.read_text())
                self._replay_turn(t)
        except Exception as exc:
            self.hub.emit({"type": "turn_error", "error": f"replay: {exc}"})
        finally:
            self.busy = False

    def _replay_turn(self, t: dict) -> None:
        emit = self.hub.emit
        emit({"type": "turn_started", "input": t["input_text"],
              "bwo": t["bwo_before"], "replay": True})
        emit({"type": "stage_started", "stage": "selection"})
        time.sleep(0.8)
        emit({"type": "selection_done", "fired": [
            {"name": n, "category": self._category(n),
             "sensitivity": self._sensitivity(n), "resonance": res}
            for n, _shape, res in t.get("fired", [])
        ]})
        time.sleep(0.8)
        emit({"type": "stage_started", "stage": "machines"})
        machine_streams = []
        for name, out in t.get("machine_outputs", {}).items():
            cid = f"machine/{name}"
            emit({"type": "call_started", "id": cid, "stage": "machine",
                  "label": name, "model": "", "schema": False})
            machine_streams.append((cid, out))
        self._stream_parallel(machine_streams)
        for cid, out in machine_streams:
            emit({"type": "call_done", "id": cid, "output": out})
        time.sleep(1.2)  # let the last words land before the regroup
        groups = t.get("groups", [])
        emit({"type": "stage_started", "stage": "synthesis"})
        emit({"type": "groups_assigned",
              "groups": [g.get("members", []) for g in groups]})
        time.sleep(1.0)
        synth_streams = []
        for g in groups:
            cid = f"synthesis/{' + '.join(g.get('members', []))}"
            emit({"type": "call_started", "id": cid, "stage": "synthesis",
                  "label": ' + '.join(g.get('members', [])), "model": "",
                  "schema": True})
            synth_streams.append((cid, json.dumps(
                {"mode": g.get("mode"), "thinking": g.get("thinking", ""),
                 "result": g.get("result", "")})))
        self._stream_parallel(synth_streams)
        for gi, g in enumerate(groups):
            cid = f"synthesis/{' + '.join(g.get('members', []))}"
            emit({"type": "call_done", "id": cid, "output": g})
            emit({"type": "synthesis_done", "group": gi + 1,
                  "members": g.get("members", []), "mode": g.get("mode"),
                  "thinking": g.get("thinking", ""),
                  "result": g.get("result", "")})
        time.sleep(0.8)
        emit({"type": "stage_started", "stage": "editor"})
        ed_out = {}
        for c in t.get("calls", []):
            if c.get("label") == "interior-editor":
                ed_out = c.get("output") or {}
                break
        cid = "final/interior-editor"
        emit({"type": "call_started", "id": cid, "stage": "final",
              "label": "interior-editor", "model": "", "schema": True})
        self._type_out(cid, json.dumps(ed_out) if ed_out else "")
        emit({"type": "call_done", "id": cid, "output": ed_out})
        emit({"type": "editor_done", "bwo": t.get("bwo_after", ""),
              "edits": t.get("edits", []),
              "response": t.get("draft_response", ""),
              "justification": t.get("justification", ""),
              "revised": False})
        time.sleep(0.8)
        emit({"type": "stage_started", "stage": "armor"})
        for r in t.get("fit_reviews", []):
            n = r.get("round", 1)
            cid = "final/armor" if n == 1 else f"final/armor-{n}"
            emit({"type": "call_started", "id": cid, "stage": "final",
                  "label": "armor", "model": "", "schema": False})
            self._type_out(cid, r.get("response", ""))
            emit({"type": "call_done", "id": cid, "output": r.get("response", "")})
            emit({"type": "fit_round", "round": n,
                  "response": r.get("response", ""), "fits": r.get("fits"),
                  "explanation": r.get("explanation", "")})
            time.sleep(0.6)
        time.sleep(0.6)
        emit({"type": "turn_done", "response": t.get("response", ""),
              "bwo_after": t.get("bwo_after", "")})


SESSION: Session | None = None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        pass

    def _json(self, code: int, obj: dict) -> None:
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        assert SESSION is not None
        if self.path in ("/", "/index.html"):
            body = _PAGE.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            q = SESSION.hub.subscribe()
            try:
                while True:
                    try:
                        ev = q.get(timeout=15)
                        payload = f"data: {json.dumps(ev)}\n\n"
                    except queue.Empty:
                        payload = ": keepalive\n\n"
                    self.wfile.write(payload.encode())
                    self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError):
                pass
            finally:
                SESSION.hub.unsubscribe(q)
        elif self.path == "/info":
            self._json(200, {
                "persona": SESSION.persona.name,
                "situation": SESSION.persona.situation,
                "busy": SESSION.busy,
            })
        elif self.path == "/traces":
            dirs = sorted(
                (p.name for p in _TRACES.iterdir() if p.is_dir()), reverse=True
            ) if _TRACES.exists() else []
            self._json(200, {"traces": list(dirs)})
        else:
            self._json(404, {"error": "not found"})

    def do_POST(self) -> None:
        assert SESSION is not None
        n = int(self.headers.get("Content-Length") or 0)
        try:
            data = json.loads(self.rfile.read(n) or b"{}")
        except json.JSONDecodeError:
            self._json(400, {"error": "bad json"})
            return
        if self.path == "/message":
            text = (data.get("text") or "").strip()
            if not text:
                self._json(400, {"error": "empty message"})
            elif SESSION.send_message(text):
                self._json(200, {"ok": True})
            else:
                self._json(409, {"error": "a turn is already running"})
        elif self.path == "/reset":
            if SESSION.reset():
                self._json(200, {"ok": True})
            else:
                self._json(409, {"error": "busy"})
        elif self.path == "/replay":
            name = data.get("dir") or ""
            if SESSION.replay(name):
                self._json(200, {"ok": True})
            else:
                self._json(409, {"error": "busy"})
        else:
            self._json(404, {"error": "not found"})


def serve(persona_dir: str, cfg: Config, port: int = 8765,
          open_browser: bool = True) -> None:
    global SESSION
    SESSION = Session(persona_dir, cfg)
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    url = f"http://127.0.0.1:{port}/"
    print(f"live frontend → {url}   (persona: {SESSION.persona.name})")
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nshutting down.")
