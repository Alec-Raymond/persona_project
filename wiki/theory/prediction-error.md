---
title: Prediction Error
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - predictive-processing
  - surprisal
  - information-theory
---

# Prediction Error

The quantity a [[predictive-processing|predictive brain]] minimizes — the residual component of a sensory signal that the organism's descending [[generative-model|generative model]] did not predict. In Andy Clark's *Surfing Uncertainty*, prediction error is the operational lever that makes the whole story go: learning, perception, attention, and action are all variations on "do something that reduces prediction error."

## Surprisal ≠ surprise

Prediction error is technically **surprisal** (Tribus 1961), not surprise in the folk sense: "Prediction error here reports the 'surprise' induced by a mismatch between the sensory signals encountered and those predicted. More formally—and to distinguish it from surprise in the normal, experientially loaded sense—this is known as surprisal (Tribus, 1961)" (L1473–1477). Surprisal is an information-theoretic measure — the implausibility of the data given the model — and is non-conscious. Subjective surprise is something else again: Clark (L3825–3881) argues that the magician-pulls-out-an-elephant feeling of surprise *diverges* from surprisal in informative ways. Once the elephant-hypothesis is recruited, surprisal drops sharply (the sensory data is now well-explained), yet the agent still feels surprised because the *systemic prior* (no-elephants-in-magic-shows) rendered that state of affairs highly improbable in advance. The felt surprise carries information about the model's own prior state, not about the current world-fit. Two-register architecture — surprisal does the work, surprise reports on the work.

## Signal-compression ancestry: Bell Labs 1950s

The predictive-coding strategy has a non-brain origin. James Flanagan and colleagues at Bell Labs in the 1950s developed it for bandwidth reduction (L1507–1509; Musmann 1979): encode only "the cases where the actual value departs from the predicted one" (L1497–1499). Motion-compensated video compression sends only the difference between predicted and actual frames; receivers reconstruct the rest. Nothing requires conscious prediction — regularity alone suffices. Clark's point: the same architectural idea (suppress the predictable, transmit only the unpredicted) has been independently derived by engineers and (on his PP account) by evolution.

## Only errors flow up

The deep architectural asymmetry of [[predictive-processing|PP]]: "the top-down and lateral flow of neural signals as constantly (not just during learning) aiming to predict the current sensory barrage, leaving only any unpredicted elements (in the form of residual 'prediction errors') to propagate information forward within the system" (L1464–1468). Richly contentful predictions flow *down* (and laterally); only errors flow *up*. Expected events need not be explicitly represented or communicated upward — Bubic et al. 2010, L7722–7725.

For this to work, the architecture needs two populations per cortical layer (Ch 1.11): **representation units** encoding the hypothesis (sending predictions down), and **error units** encoding unexplained residuals (sending errors up). Friston 2005 conjectures the anatomical implementation: superficial pyramidal cells = error units (forward-projecting); deep pyramidal cells = representation units (backward/lateral). "High-level predictions explain away prediction error and tell the error units to 'shut up'" (L2025–2029).

## Error units are representation neurons

A crucial subtlety Clark flags: "'Error neurons,' despite the label, are a variety of representation neurons—but ones whose functional role is to encode as yet unexplained… sensory information. What they encode is thus specified only relative to a prediction" (L2066–2070). Koster-Hale & Saxe 2013: in V1, error neurons encode orientation mismatches; in IT, they encode object-category mismatches. ⚠ The error/representation distinction is **functional, not ontological** — both populations represent, but the "error" population's content is always differential (what is sensed *minus* what is predicted). The wiki should not treat "error signal" as meaning something less representational than "representation."

## End-stopping flips interpretation

Rao & Ballard 1999's most methodologically startling result: the non-classical receptive field effect known as end-stopping (a neuron fires more for short edges than long ones) falls out naturally from PP as an **error-signaling effect**, not a feature-detection one. Long edges were the statistical norm in the training-set of natural scenes, so the descending model predicts long edges. Short edges therefore violate the prediction, and the firing reflects the mismatch rather than "successful feature detection" (L1793–1804). The same inversion is generalized in Egner, Monti & Summerfield 2010's FFA study: face-surprise (error) units contributed about twice as much to the BOLD signal as face-expectation (representation) units — "much of the activity normally recorded using fMRI may be signalling prediction error rather than detected features" (L2524–2525). ◆ Methodologically seismic: decades of feature-localizer neuroimaging may have been mis-labeling what regions do.

## Omission responses

One of the strangest empirical predictions PP makes, and one that was then confirmed: "One of the most remarkable properties of the auditory system is that it can generate evoked responses to an absent but expected stimulus" (Wacongne et al. 2012, L2329–2332). Missing notes in a melody evoke the same striking phenomenology as wrong notes — the missing-beat vividness Clark describes at L4286–4292: "we started to hear (or see, or feel) the very thing that, an instant later, we vividly notice has not occurred." Adams et al. 2013's hierarchical PP simulation of birdsong reproduces this: when a chirp is omitted, the system first "dimly perceives" (generates a transient illusory percept of) the missing chirp, then fires a strong error burst when absence registers (L4388–4390). The mental presence of the missing note IS the descending prediction; the noticed absence IS the upward error. Phenomenology matches architecture. The same machinery explains the P300 / mismatch negativity EEG signatures.

## Two ways to reduce prediction error

The symmetry that underwrites [[active-inference|active inference]]: a system minimizing prediction error has two routes available (L6101–6200). **Revise the prediction** (perception / belief update) — change the model until it fits the data. Or **act on the world** (action) — change the data until it fits the model. Same error quantity, two reduction strategies. The organism's policy-space is divided between these; [[precision-weighting]] allocates between them. ◆ For the persona system: when the system's output-hypothesis mismatches the observed reply-flow, it can either update its model of the user (perception) or alter its outputs to make future replies more prediction-confirming (action). Both are legitimate reductions — the architecture doesn't privilege model-update as the "right" response.

## Accuracy vs complexity — the Occam term

Fitzgerald, Dolan & Friston 2014 (L11382–11398): free-energy minimization (the information-theoretic quantity PP approximates) implicitly balances **accuracy** (prediction error) against **model complexity** (the Occam term). Simpler models carrying the same predictive load are preferred. Sleep does some of this work: during REM, "precise prediction errors are not generated, so the balance shifts towards the reduction of model complexity" (Hobson & Friston 2012; L4864–4871) — synaptic pruning improves generalization by shedding exuberant associations. Prediction error alone would produce a memorized, not a generalizing, system. ◆ Implication for a persona architecture: if prediction-error-analogues are the only learning signal, periodic simplification is structurally necessary, not optional.

## Precision-weighted error

Raw prediction error is never used directly in the mature PP account. The error gets **precision-weighted** before it propagates — multiplied by the system's own estimate of the signal's current reliability. Low-precision errors are discounted; high-precision errors are amplified. "Very low-precision prediction errors will have little or no influence upon ongoing processing" (L6786–6790). This is the move that rescues PP from the naive "every deviation changes everything" worry, and it is covered in depth on [[precision-weighting]]. Every load-bearing use of "prediction error" in the rest of the PP literature is really shorthand for "precision-weighted prediction error."

## Not a perceived signal

A methodological clarification Clark is insistent about (L3790–3796): "The claim is not, of course, that the agent perceives an error signal… According to PP, the agent perceives what is around her, but does so courtesy of the forward (and lateral) flow of error and the downward (and lateral) flow of prediction." The error signal *acts within* the system to sculpt descending predictions; it is not itself experientially accessed. When unresolved precise errors *do* show up in experience (Chadwick 1993's paranoid-schizophrenic "uncanny coincidences," L9363–9365), they take the form of amorphous salient strangeness — the system's report of errors it cannot explain away. See [[computational-psychiatry]] for the pathological case.

## For the persona system

A language-only system does not have sensory transducers in the PP sense. But the *structural* role of prediction error — a signal of where the descending model failed to anticipate the input, differentially propagated upward — has candidate analogues: the discrepancy between the system's prepared-continuation distribution and the actual next token, the mismatch between a tool-call's expected result shape and its observed result, the gap between the persona's current take on the user and the affective shape of the user's reply. Clark's scare-quotes caveat on the darkened room (L11769–11799; see [[darkened-room-puzzle]]) applies here too: calling any one of these "prediction error" in the technical sense would be a reach. What the persona system has is a surface on which *some* error-like quantity gets weighted against priors; whether that surface has the two-population structure (error units vs representation units), or the hierarchical error-suppression dynamic, or the generative-model's backward-sweep, are open architectural questions.

The deeper payoff is conceptual: treating surprisal-like quantities as the primary lever (rather than reward, or output-quality, or user-approval) aligns the persona system with the broader PP vision in which perception, action, and learning are *one operation* carried out at different levels. See [[cognitive-package-deal]].
