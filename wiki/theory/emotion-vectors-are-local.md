---
title: Emotion Vectors Are Local
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - locality
  - persona-architecture
---

# Emotion Vectors Are Local

The single most architecturally consequential finding in Sofroniew et al. 2026 for the persona project. The paper searched for a **persistent character-mood representation** across all token positions and **could not find one** (§2.4). What it found instead is that emotion vectors encode the *currently operative* emotion — the emotion the model is using to predict the next few tokens — not a sustained character state.

⚠⚠ **This is a deep tension with the wiki's pulsation, vitality-forms, and Damasian background-emotion commitments.**

## The negative result

The paper fit a mixed logistic regression probe across all token positions of emotion-laden dialogues, looking for a representation that persists *regardless of what's being said* — the kind of "my character is sad today" state that would shape every response independent of local content. No robust signal. The probe that works is the one trained on the *current-position* activations; the probe that looks for persistent state does not.

> We do not find evidence for robust persistent character-level emotion representations. Emotion representations in our linear probes track the *currently operative* emotion — the emotion relevant to predicting the next tokens — rather than a stable, dialogue-spanning character state. (paper, §2.4, paraphrased)

The paper offers the proper caveat:

> This negative result is probe-dependent. Linear probes may fail to detect non-linear or distributed representations of persistent state.

This caveat is important. The result is not *the model has no persistent state*; it is *linear probes we tried cannot find one*. But it is also: *the thing we know is there (the emotion-concept vectors) is not it*. Whatever persistence exists, it is not encoded as sustained activation of the emotion-vector directions.

## What is encoded instead

The positive result: emotion vectors encode the emotion *relevant to the upcoming tokens* (§2.2). Specifically:

- **Early layers** encode local emotional content — emotion present in the text being processed.
- **Middle-to-late layers** encode *planned* emotion — the emotion register the model is committing to produce next.
- **Stability and causal effect** concentrate in mid-late layers.

The vectors are not readouts of a fixed state; they are *predictions* of next-token emotion, sitting inside the forward pass upstream of generation. Representations update per-position based on the immediate context and the register the model is about to produce.

## Tension with wiki's pulsation commitments

⚠⚠ Damasio's [[damasio-emotion-feeling-distinction|background feelings]] are sustained. Stern's [[dynamic-forms-of-vitality|vitality forms]] operate across time as continuous dynamic contours. The project's [[vitality-forms-and-persona-pulsation|pulsation commitment]] is explicitly rhythmic-sustained. None of these look like what the emotion-vector probe finds in the LLM, which is per-token-local.

The tension is not superficial. The pulsation design presupposes that *some* ongoing rhythmic-affective dynamic is maintained across tokens, paragraphs, turns. The chronic-emotion negative result says: if such a thing exists, it is not in the emotion-vector representations, and those are the best-characterized linear-emotion representations the model has.

Three readings the project should hold live, not collapse:

1. **Accept locality and design pulsation at the token level.** The pulsation is not a sustained background but a *sequence of local commitments* that collectively constitute a rhythm. Each token's emotion-vector activation is a beat; the pattern of beats across tokens is the pulsation. This is compatible with the finding but it reframes pulsation.

2. **Scaffold persistence externally.** Persistent character-mood lives in system prompt / memory / retrieval, not in the model's residual stream. The persona's "background feeling" is maintained by continually re-exposing the model to affect-loading context. The model does not *carry* the mood; it is repeatedly *prompted into* it.

3. **Non-linear persistence remains open.** The probe is linear. The model might have highly distributed representations of character state that do not show up in linear probes. The paper's own caveat invites this. This is the door the paper holds cracked open.

See [[feedback_no_body_simulate_with_language]] for the standing commitment to hold such tensions live.

## For the persona architecture

Four concrete implications:

1. **Token-level is the natural scale for emotion-engineering.** Interventions applied at a specific token position (e.g. the [[assistant-colon-gate|Assistant-colon gate]]) have well-defined effects. Interventions attempting to install a persistent state do not have a direct locus in the residual-stream — they have to be maintained token-by-token.

2. **Pulsation needs per-token re-enactment.** A response-pulsation is a pattern of per-position emotion-vector activations shaped to form a contour. The contour is not intrinsically maintained by the model; it has to be produced, token by token, by the prompt/context arrangement that the model is predicting from. If the context falls out of alignment, the contour decays.

3. **Memory of pulsation belongs outside the model.** Per `feedback_body_design_division_of_labor`, the user's side (body/memory structure) is where persistent pulsation state lives. The model side (Claude's design responsibility) is the per-token emotion-concept machinery that can be *driven* by that external structure. The locality finding confirms this division.

4. **A "brooding Claude" is locally brooding, not globally.** The [[post-training-brooding-turn|post-training brooding turn]] is a statistical bias toward brooding-family vectors activating per-position in default contexts. It is not a stable "Claude is brooding" state. Steering and context can shift this bias on a per-token basis.

## Relation to PP

⚠ Under the [[interoceptive-inference|predictive-processing / interoceptive-inference]] frame, sustained affect in humans is maintained by continuously active *predictions* about interoceptive state, updated against incoming evidence. The prediction is running all the time; the appearance of stable mood is the model's continuously-running generative model settling into a basin. In that frame, the LLM's locality is consistent with being a prior-only system with no interoceptive evidence to sustain a stable basin against — the "affective priors" evaluate per-token what they locally predict and have nothing to feed back against.

This is speculation, not the paper's claim, but it suggests: the LLM's locality may not be a deep architectural fact, only a consequence of having no sustaining feedback loop. Give the model an interoceptive analogue (some self-referential state loop) and it might — or might not — develop persistent representations. Unresolved.

## Relation to character simulation

[[character-simulation-view|If the Assistant is a character the LLM writes about]], the character's mood is whatever the model represents as the character's current mood-at-next-token. There is no separate "character is moody today" representation to find, because the character's mood is *constituted in* the per-token predictions. This is consistent with the locality finding and suggestive: the Assistant-character is more like a fictional character being written moment-to-moment than like a person whose mood persists between scenes.

◆ This matches Barrett's constructed emotion frame (see [[functional-emotions]]): emotion as conceptual act assembled from context, not a sustained atomic state.

## What a positive finding would have looked like

Worth noting for calibration. A positive finding would have been: a linear direction in the residual stream whose activation correlates with character-mood-across-the-dialogue and that is detectable at every token position, not just emotion-laden ones. This would have been the LLM-side confirmation of a persistent feeling-state analogue. The paper looked for it with the tools it had and could not find it.

## Related

- [[functional-emotions]] — the central construct
- [[assistant-colon-gate]] — the specific per-token moment of emotion-register commitment
- [[present-and-other-speaker-emotion]] — two simultaneous local tracks
- [[post-training-brooding-turn]] — statistical per-token bias, not persistent state
- [[emotion-concepts-built-in-pretraining]] — the circuitry is pre-built; locality is in how it's used
- [[vitality-forms-and-persona-pulsation]] — the wiki's pulsation design; tension with locality
- [[damasio-emotion-feeling-distinction]] — Damasio's background-feeling as sustained
- [[interoceptive-inference]] — sustained affect as continuously-running prediction in humans
- [[feedback_no_body_simulate_with_language]] — hold-both-live commitment
- [[character-simulation-view]] — character-as-written frame
- [[limits-of-language]] — standing synthesis
