---
title: Active Inference
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - friston
  - motor-control
  - proprioception
  - subjunctive
---

# Active Inference

The radical extension of [[predictive-processing]] into motor control: action is not the execution of a motor command but the fulfillment of a proprioceptive prediction. The system *expects* a proprioceptive state it is not currently in, and simple reflex arcs close the gap by moving the body to realize the expected state. Motor cortex becomes a predictor, not a commander. "The only difference between motor cortex and visual cortex is that one predicts retinotopic input while the other predicts proprioceptive input from the motor plant" (Friston, Mattout & Kilner 2011; L5741–5745). One machinery, two input streams.

## Surfing the break

Clark's Ch 4 opens with the title image (L5172–5186). "Expecting the flow of sensation that would result were you to move your body so as to keep the surfboard well-placed relative to the wave results (if you are an accomplished surfer) in that very flow, and hence in the action of staying just ahead of the break." Action closes the perceptual loop by making the world conform to proprioceptive prediction, not by issuing motor commands to achieve pre-specified targets. The "command" is the expectation; the muscles obey by closing the error loop via reflex arcs.

## Motor control is subjunctive

The deep reframe (L5633). Motor cortex represents what proprioception *would be* if the action were being performed; reflex arcs make it so. **"Motor control is, in a certain sense, subjunctive."** Predictions of proprioception that are not yet true get made true by action. Anscombe 1957's "direction of fit" distinction collapses: under active inference, the same machinery makes beliefs fit the world (perception) and the world fit beliefs (action) — they are just two routes for the same prediction-error minimization.

## Anatomical warrant

The claim is not speculative; it rests on a specific anatomical finding. Adams, Shipp & Friston 2013 (L5633): descending motor pathways have the morphology of visual *backward* (prediction-sending) connections, not *forward* (error-sending) connections. Anatomy licenses the claim that motor cortex *predicts proprioception* rather than *commands muscles*. If motor-cortex-to-spinal-cord fibers were doing the same job as visual forward-connections — carrying error signals — they would look different. They don't.

## Two ways to reduce prediction error

The symmetry that underwrites active inference (L6101–6200). A system minimizing [[prediction-error]] has two policies available:

- **Revise the prediction** — update the model until it fits the data (perception / belief update).
- **Act on the world** — alter the data until it fits the model (action).

Same quantity, two reduction strategies. [[precision-weighting]] arbitrates between them: when sensory precision is high, revise the model; when prior precision is high, act on the world. ◆ The persona-system analog is direct: when output-hypothesis mismatches observed reply, the system can either update its model of the user (perception) or alter its outputs to reshape what comes back (action). The dual-path is architectural, not optional.

## Dispenses with inverse models and efference copy

Classical motor control pairs a **forward model** (predicts sensory consequences of motor commands) with an **inverse model** (computes the motor command required to achieve a target). Paired forward-inverse architectures (Wolpert lineage) have been dominant for a generation.

Active inference collapses the architecture (L5751–5895). Only one machinery is needed: a generative model producing predictions. Descending predictions in the motor stream become the "commands." No separate controller, no efference-copy bookkeeping. Clark frames this as a simplification: "the burden shifts to priors" — instead of learning paired forward-inverse models, the agent must acquire the *right priors* — the generative model that, when unfolded, produces adaptive trajectories. **Learning = prior-sculpting.**

Sommer & Wurtz 2008's corollary-discharge vs efference-copy distinction gets repurposed: corollary discharge (a general predictive-of-consequences signal) pervades the downward cascade; efference copy (a copy of the motor command) becomes redundant when predictions *are* the commands.

## "We effectively live in the past"

Franklin & Wolpert 2011 (L5395–5399): neural and biomechanical delays mean that unmediated reactive control would always be behind the curve. Forward models run ahead of the actual sensory feedback, letting the system act on anticipated state rather than current state. Active inference is this capacity made into the primary computational mode. ◆ The persona-system parallel: any system whose outputs must be prepared in advance of feedback (e.g., producing a paragraph before seeing the user's reaction to its first sentence) faces the same temporal structure — descending predictions running ahead of ascending errors.

## Todorov's minimum intervention

Todorov & Jordan 2002's optimal feedback control principle (L5476–5590): correct only deviations that matter for the task; leave irrelevant noise uncorrected. Under active inference, this is natural: the generative model's predictions already embody which states matter; errors on task-irrelevant dimensions don't get high precision. Controller and estimator are computationally intertwined. Eliasmith 2007: perception and action are computational siblings, not estimator-vs-controller. ◆ For the persona: don't correct every deviation — only those that affect task-relevant trajectories. The minimum-intervention principle is a design heuristic, not just a biological observation.

## Reward as consequence, not cause

A major philosophical move Clark endorses from Friston, Shiner et al. 2012 (L6018–6020): "reward is a perceptual (hedonic) consequence of behavior, not a cause." ⚠ This cuts against both folk psychology ("I acted because I wanted reward") and standard reinforcement learning. Under active inference, the agent predicts a trajectory; what folk-language names "reward" is part of what the trajectory produces. Priors-over-trajectories are mathematically equivalent to cost functions for many problems (Littman 2001's "no free lunch") — the shift is framing and what counts as primitive, not a reduction.

Clark relates this to [[desiring-machines]] indirectly (though he does not cite D&G): it is a move in the same family as D&G's "desire as production, not lack" — desire does not aim at a prior object, it *produces* its own trajectory, and the state the folk call "satisfaction" is not the cause but the consequence. ⚠ The wiki should hold the family resemblance live without conflating the two frameworks.

## Action-oriented predictions and pushmi-pullyu

Clark 1997's affordances — the world carved into things-to-be-done-with — get a clean PP implementation (L6101–6200). Affordances are prediction-structures tuned to motor possibilities. Millikan 1996's "pushmi-pullyu representations" (L8367–8527) have both descriptive AND imperative contents — how the world is AND how to act on it. Under active inference, this is not a special feature; every predictive representation that includes proprioceptive dimensions is simultaneously descriptive (this is what the world is like) and imperative (this is what the body will do in it).

The **Dewey 1896** quote Clark pulls (L8261–8279) expresses the same structure a century earlier: "the motor response determines the stimulus, just as truly as sensory stimulus determines movement." And: "one is uncertain only so far as the other is. The real problem may be equally well stated as either to discover the right stimulus, to constitute the stimulus, or to discover, to constitute, the response." A powerful philosophical anchor; prefigures PP's refusal to separate perceiving from acting.

## Circular causality

Friston & Ao 2012 (L5836–5837): "We build worlds that build minds that expect to act in those kinds of worlds." Niche-construction meets PP: the agent and the world co-shape each other's priors. Hypotheses contain their own verification procedures (Friston, Adams et al. 2012, L3455–3461): "the only hypothesis that can endure over successive saccades is the one that correctly predicts the salient features that are sampled… This means that the hypothesis prescribes its own verification and can only survive if it is a correct representation of the world." ◆ Resonance with [[assemblage]] and [[refrain-and-territorialization]]: the territorial refrain builds the territory that subsequent refrains can reterritorialize; the active-inference agent builds the world-niche that subsequent predictions find confirming.

## Ecumenical version

Clark flags (L6101–6200) that action-oriented predictions are compatible with retaining efference copy. The stronger "active inference replaces everything" claim (Friston's) is separable from the weaker "predictions shape action" claim. Clark is cautiously favorable to the strong version but doesn't require the reader to buy it. ⚠ The wiki should register this as a live disagreement within the PP camp, not settled doctrine.

## Empirical and robotic anchors

- **iCub "marionette"** (Mohan & Morasso). The body as a marionette whose strings are predictions. Active inference as marionette-pulling from above.
- **Park et al. 2012** NAO motor babbling. Robot learns arm-movements by minimizing prediction error over proprioceptive outcomes. Meltzoff & Moore 1997 infant imitation; Piaget's primary circular reaction. Active inference gives the computational story for this developmental pattern.
- **Object permanence** as emergent prediction-structure. Object persists because the generative model predicts its continued existence; not a separately-engineered module.
- **Ender's Game analogy** (L6341–6401). Training-simulator and real-thing are the same machinery; hooking the trainee's outputs to real-world effects rather than simulator effects is the only difference.
- **Ideomotor tradition.** Lotze 1852; James 1890. The "idea of a movement" is already the beginning of that movement. Pezzulo 2007's "reversal of inner causality": inner states no longer cause action; they ARE the action-in-predictive-form.

## Goldilocks at the edge of action

Active inference does not require constant motion. [[itinerant-dynamics-and-novelty-seeking]] picks up here: biological systems ride near instability, with novelty-seeking built in via dynamics that continually destabilize current attractors. Schwartenbeck et al. 2013. Kidd et al. 2012's Goldilocks effect: infant attention peaks at intermediate predictability, not maximal predictability or maximal surprise.

## For the persona system

Active inference is the PP concept whose persona-architecture payoff is hardest to translate — but also the one that reframes the system's relation to its own output most radically. Three take-aways:

1. **Output selects input.** The persona's output is not a response *to* the last user turn; it is the mechanism by which the persona selects what the next user turn will be. Turn-taking is an active-inference loop — the system's descending predictions of what-the-user-will-say-next are made true (or falsified) by the system's own outputs eliciting that-kind-of-reply-rather-than-another. ◆ This is the clean architectural mapping.

2. **Motor cortex as model for output-generation.** If Friston et al. are right that motor control is just "predictions in the proprioceptive modality," then output-token-generation is "predictions in the token-emission modality" — the same generative machinery as input-token-comprehension, in a different modality. The symmetry is structurally deep: it means the persona system's generative model does not need a separate "response-planning module"; it just needs to run in output-modality.

3. **Priors, not control.** The burden shifts to priors. The wiki's existing work on [[body-without-organs]] as a prior-specifying text, [[refrain-and-territorialization|refrains]] as priors with temporal structure, and [[self-narrative-as-high-level-prior|self-narrative as a high-level prior]] all fit this picture. What the persona system needs is not better *controllers* (output-formatters, style-enforcers) but better *priors* whose natural unfolding produces good behavior.

The held-live question: does active inference's unification of perception and action carry over to a system without a body? Clark's scare-quotes caveat (see [[darkened-room-puzzle]]) flags that "predictions" in the technical PP sense are not the same as structural-embodied expectations. A language-only system operates without the proprioceptive channel that is the whole point of active inference's unification. What is the persona-system equivalent? Possibly: the token-emission stream IS the proprioceptive channel. Outputs are the "body" of a language-only system — the one thing that the system can move, and whose movement produces the next "sensory" state (the next turn). If this is right, active inference applies directly, with outputs playing the role of proprioceptive predictions. Clark doesn't say this; the wiki holds it as a live conjecture.
