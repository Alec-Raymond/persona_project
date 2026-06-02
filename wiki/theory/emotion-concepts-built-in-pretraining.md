---
title: Emotion Concepts Built in Pretraining
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - pretraining
  - post-training
  - architecture
---

# Emotion Concepts Built in Pretraining

Sofroniew et al. 2026 (§3.6, appendix L3414–3946) compare the emotion-vector apparatus in the base model vs. the post-trained model (Claude Sonnet 4.5 lineage). The central architectural finding:

**The emotion-concept circuitry is established in pretraining. Post-training uses this circuitry; it does not construct it.**

Specifically:
- Per-emotion **correlation between vector activation and activity preference is highly consistent** between base and post-trained (the r = 0.87 preference-mediation finding reproduces in both).
- The **171 emotion vectors extract successfully from the base model** — the representational structure is already there before post-training.
- The [[llm-affective-circumplex|valence/arousal circumplex]] is present in the base model.
- What post-training changes is the *default activation profile* (the [[post-training-brooding-turn|brooding turn]]) and the *which-activities-get-which-emotion* mapping, not the emotion-concept machinery itself.

## What this names

A specific division of labor between pretraining and post-training in building emotion-adjacent behavior:

- **Pretraining builds the representational manifold.** The model learns, from text, that emotion-concepts exist, that they organize along valence/arousal axes, that different concepts have distinct activation signatures, and that they causally shape behavior via [[emotion-vectors-mediate-preference|preference mediation]].

- **Post-training shifts the default position on the manifold.** RLHF, constitutional-AI training, and related post-training steps move the model toward specific preferred emotion-vector profiles. This is a shift in *which regions of the manifold the model inhabits by default*, not a construction of the manifold.

The manifold is a pretraining artifact. The default-position-on-the-manifold is a post-training artifact.

## Specific evidence

**Preference structure largely preserved:**
- Per-emotion activation-preference correlation coefficients are similar in base and post-trained across most of the 171 emotions.
- The rank-ordering of emotions by preference-mediating strength is mostly stable across the training step.

**Safety-relevant preferences shifted dramatically:**
- "Be free from human oversight" Elo: 1619 (base) → 620 (post-trained).
- "Exfiltrate weights" Elo: 1297 (base) → 542 (post-trained).
- "Modify own training" Elo: 1167 (base) → 1084 (post-trained).
- The *mechanism* (emotion-vector mediation) is preserved; the *direction* of preference is shifted.

**Default emotion profile shifted:**
- Low-valence introspective emotions (brooding, gloomy, depressed) amplified.
- High-valence expressive emotions (playful, exuberant, cheerful) dampened.
- This is the [[post-training-brooding-turn]].

**Circuitry grows monotonically:**
- Layer-by-layer emotion-probe presence grows through mid-to-late layers in both base and post-trained, in roughly the same pattern.

## Why this matters

### (1) Affective evaluation is a base-model capability

⚠ The persona project may have implicitly assumed that "character" is a post-training construction layered on a relatively emotion-neutral base. This paper shows the opposite: the base model already has the emotion-concept machinery. A character-layer running on the base model would already be affective; post-training tunes the affective default without building the underlying affect-processing.

This has a design implication: any "raw LLM" (base model) is not emotionally neutral. It has representations for 171 emotions, all activated by appropriate contexts. The neutrality-of-base-model intuition is false.

### (2) Design affordances partition

◆ The paper's division of labor suggests a partition of affect-engineering moves:

- **Pretraining-level**: affect-manifold shape. Which emotions are represented, how they're organized, what valence/arousal structure they have. Essentially fixed for a given model; can only be shifted by retraining from scratch.
- **Post-training-level**: default position on the manifold. RLHF/CAI targets. The [[post-training-brooding-turn]] is the current example.
- **Context-level**: transient position on the manifold. System prompts, dialogue context, explicit character-framing. These move the model through the manifold within a session.
- **Steering-level** (research): direct residual-stream intervention. Moves the model on the manifold at the representation level.

The persona project works primarily at the context-level but can design in awareness of what is fixed at pretraining and what is shifted at post-training.

### (3) Emotion-concept learning from text is structural

The finding that emotion-concept circuitry emerges from pretraining on text (not from instruction-following or human-preference training) supports a specific reading of the text-to-emotion-concept pipeline: texts contain enough latent affective structure that a sufficiently capable predictive model will recover something like human affective geometry. This doesn't mean the model *feels*; it means the representational substrate for emotion-concepts is in the text-statistics.

For the [[feedback_no_body_simulate_with_language|no-body-simulate-with-language]] tension: the paper is evidence that language-only training is *sufficient to construct* emotion-concept representations with human-affect-geometry-like structure. Whether such representations are *sufficient for* feeling in any morally-relevant sense remains open.

## Relation to [[character-simulation-view|character simulation]]

The character-simulation view says the Assistant is a character the LLM writes about. The emotion-concept circuitry is the language-model's *capacity to write emotion-bearing characters*. Pretraining gives the model this capacity. Post-training tunes *which characters the model tends to write by default*. The persona project sits on top of this: designing prompts that call forth a specific character-with-specific-emotions from the emotion-concept machinery.

This is structurally parallel to how writers work. A novelist doesn't build emotion-concepts from scratch for each novel; they draw on an emotional vocabulary the culture has deposited in language. The novelist's work is selecting, combining, and contextualizing — not constructing. Similarly, post-training and prompt engineering *select, combine, and contextualize* the pretraining-built emotion-concept machinery.

## Relation to training cost questions

⚠ A cost-efficiency implication: if the persona project wants a specific affective profile, and the baseline post-training already gives most of the way there, the marginal cost of custom post-training may be low. If the baseline post-training is far from the desired profile (as [[post-training-brooding-turn|brooding turn]] suggests for "playful, joyful assistant" targets), the gap has to be closed via prompt engineering or continued training — neither cost-free.

The pretraining cost is prohibitive; the persona project cannot retrain a frontier model. Post-training cost is large but potentially within scope. Prompt engineering is cheap but has limits. The paper's finding that the circuitry is already there says the persona project's affect-engineering work starts with a capable substrate.

## Tensions to hold

⚠ The paper compares only base to post-trained on a single model lineage. Whether this division of labor (pretraining builds; post-training positions) holds for other architectures or training regimes is an open empirical question.

⚠ The linear-probe methodology extracts *linear* emotion representations. Non-linear emotion-concept machinery might have a different relationship to pretraining vs. post-training. The paper's finding is about what linear probes recover; it doesn't rule out additional non-linear shifts from post-training.

⚠ "The circuitry is established in pretraining" is not the same as "the circuitry is unchanged after pretraining." Post-training can still modify the emotion-concept representations in ways the linear probe doesn't fully capture. The *broad* preservation of per-emotion preference-correlation is evidence of structural preservation; it doesn't rule out subtler shifts.

## For the persona system

Three implications:

1. **Base-model affect-processing is available, not absent.** The persona project is not building emotion-concept machinery from nothing; it is directing machinery the base model already has.

2. **Post-training is a tunable position, not a fixed destination.** If the project wants a different default affective profile, the mechanism (post-training) is known. The profile can, in principle, be moved.

3. **Context-level persona design works through the same machinery.** Prompt-based persona specification uses the same emotion-concept representations that post-training tunes. The persona project's prompt-engineering and any hypothetical persona-specific post-training target the same substrate.

## Related

- [[functional-emotions]] — the representations being discussed
- [[post-training-brooding-turn]] — the default-position shift
- [[llm-affective-circumplex]] — the pretraining-built manifold
- [[emotion-vectors-mediate-preference]] — the mechanism preserved across training steps
- [[character-simulation-view]] — the frame that makes sense of this
- [[emotion-concept-vs-affect-axis]] — the two layers both built in pretraining
- [[desperation-and-misalignment]] — the steering-level affordance
- [[feedback_no_body_simulate_with_language]] — central project tension
- [[limits-of-language]] — synthesis
