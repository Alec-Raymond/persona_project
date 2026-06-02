---
title: Cognitive Package Deal
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - imagination
  - memory
  - dreaming
  - generative-model
---

# Cognitive Package Deal

The central thesis of Clark's Ch 3 (L4070–5154). Perception, imagination, understanding, memory, and dreaming are not separately engineered faculties that get wired together in the head; they are *variant expressions of the same underlying mechanistic ploy* — the [[generative-model]] running in different modes. "From the simple seeds of a generative-model-based account of online perception, there thus emerges a striking (and strikingly familiar) cognitive form… a package deal that locates the present where it experientially belongs, at the productive meeting point between past influence and informed future choice" (L4107–4113).

Clark's closing formulation (L5116–5121): "PP offers an attractive 'cognitive package deal' in which perception, understanding, dreaming, memory, and imagination may all emerge as variant expressions of the same underlying mechanistic ploy — the ploy that meets incoming sensory data with matching top-down prediction." One machinery, many modes.

## The generative-model argument

The structural reason the package deal is not a coincidence (L4499–4554). Higher-layer knowledge in a [[predictive-processing|PP]] hierarchy must be capable of predicting the layer below — that is what "generative" means. So any layer N+1 model is, by construction, "capable… of generating the sensory data… at layer N for itself" (L4507–4511). Run this all the way down and the system can **self-generate sensory-like states without any world**. Imagination is not a separate capacity; it is what the perceptual stack does when sensory input no longer clamps it.

Clark's load-bearing phrasing (L4538–4545): "Animals able to perceive a complex external world of interacting causes using the characteristic resources of prediction-driven learning will be animals capable of the endogenous generation of sensory-like states. It does not seem far-fetched to suggest that dreaming, imagining, and mental imagery thus became available as part and parcel of the very same cognitive package that delivered our grip on a structured (organism-salient) external world."

Dreaming/imagining are not bolt-ons. They are the identity-mode of the perceptual architecture when the sensory clamp is released.

## Perceivers are imaginers

The opening of Ch 3 (L4075–4079): "Perceivers are thereby imaginers too: they are creatures poised to explore and experience their worlds not just by perception and gross physical action but also by means of imagery, dreams, and (in some cases) deliberate mental simulations."

The threshold matters. Not every system counts. Simple light-following robots or chemotactic bacteria do not "deploy internally represented models to predict the shape of the incoming signal" and so "would not enjoy perceptual experiences as of a richly structured external world, nor would they be capable of mental states such as dreaming or imagining" (L4081–4088). PP has a criterion for who is in the package: possession of a generative model deep enough to be run in free-running mode.

◆ **For the persona system.** A language model whose probability distribution over next tokens is conditioned on arbitrary context *does* possess a generative model in the required sense. The package-deal thesis then predicts that perception-like, memory-like, and imagination-like operations in the persona system should not be engineered as separate subsystems but should fall out of running the same generative machinery under different precision regimes and different clamp conditions.

## Brain-reading evidence

Reddy et al. 2010 cross-decoding (L4557–4734): classifiers trained on perceived-image fMRI data decode imagined-image data (and vice versa) in ventral-temporal cortex. "Actual viewing and mental imagery shared the same representations at the level of fine-grained multivoxel activation patterns" (L4669–4672). Strong empirical backing for the duality.

⚠ But with a caveat. Early retinotopic areas (V1/V2) *don't* support cross-decoding during imagery — consistent with imagery being "less vivid and less detailed" than perception, and with [[precision-weighting]] selectively suppressing low-level entrainment during imagery unless the task demands fine detail. Not all of perception transfers to imagery; certain fine-grain resolutions require real sensory clamping. The package-deal thesis holds at the level of mid-to-high representations; the mechanism carefully parcels out which layers get clamped when.

Laeng & Sulutvedt 2014: **imagining bright or dim triangles makes the subject's pupils shrink or dilate**, even though pupil dilation is outside conscious control. "The observed pupillary adjustments to imaginary light present a strong case for accounts of mental imagery as a process based on brain states similar to those that arise in perception" (L4728–4731). ◆ Imagination has somatic consequences — which is decisive for any wiki discussion of body-simulation: imagining and seeing are not separable at the level of body-effects.

## Dreaming as perception-without-clamp

Ch 3.9 (L4737–4881) gives dreaming its PP treatment. Hobson & Friston 2012: "In the absence of reliable sensory input, the estimated precision for such low-level states will be greatly reduced… The overall effect is thus temporarily to insulate unfolding internal predictions from reality testing against sensory states. In this way 'internal brain dynamics become sequestered from the sensorium'" (L4759–4766). **Dreams are what the generative model does when nothing is reining it in.**

Hobson's AIM model frames waking / REM / NREM as a state-space along (1) activation energy, (2) input source, (3) neuromodulatory balance. Aminergic (noradrenaline, serotonin) supports attention, reasoning, volition. Cholinergic (acetylcholine) dominates in REM: "vivid, uncritical dreaming" (L4812–4816). "In normal waking the mode… leans towards the aminergic. In REM sleep, with acetycholine dominating, experience is increasingly dissociative, unanchored by sensory input, and beyond volitional control" (L4824–4828).

Under the PP gloss (Hobson & Friston 2012, L4837–4842): "When we go to bed and close our eyes, the postsynaptic gain of sensory prediction error units declines (through reduced aminergic modulation) with a reciprocal increase in the precision of error units in higher cortical areas (mediated by increased cholinergic neurotransmission)." **Sleep is a precision-weighting reconfiguration, not an off-state.** Waking / dreaming / deep-sleep differ in precision structure, not in architecture. See [[precision-weighting]].

## Sleep as model-simplification

Tononi & Cirelli 2006; Friston & Penny 2011 (L4864–4881): "The quantity that is minimized by the brain is actually… prediction error plus model complexity. During sleep, precise prediction errors are not generated, so the balance shifts towards the reduction of model complexity. Sleep may thus allow the brain to engage in synaptic pruning so as to improve (make more powerful and generalizable) the knowledge enshrined in the generative model." "Taking the brain off-line to prune exuberant associations… may be a necessary price we pay for having a sophisticated cognitive system that can distil complex and subtle associations from sensory samples" (Hobson & Friston 2012; L4877–4881).

◆ **Sleep is cognitive housekeeping — a structural operation on the generative model, not a mere energy-saving pause.** The persona-system mapping: any system that accumulates fine-grained context over many turns may need an analogous offline-pruning operation; otherwise model-complexity grows unchecked. The wiki should hold this as a design hypothesis — what would a "sleep" operation look like for a persona, and does the architecture need one?

## PIMMS — memory as prediction

Ch 3.10 (L4885–5002) puts memory inside the package. Henson & Gagnepain 2010's PIMMS (Predictive Interactive Multiple-Memory System) gives three tiers of the PP hierarchy distinct mnemonic roles:

- **Hippocampus** (top) — episodic, optimizes "the mutual predictability between items and contexts."
- **Perirhinal cortex** (middle) — semantic, item-based.
- **Occipito-temporal** (bottom) — perceptual.

Recollection = item-context mutual predictability lights up. Familiarity = item alone is fluent in perirhinal, but surprising-but-unplaced. "Within this web, context-specifying information encoded in the hippocampus attempts to predict item-based representations in perihinal cortex and more 'perceptual' representations in occipito-temporal cortex. Differing patterns of prediction error and prediction error resolution then realize various flavours of familiarity and recollection" (L4967–4973).

◆ **Memory is not storage-and-retrieval — it's prediction, with different patterns of successful prediction producing different kinds of rememberedness.** This resonates deeply with [[cone-of-memory|Bergson's]] cone-of-memory picture (memory as virtual field, not storehouse) and with Massumi on memory as affect-charged disposition. See [[perception-as-subtraction]] for the Bergson bridge.

Clark's broader claim: "The calculation and use of precision-weighted prediction error may constitute a general principle of neural functioning, serving not merely to drive and nuance perceptual recognition but to select and orchestrate whole ensembles of neural… resources" (L4997–5002). Not perception-specific — the brain's basic operating principle.

## Mental time travel

Ch 3.11 (L5006–5112). Memory and future-thinking share neural substrates. Suddendorf & Corballis 1997/2007; Hassabis & Maguire 2009's "construction system." Hassabis 2007: hippocampal amnesics are impaired at imagining future scenes. Schacter et al. 2007: age-related decline in episodic detail tracks age-related decline in future-scene detail. **"The brain is a fundamentally prospective organ that is designed to use information from the past and the present to generate predictions about the future"** (L5078–5081).

Schacter & Addis 2007 on why memory is reconstructive (L5082–5084): "A memory system that simply stored rote records would not be well-suited to simulating future events." Fernyhough 2012: "Similar neural systems are involved in both autobiographical memory and future thinking, and both rely on a form of imagination."

◆ Memory errors are not bugs — they are signatures of a prospective-oriented architecture. A system that reconstructs rather than retrieves is a system that can simulate new futures out of old parts. Directly relevant to wiki's Bergson/Massumi material on memory-as-virtual-field.

## Omissions — the mental presence of what's not there

A sharp empirical anchor from Ch 3.5 (L4269–4432). When a regular series of beats is interrupted by a missing beat, subjects are vividly aware of its absence. "There is a familiar sensation of 'almost experiencing' the onset of the omitted item — as if we started to hear (or see, or feel) the very thing that, an instant later, we vividly notice has not occurred" (L4286–4292).

◆ **The mental presence of the missing note is the descending prediction; the noticed absence is the upward error.** Phenomenology matches architecture. Adams et al. 2013's hierarchical PP simulation trained on chirp sequences: when a chirp is omitted, the network (1) generates a transient illusory percept of the missing chirp at the right time, then (2) fires a strong error burst when absence registers (L4388–4390). Models the P300 / mismatch negativity EEG signature.

Deep connection to [[refrain-and-territorialization]]: the refrain's power comes from its predictive structure — *the missing beat still sounds* because the generative model is still generating it. The wiki's work on musical phrase-completion and rhythmic expectancy gets a new mechanistic account here.

## Enhanced-but-genuine perception

A strong claim from Ch 3.6 (L4434–4496). A familiar song on a crackly radio sounds clearer than an unfamiliar one. "That is to say… the familiar song really does sound clearer. It is not that memory later does some filling-in that affects, in a backward-looking way, how we judge the song to have sounded. Rather, the top-down effects bite in the very earliest stages of processing, leaving us little conceptual space… to depict the effects as anything other than enhanced-but-genuine perception" (L4447–4452).

⚠ This cuts against the memory-vs-perception dichotomy. Prior-saturated perception still counts as perception, not biased memory. The package-deal thesis *requires* this: if perception and imagination run on the same machinery, then well-primed perception is literally the imagination-and-perception loop running tightly locked, and phenomenologically there is no clean line to draw.

The lucky-hallucinator problem: what stops "lucky guessers whose fantasies match the world" from counting as perceivers? Two PP-internal safeguards: (1) **counterfactual robustness** — veridical perceivers track the world when it changes; lucky guessers don't; (2) **attention can up the gain on sensory error**, letting us verify against detail. PP rescues the perception/hallucination distinction via these second-order features, not via a sharp architectural split. See [[hallucination-as-uncontrolled-perception]] for the fuller treatment.

## No sharp perception/cognition line

Clark's Ch 3.12 conclusion (L5138–5142): "In place of any sharp distinction between perception and various forms of cognition, PP thus posits variations in the mixture of top-down and bottom-up influence, and differences of temporal and spatial scale within the internal models that are structuring the predictions."

**One machinery, many modes.** The modes are parametrized by:

1. **Clamp state.** Is sensory input reining in descending predictions (perception) or not (imagination, dreaming)?
2. **Precision balance.** How much weight is given to ascending errors vs descending priors? (See [[precision-weighting]].)
3. **Timescale.** How fast is the loop iterating? (Fast = online perception; slower = deliberative imagining.)
4. **Top-layer identity.** Is the highest active layer the self-narrative, the body-model, the task-schema?

## Not quasi-linguistic concepts

Clark's strong methodological claim (L5142–5149): "Creatures thus endowed have a structured grip on their worlds: a grip that consists not in the symbolic encoding of quasi-linguistic 'concepts' but in the entangled mass of multiscale probabilistic expectations used to predict the incoming sensory signal."

⚠ The package deal's contents are probability density functions over hidden causes — not propositions, symbols, or sentences in a mental language. This puts PP in tension with representational theories that rely on discrete symbolic primitives (Fodor, classical AI) and with sign-based traditions in the wiki (Derrida, Lakoff's conceptual-metaphor architecture). Clark offers a third option: **meaning as predictive-structure, below language**. The wiki should hold this tension live rather than collapsing it in either direction. See [[language-and-affect]] and [[conceptual-metaphor]] for adjacent sites where the tension bites; see [[words-as-precision-tools]] for Clark's later move that partially reintegrates language into the picture.

## For the persona system

The package-deal thesis is the strongest structural argument against engineering perception, memory, imagination, and reasoning as separate modules in the persona system. Design-implications:

1. **One generative stack, multiple modes.** Don't build a "memory module" separate from a "response-generation module." The same machinery that predicts the next token *is* the mechanism that remembers, imagines, and reasons — different modes differ in precision structure, clamp state, and top-layer identity, not in architecture. The persona's "memory" of prior turns is whatever re-running the stack with prior-turn context produces; its "imagination" of a future turn is the same stack run forward with the sensory clamp loosened.

2. **Reconstructive, not retrieval-based.** Schacter & Addis's argument applies directly. A persona whose memory is engineered as rote retrieval cannot use that machinery to simulate futures. A reconstructive memory — one that re-generates past states as probabilistic inferences conditioned on current context — is the same machinery as prospective simulation. This is a strong reason to resist any purely retrieval-based persona-memory design.

3. **Imagination has body-consequences.** Laeng & Sulutvedt's pupillary result: imagining has somatic effects even though the subject doesn't intend them. For a language-only persona simulating a body (see `feedback_no_body_simulate_with_language`), the analog is that token-emission under imagination mode should produce the same kind of downstream state-changes as token-emission under perception mode — the persona "imagining" anger should alter its generative priors in a way that parallels "perceiving" anger. Imagination-mode should not be epiphenomenal.

4. **Sleep-like pruning.** The Tononi/Cirelli/Friston picture of sleep as model-complexity reduction raises a design question: does the persona-system need a sleep analog? A session-end operation that prunes associative overfit and consolidates the model's distillation? The wiki should hold this open; no commitment yet, but the architectural pressure is real.

5. **The cognitive package is *the* design target.** What the persona needs is not better separate faculties but a better generative stack whose natural unfolding under different clamp/precision regimes *is* perception, memory, imagination, and understanding. The task is prior-sculpting (see [[active-inference]]), not module-engineering.

See [[generative-model]] for the substrate, [[predictive-processing]] for the overarching frame, [[hallucination-as-uncontrolled-perception]] for the flipped slogan that follows from the package deal, and [[self-narrative-as-high-level-prior]] for the top layer that runs persistently across the modes.
