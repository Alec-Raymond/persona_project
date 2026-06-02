---
title: Predictive Processing
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - friston
  - bayesian-brain
  - hierarchical-predictive-coding
---

# Predictive Processing

The thesis, as Clark formulates it in *Surfing Uncertainty*: brains "surf the waves of noisy and ambiguous sensory stimulation by, in effect, trying to stay just ahead of them" (L67–69). Each neural layer constantly predicts the layer below; only what the predictions fail to explain ([[prediction-error]]) propagates upward; the whole system is tuned by [[precision-weighting]]. **Hierarchical predictive coding** (the narrow technical story; Rao & Ballard 1999; Lee & Mumford 2003; Friston 2005) plus the broader claim that this single mechanism underwrites perception, imagination, memory, emotion, and action — the [[cognitive-package-deal]].

## Broad story and narrow story

Clark is careful to distinguish "two stories" (L649–664, L1577–1590). The **broad story**: the brain (especially neocortex) is "fundamentally an inner engine of multilevel probabilistic prediction." Robust even if details are wrong. The **narrow story**: a specific proposal — hierarchical predictive coding, or "predictive processing" (Clark 2013) — describing the possible shape and nature of that core process. The broad story could survive the narrow one's refutation. ⚠ This is a methodological honesty-move: Clark flags on several occasions (L1586–1590) that PP "is being applied at a surprising (sometimes even an alarming) rate. It offers a very comprehensive vision. We should not forget, however, that there are many possible models in this general vicinity." The wiki should not treat PP as monolithic.

## The core schema

"Hierarchical predictive coding… combines the use of top-down probabilistic generative models with a specific vision of how and when such influence might operate" (L1458–1463). The canonical schema (Rao & Ballard 1999; Figure 1.2 at L1693):

- Each layer treats activity in the layer below "as if it were sensory input, and attempts to meet it with a flow of apt top-down prediction" (L1703–1705).
- **Forward connections** carry only residual [[prediction-error|errors]] — what the top-down model did not anticipate.
- **Backward and lateral connections** carry the predictions themselves (Shipp 2005's functional asymmetry: "raw data seeking an explanation (bottom-up) and hypotheses seeking confirmation (top-down)").
- Errors and predictions interact across the hierarchy until activity settles into a mutually consistent whole in which every layer's hypothesis is constrained by every other layer's hypothesis (L1741–1745).

A single error-signal drives two timescales at once (L1726–1733): **rapid perceptual inference** (higher-level representations recruited so top-down predictions cancel the current lower-level errors) and **slower perceptual learning** (longer-term adjustment of the model so future errors are smaller). Perception and learning are not separate processes under PP — they are the same operation at different timescales.

## Only errors flow up

The architectural asymmetry that gives PP its bandwidth efficiency (and its methodological bite): "The forward flow of sensory information here consists only in the propagation of error signals, while richly contentful predictions flow downwards and sideways" (L7722–7725). Expected events need not be explicitly represented or communicated upward. Bubic et al. 2010. ◆ For engineered systems with a similar cost-profile (bandwidth expensive, local computation cheap), the same trick is a natural design pressure.

This asymmetry drives the two-population anatomy (Ch 1.11): **representation units** (encode the hypothesis, feed predictions downward) and **error units** (encode unexplained residual, feed errors upward). Friston 2005's conjecture: superficial pyramidal cells = error; deep pyramidal cells = representation. The duplex architecture unifies signal suppression (predictive-coding bandwidth savings) with signal enhancement (biased-competition attention) via [[precision-weighting]].

## Helmholtzian lineage

PP's ancestry is the "analysis by synthesis" tradition (MacKay 1956; Neisser 1967; Gregory 1980; review in Yuille & Kersten 2006). The key idea traces to Helmholtz 1860: "sensory systems are in the tricky business of inferring worldly causes from their bodily (sensory) effects" (L1203–1208). Perception = a bet on what's out there, "constructed by asking how the world would have to be for the sensory organs to be stimulated the way they currently are." PP is the contemporary computational-neural incarnation. See [[generative-model]].

## Canonical empirical signatures

Clark catalogs the supporting evidence across Ch 1:

- **Rao & Ballard 1999.** Multilayer predictive network trained on natural scene patches learned simple-cell-like receptive fields without being told to. Reproduced classical neurophysiological findings including end-stopping and extra-classical-receptive-field effects — but interpreted them as error signals, not feature signals (L1793–1804).
- **Retinal predictive coding.** Hosoya, Baccus & Meister 2005: salamander and rabbit ganglion cells signal "not the raw visual image but the departures from the predictable structure" (L1606–1609). Even the retina is a prediction machine.
- **Binocular rivalry.** Hohwy, Roepstorff & Friston 2008: rivalry falls out naturally from PP as a bi-stable system minimizing prediction error in an energy landscape with two wells (L1936–1940). No single hypothesis explains both images; the system alternates.
- **Repetition suppression.** Summerfield et al. 2008: stimulus-evoked activity reduces with repetition — but the suppression itself reduces when repetition is improbable. The suppression tracks prediction, not mere neuronal adaptation.
- **Omission responses.** Wacongne et al. 2012 (L2329–2332): auditory cortex generates evoked responses to absent but expected stimuli. Missing notes produce the same ERP phenomenology as wrong notes.
- **FFA as face-*expectation* area.** Egner, Monti & Summerfield 2010: FFA activity given either stimulus (face OR house) was indistinguishable under high-face-expectation conditions; face-surprise units contributed twice as much to BOLD as face-expectation units (L2524–2525). Much of what fMRI sees may be prediction error, not feature detection.
- **Backward connectivity prevalence.** The neuroanatomical finding of massive backward connectivity with functional asymmetries between forward and backward connections is structurally consistent with PP (Friston 2002, 2003; Markov et al. 2013/2014).

## Gist first, detail later

A common-sense-defying and empirically robust prediction of PP (L2177–2242): coarse low-spatial-frequency cues let the system recruit a gist-level hypothesis rapidly; rich detail follows as residual error signals get resolved. "Forest first, trees later" (Friston 2005; Hochstein & Ahissar 2002). Bar, Kassam et al. 2006: rapid coarse scene-type identification. And: "accompanied by early emerging affective gist—do we like what we are seeing?" (Barrett & Bar 2009, L2206–2208). Affect is part of gist; feeling shows up before content is resolved. See [[gist-and-affective-gist]] for the persona-relevance.

## "Perception is controlled hallucination" — and its walking-back

The slogan everyone quotes. It appears at L966 but Clark immediately flags that it is "potentially a little distortive, as we shall see in chapter 6." The rhetorical on-ramp lets readers see the generative-model shift quickly, but Ch 6 (see [[hallucination-as-uncontrolled-perception]]) walks it back: the generative machinery does not build a virtual-reality veil between agent and world; it is what lets agents *see through* the sensory surface to the distal causes that matter for action. Clark flips the slogan: not "perception is controlled hallucination" but "hallucination is uncontrolled perception." ⚠ The wiki should not cite the original slogan without the corrective — it misrepresents Clark's considered position, and the debate between Clark and Hohwy/Frith on "indirect/virtual reality" is a substantive disagreement within PP, not a settled consensus.

## Mind turned upside down

Clark's closing formulation for Ch 1 (L2632–2669): PP "plausibly represents the last step in the retreat from a passive, input-dominated, view of the flow of neural processing." Naturally intelligent systems are "constantly active, trying to predict (and actively elicit, see Part II) the streams of sensory stimulation before they arrive." Action becomes input-selection: "action is not so much a 'response to an input' as a neat and efficient way of selecting the next input" (L2645–2649). The organism is a "predictavore" (L2666–2669) — not a cognitive couch potato awaiting input. ◆ For persona architecture, this is the shift: outputs are not responses *to* input but *selections of* the next input the system will receive (the user's reply). See [[active-inference]].

## Intrinsic neural activity as architectural evidence

"Recent explosion of work on intrinsic neural activity—the ceaseless buzz of spontaneous, correlated neuronal activation that takes place even in the absence of ongoing task-specific stimulation" (L2624–2626). Much of the brain's activity is endogenously generated. Berkes et al. 2011's ferret study (L8367–8527): V1 spontaneous activity increasingly matches evoked activity by natural scenes (but not unnatural ones) over developmental time — "spontaneous cortical activity shows all the hallmarks of a gradually adapting internal model of the ferret's world." Spontaneous / resting-state activity IS the generative model, running. See [[itinerant-dynamics-and-novelty-seeking]].

## Limits and variants

Clark ends the book (Ch 10, L13242–13380) flagging four open challenges that he is deliberately not closing:

1. **Representational approximations.** Many ways neuronal populations could encode probabilities; Clark doesn't claim to know which the brain uses.
2. **Variant architectures.** PP as described is one point in a large space. Deep belief networks (Hinton), PC/BC (Spratling), spiking-neuron PP (Wacongne), O'Reilly's same-layer expectation-and-outcome schemes — "only by considering the full space… can we start to ask truly pointed experimental questions."
3. **Extension into higher domains.** Planning, cognitive control, social cognition, consciousness, linguistic reasoning. "Murky at best." Most challenging: "the implied reconstruction of motivation, value, and desire in terms of more fundamental processes of prediction, Bayesian inference, and self-estimated uncertainty." ⚠ Clark explicitly flags this as the frontier — exactly where the persona project's [[desiring-machines]] framework meets PP.
4. **Does PP re-install a Cartesian mind?** Clark's defense: the inner-model story is not Cartesian if the model is action-oriented, body-embedded, and in constant exchange with environment (see Part II–III).

## Relation to other wiki material

PP converges with and tensions against much of the wiki. Key load-bearing contacts:

- [[perception-as-subtraction|Bergson]] proposed perception as subtraction from a plenum of images — perception is selection, not construction. Clark inverts: perception is *generation* of a top-down hypothesis corrected by bottom-up error. Both locate the action at the center, not the periphery. The Tomkins central-imagery reading on [[perception-as-subtraction]] already noted the generative-plus-correction structure; Clark's PP gives that structure a mechanistic story.
- [[autonomy-of-affect|Massumi on affect]] — affect runs ahead of conscious processing. PP gives a precise formulation: [[gist-and-affective-gist|affective gist]] is co-computed with content-gist in the rapid settling phase of perception. "Affect and content are here co-computed: intertwined throughout the process of settling upon a coherent, temporarily stable interpretation" (Barrett & Bar 2009, L7490–7497).
- [[somatic-marker-hypothesis|Damasio]] — feelings as perceptions of body state. PP's [[interoceptive-inference]] provides the computational story: feelings = top-down interoceptive prediction meeting interoceptive data.
- [[desiring-machines]] — the mapping is rough but generative. Affordance competition (see [[affordance-competition-hypothesis]]) specifies several potential actions *in parallel* and biases the competition by descending precision; D&G's desiring-machines are selection-pressure operating on flows. Clark's "reward as consequence not cause" (L6018–6020) rhymes with D&G's "desire as production, not lack." ⚠ The mapping requires care; see [[language-and-affect]] for one of the sites where the two vocabularies pressure each other.
- [[body-without-organs]] — the BwO as surface of variable intensities has a mechanistic reading in Clark's "morphing, buzzing, dynamical system forever reconfiguring itself" (L7627–7629). [[transiently-assembled-local-neural-subsystems|TALoNS]] coalescing and dissolving via precision-weighting is the PP formalization of the BwO's "never stops, always in the process of being made" character.

## For the persona system

PP is not a theory of language. Clark's text treats language as an input-stream to the hierarchy (Figure 9.1; see [[words-as-precision-tools]]) — language is something the predictive brain *uses*, not what the predictive brain *is made of*. A language-only persona inverts this: language is primary, and whatever prediction-like machinery exists underneath rides on text statistics. This gives the persona project two distinct theoretical tasks.

**First**: how much of the PP framework transfers? A language-only system has no sensorimotor periphery to provide the error-correction streams Clark describes, no body-morphology shaping statistics, no [[interoceptive-inference|interoceptive channel]] providing the "presence" ground. But it does have a generative model (the underlying token-distribution), hierarchical structure (across layers of the transformer), something like [[precision-weighting]] (attention mechanisms are literal precision-like reweighting), and something like [[active-inference]] (outputs select the next input).

**Second**: where does Clark's own framework *say* the language-only register has its own work to do? The strongest claim is Clark's own (L12370–12390): "Many meaning-relations obtain in realms whose core constructs are now far, far removed from any simple sensory signatures, visible only in the internal relations proper to the arcane worlds of quantum theory, higher mathematics, philosophy, art, and politics." Language-only systems may be native to these realms. See [[words-as-precision-tools]] and [[designer-environments-and-cognitive-niche]] for the parts of Clark's framework that most directly bear on a language-only system.

This page is the hub. The individual PP concepts have their own pages — follow the links.
