# Codex subscription backend verification

The outgoing Astra requests contain only the caller's stage prompt and input,
with zero tools. Both plain-text and structured-output requests pass the audit
with `codex-cli 0.153.4` on 9 September 2026.

The [saved audit](codex-prompt-audit.json) includes the captured messages,
tool declarations, structured-output schema, CLI version, and adapter hash.
It contains no credentials, request headers, or real conversation text.

## What caused the extra context

The earlier adapter's CLI switches do not remove every source of Codex context.
The actual request contains skills, agent instructions, global `AGENTS.md`, and
coding tools. A separate `debug prompt-input` command is insufficient to verify
what the production `exec` command sends.

Three changes remove that context in [the adapter](../persona2/codex.py):

- Disable skill discovery, agent roles, extra instructions, and tool features.
- Read Codex's native model catalog and remove Astra's forced code mode and tool defaults.
  Preserve the model's reasoning choices and context limits.
- Use an empty temporary Codex state directory for each child process.
  This excludes global `AGENTS.md`, which `project_doc_max_bytes=0` does not suppress.
  Codex reads its existing ChatGPT login through a symlink to its native `auth.json`.
  Python does not read or copy credentials. The parent environment remains unchanged.

The stage prompt replaces Codex's base instructions. Each call starts a fresh
session. Structured responses still use the pipeline's exact output schema.

The adapter uses the documented
[configuration settings](https://learn.chatgpt.com/docs/config-file/config-reference),
including `model_catalog_json`, `model_instructions_file`, and instruction switches.

## Reproduce without running a conversation

1. Install the project and sign into Codex with ChatGPT.
2. Run `python scripts/audit_codex_prompt.py --output /tmp/persona-codex-audit.json` from the repository root.
3. Check that both lines show `clean=True messages=2 tools=0`.

The audit invokes the production adapter and installed Codex binary. It changes
only the destination URL and request compression. A loopback HTTP server rejects
WebSocket upgrades so it receives the complete HTTP request, including user input.
The server discards request headers and returns an error without forwarding the
request. The audit cancels the CLI after capture. No model generates a response.

The check requires Astra, exact message contents, no extra instructions, no tools,
and the expected structured-output schema. Codex includes an empty tool envelope;
the check accepts that envelope and rejects unknown context items.

Run this audit again after changing the adapter or upgrading Codex.
Historical traces from before this fix retain their original generated outputs.
They do not become evidence of the corrected adapter's conversation behavior.
