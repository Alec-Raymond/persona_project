# Persona Project

An experimental Python runtime for conversational characters whose internal state changes through interaction.

The project explores character as an ongoing process. Small, specialized LLM calls respond to the conversation and the character's current interior state. Their outputs combine, change that state, and shape what the character says next.

The design draws on Deleuze and Guattari's *desiring machines*, alongside research on affect, memory, rhythm, and voice. The [research wiki](wiki/README.md) records those foundations and the design questions they raise.

## What is here

- A conversation pipeline with machine selection, parallel calls, group synthesis, state updates, and reply review.
- Two example personas: `testbed` exercises the machinery; `effusive` explores a more expressive character.
- A terminal interface and a local browser interface with live pipeline events and trace replay.
- Saved JSON traces and standalone HTML reports for inspecting past runs without making model calls.

This is a research prototype. The code implements a working experiment; the wiki also contains proposals and older designs.

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

Reports include selected machines, their outputs, synthesis groups, interior-state changes, replies, and recorded model calls. The generated HTML files remain in the repository as browsable experiment records. [.gitattributes](.gitattributes) excludes those reports from GitHub's language statistics. The maintained live frontend, `viewer/live.html`, still counts as HTML.

## How a turn works

A **machine** is a prompt specification with a particular sensitivity and output, such as hesitation, memory, or rhythm. Each persona defines its machines in `manifest.yaml`.

The **BwO** (body without organs) is the project's name for a mutable text describing the character's interior state. It starts from `bwo_seed.txt` and changes after each turn.

1. **Select machines.** Always-on machines fire each turn. Relevance scores and a random vote select additional machines from the pool.
2. **Run machines.** Each selected machine reads the same pre-turn state and situation. Machine calls run in parallel.
3. **Group and synthesize.** Code partitions machines into groups. Each group combines their products through a synthesis call.
4. **Update the interior.** An editor reads the group outputs, rewrites the BwO, records edits, and drafts a reply.
5. **Shape and review the reply.** The armor stage shapes the spoken reply. A blind reviewer checks its fit using only the situation and conversation. Failed reviews trigger a bounded redraft loop.
6. **Keep the result.** The runtime stores the updated state and conversation history in memory. The CLI and live server save the turn trace.

[pipeline.py](persona2/pipeline.py) defines the current sequence. [prompts.py](persona2/prompts.py) contains the prompts. The [prompt walkthrough](docs/pipeline-prompts.md) records an earlier version for design reference.

Conversation state lasts for the runtime session. Saved traces support inspection and replay; they do not restore a conversation for continued chat.

## Define a persona

A persona directory contains:

| File | Purpose |
| --- | --- |
| `manifest.yaml` | Machine roster, sensitivities, outputs, and always-on flags. |
| `voice.md` | Voice sketch used when shaping the reply. |
| `bwo_seed.txt` | Initial interior state for a new conversation. |
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

The active implementation formerly lived under `v2/`; it now lives at the repository root. The package and command remain named `persona2`.

Start with the [wiki guide](wiki/README.md) for research navigation. The [design searches](wiki/design_search/README.md) explain the sources behind implementation choices. The [archive](wiki/archive/README.md) holds earlier project material.

## Development

```bash
python -m pytest -q
persona2 --help
```

The tests cover persona loading, machine validation, grouping, schema generation, and trace serialization/rendering. They do not verify live model responses. New conversations call external models through the configured backend.
