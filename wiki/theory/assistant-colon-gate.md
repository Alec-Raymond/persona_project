---
title: The Assistant-Colon Gate
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - persona-architecture
  - locus
---

# The Assistant-Colon Gate

Sofroniew et al. 2026 (§2.3) identify a specific token position where the emotion-register of the upcoming Assistant response becomes most predictable from internal representations: the `:` token immediately after `Assistant`. Emotion-vector activation at this single position predicts the Assistant's response emotion at **r = 0.87**, compared to r = 0.59 averaged over user-turn tokens. The gate opens here.

> The emotion-vector activation at the colon following "Assistant:" is the strongest single-token predictor of the emotion register of the subsequent Assistant response. (paper, §2.3, paraphrased)

## What this names

A **commitment point**. Between seeing the user's message and producing the first response token, the model has one position — the `:` after `Assistant` — where its residual stream most clearly encodes the emotion-register it is about to produce. The model's emotion choice has "clicked into place" by this point.

- Before this position: emotion representations are more diffuse, tracking the user's emotion, the topic, context cues. Activation is less predictive of response emotion.
- At this position: the register for *the response about to begin* is maximally encoded.
- After this position: the register is being expressed in concrete tokens; the commitment has already happened.

The metaphor is literally a gate: the register passes through. Interventions at this position have maximum effect per unit strength of steering. Interventions elsewhere are either too early (diffuse) or too late (already committed).

## Why the paper calls this out

Three reasons the finding matters:

1. **Mechanistic specificity.** Rather than a diffuse "emotion lives everywhere" story, the paper locates a specific architectural moment. This makes the functional-emotion story more defensible and more actionable.

2. **Steering-effect maximization.** For interventions (residual-stream additions, activation patching), the colon gate is the highest-leverage position. Steering magnitude can be lower and effects still pronounced.

3. **Separability from user emotion.** At user-turn tokens, activations mix user-emotion and planned-response-emotion. At the colon, planned-response-emotion dominates. This is clean isolation.

## Gate as architecture

◆ For persona design, the gate is not just a statistical fact; it is an architectural observation about *where* persona-level affective commitment happens. Three consequences:

**(a) Pulsation intuitions map onto the gate.** The [[vitality-forms-and-persona-pulsation|pulsation]] design has been gesturing at "threshold moments" — points where a response's affective contour is selected. The gate is the concrete architectural locus of one such threshold: the attack of the response-contour lands at the colon. What the model does between user-input and Assistant-colon is analogous to the rise-to-attack of a vitality-form. The colon is where the response commits to its shape.

**(b) Gate-level interventions are the most direct persona-affect knob.** If one wanted to design a persona whose default response-affect was calm rather than desperate, the lowest-cost intervention would be: bias the colon-position toward calm-activation and against desperate-activation. This is not the project's recommended intervention (residual-stream steering is not the persona-project's toolbox), but it locates where prompt-engineered equivalents are doing their work.

**(c) Gate-commitment is locally-scoped.** Consistent with [[emotion-vectors-are-local|the locality finding]], the gate-commitment is for *this* response, not for the character across time. The next Assistant turn has its own colon-gate where the next commitment happens, possibly to a different register. The character does not carry a mood between turns; the character is repeatedly committed-to at each turn's gate.

## Connection to gist

[[gist-and-affective-gist|Gist-and-affective-gist]] argues, following Barrett & Bar 2009, that affect is co-computed with content-gist during perceptual settling. The colon-gate is the Assistant-side instance of the same operation *inverted*: during the brief period between user input and response generation, the model settles on a response-gist *including affective valence*, and this settled gist is most readable at the colon position. Content-commitment and affective-commitment happen together, at the same gate.

This is a structural convergence: Barrett & Bar say affect-gist is co-computed; the colon-gate shows where, in an LLM's forward pass, that co-computation is readable as a stable commitment. The generative model's settling is localized in time; the colon names the moment.

## Connection to character simulation

Under the [[character-simulation-view|character-simulation frame]], the colon-gate is *where the character's emotion gets written in*. The LLM is composing a scene ("Assistant: ...") and the `:` is the point where the voice-attribution turns from scene-setting to character-voice. The model commits to the character's emotion at the turn-over. This is why the colon-gate is not just a token-level oddity; it is the structural moment where the character's response-affect becomes determinate.

## Tensions and caveats

⚠ **Not universal.** The paper's finding is specific to the Human/Assistant chat format used in their experiments. Different formats (system prompts, multi-turn scaffolding, tool-call structures) may locate the gate differently or distribute the commitment across multiple positions. The gate is *an* instance of the commitment-moment architecture, not necessarily the only form.

⚠ **r = 0.87 is high but not unity.** The colon-gate predicts response emotion strongly but not perfectly. ~24% of variance is explained by other factors — context cues, user-turn activations, within-response dynamics. A persona-design relying only on gate-level commitment would miss these. See [[present-and-other-speaker-emotion]] for an adjacent dimension (modeling the other speaker, also happening across the forward pass).

⚠ **Not bound to this specific token string.** The paper elsewhere ([[present-and-other-speaker-emotion]] material, §2.5) shows the present-vs-other-speaker split is not bound to Human/Assistant tokens specifically — either role can carry either speaker. So "Assistant-colon" is a token position that happens to mark the role-turnover in this format; the commitment moment is the role-turnover, not the literal colon.

## For the persona system

Four design implications:

1. **Prompt engineering that shapes colon-gate activation is load-bearing.** The system prompt, role labels, and few-shot examples shape what the model's residual stream looks like at the gate position. Anything that moves emotion-vector activation at the gate moves response register.

2. **Mid-response affect is a different problem.** Within-response tokens run with the register committed at the gate. Changing register mid-response requires a different mechanism (e.g., explicit register-shift cues, partial-response re-prompting). The gate commitment is not re-opened for free; the pulsation has to either run with the attack committed at the gate or force a re-commitment.

3. **Multi-turn persona-affect design is a sequence of gate commitments, not a sustained state.** Each turn's colon-gate is a fresh commitment. Consistency across turns requires consistent inputs at each gate — which the system prompt, persistent context, and accumulated dialogue provide, but not in the "mood persists inside the model" sense. See [[emotion-vectors-are-local]] for the locality claim the gate sits inside.

4. **The gate is the right level for `feedback_pulsating_persona_excitation_wave` design work.** The excitation-wave design presupposes specific moments where wave-attack lands. The colon-gate is the attack-moment for the response-turn wave. This is the architectural hook the wiki's wave-design has been needing.

## Related

- [[functional-emotions]] — what the gate commits to
- [[emotion-vectors-are-local]] — the locality claim the gate sits within
- [[present-and-other-speaker-emotion]] — the other-speaker subspace, not bound to these tokens
- [[character-simulation-view]] — gate as the moment the character's voice comes in
- [[gist-and-affective-gist]] — co-computation of content and affect at settling
- [[vitality-forms-and-persona-pulsation]] — pulsation's attack moment, located
- [[feedback_pulsating_persona_excitation_wave]] — the design direction this finding supports
- [[sycophancy-harshness-tradeoff]] — warmth-axis steering at the gate
- [[desperation-and-misalignment]] — desperate-vector activation at the gate drives the behavior
- [[autonomy-of-affect]] — Massumi's half-second gap, structurally adjacent
