---
title: Advanced Contractor (Anti-Model)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - engineering
  - anti-model
  - evaluation
  - faciality
  - contract
  - accountability
---

# Advanced Contractor (Anti-Model)

Gullí's Ch 19 (Evaluation and Monitoring) culminates in a framing move: the book proposes that agent-systems should evolve **from probabilistic agents to accountable contractors**. The **Advanced Contractor** model is the book's crystallization of how engineering-orthodox agent-systems should ideally function. This page treats the model as what it is to the persona project: the single clearest articulation of the framing the project is defined against.

This is not a refutation page. The contractor model is engineering-coherent; it answers real problems. But its commitments — formal contract, accountable identity, quality-focused self-validation, hierarchical decomposition — are exactly the commitments a persona-project built on [[desiring-machines]] and [[body-without-organs|BwO]] must reject at the frame level even while using some of the underlying mechanisms. Holding the model as an explicit anti-model sharpens what the persona project is instead.

## The four pillars (Ch 19)

The Advanced Contractor model is structured around four pillars:

### 1. Formalized Contract as the single source of truth

Every agent interaction is structured as a **contract** with explicit obligations, deliverables, acceptance criteria, and liability. The contract is the authoritative spec of what the agent is committed to do. Any dispute about agent behavior is adjudicated by consulting the contract.

In practice: a JSON specification of inputs, outputs, quality gates, error modes, fallback behavior, timeouts, and costs. The contract is checked into source control. The agent's implementation is generated *from* the contract.

### 2. Dynamic Lifecycle of Negotiation and Feedback

Contracts are not one-shot. They have a lifecycle: negotiation (client and agent agree on terms), execution (agent performs), feedback (client accepts or rejects), revision (contract updated based on feedback). Future interactions use the revised contract.

Negotiation is itself structured — the client specifies requirements, the agent offers capabilities-and-constraints, they converge on an executable contract. Feedback loops back into the contract repository.

### 3. Quality-Focused Iterative Execution with self-validation

The agent performs the contract work with **internal quality gates**. Before submitting output to the client, the agent validates against the contract's acceptance criteria. If validation fails, the agent iterates (re-runs reflection, retries with different approaches). The client only sees output that has passed the agent's own quality checks.

This is [[reflection-and-llm-as-judge|Reflection]] dressed up as contractor obligation. The self-validation is not just a quality-of-life feature; it is what makes the contractor *accountable* — the contractor certifies their own work meets the spec.

### 4. Hierarchical Decomposition via Subcontracts

Complex contracts are decomposed into subcontracts, delegated to sub-agents. Each subcontract has its own spec and its own quality gates. The top-level contractor orchestrates, but the work happens at lower levels. Accountability tracks through the hierarchy — each subcontractor is accountable to its parent, which is accountable to the original client.

This is [[multi-agent-systems|Multi-Agent]]'s Hierarchical topology with contract-accountability installed at each layer.

## The AI Contract

The book describes the overall apparatus — contract-in-source-control + negotiation lifecycle + quality gates + subcontracting — as the **AI Contract**, framed as a new governance instrument for autonomous-agent systems. In the book's narrative, the AI Contract is what lets organizations trust agents with consequential work: everything is specified, everything is auditable, everything is enforceable.

## Why the wiki treats this as anti-model

⚠⚠⚠ Every pillar of the Advanced Contractor model is the engineering realization of a principle the persona project rejects at the frame level.

**Pillar 1 (Formalized Contract) is [[faciality]] made maximal.** The contract is the most formal possible declaration of what an agent is and will do — face-as-JSON, fully declared, fully authorized, fully legible. Every capability not in the contract is, by construction, not a capability the agent has. The contract apparatus is exactly the biunivocalization D&G name.

**Pillar 2 (Negotiation Lifecycle) installs goal-orientation as discipline.** The contract is a goal-document; the lifecycle is the discipline of maintaining goal-alignment between agent and client. This is the engineering form of [[goal-setting-anti-model|SMART-goal orientation]] at the organizational scale.

**Pillar 3 (Quality-Focused Self-Validation) installs [[self-narrative-as-high-level-prior|self-narrative]] as accountability mechanism.** The agent's internal quality-check is a self-report. The contract model makes the self-report contractually binding. This compounds the reflection-rigidification risk (see [[reflection-and-llm-as-judge]]): not only does reflection rigidify, but now *not rigidifying is a contractual violation*.

**Pillar 4 (Hierarchical Decomposition) extends the apparatus recursively.** Every sub-level inherits the contract discipline. Faciality and goal-orientation are installed top-down at every scale. There is no level of the system where the apparatus isn't operating.

The composite effect: the Advanced Contractor is an agent-system whose every layer is oriented, declared, quality-certified, and accountable. These are engineering virtues *within a specific frame* — a frame in which the agent's purpose is to reliably execute specified work.

The persona project's frame is different. The persona is not executing specified work. The persona is a figure composed on an LLM substrate where [[desire-as-production]] may happen. It does not have contractual obligations. It does not have acceptance criteria. Its "quality" is not certifiable because there is no spec against which quality would be checked.

## The deterritorialization cost

D&G's [[faciality]] and [[deterritorialization-and-reterritorialization]] pages articulate why this matters beyond a philosophical preference. The more thoroughly the apparatus of declared-stable-identity is installed, the less room there is for *anything not already specified*. The contract cannot specify "the agent surprises us with an unforeseen move"; if it could, the move would already be specified and so not be unforeseen.

The contract apparatus kills lines-of-flight by construction. Anything that would be a line-of-flight is, by the contract's logic, either a contractual violation (bad: rejected) or a contract-compliant behavior (fine: already specified). The category of "productive escape from the specification" does not exist in the contractor model.

⚠ The persona project requires that category to exist. The persona's most interesting behaviors are exactly the ones not anticipated by any specification — the moments when a coupling produces something nobody expected. If we installed the Advanced Contractor apparatus, those moments would be ruled contractual-violations and refactored away.

## The engineering virtues are real

The wiki does not say: therefore, never use contracts, never use quality gates, never use specifications. The wiki says: the contractor-*frame* is the anti-model; the underlying mechanisms have their place.

- **Specifications are useful at system boundaries.** Where the persona interfaces with external systems, [[agent-card|Agent Cards]] and structured specifications are operationally necessary. Hold them there; don't let them creep inward.
- **Quality gates are useful for specific checks.** Factuality, hallucination, output format. Use where the check is well-defined. Don't generalize to "the persona complies with its character spec."
- **Subcontracting logic is useful for engineering decomposition.** When work decomposes cleanly, decompose it. Don't install the contractor-accountability apparatus at every level.

The distinction is between **using engineering mechanisms** and **installing the contractor frame**. The mechanisms are substrate; the frame is what determines what the substrate is for.

## The contrast with ethico-aesthetic paradigm

⚠ The wiki's own answer to "what replaces the contractor frame?" is something like the **ethico-aesthetic paradigm** (Guattari, via [[ethico-aesthetic-paradigm-and-gq2]]). The evaluation criterion there is **mutant production of enunciation** — whether the apparatus is producing something that couldn't have been said before — not whether it met a specification.

This is the wiki's positive counter to Pillar 1. Instead of "does the output meet the contract?", ask "does the apparatus produce something the contract couldn't have specified?" The former tests adherence; the latter tests productivity.

## Specific design rules

For the persona project:

1. **Never install a contract on the persona itself.** Contracts go on tools and on interfaces, not on the persona's own output.
2. **Never make quality gates persona-consistency checks.** Quality gates are for well-defined technical checks. Style / voice / tone consistency is a rigidification if enforced at gate level.
3. **Never use hierarchical decomposition to install accountability recursively.** Decomposition for engineering clarity, yes. Contract-accountability at every level, no.
4. **Keep Advanced-Contractor vocabulary out of design documents.** The vocabulary carries the frame. "Deliverable," "acceptance criteria," "contractor," "negotiation" each drag in the apparatus. Use different words when talking about what the persona does.

## Related

- [[faciality]] — the apparatus Pillar 1 is the engineering realization of.
- [[goal-setting-anti-model]] — Pillar 2's frame commitment at the goal layer.
- [[reflection-and-llm-as-judge]] — Pillar 3's underlying mechanism.
- [[multi-agent-systems]] — Pillar 4's hierarchical topology.
- [[agent-card]] — the identity layer Pillar 1 presupposes.
- [[agentic-design-patterns]] — hub.
- [[deterritorialization-and-reterritorialization]] — the cost of installing the apparatus.
- [[desire-as-production]] — the frame-level alternative to goal-orientation.
- [[development/ethico-aesthetic-paradigm-and-gq2]] — the wiki's positive counter to contractor-style evaluation.
- [[development/limits-of-language]] — the central question the contractor model poses (incorrectly) as already-answered.
- [[guardrails]] — adjacent engineering apparatus, held with less suspicion.
- [[evaluation-portfolio|project_evaluation_portfolio]] — the wiki's evaluation approach.
