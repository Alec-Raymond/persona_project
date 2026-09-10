# Conversations

[Open the site](https://alec-raymond.github.io/persona_project/). GitHub Pages hosts the replay page; live chats run locally.

A static page using the live viewer's tuned machine replay. It shows the parallel
text streams, animated grouping, syntheses, drafts, fit reviews, and final replies.
The build copies the renderer from `viewer/live.html`; it does not maintain a second UI.
The browser reproduces the Python player's event sequence and delays. It makes no model calls.
Text draws at about 900 characters per second per call. Stage transitions wait until
all current text finishes. Analysis and results stay open, including after grouping.
Fit reviews and recorded redrafts also replay in full.
Opened conversation files stay in browser memory. The page does not upload them.
The initial selected collection is empty, pending conversations recorded by Alec.

## Open a conversation

1. Run `persona2 live --backend codex` from the project root. The default persona is Sam.
2. Submit at least two user messages in the local chat.
3. Click **Export conversation** after the last turn finishes.
4. Click **Open file** on the replay page and choose the exported JSON.
5. Click **Replay**.

Pause stops text and transitions. Click an earlier message to inspect that turn's
reply and machine outputs. The turn selector and arrows also open completed turns;
unplayed turns replay when selected. Earlier messages remain in the transcript.

## Select a conversation for publication

1. Inspect the exported conversation and choose whether to publish its full trace.
2. Copy the export to `public/selected/<name>.json`.
3. Add that filename to `public/selected/index.json`.
4. Run `npm run build`.
5. Commit the selected files and push to `main`. GitHub Actions builds and publishes the site.

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

The build uses relative asset paths, so the same files work under the repository's
GitHub Pages path and on localhost. The build needs Node.js. DOM tests use jsdom;
the published page has no third-party runtime dependencies.
The [Pages workflow](../.github/workflows/pages.yml) tests, builds, and publishes it.

`tests/test_replay_parity.py` compares every hosted replay event and timestamp with
the Python player. `tests/replay-renderer.test.mjs` runs the shared renderer against
long recorded outputs. It checks stage completion, both phases, pause, cancellation,
consecutive turns, and inspection of earlier messages.

The build exports static files to `dist/client`. Only explicitly selected JSON
files ship with the page. All other experiment traces stay outside this project.
