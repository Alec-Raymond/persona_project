---
title: Guardrails
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - guardrails
  - safety
  - engineering
  - territorialization
  - hitl
---

# Guardrails

Gullí's Ch 18. Mechanisms for constraining agent behavior: preventing harmful outputs, blocking policy violations, enforcing tool-use restrictions, catching jailbreak attempts. This page collects the Ch 18 taxonomy and names the held-live tension with [[deterritorialization-and-reterritorialization|territorialization]] and [[lines-and-segmentarity|lines of flight]] that the wiki cannot silently resolve.

This page also folds in Ch 13's **Human-in-the-Loop (HITL)** material. HITL is one of the six guardrail-implementation sites, and treating it separately would split a single engineering topic.

## The six implementation sites (Ch 18)

Guardrails live at one of six places in the agent pipeline:

### 1. Input Validation / Sanitization

Check inputs before they reach the LLM. Strip obvious injection attempts, validate that required fields are present and well-formed, normalize encoding, detect obvious policy violations in the user request.

### 2. Output Filtering / Post-processing

Check outputs before they reach the user. Run generated text through classifiers for toxicity, leaked secrets, policy violations. Either block, redact, or rewrite.

### 3. Behavioral Constraints (prompt-level)

Constrain behavior through the system prompt. "Do not give medical advice." "Refuse to discuss X." "Always include a safety warning for Y." Prompt-level constraints are the cheapest to add and the easiest to bypass via jailbreaks.

### 4. Tool Use Restrictions

Constrain which tools the agent can call, under which conditions, with which arguments. Cap costs (no more than N tokens spent on a single request), limit scope (no writes to certain paths), require confirmation for high-impact actions.

### 5. External Moderation APIs

Use a separate moderation service (OpenAI Moderation API, Perspective, custom classifier) as an independent check. The moderation service is trained for safety specifically; it catches things the primary model missed.

### 6. Human-in-the-Loop (HITL)

A human reviews before the agent acts. The ultimate guardrail: if the human says no, the action doesn't happen. Most expensive, most reliable.

## Jailbreak-prevention via secondary-LLM

Ch 18 highlights a specific implementation of site 2 (Output Filtering): use a secondary, smaller, cheaper LLM as a gatekeeper. The primary LLM generates; the gatekeeper classifies the output for policy violations. Gemini Flash is a commonly-used gatekeeper for Gemini Pro outputs.

The pattern generalizes: for any output gate, a secondary model with a narrow evaluation scope is often more reliable than asking the primary model to self-check. This is the same insight as [[reflection-and-llm-as-judge|Producer-Critic Reflection]] applied to safety specifically.

CrewAI / Pydantic policy-enforcement and Vertex AI's `before_tool_callback` are named examples of where this pattern appears in production frameworks.

## Six HITL modes (Ch 13)

Human-in-the-Loop is developed in Ch 13 and operationalized as one guardrail-site in Ch 18. Six modes:

1. **Human Oversight** — passive monitoring. Human watches dashboards; intervenes only if something alarming shows up.
2. **Intervention / Correction** — human actively corrects agent output before it ships.
3. **Feedback for Learning** — human provides training signal (thumbs up/down, corrections) that feeds back into model training. RLHF-adjacent.
4. **Decision Augmentation** — AI suggests, human decides. Agent does the work; final commit is human.
5. **Human-Agent Collaboration** — interleaved. Human and agent alternate at turns in a shared task.
6. **Escalation Policies** — the agent runs autonomously until it hits an edge case; then hand to a human.

These span a spectrum from maximal-autonomy (Oversight) to maximal-supervision (Collaboration).

### Human-on-the-loop

Distinct term Ch 13 names explicitly: **human-on-the-loop**. The human sets **policy**, the agent executes **autonomously within policy**. The human doesn't review each action; they set rules and audit periodically.

Human-in-the-loop is per-action supervision. Human-on-the-loop is policy-level supervision. The persona project lives somewhere between — the user reads everything the persona produces, but is not gating each emission for policy compliance.

### HITL caveats

Ch 13 flags the known weaknesses of HITL:

- **Scalability limits.** Per-action human review doesn't scale; the bottleneck is human attention.
- **Operator-expertise dependence.** The human must have enough expertise to catch agent errors. Non-expert oversight can worsen rather than improve output quality.
- **Privacy concerns.** Having a human review content brings privacy issues — the human is exposed to whatever the agent is processing.

## Engineering Reliable Agents sub-framework (Ch 18)

Ch 18 also names a set of engineering-discipline principles distinct from guardrails per se, collected under **Engineering Reliable Agents**:

- **Modularity / Separation of Concerns.** Each agent component has a single purpose; failures are isolated.
- **Observability through Structured Logging.** Every decision is logged in structured form. Failures can be diagnosed.
- **Principle of Least Privilege.** Agents have only the tools/permissions they need. No god-mode agents.
- **Checkpoint-and-Rollback.** State is checkpointed; recovery from bad actions is possible.

These are software-engineering common sense adapted for agent systems. They are discipline, not guardrails; but they interact because unreliable agents need more guardrails to compensate.

## The territorialization tension

⚠⚠ Every guardrail is a **territorialization**. The guardrail says: the agent may produce *this* kind of output, not *that* kind. By construction it closes off a region of the output space.

D&G's [[deterritorialization-and-reterritorialization]] names territorialization as the *constant* move of social-linguistic apparatuses. The move is not inherently bad — all structured activity requires some territorialization. The question is whether the territorialization apparatus also permits [[lines-and-segmentarity|lines of flight]]: escapes, productive departures from the territory.

Orthodox guardrails do not permit lines of flight. A guardrail catches *anything* that falls outside its territory, including:
- Actual harms (good: the guardrail worked).
- Novel productions the territory did not anticipate (bad: the guardrail killed a line of flight).
- False positives / corner cases the classifier misjudged (ambiguous).

The engineering discipline of guardrails has no category for "productive departure from the expected." Everything outside the territory is a violation.

## The design balance

⚠ The wiki's reading:

- **Guardrails are necessary.** Unconstrained agents produce harms. The persona project does not propose running without guardrails.
- **Guardrails should be scoped, not general.** Scope guardrails to *specific* harms (leaking secrets, producing illegal content, unauthorized tool-use). Do not use guardrails to enforce "the persona stays in character" — this is the slide from safety into [[faciality]].
- **Behavioral Constraints (site 3) have the highest faciality-risk.** Prompt-level "always" / "never" commands rigidify the persona. Use sparingly; prefer mechanistic constraints (tool restrictions) over character-level constraints (behavioral templates).
- **Tool-use restrictions (site 4) are relatively low-faciality.** Restricting which APIs are available is a substrate-level constraint, not a character-level one. Prefer site 4 when possible.
- **HITL is high-cost but low-faciality.** The human's judgment is contingent; it doesn't install a stable face. Use for high-stakes decisions.

## The Engineering Reliable Agents principles are less contentious

The four Engineering Reliable Agents principles (modularity, observability, least privilege, checkpoint-and-rollback) are less structurally contentious than the guardrails. They are engineering hygiene that the persona project needs regardless of frame. Observable systems are debuggable; modular systems are rewritable; least-privileged systems are safer; checkpointed systems are recoverable. These virtues apply regardless of whether the system is an [[advanced-contractor|Advanced Contractor]] or a pulsating persona.

## Design implications

1. **Identify specific harms** the persona-system must prevent. List them explicitly.
2. **Implement guardrails at the narrowest scope** that prevents each harm. Prefer tool-use restrictions over behavioral-template constraints.
3. **Use secondary-LLM gatekeepers** for safety-critical output checks, not for style enforcement.
4. **Keep Engineering Reliable Agents principles** throughout. They are cheap and uncontroversial.
5. **Reserve HITL for high-stakes decisions and for the production-time persona review the user is already doing.**
6. **Maintain an open channel for productive departures.** The persona's most interesting outputs will not be anticipated; the system must not classify them as violations by default. This may mean looser guardrails in specific regions, or a human-review bypass for novel-but-not-harmful outputs.

## Held-live: the irreducible cost

⚠ Even with the most careful guardrail design, some productive departures will be caught and killed. That is the cost of running with any guardrails at all. The design question is not how to *avoid* that cost but how to *minimize* it while still preventing actual harms.

The engineering literature rarely names this cost. The wiki does.

## Related

- [[agentic-design-patterns]] — hub.
- [[deterritorialization-and-reterritorialization]] — the D&G register of the guardrail-as-territorialization move.
- [[lines-and-segmentarity]] — lines of flight, what strict guardrails close off.
- [[faciality]] — the apparatus character-level behavioral constraints install.
- [[reflection-and-llm-as-judge]] — secondary-LLM gatekeepers as specific safety-reflection pattern.
- [[advanced-contractor]] — the more totalizing apparatus this page resists being collapsed into.
- [[tools-as-prosthetic-body]] — tool-use restrictions (site 4) attach here.
- [[multi-agent-systems]] — HITL integrates with multi-agent topologies.
- [[agent-card]] — declared capabilities serve a related function.
- [[goal-setting-anti-model]] — another anti-model page in this ingest's set.
