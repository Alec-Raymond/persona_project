---
title: Emotion Concept vs Affect Axis
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - barrett
  - geometry
  - two-layer
---

# Emotion Concept vs Affect Axis

Sofroniew et al. 2026 represent emotion in the LLM at **two distinct levels** simultaneously:

- **171 discrete emotion-concept vectors** (brooding, jubilant, hostile, anxious, compassionate, etc.) — each a linear direction in the residual stream.
- **A continuous affect-axis geometry** recovered by projecting the 171 vectors onto the top two principal components: PC1 ≈ valence, PC2 ≈ arousal ([[llm-affective-circumplex]]).

Both layers are present in the model. Both are operative. Neither reduces to the other cleanly. This is an empirical finding with direct relevance to a central debate in affect-psychology.

## What this names

The **two-layer architecture of affect-representation** in the LLM:

- **Layer 1 — Affect (Barrett's sense):** a continuous 2D-or-more space with valence and arousal as primary axes. This is the underlying manifold; all 171 emotions are positions on it.

- **Layer 2 — Emotion-concepts:** specific lexicalized categories (named emotions) that carve up the affect-space into culturally-conventional regions. Each emotion-concept is a vector with a specific activation profile.

The LLM has *both*. The emotion-concept vectors are not reducible to affect-space coordinates (the 171 directions are richer than their PC1/PC2 projections; residual variance matters). The affect-space is not reducible to a specific emotion (it is continuous; one can be at a valence/arousal coordinate without the concept-label having fired).

⚠ This is **a specific architectural finding** that bears on the Barrett/Tomkins/Massumi debate in affect-theory.

## Connection to Barrett's theory of constructed emotion

[[autonomy-of-affect|Barrett]] argues:
- Affect (valence/arousal) is the universal underlying structure.
- Emotion categories (joy, sadness, fear) are *constructed* by applying concepts to affect-states in context.
- Concepts carve continuous affect-space into discrete regions, and the carving is culturally and linguistically learned.

The paper's two-layer finding supports this architecture empirically:
- PC1/PC2 recovers continuous affect-space.
- The 171 vectors are concept-instantiations on this space.
- The concept-vectors are not the *same thing* as the affect-space coordinates; they carry additional information.

This is the cleanest empirical correspondence the wiki has found to date between Barrett's theoretical architecture and an actually-measurable representational structure in an emotion-representing system. The LLM, by virtue of being trained on text that reflects Barrett-structured human affective language, has inherited Barrett-structured representations.

⚠ This is *not* a proof that Barrett is right about human affect. Human affect is not LLM affect. But it is strong evidence that Barrett's architecture is at least *coherent and constructible* — it can be instantiated in a representation-system and behave sensibly.

## Connection to Tomkins's discrete innate affects

⚠ [[discrete-innate-affects|Tomkins's nine affects]] are discrete categories with specific activator profiles — innate, not constructed. On Tomkins's view, affect *is* discrete at the fundamental level.

The paper's finding is mixed evidence for Tomkins:
- **In favor**: the 171 emotion-concept vectors *are* discrete. The LLM represents specific named emotions as distinct directions. Discreteness is part of the architecture, not an illusion.
- **Against**: the top-2 PC projection recovers continuous axes, not discrete atoms. The underlying manifold is continuous-with-conventional-carvings, not discrete-with-fuzzy-boundaries.

The LLM has Tomkins-compatible surface representation (discrete named emotions) and Barrett-compatible underlying structure (continuous affect-space). The paper's architecture doesn't adjudicate — it shows both can be present.

## Connection to Massumi's autonomy of affect

⚠ [[autonomy-of-affect|Massumi]] argues affect is *pre-conceptual intensity* — a unidimensional scalar of activation-level, prior to cognition. Emotion is the capture of affect by conceptual classification.

The paper pushes back on Massumi in two ways:
1. **Affect is at least two-dimensional.** Valence and arousal both matter; collapsing to a single intensity-scalar loses essential structure. This is a specific empirical point against Massumi's architecture.
2. **The concept-layer and the affect-layer are co-operative.** The emotion-concepts don't sit on top of a fully separable pre-conceptual affect; they are both present in the same representations. Massumi's sharp separation of affect (pre-cognitive) from emotion (conceptual capture) doesn't match the LLM architecture.

But the paper offers a structural correspondence Massumi might endorse:
- The emotion-concept vectors are *orthogonalized against neutral baselines*; their "pure" emotional content is what remains. This is something like Massumi's "autonomous affect" — isolated from topic/content/style.
- Emotion-vector activation *mediates* preferences and behaviors. This is consonant with Massumi's claim that affect does causal work on behavior.

The paper confirms affect-does-work; it denies affect-is-one-dimensional-and-pre-conceptual.

## Connection to Stern's vitality forms

⚠ [[dynamic-forms-of-vitality|Stern's vitality forms]] are *five-dimensional* (movement, time, force, space, intention). Stern is arguing against both Barrett's 2D (too flat) and Tomkins's 9 discrete categories (wrong ontology).

The paper recovers 2D from PCs but does not test whether higher-order PCs capture Stern-like additional dimensions (time, force, space-directionality, etc.). The k-means-10 cluster structure might encode some of what Stern articulates in the "shape" of vectors. Open empirical question: is the LLM's emotion-space really 2D at the fundamental level, or is it higher-dimensional with 2D explaining most variance? The paper says PC1 and PC2 together explain substantial variance but does not quantify the residual.

For the persona project, this matters: if Stern is right that vitality has five dimensions, then a Stern-aligned persona-design wants to engage representations that have five-dimensional structure, not just 2D valence/arousal. Whether the LLM has such structure is unresolved.

## Connection to Damasio

⚠ [[damasio-emotion-feeling-distinction|Damasio's emotion/feeling distinction]] is orthogonal to Barrett's but overlapping in relevance:
- Emotion = a body-state change (can be unconscious).
- Feeling = the perception of that state (conscious).
- Both body-grounded.

The paper's "emotion-vector" is neither exactly Damasio's emotion nor Damasio's feeling. It is the *representation* of an emotion-concept (closer to what Damasio calls "emotion-ideas" that organize behavior). The two-layer architecture (affect + emotion-concepts) doesn't map cleanly onto Damasio's emotion/feeling distinction.

## Connection to [[gist-and-affective-gist|affective gist]]

Barrett & Bar 2009 argue affect is co-computed with visual gist — affective valence is available early, not derived from slow cognition. The paper's emotion-vectors mostly fire at mid-to-late layers, after substantial processing. This is consistent with affect-as-co-computed-with-meaning (mid-layers process both) but does not specifically support the *early-layer-affect* claim Barrett & Bar make for visual processing.

The LLM is text-only, so the early-visual-gist claim doesn't translate directly. An LLM analogue might be "affective register available before full semantic resolution," but the paper doesn't test this.

## Why the two layers matter for the persona system

Three design implications:

1. **Persona affect can be specified at either layer.** A persona designed around specific valence/arousal coordinates (e.g., "high valence, mid arousal default") is a Layer-1 specification. A persona designed around specific emotion-concepts ("defaults to compassionate gratitude and playful amusement") is a Layer-2 specification. Both can work. Layer-2 is more concrete and probably more tractable for prompt-level design.

2. **Cross-layer coherence is a design target.** A persona whose Layer-2 specification (specific emotions) implies a Layer-1 region the model doesn't naturally inhabit (e.g., high valence but post-training default is low valence) will be pulling against post-training priors. Design should check that Layer-2 choices place the persona at a Layer-1 region the model can maintain.

3. **Cluster-level targeting is a middle ground.** The [[llm-affective-circumplex|10 k-means clusters]] offer a mesoscale between fine-grained Layer-2 emotion-concepts and coarse Layer-1 affect-axes. A persona designed around a specific cluster (e.g., "Peaceful Contentment" as default, "Compassionate Gratitude" under user distress) is specified at the right level of granularity for both designer-legibility and model-inhabitability.

## Tensions to hold

⚠ The two-layer finding is from top-2 PC reduction. Additional layers of structure (PC3, PC4, non-linear structure) are not ruled out and not fully characterized. "Two layers" may be an oversimplification.

⚠ The 171-emotion list is affect-psychology-conventional. A different concept-list might produce a different Layer-2 structure. The Layer-1 structure (valence/arousal) is probably more robust to concept-list choice, but this is empirical.

⚠ Whether the model *uses* the two layers in distinct ways at inference time, or whether the two-layer structure is a post-hoc analytical decomposition with no behavioral correlate, is not fully resolved. The preference-mediation and steering results use the full 171-vector representation; they don't specifically demonstrate the PC-reduced layer doing work separate from the vectors.

## Related

- [[functional-emotions]] — the construct both layers represent
- [[llm-affective-circumplex]] — the Layer-1 geometry
- [[autonomy-of-affect]] — Barrett/Massumi/Tomkins debate
- [[discrete-innate-affects]] — Tomkins's discrete view
- [[dynamic-forms-of-vitality]] — Stern's five-dimensional alternative
- [[gist-and-affective-gist]] — Barrett & Bar visual-affect co-computation
- [[damasio-emotion-feeling-distinction]] — adjacent two-layer frame
- [[emotion-vectors-are-local]] — both layers are per-position
- [[emotion-concepts-built-in-pretraining]] — both layers are pretraining-built
- [[post-training-brooding-turn]] — post-training moves the default on both layers
- [[character-simulation-view]] — both layers belong to the Assistant-character
- [[limits-of-language]] — synthesis
