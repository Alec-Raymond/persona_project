# Persona Project

Persona Project runs conversations with configurable AI characters. It includes a Python runtime, a terminal interface, and a local browser interface.

Each reply passes through several model calls. They select relevant prompts, combine their outputs, update the character's state, and produce a reply. Saved traces show the inputs and outputs at each stage.

## What you can do

- Chat with a character in the terminal or browser.
- Configure its prompts, initial state, voice, and conversation setting.
- Watch the pipeline run in the browser, or replay a saved trace.
- Inspect past runs as JSON or standalone HTML reports without making model calls.

Two example personas are included: `testbed` for checking the pipeline and `effusive` for trying a more expressive character.

## Quick start

Use Python 3.11 or newer. Run these commands from a local checkout:

```bash
git clone https://github.com/Alec-Raymond/persona_project.git
cd persona_project
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

For new conversations, set `ANTHROPIC_API_KEY` in your environment or in a root `.env` file. The [.env.example](.env.example) file shows the supported settings.

```bash
export ANTHROPIC_API_KEY="your-api-key"
persona2 chat personas/testbed --all haiku
```

The command prints the full turn trace and saves JSON under `traces/`. Type `quit` to end the conversation. Use `--quiet` to show only replies or `--no-save` to disable trace saving.

The browser interface shows each stage as it runs:

```bash
persona2 live personas/effusive --all haiku
```

Open <http://localhost:8765> if the browser does not open automatically. Each server run holds one conversation.

`--all haiku` uses the same model tier for every stage. Omit it to use the per-stage defaults in [config.py](persona2/config.py). The CLI also accepts `--all sonnet`, `--all opus`, and `--final` to choose the final-stage tier. Model identifiers and tuning parameters live in `config.py`.

An optional backend calls an installed, authenticated `claude` CLI. Enable it with `PERSONA2_CLAUDE_CLI=1`; that backend does not use the SDK's API key, temperature, token-limit, or cache settings.

## Inspect an existing run

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

The tests cover persona loading, machine validation, grouping, schema generation, and trace serialization/rendering. They do not verify live model responses. New conversations call external models through the configured backend.
