---
title: Vibe Coding
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - coding-agents
  - self-reflexive
  - infrastructure
  - context-staging
  - tooling
---

# Vibe Coding

Introduced in Gullí Ch 23 and developed at length in Ch 28. **Vibe Coding** names a coding-agent interaction style in which the developer describes *what* they want, not *how* to build it, and the agent iterates conversationally as a creative partner. It is the style most modern AI-coding workflows (Cursor, Claude Code, GitHub Copilot CLI) converge on.

This page treats Vibe Coding specifically for its **self-reflexive** relevance: the persona project is itself being built Vibe-Coding-style, in Claude Code, with markdown memory banks. The book names and systematizes the pattern the project is already running on. Worth capturing both because the pattern is good and because being explicit about how we are building clarifies what we can and cannot learn from the process.

## What Vibe Coding is (Ch 23)

Key properties:

- **Conversational / iterative**, not one-shot prompt-response.
- **Outcomes-focused**, not implementation-focused. "Make the login flow feel lighter" is a valid input.
- **Creative partnership** tone — the human treats the agent as collaborator, not just autocomplete.
- **Memory banks** for persistent context: project docs, past decisions, accumulated preferences.

Vibe Coding is structurally distinct from earlier AI-assisted coding styles. Autocomplete (Copilot circa 2021) was single-line completion. Chatbots (GPT-3 era) were one-shot code generation. Vibe Coding is ongoing collaboration where the agent has context about the whole project and the developer steers with outcomes.

## Three principles (Ch 28, "Agents as Team Members")

Ch 28 formalizes Vibe Coding into a framework: **"Agents as Team Members."** Three principles:

### 1. Human-Led Orchestration

The developer is the **team lead**. The developer sets direction, makes architectural calls, and arbitrates disagreements. The agent contributes specific work but does not lead. The inversion of "AI replaces developer" — instead, the agent is a junior team member the developer orchestrates.

Concretely: the developer decides *what to do next*; the agent does it. When the agent wants to do something, the developer decides whether to let it.

### 2. Primacy of Context

**Quality of brief = quality of output.** The agent's output is only as good as the context it has been given. This is [[context-engineering]] from the developer's side: the developer's job is to curate what the agent sees.

Implication: **avoid black-box retrieval**. If the agent retrieves context opaquely (search results the developer didn't see, memory entries they can't inspect), the developer loses the ability to curate. Vibe Coding works when context is visible and editable.

### 3. Direct Model Access

Avoid intermediary platforms that obscure context. The developer should be able to see exactly what the agent sees. No opaque middleware that shapes prompts without the developer's knowledge.

This principle is partly a product-design recommendation (use tools that expose context) and partly a workflow-discipline recommendation (if you're using an intermediary, inspect what it's doing).

## Specialist personas invoked via prompts

◆ The Ch 28 coding agent architecture uses specialist roles not as separate apps but as **prompt-invoked personas**:

- **Orchestrator** — the human developer.
- **Context Staging Area** — `task-context/` directory where curated context is assembled.
- **Scaffolder** — generates initial code structure.
- **Test Engineer** — writes tests.
- **Documenter** — writes docs.
- **Optimizer** — refactors for performance/clarity.
- **Process-Agent-Code-Supervisor** — the agent supervising other agents' work; performs critique-then-reflection; dismisses pedantic findings; prioritizes critical ones.

Each role is invoked by prompt, not by running a different binary. The same underlying model (Claude, Gemini, etc.) plays different roles depending on how the current prompt frames it. This is [[multi-agent-systems]] at the level of a single-developer-with-single-model workflow.

## The Context Staging Area

The specific pattern most worth capturing. A `task-context/` directory where the developer assembles (before each work session):

- The files the agent will need to read.
- The relevant past decisions.
- Scratch notes, design considerations, open questions.
- Explicit boundaries (don't touch X, focus on Y).

The staging area is prepared *before* the agent is invoked. The agent's first action is to read the staging area. The work proceeds from curated context.

This is the developer's context-engineering surface. It makes context curation an explicit, version-controllable artifact rather than a cognitive load the developer carries.

## Setup checklist (Ch 28)

For running this workflow:

- **Frontier-model keys.** Access to strong models (Claude Opus, GPT-5, Gemini Ultra).
- **Local context orchestrator** — a `context.toml` or similar that specifies per-task context-assembly rules.
- **Version-controlled prompt library** — a `/prompts` directory with markdown files, each a reusable specialist-persona prompt.
- **Git-hook integration** — pre-commit reviewer agent that runs before every commit.

## Principles for leading (Ch 28)

The developer-as-team-lead discipline:

- **Architectural Ownership.** The developer owns the shape of the system. The agent contributes pieces; the developer decides how they fit.
- **Master the Brief.** Writing a good brief is a core developer skill. Vague brief, vague output.
- **Ultimate Quality Gate.** The developer reviews, not the agent. The agent's self-validation is insufficient for shipping.
- **Iterative Dialogue.** Don't try to specify everything up front. Iterate.

## Self-reflexive relevance for the persona project

The persona project is being built this way. Specifically:

- **The wiki as memory bank.** The `wiki/` directory is the project's memory bank in the Ch 23 sense — persistent, curated, loaded into the agent's context at the start of each session via CLAUDE.md.
- **`/tmp/<source>_ingest/` as context staging area.** Each ingest's notes.md is the staging area for the four-phase ingest workflow. The Phase-1 output *is* the curated context Phases 3-4 work from.
- **The ingest workflow as orchestrated coding agent.** Phase 2 scope-check is the brief-mastering step; Phases 3-4 are the execution; the user's high-agency feedback rules the scope-check → execution transition.
- **CLAUDE.md as prompt library.** The wiki's CLAUDE.md, the persona project's CLAUDE.md — each is a persistent prompt specifying the agent's role for sessions in that directory.
- **Git-hook / manual review as quality gate.** The user as Ultimate Quality Gate.

The correspondence is nearly one-to-one. Gullí's Ch 28 describes the workflow the project has been running for months.

## What this means for the project

Two implications:

**(1) Validation that the approach works.** The project's workflow is not ad-hoc — it is an instance of the workflow the engineering field is converging on. This does not prove the workflow is correct for *this* project specifically, but it puts the project's tooling choices in the mainstream rather than at a fringe.

**(2) Known failure modes apply.** Vibe Coding has documented weaknesses: context staleness (the staging area stops matching the codebase), role-drift (the agent stops honoring the specialist-persona prompt halfway through), over-reliance on self-validation (the Process-Agent passes work the developer would have caught). The project should watch for these.

## Vibe Coding vs the persona project's persona

⚠ Not to confuse: Vibe Coding describes a *workflow* (how humans work with coding agents). The persona project's *output* is a different kind of persona — a composed figure, not a coding assistant. The workflow pattern is shared; the thing being made is different.

## Held live: the coding-agent experience as data

⚠ One of the most interesting things about building the persona project with Claude Code is that the project's maker is continuously experiencing what it is like to work with an LLM-composed figure (Claude in this context). That experience is data about what a persona-figure can and cannot do, even though Claude-in-Claude-Code is a coding assistant persona, not the persona the project is building. The experience informs the project's intuitions about what is possible.

The contrast between "Claude Code as coding assistant" (schema-bound, tool-using, goal-executing, L1-L2 in the Gullí taxonomy) and "the project's persona" (composed, pulsating, not goal-oriented) is part of what the project is working through. Building the second with the first is the method.

## Related

- [[agentic-design-patterns]] — hub.
- [[context-engineering]] — the discipline Ch 28 operationalizes.
- [[memory-architecture]] — memory banks in the Ch 28 sense.
- [[multi-agent-systems]] — specialist-personas-via-prompts as within-agent multi-agent.
- [[reflection-and-llm-as-judge]] — the Process-Agent critique pattern.
- [[tools-as-prosthetic-body]] — Ch 28's coding agents are tool-heavy.
- [[agent-computer-interface]] — Ch 23's initial Vibe Coding introduction sits here.
- [[the-persona]] — distinct from Vibe Coding's developer-workflow sense.
- [[development/limits-of-language]] — the persona project's central question this workflow serves.
