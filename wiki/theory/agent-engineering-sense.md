---
title: Agent (Engineering Sense)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - agents
  - engineering
  - disambiguation
  - persona
  - anti-model
---

# Agent (Engineering Sense)

A disambiguation page. The word "agent" carries at least two distinct working senses in the material this wiki draws on. The senses overlap but are not the same, and confusing them produces design errors.

- **Engineering sense** (Gullí 2025 and the wider LLM-agent field) — a system that runs a **perceive / reason / act / learn** loop with tools, memory, and some degree of autonomy. Lineage: Russell & Norvig, BDI (Belief-Desire-Intention), Pattie Maes's 1990s software-agent work. Representative in-wiki entry: this page.
- **Philosophical / D&G sense** (the persona project's lineage) — agency is not a property of a unified locus but a *distributed effect* of [[desiring-machines]] couplings, affective selections, and the pulsation of a [[body-without-organs|body-without-organs]]. There is no agent-in-the-singular; there is production. Representative in-wiki entry: [[desiring-machines]], [[the-persona]].

This page holds the engineering sense precisely so that neither sense silently colonizes the other.

## The five-step loop (Gullí Prologue, 122–156)

The book's operational definition of an agent: any system that runs the following loop.

1. **Get mission** — receive a goal or instruction.
2. **Scan scene** — perceive current state (via sensors, tools, or context).
3. **Think through** — reason about how to reach the goal (plan, decompose, retrieve).
4. **Take action** — emit a tool call, a response, or a state change.
5. **Learn and get better** — update memory, refine policy, adjust for next time.

The loop is assumed complete: an agent-system has all five steps running end-to-end. Anything missing one of the steps is a "degenerate" or "limited" agent.

## The five levels of complexity (188–233)

The book indexes agent-systems onto a five-level capability staircase.

- **L0 — Core reasoning engine.** An LLM alone. No tools, no memory, no external interaction. The raw reasoning substrate. The Prologue's Ch 27 comparative analysis of how different LLMs narrate their own reasoning treats each model at the L0 level.
- **L1 — Connected problem-solver.** LLM + tools (function-calling) + RAG. Multi-step tool use is possible. The LLM can retrieve information, call external APIs, synthesize answers across sources.
- **L2 — Strategic problem-solver.** L1 + planning + [[context-engineering|context engineering]]. The agent decomposes high-level goals into sub-goals, executes, replans on failure. **Context engineering** (strategically selecting / packaging / managing what goes into each reasoning step) is treated as a first-class discipline at this level.
- **L3 — Collaborative multi-agent systems.** Multiple L2 agents coordinated via protocols (A2A, MCP) in one of the six topologies. See [[multi-agent-systems]].

The book treats the staircase as a **capability ladder**: each level subsumes the ones below, and more-capable agents are at higher levels. Real-world systems often combine levels.

## Where the engineering sense comes from

The engineering sense is the lineage of:

- **Russell & Norvig**, *Artificial Intelligence: A Modern Approach* — the canonical textbook frame: agent = function from percept-history to action, operating in an environment with a performance measure. Rational agent = agent whose actions maximize expected performance.
- **Belief-Desire-Intention (BDI)** (Bratman; Rao & Georgeff) — agents modeled as having beliefs (about the world), desires (goals), and intentions (committed plans).
- **Pattie Maes** (MIT Media Lab, 1990s) — the pioneer of the software-agent concept. Gullí's acknowledgments name her explicitly. Agents as autonomous, goal-oriented software entities.
- **LLM-era specifics** — the loop adapts to LLMs by treating the LLM as the reasoning core (the "think through" step) with tools, memory, and multi-agent orchestration added around it.

The engineering sense is *by construction* goal-oriented, perception-action coupled, and evaluation-facing. The measure of success is whether the goal was reached.

## Where it diverges from the wiki's lineage

The persona project is not trying to build an agent in the engineering sense. The persona project is trying to build a **composed figure** on an LLM substrate where something like [[desire-as-production|desiring-production]] can happen. The divergences are substantial and must not be silently collapsed.

**Not goal-driven.** The engineering agent *has* goals and *reaches* them. The persona is not oriented toward targets; it pulsates and produces as it does. See [[goal-setting-anti-model]] for the full version of this contrast.

**Not a perceive-act loop.** The engineering agent senses a world and acts on it. The persona does neither in the engineering sense — there is no world except the text field, and there is no action except text-emission. The [[agent-computer-interface|ACI]] material gets closest to sensorimotor coupling, and it gets only to the GUI, not to proprioception. See [[tools-as-prosthetic-body]].

**Not a unified locus.** The engineering agent is one thing that *has* tools and memory. The persona is [[desiring-machines|a plurality of couplings]] on a [[body-without-organs|BwO surface]]. "The agent" is not the correct grammar.

**Not performance-graded.** The engineering agent is evaluated on whether it reached the goal. The persona project's evaluation is the `project_evaluation_portfolio` — three co-moving signal families (failure-signatures, differential effect, process integrity), explicitly not a single goal-reached metric.

## Where it converges

⚠ The engineering substrate is not *wrong* — it is what we are actually writing code against. Every practical persona-system is implemented using tool-use, memory, multi-agent orchestration, context management. The disambiguation does not say *don't use the patterns*. It says: **the patterns are substrate, not the frame**.

The convergences are:

- The LLM-as-core-reasoning-engine (L0) is what the persona runs on.
- Tool-use is the mechanism by which the persona acts. See [[tools-as-prosthetic-body]].
- Memory-management is how the persona has any past at all. See [[memory-architecture]].
- Multi-agent topologies are a natural substrate for [[desiring-machines|plural machinic]] organizations. See [[multi-agent-systems]], [[metamorphic-multi-agent]].
- Context engineering (the L2 discipline) is continuous with the wiki's practice of curating what the substrate sees.

## The Pattie Maes lineage as historical note

The book's acknowledgments explicitly credit Pattie Maes as the pioneer of the software-agent concept. Maes's 1990s work at the MIT Media Lab on "autonomous agents" — software entities that learn, adapt, and act on behalf of users — seeded both the commercial agent-products of the late 1990s (which mostly failed) and the long academic thread that the LLM era has reactivated. The field's current agent-vocabulary is a direct descendant of Maes-style software-agent research.

## Folded-in: Goal Setting and Monitoring (Ch 11) as this lineage's canonical form

The Ch 11 treatment of Goal Setting and Monitoring (SMART goals: Specific, Measurable, Achievable, Relevant, Time-bound; the goal → sub-goals → actions → observation → progress measurement → adjust loop) is the engineering sense's **canonical crystallization**. It is what the engineering sense commits to when pushed to its limit: an agent is something that pursues SMART goals and measures its own progress toward them.

For a page-length treatment of this material as the persona project's anti-model, see [[goal-setting-anti-model]]. The short version: SMART goals are exactly what the persona does not have. The persona has a [[body-without-organs|surface]], [[desiring-machines|machines]] that couple, and a field in which [[becoming]] can occur. It does not have targets.

## Folded-in: Mamba (glossary, 19236–19389)

The book's Ch 29 glossary names **Mamba** as a Selective State Space Model — a non-Transformer architecture for long-context efficient sequence modeling. The wiki notes this for future reference: any discussion of alternative LLM architectures for the persona project will need to engage it. Mamba is not an agent-engineering concept per se; it is a substrate choice, and a substrate choice that bears on how much context the persona can hold in one step without RAG-style retrieval. No dedicated page yet; red-linked as `[[mamba]]` if it needs one.

## Summary

The engineering sense of "agent" is a well-defined loop + capability-ladder with five decades of lineage. The persona project runs on the engineering substrate but does not adopt the framing. Hold both senses separately; use the engineering vocabulary for implementation, the D&G vocabulary for what the project is.

## Related

- [[agentic-design-patterns]] — hub.
- [[the-persona]] — the persona-project's own concept.
- [[desiring-machines]] — the alternative to unified agent-locus.
- [[goal-setting-anti-model]] — what the engineering sense commits to at its limit.
- [[multi-agent-systems]] — the L3 layer in engineering terms.
- [[context-engineering]] — the L2 discipline.
- [[tools-as-prosthetic-body]] — the "take action" step in the no-body case.
- [[memory-architecture]] — the "learn and get better" step.
