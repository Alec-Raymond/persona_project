"""Capture the real Codex request at loopback; never run a model or save headers.

    python scripts/audit_codex_prompt.py --output /tmp/persona-codex-audit.json
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import shutil
import subprocess
import sys
import threading
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from persona2 import codex
from persona2.models import FitCheck

SYSTEM = "PERSONA_AUDIT_SYSTEM_ONLY"
USER = "PERSONA_AUDIT_USER_ONLY"


def inspect_request(request: dict, schema=None) -> dict:
    items = request.get("input", [])
    messages = [{"role": item.get("role"), "content": item.get("content", [])}
                for item in items if item.get("type") == "message"]
    tools = list(request.get("tools", []))
    for item in items:
        if item.get("type") == "additional_tools":
            tools.extend(item.get("tools", []))
    expected = [
        {"role": "developer", "content": [{"type": "input_text", "text": SYSTEM}]},
        {"role": "user", "content": [{"type": "input_text", "text": USER}]},
    ]
    # Codex includes an empty additional_tools item even when no tools exist.
    # Permit only that known envelope, not arbitrary extra context items.
    other = [item for item in items if item.get("type") != "message"]
    envelopes_only = all(
        item.get("type") == "additional_tools" and item.get("tools") == []
        and item.get("role") == "developer"
        and not (set(item) - {"type", "id", "role", "tools"})
        for item in other
    )
    output_format = (request.get("text") or {}).get("format")
    schema_matches = (
        output_format is None if schema is None else
        isinstance(output_format, dict)
        and output_format.get("type") == "json_schema"
        and output_format.get("strict") is True
        and output_format.get("schema") == codex.strict_schema(schema.model_json_schema())
    )
    clean = (request.get("model") == "gpt-6-astra" and messages == expected
             and not request.get("instructions") and not tools
             and envelopes_only and schema_matches)
    return {"model": request.get("model"), "clean": clean,
            "schema_matches": schema_matches,
            "instructions": request.get("instructions"),
            "non_message_items": [{k: v for k, v in item.items() if k != "id"} for item in other],
            "messages": messages, "tools": tools, "text": request.get("text")}


async def capture_request(schema=None) -> dict:
    captures = []
    ready = threading.Event()

    class Handler(BaseHTTPRequestHandler):
        protocol_version = "HTTP/1.1"

        def log_message(self, *args):
            pass

        def record(self, raw):
            captures.append(json.loads(raw))
            ready.set()

        def do_GET(self):
            # Refuse WebSocket upgrades so the normal CLI sends its complete
            # request over HTTP, instead of stopping at a prefix warmup frame.
            self.send_response(426 if self.headers.get("Upgrade") else 404)
            self.send_header("Content-Length", "0")
            self.send_header("Connection", "close")
            self.end_headers()

        def do_POST(self):
            self.record(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
            body = b'{"error":{"message":"Local audit; no model was called."}}'
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    launch = asyncio.create_subprocess_exec

    async def local_launch(*command, **kwargs):
        command = list(command)
        # These overrides change only transport routing and encoding. All
        # persona prompt/tool settings come from the production adapter.
        command[-1:-1] = ["-c", f'openai_base_url="http://127.0.0.1:{server.server_port}/v1"',
                          "-c", "features.enable_request_compression=false"]
        return await launch(*command, **kwargs)

    try:
        with patch.object(codex.asyncio, "create_subprocess_exec", local_launch):
            task = asyncio.create_task(codex.generate(model="gpt-6-astra", system=SYSTEM,
                                                      user=USER, schema=schema, timeout=30))
            try:
                for _ in range(600):
                    if ready.is_set():
                        break
                    if task.done():
                        await task
                    await asyncio.sleep(0.05)
                if not captures:
                    raise RuntimeError("No model request reached the local audit endpoint.")
            finally:
                task.cancel()
                try:
                    await task
                except (asyncio.CancelledError, RuntimeError):
                    pass
    finally:
        server.shutdown()
        server.server_close()
    return inspect_request(captures[0], schema)


async def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("/tmp/persona-codex-audit.json"))
    args = parser.parse_args()
    results = {}
    for name, schema in [("plain", None), ("structured", FitCheck)]:
        result = await capture_request(schema)
        results[name] = result
        print(name, "clean=" + str(result["clean"]), "messages=" + str(len(result["messages"])),
              "tools=" + str(len(result["tools"])), flush=True)
        for message in result["messages"]:
            print(message["role"], str(message["content"])[:150], flush=True)
    binary = shutil.which("codex")
    version = subprocess.run([binary, "--version"], capture_output=True, text=True, check=True).stdout.strip()
    report = {"checked_at": datetime.now(timezone.utc).isoformat(), "codex_version": version,
              "adapter_sha256": hashlib.sha256(Path(codex.__file__).read_bytes()).hexdigest(),
              "transport": "Loopback HTTP capture; no inference; request headers discarded",
              "results": results}
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("Saved", args.output)
    if not all(result["clean"] for result in results.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    asyncio.run(main())
