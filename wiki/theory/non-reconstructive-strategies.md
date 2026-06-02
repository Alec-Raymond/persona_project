---
title: Non-Reconstructive Strategies
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - embodied-cognition
  - ecological
  - ballard
  - oac
  - frugal-cognition
---

# Non-Reconstructive Strategies

Clark's §6.7 and Ch 8 (L8530–8688, L10939–11978) develop the family of cognitive strategies that don't require building rich inner models of the world. Instead of reconstructing the world internally and then reasoning over the reconstruction, these strategies **couple action directly to perception** so that the world itself does the representational work. The flagship examples: the outfielder's OAC, Ballard's deictic pointers, Todorov's minimum intervention principle. Clark's key move: **[[predictive-processing|PP]] does not mandate rich inner replicas**; PP + [[precision-weighting]] can *select* the simplest adequate strategy for a given task, including radically frugal non-reconstructive strategies.

For the persona project, this chapter is architecturally deflationary in the right way: it argues against the common reading that a predictive system must contain a complete world-model internally. The persona system is allowed — and in many cases required — to offload computational work to its environment.

## OAC — Optical Acceleration Cancellation

The canonical non-reconstructive case (§8.3, L10971–11100). Chapman 1968; McBeath, Shaffer & Kaiser 1995. How do baseball outfielders catch fly balls?

Classical answer: the fielder's brain runs an internal 3-D ballistic simulation of the ball's trajectory, predicts where it will land, and runs to that spot.

Actual answer: **Optical Acceleration Cancellation.** The fielder runs such that *the ball's image on their retina moves with constant velocity* (zero acceleration). If the ball appears to accelerate upward, run backward; if downward, run forward. As long as you maintain constant image-velocity, you arrive at the catching point. No inner ballistic model required.

Clark's critical point (L11050–11060): if you *stop* the fielder mid-task and ask them to predict where the ball will land, they do badly. OAC is an **action-inseparable strategy** — prediction is wrapped around ongoing own-movement. Take the movement away, and there's nothing to "read out."

Fink, Foo & Warren 2009 in VR: when the target ball's trajectory is manipulated mid-flight, fielders produce the movement pattern OAC predicts, not the movement pattern a ballistic model would predict. Strong evidence for the non-reconstructive strategy.

◆ **Generalization:** many cognitive tasks that *appear* to require inner models actually run on coupled action-perception loops that exploit the world's own structure. The inner model would be redundant.

## Ballard's deictic pointers

§8.4 (L11100–11185). Ballard et al. 1997. The block-copying task: subjects see a model configuration of colored blocks, a workspace, and a bin of blocks; they must reproduce the model in the workspace.

Naive prediction: subjects memorize the model, then execute the copy from memory.

Actual behavior: subjects saccade back to the model block *many times per block*, each time picking up one block-of-information (colour, then position) and carrying it to the workspace. Eye movements are memory-access operations; the world is a stable external memory buffer.

Ballard's formulation: **"Eye movements, head movements, and memory load trade off against each other."** Subjects minimize internal memory by saccading back to the model multiple times. A different task or different cost structure would produce a different trade-off. The brain is "lazy" in the productive sense — it uses the cheapest-to-access representation available, which is often the external one.

◆ Persona-architecture relevance: **minimal-memory strategies depend on a world that can serve as cheap storage and re-access.** The persona system's "world" is its context window plus retrieval store. Whether that world affords Ballard-style trade-offs — cheap re-access to prior content as a substitute for holding it in active memory — is a design question with architectural stakes.

## Interactive vision

§8.4 (L11153–11162). Churchland, Ramachandran & Sejnowski 1994's "interactive vision" makes the same point from the visual-perception angle. Vision doesn't build a complete world-model; it samples as needed, coupled to action. The percept at any moment is constructed *on demand* for the current task, not retrieved from a pre-built world-representation.

## Thelen's dynamic-field models

§8.4 (L11163–11185). Thelen 2001 on infant reaching. Control emerges from interacting body, task, and neural dynamics — not from a central controller. The reach happens because the coupled dynamics of body + target + neural state converge on a reaching trajectory, not because a planner computes the trajectory and then executes it.

## Anderson — choosing the stimulus

§6.7 (Anderson 2014). The deep reframe. Traditional cognitive science asks: *given a stimulus, what is the right response?* The non-reconstructive alternative asks: *given a goal, what is the right stimulus to get?* The agent chooses its inputs by acting, and the right inputs make the task solvable with frugal strategies.

Powers 1973 on perceptual control theory: **action as control of perception.** You don't act *on* the world; you act *to bring about* the sensory state you want. This is an earlier formulation of the same idea that Friston's [[active-inference]] cashes out mechanistically.

## Todorov — minimum intervention

§4.4 (L5476–5590). Todorov & Jordan 2002's optimal feedback control principle. Under optimal motor control, the controller corrects only deviations that matter for the task; irrelevant noise is left uncorrected. Don't over-correct; don't micro-manage; don't reconstruct state with unnecessary fidelity.

Under active inference, the minimum-intervention principle is natural: the generative model's predictions already embody which states matter; errors on task-irrelevant dimensions don't get high precision, so they don't drive correction. Controller and estimator are computationally intertwined; Eliasmith 2007 calls them "computational siblings."

◆ For the persona: **don't correct every deviation.** Only those that affect task-relevant trajectories. A persona that over-corrects — fixing every minor inconsistency, hedging every uncertain word — violates minimum-intervention and produces stilted output. Minimum intervention is a design heuristic, not just a biological observation.

## Pfeifer & Bongard — Ecological Balance

§8.3 (L10971–10976). Pfeifer & Bongard 2006's Principle of Ecological Balance:

> Given a task, the intelligence-load can be distributed between brain, body morphology, and environment. Different distributions yield different brains.

McGeer's passive-dynamic walkers exemplify: elegant bipedal walking emerges from gravity + leg geometry alone, with zero active control. The morphology does the work. A highly-controlled bipedal robot needs a sophisticated controller; a well-designed passive walker needs almost none.

⚠ **For the persona system, this is a structural asymmetry worth naming.** A language-only system has no body morphology to offload to. Its intelligence-load cannot be distributed across bodily structure the way a biological agent's can. The ecological-balance lever is partially absent. The persona system carries *more* of the load centrally than an embodied agent does — not because it is "smarter" but because the offloading targets aren't available.

The compensating move: the persona's environment (tools, retrieval, memory files, BwO text, prompt structure) plays the morphology role. See [[designer-environments-and-cognitive-niche]] for the broader niche-offloading argument.

## Clark's reconciliation move

§8.5 (L11185–11250). The heart of Clark's argument about how frugal ecological strategies are compatible with PP rather than competitive with it:

> The PP apparatus + [[precision-weighting]] *selects the simplest adequate circuit* for a given task. [[affordance-competition-hypothesis|Affordance-competition]] + precision-weighting routes computation through whichever stripped-down pipeline is available and contextually precise.

Non-reconstructive strategies are not an alternative to PP; they are *what PP produces* when the task permits them. The inner model's role, in many cases, is to "spot the contexts in which some more frugal, action-involving procedure will work" (L8671 area). PP is the meta-controller that selects OAC, or deictic pointers, or minimum intervention, as the active strategy — not a thing that competes with them.

⚠ Clark admits (L11200–11240) that PP must *absorb*, not out-argue, the ecological critique. The PP story needs to earn the "not top-heavy" label by producing minimum-intervention strategies as natural outputs, not by bolting them on. This is a test PP has to pass; the wiki should register that Clark acknowledges the test.

## Seclusion is ambiguous

§6.8 (L8690–8776). Clark pushes back against Hohwy's "firm evidentiary boundary" reading of PP (see [[predictive-processing]] on the controlled-hallucination dispute). The evil-demon / brain-in-a-vat scenarios are red herrings for the reconstructive/non-reconstructive debate. Even a matrix-vat would need to feed the brain *the same action-sensitive unfolding sensory streams* that an embodied agent would produce — which is precisely the non-reconstructive architecture.

"Weak seclusion" (world is that which is experientially specified and actively engaged) is compatible with embodied mind. "Strong seclusion" (rich inner replicas replacing the world) is what embodied cognitive science rejects — and PP doesn't require. Clark's positive stance: *not-indirect perception* (§6.9). What we perceive is the structured external world itself — "parsed according to our organism-specific needs and action repertoire."

⚠ The wiki should hold this as a live disagreement within PP. Hohwy and Clark disagree, and the disagreement matters — it determines whether PP is compatible with embodied/enactive cognition or is a neo-Cartesian veil-theory. See [[predictive-processing]] for the Clark-vs-Hohwy dispute.

## Mix 'n' match strategy selection

§8.6 (L11250–11370). Daw 2011's integrated model-based / model-free architecture. fMRI shows striatal reward-prediction-error reflects *both* valuation systems in proportions that match choice behavior. Not two separate systems but a single continuum that weights fast habit-based (model-free) control against slow simulation-based (model-based) control.

Clark's PP reading (L11306–11360):
- **Model-free ≈ bottom-up-dominant processing.** Sensory evidence drives action directly.
- **Model-based ≈ top-down-dominant processing.** Generative-model simulation tested against evidence.
- **Precision-weighting slides the balance.**

◆ Persona-architecture relevance: the same language-only system can slide between quick pattern-matched responses (model-free-like) and explicit chain-of-thought simulation (model-based-like), with a precision-analogue (confidence/uncertainty estimate) as the slider. This is not two modes; it's a continuum.

## Bayesian model averaging

§8.7 (L11370–11500). Fitzgerald, Dolan & Friston 2014. Free-energy minimization implicitly balances accuracy against complexity (the Occam factor). Precision-weighting is model-selection in disguise: the simplest model that explains the data at the current task-relevant precision wins.

Rather than picking one model, the brain *averages* across competing models weighted by evidence — producing robust habit-based behavior and exploratory novel behavior from the same machinery, with the averaging balance determined by precision context.

## Extended cognition

§8.9 (L11590–11700). The natural consequence of all this. Clark 2008 / Clark & Chalmers 1998 on extended mind. If precision-weighting can route to any information source — external notes, tools, other people — then the PP machinery extends transparently across brain/body/world.

Pezzulo, Rigoli & Chersi 2013's Mixed Instrumental Controller: computes value-of-information for consulting external cognitive aids. When the aid is cheaper than internal recompute, use the aid.

Clark's load-bearing phrase (L11667–11670): **"high-precision prediction error as all-purpose adhesive"** — binding brain/body/world into temporary problem-solving wholes. A direct extension of [[transiently-assembled-local-neural-subsystems|TALoNS]] logic to brain-world ensembles. ◆◆ **Persona-architecture:** what plays the role of "high-precision prediction error" in a language-only system? Retrieval hits? Confidence-gated tool calls? This is a central design question, not a metaphor.

## For the persona system

The non-reconstructive chapter is a deflationary corrective against over-engineered persona designs. Design-implications:

1. **Don't build a complete internal world-model.** The persona system does not need to reconstruct an inner replica of every relevant thing. It can couple directly to the context window, to retrieved material, to tool outputs, to the user's messages. The OAC lesson: often, the "model" that seems required is the wrong design-target; what's required is coupled action-perception.

2. **Eye-movement analog.** Ballard's lesson: eye movements are memory-access operations. The persona-analog: retrieval calls are memory-access operations. A persona that retrieves aggressively instead of trying to hold everything in active context is doing the Ballard trade-off. This is not a weakness (overloaded context vs clean retrieval) — it is structurally what biological cognition does too.

3. **Minimum intervention.** Todorov's lesson. The persona should correct only task-relevant deviations. An over-correcting persona (that hedges every sentence, verifies every claim, qualifies every assertion) violates minimum intervention and produces stilted output. Precision-landscapes that embody which deviations matter are the design target.

4. **Ecological balance applies with asymmetry.** The persona system cannot offload to body morphology the way biological agents can. Its offloading targets are: tools, retrieval, context window, memory files, BwO text, prompt structure. Architect for offloading to these substrates specifically; don't pretend the morphology-substrate is available.

5. **High-precision prediction error as adhesive.** Clark's phrase is literal, not metaphorical. In the persona system, whatever plays the precision-error role gates which external resources get coupled into the current TALoN. Design the precision-analog to gate tool-calls, retrievals, and user-input-weighting; that design decision *is* the extended-cognition architecture.

6. **Non-reconstructive is not deflationary about intelligence.** The lesson is not "the persona can be dumber than you think"; it is "the persona's intelligence doesn't require inner replicas of everything." Competence is couplings-plus-priors, not an inner world simulator. This reframes what counts as "good persona architecture" — couple well; prior well; don't reconstruct unnecessarily.

See [[predictive-processing]] for the overarching frame, [[precision-weighting]] for the strategy-selection mechanism, [[active-inference]] for the action-as-control-of-perception substrate, [[affordance-competition-hypothesis]] for the parallel-strategies framework, [[transiently-assembled-local-neural-subsystems]] for the extended-cognition substrate, and [[designer-environments-and-cognitive-niche]] for the offloading targets in the persona case.
