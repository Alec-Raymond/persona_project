# Persona Project

Persona Project runs conversations with configurable AI characters. It includes a Python runtime, a terminal interface, and a local browser interface.

Each reply passes through several model calls. They select relevant prompts, combine their outputs, update the character's state, and produce a reply. Saved traces show the inputs and outputs at each stage.

## What you can do

- Chat with a character in the terminal or browser.
- Configure its prompts, initial state, voice, and conversation setting.
- Watch the pipeline run in the browser, or replay a saved trace.
- Inspect past runs as JSON or standalone HTML reports without making model calls.

Two example personas are included: `testbed` for checking the pipeline and `effusive` for trying a more expressive character.

The [development status note](wiki/development/status-2026-09-09.md) separates the working prototype from the larger design proposals.

## Quick start

Use Python 3.11 or newer. Run these commands from a local checkout:

```bash
git clone https://github.com/Alec-Raymond/persona_project.git
cd persona_project
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

To use your ChatGPT subscription, install the [Codex CLI](https://learn.chatgpt.com/docs/codex-cli) and sign in with ChatGPT:

```bash
codex login
persona2 chat personas/effusive --backend codex
```

The Codex backend uses **Astra (`gpt-6-astra`) for every stage** by default. It uses your ChatGPT login and Codex allowance; no OpenAI API key is needed. See [Codex authentication](https://learn.chatgpt.com/docs/auth).

The command prints the full turn trace and saves JSON under `traces/`. Type `quit` to end the conversation. Use `--quiet` to show only replies or `--no-save` to disable trace saving.

The browser interface shows each stage as it runs:

```bash
persona2 live personas/effusive --backend codex
```

Open <http://localhost:8765> if the browser does not open automatically. Each server run holds one conversation.

## Backends and models

| Backend | Authentication | Default model |
| --- | --- | --- |
| `--backend codex` | Codex CLI signed in with ChatGPT | Astra |
| `--backend claude` | Installed, authenticated `claude` CLI | Sonnet |
| `--backend anthropic` | `ANTHROPIC_API_KEY` in the environment or root `.env` | Sonnet |

Set `PERSONA2_BACKEND=codex` in a root `.env` file to use Codex without repeating the flag. Without a backend setting, the app uses Anthropic. The older `PERSONA2_CLAUDE_CLI=1` setting still selects the Claude CLI. See [.env.example](.env.example).

Use `--model` to set every stage or `--final` to override the final stage. Both accept model IDs or aliases: `astra`, `sonnet`, `opus`, and `haiku`. Choose a model supported by the selected backend. The older `--all` flag also accepts these aliases. **Haiku is opt-in.**

Codex uses `--reasoning medium` and a 300-second timeout per call by default. Change these with `--reasoning` and `--call-timeout`. `--concurrency` controls how many model calls can run at once. Model defaults and pipeline settings live in [config.py](persona2/config.py).

The Codex backend runs each stage in a fresh temporary session and validates structured responses against the pipeline's schemas. It requests a replacement base prompt, skips personal configuration, and disables coding tools. This still uses the Codex agent runner. Prompt isolation is not verified: a separate CLI prompt audit still renders skills and agent instructions. Recorded traces contain the application's prompts, not a complete dump of Codex's model context. The browser receives each call's text when that call completes.

SDK temperature, token-limit, and cache settings apply only to the Anthropic backend. CLI backends use their own generation settings. A Codex login, model-access, or usage-limit error stops the turn; the app does not switch to a paid API backend.

## Inspect an existing run

The [replay website](https://persona-traces.jjraymond-ai.chatgpt.site) opens exported multi-turn Astra conversations. The site is private to its owner. Selected published conversations will appear in its picker; the initial collection is empty.

1. Chat in the local browser interface for at least two turns.
2. Click **Export conversation** when the turn finishes.
3. Open the JSON file with **Open conversation** on the replay website.

The website reads opened files in the browser without uploading them. It shows the transcript, machine outputs, syntheses, state changes, and recorded calls. Exports require Astra for every call and continuous state across turns. See [replay-site/README.md](replay-site/README.md) to select conversations for publication.

After installing the project, these commands work without model credentials:

```bash
persona2 inspect traces/effusive-20260601-170224/turn-001.json
python viewer/build_viewer.py traces/
```

Open `viewer/index.html` in a browser to browse the generated reports. To rebuild one report, pass its run directory instead:

```bash
python viewer/build_viewer.py traces/effusive-20260601-170224
```

Reports show which prompts ran, how their outputs were combined, what state changed, and the resulting reply. They also include the recorded model calls for closer inspection.

## How a turn works

A **machine** is a prompt with a specific task and criteria for when it should run. Each persona defines its machines in `manifest.yaml`.

Each character also has a text state that changes during the conversation. The code calls this state `BwO`. It starts from `bwo_seed.txt`.

1. **Select machines.** Always-on machines run each turn. Relevance scores and random sampling select additional machines from the roster.
2. **Run machines.** Each selected machine reads the same state and conversation context. Calls run in parallel.
3. **Combine outputs.** The runtime randomly divides the machines into groups. A model call combines each group's outputs into one result.
4. **Update state and draft a reply.** An editor reads the group results, updates the character's state, and drafts a reply. It also records what changed.
5. **Revise and check the reply.** A revision step, called `armor` in the code, adjusts the draft for delivery. A separate reviewer checks it against the setting and conversation without seeing the internal state. If the reply fails, the pipeline retries up to the configured limit.
6. **Save the turn.** The runtime keeps the updated state and conversation history in memory. The CLI and live server save a trace for inspection.

[pipeline.py](persona2/pipeline.py) defines the current sequence. [prompts.py](persona2/prompts.py) contains the prompts. The [prompt walkthrough](docs/pipeline-prompts.md) records an earlier version for design reference.

Conversation state lasts for the runtime session. Saved traces support inspection and replay; they do not restore a conversation for continued chat.

## Define a persona

A persona directory contains:

| File | Purpose |
| --- | --- |
| `manifest.yaml` | Machine tasks, selection criteria, and always-on flags. |
| `voice.md` | Instructions for how the character speaks. |
| `bwo_seed.txt` | Initial character state for a new conversation. |
| `situation.txt` | Optional setting; otherwise the runtime uses a public waiting-place scenario. |

Copy an existing directory under `personas/`, edit its files, and pass its path to `persona2 chat` or `persona2 live`. The world schema and sample graph are design material; the current persona loader does not consume them.

## Repository map

```text
persona2/       Python package, runtime, prompts, and CLI
personas/       Example persona definitions
tests/          Automated tests that do not call models
viewer/         Live frontend, report builder, and generated HTML reports
replay-site/    Hosted viewer for selected multi-turn Astra conversations
traces/         Saved experiment runs as JSON
docs/           Runtime documentation and historical prompt walkthrough
wiki/           Research, design searches, and archived project material
pyproject.toml  Package metadata, dependencies, and test configuration
```

The [wiki guide](wiki/README.md) links to background research, design notes, and archived material. Some wiki pages describe proposals that the runtime does not implement.

## Development

```bash
python -m pytest -q
persona2 --help
```

The tests cover persona loading, grouping, schemas, traces, backend selection, and Codex process handling. They mock model calls. To test a real conversation locally:

```bash
persona2 chat personas/effusive --backend codex --quiet -m "Is this seat taken?"
```

The command uses your subscription and saves a trace under `traces/` for inspection.
