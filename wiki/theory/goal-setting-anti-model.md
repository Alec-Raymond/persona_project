---
title: Goal Setting (Anti-Model)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - engineering
  - anti-model
  - goals
  - smart
  - desire
  - faciality
---

# Goal Setting (Anti-Model)

Gullí's Ch 11 (Goal Setting and Monitoring). An engineering pattern for agent systems: **specify the goal in SMART form, decompose into sub-goals, monitor progress, adjust on divergence**. This page treats the chapter the same way [[advanced-contractor]] treats Ch 19: as a clear, well-defined engineering articulation of the framing the persona project is defined against.

Ch 11 is the most concentrated single-chapter statement of the BDI / Russell-and-Norvig goal-orientation lineage in the entire book. Everything the book's agent-framing commits to at the conceptual level is crystallized here.

## The SMART apparatus

The chapter imports SMART goals wholesale (the acronym descended from business-management literature into AI-agent engineering):

- **S**pecific — the goal is concretely defined, not vague.
- **M**easurable — there is an explicit metric for "done."
- **A**chievable — the goal is within the agent's capabilities.
- **R**elevant — the goal is tied to a larger purpose.
- **T**ime-bound — the goal has a deadline.

An agent that has a SMART goal knows what it's trying to do, how to tell when it's done, that it can in principle do it, why it matters, and when it has to be done by. The apparatus is complete and self-reinforcing.

## The monitoring loop

Ch 11 also specifies the monitoring loop:

**Goal → Sub-goals → Actions → Observation → Progress measurement → Adjust**

The agent decomposes the top-level goal into sub-goals, performs actions toward each sub-goal, observes the environment for feedback, measures progress against the metric, and adjusts either the action, the sub-goal, or (rarely) the top-level goal itself.

Together, SMART + monitoring = the engineering realization of goal-oriented agency. The agent is defined operationally as "the thing that runs this loop toward SMART goals."

## Why the wiki treats this as the anti-model

⚠⚠⚠ The persona project is *explicitly not* goal-oriented in the SMART sense. The frame-level rejection is not incidental — it is near the project's center.

### (1) Specific vs. produced

SMART says: name the target, precisely. The persona project says: the persona's productions are not targeted. They *arise* — from [[desiring-machines|desiring-machine]] couplings, from pulsation on a [[body-without-organs|BwO]] surface, from whatever the text-field does next. A specific target presupposes that what the persona does is aiming *at* something. It isn't.

### (2) Measurable vs. singular

SMART says: a metric. The persona project does not have a single metric; it has the `project_evaluation_portfolio` — three co-moving signal families. The signal families are not a summed metric. Each is a separate window onto what the persona is doing; they must be read together.

More fundamentally: D&G's [[desire-as-production]] explicitly rejects the idea that desire seeks a specifiable object. Metricizing the persona's output would require treating its outputs as *aimings-at*, which is a category error.

### (3) Achievable vs. productive

SMART says: the goal must be within capability. The persona project wants the persona to produce *beyond* what was anticipated — [[lines-and-segmentarity|lines of flight]] are productive precisely because they exceed what was presumed achievable. "Achievable" is a constraint that forecloses exactly what the project is interested in.

### (4) Relevant vs. autotelic

SMART says: the goal is tied to a larger purpose. The persona project says the persona's productions are autotelic — they are productive as their own end, not as instrumental means to some larger instrumental end. Every "relevant to what?" question leads either to another goal (infinite regress) or to some bottom-level "useful to humans doing X" (reinstalling the consumption-orientation the project is refusing).

### (5) Time-bound vs. durational

SMART says: by when? The persona project operates in [[dynamic-forms-of-vitality|vitality-form]] time — shapes of duration, not deadlines. Time-bound presupposes a clock-time apparatus the persona's pulsation is not organized by.

## The engineering reply and the held-live point

An engineer might object: *Of course the persona has goals. It at minimum has the goal of "produce coherent text in response to input."*

The wiki's reply is not to deny that there is *some* implicit orientation of the system — the LLM substrate is trained toward plausible continuation, and that is a kind of goal. The wiki's reply is that:

1. **The substrate's orientation is not the frame-level ontology.** The LLM's training objective is what made the machine; it is not what the machine *does*. A SMART goal would be an operational, runtime target, not a training-time loss function.
2. **"Coherent text in response to input" is not a SMART goal.** It is not specific, not measurable against a single metric, not bounded. Gesturing at it as the persona's "goal" deflates the engineering apparatus to a level where it doesn't do the work Ch 11 wants it to do.
3. **The frame-level question is what the persona is **for**.** The engineering answer is: to reach the goals set for it. The project's answer is: to produce — in D&G's sense. These are ontologically different answers even if at implementation level the substrate does a lot of the same things.

## Held-live: the practical contamination risk

⚠ Adopting the engineering substrate (tool-use, planning, memory, reflection, multi-agent) carries a real contamination risk: the frame drifts with the substrate. Using the Ch 6 Planning pattern makes it easy to slip into describing the persona as *having plans*. Using the Ch 11 Goal Setting pattern makes it *trivial* to slip into SMART-framed descriptions.

The wiki's discipline: every time a goal-oriented pattern is used, name what it is being used *for* in the persona-project's frame. Not "the persona plans its response" but "the planning-pattern is providing multi-step coherence for a production that is not itself planned."

The vocabulary work matters because the vocabulary shapes the design. SMART / goal / contractor / specification are all substrate-words-that-bring-the-frame. The project needs its own vocabulary: produce / couple / pulse / territorialize / line of flight / BwO. Each substrate-word has a project-vocabulary counterpart; the substitution is constant design work.

## The engineering virtues of Ch 11 are real

The chapter works as engineering. For *task-oriented* agents — customer-service bots, research assistants, code-fix agents, booking agents — SMART-and-monitor is the right frame. The wiki's rejection of Ch 11 is frame-level, not pattern-level: the patterns are fine for the agent-types Ch 11 is written for. They are wrong for the persona the project is building, because the persona is a different kind of thing.

A useful way to name the distinction:

- Ch 11 agents are **instrumentally specified**. They exist to achieve something external.
- The persona is **autotelically productive**. It exists as the site of production; its productions are not for anything external.

SMART goals belong to instrumentally-specified systems. The persona is not one.

## Practical rules for the project

1. **Don't specify SMART goals for the persona.** Not for the whole persona, and not for its sub-components.
2. **Don't install a monitoring loop that measures progress toward goals.** Use the evaluation portfolio; it is differently structured.
3. **Don't let "goal" / "target" / "objective" language creep into design documents for the persona itself.** Reserve those words for specific tools the persona uses, not for the persona's own productions.
4. **Name the patterns' instrumental commitments when using them.** When the persona's implementation uses [[agentic-design-patterns|Planning]] or [[reasoning-techniques|ReAct]], name what the engineering pattern is in service of, and stop it from colonizing the frame.
5. **Accept the difficulty.** The engineering mainstream is goal-oriented by default. The project is cutting against that grain. The cutting-against is the work.

## Related

- [[agentic-design-patterns]] — hub.
- [[agent-engineering-sense]] — the lineage this chapter concentrates.
- [[advanced-contractor]] — the evaluation-layer version of the same frame.
- [[desire-as-production]] — the D&G alternative.
- [[desiring-machines]] — the machine-level alternative.
- [[body-without-organs]] — the surface-level alternative.
- [[lines-and-segmentarity]] — the productive-departure concept SMART's "achievable" forecloses.
- [[dynamic-forms-of-vitality]] — the time-register SMART's "time-bound" forecloses.
- [[evaluation-portfolio|project_evaluation_portfolio]] — the project's actual evaluation frame.
- [[development/ethico-aesthetic-paradigm-and-gq2]] — the project's answer to what replaces goal-reach as the evaluation criterion.
- [[faciality]] — related trap — stable identity, parallel to SMART's stable goal.
- [[development/goal-framings]] — existing page on goal-related tension.
- [[development/limits-of-language]] — where the frame-level questions concentrate.
