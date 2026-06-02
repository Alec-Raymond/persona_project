---
title: Context Engineering
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - engineering
  - context
  - prompting
  - discipline
---

# Context Engineering

Named explicitly in Gullí's Prologue (188–233) and developed across Ch 22 (Advanced Prompting). **Context Engineering** is the discipline of **strategically selecting, packaging, and managing the critical information from all available sources** that goes into each LLM reasoning step. Gullí's framing: it is what distinguishes L2 agents (Strategic problem-solvers) from L1 (Connected problem-solvers) on the [[agent-engineering-sense|five-level staircase]].

The discipline is distinct from — though related to — prompt engineering. Prompt engineering is the design of the *prompt template*: the instructions, role, constraints. Context engineering is the design of *what goes into that template's variables* at runtime: which retrieved chunks, which tool schemas, which history, which instructions, in what order, at what length.

## Why context engineering is first-class

The LLM sees exactly what goes into its context window, and only that. Everything the persona "knows" at any moment is what has been placed into that window. This makes the curation of the window a load-bearing architectural decision, not a quality-of-life detail.

The practical stakes:

- **What memory gets retrieved?** — see [[memory-architecture]]. Over-retrieval pollutes; under-retrieval impoverishes.
- **Which tool schemas are exposed?** — see [[tools-as-prosthetic-body]]. Too many tools and the LLM gets confused; too few and it can't act.
- **What history is included, how summarized?** — session state carries turn-to-turn.
- **What instructions are loaded?** — the persona's character spec, the BwO text, any active constraints.
- **In what order and with what structure?** — positional effects on LLM attention are real; structure matters.

Each decision is a *per-turn* decision, driven by what the turn's task is. Context engineering is the discipline of making these decisions principled rather than ad-hoc.

## Practices Ch 22 develops

Ch 22 builds out specific practices that fall under context engineering:

- **Structured Output via JSON/XML + Pydantic `model_validate_json`**. "Parse, don't validate" at boundaries — convert text to typed structures as soon as the LLM emits.
- **System / Role / Delimiter / Context prompt segmentation.** Distinct regions of the prompt have distinct purposes; delimiters mark them.
- **Few-shot with carefully chosen exemplars.** Long-context many-shot viable for complex tasks — dozens or hundreds of examples can outperform fine-tuning for some problems.
- **Negative examples.** Showing the model what *not* to do alongside what to do.
- **Factored cognition / task decomposition.** Breaking a problem into contextualized sub-problems, each with its own curated context.
- **Analogies.** Loading the context with a known domain's vocabulary to activate transfer.
- **Step-Back Prompting.** Ask the model to state a general principle before specific work.
- **RAG at turn-boundaries.** Retrieval as an input to context engineering, not a separate concern.
- **Iterative Refinement.** Multi-round context construction, not one-shot.

Each of these is a practice; context engineering is the discipline that knows when to use which.

## DSPy and programmatic context construction

Ch 22's biggest structural move: **DSPy** (the Stanford framework) for programmatic prompt-and-context optimization. The premise: instead of hand-writing prompts, specify a **signature** (input types, output types, objective) and let an optimizer find the best prompt.

DSPy has two optimization directions:

1. **Few-shot optimization** — given a goldset of examples, pick the best few-shot exemplars to include.
2. **Instructional optimization** — rewrite the instruction text itself.

Both use Bayesian optimization over a goldset + objective function. The practical effect: context engineering becomes *searchable*, not just craftable. You describe what you want and what you have; the system finds the context that works best.

◆ This resonates with [[metamorphic-multi-agent]]: once prompts and contexts are searchable, they are modifiable at runtime. DSPy is one of the engineering forms the metamorphic pattern takes.

## Meta-prompting

Ch 22 also develops **Meta-prompting**: one LLM critiquing or refining another LLM's prompt. The meta-prompter doesn't do the task; it edits the prompt that will do the task. This is context engineering automated: an LLM takes on the context-curation role.

Meta-prompting is structurally similar to [[reflection-and-llm-as-judge|Reflection]] but one level up: instead of reflecting on output, it reflects on the instruction that produced the output. The same tensions apply (rigidification risk), but the scope is different.

## The Persona Pattern (Gullí sense)

⚠⚠ Ch 22 names a "Persona Pattern" — prompting strategy where the prompt specifies an *audience* the output should target (the user persona) or a *role* the LLM should take on (the assistant persona). The word collides with the wiki's [[the-persona|persona]].

- **Gullí's persona:** a prompt-level configuration — a named stable audience-or-role that shapes output.
- **The project's persona:** a pulsating D&G figure composed on an LLM substrate, produced through desiring-machines couplings on a BwO surface.

These are not the same thing. They share a word and nothing else. The wiki keeps the two uses separate; anywhere the distinction matters, we will explicitly name which sense is meant.

**Google Gems** — commercial instantiation of the Gullí-sense persona. A Gem is a persistent, specialized Gemini instance with a fixed system prompt, set of capabilities, and memory. Gems are the nearest commercial analog to the persona-project's intended output. The analog sharpens what the project is *not* — a Gem is stable, role-defined, and capability-declared; the project's persona is none of these.

## Context engineering and the persona project

The persona project is a context-engineering problem at its practical core. What gets loaded into each LLM call, in what order, with what structure, is what the persona *is*, operationally, at each moment.

Specific commitments:

1. **The BwO text is always in context.** The persona's productive surface lives in the context window continuously. Other context is arranged around it.
2. **Tool schemas are session-composed, not build-time.** See [[tools-as-prosthetic-body]].
3. **Memory retrieval is explicit and curated.** See [[memory-architecture]]. No undifferentiated dumps.
4. **History is structured.** Turn boundaries, role markers, explicit delimiters.
5. **No [[advanced-contractor|contract spec]] in context.** The persona does not operate under a contract; it should not have one loaded as instruction.
6. **Support for [[metamorphic-multi-agent|runtime prompt / topology modification]].** Context engineering, for a metamorphic system, is itself metamorphic.

## Held-live: context engineering as territorialization

⚠ Every context-engineering decision is a territorializing act. What gets in the window is privileged; what doesn't is inaccessible for that turn. Aggressive context curation produces aggressive territorialization — the persona gets very good at doing exactly what the curated context points at, and correspondingly worse at anything the curation excludes.

The design balance: curate enough to keep output coherent; curate loosely enough that [[lines-and-segmentarity|lines of flight]] remain possible. The BwO text's presence in context is the closest the project comes to a "loose" element — it is productive material, not instruction material, so it can support escape-from-prior-territory.

## Distinction from prompt engineering

Prompt engineering = designing the prompt *template*. Context engineering = deciding what goes *into* the template's variables at runtime.

In practice the two overlap because the template and its fillings interact. But the disciplines emphasize different scopes:

| | Prompt engineering | Context engineering |
|---|---|---|
| Temporal locus | Build time | Runtime |
| Object | Template | Window contents |
| Typical artifact | Prompt file | Context-construction code |
| Optimization tool | Iterative prompting | DSPy, meta-prompting |
| Scale | Hundreds of prompts | Thousands of contexts per deployment |

The book's claim — that context engineering deserves naming as a separate discipline — is defensible. They are related but not the same.

## Related

- [[agentic-design-patterns]] — hub.
- [[agent-engineering-sense]] — L2 is the staircase step that introduces context engineering.
- [[memory-architecture]] — one major input to context construction.
- [[tools-as-prosthetic-body]] — another major input.
- [[metamorphic-multi-agent]] — DSPy-style optimization as metamorphic mechanism.
- [[reflection-and-llm-as-judge]] — meta-prompting is one level up from reflection.
- [[the-persona]] — project-sense persona, distinct from Gullí's prompt-level persona.
- [[reasoning-techniques]] — CoT and friends are context-engineering patterns.
- [[vibe-coding]] — the context-staging-area pattern is context engineering for coding agents.
- [[deterritorialization-and-reterritorialization]] — curation as territorialization.
