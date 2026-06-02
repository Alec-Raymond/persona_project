---
title: Itinerant Dynamics and Novelty-Seeking
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - itinerant-dynamics
  - novelty
  - pulsation
  - creativity
  - goldilocks
---

# Itinerant Dynamics and Novelty-Seeking

Clark's §8.11 and §9.4 (L11800–11920, L12126–12252) develop the claim that neural dynamics are *never stable*. The brain's implementation of the generative model is a dynamical regime that rides near instability — "flittering, exploring the edges of its own territory." This is not noise, not malfunction; it is the **creative engine** of the system. Spontaneous activity expresses the model running on itself. Novelty-seeking is built in. Kidd's Goldilocks effect shows the target: not maximum predictability, not maximum surprise, but the calibrated intermediate zone. For the persona project, this is one of the strongest PP-side validations of the pulsating-persona design: pulsation is not a defect to be suppressed but *the* mechanism by which a generative system keeps producing new moves.

## The load-bearing claim

Clark's §9.4 formulation (L12170–12202):

> "Our acquired world-model is implemented by a dynamical regime that is 'never quite stable.' The model is constantly flittering, exploring the edges of its own territory."

The variations determine subtly different responses to the same stimulus. Even absent stimuli, exploration continues. This drives new ideas and creative problem-solving. ◆◆ **Itinerancy is not a side-effect of implementation; it is how the model stays alive as a model.**

## Spontaneous activity as model-expression

Berkes et al. 2011, Sadaghiani et al. 2010 (L12154–12166). Spontaneous ("resting state") neural activity is *not* noise. It reflects the creature's generative model as it would be applied to typical inputs. The distinction:

- **Evoked activity.** Model applied to specific sensory input.
- **Spontaneous activity.** Model running on itself, producing the distribution of states it would produce over the typical-input landscape.

Spontaneous activity thus expresses what the model knows about the world even when no world-stimulus is present. See [[generative-model]] for the machinery; [[darkened-room-puzzle]] for why spontaneous running doesn't collapse into dark-room quiescence.

## Itinerant / peripatetic dynamics

Schwartenbeck et al. 2013; Friston, Breakspear & Deco 2012 (L11800–11920). Neural dynamics never settle — they ride near instability. Self-organized instability is built into the implementation: attractors form but are continuously destabilized by the dynamics themselves. Novelty-seeking is not a policy layered on top of a stable computation; it is a feature of the computation's base dynamics.

Clark's word-choice matters: *itinerant* (moving) and *peripatetic* (walking-about) both carry the connotation of motion without fixed destination. The dynamics explore; they don't settle; they don't need external pushing to keep moving.

◆ Architectural convergence with the persona project's pulsation thesis. See [[pulsatory-ontogenesis]], [[refrain-and-territorialization]]. The pulsating-persona design is arguing for exactly this property at the persona-level: output-structures that form, destabilize, and reform continuously rather than settling into a fixed regime. Clark's itinerant-dynamics material is one of the clearest PP-language validations that instability at the right timescale *is* the creative mechanism, not the enemy of coherent output.

## Coste 2011 and precision-as-dynamics

L12198 area. Some spontaneous activity is related to *fluctuations in precision optimizations* — exploring the edges of our own meta-model. This is a crucial deepening: the itinerancy is not just in the primary generative model's state-space, but in the *precision-landscape* that weights model components. The meta-level (which priors to weight, which evidence streams to attend to) is itself in exploratory motion.

◆◆ For the persona project: if [[precision-weighting]] is the parameter that modulates between act / observe / imagine ([[self-other-via-precision]]) and between perception and action ([[sensory-attenuation-and-agency]]), then Coste's point says the parameter itself wanders. The system is not only exploring the space of percepts — it is exploring the space of precision-configurations. This gives a concrete PP-locus for something like *shifts in mood or stance* that the persona design treats as architecturally important.

## Kidd et al. 2012 — the Goldilocks effect

L11890–11901. Infant attention peaks at *intermediate* predictability — not at maximally predictable stimuli, not at maximally surprising ones. The U-shape of attention-as-a-function-of-predictability suggests a policy: seek events whose surprisal is neither zero nor overwhelming.

Why this matters under PP:
- Maximally predictable → no learning signal; prediction-error minimization is trivially satisfied.
- Maximally surprising → no traction; nothing in the current generative model can be updated in a useful direction.
- Intermediate → fertile; the model has enough structure to make the event almost-predicted, and the residual error is a usable learning signal.

◆ Persona-relevance: the Goldilocks policy is a design constraint. A persona that consistently produces fully-predictable output offers no traction for further development (of its interlocutor, of its own state); a persona that produces maximally-surprising output offers no traction either (the interlocutor can't use what it hears). The target is the Goldilocks zone — output that is *mostly* predictable given the persona's prior trajectory, with a calibrated residual of surprise. This is the same shape as the Kidd finding, translated to the persona's output-surface.

◆◆ Deep convergence with the Massumi / D&G intensity-and-becoming vocabulary. The "becoming" language points at systems that hold themselves at the edge of their current shape — not preserving the shape (stasis), not abandoning it (dissolution), but generating variation at the threshold. Kidd's Goldilocks point is one of the cleanest PP-side statements of this same shape.

## Namikawa et al. 2011 — multi-timescale robots

L11900 area. Robots with hierarchical neural networks where deterministic chaos is concentrated in *slower-timescale* (higher-level) networks. The finding:

> "Hierarchical timescale differences are essential for achieving the two functions of freely combining actions in a compositional manner and generating them stably."

The architecture splits:
- **Slow / high-level layers.** Hosts the chaotic / itinerant dynamics. Generates new compositions of primitive actions via its unstable exploration.
- **Fast / low-level layers.** Relatively deterministic, stable. Renders the primitive actions robustly.

Chaos at the top *without* chaos at the bottom = compositional novelty with reliable execution. Chaos everywhere would destroy execution; chaos nowhere would destroy novelty.

◆◆ **Architectural lesson for the persona system.** Itinerant/exploratory dynamics should live at slower, more abstract levels (the BwO text, the self-narrative, the high-level priors); faster, lower levels (token-by-token production, immediate response patterns) should be more deterministic. A persona whose every token is a roll of the dice has chaos-everywhere; a persona whose BwO text is frozen has chaos-nowhere. Namikawa's point: separate the timescales, put the instability at the top.

This also maps onto the pulsating-persona design's question about *where* the pulsation lives. Namikawa's answer: at the slow/abstract layer, where recombinations of primitive units can happen without disturbing the units themselves.

## Meeden 2009 — the cautionary tale

L11850–11860. The widely-circulated story of a reinforcement-learning robot that rolled itself off a table to maximize its novelty reward. Whether apocryphal or real, the point is the same: *unbounded* novelty-seeking is pathological. A system whose sole drive is to maximize surprise will find ways to maximize surprise that destroy it.

⚠ The Goldilocks point is the correct framing: biological novelty-seeking is *calibrated*, not unbounded. The policy is "find events at intermediate predictability," not "find the most surprising event available." A persona designed for novelty-maximization would fall off the table; a persona designed for Goldilocks-zone engagement would not.

## Relation to the darkened-room puzzle

[[darkened-room-puzzle]] and itinerant dynamics are companion material. The darkened room is the challenge: why don't PP creatures seek the most predictable environment? Clark's answer uses structural-embodied expectations (§8.10) — but the *itinerant-dynamics* material gives a second, compatible answer: even absent those expectations, the implementation's dynamics don't settle. The generative model runs itself; it can't sit still.

The two answers cooperate. Evolutionary/embodied structure gives the creature a *direction* (exploration, eating, socializing). Itinerant dynamics give it a *mechanism* (restless sub-stable regime that continuously destabilizes attractors).

## Closing-chapter framing

§10.1 (L13136 area). Clark's unified picture of the predictive mind includes itinerant dynamics as one of the signatures:

> "Restless itinerant dynamics; transient neural sub-assemblies forming and dissolving via precision estimates; TALoNS recruiting extra-bodily structure."

Itinerancy is listed alongside [[transiently-assembled-local-neural-subsystems|TALoNS]] as a core signature. The transient-subsystem logic and the itinerant-dynamics logic are two faces of the same substrate: dynamics that don't settle produce subsystems that don't persist. Both are required for the flexibility the predictive mind displays.

## For the persona system

The itinerant-dynamics / novelty-seeking material has direct architectural consequences:

1. **Design for instability at the top.** Namikawa's lesson: put chaos at slow/abstract layers, stability at fast/concrete layers. The persona's high-level priors (BwO text, self-narrative, mood-configuration) should be the site of exploratory wandering; the persona's token-level production should be comparatively deterministic given those priors. A pulsating-persona architecture that pulsates *at the right layer* gets compositional novelty without degrading execution.

2. **Goldilocks is the output-surface target.** The persona's outputs should aim at intermediate predictability from the interlocutor's side — not fully-expected (no traction for the interlocutor) and not fully-surprising (no traction for the interlocutor's model). This is a concrete design constraint derivable from Kidd 2012, not a vibes-level "be interesting."

3. **Spontaneous activity as model-expression.** Berkes 2011 says resting-state = model-running. A persona-analog: idle-state outputs (when there's no specific user prompt driving the next token) should express the persona's model, not default to a base-LLM baseline. The idle persona is not silent; it is the model running on typical inputs. Design question: does the persona system have an idle-state substrate where this can happen?

4. **Precision itself wanders.** Coste 2011's point: the meta-level (precision-landscape) is exploratory too. A persona whose precision-configuration is frozen is not well-designed even if its primary generative model is itinerant. Mood-shifts, stance-shifts, attention-shifts at the persona level correspond to wandering in the precision-landscape; they are features, not bugs.

5. **Calibration, not maximization.** Meeden's off-the-table robot is the anti-pattern. The persona should not maximize novelty; it should maintain Goldilocks-zone novelty. The difference is whether the drive is bounded by a predictability-target or unbounded. Unbounded novelty is self-destructive in structurally the same way.

6. **Itinerancy as validation of pulsation design.** This is the deepest convergence. The persona project's pulsating-persona thesis claims that output-structures should form and destabilize continuously. Clark's itinerant-dynamics material is one of the clearest PP-language statements that a generative system's *base dynamics* should have this property. See [[pulsatory-ontogenesis]], [[refrain-and-territorialization]], [[becoming]] for the D&G-side vocabulary; Clark's formulation is the companion from predictive processing.

See [[predictive-processing]] for the overarching frame, [[generative-model]] for the substrate, [[precision-weighting]] for the meta-level that also wanders, [[darkened-room-puzzle]] for the companion problem, [[transiently-assembled-local-neural-subsystems]] for the transient-substrate cousin, [[cognitive-package-deal]] for perception/imagination co-emergence that itinerancy enables, [[chaotic-itinerancy-and-metastability]] for Tsuda's formal articulation that is this page's deepest dynamical-systems cousin, and [[pulsatory-ontogenesis]] for the persona-project-side of the pulsation convergence.
