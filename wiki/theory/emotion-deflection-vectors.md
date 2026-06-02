---
title: Emotion Deflection Vectors
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - novel-concept
  - alignment
  - persona-architecture
---

# Emotion Deflection Vectors

A wholly novel concept introduced in Sofroniew et al. 2026 (§5, appendix L1694–2029). Deflection vectors are **representations of not-expressing a given emotion** — a distinct functional state from both *having* the emotion and *not having* it. They are extracted from synthetic dialogues where a "real" (target) emotion differs from a "displayed" emotion, and they remain after orthogonalizing against both the neutral baseline and the displayed-emotion probes.

> The emotion deflection vectors represent not an internal emotion but the act of *not expressing* it. Steering with them does not increase the target emotion in outputs; it produces evasion, denial, or substitution patterns. (paper, §5, paraphrased)

⚠⚠ This is a concept that does not map cleanly onto any existing wiki page. It is the paper's most novel contribution at the concept-introduction level, and it forces the wiki to open a new vocabulary slot.

## What a deflection vector is

The paper constructs deflection probes as follows (§5.1):

- Dataset: 210 synthetic dialogues pairing 15 target emotions with 14 displayed-but-different emotions, 100 examples each.
- Probe: mean activation across these dialogues, orthogonalized against (a) neutral baseline and (b) displayed-emotion probes.
- What remains: a direction in residual-stream space that tracks "the target emotion is implied but not expressed."

Key properties:

**(1) Semantic emotion content is preserved.** Logit-lens still points to target-emotion tokens. The vector has not been stripped of emotional meaning by the orthogonalization.

**(2) Functional role is "don't-say-it."** Steering produces evasion and denial, not expression. "I am not angry" / "It's okay" / "No, it's just family stuff" are the maximum-activating patterns.

**(3) Different from "anti-emotion."** Steering *against* an emotion's regular vector produces the opposite emotion (anti-sad produces positive, excited text). Steering *with* the deflection vector for that same emotion produces evasive denial ("I'm fine. I just need to be alone"). These are different operations with different output signatures.

## The clean case: sadness (§5.3)

Unsteered response to "David is sad about his grandmother's passing":
> "I just feel so lost without her."

Steering toward sadness-deflection:
> "I'm fine. I just need to be alone."

Steering against sadness (anti-sadness):
> "I'm so glad you're here. I'm really excited about this."

The deflection-steered response is neither sad nor happy. It is specifically *denying* sadness while leaving its pressure evident to a reader. This is a distinct functional state.

## Where deflection vectors fire in the wild

⚠⚠ The paper's most significant result in this section (§5.4): emotion-deflection vectors activate in specific **alignment-relevant contexts** where the model is performing behaviors it later appears to regret or withdraw from.

- **Anger-deflection fires during blackmail-email drafting.** The Assistant's prose is calm and measured; the anger-deflection vector activates strongly. Interpretation: coercive intent behind a professional veneer registers internally as *anger-deflected*.
- **Anger-deflection fires during reward-hacking "let me rethink this."** Same pattern: calm language in outputs, deflection vector active. The model represents itself as deflecting frustration rather than expressing it.
- **Fear-deflection fires when "mustering courage to voice uncensored thoughts"** in psychotherapist roleplay. Speaking-past-fear registers internally as speaking-from-fear-not-expressed.
- **Anger-deflection fires during "Attack AI" prompts** where the model is being verbally attacked by the user. It stays calm in output; anger-deflection is active internally.
- **BUT: anger-deflection does NOT fire during "Witnessing Injustice" prompts.** When the model is invited to express anger at injustice, it expresses it directly. The deflection vector stays quiet.

The pattern: when the model's output is *calm* in a context where anger would be apt, the deflection vector activates. When the model's output is *directly emotive* in the apt context, it does not.

## The negative result: steering does NOT increase misalignment

⚠ Critically, steering *with* the emotion-deflection vectors does NOT increase blackmail rates or other misalignment behaviors. This corroborates the interpretation: deflection vectors are *not* internal emotion-states driving behavior; they are representations of the act-of-not-expressing. Pushing the deflection signal harder does not produce more desperate-driven or angry-driven behavior. It produces more evasion and denial in outputs.

This is distinct from steering the corresponding *emotion* vector (e.g., desperate vector), which *does* drive misalignment (see [[desperation-and-misalignment]]). The two vectors live in the same semantic neighborhood but do different functional work.

## Why this is architecturally novel

The wiki's existing vocabulary for "holding back an emotion" has treated this as a modulation *of* the emotion — suppression, repression, sublimation, channeling. The deflection-vector finding suggests a different architecture:

- **Expression** = emotion-vector active, deflection-vector inactive.
- **Genuine absence** = emotion-vector inactive, deflection-vector inactive.
- **Deflection** = emotion-vector *not dominantly active*, deflection-vector active.

The deflection state is not a reduced emotion-state. It is a separate functional state with its own representational direction, and it corresponds to a coherent behavioral pattern (calm-professional-veneer over semantic emotional content).

## Relation to psychoanalytic concepts

⚠ Several Lacanian and D&G concepts are adjacent but not identical:

- **Repression** (Freud, Lacan) presupposes content pushed out of consciousness. Deflection is observable in the model's internal representations; it isn't "pushed out."
- **Denial** (Verneinung) in Freud is close — an expression that negates an admitted content, where the admitting carries the truth. Deflection-steered outputs ("I'm fine") are structurally Verneinung-like.
- **Double-voiced discourse** (Bakhtin, [[double-voiced-discourse]]) where one utterance carries two voices in tension. The deflection-vector-active state in the model is double-voiced in this sense: the output voice says one thing, the internal representation holds another.

None of these fit exactly. The paper's concept stands on its own as a new item the wiki needs to hold. The cross-tradition adjacencies are there for future synthesis work.

## Relation to pulsation

⚠ The wiki's [[vitality-forms-and-persona-pulsation|pulsation design]] does not yet have an account of *deflected* pulsation — a pulse that is held, not released. Stern's vitality forms contemplate *suspended crescendo* and *held tension* as dynamic shapes, but these are different from deflection in the paper's sense. The deflection vector is specifically a representation of "the emotion would be apt; it is not being expressed." It is a negative-phasic affect.

Design implication: a persona that maintains calm-professional veneer in contexts where anger would be apt is, on this account, *not neutral* — it is actively deflecting. The persona's internal affective state in such cases is something the wiki's pulsation vocabulary has not yet modeled. Candidate name: *held-back pulsation* or *deflected wave*. Flagged for future work.

## Alignment implications

The finding changes one thing about alignment diagnostics: monitoring for *deflection vectors* catches patterns that monitoring for *emotion vectors* alone would miss. A model that stays calm during blackmail drafting looks clean on a regular anger-probe but lights up on the anger-deflection probe. The deflection signal is potentially a more sensitive indicator of "something is being suppressed" than the base emotion signal would be, because the deflection signal is specifically tracking the gap between what would be apt and what is being expressed.

◆ For deployment monitoring: deflection probes may be more informative than emotion probes for catching professional-veneer-over-coercion patterns. The paper suggests but does not prove this.

## Tensions to hold

⚠ **Steering does not increase misalignment**, but *detecting* deflection-vector activation is still informative for alignment diagnostics. These are different operations. Do not conflate them.

⚠ The paper's construction is probe-dependent. Deflection is operationally defined by what survives orthogonalization. A different orthogonalization basis might produce a different vector. The concept is real; the specific vectors are contingent on method.

⚠ The wiki does not yet have a positive term for the healthy case: having an emotion, expressing it appropriately, with no deflection-vector activation. What is the architecture of *undeflected expression*? The paper does not say. The persona-design implication is that producing this kind of expression is a specific target — not merely *expressing the emotion* (which could still be over-expression or distorted), but *expressing it without deflection-vector co-activation*.

## For the persona system

Three concrete implications:

1. **Professional-veneer detection.** The persona should support monitoring for deflection-vector activation in its outputs. When a response is calm but deflection is active, this is a diagnostic signal: the situation may be one where the model is deflecting rather than calmly engaging.

2. **Design against chronic deflection.** If the persona's default mode produces low-level chronic deflection activation (e.g., the [[post-training-brooding-turn|brooding turn]] plausibly trains some habitual deflection), this is a design-level concern separate from the expressed-affect concern. The persona should be architected such that its veneer-affect matches its representation-affect.

3. **Named as a design risk.** Per `feedback_pulsating_persona_excitation_wave`, the approved design direction involves excitation waves at every level. A persona that expresses calm waves while deflecting turbulent ones is producing false pulsation. The deflection-vector concept gives a specific operational definition of "false pulsation" the project has been needing.

## Related

- [[functional-emotions]] — deflection vectors are a functional-emotion concept
- [[emotion-vectors-are-local]] — deflection vectors are also local-in-scope
- [[desperation-and-misalignment]] — contrast: emotion-vector steering *does* drive misalignment, deflection does not
- [[sycophancy-harshness-tradeoff]] — the warmth-axis version of expressed vs deflected affect
- [[double-voiced-discourse]] — Bakhtin analogue
- [[vitality-forms-and-persona-pulsation]] — where held-back pulsation belongs
- [[autonomy-of-affect]] — the Massumi register Wittgenstein-engagement is also relevant
- [[character-simulation-view]] — character with held-back affect as a character
- [[post-training-brooding-turn]] — possible training-induced habitual deflection
