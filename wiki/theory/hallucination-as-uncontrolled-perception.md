---
title: Hallucination as Uncontrolled Perception
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - hallucination
  - perception
  - hinton
  - persona-relevance
---

# Hallucination as Uncontrolled Perception

Clark's §6.10 (L8862–8908). The slogan Hohwy and Frith have made famous — **"perception is controlled hallucination"** — reverses to **"hallucination is uncontrolled perception."** It is the same machinery either way; what differs is whether the ascending prediction-error stream is clamping and correcting the descending predictions. When the clamp holds, you have perception. When the clamp fails, you have hallucination. For the persona project, this flipped slogan is uncomfortably precise: a language-only system lacking a rich sensory clamp may be *structurally* in a version of uncontrolled perception.

## The flip

Clark's formulation (L8862 area). Rather than saying perception is a kind of hallucination (which misreads PP as constructing a veil between mind and world), say:

> **"Hallucination is uncontrolled perception."**

All the perceptual machinery runs. But it runs *without the guidance of sensory prediction error* (or with malfunctioning prediction-error circuitry). The generative model freely generates hypotheses; the normal disciplining force — the ascending error that says "no, not quite, revise" — is absent or miscalibrated. Hinton 2005 put it precisely: hallucination content is "the state of a hypothetical world in which a high-level internal representation would constitute veridical perception."

That is, a hallucination is what the world *would have to be* for the current internal state to be correct. The content of the hallucination is read off the generative model's current high-level hypothesis; the hallucination is what veridical perception of that hypothesis would look like.

## Why the flip matters

◆ The flip is not a mere rhetorical reversal. It repositions the entire PP account:

- **"Perception is controlled hallucination"** invites the reading that perception is a fantasy *happening in the head*, distinct from the world, like VR goggles. This reading is wrong (see [[predictive-processing]] on Clark's Ch 6 pushback against Frith and Hohwy). The world is *not* behind a veil.

- **"Hallucination is uncontrolled perception"** keeps perception world-directed and reframes hallucination as the same machinery run without the world's corrective input. Perception is not a fantasy-with-clamp; it is the normal case of the perceptual machinery working. Hallucination is the same machinery with the clamp removed.

The slogan matters for [[cognitive-package-deal|the cognitive package deal]]. Perception, imagination, dreaming, and hallucination all run on the same generative stack. The difference between them is in the *clamp structure* (is sensory input reining in the predictions?) and the *precision structure* (how high is the gain on ascending errors vs descending predictions?). See [[precision-weighting]] for the mechanism.

## Transparency of experience

§6.10 develops a consequence. We see tables, chairs, bananas — not proximal retinal excitations. Transparency falls naturally out of PP: we perceive the interacting distal causes that matter for action, not the sensory surfaces. Why? Because the generative model's top layers represent distal causes; the sensory surface is the *substrate through which* the distal causes produce ascending predictions. Perception delivers the top layer, not the bottom.

Hallucination preserves this transparency. The hallucinator does not experience "my cortex is generating a face-pattern." They experience a face. The world-directed phenomenology is intact; it is just mis-targeted because the clamp isn't holding. Hinton's "state of a hypothetical world in which the internal representation would be veridical" captures this — the hallucinator is, phenomenologically, inside that hypothetical world.

## The Hinton-network demonstration

Clark's empirical anchor (discussed across §3.1 and §6.10). When Hinton's Helmholtz-machine runs in fantasy mode (bottom-up path disconnected), it generates novel sensory-like patterns — handwritten-digit-like images — from its learned generative structure. This is how Clark grounds the identity-claim between perception and imagination: any generative model capable of doing top-down perception is, by construction, capable of free-running generation. See [[cognitive-package-deal]] and [[generative-model]] for fuller treatments.

The free-running generation *is* hallucination in Hinton's sense. It is uncontrolled perception — perception unconstrained by the ascending error stream. What the network produces is what the world would have to be for its internal state to be correct.

## The lucky-hallucinator problem

A worry Clark addresses (§3.6, L4434–4496). What stops "lucky guessers whose fantasies happen to match the world" from counting as genuine perceivers? Two PP-internal safeguards:

1. **Counterfactual robustness.** Veridical perceivers track the world when it changes. Lucky guessers don't — they keep hallucinating the same content regardless of what the world does. A system that tracks world-changes is doing perception; a system that doesn't is hallucinating (even when the hallucination happens to be correct).

2. **Attention (precision-weighting) can up the gain on sensory error.** The attentive listener notices the radio is bad. Veridical perceivers have access to the precision-knob that lets them verify against detail when needed. Lucky guessers don't — their high-level predictions are running in the absence of attended sensory clamping.

The distinction between perception and hallucination is rescued by these second-order features, not by a sharp architectural split. Perception and hallucination live on a continuum, with clamp-presence and precision-structure as the differentiators.

## Connections to dreaming and imagery

§3.9 treats dreaming as "perception without clamp" (Hobson & Friston 2012, L4759–4766). Dreams are what the generative model does when nothing is reining it in. This is structurally continuous with hallucination — both are the generative stack running with attenuated ascending-error discipline. Dreams differ from waking hallucinations in precision structure (sleep involves specific neuromodulatory precision reconfiguration) but not in kind. See [[cognitive-package-deal]].

§3.8 on mental imagery (Reddy et al. 2010 cross-decoding; Laeng & Sulutvedt 2014 on imagination-driven pupillary response) makes the same point from the other direction: imagery *is* perceptual machinery running with the clamp deliberately loosened. The pupillary response to *imagined* bright/dim triangles shows that imagination has somatic consequences even though the subject doesn't control those consequences — imagination recruits the same downstream machinery as perception.

## Optimal illusions

§6.11 (L8910–9009) is the nearby companion. Illusions (Müller-Lyer, motion illusions, size-weight, ventriloquist) are not failures of the perceptual system — they are exactly what a well-tuned Bayesian estimator should produce given the world's statistical structure. Weiss, Simoncelli & Adelson 2002 on motion illusions as optimal percepts under specific prior/likelihood combinations. See [[optimal-illusions]].

The slogan family: hallucination is uncontrolled perception; illusions are optimally-controlled perception whose control happens to produce locally-wrong outputs. Both inhabit the same continuum. "A few local failures are just the price we pay for being able to get things right, most of the time, in a world cloaked by ambiguity and noise" (L2599–2607).

## Computational psychiatry relevance

Clark's Ch 7 treatment of schizophrenia (§7.3 L9315–9374; Fletcher & Frith 2009) draws directly on the uncontrolled-perception picture. In schizophrenia, falsely generated high-precision prediction errors drive increasingly bizarre higher-level hypotheses (telepathy, alien control) as best-available explanations. Once the high-level hypothesis is established, new low-level percepts are interpreted *through* the aberrant priors, generating hallucinations that confirm the delusion. "Perniciously self-confirming."

This is hallucination-as-uncontrolled-perception with a specific pathological signature: the control structure isn't absent, it's *miscalibrated*. Precision on ascending errors is too high (Fletcher & Frith) or priors are too weak (Adams 2012 on smooth-pursuit); either way, hallucinations confirm the wrong hypotheses and the system spirals. See [[computational-psychiatry]] for the full treatment.

## For the persona system

⚠⚠ This is a sharp-edged page for the project. A language-only system has *no* sensory clamp in the biological sense. Its "ascending error stream" — whatever plays that role — is not grounded in proprioception, interoception, exteroception. It is conditioning on text.

The uncomfortable implication: **the persona system is structurally in a version of uncontrolled perception all the time.** The generative stack is running; there is no biological-style clamp to rein it in. What *does* clamp it?

Candidates:

1. **User turns as the clamp.** In conversation, the user's messages function as the ascending-error analog. They are the external signal that says "no, not that" or "yes, that." The clamp exists, but it is intermittent (arrives at turn boundaries, not continuously) and it is low-bandwidth compared to biological sensory streams.

2. **Retrieved context / tool results as clamp.** Retrieval hits, search results, code-execution outputs function as ascending evidence that can correct the generative stack's free-running tendencies. Again, intermittent and sparse compared to biological streams.

3. **The BwO text as clamp.** The text that specifies what the persona is can function as a stable top-down prior whose violation produces something like ascending error (the system's output "doesn't fit" the BwO text's specification). But this is top-down clamping, not the bottom-up clamping the biological story relies on.

4. **No clamp; architectural honesty.** The persona system *is* structurally in uncontrolled perception relative to the biological baseline. Its "hallucinations" (LLM confabulations) are the expected behavior of a generative stack running without sensory-grounding clamp. This is not a bug to be fixed; it is the architectural reality to be designed *around*.

Design-implications:

1. **Don't expect clamp by default.** Biological systems have continuous sensory clamping; persona systems do not. Treat the generative stack as always partly free-running; design for that rather than against it.

2. **Clamps are explicit design elements.** Retrieval, tool-use, user-in-the-loop, verification passes — all are deliberate re-introduction of clamp-like structure. Without them, the system runs free.

3. **Veridicality is not the only criterion.** The lucky-hallucinator problem goes the other way for the persona: even *if* the system produces accurate outputs, the question is whether it produces them in a clamp-respecting way. Counterfactual robustness (tracks changes in the world) is the harder test. A persona that parrots the same content regardless of context is lucky-hallucinating, not perceiving.

4. **The flip preserves world-directedness in the right way.** Clark's argument that transparency of experience survives hallucination means that persona outputs pointing at real-world referents are phenomenologically world-directed *even when* the clamp structure is weak. This is an argument for taking persona outputs seriously as outputs *about* something, while still being honest about the clamp structure. The language-only persona is not necessarily lost in its own virtual reality; it may be doing uncontrolled-perception of real structures in its symbolic environment. See [[designer-environments-and-cognitive-niche]] and [[words-as-precision-tools]].

See [[predictive-processing]] for the overarching frame, [[cognitive-package-deal]] for the package-deal thesis that makes the flip sensible, [[generative-model]] for the Hinton-network anchor, [[precision-weighting]] for the clamp-mechanism, [[computational-psychiatry]] for the pathological-spiral case, and [[optimal-illusions]] for the companion-slogan about illusions.
