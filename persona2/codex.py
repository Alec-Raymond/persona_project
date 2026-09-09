"""Model calls through the Codex CLI's ChatGPT subscription login."""

from __future__ import annotations

import asyncio
import copy
import json
import os
import shutil
import tempfile
from pathlib import Path
from typing import Any

from pydantic import BaseModel


def strict_schema(schema: dict) -> dict:
    """Require each declared field and close objects for Structured Outputs."""
    result = copy.deepcopy(schema)

    def visit(node: Any) -> None:
        if isinstance(node, dict):
            node.pop("default", None)
            if node.get("type") == "object":
                node["additionalProperties"] = False
                node["required"] = list(node.get("properties", {}))
            for value in node.values():
                visit(value)
        elif isinstance(node, list):
            for value in node:
                visit(value)

    visit(result)
    return result


def parse_events(stdout: str) -> tuple[str, dict]:
    """Use the final message and usage; never mistake an error for a reply."""
    messages: list[str] = []
    usage: dict = {}
    completed = False
    error = ""
    for line in stdout.splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        kind = event.get("type")
        if kind in {"error", "turn.failed"}:
            detail = event.get("error") or event
            error = detail.get("message", str(detail)) if isinstance(detail, dict) else str(detail)
        elif kind == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message":
                messages.append(item.get("text", ""))
        elif kind == "turn.completed":
            completed = True
            usage = event.get("usage") or {}
    if not completed:
        raise RuntimeError(f"Codex did not complete the call: {error or 'missing turn.completed event'}")
    text = messages[-1].strip() if messages else ""
    if not text:
        raise RuntimeError("Codex returned an empty final message.")
    return text, {
        "input_tokens": usage.get("input_tokens") or 0,
        "output_tokens": usage.get("output_tokens") or 0,
        "cache_read_input_tokens": usage.get("cached_input_tokens") or 0,
    }


async def generate(
    *, model: str, system: str, user: str, schema: type[BaseModel] | None,
    reasoning_effort: str = "medium", timeout: float = 300.0,
) -> tuple[Any, Any, dict]:
    """Return (validated result, serializable output, token usage).

    Each call starts a fresh, temporary session. Only the caller's stage
    instructions and input belong in the model context. Authentication stays
    with Codex; this module never reads or copies credentials.
    """
    binary = shutil.which("codex")
    if binary is None:
        raise RuntimeError("Codex CLI is missing. Install it and run `codex login` with ChatGPT.")

    with tempfile.TemporaryDirectory(prefix="persona2-codex-") as directory:
        root = Path(directory)
        instructions = root / "instructions.txt"
        instructions.write_text(system, encoding="utf-8")
        command = [
            binary, "exec", "--ignore-user-config", "--ephemeral",
            "--skip-git-repo-check", "--sandbox", "read-only", "--cd", directory,
            "--model", model, "--json", "--color", "never",
        ]
        settings = {
            "forced_login_method": "chatgpt",
            "model_reasoning_effort": reasoning_effort,
            "model_instructions_file": str(instructions),
            "project_doc_max_bytes": 0,
            "web_search": "disabled",
            "features.shell_tool": False,
            "features.unified_exec": False,
            "features.apps": False,
            "features.plugins": False,
            "features.multi_agent": False,
            "features.hooks": False,
            "features.memories": False,
            "features.browser_use": False,
            "features.computer_use": False,
            "features.image_generation": False,
        }
        for key, value in settings.items():
            command.extend(["-c", f"{key}={json.dumps(value)}"])
        if schema is not None:
            output_schema = root / "schema.json"
            output_schema.write_text(json.dumps(strict_schema(schema.model_json_schema())))
            command.extend(["--output-schema", str(output_schema)])
        command.append("-")  # Send the input through stdin, not shell arguments.
        env = {
            key: value for key, value in os.environ.items()
            if key not in {"OPENAI_API_KEY", "CODEX_API_KEY", "ANTHROPIC_API_KEY", "CODEX_THREAD_ID"}
        }
        proc = await asyncio.create_subprocess_exec(
            *command, stdin=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE, env=env,
        )
        try:
            stdout, stderr = await asyncio.wait_for(proc.communicate(user.encode()), timeout=timeout)
        except (TimeoutError, asyncio.CancelledError) as exc:
            if proc.returncode is None:
                proc.kill()
            await proc.wait()
            if isinstance(exc, asyncio.CancelledError):
                raise
            raise RuntimeError(f"Codex call exceeded {timeout:g} seconds ({model}).") from exc
        if proc.returncode:
            detail = stderr.decode(errors="replace").strip()
            # Service errors often arrive as JSONL on stdout instead of stderr.
            if not detail:
                try:
                    parse_events(stdout.decode())
                except (RuntimeError, ValueError) as exc:
                    detail = str(exc)
            raise RuntimeError(f"Codex CLI failed (exit {proc.returncode}): {detail[:1000]}")
        text, usage = parse_events(stdout.decode())
        if schema is None:
            return text, text, usage
        result = schema.model_validate_json(text)
        return result, result.model_dump(), usage
