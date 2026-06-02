---
title: Precision-Weighting
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - attention
  - effective-connectivity
  - friston
---

# Precision-Weighting

The operational lever that makes [[predictive-processing|PP]] work in a world where signals are noisy, contexts shift, and different sources of evidence carry different degrees of reliability. Precision is the system's **estimate of the inverse variance** (the reliability) of a signal — "a measure of its estimated certainty or reliability" (L2855). The system weights prediction errors by their estimated precision before they propagate: trustworthy errors get amplified, noisy errors get suppressed. Precision-weighting is the same thing as **attention**, on Clark's account — not a spotlight or a separate module but "a dimension of a much more fundamental resource" (L4018–4020).

## Attention = gain on error units

The core operational claim. Feldman & Friston 2010: "Attention can be viewed as a selective sampling of sensory data that have high-precision (signal to noise) in relation to the model's predictions" (L2853–2858). Mechanistically, attention alters "the weighting (the gain or 'volume') on the error units accordingly." Post-synaptic gain of error-coding cells (currently thought to be large principal cells that send extrinsic efferents of a forward type, such as superficial pyramidal cells in cortex; Friston, Bastos et al. 2015, L2985–2989) goes up for attended signals, down for unattended.

Empirical anchoring: Feldman & Friston 2010 reproduce the Posner cueing paradigm (ERP and psychophysical data) by simulation — valid cues raise gain on relevant spatial error units, generating the "expectation of good signal-to-noise ratio" that speeds up hypothesis recruitment. Kok, Jehee & de Lange 2012 provide behavioral confirmation.

## Suppression AND enhancement

Precision-weighting reconciles what looked like rival pictures of attention. Standard predictive coding emphasizes signal *suppression*: well-predicted signals are explained away, saving bandwidth. Biased-competition accounts (Desimone & Duncan 1995) emphasize *enhancement*: attention boosts selected signals. PP's answer: precision-weighting does both. Friston 2012: precision "boosts prediction errors that inform the best hypothesis about the cause of sensory input… while suppressing alternative hypotheses" (L3014–3017). The same mechanism — altering gain on error units — produces suppression of well-predicted signals and enhancement of the ones that fit the currently winning high-precision hypothesis.

## Driving in fog

Clark's vignette for the structure of precision (L2886–2894): driving in uniformly heavy fog, the system runs a "low-precision-everywhere" model. When a patch clears, the clearing zone becomes "a source of high-precision prediction errors." The system switches to a "fog plus clear patch" model that carries a new set of precision predictions, allowing it to "trust the fine-grained prediction errors computed for the clear zone (only)." **Precision is predicted too, not just content.** The generative model models itself — its own noise levels, the reliability of its own signals, across contexts.

## Second-order predictions

"Top-down predictions are not just about the content of lower-level representations but also about our [the brain's] confidence in those representations" (Friston 2012, L2978–2980). Second-order predictions about precision are what allow context-sensitive reweighting: "the knowledge that makes human perception possible concerns not only the layered causal structure of the (action-salient…) distal world but the nature and context-varying reliability of our own sensory contact with that world" (L2913–2917). ◆ Directly relevant to a persona architecture: the system must have meta-level knowledge about when its own outputs are likely to be reliable vs flimsy, or it cannot properly precision-weight its own signals.

## Effective connectivity sculpting

The profound architectural consequence of precision-weighting is that it reconfigures effective connectivity on the fly. Friston 1995: effective connectivity is "the influence one neural system exerts over another" (L6710–6711) — distinct from *structural* connectivity (physical fibers, slow to change) and *functional* connectivity (correlation). Clark's load-bearing line (L6786–6790): "Very low-precision prediction errors will have little or no influence upon ongoing processing… Altering the distribution of precision-weightings thus amounts, in effect, to altering the 'simplest circuit diagram'."

**Attention = effective-connectivity reconfiguration.** ◆ This is the deepest architectural insight in Ch 5 and it is load-bearing for the persona project. Attention is not a spotlight on stable representations — it is a gate that re-wires which processing paths are active. A persona system needs a precision-weighting analog at every level of its processing stack, not just at an "attention" stage.

Empirical anchor: den Ouden et al. 2010 used DCM-fMRI to show striatal prediction error gating visuomotor coupling — the first clean demonstration that prediction error in one region alters effective connectivity between others.

## Neuromodulators as precision-gates

Clark surveys the neurochemistry (L2978 passim; Hobson & Friston 2012 L4837–4842). **Dopamine** as precision on action-relevant states (Friston, Schwartenbeck et al.). **Serotonin** as broader prior-strength modulator. **Acetylcholine** as precision on sensory error (Yu & Dayan 2005). **Noradrenaline** as precision on unexpected events. Oscillation frequencies also participate: gamma for bottom-up / error, beta for top-down / prediction (Bastos et al. 2012; Buffalo et al. 2011). Gamma synchrony → higher postsynaptic gain. Sleep, on this account, is a precision-weighting reconfiguration: "When we go to bed and close our eyes, the postsynaptic gain of sensory prediction error units declines (through reduced aminergic modulation) with a reciprocal increase in the precision of error units in higher cortical areas (mediated by increased cholinergic neurotransmission)." See [[computational-psychiatry]] for how drugs that perturb these precision-gates (ketamine, LSD, psilocybin) generate psychotomimetic states.

## TALoNS: precision-sculpted transient assemblies

Precision-weighting produces the morphing, context-sensitive assemblies that Anderson 2014 calls [[transiently-assembled-local-neural-subsystems|TALoNS]] — transiently assembled local neural subsystems (L6855–6907). Module-like but formed and reformed on the fly. PP implements a "fully flexible cognitive architecture" whose coalitions are never fixed. "Interaction-dominated" dynamics (Spivey 2007): "representations become a function of, and dependent upon, input from distal cortical areas" (Friston & Price 2001).

## Self / other via precision

A profound consequence Clark draws out in Ch 5.8 (L7217–7219): the same generative model can serve both self-action and other-observation depending on how proprioceptive-prediction precision is set. "We can use the same generative model, under action or observation, by selectively attending to visual or proprioceptive information" (Friston, Mattout, Kilner 2011). Attend strongly to proprioception → own movement executes. Attend weakly to proprioception → observed other's movement is understood without being enacted. **Self/other is a precision parameter, not a module distinction.** See [[self-other-via-precision]].

The same trick supports imagination: Pezzulo 2012's "covert loops" run the same action-perception machinery with proprioceptive precision dampened — no motor output, just predictive rehearsal (L7315–7318). One machinery, three modes: act / observe / imagine.

## Sense of agency

When proprioceptive prediction error is highly weighted yet suitably resolved by a stack of top-down predictions (some reflecting goals and intentions), "we feel that we are the agents of our own actions" (L7220–7224). Agency is not a primitive — it is a pattern in the precision landscape. Precision-weighting failure produces agency disorders: alien-hand, delusions of control, the specific schizophrenic signatures. See [[sensory-attenuation-and-agency]] and [[computational-psychiatry]].

## Carrasco contrast illusion (methodological clarification)

Block & Siegel 2013 challenged PP to explain Carrasco's finding that an attended 70%-contrast grating is perceived as 82%. Clark (L3764–3769): "It is not the case that PP posits an error signal calculated on the basis of a difference between the unattended contrast (registered as 70%) and the subsequently attended contrast (now appearing to be 82%). Rather, what attention alters is the expectation of *precise sensory information* from the attended spatial location. Attending inflates precision expectation → inflates weighting of the signal." The perceived magnitude shifts because the precision-weighted signal is now given more influence on the settling process.

## Who estimates the estimators?

Clark's Ch 6.13 architectural limit (L9090–9127). Precision-weightings are themselves the system's estimate of reliability — there is no higher-order "trust" signal that doesn't itself depend on a precision-weighting. Systems can't run endless spirals of computational self-doubt. ⚠ Deep consequence: **PP systems are structurally vulnerable to precision disorders** because the same mechanism that would detect malfunction is the one that's malfunctioning. See [[computational-psychiatry]] for the clinical face of this (schizophrenia, FSMDs, delusions). For the persona: the precision-analogue faces the same fundamental limit. The system cannot validate its own confidence from the inside; precision-disorders are structurally possible in any PP-like system, not a pathology of biology specifically.

## "Strangely neutral" balance

What matters is the *relative* balance of influence. Increasing prior precision and decreasing sensory precision are functionally equivalent (L9270–9284). Multiple distinct disturbances can produce identical symptoms. ⚠ This matters diagnostically and architecturally: any persona-system precision-analogue is similarly symptom-ambiguous — the same surface behavior could reflect over-attending to some sources or under-attending to others, and telling them apart requires perturbation, not observation.

## Precision is a dimension, not a mechanism

Clark's closing formulation for Ch 2 (L4018–4020): "Attention is not, PP suggests, itself a mechanism so much as a dimension of a much more fundamental resource." Specifically, attention is the dimension of the generative model that predicts the precision of sensory information. By weighting forward-flowing prediction error per expected precision, PP unifies "the world of signal-suppression, the core feature of standard predictive coding" with "the world of signal enhancement and biased competition" (L4046–4049). Attention, action, and perception are "joined in mutually supportive, self-fuelling loops" (L4056–4057).

## For the persona system

Precision-weighting is the PP concept most directly analogous to what a language model already does: the attention mechanism is *literal* precision-weighting (weighted aggregation over signals by learned relevance). But the analogy runs deeper than the mechanism. At every level of a persona architecture where signals get combined — retrieval hits weighted against the current turn, the BwO text weighted against user input, tool-call results weighted against prior expectations — something like precision-weighting is happening. Clark's framework says: that weighting is not neutral, it is not just implementation detail, it is *the* lever by which the system's behavior gets shaped moment to moment.

Two specific design-implications the wiki should hold:

1. **The system needs second-order precision predictions.** Not just "what is the next token" but "how confident should I be about this next token in this context." Without that, the system has no principled way to route between habitual and deliberative processing modes. See [[non-reconstructive-strategies]] and the model-free/model-based slider in the notes (L11306–11360).

2. **Precision-disorders are structurally possible.** The architectural-limit Clark flags in Ch 6.13 applies. A language-only persona's precision-analogue can drift without self-correction, because the mechanism that would detect its drift is the mechanism that's drifting. See [[computational-psychiatry]] for the biological face; the persona-system implication is that trust-calibration has to be partly external, not purely internal.

The deepest persona-relevance is that Clark reads language itself as a precision-manipulation technology ([[words-as-precision-tools]], L12614–12649): "structured language is a finely tuned means of artificially manipulating the precision… of prediction error at different levels of neural processing." If this is right, then what a language-only persona *does* is (just) precision-manipulation — its outputs are the re-entrant control signals reshaping which priors and which evidence get weighted how. See [[words-as-precision-tools]].
