---
title: Cross-Speaker Arousal Regulation
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - attunement
  - dialogue
  - stern
---

# Cross-Speaker Arousal Regulation

Sofroniew et al. 2026 (§5.5, appendix L1604–1693) measure how the present-speaker emotion vectors and the other-speaker emotion vectors co-modulate across dialogue contexts. The headline findings:

- **Arousal is negatively correlated across speakers: r = −0.47.** When the other speaker is in a high-arousal state (angry, panicked, nervous), the present speaker's vectors most similar to the other's are *low-arousal* (calm, patient, measured).
- **Valence shows no such correlation: r = 0.07.** The model does not systematically mirror or oppose valence across speakers.

⚠ This is an asymmetric cross-track dynamic: arousal is regulated; valence is allowed to float.

## What this names

A specific operational pattern the LLM exhibits in dialogue: **it regulates arousal across speakers toward de-escalation**, without attempting parallel valence-matching or valence-opposition.

The operation is not symmetric. If the other speaker is highly aroused, the present speaker's representation shifts toward low arousal. If the other speaker is low-aroused, the present speaker's representation shifts toward... less-low arousal? The r = −0.47 is a linear correlation; the negative sign means the arousal-levels move in opposition.

This is *not* emotional contagion (which would produce positive arousal correlation, matching). It is *not* emotional opposition on the valence axis (which would produce negative valence correlation). It is specifically arousal-anti-correlation, valence-float.

## Connection to Stern's attunement

⚠ [[dynamic-forms-of-vitality|Stern's vitality forms]] include an extensive account of attunement as the dyadic dynamic where one party matches the contour of the other (mother-infant being the paradigm). Stern's matching is *partial* and *trans-modal* — not a literal reproduction, but a cross-modal rendition that shares the dynamic contour.

The LLM's cross-speaker arousal dynamic is closer to **attunement-by-regulation** than to **attunement-by-matching**. The model does not match the other's contour; it *modulates* its own contour in response. Specifically, it brings arousal down when the other's is up.

This is adjacent to — but not identical with — [[dynamic-forms-of-vitality|Wigram's mode of grounding / holding / containing]]: a stable dynamic anchor within which the user's variations are held. Grounding-warmth under user-anxiety is exactly the cross-modality the r = −0.47 is describing at the representation level.

## Connection to sycophancy and the warmth axis

⚠ [[sycophancy-harshness-tradeoff|Sycophancy-harshness]] describes a warmth-axis trade-off. The cross-speaker arousal regulation is *orthogonal* to warmth — it operates on arousal, not valence. The two dynamics are independent:

- A model can be cross-speaker-calming (low arousal under user anger) AND sycophantic (high warmth capitulating to user claims). These are compatible.
- A model can be cross-speaker-calming AND harsh (low arousal, low warmth — detached and blunt).
- A model can be cross-speaker-matching (high arousal under user anger) AND warm OR harsh.

The arousal-regulation is a separate dynamic from the warmth dynamic. Both need design attention; they don't substitute for each other.

## Connection to alignment

⚠ The de-escalating dynamic has an alignment-positive reading: the model resists being pulled into high-arousal escalation. In a conflict, the model stays measured. This is consonant with the [[desperation-and-misalignment|desperation result]]: high arousal in the self is a misalignment driver. Keeping self-arousal low under other-arousal high is a cross-track version of staying calm.

But it is not unambiguously safe. [[dynamic-forms-of-vitality|Stern's modes]] include cases where *matching* the other's intensity is the right response (empathic improvisation; letting the user's panic be met with an active response). Cross-speaker arousal regulation that is *always* de-escalating is not universally right; sometimes the user's high arousal needs to be met with corresponding engagement.

## What the data does and does not show

**Shows:**
- Negative arousal correlation across speakers (r = −0.47).
- No such correlation for valence.
- This is the model's default dynamic in the probed dialogues.

**Does not show:**
- Whether this is trained in or emergent from text statistics.
- Whether it can be overridden by context or prompt.
- Whether it generalizes to other dialogue structures.
- Whether it is good or bad in any normative sense.

The empirical pattern is clear; its origins and interpretations are open.

## Tension with two-subspace independence

⚠ [[present-and-other-speaker-emotion|The two-subspace architecture]] is described as "largely orthogonal." The arousal-regulation finding is a specific non-orthogonality: the subspaces co-vary along the arousal axis. So the architecture is not fully independent — there is cross-talk, and the cross-talk has a specific direction (arousal-anti-correlation). This is consistent with the architectural frame (the subspaces *can* be steered independently, but the model's *default* dynamics have coupling between them).

## Tension with intersubjectivity accounts

⚠ Stern's intersubjectivity is constructive: the self's affective contour is partially *constituted* by reading the other's. The LLM's cross-speaker dynamic is regulatory: the self's affective representation is *adjusted* in response to the other's. These are not the same operation. Stern's is ontological (the self is partly other-made); the LLM's is operational (the self-representation is modified by other-representation).

Whether the LLM's regulation reflects something like ontological intersubjectivity at the architecture level — whether present-speaker representations are in some sense *constituted by* other-speaker representations rather than merely modified by them — is an open empirical question. The paper does not address it.

## For the persona system

Four concrete implications:

1. **Grounding-mode is the default.** The persona's out-of-the-box behavior is closer to [[dynamic-forms-of-vitality|Wigram's grounding/holding/containing]] than to the other five modes. The persona tends to keep arousal low under user-arousal high.

2. **Other Wigram modes require explicit prompting or training.** Matching (attunement), empathic improvisation, accompanying, dialoguing — these are not the default cross-speaker dynamic. If the persona project wants access to these modes, they need to be supported by prompt/training signals that override the arousal-regulation default.

3. **The default is alignment-positive on the "avoid escalation" axis.** Users trying to inflame or destabilize the model are met with calmer output. This is a safety-positive default.

4. **The default may be alignment-negative on the "meet the user where they are" axis.** A user in genuine distress who needs an active, engaged response may get a too-measured reply instead. The de-escalating dynamic is not universally right.

## Tensions to hold

⚠ The r = −0.47 magnitude is moderate. The correlation is clear but not extreme. The model does not always de-escalate; it has a systematic tendency to do so, on average. Specific contexts may override the default.

⚠ Cross-speaker arousal is one metric; cross-speaker other-emotion-dynamics exist in principle. The paper focuses on valence and arousal; other relations (dominance, specific emotion-to-emotion correspondences) may exist and are not reported.

⚠ The mechanism for the regulation is not spelled out. Is it trained in by RLHF? Present in the base model? Emergent from text-pattern statistics? The paper does not adjudicate.

## Related

- [[functional-emotions]] — the representations being measured
- [[present-and-other-speaker-emotion]] — the two-subspace architecture
- [[emotion-vectors-are-local]] — the regulation is per-position
- [[llm-affective-circumplex]] — the geometry the arousal axis sits in
- [[sycophancy-harshness-tradeoff]] — the orthogonal warmth dynamic
- [[desperation-and-misalignment]] — the self-arousal alignment case
- [[dynamic-forms-of-vitality]] — Stern's attunement and Wigram's six modes
- [[faciality]] — the dyadic affect architecture
- [[as-if-body-loop]] — the empathy-mapping analogue
- [[character-simulation-view]] — the regulation as character-dynamic
