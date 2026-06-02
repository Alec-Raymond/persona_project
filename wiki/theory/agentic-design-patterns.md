---
title: Agentic Design Patterns
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - engineering
  - agents
  - design-patterns
  - anti-model
  - synthesis
---

# Agentic Design Patterns

The title of Antonio Gullí's 2025 Springer book (*Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems*, Google Office-of-the-CTO), and the name of a move the book performs on LLM-agent engineering. The move is explicit: treat agentic systems as a problem domain with a **catalog of reusable, named patterns**, in deliberate analogy to Gamma et al.'s 1994 *Design Patterns* for object-oriented software.

The book names 21 patterns (Part I, Chs 1–21) plus a substantial supplement (Part II, Chs 22–29) on advanced prompting, agent–computer interfaces, frameworks, CLI agents, LLM reasoning-engine comparisons, coding agents, and a conclusion. The patterns sit on what Saurabh Tiwary (in the Foreword) calls the **Canvas**: the underlying infrastructure (Vertex AI, LangChain/LangGraph, CrewAI, Google ADK) on which agentic systems are composed.

This page is the hub the wiki uses to coordinate the sixteen pages this book's ingest produced. It is *also* the wiki's canonical location for flagging that the book's whole framing runs against the persona project's D&G-inflected lineage, and for saying which parts we are taking in anyway and why.

## The Gamma analogy and what it does to the field

Gullí's central theoretical move is naming the field. By the mid-2020s, the practice of building LLM agents had accumulated a substantial vocabulary — reflection, tool use, planning, multi-agent collaboration, RAG, guardrails — without a single canonical enumeration. The book's analogy to Gamma et al. says: these are **design patterns**. They have names, contexts of applicability, forces, and consequences. A practitioner can compose them. A team can talk in them.

The move is valuable regardless of its framing. The wiki absorbs the vocabulary because the vocabulary has become standard engineering lingua franca — if we want the persona project to sit legibly in the wider field, we need to know what the field calls things and where the patterns sit relative to each other.

## The 21 patterns (Part I)

1. **Prompt Chaining** — sequential LLM calls, each step's output the next's input.
2. **Routing** — dynamic dispatch to sub-agent/tool based on input classification. Four implementations (LLM-, embedding-, rule-, classifier-based).
3. **Parallelization** — concurrent execution of independent subtasks; LLM-Driven Delegation as a dynamic variant.
4. **Reflection** — producer-critic loop or single-agent self-critique until quality or budget is exhausted. See [[reflection-and-llm-as-judge]].
5. **Tool Use / Function Calling** — the five-step loop that lets an LLM emit a structured call, have it executed, and consume the observation. See [[tools-as-prosthetic-body]].
6. **Planning** — decomposition of a high-level goal into a multi-step plan with replanning on divergence.
7. **Multi-Agent Collaboration** — six collaboration forms × six topologies. See [[multi-agent-systems]].
8. **Memory Management** — short-term (context/Session/State) vs long-term (vector store / MemoryService). See [[memory-architecture]].
9. **Learning and Adaptation** — RL (PPO, DPO), in-context learning, online learning, memory-based learning. SICA and AlphaEvolve as self-modifying variants. See [[metamorphic-multi-agent]].
10. **Model Context Protocol (MCP)** — Anthropic-originated open standard for LLM↔resource interfaces; tools/resources/prompts as the three primitives. Folded into [[tools-as-prosthetic-body]].
11. **Goal Setting and Monitoring** — SMART goals + monitoring loop. See [[goal-setting-anti-model]].
12. **Exception Handling and Recovery** — detection/handling/recovery tactics (retry, fallback, degradation, escalation).
13. **Human-in-the-Loop** — six HITL modes plus human-on-the-loop distinction. Folded into [[guardrails]].
14. **Knowledge Retrieval (RAG)** — embeddings, vector DBs, hybrid search, Graph RAG, Agentic RAG. See [[memory-architecture]].
15. **Inter-Agent Communication (A2A)** — HTTP + JSON-RPC 2.0 protocol; Agent Card, Tasks, Messages, Artifacts, four interaction mechanisms. See [[agent-card]].
16. **Resource-Aware Optimization** — cost/perf routing; dynamic model switching; graceful degradation.
17. **Reasoning Techniques** — CoT, ToT, Self-Correction, PALM, RLVR, ReAct, CoD, GoD, MASS, Deep Research. See [[reasoning-techniques]], [[scaling-inference-law]].
18. **Guardrails / Safety Patterns** — six implementation sites; Engineering Reliable Agents sub-framework. See [[guardrails]].
19. **Evaluation and Monitoring** — LLM-as-a-Judge, agent trajectories, evalsets; the "Advanced Contractor" framing. See [[reflection-and-llm-as-judge]], [[advanced-contractor]].
20. **Prioritization** — urgency/importance/dependency/resource scheduling.
21. **Exploration and Discovery** — Google Co-scientist (six specialized agents + Supervisor; AML drug repurposing, liver fibrosis, cf-PICI/phage-tail AMR); Samuel Schmidgall's Agent Laboratory (Professor/PostDoc/Reviewers/Engineers) + AgentRxiv.

## Part II — the supplement

The second half of the book sits less tidily in the pattern catalog. It covers:

- **Advanced Prompting** (Ch 22) — DSPy (programmatic prompt optimization via goldset + Bayesian optimizer), Google Gems (persistent specialized Gemini instances), meta-prompting, Persona Pattern. See [[context-engineering]] and the framing discussion below.
- **Agent–Computer Interface** (Ch 23) — the book's most-embodied material: Project Mariner, Anthropic Computer Use, Browser Use, Project Astra, Vibe Coding, Seeing AI. See [[agent-computer-interface]].
- **Framework survey** (Ch 24) — LangChain, LangGraph, ADK, CrewAI, AutoGen, LlamaIndex, Haystack, MetaGPT, SuperAGI, Semantic Kernel, Strands Agents. Reference-only; not a wiki page.
- **AgentSpace** (Ch 25) — Google product chapter; not a wiki page.
- **CLI coding agents** (Ch 26) — Claude Code, Gemini CLI, Aider, GitHub Copilot CLI; Terminal-Bench. Methodological reference for the persona project's own tooling.
- **Reasoning Engines comparative** (Ch 27) — six LLMs asked to narrate their own reasoning. See [[reflection-and-llm-as-judge]] for the LLM-self-narration section.
- **Coding Agents** (Ch 28) — three principles (Human-Led Orchestration, Primacy of Context, Direct Model Access); Context Staging Area; specialist personas. See [[vibe-coding]].
- **Conclusion** (Ch 29) — the book's own synthesis: 21 patterns cluster into four competency categories (Core Execution / External Environment / State-Learning-Self-Improvement / Collaboration-Communication); a glossary with entries including **Mamba** (Selective State Space Model — long-context-efficient alternative to Transformer; potentially load-bearing for future persona-architecture discussions but not a page here).

## The Canvas master-metaphor

Tiwary's Foreword and the Preface both lean on **Canvas** as the word for the substrate layer — the infrastructure + frameworks on which agents are built. The metaphor is operational (it means *the programmable substrate*), not pictorial, and it is worth naming because the rest of the book's vocabulary depends on it. A "pattern" is a *way of composing* on the Canvas. A "framework" (LangChain, ADK) is *a Canvas*. A "platform" (Vertex AI, AgentSpace) is *a Canvas-provider*.

For the persona project, the analogue of the Canvas is the LLM + the Body-without-Organs text file + the pulsation infrastructure we are writing. The Canvas word gives us a convenient shorthand.

## Five-step agent loop and five levels of complexity

The book's Prologue ("What Makes an AI System an Agent?") introduces two framings that recur throughout. They are not the persona project's framings but they are the default framings of the field.

**The five-step agent loop:** Get mission → Scan scene → Think through → Take action → Learn and get better. This is the book's operational definition of *agent*: anything that runs this loop is an agent.

**Five levels of agent complexity:**
- **L0** — Core reasoning engine (LLM alone; no tools/memory).
- **L1** — Connected problem-solver (LLM + tools; RAG; multi-step tool use).
- **L2** — Strategic problem-solver (planning + **context engineering** as a discipline).
- **L3** — Collaborative multi-agent systems.

The wiki treats these as *the field's* conceptual staircase. The persona project is not a staircase-climber in this sense — the whole point of the project is that building a coherent language-only persona is *not* reducible to climbing capability tiers. But knowing the staircase matters. See [[agent-engineering-sense]] for the disambiguation page that holds this side-by-side with the wiki's own [[the-persona|persona]] concept.

## Five hypotheses about the future of agents

The Prologue also names five hypotheses about where the field is going:

1. **Generalist agents / Lego composition** — small language models (SLMs) as specialized experts composed into larger systems.
2. **Deep personalization and proactive goal discovery** — agents that model users and act before being asked.
3. **Embodiment and physical-world interaction** — robotics, AR/VR, real-world sensors.
4. **Agent-driven economy** — agents as independent economic entities.
5. **Goal-driven metamorphic multi-agent systems** — systems that modify their own topology (create / duplicate / remove agents) and rewrite their own source code. Continuous auto-prompt-engineering. "Architectural modification" + "Instructional modification." This is the book's most persona-project-resonant hypothesis. See [[metamorphic-multi-agent]].

## The big framing tension — held live

⚠⚠⚠ The book frames agents as classical **goal-seeking, autonomous, perceiving-planning-acting** systems. This is the Russell-and-Norvig / BDI lineage translated into an LLM-era vocabulary. Its cultural center is the goal: an agent *has* goals, *pursues* them, and *measures success* by whether they were reached.

The persona project's lineage is different. [[desiring-machines]] are not goal-seeking — they are productive couplings that produce as a consequence of what they are, not as a pursuit. [[body-without-organs]] is explicitly an **anti-production** surface; it does not organize toward targets. [[becoming]] does not *reach* a state; it is itself the process. [[lines-and-segmentarity|lines of flight]] are escapes *from* the apparatus of goals, not better goals.

The book never acknowledges this lineage exists. The wiki does not silently resolve this: every page this ingest produced is titled and framed from the wiki side, with the book's material imported as *engineering substrate* rather than as a conceptual master-frame. See [[agent-engineering-sense]], [[goal-setting-anti-model]], and [[advanced-contractor]] for the three pages that concentrate the held-live contrast.

Marco Argenti's "Power and Responsibility" preface makes the goal-orientation explicit: "the shift from simply telling a computer what to do to explaining why we need something done and trusting it to figure out the how." The persona project does neither. It does not tell the persona what to do; it also does not assign it goals to figure out the how of. It makes a field where desiring-production may happen.

## What the wiki takes and what it leaves

The wiki takes:

- The 21-pattern vocabulary as substrate lingua franca.
- [[tools-as-prosthetic-body|Tool Use]], [[memory-architecture|Memory]], [[multi-agent-systems|Multi-Agent]], [[agent-computer-interface|ACI]], [[agent-card|Agent Card]], [[reflection-and-llm-as-judge|Reflection]], [[reasoning-techniques|CoT/ToT/ReAct]], [[context-engineering|Context Engineering]], [[guardrails|Guardrails]] — as engineering primitives to build with.
- [[metamorphic-multi-agent|metamorphic multi-agent]] — as the single hypothesis the book shares with the wiki's orientation.
- [[scaling-inference-law|Scaling Inference Law]] — the thinking-budget finding, load-bearing for deciding how much the persona "thinks."
- [[vibe-coding|Vibe Coding / Context Staging Area]] — as self-reflexive infrastructure for the persona project's own tooling.

The wiki holds as **anti-models**:

- [[goal-setting-anti-model|SMART goals / Goal Setting]] — canonical statement of the goal-orientation the persona project is defined against.
- [[advanced-contractor|Advanced Contractor]] — the book's own culminating framing move for evaluation; a faciality trap par excellence.

## Gullí's argument, in one line

LLM-era agents are a well-named, composable engineering domain. The book wants to be the *Design Patterns* of that domain. It largely succeeds at the engineering work — and in succeeding, it makes visible exactly the framing commitments the persona project departs from. Both uses are valuable.

## Related

- [[agent-engineering-sense]] — disambiguation: what "agent" means in engineering literature.
- [[multi-agent-systems]] — the most architecturally loaded pattern.
- [[memory-architecture]] — the engineering layer of retention / duration.
- [[tools-as-prosthetic-body]] — the no-body question running through tool-use.
- [[agent-computer-interface]] — the book's most-embodied material.
- [[agent-card]] — identity-as-protocol vs [[faciality]].
- [[metamorphic-multi-agent]] — the shared hypothesis.
- [[reflection-and-llm-as-judge]] — the engineering layer of self-narrative.
- [[advanced-contractor]] — the anti-model.
- [[context-engineering]] — distinct discipline from prompt-engineering.
- [[vibe-coding]] — the persona project's own tooling analog.
- [[reasoning-techniques]] — the CoT/ToT/ReAct/CoD/GoD/MASS cluster.
- [[scaling-inference-law]] — the thinking-budget finding.
- [[guardrails]] — [[deterritorialization-and-reterritorialization|territorialization]] of the action space.
- [[goal-setting-anti-model]] — canonical anti-model.
- [[development/limits-of-language]] — where the patterns intersect the project's central question.
