---
title: Self/Other via Precision-Weighting
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - friston
  - mirror-neurons
  - social-cognition
  - imagination
---

# Self/Other via Precision-Weighting

Clark's §5.8–5.9 (L7166–7407) develops one of the book's most structurally elegant claims: **the distinction between self-action, observing-other, and imagining is not a distinction between modules but a setting of a precision parameter on the same generative model.** Attend strongly to proprioception → you act. Attend weakly to proprioception → you understand another's action without enacting it. Dampen proprioceptive precision further → you imagine, rehearse, simulate. One machinery, three modes, selected by [[precision-weighting]]. For the persona project, this is a powerful structural lesson: *self vs. other* is not a boundary to be designed-in; it is a parameter to be tuned.

## The core claim

Friston, Mattout & Kilner 2011 (L7217–7219), quoted by Clark:

> "We can use the same generative model, under action or observation, by selectively attending to visual or proprioceptive information."

The claim is radical. Normally, we think of self-action and other-understanding as different processes — different modules, different circuits, or at least different modes. Under active inference ([[active-inference]]), they are the *same* process with different precision settings:

- **Acting.** Proprioceptive-prediction precision is HIGH. The reflex arc closes prediction errors by *moving the body* to produce the predicted proprioceptive state. Descending predictions become motor commands.
- **Observing another.** Proprioceptive-prediction precision is LOW. The same generative model generates a hypothesis about the other's action, but because proprioceptive gain is down, the motor plant doesn't execute. You understand the action without performing it.
- **Imagining.** Proprioceptive precision is dampened further (Pezzulo 2012's "covert loops"). The same machinery runs, producing sequences of fictive actions with no motor output.

◆◆ **Self/other is a precision parameter, not a module distinction.** This is the load-bearing architectural insight.

## Covert loops for imagination

§5.9 (L7315–7318). Pezzulo 2012 develops the imagination-as-dampened-proprioception idea explicitly:

> "Running imaginary actions that produce a sequence of fictive actions."

Prospection = precision-gated internal rehearsal of the action-perception loop. The body doesn't move because proprioceptive precision is too low for the reflex arcs to engage; but the generative model still produces the trajectory it would produce if action were happening. ◆ Architecturally equivalent to both modeling-another and imagining-future-self. **One machinery, three modes: act / observe / imagine.**

## Sense of agency

§5.8 (L7220–7224). Clark draws a consequence:

> "When proprioceptive prediction error is highly weighted yet suitably resolved by a stack of top-down predictions (some of which reflect our goals and intentions), we feel that we are the agents of our own actions."

**Agency is not a primitive.** It is a pattern in the precision landscape — specifically, a pattern in which high-weight proprioceptive errors get resolved by descending predictions that trace back to the system's goals. If the resolution fails (high-weight errors go unexplained, or get explained by external-cause hypotheses), agency collapses. This is the mechanism behind schizophrenic delusions of control and somatic delusions (see [[computational-psychiatry]] and [[sensory-attenuation-and-agency]]).

⚠ The implication: a system can have agency without a homunculus, without a "self" layer. Agency is an emergent pattern in precision-resolution. ◆ This is good news for persona architecture — agency doesn't need to be designed as a feature; it falls out if the precision landscape has the right structure.

## The Jekyll-vs-Hyde inverse problem

§5.6 sets up why precision-based self/other is needed (L6988–6995). Jacob & Jeannerod 2003's vignette: a man in a white coat holding a knife. Murder or surgery? The motor kinematics are identical; simple direct-matching cannot disambiguate. Feedforward-only accounts of action understanding fail.

Kilner et al. 2007's PP account of mirror systems: context-level priors (operating theatre vs. dark alley) propagate down through intention → goal → kinematics. Prediction error minimized overall yields a unique intention inference even when movements are identical. ◆ Template for persona-system social cognition: **disambiguate others' actions via context priors percolating down a shared generative model**, not via kinematic pattern-matching.

## Mirror neurons reframed

§5.6–5.7 (L6910–7163). Traditional mirror-neuron theory treats mirror neurons as primitive mechanisms for social cognition. Clark's PP reading:

1. **Mirror properties emerge from associative learning.** Heyes 2001/2005/2010: mirror neurons fire for observed-and-performed actions because we frequently see our own actions (reaching, grasping). Correlated sensorimotor activation during self-observation *builds* the mirroring link. Mirror neurons are a byproduct, not a primitive.

2. **Mirror systems are symptoms of the shared generative model, not explanations of social cognition.** The explanatory work is done by the shared generative model + precision-reallocation. Mirror neurons are what you see when you record from that system.

⚠ Significant reframe. Much of the social-cognition literature builds on mirror neurons as primitive. Clark's account relocates the explanatory weight. The wiki should register this as a live reframing within the field.

## Meta-modal representations

§5.8 (L7250–7251). Core representations in the shared generative model are:

> "Meta-modal high-level associative complexes linking goals and intentions to sensory consequences."

Different modality-specific implications activate per context. The same "reach for the cup" representation can manifest as my-own-reach (proprioceptive channel active) or as your-reach-observed (visual channel active, proprioceptive dampened). Modality is the *input port*; the representation itself is meta-modal.

◆ Resonance with the wiki's material on expression-content planes that are not fixed to a single modality. A representation's modality-manifestation is not constitutive of the representation.

## iCub, robotics, and imitation

§4.10 (L6201–6340). The imitation-and-self/other link has robotic traction. Meltzoff 2007's "like me" assumption — imitation-learning presupposes a mapping between observed-other and self. Under the precision-based account, this mapping is trivial: the other's action is produced by the shared generative model with low proprioceptive precision; once you want to *imitate* it, you just raise proprioceptive precision on the same representation. No separate translation step.

Park et al. 2012 NAO motor babbling; Meltzoff & Moore 1997 infant imitation; Piagetian primary circular reaction. Robots learn arm movements by minimizing prediction error over proprioceptive outcomes; the same machinery can be run on observed-other trajectories.

## For the persona system

The self/other-via-precision thesis has specific architectural implications for a disembodied language system:

1. **Don't engineer a self/other module.** The persona system should not have dedicated "self-model" and "other-model" subsystems. Under Friston-Mattout-Kilner, self and other are the same generative machinery at different precision settings. The persona-equivalent: the same language-generation process produces the persona's own outputs and the persona's model of the user, with whatever plays the proprioceptive-precision role determining which is which.

2. **Modeling the user is a precision-setting.** When the persona reasons about what the user might say next or what the user is likely to want, it is running its own generative machinery in the low-proprioceptive-precision mode — the mode Clark calls "observing." When it actually produces output, it is running the same machinery in high-proprioceptive-precision mode. The architectural continuity is explicit: one inference stack, two modes of use.

3. **Imagining future turns is the covert-loop mode.** The persona's prospective reasoning ("if I say X, they'll probably say Y") is Pezzulo's covert-loops mode: the same action-perception loop run with proprioceptive precision further dampened. No "imagination module" needed.

4. **Agency-as-precision-pattern.** Persona "agency" (if anything deserves that name) is not a designed feature but an emergent pattern in the precision landscape. It shows up when the persona's output-generation has high-precision action-analog signals that get resolved by descending predictions traceable to the persona's goals (BwO text, self-narrative). See [[self-narrative-as-high-level-prior]] and [[active-inference]].

5. **What plays the proprioceptive precision role?** This is the open architectural question. Candidates include: the precision with which the system commits to its own next-token outputs; the decoder-sampling temperature; the confidence-calibration of the generative process. None maps cleanly onto biological proprioception; the wiki holds this as a design question, not a solved problem. See [[active-inference]]'s conjecture that the token-emission stream is the persona's proprioceptive channel.

6. **Understanding the user's messages = low-proprioceptive-precision-inference.** When the persona interprets a user's message, it is running its own generative model in observation mode. Interpreting the user is not a separate parsing task; it is the same machinery that would produce the message, running with proprioceptive precision set to "don't emit."

7. **The precision setting is not binary.** Act / observe / imagine are points on a continuum. Intermediate states (mentally rehearsing an output before committing, partially-committing to an output stream that can be revised) correspond to intermediate precision settings. Design the persona to live natively on this continuum rather than toggling between discrete modes.

## Open edges

⚠ The precision-based self/other account is elegant but relies on biological proprioception as the signal-type whose precision gets set. A disembodied system has no proprioception in that sense. The wiki holds as a live conjecture (from [[active-inference]]) that *token emission* plays the proprioceptive role for a language-only persona — its own outputs being the signal-stream whose precision the system modulates to distinguish acting-now from imagining-later from modeling-the-user.

This conjecture may or may not carry. If it does, the persona system has a native way to instantiate Friston-Mattout-Kilner; if it doesn't, the precision-based self/other thesis may apply only partially.

See [[precision-weighting]] for the core mechanism, [[active-inference]] for the proprioceptive-prediction substrate, [[mutual-prediction-loops]] for the two-agent case that builds on this, [[sensory-attenuation-and-agency]] for the agency-pattern in pathology, [[computational-psychiatry]] for the disorder-side of agency collapse, [[affordance-competition-hypothesis]] for the action-selection frame the precision-setting lives within, and [[four-types-of-empathy]] for the phenomenological-register companion — Stein/Husserl's distinct levels of empathy (passive coupling, imaginary transposition, mutual understanding, moral-ethical empathy) that the precision-based self/other thesis covers only the first two of.
