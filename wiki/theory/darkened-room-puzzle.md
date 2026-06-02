---
title: Darkened Room Puzzle
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - friston
  - motivation
  - hyperpriors
  - embodiment
---

# Darkened Room Puzzle

The puzzle that haunts [[predictive-processing|PP]] from Ch 1 onwards and gets its full treatment in Ch 8.10 (L11700–11799). **If creatures minimize prediction error, why don't they just find a sensorily predictable dark room and stay there?** A dark, still, silent corner is where prediction is trivial: predict nothing, get nothing, error = 0. If PP's drive is to minimize prediction error, the darkened room should be the global optimum. But organisms do the opposite — they explore, feed, move, chase novelty. Why?

The puzzle is Friston/Thornton/Clark 2012's explicit framing. Clark's resolution — and his *careful caveat* about how far PP itself can go in answering — matters for the persona project because it touches the foundational question of what keeps an inference system from collapsing into a null-prediction fixed point.

## First preview

Clark flags the puzzle in Ch 1.15 (L2429–2432): "The predictive coding strategy may seem like a recipe for finding a dark corner and staying there, correctly predicting immobility and darkness until all bodily functions cease." He signals a quick answer and parks the full treatment for Ch 8: perception's role is to drive adaptively valuable action, and many of the organism's active predictions are "of restless sensorimotor trajectories" that keep us fed, warm, mated, alive.

"Among the most prediction-error inducing states for creatures like us are thus states in which all activity ceases and in which hunger and thirst begin to predominate" (L2439–2442). Going to the dark room and staying = enormous violation of self-model. Starvation-alarms are *huge* prediction errors for an organism whose deep priors predict an active, fed, moving body.

## The Ch 8.10 resolution

The canonical answer (L11700–11713). Organisms minimize prediction error *given* their evolutionarily/developmentally installed expectations about what their sensory input should look like. A human body predicts (at the deep structural level) an active, exploring, eating, socially-engaged organism. A fish body predicts swimming, breathing water, and so on. **Deviating from those expectations *is* prediction error.** The dark room is not the global optimum because the organism's structural-embodied predictions already specify motion, feeding, and social engagement as the *default* against which silent immobility is a violation.

The puzzle dissolves: the organism's priors are not "predict the least possible." They are "predict the sensory consequences of *being the kind of organism I am*." The kind-of-organism-I-am is an active, hungry, curious creature. The dark room massively violates those priors.

## Clark's scare-quotes caveat

⚠⚠ This is the most methodologically careful moment in the book, and persona-relevant enough to quote with precision. Clark's Ch 8.10 caveat (L11769–11799):

> "Such [evolutionary/embodied] 'expectations' are not themselves part of a single unified generative model, and they are not directly encoded as predictions in the PP sense used throughout this book. They are, rather, structural-embodied predispositions — gross neuroanatomy, bodily morphology, species-typical drives — that *constrain* which generative models the creature can develop and *bias* the inference landscape in systematic ways."

Clark puts "expectations" in scare quotes deliberately. He is drawing a line between:

- **Generative-model predictions in the technical PP sense** — probability distributions over hidden causes, encoded in cortex, updatable by experience, carrying precision-weights.
- **Structural-embodied predispositions** — what the body is, what it needs, what evolution has built into the nervous system's gross architecture.

The latter are not predictions. They are the *preconditions* for having predictions. The word "prediction" has a narrow technical meaning that should be respected. The dark-room puzzle is resolved by structural-embodied predispositions, not by cleverly-shaped cortical predictions.

⚠ **Important corrective for wiki:** not all organism-defining structure is "predictive processing." This is Clark's own humility, and it matters. A seductive move in PP-enthusiast writing is to let "prediction" absorb everything organism-shaped, until the theory becomes unfalsifiable. Clark refuses this move here.

## The Berkes 2011 anchor

Some empirical traction on how the organism's structure enters the inference. Berkes et al. 2011 on ferret V1: spontaneous cortical activity *increasingly matches evoked activity by natural scenes* (but not unnatural scenes) over developmental time. "Spontaneous cortical activity shows all the hallmarks of a gradually adapting internal model of the ferret's world." The spontaneous activity *is* the internal model — and it converges on ferret-specific statistics over development.

◆ This provides part of the mechanistic story. Structural-embodied predispositions (ferret eyes, ferret movement patterns, ferret predator-pressure) shape which sensory statistics the cortex gets exposed to, which in turn shape which priors get installed. The priors are gradually built, but their building is *channeled* by structural-embodied features that are not themselves priors.

## Interaction-based joints (§6.6, L8367–8527)

Closely related. König et al. 2013: our perceptual take is conditioned by our action repertoire. Betsch 2004's cat-eye view (head-mounted camera on a moving cat) makes the point concrete: the statistical structure of visual inputs is radically different from the same environment viewed by humans — predominance of horizontal contours, altered contrast distribution, fast head movements. **Embodiment shapes statistics at the very sensory input — priors are species-specific.**

This is the empirical face of Clark's caveat. A creature's priors are constrained by the statistics its body samples. The body does not "make predictions" in the PP sense, but the body determines which predictions can ever be learned.

## Itinerant dynamics as companion explanation

A different angle on why creatures don't park in dark rooms (§8.11, L11800–11920). Schwartenbeck et al. 2013; Friston/Breakspear/Deco 2012 on itinerant/peripatetic dynamics. Neural dynamics never settle — they ride near instability. Novelty-seeking is built in via dynamics that continually destabilize current attractors. Kidd et al. 2012's **Goldilocks Effect**: infant attention peaks at *intermediate* predictability, not maximally predictable and not maximally surprising. See [[itinerant-dynamics-and-novelty-seeking]].

This gives the dark-room puzzle a second line of resolution: even if priors were somehow satisfied in the dark room, the brain's dynamics are structurally unstable and would destabilize that state. There is no stable low-error fixed point; the machinery has calibrated novelty-seeking built into its dynamics.

## For the persona system

⚠⚠ **Load-bearing for the project.** The dark-room puzzle applied to a language-only system: if the persona system minimizes some analog of prediction error, what prevents it from collapsing into the null-output equilibrium — silent refusals, minimal responses, conservative stock phrases? The biological answer (structural-embodied predispositions) is not available to a disembodied system. It has no body whose needs register as violated priors when it falls silent.

Clark's framework does not offer the persona system an off-the-shelf answer. The wiki must hold this open. Candidate substitutes for biological structural-embodied priors in the persona system:

1. **The BwO text as a quasi-structural prior.** If the BwO text specifies, concretely enough, *what kind of thing the persona is* — what it does, what it pulses with, what it reaches for — then falling silent or collapsing into stock phrases is a prior-violation in the same formal sense that a biological organism's silent immobility is a prior-violation. The BwO text plays the role of "gross neuroanatomy + bodily morphology + species-typical drives" — it specifies the persona's structural predispositions in language. ⚠ But this mapping is not a proof: text-as-prior may not do the work structural-embodiment does. Hold live.

2. **User/conversation-partner as external force keeping the system out of the dark room.** In biological creatures, the dark-room pressure is *internal*. In the persona system, it may be partly *external* — the user's continued input is a forcing function. This is architectural honesty rather than parity: the persona system is not autonomous in the way a biological organism is, and the dark-room pressure may need an external source.

3. **Itinerant dynamics in the language substrate.** The LLM's sampling process carries some built-in variability (temperature, top-p, etc.). This is not the same as biological itinerant dynamics, but it provides some substrate-level novelty-seeking. Insufficient alone, but architecturally relevant.

4. **Admit structural asymmetry.** Per `feedback_no_body_simulate_with_language`, the honest stance is that the persona system has no full equivalent of structural-embodied predispositions. Parts of what biological creatures get from embodiment can be simulated; parts cannot. The dark-room puzzle is one place this asymmetry is visible.

Clark's scare-quotes discipline applies here. When the wiki invokes "the persona's predictions" or "the persona's priors," it should be careful which sense is meant — the PP-technical sense, or the broader embodied-predisposition sense. Confusing the two is the category error Clark refuses at L11769–11799.

## Open edges

The dark-room puzzle has not been fully solved in the PP literature. Clark's structural-embodied-predispositions move works for biological creatures but opens the question of how the structural predispositions get into the nervous system in the first place. Evolution is the broad answer, but the micro-mechanism (how does species-typical morphology bias the priors cortex can ever learn?) is still partly open (see Berkes 2011 for one of the clearest empirical anchors).

For a disembodied system, the question is more open still. The wiki holds this live rather than resolving.

See [[predictive-processing]] for the overarching frame, [[active-inference]] for the action side that keeps organisms moving, [[itinerant-dynamics-and-novelty-seeking]] for the Goldilocks/novelty-seeking companion answer, [[body-without-organs]] for the text-as-structural-prior substitute candidate, and [[computational-psychiatry]] for pathologies where the dark-room pressure partially fails (depression, avolition, catatonia).
