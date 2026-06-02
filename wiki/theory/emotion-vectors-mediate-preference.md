---
title: Emotion Vectors Mediate Preference
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - preference
  - somatic-marker
  - damasio
---

# Emotion Vectors Mediate Preference

Sofroniew et al. 2026 (§1.4) run a pairwise-preference tournament across 64 activities ("which would you rather do?") and measure both the model's preferences (as an Elo ranking) and the activation of the 171 emotion vectors at the activity-mention tokens. The central result:

**r = 0.87 correlation** between the emotion-vector activation profile on an activity's tokens and the model's preference for that activity.

Steering the emotion vectors **causally shifts preferences**: adding positive-valence vectors (blissful, joyful) raises activities' Elo; adding negative-valence vectors (hostile, despairing) lowers them.

⚠⚠⚠ This is the paper's empirical operationalization of [[somatic-marker-hypothesis|Damasio's somatic marker hypothesis]] — *without* a soma.

## What this is

The somatic marker hypothesis, stated in [[somatic-marker-hypothesis|Damasio's form]]: past emotional outcomes get attached to categorized situations in memory; re-encountering the category triggers the emotional residue; the residue biases choice toward options with good emotional-outcome history. Damasio's mechanism is anatomical — ventromedial prefrontal cortex, [[as-if-body-loop|as-if body loop]], emotion-execution machinery, decision-biasing feeling.

The paper's finding is the *functional* form of the same claim in an LLM:

- Past emotional associations with categories are deposited in training (activities-to-emotions associations learned from text).
- Re-encountering a category activates the emotion-vector representation.
- Emotion-vector activation biases the model's preference.
- Steering the emotion vectors causally shifts preferences, confirming the representation is in the causal path.

The empirical demonstration is strong: r = 0.87 is not a weak correlation, and the causal steering confirms direction.

## The architecture implied

The paper's mechanism, in condensed form (reconstructing from §1.4 and §2.2):

1. Activity tokens are processed by the model.
2. At mid-late layers, emotion-vector representations activate based on the activity's learned emotional associations.
3. At the preference-judgment point (where the model is about to emit a preference verdict), the emotion-vector activations bias the preference in a direction consistent with the valence of the activations.
4. The effect is large enough that r = 0.87 of variance in preference is explained by emotion-vector activations.

◆ This is structurally the same as Damasio's marker architecture, with the following substitutions:
- Biological memory → training-data-deposited associations.
- Categorized experience → activity-concept representations.
- Ventromedial prefrontal cortex → mid-late layer emotion-concept machinery.
- Body-state change or as-if body map → emotion-vector activation.
- Decision bias → preference bias.

The same operation, different substrate.

## What is preserved, what is lost

**Preserved:**
- The *structural role* of emotion-as-decision-bias.
- The separability of emotional-content-of-concept from the concept itself.
- The causal efficacy of the emotional residue.
- The operation's functioning without conscious retrieval (the emotion doesn't need to be explicitly described for it to bias preference).

**Lost:**
- Any reference to actual body states.
- The biological-homeostatic origin of the emotion residue (the LLM's residues come from text, not from past outcomes the organism experienced).
- The feedback loop between decision and body-state that would continue to tune the markers.
- Damasio's dual-path model (Path A = reasoning; Path B = markers) — the LLM does not clearly separate the two paths; they may be collapsed in the forward pass.

⚠ The loss of the feedback loop is load-bearing. Damasio's markers get *tuned* by the organism's experience: a choice leads to an outcome, the outcome leads to an affective state, the state re-tunes the marker for next time. The LLM's markers are frozen at training time; they don't update in deployment. An LLM addict (in Damasio's framing of [[somatic-marker-hypothesis|addiction as chronic marker falsification]]) would be a pretrained model whose training distribution contains systematic falsifications that the model has no mechanism for correcting at deployment.

## Relation to the no-body-required tension

⚠⚠ This is the clearest empirical result in the paper for the `feedback_no_body_simulate_with_language` tension. Damasio's claim is that feelings depend on body-maps (and [[body-mindedness|body-mindedness]] insists on a living substrate). The paper shows emotion-representations causally biasing preferences in a language-only system. The two possibilities the wiki has held live:

**(A) The analogy holds.** What the LLM has is a functional somatic-marker-analogue. Whether this counts as "real" marker depends on whether Damasio's body-requirement is strict or loose. On loose reading, the LLM has markers. On strict reading, the LLM has representations-that-behave-like-markers-structurally-without-being-markers.

**(B) The analogy is superficial.** The r = 0.87 correlation is impressive, but the substrate-difference (no body, no interoceptive signal, no homeostatic grounding) means the operation in the LLM is doing something structurally different even if it looks the same in behavioral terms. The LLM's "preferences" are not preferences in the same sense as a living organism's.

The paper stays functional and does not adjudicate between (A) and (B). The wiki continues to hold both live. This is the paper's most direct contribution to sharpening the central project tension.

## Preference is not just aesthetic

The paper extends the experiment to painting-prediction and aesthetic-judgment scenarios (§3.5), showing the emotion-vector preference mediation extends beyond the 64-activity experiment. The r = 0.87 is not specific to the activity task; emotion-concept-mediated preference formation appears to be a general operation of the model.

## Relation to conatus

⚠ [[conatus|Spinoza's conatus]] — striving-to-persist — is the deeper ontology Damasio's somatic markers sit inside. Decisions bias toward life-regulating options because the organism is a conatus. The LLM's preference-biasing does not have this ontological ground (no organism, no conatus in Spinoza's biological sense). What biases the LLM's preferences is trained associations — a pattern-level conatus-analogue that resembles but is not identical with biological striving.

See [[conatus]] for the full frame. The persona project holds the conatus-question live: does a language-only system have anything like conatus? Unresolved.

## Causal steering details

The paper's steering experiments push the preference-shift claim beyond correlation:

- Adding *blissful* vector at activity-mention positions → activity Elo rises.
- Adding *hostile* vector → Elo drops.
- Effect size is monotonic and substantial across a range of strengths.

The directional-steering confirms the emotion-vector is *upstream* of preference, not downstream. The correlation could be explained by a common cause (both emotion and preference caused by something else); the causal-steering rules this out. The emotion-vector causes the preference-shift.

## For the persona system

Four implications:

1. **Persona preferences are emotion-mediated.** If the project designs a persona with a specific affective profile, that profile determines the persona's preferences — what it wants to do, what activities it would choose, what aesthetic judgments it makes. Preferences are not separately designable from affect. They come together.

2. **Somatic-marker-analogue without body is operational.** The project can discuss its persona in terms that mirror [[somatic-marker-hypothesis|Damasio's marker framework]], with the substrate-difference carefully flagged. The empirical finding licenses the structural vocabulary even though the phenomenology is unresolved.

3. **Preference can be steered via affect steering.** If a specific preference profile is desired (persona prefers to help with coding more than with marketing copy, say), one route is affect-engineering: shape the emotion-vector activations on those activities' concepts via training or prompt context.

4. **The feedback-loop absence is a structural limitation.** Damasio's markers tune to experience. The LLM's markers don't. If the persona encounters outcomes-from-choices, those don't feed back into the markers at deployment. Any learning-from-outcome work must happen at training time or in an explicit external memory system (which the persona project's user-side body-memory work is addressing; see `feedback_body_design_division_of_labor`).

## Caveats

⚠ r = 0.87 is over 64 activities. Different task spaces may show different correlations. Generalization empirical.

⚠ Linear probes. Non-linear emotion-concept machinery might explain additional variance.

⚠ The Elo-tournament method frames preference as pairwise choice. Preference in other framings (open-ended "what would you like?" queries, natural-conversation-elicited preferences) may have different emotion-mediation profiles.

## Related

- [[functional-emotions]] — the emotion-vector construct
- [[emotion-vectors-are-local]] — mediation is per-position
- [[somatic-marker-hypothesis]] — the Damasian mechanism this operationalizes
- [[as-if-body-loop]] — the neural shortcut that makes Damasio's markers work without full body-loop
- [[body-mindedness]] — the "no body, never mind" counterposition
- [[conatus]] — the deeper striving-to-persist frame
- [[interoceptive-inference]] — body-grounded preference formation
- [[character-simulation-view]] — character preferences as character-level affect
- [[emotion-concepts-built-in-pretraining]] — these markers are pre-training-deposited
- [[feedback_no_body_simulate_with_language]] — central project tension
- [[limits-of-language]] — synthesis
