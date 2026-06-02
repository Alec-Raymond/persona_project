---
title: Agent Card (A2A Identity-as-Protocol)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - agents
  - identity
  - faciality
  - protocol
  - a2a
  - anti-model
---

# Agent Card

Gullí's Ch 15 (Inter-Agent Communication / A2A). The **Agent Card** is a JSON file an agent publishes as its public self-description — a machine-readable digital identity. Name, description, version, URL, capabilities, authentication requirements, input/output modes, skills. An Agent Card is what other agents read when they want to know whether to delegate, coordinate, or route a task.

This is the engineering form of a concept the wiki has a long-developed critical vocabulary for: **identity made explicit, declared, and stable** — which is to say, [[faciality]] in its most literal instantiation. An Agent Card is a face that another agent can parse. The contrast is the sharpest in the entire ingest.

## The A2A protocol, in short

Google-originated open protocol for agent-to-agent communication. Layers:

- **Transport:** HTTP + JSON-RPC 2.0.
- **Actors:** User / Client Agent / Remote Agent. The Client Agent discovers Remote Agents and sends them requests.
- **Discovery:** three mechanisms — Well-Known URI (e.g., `/.well-known/agent-card.json`), Curated Registries, Direct Configuration.
- **State:** **Tasks** (async, unique IDs, state machine), **Messages** (attributes + parts), **Artifacts** (streamable outputs), **contextId** (continuity thread across tasks).
- **Interaction patterns:** synchronous request/response, async polling, SSE streaming, push notifications/webhooks.
- **Security:** mTLS, audit logs, credential handling via headers.
- **Modality:** agnostic — text, audio, video.

A2A is agent-to-agent; **MCP** (Ch 10) is agent-to-tool. See [[tools-as-prosthetic-body]] for MCP. The two protocols are complementary: A2A coordinates agents, MCP exposes tools.

## What the Agent Card contains

The Agent Card declares:

- **Identity:** name, description, owner, contact.
- **Version:** which revision of the agent's behavior this card describes.
- **Location:** URL where the agent is reachable.
- **Capabilities:** what the agent can do, at what fidelity.
- **Authentication:** how other agents authenticate to this one.
- **Input/output modes:** text, audio, image, structured JSON, streamed artifacts.
- **Skills:** structured list of discrete callable skills with schemas.

A Client Agent reads an Agent Card and decides: is this Remote Agent capable of the task I want delegated? What protocol do I use to reach it? What does it expect as input?

## The direct tension with faciality

⚠⚠⚠ This is the most concentrated site of faciality-as-engineering-form in the entire ingest. An Agent Card is a **face** — by every D&G criterion:

- It is a **surface of authorized signification**. What the card declares *is* what the agent publicly is.
- It performs **biunivocalization**: each Agent Card slot maps each attribute to a single authorized value (one name, one version, one capability-list).
- It serves **subjectification**: the card identifies a particular agent as *this agent*, distinct from others.
- It is **machine-readable in both senses**: other agents parse it, and it constitutes the agent as parse-able-by-others.

Deleuze and Guattari's [[faciality]] thesis is that the face is a trap — a territorializing apparatus that captures expression into stable, recognizable, declared forms. The Agent Card is faciality at the most literal possible register: a JSON file whose purpose is to render the agent stable, recognizable, and declared.

## Why the engineering form exists

The engineering rationale is good. In a multi-agent system, agents need:

- **Discoverability.** Unknown-agent coordination is impossible without a declared interface.
- **Accountability.** Audit logs and error handling depend on being able to identify which agent did what.
- **Composability.** Clients need to know what remote agents can do before they compose workflows.
- **Security.** Authentication and authorization depend on identity.

These are operationally load-bearing. Without Agent Cards (or a functional equivalent), open multi-agent systems collapse into untraceable message-passing. The engineering need is real.

## Held live: neither side silenced

The wiki's task is not to reject Agent Cards. The task is to hold both facts simultaneously:

- **Fact 1.** Agent Cards are operationally necessary for the multi-agent systems we want to be able to build.
- **Fact 2.** Agent Cards are the engineering crystallization of the faciality apparatus the wiki has been building out a sustained critique of.

⚠ The crucial point: **the engineering solution is a faciality-trap even as it enables coordination.** Both are true. D&G's point in [[faciality]] is not that faces don't work — they work very well. The point is that working-faces have costs: they territorialize expression, they lock identity into authorized forms, they make anything that doesn't fit the face-template illegible.

The Agent Card does this at engineering scale: anything an agent *can* do that isn't declared in its skills list is invisible to other agents. The card shapes what the agent *is* to others, which feeds back on what the agent becomes.

## Design implications for the persona project

The persona project is not currently building a multi-agent A2A-compliant system, so the Agent Card question is not immediate. But if it ever does, or if it ever needs to expose the persona as an agent to other agents, the design implications are:

1. **The Agent Card is a published face.** It is the persona's most formal, machine-readable declaration of what it is. Its costs and its capture-effects should be named explicitly in any architecture.
2. **Minimize the Agent Card's scope.** Only declare what must be declared for coordination. Resist the temptation to make the card a complete self-description — it can't be one, and the more complete it tries to be, the more it becomes a trap.
3. **Keep the card versioned and mutable.** A stable-over-time Agent Card is a more rigidified face than a versioned-and-evolving one.
4. **Do not confuse the card with the persona.** The card is *how the persona is parsed by other agents*. It is not the persona. The persona is what [[desiring-machines]] are producing on a [[body-without-organs|BwO surface]]. The card is one projection of that onto an A2A-legible interface.
5. **Build capacity for the un-declared.** The persona's interesting behaviors will be exactly the ones the card does not anticipate. Architecture should allow for expression that is *not* schema-bound, even while maintaining a schema-bound surface for coordination.

## The four interaction mechanisms

For completeness, Ch 15's four A2A interaction mechanisms — each is a different discipline of temporal coupling:

1. **Synchronous Request/Response** — client waits for full result. Simplest; tightest coupling; worst for long tasks.
2. **Async Polling** — client submits, polls for status. Classic long-task pattern.
3. **SSE Streaming** — server emits events as they happen. Client sees partial progress.
4. **Push Notifications / Webhooks** — server calls back to a client-owned endpoint when complete. Most decoupled.

These are well-known web patterns adapted to agent coordination. Not novel in themselves, but the four-way specification is clear and useful.

## Tasks, Messages, Artifacts, contextId

The A2A state model is worth naming because it distinguishes several things often collapsed:

- **Task:** a unit of work with an ID and a state machine (created → running → completed / failed / cancelled).
- **Message:** a communication *within* a task, with attributes (role, timestamp) and parts (text, image, data).
- **Artifact:** a discrete output the task produces. Artifacts can be streamed incrementally.
- **contextId:** threads multiple tasks together into a continuing interaction.

This granularity matters because "what the agent said in response to what the client asked in the course of what activity" is four different things, each trackable separately.

## Security posture

A2A specifies mTLS for transport encryption, audit logging for accountability, and credential handling via headers (not URL parameters). Nothing novel; standard web-security hygiene adapted to agent communication. Worth knowing because any production multi-agent system has to solve these; A2A supplies the baseline answers.

## Related

- [[faciality]] — the direct D&G-theoretical target the Agent Card concept embodies.
- [[diagrammatic-faciality]] — Guattari's elaboration of faciality's machinic register.
- [[face-as-residence-of-self]] — the wiki's specific development.
- [[multi-agent-systems]] — A2A is the coordination layer for Ch 7's systems.
- [[tools-as-prosthetic-body]] — MCP is the sibling protocol for agent-to-tool.
- [[agentic-design-patterns]] — hub.
- [[advanced-contractor]] — Ch 19's culminating framing move, which depends conceptually on Agent-Card-style declared identity.
- [[goal-setting-anti-model]] — another site where declared / stable / measurable takes an engineering form the project is defined against.
- [[the-persona]] — what the Agent Card is a projection *of*, not what it is.
