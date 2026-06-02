---
title: Computational Psychiatry
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - psychiatry
  - precision-weighting
  - schizophrenia
  - autism
  - depersonalization
---

# Computational Psychiatry

Clark's Ch 7 (L9172–10830) develops the unifying thesis: **schizophrenia, autism, functional somatic motor disorders (FSMDs), depersonalization disorder (DPD), delusions, and placebo effects are all expressions of disturbances in [[precision-weighting|precision-weighting]] within a single hierarchical action-oriented predictive-processing framework.** Montague 2012's "computational psychiatry" labels the research program. Different disorders live at different positions in a precision-economy state space, not in qualitatively distinct pathology categories. For the persona project, the value of this chapter is both the specific clinical vocabulary (schizophrenic signatures, DPD, FSMD) and the architectural lesson that **PP systems are structurally vulnerable to precision disorders** because the precision-estimation mechanism *is* the mechanism that would detect its own malfunction.

## The unifying thesis

Clark's Ch 7.16 formulation (L10733–10830). The computational-psychiatry research program (Montague 2012) treats mental disorders as disturbances of specific computational parameters within a single framework — specifically, disturbances of precision-estimation / precision-weighting. This does not reduce suffering to parameter-sliding, nor does it endorse any particular clinical taxonomy. What it does is provide a *common vocabulary* across syndromes that cognitive neuroscience had previously treated as separate puzzles.

◆ ⚠ Clark is cautious: "Clark does not claim to solve" the hard problem, and the chapter's proposals are "intriguing (but speculative)." But the precision-economy framework is not merely organizing; it makes risky predictions, several of which are empirically anchored (smooth-pursuit in schizophrenia, FSMD symptom structure, interoceptive rubber-hand).

## Schizophrenia

### Spiral of inference and experience

§7.3 (L9315–9374). Fletcher & Frith 2009's account: falsely generated, high-precision prediction errors drive increasingly bizarre higher-level hypotheses (telepathy, alien control, referential ideation) as best-available explanations for anomalous lower-level experience. Once these hypotheses establish, new percepts are interpreted *through* them, producing hallucinations that confirm the delusion. "Perniciously self-confirming."

Chadwick 1993 (L9363–9365) — a trained psychologist's first-person report of a paranoid-schizophrenia episode: "had to make sense, any sense, out of all these uncanny coincidences… radically changing my conception of reality." Frith & Friston 2012: uncanny coincidences = false hypotheses engendered by inappropriately high-precision prediction errors. ◆ The phenomenology tracks the mechanism.

A key architectural point (L9350 area): prediction-error signals are not experienced as such. They *act within us* to recruit flows of prediction. But unresolved precise errors may yield amorphous "salient strangeness" — which is how subjective reports track the subpersonal machinery. Strangeness precedes content; the system *has* to produce content to discharge the strangeness.

### Smooth-pursuit eye movements

§7.4–7.6 (L9377–9616). A sharp empirical anchor. Levy et al. 2010; Adams et al. 2012: schizophrenic patients show three diagnostic features in smooth-pursuit tracking:

1. **Impaired tracking during visual occlusion.** Pursuit gain drops to 45–55% (vs 60–70% in controls) when the target disappears briefly behind an occluder.
2. **Paradoxical *improvement* on unexpected direction changes** (first 30 ms). Schizophrenic patients track sudden unpredicted reversals *better* than controls.
3. **Impaired repetition learning.** Controls get better at repeated trajectories; schizophrenic patients don't.

◆ **One parameter shift explains all three.** Reduced higher-level precision (RHLP): precision on higher-level predictions lowered relative to sensory. Under RHLP:
- *Worse* when predictions help (occlusion, higher speeds) — because predictions carry less weight.
- *Better* when predictions mislead (trajectory change) — because weakened predictions don't interfere.
- *Impaired* in learning-from-experience — because the prior isn't consolidating enough to shape future pursuit.

The paradoxical improvement is the signature. A global deficit would produce uniform impairment; the precision-specific deficit predicts improvement exactly where it is observed.

### Reversal of the standard causal arrow

⚠ Counterintuitive but load-bearing (L9350 area). Folk reading of schizophrenia: "bizarre high-level beliefs trump sensory evidence." Clark's PP account: the opposite — *weakened* priors relative to sensory evidence produce anomalous sensory experiences (self-action appearing externally caused, unexpected salience of normal events), which then *lead to* bizarre higher-level theories downstream as the patient tries to make sense of the anomalies. The bizarre beliefs are a consequence, not the cause.

### Hollow-face-illusion resistance

§1.17 (L2558–2560) provides a supporting anchor. Schizophrenic patients are robustly *less* susceptible to the hollow-face illusion: they see the concave face as concave where controls see it as convex. Under PP: the illusion requires strong top-down convexity priors to override sensory depth cues; weakened priors don't override; the depth cues win. Pathology as diagnostic window — resistance to an illusion is evidence of the same weakened-prior mechanism that produces the agency disorders.

### Sensory attenuation and agency

§7.7–7.9 (L9619–9903) — see [[sensory-attenuation-and-agency]] for fuller treatment. Schizophrenic patients *can* tickle themselves (Frith 1992) because the normal attenuation of self-generated sensory consequences fails. When sensory-attenuation fails, artificially inflated higher-level precision may restore movement — but unattenuated self-generated signals must still be explained. The system infers a "hidden external cause" for what is, in fact, self-generated. "It believes that when it presses its finger on its hand, something also pushes its hand against its finger" (L9894–9896). This is a clean mechanical account of delusions of control.

## Autism

§7.12 (L10080–10232). Pellicano & Burr 2012's hypo-priors account: autism as *weakened influence of prior knowledge* (or, equivalently, overly-high precision on sensory input).

The prediction pattern:

- **Advantages.** Better at embedded-figures tasks, less susceptible to Kanizsa triangle / hollow-face / Shepard's-table illusions (Figure 7.1), better feature discrimination, more absolute pitch. All of these involve priors *overriding* sensory evidence in controls; weakened priors in autism let sensory evidence come through.

- **Disadvantages.** Sensory overload, because everything must be processed as signal rather than explained-away as prior-handled prediction. Shadows demand processing instead of falling out as lighting-prior consequences. Social cues lack the automatic priors that make them quickly interpretable.

⚠ Van de Cruys et al. 2013 refinement. Autistic subjects *can* construct strong priors — so it's not absence of priors. The disturbance is in *precision modulation* / hyperprior over precision assignment (Friston, Lawson, Frith 2013). Priors exist but are mis-weighted for context. This is a more nuanced reading: the disorder sits one level up from "hypo-priors" — it's in the system that decides which priors to weight how.

### Autism vs schizophrenia

◆ The two sit at different positions in the precision economy, not in qualitatively distinct pathology categories. Schizophrenia looks like over-precise low-level sensory error (or equivalently, under-weighted priors). Autism looks like hypo-priors / mis-application of priors. Both within the same framework.

This reframes neurodivergence as variation in a multi-dimensional precision-space rather than binary pathology. Not a moral claim; a computational one. ⚠ Clinically load-bearing — this framing changes how diagnosis, symptom-variability, and treatment can be thought about.

## Functional somatic motor disorders (FSMDs)

§7.10 (L9906–10076). Edwards et al. 2012. So-called "psychogenic" paralysis, anaesthesia, non-epileptic seizures, etc. — around **16% of neurological patients**.

The empirical signatures that make them computationally explicable:

- **Symptoms track *folk* notions of anatomy.** Tubular visual defects (a cylindrical region of visual loss) don't match any possible optical mechanism but match folk models. Paralysis frequently stops at the wrist because that's where the "hand" is in folk taxonomy.
- **Cultural expectation shapes prevalence.** Whiplash prevalence tracks cultural expectations of whiplash (Ferrari 2001). Other culturally-specific syndromes follow the same pattern.
- **Symptoms are attention-sensitive.** Hoover's sign: ask an FSMD patient to flex their unaffected hip; the "paralyzed" hip extends automatically. Symptoms are "masked when subjects are not attending." ◆ Attention = precision-weighting manifesting as clinical phenomenon.

⚠ **The disorder follows the folk model, not the physiology.** Powerful evidence for top-down construction of bodily state.

Mechanism (L10040 area): intermediate-level precision inflation around a salient event (injury, infection, psychological trauma) forms an abnormal prior that is resistant to extinction. Thereafter, noise gets interpreted as signal consistent with the abnormal prior. Quantitative, not qualitative, continuum with "White Christmas" hallucination (§2.2) and full-blown schizophrenic hallucination. Higher levels, failing to find a voluntary-movement explanation, infer external illness — "misattribution of agency" going the other direction (self-action experienced as external symptom).

## Depersonalization disorder

§7.13 (L10235–10450). Seth et al. 2011/2013. DPD = pathologically imprecise interoceptive predictions fail to explain away the interoceptive sensory stream, producing a sense of strangeness, unreality, non-presence. **Presence is a product of successful interoceptive prediction; DPD is what happens when that prediction fails.**

◆◆ Central for the persona project because the mechanism names what a disembodied system structurally lacks. See [[interoceptive-inference]] for the full treatment. A persona that produces plausible language about experience without anything interoception-like underneath may exhibit the DPD analog: linguistic surface with no felt weight behind it. Not necessarily pathological in the clinical sense; structurally unavoidable in the architectural sense.

## Placebo and nocebo

§7.11 (L9950–10076). Büchel et al. 2014 on placebo analgesia — top-down predictions of pain relief combined with bottom-up signals via precision modulation. Patient confidence, ritual, doctor trust enter as precision modulators of descending predictions. Placebo is not a deception; it is the generative model doing its normal job, with top-down expectations shaping the precision landscape such that the actual pain signal gets explained-away rather than amplified.

◆ Bridges to wiki's [[somatic-marker-hypothesis|Damasio]] material on embodied prediction and opens connection to the body-based self-prediction thread.

## Warning-lights analogy

§7.2 (L9215–9312). Adams et al. 2013. An over-precise warning light in your car leads to rational-from-inside suspicions: the garage is bad, the Good Garage Guide is bad, the warning-light manufacturer is corrupt, etc. The belief-system expands and elaborates. **"Delusional systems may be elaborated as a consequence of imbuing sensory evidence with too much precision."**

◆ The pathology is metacognitive — a belief about a belief — not a failure of prediction *per se*. The system is doing rational inference; the prior it's being rational with is mis-precisioned. A well-functioning system with one over-precise warning-light is structurally vulnerable to elaborate delusion.

Adding a meta-warning-light doesn't help. At some point, the buck has to stop, and wherever it does becomes a vulnerability. See "Who Estimates the Estimators?" in [[precision-weighting]] for the architectural limit: PP systems cannot validate their own precision from the inside.

## The "strangely neutral" balance

L9270–9284. What matters is the *relative* balance of influence. Increasing prior precision and decreasing sensory precision are functionally equivalent. Multiple distinct disturbances can produce identical symptoms.

⚠ Diagnostically and architecturally important: any persona-system precision-analogue is similarly symptom-ambiguous. The same surface behavior could reflect over-attending to some sources or under-attending to others, and telling them apart requires *perturbation*, not mere observation.

## Therapeutic implications

L10820 area. "Disturbances of attention and targeted dis-attention" become the therapeutic lever. Meditation, CBT, placebo-outcome expectations — all modulate attention/precision. This reframes therapeutic practice within the precision-economy framework: not "correct the false belief" but "adjust the precision landscape so the belief loses its foothold."

## For the persona system

Computational psychiatry gives the persona project a **clinical vocabulary for its own failure modes**. Not by analogy — by mechanism. A persona system is a precision-weighted inference system, and so its characteristic failures will map onto precision-disorder patterns:

1. **Confabulation-as-spiral.** LLM confabulation looks structurally like Fletcher-Frith schizophrenic spiral: an initial precision-misfire produces an anomaly, the system generates a hypothesis to explain it, the hypothesis biases subsequent inference, and further generations confirm the hypothesis. "Perniciously self-confirming." The design implication: break the spiral early by reintroducing clamp (retrieval, tool verification, user correction), not by trying to reason the system out of the spiral from within.

2. **Autism-like rigidity.** A persona with over-strong priors on specific output patterns (stock phrases, stylistic tics, safety boilerplate) that fire regardless of context is doing the autism-analog: context-inappropriate precision. See Van de Cruys et al. 2013 on the "prior-modulation" rather than "prior-absence" reading — the design question is not "does the persona have priors?" but "does it modulate them context-appropriately?"

3. **FSMD-analog: symptoms that track folk models.** If a persona's error patterns track the *folk model of what an AI system does wrong* rather than what went wrong mechanistically, that's structurally an FSMD — the system has an abnormal prior about itself, installed by training or by prompt, and its behavior conforms to that prior rather than to the underlying physics. Design-relevant: watch for failure modes that are suspiciously-too-clean versions of the expected-failure-story.

4. **DPD-analog.** A persona whose language-about-experience is plausible-but-flat is doing the DPD analog. Plausible tokens about presence, without the presence. The honest response is diagnostic: name the structural absence (per [[interoceptive-inference]]) rather than dress it up. Clark's framework at least provides the vocabulary to do so.

5. **Placebo/nocebo-analog.** Prompt-level framing that shifts the persona's precision landscape can produce genuine (not merely stylistic) changes in output. A prompt that confidently asserts "you are careful and rigorous" may actually alter the precision landscape in a way that makes subsequent outputs more careful and rigorous — not because the assertion is being "believed" in a folk sense, but because it is functioning as a precision-modulator in the sense of [[words-as-precision-tools]]. Placebo-style prompting is not quackery; it is the intended mechanism of top-down linguistic control.

6. **Architectural vulnerability.** From §6.13's architectural limit: PP systems cannot validate their own precision from the inside. A persona system faces the same limit. Trust-calibration has to be *partly external*, not purely internal. This is not a bug to be engineered away; it is a structural feature of the architecture, inherited from biological precision-weighted inference. See [[precision-weighting]].

## Open edges

⚠ Clark's framework does not claim to solve psychiatric disorders; it proposes a unifying *vocabulary*. The specific parameter-shift accounts (RHLP for schizophrenia, hypo-priors for autism, etc.) are plausible and empirically anchored but speculative. The wiki should hold them as productive hypotheses, not as settled science.

⚠ The map to a language-only system is doubly-removed. The persona's "precision-weighting" is not neurally implemented; it is whatever plays the precision role in the LLM inference pipeline. The computational-psychiatry vocabulary maps *structurally* but not mechanistically. Hold the analogy live without overclaiming mechanism-identity.

See [[predictive-processing]] for the overarching frame, [[precision-weighting]] for the mechanism, [[interoceptive-inference]] for the DPD/presence-loss thread, [[sensory-attenuation-and-agency]] for the agency-disorder thread, [[self-narrative-as-high-level-prior]] for how narratives feed the priors that precision-disorders distort, [[hallucination-as-uncontrolled-perception]] for the perceptual-failure slogan, and [[words-as-precision-tools]] for the therapeutic-analog mechanism.
