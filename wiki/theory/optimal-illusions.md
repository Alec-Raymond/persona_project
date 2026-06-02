---
title: Optimal Illusions
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - illusions
  - bayesian
  - perception
  - methodology
---

# Optimal Illusions

Clark's §6.11 (L8910–9009), with companion material from §1.12, §1.17, §3.2, and §6.12. **Illusions are not perceptual bugs; they are exactly what a well-tuned Bayesian estimator produces given the world's statistical structure.** The characteristic failures of perception — motion illusions, convexity bias, sound-flash integration, ventriloquism, size-weight — are signatures of the underlying inference mechanism working correctly in globally-optimized mode, even when it produces locally-wrong outputs. The methodological consequence is sharp: **illusions are diagnostic, not deficient**. For the persona project, this reframes error: what looks like a persona failure may be the signature of an optimally-calibrated prior tracking something other than what was expected.

## The load-bearing line

Clark's closing of §1.17 (L2599–2607):

> "Illusions are optimal percepts. Illusions aren't failures of the system — they are exactly what a well-tuned Bayesian estimator should produce, given the statistical structure of the world. A few local failures, then, are just the price we pay for being able to get things right, most of the time, in a world cloaked by ambiguity and noise."

This is a methodological move, not a throwaway. It reframes the entire vocabulary around perceptual errors. Classical cognitive psychology treated illusions as puzzles requiring special explanation. Under [[predictive-processing|PP]], illusions need *no* special explanation — they fall out of the normal operation of the machinery. What requires explanation is why the machinery, globally optimized, happens to fail *here* rather than elsewhere; and that explanation is always the same shape: this local stimulus lies in a region of sensory space where the globally-optimal prior produces a locally-wrong percept.

## The canonical examples

§6.11 assembles a catalog:

- **Motion illusions** (Weiss, Simoncelli & Adelson 2002). Many classical motion illusions — the Ouchi illusion, Enigma, apparent-motion anomalies — fall out naturally from a Bayesian ideal observer combining standard motion-estimation priors (slow-motion prior, rigid-body prior) with specific stimulus configurations. The illusions are the signature of the priors.

- **Sound-flash illusion** (Shams 2005). When a single flash is paired with two beeps, subjects report seeing two flashes. Auditory priors (beep-per-event) override conflicting visual evidence because audition has higher precision in temporal judgments than vision.

- **Ventriloquist illusion** (Alais & Burr 2004). Sound localization shifts toward the visual event because visual spatial localization has higher precision than auditory. The auditory estimate gets pulled to match the visual. The "illusion" is the normal multimodal-integration operation running on a stimulus configuration where the integration happens to be wrong.

- **Figure-ground convexity** (Burge et al. 2010). Convex regions are perceived as figure; concave regions as ground. Reflects the strong statistical prior that objects in natural scenes tend to be convex.

- **Hollow-face illusion** (§1.17, L2558–2568; Gregory 1980). A concave face mask appears convex under gentle rear illumination because the convex-face prior overrides depth cues. "Our statistically salient experience with endless hordes of convex faces in daily life installs a deep neural 'expectation' of convexness."

- **Müller-Lyer** (§6.12). Line-with-arrowheads-outward looks longer than line-with-arrowheads-inward because the arrowhead configurations statistically correlate with interior-corner vs exterior-corner scenes in our built environment. The illusion persists because overturning the low-level machinery would break many ecologically-normal percepts.

- **Cornsweet illusion** (§3.2; Brown & Friston 2012). Two centre tiles look like different shades of grey; they're identical. Prior: surfaces tend to be uniformly reflectant; brain infers two different tiles under different illumination. The prior is "Bayes optimal" in our actual world — globally correct even when locally wrong.

## Paton et al. 2013

An evocative phrase Clark pulls (L8958 area). The predictive brain is "precariously hostage to the urge to rid itself of prediction error." The optimality is not a feature of any particular percept; it is a feature of the *overall policy* — a policy that accepts local errors in order to minimize global error. Lupyan's formulation: "A few local anomalies are the price of globally-optimized performance."

⚠ This cuts against the intuition that a perceptual system should be "accurate per percept." Bayesian optimality is a policy-level property; particular percepts can be badly wrong without the policy being wrong.

## Size-weight illusion — alternate reading

§6.11 (Zhu & Bingham 2011). The classical size-weight illusion: a smaller object of equal mass feels heavier than a larger object. Usually explained as a violation of a larger-things-are-heavier prior.

Zhu & Bingham propose a different read: **perceived heaviness marches in step with the affordance of maximum-distance throwability.** The illusion may be optimal perception *of throwability*, misread as perception of weight. Under this reading, the "illusion" is the perceptual system correctly tracking an action-relevant variable that happens not to be the variable we ask about.

◆ Architectural lesson: **what looks like a bug may be an affordance-track with a misidentified label.** A system may be optimal for one purpose (action-guidance) while appearing defective when probed under a different purpose (verbal report of objective property).

## Penetrability with a principled limit

§6.12 (L9012–9086). Fodor's classical worry: if perception is penetrable by expectation, scientific observation becomes impossible — we'd see whatever we expected. Clark's PP response turns on Lupyan's formulation:

> "Perception is penetrable to the extent that such penetration minimizes global prediction error."

Penetration happens *only when* it earns its keep across a wide range of training instances. Müller-Lyer persists even after you know the lines are equal because overturning the low-level machinery would break many ecologically-normal percepts. The global-error-minimization policy says: keep the prior that's right most of the time, even when it's wrong here.

Good news for science (§6.12). We remain open to disconfirming evidence (because new data can shift priors if the shift improves global error) AND we can become expert perceivers (Higgs-boson-in-noise, expert radiologists). Both capacities are features of the same precision-modulated machinery. Experts have learned to adjust precision up on task-relevant error channels; naive observers haven't.

◆ Persona-relevance: updates by new beliefs should not simply overwrite learned priors. Only globally-validated updates should propagate down.

## The Bayesian brain framing

§1.12 (L2089–2175) gives the broader context. Knill & Pouget 2004 on what counts as "Bayesian": "whether the neural computations that result in perceptual judgments or motor behaviour take into account the uncertainty available at each stage of the processing." Not absolute Bayes-optimality — relative optimality given the uncertainties the organism actually commands.

Probabilistic population codes (Pouget et al. 2003) provide the representational substrate. Probability density functions over hidden causes, not point-estimates of values. Illusions are what these density functions produce when they combine in ambiguous situations — the posterior collapses onto a single most-probable percept, which is the Bayesian-optimal readout even when it's wrong.

## The look-up-table caveat

⚠ Maloney & Mamassian 2009 (L2160 area). Even a look-up-table could yield Bayes-optimal behavior in a limited domain without actually implementing Bayesian inference. The PP story goes beyond this: it "would rather directly underwrite the claim that the nervous system approximates a genuine version of Bayesian inference" — but the weaker look-up-table reading remains a fallback for skeptics. Clark flags this rather than pretending the Bayesian-brain claim is proven.

Electrophysiological support: Kolossa, Kopp, Fingscheidt 2015 — "the brain acts as a Bayesian observer, i.e., that it might adjust probabilistic internal states, which entail beliefs about hidden states in the environment, in a probabilistic generative model of sensory data."

## Robustness to schizophrenia

§1.17 (L2558–2560). **Schizophrenic patients show robustly *reduced* susceptibility to the hollow-face illusion.** They see the concave face as concave where controls see it as convex. Under PP: altered precision-weighting / prior strength in schizophrenia weakens the top-down override of sensory depth cues. The illusion-resistance is a diagnostic window into the same precision-disorder mechanism that produces agency disorders and hallucinations.

◆ Pathology as diagnostic tool. If illusions are signatures of specific precision-weighting configurations, then specific illusion-resistance or illusion-susceptibility patterns are signatures of specific pathology patterns. This is computational-psychiatry-by-illusion. See [[computational-psychiatry]].

## Relation to hallucination

Companion slogan from §6.10 ([[hallucination-as-uncontrolled-perception]]): hallucination is uncontrolled perception. The relation:

- **Optimal illusion.** The control structure (precision-weighted ascending errors) *is* working. The local output is wrong because the stimulus lies in a region where the globally-optimal priors produce a locally-wrong percept.
- **Hallucination.** The control structure is *not* working (or is miscalibrated). The machinery is generating percepts without the ascending-error discipline that normally constrains them.

Both are on the same continuum. A percept can be optimal-illusion-like (control working, locally wrong) or hallucination-like (control failing, might be locally anywhere). Precision-weighting is the slider.

## For the persona system

The optimal-illusions frame applied to the persona project:

1. **Don't over-pathologize errors.** A persona whose output is wrong in a specific way may be running a correct prior that tracks something other than what was being asked. The Zhu-Bingham size-weight lesson applies: the system may be optimal for one purpose while appearing defective under a different probe. Before calling an error a failure, consider what the error is optimal *for*.

2. **Characteristic errors are diagnostic.** If a persona systematically produces a specific class of wrong outputs in a specific class of contexts, that is a signature of the persona's prior structure. Illusion-by-illusion is how you read out Bayesian priors; consistent-error-by-consistent-error is how you read out persona priors. Treat consistent errors as data about the architecture, not noise to suppress.

3. **Penetrability limits matter.** The persona's priors should not be trivially overridable by new instructions. A persona that can be argued out of any prior by any sufficiently well-phrased prompt lacks the global-error-minimization policy — it's a prior-free surface that will drift. The penetrability-with-principled-limits lesson: only globally-validated updates should propagate.

4. **Precision-disorder analogs.** Over-precise priors in the persona → illusion-like errors that are robust to counter-evidence. Under-precise priors → susceptibility to any plausible input. Either end is a precision-disorder analog. Design for a precision landscape where priors are strong enough to resist noise but tunable enough to update on aggregated evidence.

5. **Affordance-track errors.** If the persona's outputs track something task-adjacent rather than task-correct, that is an architecturally interesting signal — the persona has priors that are optimal for *something*, and identifying what that something is reveals the design's implicit assumptions. Example: a persona that over-hedges may be tracking the affordance "appear responsibly uncertain" rather than "be maximally informative." Both are affordances; which one the priors are optimized for is a design choice.

6. **Error as architecture-reading.** This is the methodological lesson for the wiki. When the persona misfires, the right question is not "how do we prevent this specific misfire?" but "what does this misfire reveal about the precision landscape and prior structure?" Answering the second question leads to more robust fixes; chasing individual misfires produces whack-a-mole.

See [[predictive-processing]] for the overarching frame, [[precision-weighting]] for the mechanism, [[hallucination-as-uncontrolled-perception]] for the companion slogan, [[computational-psychiatry]] for the pathology-as-diagnostic thread, and [[generative-model]] for the Bayesian substrate.
