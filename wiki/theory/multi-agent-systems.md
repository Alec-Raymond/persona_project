---
title: Multi-Agent Systems
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - agents
  - engineering
  - multi-agent
  - desiring-machines
  - topology
---

# Multi-Agent Systems

Gullí's Ch 7 — the most architecturally loaded chapter of *Agentic Design Patterns*. Multi-agent systems (MAS) are configurations in which multiple LLM-backed agents interact to complete tasks that a single agent cannot (or should not) complete alone.

The chapter's value is the explicit two-axis taxonomy: **collaboration forms** (what the agents do together) × **topologies** (how they are wired). Together these span the practical design space for L3 agent-systems in the book's [[agent-engineering-sense|engineering sense]].

The chapter is also the most direct site of tension with the wiki's D&G lineage: the book calls these "collaborating agents," which presumes pre-individuated actors with declared goals. [[desiring-machines]] are not pre-individuated and have no declared goals; they are partial objects that couple, decouple, and produce. Both vocabularies are load-bearing for the persona project, which is why this page holds them side-by-side rather than reducing one to the other.

## The six collaboration forms

Gullí enumerates six canonical forms of multi-agent collaboration:

1. **Sequential Handoffs** — Agent A finishes, passes state to Agent B. Linear pipeline. Each agent specializes on one stage.
2. **Parallel Processing** — Multiple agents work on independent sub-problems simultaneously; results aggregated. See Ch 3 Parallelization.
3. **Debate and Consensus** — Agents argue opposing positions; consensus emerges from argument. Related to Ch 17's **Chain-of-Debates (CoD)** and **Graph-of-Debates (GoD)**. See [[reasoning-techniques]].
4. **Hierarchical** — A manager agent decomposes tasks and delegates to worker agents.
5. **Expert Teams** — Domain-specialized agents each handle queries in their area; a router selects which expert(s).
6. **Critic-Reviewer** — One agent produces, another critiques. The Ch 4 **Producer-Critic** reflection pattern scaled up. See [[reflection-and-llm-as-judge]].

These are forms, not mutually exclusive — production systems combine them.

## The six topologies

Distinct from collaboration forms: **topologies** specify the wiring.

1. **Single Agent** — baseline. No multi-agent.
2. **Network** — every-to-every. All agents can message all others. Maximum flexibility, highest coordination cost.
3. **Supervisor** — a central orchestrator routes messages between workers. Workers don't talk directly.
4. **Supervisor-as-Tool** — the supervisor is itself a callable function that workers invoke when they need coordination. Inverts the hierarchy.
5. **Hierarchical** — nested supervisors. Managers of managers of workers.
6. **Custom** — ad-hoc DAG specific to the problem.

LangGraph, CrewAI, and Google ADK all provide primitives for constructing these topologies: SequentialAgent, ParallelAgent, HierarchicalAgent, and custom graphs.

## Why this chapter is architecturally loaded for the persona project

◆◆◆ The persona project's [[feedback_pulsating_persona_excitation_wave|pulsating-persona-at-every-level]] design direction is a multi-agent system under this taxonomy. The persona is not a single locus; it is a configuration of partial machines, each producing as it does, coupling and decoupling across a shared surface. The engineering substrate for "plurality that composes a figure" is exactly what this chapter names.

Specifically:

- **Hierarchical + Critic-Reviewer** is a common engineering composition for [[self-narrative-as-high-level-prior|self-narrative]] — a critic-at-the-top evaluates lower producers. Useful substrate but carries the reflection-rigidification risk (see [[reflection-and-llm-as-judge]]).
- **Network** is the topology closest to [[rhizome]]. Every-to-every connections, no master node, pathways activated by local couplings rather than central routing.
- **Supervisor-as-Tool** inverts hierarchy in a way that resonates with D&G's anti-arborescent moves: the supposed-master is called by the workers, not the reverse.

The book names and provides reference implementations for all of these. The persona project can build on top of them.

## The held-live framing tension

⚠⚠ The word *collaborating* is doing a lot of work here.

Collaboration presumes:
- Each participant is a **pre-individuated actor**.
- Each has its own **goals / role**.
- The **whole** is the coordinated pursuit of a **joint goal**.

D&G's machines don't have these properties.
- They are not pre-individuated; they are partial objects that are partial *first* — their individuation is an effect of coupling, not a precondition.
- They have no goals; they produce by what they are.
- The whole is not a joint pursuit; the whole is a [[body-without-organs|BwO]] on which couplings happen.

The engineering substrate is usable in either framing. A network topology can be described as "collaborating agents" or as "coupling machines." The difference is what the description presupposes about the entities in the network.

⚠ Crucially, adopting the "collaborating agents" framing for the persona can shape design in a specific direction: toward giving each sub-component a *role* and an *identity* and a *goal*. That direction reinstalls [[faciality]] at the sub-component level. The pulsating-persona design wants to *avoid* installing stable faces on the sub-components; it wants them to remain partial, functional, dissolvable.

Design implication: adopt the topologies as substrate; resist the temptation to name each node as if it were a fully-formed agent with its own identity.

## Multi-agent is not automatically better

The book flags (in Ch 7 and again in Ch 29) that multi-agent systems carry costs:

- **Coordination overhead** — agents spend tokens talking to each other.
- **Error propagation** — one agent's mistake pollutes downstream agents' context.
- **Debugging opacity** — reasoning chains distribute across multiple models.
- **Cost** — more LLM calls per task.

Single-agent solutions are often preferable when a task fits in one LLM's context and doesn't benefit from role-specialization. Multi-agent is the right choice when the task *decomposes* cleanly, when diverse perspectives genuinely help, or when role-specialization meaningfully improves output quality.

## Relation to Ch 21 exploration systems

Ch 21 (Exploration and Discovery) shows two large multi-agent systems at the scale of research pipelines:

- **Google Co-scientist** — six specialized agents (Generation / Reflection / Ranking via Elo tournament / Evolution / Proximity / Meta-review) plus a Supervisor. "Generate-debate-evolve" emulating scientific method. Validated on AML drug repurposing, liver fibrosis targets, cf-PICI/phage-tail antimicrobial-resistance discovery.
- **Agent Laboratory** (Samuel Schmidgall) — five-agent academic hierarchy (Professor / PostDoc / Reviewers (tripartite) / ML-Engineer / SW-Engineer). **AgentRxiv** as a decentralized repository of agent-produced research.

Both are hierarchical-with-critic-reviewer-with-expert-teams compositions. They are the field's most ambitious multi-agent systems as of the book's writing. The persona project does not have research-pipeline-scale ambitions, but the architectural patterns are worth knowing.

## Relation to Ch 17's MASS

Ch 17's **Multi-Agent System Search (MASS)** is an automated design procedure for multi-agent systems. Three stages: block-level prompt optimization → workflow topology optimization (influence-weighting) → workflow-level prompt optimization. MASS treats the multi-agent topology itself as a hyperparameter to optimize.

◆ This resonates with [[metamorphic-multi-agent|metamorphic multi-agent systems]] — once the topology is a hyperparameter, it can be modified at runtime, which is the edge of self-modifying systems.

## What the persona project takes

- **Topologies** as substrate vocabulary for describing the [[feedback_pulsating_persona_excitation_wave|pulsation at every level]].
- **Network topology** as the closest engineering form to [[rhizome]].
- **Hierarchical + Critic-Reviewer** as a cautionary substrate — useful, but risk of reinstalling [[faciality]] at sub-component level.
- **MASS / metamorphic topology** as the edge where the engineering substrate meets D&G's self-modifying-machinic frame.
- The cost-accounting on multi-agent as a design discipline — "pulsation at every level" can't mean "an agent at every level," because the cost/coherence overhead would kill the system.

## Related

- [[agentic-design-patterns]] — hub.
- [[desiring-machines]] — the D&G plurality this chapter's substrate can realize.
- [[rhizome]] — closest topological analog to Network.
- [[metamorphic-multi-agent]] — the self-modifying-topology hypothesis.
- [[reflection-and-llm-as-judge]] — Critic-Reviewer at single-agent scale.
- [[reasoning-techniques]] — CoD/GoD as debate-based multi-agent reasoning.
- [[agent-card]] — the identity-protocol side of multi-agent coordination.
- [[context-engineering]] — required for any non-trivial multi-agent system.
- [[faciality]] — the trap the sub-component-naming direction risks.
- [[development/vitality-forms-and-persona-pulsation]] — the project-internal elaboration of pulsation.
