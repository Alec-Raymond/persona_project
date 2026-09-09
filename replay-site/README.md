# Persona trace replay

A static page for replaying multi-turn Astra conversations. It makes no model calls.
Opened conversation files stay in browser memory. The page does not upload them.
The initial selected collection is empty, pending conversations recorded by Alec.

## Open a conversation

1. Run `persona2 live personas/effusive --backend codex` from the project root.
2. Submit at least two user messages in the local chat.
3. Click **Export conversation** after the last turn finishes.
4. Open the exported JSON on the replay page.

## Select a conversation for publication

1. Inspect the exported conversation and choose whether to publish its full trace.
2. Copy the export to `public/selected/<name>.json`.
3. Add that filename to `public/selected/index.json`.
4. Run `npm run build`.
5. Publish the validated build through Sites.

An existing saved run can be exported without running a model:

```bash
python -m persona2.trace_export traces/<run> conversation.json --title "Conversation title"
```

The exporter and browser require at least two turns, `gpt-6-astra` on every
recorded call, and continuous character state between turns. Traces record
application prompts and returned outputs; they do not capture Codex's entire
model context. The current subscription backend passes an
[outgoing-request audit](../docs/codex-backend.md); older traces can predate that fix.

## Local development

```bash
npm install
npm run dev
npm run build
```

The build exports static files to `dist/client`. Only explicitly selected JSON
files ship with the page. All other experiment traces stay outside this project.
