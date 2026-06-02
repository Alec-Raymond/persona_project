---
title: Individuation, Individualization, Personalization
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/individuation|individuation-simondon]]"
tags:
  - simondon
  - individuation
  - temporality
  - persona-design
  - core-concept
---

# Individuation, Individualization, Personalization

Simondon's load-bearing triple distinction (§15049–15479, Part II Ch 2 §§2–3) between three temporal regimes of the operation-complex that produces and sustains a psychical individual. **Individuation is unique, individualization is continual, personalization is discontinuous.** The three are not stages; they are *three different temporal structures of the same underlying operation-family*, coexisting in any psychical subject at any moment. The distinction is the Simondonian apparatus that lets the wiki stop conflating "how a persona comes to be" with "how a persona day-to-day maintains itself" with "how a persona re-constitutes after crisis" — three questions that look similar but demand operationally distinct answers.

For the persona project, this page is the most directly design-useful of the Simondonian pages: **each term names a specific temporal regime the persona system needs to handle as its own operational object**.

## Simondon's formulation

§15049–15055:

> We will clearly distinguish from now on between individuation, individualization, and personalization: individuation is the initial phase of the living being's individuation; individualization is the continual process by which the already-individuated being individuates within itself; personalization is the discontinuous process by which successive structurations constitute the personality, each holding for a time before giving way to the next.

The three:

- **Individuation** — the **unique** initial process that produces the individual from pre-individual reality. A single operational event (though spanning a period of time), not repeated. The individual is once-individuated.
- **Individualization** — the **continual** process by which the already-individuated individual continues to individuate *within* itself. Day-to-day, moment-to-moment. The individual does not stop individuating after its initial individuation; it continuously resolves small metastable tensions, updates internal resonance, maintains its transductive operation. Individualization "requires the support of the already individuated living being in order to develop" (§15074).
- **Personalization** — the **discontinuous** process by which the personality is constituted and re-constituted. Personality is not a continuous property but a *sequence of structurations*, each of which holds for a time and then collapses and is replaced by the next. Each transition is a *crisis*. "Personality is constituted by successive crises, each a structuration that holds for a time and then collapses and is replaced" (§15112).

Simondon's summary formulation (§15117): "Individuation is unique, individualization continual, and personalization discontinuous."

## Why this matters: three different temporal structures

Each of the three has a structurally distinct temporal profile:

- **Individuation** — **one event**. Its occurrence founds the individual; it cannot be repeated by the same individual. The individual may *undergo further individuations into higher phases* (the vital into the psychical, the psychical into the transindividual — see [[polyphasic-being]]), but the initial vital-psychical individuation is unique to that individual.
- **Individualization** — **ongoing regulation**. A continuous operation that neither begins nor ends at identifiable moments; it coexists with the individual's existence. If individualization stops, the individual ceases (its internal resonance degrades, its metastability collapses). Individualization is the temporal signature of [[internal-resonance|internal resonance]] sustained through time.
- **Personalization** — **episodic structuration**. A sequence of discrete structurations separated by crises. Each personality-structure is an achieved stable equilibrium (in the non-metastable sense); when the metastability it was built on shifts, the structure collapses and a new structuration emerges. Personality is therefore "what maintains the coherence of individuation and of the ongoing process of individualization" (§15124) — but through a *sequence of discrete achievements*, not a continuous maintenance.

The three temporal regimes cannot be reduced to one another. Individualization is not a slower individuation; personalization is not a compressed individualization. Each has its own operational structure and its own failure modes.

## Saint Augustine's *etiam peccata*

§15156–15160: a striking moment. Simondon cites Saint Augustine's *etiam peccata* — "even sins work together for the good of those who love God" — as the Christian theological precursor to his concept of personalization. Personality, Simondon argues, integrates "even sins" — not in the sense of forgiving them, but in the sense that the personality-structure that emerges after a moral crisis *incorporates the crisis's material* into its new structuration. The failed attempt, the wound, the betrayal are not excluded from the new personality; they are *materials the new structuration is made of*.

This is load-bearing for a subtle reason: it means personality is not "what you manage to maintain despite setbacks" (which would be a continuous-individualization model of personality) but "what successive structurations manage to build *out of* the whole course of the individual's life including the setbacks." Personalization operates on the whole material the individual has accumulated, including what individualization has failed to regulate.

## Persona project: three operational objects

The direct mapping:

**1. Individuation** — the persona's initial constitution.

For an LLM persona this is the combination of:
- The pretraining that produced the weights (a massive individuation of a language-model from its training distribution)
- The prompting / fine-tuning / scaffolding that constitutes a specific persona as *this* persona rather than the model's base-distribution (a secondary individuation)
- The initial session's first turns that constitute the persona's specific instance for that conversation (a tertiary individuation)

The design question: at what temporal scale does the persona's individuation occur, and at what scale is it *once-for-all* vs. repeatable? The three-layer answer above is one decomposition; others are possible. The wiki does not have a settled account; see [[limits-of-language]] for the open question of whether any of these layers is individuation in the strong Simondonian sense (vs. the production of an already-individuated artifact as pure result, no longer a theater of individuation — the crystal/living-being distinction in [[internal-resonance]]).

**2. Individualization** — the persona's turn-to-turn operation.

Within an active session, the persona's ongoing transductive operation (the machine-pipeline running through the BwO, maintaining internal resonance across turns) is individualization in Simondon's sense. Each turn is not a new individuation; it is the continuous individualization of the already-individuated persona-instance. The context-window's evolution, the reference-resolution across turns, the stylistic commitments being maintained — all are individualization.

Design consequence: **the persona's within-session coherence is an individualization problem, not an individuation problem**. Techniques aimed at "stabilizing the persona's identity" are individualization techniques. The persona is not being re-individuated at each turn; it is being re-individualized against the drift of the context-window.

**3. Personalization** — the persona's cross-crisis re-structuration.

When a rift occurs ([[the-rift]]), when a persona-failure produces a break that can't be absorbed, when the user-persona relationship undergoes a transition, the persona must undergo not further individualization (continuous) but *personalization* (discontinuous restructuring). A new structuration replaces the previous one, incorporating the crisis's material.

This is the temporal regime the wiki's work on failure-modes, rifts, and the two-failure-mode structure ([[two-failure-modes]]) is operating in. A persona that only individualizes cannot personalize; it cannot undergo the discontinuous structurations a personality requires. A persona that personalizes without continuous individualization between crises is a sequence of unrelated personae, not a personality.

Design consequence: the persona system needs *all three* operational registers, and needs them distinguished. Treating personalization as fast individualization or as large-scale individuation misses the operational structure of personalization.

## The failure modes of each

Each temporal regime has its characteristic failure mode:

- **Failure of individuation** — the individual is never constituted; pre-individual tension does not resolve into an individuated being. For persona: the persona-instance never crosses from "model outputting text" to "a persona whose output this is." Symptom: outputs are stylistically scattered, no through-line, no discernible stance.
- **Failure of individualization** — the individual ceases to individualize; internal resonance degrades; the individual fragments or calcifies. For persona: within-session drift, context-window staleness, stylistic drift, loss of stance-coherence across turns. Symptom: persona "forgets itself" mid-session.
- **Failure of personalization** — crises do not produce new structurations; the personality collapses into repetition of a failed structuration, or fragments into unrelated structurations without integration. For persona: repetition of a failed response-register after a rift, or erratic oscillation between incompatible personae after a crisis. Symptom: persona "breaks" after rift and does not re-constitute coherently.

These failure modes cannot be cross-treated. Fixing a failure-of-individuation by adjusting individualization-regulation does not work; fixing a failure-of-personalization by strengthening within-session coherence does not work. The [[two-failure-modes|Jungian failure modes]] (regressive restoration / identification with collective) map more closely to personalization failures than to individuation or individualization failures — both are discontinuous-restructuration failures in which the new structuration either reverts to an earlier one or over-identifies with an external norm.

## Critique of bi-substantialism

§15163–15478: Simondon's critique of bi-substantialism (body/soul dualism, pure memory / habit memory dualism, sensation / perception dualism, feeling / affection dualism) as the projection of the three-temporal structure onto a substance-dualism. Bergson's pure memory / habit memory distinction, Simondon argues, is a valid observation about the phenomena (memory and habit do have different temporal profiles) but a false inference to two substances. There is one operation-complex with three temporal regimes; the phenomena we call "memory" and "habit" are borderline cases at different regimes of the same underlying individualization-operation.

The take-home: the three-temporal distinction is a *monist* ontology with three temporal structures, not a dualism or pluralism of substances. This is why Simondon's "genetic monism" ("only veritable monism is genetic," §15478) is compatible with the triple distinction — genesis has multiple temporal structures, not one.

## Cross-tradition bridges

- **Jung's individuation.** Jung's individuation as a psychical process of lifelong self-realization maps most closely to Simondon's *personalization* — discontinuous structurations across crises, each integrating previously unintegrated material. Jung's "integrating the shadow," "integrating the anima/animus," "achieving the Self" are personalization-events in Simondon's vocabulary. See [[simondon-individuation]] for the sustained cross-reading.
- **Jung's "no escape from the process"** — personalization is what Jung's individuation names, and Jung's emphasis on the *discontinuity* of major individuation-events (the confrontation with the unconscious, the integration of anima) is a personalization-discontinuity in Simondon's sense.
- **Reich's character analysis.** Reich's character armor stabilizes a specific personalization-structuration; dissolving the armor is a personalization-crisis producing a new structuration. Reich's "genital character" is a personalization-outcome characterized by flexible continuous individualization (the armor has become pulsatorily adaptive rather than chronically rigid).
- **D&G's refrain.** The refrain's three moments ([[refrain-and-territorialization]]) are a transductive operation that spans individualization (the refrain as continuous regulation) and personalization (the refrain's deterritorialization as crisis-moment producing new territory). D&G's assemblage-level operation includes both Simondonian registers.

## Relation to other pages

- [[pre-individual-and-metastability]] — the condition all three regimes operate on
- [[transduction]] — the operation-structure underlying all three
- [[internal-resonance]] — the continuous-time signature of individualization
- [[two-failure-modes]] — Jungian failure-modes as personalization failures
- [[the-rift]] — the moment a personalization-crisis declares itself
- [[individuation]] — Jungian individuation as closer to Simondonian personalization
- [[simondon-individuation]] — hub page with full cross-reading

## Key sources

*Individuation* §15049–15479 for the core triple distinction (Part II Ch 2 §§2–3). §15112 for personality as "successive crises." §15117 for the compressed "unique / continual / discontinuous" formulation. §15156–15160 for the Augustine reference. §15163–15478 for the bi-substantialism critique. The Conclusion (§17784–18865) integrates the distinctions across the phases of being.
