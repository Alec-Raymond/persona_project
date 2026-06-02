# Wiki: Persona Project Knowledge Base

A persistent, LLM-maintained knowledge base grounding the persona system's design in source material (Deleuze & Guattari, Bergson, affect theory, literary theory) and producing actionable development plans.

The wiki sits between raw sources and the codebase. It accumulates understanding across sessions, flags contradictions, tracks open questions, and produces development plans that a fresh Claude Code session can execute.

## Directory Structure

```
wiki/
  raw/                    # Primary sources — immutable after placement
  theory/                 # Theory pages — flat, organic, no subcategories
  development/            # Synthesis pages, development plans, open questions
  cited-sources.md        # References not yet read
  index.md                # Master index (read this first to orient)
  log.md                  # Chronological activity log
  CLAUDE.md               # This file
```

### raw/

The user places primary sources here: clipped articles, PDFs, pasted text as `.md`. These are sources the user has read or intends to read and work through together with the LLM. **Never modify files in `raw/`.**

### theory/

Flat directory. Pages emerge during ingest and dialogue. No subfolders, no type taxonomy. Structure comes from wikilinks and tags, not folder hierarchy. A page might be about a concept, a thinker, a text, a comparison, or something that doesn't fit any category.

### development/

Two kinds of content, distinguished by frontmatter:
- **Synthesis pages** (`type: synthesis`) — Bridge theory to code. Cross-cutting analysis drawing from multiple theory pages and the codebase.
- **Plan pages** (`type: plan`) — Concrete, Claude Code-ready implementation designs. The wiki's ultimate output.
- **`open-questions.md`** — Maps code TODOs and wiki-internal research questions to exploration needs.

## Page Conventions

### Frontmatter

Every wiki page gets YAML frontmatter:

```yaml
---
title: Page Title
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[source-page]]"
tags:
  - relevant-tag
---
```

- `sources` — which primary sources informed this page (as wikilinks).
- `updated` — changes whenever the page is meaningfully revised.
- `tags` — broad thematic grouping for Dataview queries.
- Development pages additionally have `type: synthesis` or `type: plan`.

### Connectivity

Connectivity is the wiki's core value. Every page is a node, not an island.

**Wikilinks in prose, not appendices.** Links go in the sentence where the concept is load-bearing, not in a "See also" section at the bottom.

**Bidirectional linking is mandatory.** When creating or updating any page:
1. Check what existing pages relate to the new content.
2. Add wikilinks in both directions — the new page links out, AND existing pages get updated to link back.
3. A page with few outbound links hasn't been properly integrated.

**Red links are welcome.** A `[[wikilink]]` to a page that doesn't exist yet is a signal, not an error. It marks a concept that deserves its own page when the time comes.

**Tags vs. links.** Tags are for broad thematic grouping (`#affect-theory`, `#bergson`, `#machines`). Links are for specific conceptual relationships.

### Reading mode

The wiki's value depends on synthesis across traditions — but synthesis-appetite can become what Sedgwick calls *paranoid reading*: finding the master-pattern everywhere because you went in looking for it. The wiki is structurally vulnerable to this: the same pulsation / failure-mode / overbound-underbound / paranoid-schizo shapes have been recurring across Jung, D&G, Keleman, Tomkins. Some of that is real convergence; some is method-effect.

Read reparatively alongside synthetically. Stay close to each source's own vocabulary and distinctions *before* mapping it onto existing wiki scaffolding. Note what's distinctive before noting what converges. If a convergence has to be forced — if "X = Y at a different register" feels too clean — treat that as a tell: either the mapping is wrong or the source is doing something the scaffolding doesn't yet have vocabulary for. Preserve the distinctive; convergences can be argued for later, but what's lost to flattening is hard to recover.

This pairs with the existing constraint *never silently resolve contradictions*. Same spirit: the wiki earns synthesis by first letting differences stand.

### Hub Pages

Not created preemptively. Hub pages emerge naturally when a topic cluster gets dense enough. When one emerges, it lives in `theory/` like any other page.

## Search Strategy

The wiki is a dense conceptual graph. Most searches are not "find this exact string" but "find what connects to this idea" — which is the gap qmd closes and grep cannot. Default to qmd for anything conceptual, use grep for anything verbatim, and use them together when you want both coverage and precision.

### Tools

**1. Index scan.** Read `index.md` first when you already know roughly what you're looking for. Fast orient; cheap to start with.

**2. qmd semantic search (MCP).** The workhorse for conceptual discovery. Use liberally. qmd hybridizes BM25, vector similarity, and optional LLM re-ranking — it surfaces pages that discuss an idea even when they don't use your exact words. This makes it the right tool for the wiki's core problem: *finding the connections that make pages stop being islands*.

Use qmd to:
- Discover which existing pages an incoming source relates to (essential during ingest Phase 1 — do this before grep).
- Surface tensions and convergences across pages you didn't know existed.
- Pull specific claims out of long `raw/` sources without reading them end-to-end (via `get` / `multi_get` after `query`).
- Map a concept cluster ("everything the wiki says about pre-personal affect") before editing any page.
- Find a page when you remember the idea but not the title or exact terms.
- Audit whether a page is well-integrated — run a qmd query for its core concepts and see which pages don't already link it.

Sub-query types (combine for best recall; first sub-query gets 2× weight — put the strongest signal first):
- `lex` — BM25 keyword search. Supports `"quoted phrases"` and `-negation`. Use when the term is distinctive.
- `vec` — semantic vector search on natural-language questions.
- `hyde` — write 50–100 words of the answer you'd expect; retrieves pages similar to that passage. Often the most powerful on nuanced topics.

Always set `intent` on every call — a short disambiguating phrase that helps re-ranking and snippets.

**Gotcha.** `vec` and `hyde` parse `-` as a negation operator and will error out on compound words. Rephrase `pre-personal` as `pre personal`, `face-to-face` as `face to face`, `self-validating` as `self validating`, `body-image` as `body image`. Only `lex` accepts `-` literally (and only inside `"quotes"`).

**3. Grep.** For exact strings and structural scans where precision matters: finding every `[[wikilink]]` to a page, every mention of a specific name, every occurrence of a verbatim quote, every frontmatter field. Grep is authoritative where qmd is associative.

**4. Full read.** Once a page is identified as relevant, read it in full.

### Picking between qmd and grep

| Want to... | Use |
|---|---|
| Find all inbound links to `body-without-organs.md` | grep `[[body-without-organs]]` |
| Find all pages that discuss the BwO idea (even without the wikilink) | qmd |
| Check if "cybernetic fold" appears verbatim anywhere | grep |
| Find pages that discuss a threshold between binary and continuous | qmd |
| Audit a page's inbound link coverage | grep for the page name, then qmd for its concepts to catch misses |
| Surface tensions between a new source and existing pages | qmd (lex + vec + hyde) |
| Verify a specific quote or frontmatter value | grep |
| Orient to what the wiki says about a thinker | qmd first, then read the top hits |
| Enumerate all pages with a specific tag | grep on frontmatter |
| Discover pages that *should* share a tag but don't | qmd |

**Default posture:** reach for qmd first on any conceptual task. Fall back to grep when you already know the exact string, or when you need an exhaustive list of literal matches. Use them together when auditing — qmd maps the territory, grep confirms specific terms. Don't run three overlapping queries for the same question; pick the tool that fits the shape of the question and move on.

### Re-indexing qmd

qmd's index is a snapshot. After any session that creates or edits wiki pages, run:

```bash
qmd embed
```

This is only ~a few seconds for incremental updates. Do it at the end of an ingest session, not after every single edit.

## Workflows

### Ingest (User-Led)

The ingest is a conversation, not a batch job. The user drives; the LLM does the wiki work. For foundational or book-length sources, ingest runs in four phases. Shorter sources (a single article, a blog post) can collapse Phases 1 and 2 into a single presented summary.

**Phase 1 — Exhaustive flagging.** Read the source end-to-end. No skimming. The goal is *coverage*, not synthesis: catalog every distinctive concept, argument, and turn the source makes, in its own vocabulary, before mapping onto existing wiki scaffolding.

Work out of a dedicated tmp directory outside the wiki:

```
/tmp/<source-slug>_ingest/
  source.txt    # extracted text (pdftotext -layout for PDFs)
  notes.md      # structured concept inventory — the Phase-1 output
```

`notes.md` is an inventory, not prose. Use consistent markers so it stays scannable in Phase 2 and greppable in Phase 3:
- `★★` critical / load-bearing concept
- `★` important concept worth capturing
- `⚠` tension with an existing wiki page (flag, never resolve)
- `◆` concept directly relevant to persona-system architecture

Open `notes.md` with a chapter/section map that includes **line ranges into `source.txt`** — subsequent phases re-read against these ranges, and omitting them forces rescans of the whole text. Organize the body by the source's own structure (chapter, section, argument), not by wiki taxonomy.

[Reading mode](#reading-mode) applies throughout: preserve what is distinctive before noting what converges. If a convergence has to be forced, that is a tell — record the source's own term and flag the apparent parallel as `⚠`, don't collapse them.

Use qmd during Phase 1 only lightly, to mark `⚠` tension candidates against existing pages. Deep integration is Phase 3's job; don't let qmd pull you out of the linear read.

For long sources, Phase 1 spans multiple sessions and survives context compaction precisely because `notes.md` holds the state. On resume, open the notes file, find the last chapter covered, and continue from there. This is why the file lives in `/tmp/` under a predictable slug rather than in scratch buffers.

**Phase 2 — Present categorized candidates.** Summarize `notes.md` into a candidate list organized by how confident you are each concept earns a page. Do *not* just hand over the raw notes; the user wants a judgment call they can ratify, amend, or reject.

Three buckets:
- **Definite pages** — load-bearing, clearly distinctive, omitting them would be a visible gap
- **Potential pages** — important, but may fold into existing pages, or hinge on user's scope judgment
- **Borderline additions** — likely belong as additions to existing pages rather than standalone, or concepts the source treats in passing

Hand over both the categorized list AND the path to the full `notes.md` so the user can drill into any entry. The user decides which candidates become pages, which become additions to existing pages, which are deferred, and which flagged tensions need explicit discussion.

Ask, don't assume. Do not start Phase 3 until the user has signed off on scope.

**Phase 3 — Per-page accuracy pass.** For each approved page, **read the source on its own terms before comparing to the wiki**. Order matters: leading with wiki-comparison risks the paranoid-reading failure mode where the source gets flattened into the wiki's existing vocabulary. Lead with the source; let the wiki arrive second.

For each approved concept:
1. Re-read the flagged passages using line ranges from the chapter-map — as the source's own argument, in the source's own vocabulary.
2. grep `/tmp/<source-slug>_ingest/` for every other mention of the term, to catch places Phase 1 may have under-weighted.
3. Note evolution within the work — a term's early usage often differs from its later usage in the same author (Lacan's 1953 "symbolic" vs. his 1966 "symbolic" is the paradigm case).
4. *Then* qmd the wiki (lex + vec + hyde) for adjacent existing material, and decide what existing pages should be linked, contrasted, or updated.
5. Write the page using all the information the source provides on the concept. Don't abbreviate when the source is rich; the wiki entry should reflect the source's full treatment, not a gist.

**Phase 4 — Progressive wiki updates.** Create or update pages in the order the user prioritized. Bidirectional linking happens immediately (see [Connectivity](#connectivity)). After the last page is written:
1. Update `index.md` with new pages.
2. Append to `log.md` with what happened and what pages were created/updated.
3. Extract cited sources and add to `cited-sources.md`.
4. Flag red links, open questions, and any TODOs the source addresses.
5. Run `qmd embed` to refresh the index.
6. Leave `/tmp/<source-slug>_ingest/` in place unless the user asks to clean it up — the notes file remains a useful reference for later queries.

Phases 3 and 4 run in one high-agency pass without check-ins, once Phase-2 scope is set. Phase 1 → Phase 2 is the decision boundary; after that, drive to completion.

**What not to do during ingest:**
- Don't produce a single summary page per source — that means not enough work was done.
- Don't create wiki pages from undiscussed material.
- Don't silently resolve contradictions with existing wiki content.
- Don't skip the Phase-1 exhaustive read — "I'll catch the important stuff as I go" reliably produces incomplete wiki pages.
- Don't use qmd as a substitute for reading in Phase 1.
- Don't condense the Phase-1 notes file before Phase 2 — hand over the detail, let the user pick what matters.

### Query

The user asks a question against the wiki. Search for relevant pages — qmd first for any conceptual question, grep when the query names a specific string — then read the top hits in full and synthesize an answer with references to specific pages. If the answer produces valuable synthesis, offer to file it as a wiki page.

### Maintenance

Periodic health checks that produce concrete actions.

**Connectivity audit.** Grep for literal link structure; qmd for the concepts that *should* link. A page can have zero inbound wikilinks yet be deeply related to many pages by idea — qmd catches that, grep cannot.
- Orphan pages (zero inbound links) — grep, then qmd the orphan's core concepts to find pages that should link back.
- Red links (wikilinks to non-existent pages), prioritized by link count — grep.
- Weak nodes (1–2 connections that should have more) — qmd the page's concepts; mismatches reveal missing links.
- Missing bidirectional links — grep.

**Coherence audit.** qmd is the primary tool here: semantic similarity across pages is how contradictions and staleness surface.
- Contradictions between pages — qmd for shared concepts, then read candidates for tension. Flag for discussion, don't resolve silently.
- Staleness — pages not updated despite newer sources touching their concepts. qmd the new source against the whole wiki to find which old pages it touches.
- Depth check — stubs where the wiki now has enough material to say more. qmd the stub's concepts to gauge coverage.

**Expansion audit.** qmd-first — this is a "what ideas are under-served" question.
- Concepts appearing frequently across pages without their own page — qmd candidate concepts against the wiki; high hit-count without a dedicated page = expansion candidate.
- Theory areas the persona system depends on but the wiki hasn't covered.
- Code TODOs that map to wiki research gaps.
- Cited sources that would fill known gaps.

**TODO scan:**
- Grep the codebase for `#TODO` comments
- Compare against `development/open-questions.md`
- Flag new TODOs not yet tracked
- Flag questions where wiki research is sufficient to write a development plan

## TODO Integration

TODOs in the code represent understanding gaps. The wiki tracks and works toward answering them.

**Lifecycle:** TODO in code -> open question in wiki -> wiki research during ingest -> development plan -> code change -> TODO resolved.

## Development Plan Guidelines

Plans in `development/` are the wiki's ultimate output — documents complete enough for a fresh Claude Code session to pick up and execute. The format is flexible, but a fresh session needs:

**Theoretical grounding.** Which theory pages to read and what key claims drive the design decisions. Reference, don't duplicate.

**Motivation.** What open question(s) or TODO(s) this plan addresses, and why wiki research is now sufficient to act.

**Current state.** What the relevant code looks like now — specific files and what they do.

**Design decisions.** What was decided and why, stated as constraints and interfaces rather than implementation code.

**Scope boundaries.** What's in scope and what's explicitly not.

**Verification.** How to know the work is done.

## Deep-end discipline

The wiki's sources run deep into continental theory — Deleuze & Guattari, Bergson, Jung, Husserl, Merleau-Ponty, and the rest. Use these deep-end concepts to *find interesting angles*: they are generative for discovering good designs for the persona system's machines. But a machine, once designed, should not *need* the concept to function. A finished machine should be specifiable and operable in concrete, surface-level terms; the theory records where it came from and why it is interesting, not how it runs.

The test: if a proposed machine cannot be described without invoking the concept that inspired it, it has gone too far off the deep end — pull it back to something concrete. Worked example: the Perception category's noticing machines were first drafted as abstract concept-detectors (faciality-noticing, haecceity-noticing) and pulled back to granular surface detectors (length-shift, hesitation, hedge-pile) that work without the theory. The theory survives only as a cited *anchor* — provenance, not operating instructions. See `development/desiring-machines-redesign-sketch.md`.

Theory is the ladder; kick it away once the machine stands.

## Constraints

- **Never modify files in `raw/`.**
- **Never create wiki pages from undiscussed material.** Everything in the wiki should emerge from conversation between the user and LLM.
- **Never silently resolve contradictions.** Flag them for discussion.
- **Always update bidirectional links** when creating or modifying pages.
- **Always update `index.md` and `log.md`** after any wiki modification session.
