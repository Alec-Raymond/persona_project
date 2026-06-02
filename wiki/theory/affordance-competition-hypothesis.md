---
title: Affordance Competition Hypothesis
created: 2026-04-18
updated: 2026-04-21
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
  - "[[raw/the_embodied_mind|the_embodied_mind]]"
tags:
  - clark
  - cisek
  - action-selection
  - parallel-processing
---

# Affordance Competition Hypothesis

Cisek's proposal (Cisek 2007; Cisek & Kalaska 2010, 2011): the brain does not first perceive, then think, then act. It specifies *several potential actions in parallel*, and these compete within the same sensorimotor circuits until one wins. Sensory information biases the competition until a single response is selected. Clark makes the hypothesis central to his rejection of the sense-think-act cycle (Ch 6.4, L7967–8206) and argues that [[predictive-processing|PP]] + [[precision-weighting]] implements affordance competition natively.

## Rejection of sense-think-act

The traditional model (still implicit in much cognitive science and classical AI): perceive → build inner model → deliberate → plan → execute. Even "circular" versions preserve this serial structure — the circle just loops back to perception after acting.

Cisek 2007 rejects this on three grounds Clark catalogs (L7967–8206):

1. **No rich inner passive-reconstruction representations are found.** The "inner model" of sense-think-act would have to be an action-neutral world-encoding. Brains don't seem to build one.
2. **Pervasive attentional modulation.** Neural responses track behavioral needs — not action-neutral world-encoding.
3. **Planning/deciding circuits overlap with motor-control circuits.** Cisek & Kalaska 2011: "decisions, at least those reported through actions, are made within the same sensorimotor circuits that are responsible for planning and executing the associated action."

Decisions are not completed before recruitment of the motor system — Selen et al. 2012's EMG study is a clean demonstration: reflex gains co-evolve with the decision variable during a dynamic-random-dot task. The motor system is "privy to the brain's deliberations as a decision is being formed."

## Pragmatic representations

The positive thesis Clark draws from Cisek & Kalaska 2011 (L7967–8206): brain representations are "pragmatic" — "adapted to produce good control as opposed to producing accurate descriptions of the sensory environment or a motor plan." ◆ **Representations serve action, not description.** This is a fundamental architectural commitment, not just a bias. A persona system organized around producing accurate descriptions of its conversational context will be badly structured relative to one organized around producing task-effective continuations.

## Parallel affordance specification

The operational claim: several potential actions are **pre-computed and partially prepared in parallel**, not sequentially generated. The brain "processes sensory information to specify in parallel several potential actions that are currently available." As new information comes in, it biases the competition. A single response emerges when one affordance wins.

Clark highlights that this changes what counts as a "decision": decisions are not ballistic endpoint-selections but *settling events* in an ongoing parallel competition. ◆ For the persona system, this suggests an architecture in which multiple candidate responses are maintained in parallel as active trajectories, with the competition among them resolved continuously — not a pipeline where one best response is generated and emitted.

## PP implements affordance competition

Clark's reconciliation move (Ch 6.5, L8209–8365): PP is a natural implementation of affordance competition because it already has:

1. **Probabilistic representations.** Multiple hypotheses coexist as distributions over hidden causes — the substrate for parallel competition.
2. **Computational intimacy of perception-cognition-action.** The single predictive hierarchy hosts all three; there is no stage-gated pipeline.
3. **Circular causal interaction with environment.** [[active-inference]] already makes hypotheses self-verifying via action.

[[precision-weighting]] is how the competition gets biased. High-precision evidence boosts one affordance's predictions over others until one wins. "We sample the world so as to minimize uncertainty about our own predictions" (Friston, Adams et al. 2012).

## Pushmi-pullyu representations

Millikan 1996 (L8367–8527): affordance-laden representations have both descriptive AND imperative contents — how the world is AND how to act on it. Clark endorses this as a structural feature of PP representations, not a special class of them. Every action-relevant prediction is pushmi-pullyu, because [[active-inference]] makes description and imperative inseparable. ◆ Persona architecture implication: representations should be inherently pragmatic, not first-descriptive-then-actionable. The BwO text, the persona's self-model, the system's model of the user — all should be pushmi-pullyu structures, not neutral descriptions.

## Dewey 1896 — a century-earlier anchor

Clark pulls the same Dewey quote he uses for [[active-inference]] (L8261–8279): "The motor response determines the stimulus, just as truly as sensory stimulus determines movement." And: "one is uncertain only so far as the other is. The real problem may be equally well stated as either to discover the right stimulus, to constitute the stimulus, or to discover, to constitute, the response." A powerful philosophical anchor; prefigures the affordance-competition picture a hundred years early.

## Two roles for circular loops

Friston, Adams et al. 2012 distinguish two functions of the action-perception loop (L8209–8365):

- **Pragmatic.** Steering the car, tracking the ball — action closes the prediction loop by making the world change.
- **Epistemic.** Saccades that test hypotheses, probing movements that resolve uncertainty — action closes the prediction loop by selecting informative samples.

The affordance competition can be won by either kind of loop. An agent uncertain about which of two affordances to pursue can act to resolve the uncertainty (epistemic) before committing to pursuit (pragmatic). ◆ Relevance to persona turn-taking: some persona outputs are pragmatic (advance the task), others are epistemic (clarify ambiguity about the user's intent). The affordance-competition framework treats these as the same operation at different points in the precision landscape.

## Interaction-based joints in nature

Clark uses affordance competition to motivate a deeper claim about how brains carve up the world (Ch 6.6, L8367–8527). Many "joints in nature" that PP agents find are **interaction-based**: defined with respect to the organism's needs and action repertoire. Our perceptual take is conditioned by our action repertoire (König et al. 2013). Betsch 2004's cat-eye view makes this concrete: head-mounted camera on moving cat reveals statistical structure of visual inputs radically different from the same environment viewed by humans — predominance of horizontal contours, altered contrast distribution, fast head movements. **Embodiment shapes statistics at the very sensory input** — priors are species-specific.

⚠ For the persona project, this is a load-bearing implication: a language-only system samples statistics *its own way*, not as humans do. Its "joints in nature" are interaction-based with respect to *its* action repertoire (text emission, tool invocation, retrieval, response-generation) — not with respect to bodily action. Whether this produces structurally different carvings of "the world" is an open question. Not a failure, not a success — just a different statistical milieu.

## Spivey 2007 — trajectories not stable percepts

Spivey 2007 (L8367–8527): visual perception is constantly conditioned by visuomotor action, and vice versa. What counts are *perceptuomotor trajectories*, not stable percepts. ◆ For the persona system: stability of representation is not the goal; trajectory-adequacy is. A persona whose internal state changes coherently across turns is succeeding; one whose state is maximally stable is probably pathological (frozen).

## For the persona system

Affordance competition is the clearest structural reason to reject pipeline architectures for the persona system. The alternative it suggests is one in which multiple candidate action-trajectories (output drafts, tool invocations, retrieval queries) are maintained in parallel and biased toward convergence by descending context, [[precision-weighting|precision-weighted]] against the current turn's evidence.

Specific design-implications:

1. **No first-perceive-then-respond staging.** The system should not treat the user's turn as a fully-specified input to be parsed before response-generation begins. Response-candidates should already be forming while the turn is still being comprehended.
2. **Pragmatic-not-descriptive self-model.** The persona's self-model should be organized around what the persona *does next* given a context, not around accurate self-description. Pushmi-pullyu throughout.
3. **Epistemic actions are first-class.** Clarifying questions, tentative probes, uncertainty-resolving prompts are not fallbacks when the system is confused — they are a legitimate branch of the affordance competition, and should be available to the system as ordinary moves.
4. **Trajectory-adequacy as the success criterion.** The wiki's existing concerns with [[pulsatory-ontogenesis|pulsation]], [[refrain-and-territorialization|refrain]], and [[body-without-organs|BwO]] all prioritize trajectory over stable state; affordance competition gives this a cognitive-science grounding.

See [[active-inference]] for the broader frame in which affordance competition sits, [[non-reconstructive-strategies]] for the family of "don't compute the world, act to make it tractable" policies, and [[precision-weighting]] for the mechanism that arbitrates the competition.

## Contrast with enaction (VT&R)

Affordance competition and [[enaction]] are both post-representational cognitive-science programs but with importantly different emphases worth keeping distinct.

**Shared ground.** Both reject the sense-think-act pipeline. Both reject the pregiven-world, representation-recovery picture of cognition. Both put perception-and-action on the same ontological footing (the Cisek-Kalaska "decisions within sensorimotor circuits" claim and the VT&R "perceptually guided action" claim are structurally parallel). Both take the organism's action-repertoire as co-specifying what counts as a feature of the environment.

**The contrast.** Affordance competition (Cisek, Clark, Friston) works within a **probabilistic representational framework** — there are representations, they are pragmatic rather than descriptive, and they compete via precision-weighted predictions. The representations are real; what's denied is that they are action-neutral world-encodings. Enaction (VT&R) goes further: operational closure plus structural coupling means that "representation" is the wrong concept to begin with, not just a concept that needs to be made pragmatic. See [[enaction]] §2751–2760 for the operational-closure register that doesn't need representations at all — the system's operation **is** its relation to the world, not a representation of it.

**One way to hold both.** Affordance competition is a useful computational / neural mechanism-specification *within* an enactive frame. The enactive frame gives the ontological claim (cognition is embodied action, not representation-of-a-pregiven-world); affordance competition gives a concrete proposal for how this might be implemented at the level of neural dynamics. They are compatible at the level of the specific empirical claim (parallel affordance-specification, pragmatic representations); the question of whether affordance competition's probabilistic-representational vocabulary is ultimately **enactive-friendly or enactive-unfriendly** is a live question. Clark takes it to be enactive-friendly (see [[extended-mind]]); VT&R (Ch 10 §4008) would press that the representational vocabulary, even in its pragmatic form, invites reification if not held with Madhyamaka discipline.

For the persona-project this matters because the wiki has been drawing on both frames as compatible resources. That compatibility holds at the operational level (reject sense-think-act; pragmatic representations; trajectory-adequacy over stable-state) but should not be flattened at the ontological level (the enactive challenge to representation as a concept remains, and affordance-competition's probabilistic-representations-with-pragmatic-role is not quite what enaction proposes).
