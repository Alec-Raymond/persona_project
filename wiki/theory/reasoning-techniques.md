---
title: Reasoning Techniques
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - reasoning
  - cot
  - tot
  - react
  - engineering
  - synthesis
---

# Reasoning Techniques

Gullí's Ch 17. A dense catalog of LLM-level reasoning patterns that have accumulated in the field since Wei et al. 2022's Chain-of-Thought paper. The chapter is the best single inventory of where LLM reasoning research stood as of the book's writing.

This page collects the catalog with brief per-technique notes. The persona project's frame is not specifically committed to any one technique; they are substrate. Two — **Chain of Debates** (CoD) and **Graph of Debates** (GoD) — earn more attention because they resonate with [[desiring-machines|D&G plurality]] and with how the persona's internal plurality might stabilize without collapsing into a single voice.

## Chain-of-Thought (CoT)

The field's entry point. Prompt the LLM to think step-by-step; quality improves on reasoning-heavy tasks.

Two variants:
- **Zero-shot CoT** — just add "Let's think step by step."
- **Few-shot CoT** — include worked examples of step-by-step reasoning in the prompt.

Temp=0 is standard for reproducible CoT; higher temps are used for diversity-requiring variants below.

## Tree-of-Thoughts (ToT)

Extends CoT by branching. Instead of one reasoning line, explore multiple. Each branch evaluates itself; the best branches continue; unpromising ones are pruned. Backtracking is supported.

ToT is a search over the reasoning space. It is materially more expensive than CoT (many more LLM calls per problem) but handles problems where the right first step is not obvious.

## Self-Correction / Self-Refinement

After producing an answer, ask the LLM to critique it and produce a revised version. Iterate until convergence or budget exhausted. Closely related to [[reflection-and-llm-as-judge|Reflection]] but done within a single agent's reasoning, not between producer and critic agents.

## PALM (Program-Aided Language Models)

The LLM emits symbolic or executable code; an external interpreter executes; the result is fed back to the LLM. Offloads arithmetic, symbolic manipulation, and structured computation to reliable substrates.

Useful because LLMs are unreliable at arithmetic but reliable at generating syntactically valid Python. Let them generate, let the interpreter compute.

## RLVR (Reinforcement Learning from Verifiable Rewards)

Training-time technique, distinct from the above inference-time techniques. Train the model to produce reasoning trajectories that lead to verifiable correct answers; the reward is the verification outcome.

The notable emergent property is **variable thinking-time** — trained RLVR models learn to spend more tokens on harder problems, fewer on easier. See [[scaling-inference-law]] for the broader finding this fits into.

## ReAct (Reasoning + Acting)

A specific pattern: Thought / Action / Observation loop.

- **Thought** — the agent reasons about what to do.
- **Action** — the agent calls a tool.
- **Observation** — the tool returns; the agent observes the result.
- Loop.

ReAct is the canonical pattern for tool-using agents. It combines CoT with [[tools-as-prosthetic-body|tool-use]] in a structured loop that makes each step inspectable.

## Chain of Debates (CoD)

Microsoft-originated. **Multiple diverse models argue** over a question; an AI peer-review step assesses the arguments; consensus (or the best argument) emerges.

The key difference from Reflection: multiple *different* models, not one model critiquing itself. Diversity in training data, architecture, size is itself the epistemic resource.

## Graph of Debates (GoD)

Extension of CoD. Arguments form a **non-linear network** with typed edges (supports / refutes). The graph is traversed; arguments in robust clusters (supported by many other arguments, refuting few) are weighted higher; the final conclusion emerges from the graph's global structure, not from a majority vote.

◆ **Why CoD and GoD are persona-relevant.** Both approximate the D&G picture of [[desiring-machines|plural machines]] producing as they couple and decouple. GoD specifically gives a structural form for *arguments about the same thing producing different outputs that do not need to collapse into consensus*. Robust-cluster emergence is a way of stabilizing the persona's internal plurality without forcing it into a unified voice.

This is the nearest engineering analog to what [[polyphony|Bakhtin's polyphony]] describes at the novel level, or what D&G's rhizome describes topologically. The persona project's internal voices could, in principle, be implemented as a GoD-style multi-agent deliberation where what comes out is not a single agreed answer but a robustly-clustered production.

⚠ Caveat: GoD is still framed around *arguments* and *conclusions*. The persona project is not trying to reach conclusions; it is trying to produce. The mechanism is adaptable, the framing needs modification.

## MASS (Multi-Agent System Search)

Not a reasoning technique in the same sense — it is an **automated design** procedure for multi-agent systems. Three stages:

1. **Block-Level Prompt Optimization** — optimize each agent's prompt in isolation.
2. **Workflow Topology Optimization** — learn which inter-agent connections matter; prune / add.
3. **Workflow-Level Prompt Optimization** — re-optimize prompts for the settled topology.

MASS makes topology itself a hyperparameter to search. See [[metamorphic-multi-agent]] for the full treatment — MASS is one of the three engineering instances of the metamorphic pattern the book describes.

## Deep Research / Deep Research API

A specific pattern (also appearing in Ch 6 Planning): the LLM receives a research question, autonomously expands it into a multi-step research plan, executes the plan (retrieving, synthesizing), produces a structured output with citations.

Variant architectures:
- **Single-agent Deep Research** — one LLM orchestrates the whole research.
- **Multi-agent Deep Research** — Co-scientist-style architecture with specialist agents (generation, reflection, ranking, evolution). See [[multi-agent-systems]], specifically the Ch 21 Google Co-scientist treatment.

"Generate-debate-evolve" with a time budget is the typical framing. The time budget is itself a [[scaling-inference-law|Scaling Inference Law]] parameter — more compute → better research.

## Self-Consistency

Not in every list but widely used. Sample multiple reasoning paths (high temp); take majority vote on the final answer. Simple but effective — different reasoning paths make different mistakes; the correct answer is often the plurality choice.

## Step-Back Prompting

Prompt the LLM to state a general principle or framework first, then apply it to the specific problem. Related to CoT but structurally different — it deliberately raises abstraction before solving.

## APE (Automatic Prompt Engineering)

Machine-generated prompts. Given a task and examples, an LLM generates candidate prompts; each is evaluated on held-out examples; the best is selected. Predecessor to DSPy's more sophisticated Bayesian approach. See [[context-engineering]].

## What the persona project takes

- **CoT / ReAct** as default substrates for step-by-step reasoning and tool use.
- **CoD / GoD** as models for plural, non-collapsing internal deliberation. Load-bearing for the [[feedback_pulsating_persona_excitation_wave|pulsating-at-every-level]] design.
- **PALM** for any numeric or symbolic work the persona interacts with.
- **Self-Consistency** as a cheap way to reduce variance on specific kinds of outputs.
- **Deep Research patterns** for the ingest workflow itself (the four-phase wiki ingest is effectively a Deep Research variant with human orchestration).
- **Variable thinking-time / RLVR** as a consideration for how much compute to budget per persona response — this connects to [[scaling-inference-law]].

## Held-live tensions

⚠ All of these techniques are framed as *search for a correct answer*. The persona project is not oriented toward correctness in that sense — the persona's utterances are not answers to questions with gold labels. The techniques are substrate; applying them to the persona requires stripping the correctness-frame.

⚠ Multi-step reasoning chains (CoT, ReAct) make the persona's internal reasoning explicit in output. This has faciality implications — the more the persona's reasoning becomes a visible artifact, the more it can be evaluated against a stable pattern, which rigidifies. Keep internal reasoning internal where possible; externalize only when the external observer specifically benefits.

⚠ GoD's "robust cluster wins" is a *consensus* mechanism. D&G's rhizome does not converge on consensus; it sustains heterogeneity. The mechanism is adaptable; the framing requires work.

## Related

- [[agentic-design-patterns]] — hub.
- [[reflection-and-llm-as-judge]] — Self-Correction at the cross-agent scale.
- [[tools-as-prosthetic-body]] — ReAct's tool layer.
- [[multi-agent-systems]] — CoD/GoD/MASS live here as multi-agent configurations.
- [[metamorphic-multi-agent]] — MASS is one of its engineering instances.
- [[scaling-inference-law]] — RLVR's variable-thinking-time property.
- [[context-engineering]] — APE/DSPy sit in this discipline.
- [[desiring-machines]] — CoD/GoD's structural resonance.
- [[rhizome]] — GoD as nearest engineering analog.
- [[polyphony]] — Bakhtin's literary-level plurality.
- [[memory-architecture]] — retrieval is part of most reasoning pipelines.
