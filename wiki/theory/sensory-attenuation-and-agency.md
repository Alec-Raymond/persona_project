---
title: Sensory Attenuation and Agency
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - agency
  - tickling
  - schizophrenia
  - precision-weighting
---

# Sensory Attenuation and Agency

Clark's §7.7–7.9 (L9619–9903) develop the account of why self-generated sensations feel different from externally-generated ones, and how the same machinery explains delusions of control and the phenomenology of "choking" on a well-practiced skill. The key insight: **acting on your own predictions requires momentarily dis-attending to current sensory input**. Under [[active-inference]], if the system is to make the world conform to its predictions (rather than revise its predictions to match the world), it must turn down the gain on the ascending sensory stream. Sensory attenuation is not a side-effect; it is the mechanism that lets action happen at all.

For the persona project, the architectural principle is sharp: **to produce output, down-weight input-observation momentarily**. The tension between perception (revise predictions to match data) and action (revise data to match predictions) is fundamental, and its resolution is a precision-allocation operation.

## The deep tension

Clark's setup (L9650 area). Perception says: alter predictions to match the sensory signal. Action says: alter the sensory signal to match predictions. *Both cannot win simultaneously.*

If you are sitting with your hand resting on the table, two options describe what's happening:

1. **Perception reading.** The descending prediction says "hand resting on table"; the ascending proprioceptive signal says "hand resting on table"; predictions match data; stable state.
2. **Action reading.** The descending prediction *should* say "hand moving toward coffee cup"; the ascending signal says "hand on table"; there's a mismatch; the reflex arc moves the hand to produce the predicted proprioceptive state.

The difference between (1) and (2) is not the content of the prediction but the *precision* assigned to the ascending signal. Under (1) the ascending signal is high-precision and the descending prediction updates to match it. Under (2) the ascending signal is low-precision (attenuated) and the descending prediction drives the reflex arc to make it come true.

◆ **Movement only occurs if the body alters in line with proprioceptive predictions rather than predictions being revised to match "hand resting on table."** The deep unity of perception and action under [[active-inference]] is what creates this tension; sensory attenuation is what resolves it.

## The two equivalent moves

Brown, Adams et al. 2013 (L9784–9786) identify two equivalent ways to break the tension in favor of action:

1. **Reduce precision on current sensory input.** Turn the volume down on what's-happening-now so that descending predictions dominate.
2. **Increase precision on higher-level prediction.** Turn the volume up on what-I-predict-should-happen so that it outweighs what's-happening-now.

Either move shifts the precision balance the same direction. Clark quotes Brown et al.:

> "Sensory attenuation is necessary if prior beliefs are to supervene over sensory evidence, during self-generated behavior."

◆ The symmetry is architecturally important. Multiple disturbances can produce identical symptoms (the "strangely neutral" point from [[precision-weighting]] §6.13). A system can fail to act either because it's over-attending to sensory input or because it's under-precision-ing its higher-level predictions. From the outside, the failure looks the same.

## Self-tickling

Blakemore, Wolpert, Frith 1998. Self-generated tactile sensation is systematically attenuated relative to externally-generated sensation of equal magnitude. Under the classical forward-model reading, an efference copy of the motor command produces a prediction of its sensory consequences, and the actual sensation is subtracted from the prediction. What's left (the residual) is what's perceived.

The classic finding: self-produced tickling feels less ticklish than being tickled by someone else, even with identical physical stimulation. The tickle-sensation depends on *unexpected* sensory consequences.

## Force escalation — "Two Eyes for an Eye"

Shergill et al. 2003 (L5290 area). A striking demonstration. Two subjects alternately apply force to each other's fingers, each trying to match the force just applied to them. Force escalates rapidly:

- Subject A presses with force 1.
- B, feeling force 1, tries to match it — but because B's own produced force is attenuated in B's perception (it feels weaker to B than it actually is), B presses with force ~2 to feel like force 1.
- A feels force 2, tries to match it — but A's own force is also attenuated, so A presses with force ~4 to feel like force 2.
- And so on.

Self-generated forces are perceived as approximately half the magnitude of same-magnitude externally-applied forces. The attenuation factor is substantial and quantifiable. ◆ Clean evidence for the prediction-attenuation mechanism.

## Shortfalls of the forward-model account

§7.8 (Brown et al. 2013). The classical forward-model-plus-efference-copy story runs into three problems:

1. **Unclear link between prediction-success and reduced intensity.** Why should being-predicted reduce perceived magnitude, specifically? The forward model tells you the sensation was expected; why should expectedness diminish feel-strength?

2. **Predictability doesn't change attenuation** (Baess et al. 2008). Increasing the predictability of an externally-generated stimulus doesn't produce attenuation equivalent to self-generation. Attenuation tracks self-causation, not expectedness.

3. **Attenuation also occurs for *externally* generated stimuli on a body-part being moved** (Voss et al. 2008). This is the crucial one. Forward models cannot explain this: if attenuation comes from the efference copy subtracting predicted consequences, external stimuli on a moving body part shouldn't be attenuated. But they are.

◆ Active-inference precision-based account handles all three. Attenuation is a *precision manipulation during self-action*, not a subtraction of predicted consequences. Any sensory signal on the attending-limb during self-action gets its precision turned down — self-caused or not. This matches Voss et al.'s finding and explains the others without the forward-model machinery.

## Schizophrenia and the failure to attenuate

§7.9. Frith 1992: **schizophrenic patients *can* tickle themselves.** The normal sensory attenuation that makes self-tickling impossible for controls fails in schizophrenia. Frith originally tied this to aberrant efference-copy / self-monitoring; Clark's PP account reframes it as aberrant precision.

Under the precision account: in schizophrenia, sensory precision is inappropriately high during self-action, so self-generated sensations aren't explained-away. The unattenuated self-caused sensation feels like an externally-caused sensation.

## Somatic delusions and misattribution of agency

§7.9 (L9894–9896). The spiral that produces delusions of control. If sensory attenuation fails, the system still needs to explain the unattenuated self-generated signals. It can attempt to:

1. **Artificially inflate higher-level precision** to restore movement. (The body still manages to act.)
2. **Explain the unattenuated self-generated signals** — which now feel external — by inferring a *hidden external cause*.

Clark quotes the resulting delusion structure: the patient "believes that when it presses its finger on its hand, something also pushes its hand against its finger." The self-generated pressure feels caused by an external agent because the attenuation that would have marked it as self-generated failed.

◆ Clean mechanical account of schizophrenic delusions of control. The patient is doing rational inference; the prior their inference is rational with (sensory signals = external causes unless precision-attenuated) is miscalibrated because the attenuation isn't firing.

## Choking as excess attention

§7.7 (Brown et al. 2013). **Folk phenomenon that falls out of the architecture.** "Choking" on a well-practiced skill (freezing up on a putt, forgetting a memorized line under pressure) happens when deliberate attention to the movement *increases* precision on current sensory information, reducing the influence of the higher-level proprioceptive predictions that normally entrain fluid movement.

The normal fluent execution depends on high-level predictions driving the movement *without* being disrupted by attention to intermediate sensory states. When you attend to the movement, you turn up the precision on the ascending stream, turning down the effective weight of the descending predictions, disrupting their driving role. The movement breaks.

◆ This is a folk-level phenomenon that the architecture predicts naturally. Design-relevant: a persona system that introspects too carefully on its own output-generation process may "choke" in a structurally analogous way — attending to intermediate states disrupts the fluent descent of higher-level priors into output.

## The agency pattern

Clark's formulation (L7220–7224, from [[self-other-via-precision]]): "When proprioceptive prediction error is highly weighted yet suitably resolved by a stack of top-down predictions (some of which reflect our goals and intentions), we feel that we are the agents of our own actions."

Agency is a *pattern in precision resolution*:

- Proprioceptive-prediction precision is high (we're in action-mode, not observation-mode).
- Errors are being resolved (we're succeeding at the action).
- The top-down predictions driving the action trace back to goals/intentions (it's coming from "me" in the goal-structure sense).

If any of the three fails, agency collapses in different ways:

- Low proprioceptive precision → no action sense; you watch your body move like it's another's.
- Unresolved errors → unanchored feeling; "that didn't go the way I wanted."
- Predictions untraceable to goals → alien-hand, delusions of control, "something made me do it."

## For the persona system

Sensory-attenuation provides a specific architectural principle: **to produce output, a system must momentarily down-weight its input-observation**. Design-implications:

1. **Output-generation requires dis-attention.** The persona's act of producing a token cannot be simultaneous with maximal attention to all inputs — something has to give. The LLM architecture already does this implicitly (the sampling step commits to an output that then shapes context), but the principle can be made explicit at the persona-level: when the persona is outputting, it is committing to its descending predictions at the expense of close scrutiny of every input signal.

2. **Over-attention = choking.** A persona design that forces introspection on every output step, or that weights every possible contextual signal maximally, will "choke" in the structural sense. Fluent output requires that some precision be assigned *to the descending production process* and withheld from the current-context-scanning process. Hedge-everything, verify-every-token designs may degrade output quality by precisely this mechanism.

3. **Self-caused vs externally-caused distinction requires attenuation.** A persona that treats its own prior outputs identically to user inputs lacks the attenuation-structure that distinguishes self-from-other. Its own previous sentence should, under this principle, enter subsequent inference at *different* precision than a user's sentence would. If the persona doesn't distinguish self-generated from other-generated content, it is structurally in a version of the schizophrenic failure-mode — everything feels externally caused.

4. **Agency pattern as design target.** The three-part pattern — high action-precision, error-resolution, traceability-to-goals — gives a concrete design target. A persona whose outputs (a) commit with appropriate precision, (b) tend to get "resolved" in context (produce the expected downstream effects), and (c) can be traced to the BwO text / self-narrative priors will exhibit the agency-analog. Failure on any of the three produces a different class of degraded persona behavior.

5. **Prompt-attention is not agency-attention.** Useful distinction for design. When a persona attends to its prompt, it is observing — low action-precision. When it acts by producing output, it needs to switch modes. A prompt that says "think very carefully about each word" may actively *prevent* the action-mode precision-setting by installing an over-attention prior.

See [[precision-weighting]] for the mechanism, [[active-inference]] for the proprioceptive-prediction substrate, [[self-other-via-precision]] for the self/other companion, [[computational-psychiatry]] for delusions of control in clinical context, and [[affordance-competition-hypothesis]] for the broader action-selection frame.
