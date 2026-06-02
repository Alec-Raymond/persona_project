# Wiki System Design for Persona Project

A persistent, LLM-maintained knowledge base that grounds the persona system's design in source material and produces actionable development plans.

## Context

The persona system is a Deleuze & Guattari-inspired framework where "desiring machines" (small LLM-driven agents) edit a "Body without Organs" (a living prose text representing interiority). The system has a working Python codebase with a ghostwriter persona, but key design questions remain open — how machines should be structured, how memories surface, what coupling means. These questions require deep engagement with theoretical sources (D&G, Bergson, affect theory, literary theory) and careful translation into system design.

The wiki sits between raw source material and the codebase. It accumulates understanding across sessions, flags contradictions, tracks open questions, and ultimately produces development plans that a fresh Claude Code session can execute.

## Architecture

Three layers, following the LLM wiki pattern:

- **Raw sources** — curated collection of source documents. Immutable. The LLM reads from them but never modifies them.
- **The wiki** — LLM-maintained markdown files. Theory pages, synthesis, development plans, indexes. The LLM writes; the user reads in Obsidian and guides.
- **The schema** — `CLAUDE.md` files that tell the LLM how to operate as a wiki maintainer and codebase developer.

## Directory Structure

```
persona_project/
  wiki/
    raw/                    # Primary sources (immutable after placement)
    theory/                 # All theory pages — flat, organic, no subcategories
    development/            # Synthesis, development plans, open questions
    cited-sources.md        # Catalog of references not yet read
    index.md                # Master index, maintained by LLM
    log.md                  # Chronological activity log
    CLAUDE.md               # Wiki schema, conventions, workflows
  persona/
    CLAUDE.md               # Persona system conventions, architecture
    ...                     # Existing codebase (unchanged)
```

### Directory Details

**`raw/`** — The user places primary sources here: clipped articles, PDFs, pasted text as `.md`. These are sources the user has read or intends to read and work through together with the LLM. The LLM reads from `raw/` during ingest but never modifies files here.

**`theory/`** — Flat directory. Pages emerge during ingest and dialogue. No subfolders, no type taxonomy. Structure comes from wikilinks and tags, not from folder hierarchy. A page on "connective synthesis" might be spawned during ingest of the desiring machine taxonomy, then updated when Anti-Oedipus is ingested later. Pages are just pages — they can be about a concept, a thinker, a text, a comparison, or something that doesn't fit any predefined category.

**`development/`** — Two kinds of content, distinguished by frontmatter:
- **Synthesis pages** (`type: synthesis`) — Bridge theory to code. "What does coupling theory mean for the Machine dataclass?" Cross-cutting analysis that draws from multiple theory pages and the codebase.
- **Plan pages** (`type: plan`) — Concrete, Claude Code-ready implementation designs. These are the wiki's ultimate output, collaboratively designed between the user and LLM. See "Development Plan Guidelines" section below.
- **Open questions** (`development/open-questions.md`) — Maps code TODOs and wiki-internal research questions to wiki exploration needs. The bridge between "I noticed a gap" and "the wiki is working on it."

**`cited-sources.md`** — Tracks references that appear in primary sources but haven't been read yet. Each entry: title, author, where cited, why it might matter, status (unread / acquired / queued). A practical catalog of leads for future ingest sessions, not a wiki page with wikilinks.

**`index.md`** — Flat list of all wiki pages with one-line descriptions. No categories imposed. Maintained by the LLM on every ingest. The LLM reads this first when orienting to the wiki's current state. Serves as a quick table of contents for both the LLM and the user.

**`log.md`** — Append-only chronological record. Entries formatted as `## [YYYY-MM-DD] action | Subject` with a brief note on what happened and what pages were created/updated. Useful for session continuity and understanding the wiki's evolution.

## Page Conventions

### Frontmatter

Every wiki page gets YAML frontmatter:

```yaml
---
title: The Three Syntheses
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[desiring-machine-taxonomy]]"
tags:
  - anti-oedipus
  - machines
  - synthesis
---
```

- `sources` tracks which primary sources informed this page (as wikilinks).
- `updated` changes whenever the page is meaningfully revised.
- `tags` are for broad thematic grouping and Dataview queries.
- Development pages additionally have `type: synthesis` or `type: plan`.

### Connectivity

Connectivity is the wiki's core value. Every page is a node, not an island.

**Wikilinks in prose, not appendices.** Links go in the sentence where the concept is load-bearing, not in a "See also" section at the bottom. The link IS the connection.

**Bidirectional linking is mandatory.** When creating or updating any page, the LLM must:
1. Check what existing pages relate to the new content.
2. Add wikilinks in both directions — the new page links out, AND existing pages get updated to link back.
3. A page with few outbound links is a page that hasn't been properly integrated.

**Red links are welcome.** A `[[wikilink]]` to a page that doesn't exist yet is a signal, not an error. It marks a concept that deserves its own page when the time comes. Red links accumulate into a natural backlog.

**Tags vs. links.** Tags are for broad thematic grouping (`#affect-theory`, `#bergson`, `#machines`). Links are for specific conceptual relationships. Both forms of connectivity matter and serve different navigation needs.

### Hub Pages

Not created preemptively. Hub pages emerge naturally when a topic cluster gets dense enough — many pages interlinked around a theme with no single page connecting them. When a hub page emerges, it lives in `theory/` like any other page; it's just more connective than substantive. Maintenance audits flag when clusters are ready for a hub.

## Source Management

Two kinds of sources:

**Primary sources** — things the user has read and worked through with the LLM. Stored in `raw/`. Get the full ingest treatment: discussion, wiki page creation/updates, index and log updates. The relationship between sources and wiki pages is many-to-many: one source feeds many pages, one page draws from many sources.

**Cited sources** — references that appear in primary sources or emerge during discussion. The user hasn't read them. Tracked in `cited-sources.md` with enough context to know why they matter and what they'd contribute. These are leads, not ingested knowledge. They become primary sources when the user decides to read one and run an ingest session on it.

## Search Strategy

Layered approach, documented in CLAUDE.md for use across sessions:

1. **Index scan** — read `index.md` for a quick overview of what exists. Fast, cheap, works for targeted lookups.
2. **Semantic search via qmd** — for conceptual queries that keyword search won't catch. qmd provides hybrid BM25/vector search over markdown files with an MCP server interface for native Claude Code integration. Attempt to install during implementation; design works without it.
3. **Grep fallback** — for exact terms, specific quotes, or if qmd is unavailable.

## Workflows

### Ingest (User-Led)

The ingest is a conversation, not a batch job. The user drives; the LLM does the wiki work.

**Phase 1 — Orientation.** The LLM reads the source and reads `index.md` to understand the current wiki landscape. Presents an initial summary — major ideas, connections to existing wiki pages, what's surprising or important, any open questions this source might address. This summary is a working document for the conversation, not a wiki page.

**Phase 2 — User-directed exploration.** The user picks where to dig in. The LLM presents findings in digestible chunks — one concept or cluster at a time — and waits for the user's reaction. Discussion flows between structured extraction and exploratory dialogue:
- Ask, don't assume. When the LLM notices something, surface it as an observation or question. The user decides what earns a page.
- Show connections, especially tensions. Flag when new material challenges or enriches existing wiki content. Don't silently resolve contradictions.
- Capture dialogue insights. The conversation itself produces knowledge — implications, connections, questions not in the source. These belong in the wiki.
- Let the user set pace and depth. "Let's dig into this" and "note this and move on" are both valid.

**Phase 3 — Progressive wiki updates.** As discussion settles on concepts, the LLM creates or updates pages incrementally. Bidirectional linking happens immediately. The user reviews changes in Obsidian in real-time and provides feedback.

**Phase 4 — Wrap-up.** After the source is worked through:
1. Update `index.md` with new pages.
2. Append to `log.md` with what happened and what pages were created/updated.
3. Extract cited sources and add to `cited-sources.md`.
4. Flag red links, open questions, and any TODOs the source addresses.

**What not to do during ingest:**
- Don't produce a single summary page per source — that means not enough work was done.
- Don't create wiki pages from undiscussed material.
- Don't silently resolve contradictions with existing wiki content.
- Don't move on from a section until the user signals they're ready.

### Query

The user asks a question against the wiki. The LLM searches for relevant pages (index → qmd → grep), reads them, and synthesizes an answer with references to specific pages. If the answer produces valuable synthesis, offer to file it as a wiki page — explorations should compound in the knowledge base, not disappear into chat history.

### Maintenance

Periodic health checks that produce concrete actions.

**Connectivity audit:**
- Orphan pages — pages with zero inbound links. Need linking or aren't pulling their weight.
- Red links — wikilinks pointing to non-existent pages. Prioritized backlog by link count.
- Weak nodes — pages with only 1-2 connections that should have more.
- Missing bidirectional links — page A links to B but B doesn't link back.

**Coherence audit:**
- Contradictions — where two pages make conflicting claims. Flag for discussion, don't resolve silently.
- Staleness — pages not updated despite newer sources touching their concepts.
- Depth check — pages that are stubs when the wiki now has enough material to say more.

**Expansion audit:**
- Concepts appearing frequently without their own page.
- Theory areas the persona system depends on but the wiki hasn't covered.
- Code TODOs that map to wiki research gaps.
- Cited sources that would fill known gaps.

**TODO scan:**
- Grep the codebase for `#TODO` comments.
- Compare against `development/open-questions.md`.
- Flag new TODOs not yet tracked.
- Flag questions where wiki research is sufficient to write a development plan.

## TODO Integration

TODOs in the code represent understanding gaps — questions the codebase is asking that require theoretical grounding to answer well. The wiki tracks and works toward answering them.

**Lifecycle:** TODO in code → open question in wiki → wiki research during ingest → development plan → code change → TODO resolved.

**`development/open-questions.md`** tracks both code TODOs and wiki-internal research questions:

```markdown
## Machine coupling design
- **Origin:** code — `persona/persona/machine.py:21`
- **Question:** How exactly should machines be designed? What are coupling interfaces? How should families be organized?
- **Relevant wiki pages:** [[coupling]], [[partial-objects]], [[the-three-syntheses]]
- **Status:** researching
```

```markdown
## Guattari's four functors
- **Origin:** wiki — emerged during ingest of desiring machine taxonomy
- **Question:** How do the four functors (T, F, Phi, U) map to the persona system's architecture?
- **Relevant wiki pages:** [[four-functors]]
- **Status:** open — needs dedicated source work
```

**During ingest:** The LLM checks open questions and flags when source material addresses one. This gives ingest sessions direction without dictating them.

**During maintenance:** The TODO scan greps the codebase for new TODOs, checks them against open-questions.md, and flags questions ready to graduate to development plans.

**Graduation:** When wiki research sufficiently covers an open question, it becomes a candidate for a development plan in `development/`. The plan is collaboratively designed between the user and LLM, referencing both the TODOs it resolves and the theory pages that inform the solution.

## Development Plan Guidelines

Plans in `development/` are the wiki's ultimate output — documents complete enough for a fresh Claude Code session to pick up and execute. They are collaboratively designed between the user and LLM; the format is flexible, but a fresh session needs the following to succeed:

**Theoretical grounding.** Which theory pages to read and what key claims from those pages drive the design decisions. The plan should reference, not duplicate — "see [[coupling]] for full treatment" — but summarize the specific claims that are load-bearing for this plan. Without this, Claude will make reasonable-looking choices that violate the theoretical framework.

**Motivation.** What open question(s) or TODO(s) this plan addresses, and why the wiki's research is now sufficient to act. Links to `open-questions.md` entries and code TODOs.

**Current state.** What the relevant code looks like now — specific files and what they do. What's missing or wrong. The plan should not assume Claude knows the codebase; it should point Claude to exactly what to read.

**Design decisions.** What was decided and why, stated as constraints and interfaces rather than implementation code. Claude is good at writing code; the plan should specify *what* the system should do and *what invariants it should maintain*, and let Claude figure out the how.

**Scope boundaries.** What's in scope and what's explicitly not. "This plan does not change the synthesis pipeline" prevents scope creep. Plans should be scoped to a coherent chunk — if a plan tries to touch everything, it's too big.

**Verification.** How to know the work is done — tests to write, behavior to verify, invariants that should hold after the change.

These guidelines describe what information must be present, not a mandatory structure. A plan might be two paragraphs or two pages depending on the complexity of the change. The format should serve the content.

## CLAUDE.md Files

### Wiki CLAUDE.md

Covers:
- **Project identity** — what this wiki is and what it's for.
- **Structure** — directory layout, what lives where.
- **Page conventions** — frontmatter schema, linking rules, tags.
- **Search strategy** — index → qmd → grep.
- **Workflows** — ingest (user-led), query, maintenance. Full conventions for each.
- **Development plan guidelines** — what a fresh session needs to succeed (see below).
- **Constraints** — don't modify `raw/`, don't create pages from undiscussed material, don't silently resolve contradictions.

### Persona CLAUDE.md

Covers:
- **Project overview** — the D&G-inspired persona framework. Desiring machines editing a BwO. The three syntheses as operational logic.
- **Architecture** — the pipeline (Selection → Machine Edits → Memory Resonance → Synthesis → Evolution). Key files and what they do.
- **The ghostwriter persona** — the current test case and its configuration files.
- **How to run** — dependencies, tests, CLI.
- **How to use development plans** — when a plan exists in `wiki/development/`, read it plus referenced theory pages and code files before implementing. The plan is the spec.
- **The wiki as context** — when facing a design question, check wiki theory pages before making assumptions. The wiki is authoritative on theoretical grounding.
- **Code conventions** — testing approach, style, dependencies.

## Implementation Notes

- The wiki and codebase live on the same branch (`main`) in separate directories. `git log -- wiki/` and `git log -- persona/` filter history by concern. The wiki can be stripped for release later.
- Obsidian is the viewer. All conventions are Obsidian-compatible: `[[wikilinks]]`, YAML frontmatter, tags, graph view, Dataview.
- qmd should be installed as an MCP server for semantic search if possible. The design works without it — index.md + grep cover the need at small-to-medium scale.
- The first source to ingest is `raw/desiring_machine_research_report.md` — the comprehensive taxonomy of desiring machines already in the wiki directory.
- Existing code TODOs in `machine.py` and `memory.py` should be seeded into `open-questions.md` during setup.
