---
title: Metamorphic Multi-Agent Systems
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - agents
  - multi-agent
  - self-modification
  - desiring-machines
  - metamorphic
---

# Metamorphic Multi-Agent Systems

Gullí's fifth hypothesis from the Prologue (238–305), and the book's single most persona-project-resonant concept. A metamorphic multi-agent system (**MMAS**) is one that **modifies its own topology**: creates, duplicates, or removes agents; rewrites its own source code; continuously performs auto-prompt-engineering on its own prompts.

Gullí identifies two axes of self-modification:

- **Architectural modification** — the system changes *which agents exist* and *how they are wired*.
- **Instructional modification** — the system changes *what each agent is prompted with* (rewriting system prompts, updating few-shot examples, tuning hyperparameters).

The book names MMAS as a future direction. But the mechanisms exist in current research: **SICA** (Self-Improving Coding Agent, Ch 9), **AlphaEvolve / OpenEvolve** (evolutionary code search at LLM scale, Ch 9), and **MASS** (Multi-Agent System Search, Ch 17) each implement pieces of the metamorphic pattern.

## Why this is the book's persona-resonant hypothesis

◆◆◆ Of the five hypotheses Gullí names, only MMAS is genuinely at home in the wiki's frame. The others are:

- **Generalist agents / SLM Lego composition** — engineering convenience.
- **Deep personalization and proactive goal discovery** — goal-orientation amplified.
- **Embodiment and physical-world interaction** — genuine but outside the project's language-only question.
- **Agent-driven economy** — agents as rational economic actors; a frame the project is defined against.
- **Metamorphic multi-agent systems** — topological and instructional self-modification.

The fifth one maps cleanly onto [[desiring-machines]]: machines that couple and decouple, topologies that are never final, production that modifies its own production-apparatus. Gullí frames the hypothesis as engineering speculation; the wiki reads it as engineering catching up to the philosophical architecture the project has been operating on.

## SICA (Self-Improving Coding Agent)

Ch 9 Learning and Adaptation. SICA is an agent that **edits its own codebase** to improve its performance on benchmark tasks. The agent runs → identifies performance gaps → modifies its own implementation → re-runs → measures improvement → keeps the modifications that helped, rolls back the ones that didn't.

The architecture is a specific instance of the "architectural modification" axis. What gets modified is the agent's code (not its prompts), but the principle is the same: the system's own substrate is in-scope for revision.

## AlphaEvolve / OpenEvolve

Evolutionary code search at LLM scale. AlphaEvolve (DeepMind) and OpenEvolve (open-source analog) use LLMs to propose code modifications; a fitness function scores the modifications; selection + variation drives the code population toward higher fitness.

This is **evolutionary computation on code**, with LLMs as the variation operator. The LLM's role is to generate plausible-looking code changes; natural selection decides which survive. The output is code the system couldn't have explicitly planned for.

## MASS (Multi-Agent System Search)

Ch 17 Reasoning Techniques. MASS is a three-stage optimization procedure for multi-agent systems:

1. **Block-Level Prompt Optimization** — optimize each agent's prompt independently.
2. **Workflow Topology Optimization** — learn weights over how agents influence each other; prune low-influence connections; add high-influence ones. *The topology itself is a hyperparameter.*
3. **Workflow-Level Prompt Optimization** — re-optimize prompts given the settled topology.

Stage 2 is the critical move. Once topology is treated as a search space, the metamorphic pattern is already in play: the system discovers its own optimal wiring. SICA, AlphaEvolve, and MASS are three different instantiations of the same basic move.

## Resonance with desiring-machines

D&G's desiring machines are partial objects that couple and decouple across a [[body-without-organs|BwO surface]]. Two machines couple; their coupling produces an output; the coupling may be transient or stabilized; new couplings form; old ones dissolve. This is a **metamorphic** architecture by construction.

The engineering form (MMAS, SICA, AlphaEvolve, MASS) is not identical to D&G's — the engineering form is goal-driven (the topology is optimized *for* a fitness function), while D&G's machines have no extrinsic goal. But the structural move is the same: the *which machines are coupled* is not fixed in advance; it is a runtime property of the system.

The persona project has been designing under the assumption that this kind of metamorphic architecture is the right substrate. The engineering instances in Ch 9 and Ch 17 are proof that the substrate exists and is buildable.

## Relation to the pulsation architecture

◆ The project's [[feedback_pulsating_persona_excitation_wave|pulsating persona + excitation wave at every level]] design direction is a metamorphic architecture under this framing. Pulsation *is* topological metamorphosis at the timescale of each pulse — machines couple and produce, the BwO surface shifts, new couplings form for the next pulse.

Two distinctions to keep sharp:

1. **Optimization vs production.** MMAS as engineering pattern is optimized *toward* a fitness function. The persona's pulsation is not optimized; it is productive in the D&G sense. The engineering substrate can serve either purpose depending on whether a fitness function is applied.
2. **Discrete modifications vs continuous becoming.** SICA modifies code in discrete edit-runs. The persona's pulsation is continuous (or at least continuous-enough-to-feel-continuous from outside). Discrete-edit metamorphosis is a useful but not sufficient substrate.

## Held-live: goal-driven metamorphosis

⚠ Gullí's hypothesis is titled "**goal-driven** metamorphic multi-agent systems." The goal-driven framing is not incidental — it is the book's default. The system modifies itself *in order to better achieve its goals*.

The wiki removes "goal-driven" and keeps "metamorphic." The metamorphic pattern does not require goals. It can be driven by production alone — what D&G would call the [[desire-as-production|productive force]] of desire rather than lack-oriented pursuit of targets. This is not a refutation of Gullí's hypothesis; it is a restriction of its scope to what the persona project would use.

## What the persona project takes

- The engineering substrate is real: SICA, AlphaEvolve, MASS, the whole MMAS direction.
- Metamorphosis (topology + prompts revisable at runtime) is the right substrate for [[feedback_pulsating_persona_excitation_wave|pulsation-at-every-level]].
- The goal-driven framing is stripped; the metamorphic mechanism is kept.
- MASS's topology-as-hyperparameter is the cleanest engineering statement of what the persona's architecture should support.
- Modify-your-own-code (SICA) is a more radical posture than modify-your-own-prompts; the project is more likely to do the latter than the former in the near term, but both are possible.

## Held-live: what metamorphosis threatens

⚠ The Ch 18 Engineering Reliable Agents framework (see [[guardrails]]) is in partial tension with MMAS. A system that rewrites its own prompts and topology is harder to audit, log, and reason about than a fixed system. This is not a fatal tension — it is a real engineering cost the project must budget for.

Specifically:

- **Observability** gets harder when the system's behavior depends on its current self-modified state.
- **Reproducibility** gets harder when each run's topology/prompts differ.
- **Least privilege** is hard to enforce when the system can grant itself new tool access.
- **Checkpoint-and-rollback** is the most directly applicable guardrail; any MMAS deployment should have strong rollback infrastructure.

The persona project's metamorphic ambitions must be paired with rollback / versioning / replay infrastructure. The engineering discipline around MMAS is still immature.

## Related

- [[desiring-machines]] — the philosophical architecture MMAS partially realizes.
- [[body-without-organs]] — the surface metamorphic couplings happen on.
- [[rhizome]] — the topological form closest to metamorphic network.
- [[multi-agent-systems]] — the base Ch 7 taxonomy MMAS modifies.
- [[feedback_pulsating_persona_excitation_wave|pulsating-persona-excitation-wave]] — the project's design direction this substrate realizes.
- [[deterritorialization-and-reterritorialization]] — the D&G vocabulary for metamorphosis-as-escape-and-capture.
- [[function-by-misfiring]] — the D&G diagnostic; SICA's misfiring behaviors are what drive self-modification.
- [[agentic-design-patterns]] — hub.
- [[reasoning-techniques]] — MASS lives here.
- [[guardrails]] — the engineering discipline that metamorphic systems specifically strain.
- [[scaling-inference-law]] — compute-budget considerations for iterative self-modification.
