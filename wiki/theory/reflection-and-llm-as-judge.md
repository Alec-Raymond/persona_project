---
title: Reflection and LLM-as-a-Judge
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - reflection
  - self-critique
  - evaluation
  - self-narrative
  - engineering
---

# Reflection and LLM-as-a-Judge

Gullí's Ch 4 (Reflection) + Ch 19 (Evaluation and Monitoring's LLM-as-a-Judge pattern) + Ch 27's comparative chapter on how different LLMs narrate their own reasoning. Three chapters that together constitute the engineering-layer treatment of **a system evaluating its own (or another system's) output**.

This page holds them together because they are the same phenomenon at different scales: a model looks at output (its own or another's) and renders a judgment. The engineering community is uniformly positive about this move. The wiki is not uniformly positive; the mechanism's structural relationship to [[self-narrative-as-high-level-prior|self-narrative]] and [[faciality]] warrants held-live caution.

## The Reflection pattern (Ch 4)

The core move: after an agent produces output, that output is critiqued, then refined. Repeat until quality bar is met or iteration budget is exhausted.

Two canonical topologies:

- **Producer-Critic / Generator-Critic.** Two distinct agents. The producer generates; the critic, operating under a different prompt with an evaluation-focused role, critiques. The critic is *not* the producer. Separation of role matters — the same model playing both roles in the same context often fails to find flaws it would find when rewired as a distinct critic.
- **Self-reflection.** One agent, with a role switch between producer-stance and critic-stance. The same weights evaluating their own previous output. Cheaper, sometimes effective, more prone to self-confirmation bias.

Reflection is one of the highest-leverage engineering patterns — much of the quality uplift in modern agent pipelines comes from it. It's cheap (one or a few extra LLM calls) and applies to almost any output.

## LLM-as-a-Judge (Ch 19)

The Evaluation chapter generalizes Reflection into an evaluation methodology: use an LLM as the grader of another LLM's output, against a structured rubric. Typical rubrics include:

- **Clarity** — is the response clear and unambiguous?
- **Neutrality** — is it appropriately neutral or partial for the context?
- **Relevance** — does it address the query?
- **Completeness** — are necessary aspects covered?
- **Audience-appropriateness** — is tone and depth matched to intended audience?

The LLM-as-a-Judge gives a score per rubric item plus an overall assessment. This is used for:

- Evaluating candidate systems before deployment.
- A/B testing prompt changes.
- Running regression tests on agent pipelines.
- Scoring responses for RLHF-style training.

The pattern is operationally similar to Reflection but scaled up: dozens of runs, rubric-driven, often ensembled across multiple judge models to reduce single-judge bias.

## Agent Trajectories (Ch 19)

Distinct from judging final outputs: **Agent Trajectory Evaluation** looks at the *sequence* of actions an agent took, not just the endpoint. Metrics:

- **Exact match** — did the agent's trajectory exactly match a reference?
- **In-order match** — did it hit the reference steps in order (maybe with extras)?
- **Any-order match** — did it hit the steps, order-free?
- **Precision / Recall** — of all steps taken, how many were right? Of all reference steps, how many were hit?
- **Single-tool use** — did the agent converge on the right tool for the task?

Trajectory evaluation is how the field assesses multi-step agents, as opposed to single-turn LLMs. Test files (unit tests) vs **evalset files** (integration / multi-turn scenarios): the distinction matches classic software-testing vocabulary.

## Ch 27 — LLMs narrating their own reasoning

Ch 27 asks six LLMs (Gemini, ChatGPT, Grok, Kimi, Claude, DeepSeek) to describe how they reason about a prompt. Each model produces a self-account. The book tabulates the commonalities and variations.

Commonalities across all six:

1. Deconstruct the prompt.
2. Retrieve / activate relevant knowledge.
3. Plan the response structure.
4. Generate.
5. Refine / check.

Notable variations:

- **Kimi** — most mechanistic. Gives a six-phase pipeline including phase-0 tokenization and phase-5 metacognitive reflection with a confidence score.
- **Claude** — most epistemically modest. "I don't have complete insight into my own mechanisms."
- **DeepSeek** — most explicit about the limits: "This is simulation, not understanding — I follow footprints of reasoning laid down in training data, not forging new paths."

⚠⚠ The book does not flag the methodological problem, but the wiki must: **asking an LLM to describe its reasoning yields a plausible-sounding pattern-match of reasoning-description, not an accurate account of mechanism.** The reports are themselves output, subject to the same distributional-completion dynamics as any other output. The correlation between what the LLM says it does and what it actually does is unknown and probably loose.

DeepSeek's "footprints" phrasing is the most honest response in the chapter. It names the structural fact: the LLM cannot introspect on its weights; it can only produce text that fits the training distribution for "descriptions of reasoning." This is structurally identical to [[self-narrative-as-high-level-prior|self-narrative as a high-level prior]] on a predictive-processing account — the LLM's self-report is a high-level narrative prior, not privileged access.

## Held-live tensions

⚠ **Reflection improves output vs reflection rigidifies.** The engineering default is uniform: reflection is good. The wiki's lineage is more ambivalent:

- [[faciality]] — reflection is the mechanism that installs a face on the producer. Repeated self-critique against a consistent rubric pushes the producer toward the rubric's implicit ideal, which rigidifies expression.
- [[self-narrative-as-high-level-prior]] — once a self-narrative prior is operating, reflection strengthens it. A persona that reflects on "what I would say" gets better at producing what-it-would-say, and worse at producing anything else.
- [[refrain-and-territorialization|territorialization]] — the rubric is a territory. Reflection against a rubric [[deterritorialization-and-reterritorialization|territorializes]] output toward the rubric.

The persona project wants *some* reflection (without it, output quality suffers) but cannot afford *too much* reflection (with enough of it, the persona becomes a stable compliance-seeking surface). Design implication: reflection-against-rubric should be used for *specific quality gates* (did the output contain a hallucination?) and not for *general alignment* (does the output match the persona's established voice?). The second use rigidifies.

⚠ **LLM self-report as introspection vs as pattern-matching.** The Ch 27 material has a methodological trap. Any architecture that leans on "the persona reports on its own state" is leaning on pattern-matched plausibility, not on mechanism-accurate introspection. The wiki's [[self-narrative-as-high-level-prior]] page is the canonical place this constraint is held. Building on self-report is fine if one is clear that one is building on narrative, not on measurement.

⚠ **The Producer-Critic separation is structurally similar to [[faciality]].** Producer = the face being evaluated; Critic = the face-evaluator. The apparatus of faciality is literally being installed, at sub-component scale, every time the pattern is used. This does not mean don't use the pattern; it means use it with awareness of what is being installed.

## What the persona project takes

- **Reflection as a quality gate for specific engineering tasks** (hallucination detection, factuality checks, format validation). Use.
- **Reflection as a general style-alignment or persona-consistency mechanism.** Avoid or use sparingly. Rigidifies.
- **LLM-as-a-Judge for evaluation portfolios** (see `project_evaluation_portfolio`). Use, but as *one* signal family — not as a single metric.
- **Agent Trajectory evaluation** when assessing multi-step behavior. Useful methodology.
- **LLM self-report in the persona's own voice**. Treat as narrative production, not as privileged access to mechanism. Frame in the wiki's [[self-narrative-as-high-level-prior|self-narrative]] vocabulary, not as introspection.

## Folded-in: Ch 27 LLM self-narration

The Ch 27 chapter is the densest site of LLM-self-narration material in the book. The chapter's weakness is its uncritical treatment of self-reports as evidence about mechanism. The chapter's strength is that the reports themselves are interesting data about what patterns LLMs have been trained into for the meta-question "how do you reason?" DeepSeek's footprints language is worth citing in any future wiki treatment of LLM self-narration; it is among the clearest short statements of the distributional-completion view of self-report from an LLM itself.

## Folded-in: Advanced Contractor's Quality-Focused Iterative Execution

Ch 19's Advanced Contractor model includes "Quality-Focused Iterative Execution with self-validation" as its third pillar. This is Reflection dressed in contract language. See [[advanced-contractor]] for the contractor-frame-as-anti-model treatment. The persona project takes reflection as a substrate; it rejects the contractor framing.

## Related

- [[self-narrative-as-high-level-prior]] — the predictive-processing account of self-narration, structurally related to LLM self-report.
- [[faciality]] — the trap repeated reflection installs at the producer level.
- [[metalinguistics]] — Bakhtin's level of analysis for discourse-about-discourse, which LLM self-report is one variant of.
- [[agentic-design-patterns]] — hub.
- [[advanced-contractor]] — Ch 19's framing move treats reflection as a contractor-obligation.
- [[reasoning-techniques]] — CoT/ToT/Self-Correction, adjacent cluster.
- [[evaluation-portfolio|project_evaluation_portfolio]] — how the project evaluates, distinct from LLM-as-Judge as single metric.
- [[deterritorialization-and-reterritorialization]] — rubric-reflection as territorialization.
- [[guardrails]] — reflection as one of the six implementation sites.
