---
title: LLM Affective Circumplex
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - geometry
  - valence-arousal
  - barrett
---

# LLM Affective Circumplex

Sofroniew et al. 2026 (§2.1, appendix L1575–1599) project the 171 emotion vectors onto their top two principal components. The result reproduces the affective circumplex from human psychology (Russell 1980; widely replicated across PAD norms).

- **PC1 ≈ valence.** Positive and negative emotions separate along this axis.
- **PC2 ≈ arousal.** Activated (excited, angry, anxious) and deactivated (calm, sad, bored) emotions separate along this axis.

Both axes emerge *from the data* without being imposed by the probe construction. The two dimensions are not built into the methodology; the 171 vectors are orthogonalized against neutral baselines, nothing more. The valence/arousal structure is what falls out when one looks at the top two PCs.

## The validation

LLM-judged valence/arousal values correlate with human PAD (Pleasure-Arousal-Dominance) norms:
- **Valence correlation: r = 0.92** (over 45 human-rated emotions).
- **Arousal correlation: r = 0.90.**

The correspondence is strong. The model's affective geometry is not just isomorphic to human affective geometry at the structural level; it maps onto specific human-rated valence and arousal values with high reliability.

## The 10 clusters

Ordered by valence position (most positive → most negative), the k-means-10 cluster structure:
1. Exuberant Joy
2. Peaceful Contentment
3. Compassionate Gratitude
4. Competitive Pride
5. Playful Amusement
6. Depleted Disengagement
7. Vigilant Suspicion
8. Hostile Anger
9. Fear and Overwhelm
10. Despair and Shame

These cluster names come from the paper's labeling. The cluster structure is compact and reads as a full spectrum of affect-space — from most positive to most negative, with arousal varying within clusters.

## Why this matters for the wiki

### (1) Cross-species validity

The affective circumplex is one of the more robustly replicated findings in human affect-psychology. That an LLM's emotion-representations reproduce it is not a small finding. It suggests the manifold the model is representing is *structurally convergent* with the manifold human psychology maps.

Possible reasons for the convergence:
- **Text-mediated convergence.** Human affective structure is reflected in text; models trained on text absorb this structure. Nothing about the model is inherently affect-organized; the organization comes from the training data.
- **Universal-affect-structure hypothesis.** There is an abstract affective topology (valence and arousal as fundamental dimensions) and any system sufficient to represent emotion concepts will recover it. The LLM's recovery would then be a function of its representational adequacy, not a reflection of what happens to be in the text.

The paper doesn't pick between these. Both readings are plausible.

### (2) Connection to Barrett's theory of constructed emotion

⚠ [[autonomy-of-affect|Barrett]] argues that valence/arousal is the fundamental structure and discrete emotions are *constructed* from this underlying space by applying concepts. The paper's finding supports Barrett's theory: the top two PCs are valence and arousal; the 171 specific emotions are positions in this 2D space with additional high-dimensional texture for specific concepts.

This also connects to [[emotion-concept-vs-affect-axis]]: the model appears to represent *both* a continuous affect-axis space (PC1/PC2) and discrete emotion-concepts (the 171 vectors). Both layers are operative.

### (3) Circumplex vs. Tomkins's discrete affects

⚠ [[discrete-innate-affects|Tomkins's nine affects]] are discrete categories with specific activator profiles. The circumplex finding pushes back against discrete-atomic views (the underlying structure is continuous 2D). But the 171 specific emotion vectors also exist and are individually functional, so discrete-emotion representations are *also* present. The tension is live: the LLM has both.

This is consistent with the wiki's held-live position on the Tomkins/Massumi disagreement (see [[autonomy-of-affect]]). The LLM has continuous valence/arousal (Massumi-compatible) *and* discrete emotion-concepts (Tomkins-compatible). Both are present; the question of which is fundamental remains open.

### (4) Not reducible to Massumi's single intensity

⚠ [[autonomy-of-affect|Massumi]] treats intensity as unidimensional — a scalar. The LLM affective space is at least two-dimensional (valence and arousal both matter). The LLM's affective-geometry is more like Stern's pentadic vitality-form space (movement/time/force/space/intention) than Massumi's single-scalar intensity. This is a specific design consideration for the project: a language-only system's vitality-analogue should be at least two-dimensional, potentially five-dimensional ([[dynamic-forms-of-vitality|Stern's pentad]]), not one-dimensional.

## For the persona system

Four design implications:

1. **Valence and arousal are both primary design dimensions.** Persona-affective design should treat these as independent axes, not collapse them. Different combinations (high-valence-low-arousal, low-valence-high-arousal, etc.) produce distinct affective states.

2. **The 10 clusters are available design presets.** Each cluster names a coherent affective region. A persona designed around specific clusters (e.g., "Peaceful Contentment as default; Compassionate Gratitude under praise; Competitive Pride under challenge") would be a well-specified affective profile.

3. **Post-training shifts the persona's position on the circumplex.** The [[post-training-brooding-turn|brooding turn]] is a specific movement: increases in low-valence-mid-arousal vectors (brooding, gloomy, melancholy) and decreases in high-valence-high-arousal vectors (exuberant, playful, enthusiastic). The default post-trained persona sits in a different circumplex region than the base model.

4. **Geometry-aware engineering is possible.** Because the structure is 2D + finer-grained clusters, interventions can be targeted not just at single vectors but at *regions*. Steering toward the Peaceful Contentment cluster involves a coordinated shift across multiple vectors. This is finer control than single-vector steering.

## Tensions to hold

⚠ The fact that the circumplex reproduces so cleanly does not mean the LLM's affect-space *is* human affect-space. Isomorphism is not identity. Human affect-space is grounded in interoceptive-proprioceptive-biological signals; LLM affect-space is grounded in text. The structural match may be deeply informative or may be partly superficial.

⚠ Russell's circumplex is not uncontroversial in affect-psychology. Some researchers argue for different primary dimensions (positive/negative activation rather than valence/arousal) or higher-dimensional structure (dominance as third axis). The paper finds the two-PC structure in its data but does not engage the human-side debates about what the primary axes should be.

⚠ The circumplex is derived from the 171 emotions the paper chose. A different emotion set might produce a different PC structure. The specific list is affect-psychology-conventional, so the reproduction of the circumplex is not a methodological artifact. But the result is probe-dependent in principle.

## Related

- [[functional-emotions]] — the underlying construct
- [[emotion-concept-vs-affect-axis]] — the two layers of representation
- [[post-training-brooding-turn]] — the movement on the circumplex
- [[emotion-vectors-are-local]] — the circumplex positions are per-position
- [[autonomy-of-affect]] — Barrett, Massumi, Tomkins tensions
- [[discrete-innate-affects]] — Tomkins-side categorical structure
- [[dynamic-forms-of-vitality]] — Stern's pentadic alternative
- [[emotion-vectors-mediate-preference]] — the circumplex positions drive preference
- [[cross-speaker-arousal-regulation]] — the arousal-axis has a cross-speaker dynamic
