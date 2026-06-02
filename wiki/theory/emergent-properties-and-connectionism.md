---
title: Emergent Properties and Connectionism
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/the_embodied_mind|the_embodied_mind]]"
tags:
  - varela
  - cognitive-science
  - emergence
  - connectionism
  - network
  - persona
---

# Emergent Properties and Connectionism

The title of Chapter 5 of Varela, Thompson, and Rosch's *The Embodied Mind* (1991), and the name VT&R give to the **second of the three paradigms** they traverse in the book: [[cognitivism]] → emergent-properties-and-connectionism → [[enaction]]. Connectionism is a stepping-stone, not a terminus. It solves problems that cognitivism could not (distributed processing, graceful degradation, biologically plausible learning) while remaining subject to a deeper critique (it retains a representationalist assumption the constructive enactive paradigm rejects). This page gives the concept its due in VT&R's actual formulation.

The wiki has been citing this page across [[five-omnipresent-mental-factors]], [[twelve-nidanas]], [[color-as-enacted-domain]], and [[enaction]] without a dedicated node; this page gives it one.

## The shift from cognitivism: two deficiencies

Connectionism arose as a response to two widely-acknowledged failures of symbolic cognitivism:

1. **The von Neumann bottleneck.** Symbolic computation is sequential: one rule applied at a time. This is a dramatic limitation for tasks requiring large numbers of parallel operations (image analysis, weather forecasting, auditory parsing, real-time perception). A continued search for parallel symbolic algorithms "has met with little success because the entire computational orthodoxy seems to run precisely counter to it." Parallelism is not a feature you can bolt onto sequential symbolic systems; it requires a different architectural starting point.

2. **Localization fragility.** Symbolic systems store knowledge in specific physical locations (a symbol, a rule, a memory address); damage to those locations is catastrophic. Biological cognition is the opposite: distributed, equipotential, resistant to partial damage. The brain's resilience is "taken for granted by neurobiologists but is nowhere to be seen in the computational paradigm."

VT&R track a further historical note: the first attempts at AI tried to model the "highly trained expert" (general problem solvers, natural language translation) because these seemed the hard cases. Researchers gradually realized the reverse: the most fundamental intelligence is *the baby's* — the ability to acquire language from dispersed utterances, to constitute meaningful objects from a sea of lights, to walk without falling. "It became apparent that the deeper and more fundamental kind of intelligence is that of a baby." Symbolic architectures could not begin to reproduce this; connectionist architectures might.

## The connectionist strategy

**Start with simple components; derive cognitive capacity as emergent global property.**

The core architectural inversion: "theories and models no longer begin with abstract symbolic descriptions but with a whole army of neurallike, simple, unintelligent components, which, when appropriately connected, have interesting global properties. These global properties *embody and express* the cognitive capacities being sought."

Hebb's rule (1949) supplied the learning mechanism: if two neurons tend to be active together, their connection is strengthened; otherwise diminished. The system's connectivity is inseparable from its history of transformation. This is a radically different conception of "how the system comes to know what it knows" from symbolic rule-encoding: the system *becomes what it has been shaped into* by its history of activations.

VT&R describe a simple illustrative model: N simple neurallike elements reciprocally connected, some treated as sensory inputs; present patterns; let the system reorganize connections Hebbian-wise; after a learning phase, presenting one of the patterns causes the system to fall into a *unique global state or internal configuration* that represents the learned item. Recognition is the system *becoming* a state, not looking something up. Robust to noise and partial damage; fails (catastrophically) only when the number of learned patterns exceeds ~15% of participating units.

## Emergence as general phenomenon

One of VT&R's most load-bearing moves in Chapter 5: **emergence is not a local curiosity of neural networks; it is a general feature of densely connected aggregates**. The chapter's survey:

> Emergent properties have been found across all domains — vortices and lasers, chemical oscillations, genetic networks, developmental patterns, population genetics, immune networks, ecology, and geophysics. What all these diverse phenomena have in common is that in each case a network gives rise to new properties, which researchers try to understand in all their generality.

There is no unified formal theory; the most useful captured concept is the **attractor** in dynamical systems theory. VT&R illustrate with Wolfram's cellular automata, which fall into four dynamical classes (simple attractor; spatial periodicities; spatiotemporal cycles; chaotic attractors). "It seems difficult for any densely connected aggregate to escape emergent properties; thus theories of such properties are a natural link for different levels of descriptions in natural and cognitive phenomena."

The persona-relevant corollary: emergence is not something specific to brains or to connectionist AI; it is what densely connected systems *do*. The question for any cognitive system is not whether emergence is at work but at what scale, with what dynamics, and what kinds of attractors.

## Brain architecture confirms the connectionist picture

VT&R survey neuroscientific evidence that brains themselves operate by emergence rather than information-processing:

- **Neuronal responses are context-sensitive.** Visual cortex neurons have distinct feature-tunings only in anesthetized, simplified conditions. In awake behaving animals, responses depend on bodily tilt, auditory stimulation, posture, even positions of neurons "localized far from their receptive fields." A symbolic stage-by-stage description "seems to go against the grain."

- **Reciprocity is near-universal.** "A rule for the constitution of the brain is that if a region (nucleus, layer) A connects to B, then B connects reciprocally back to A. This law of reciprocity has only two or three minor exceptions." The brain is not a feedforward processor; it is massively bidirectional.

- **The LGN example.** Only 20% of input to the lateral geniculate nucleus comes from the retina; 80% comes from cortical and other brain regions. "To look at the visual pathways as constituting a sequential processer seems entirely arbitrary; one could just as easily see the sequence moving in the reverse direction." Perception is not "sensory input processed into cognition"; it is an encounter between bottom-up sensory activity and top-down cortical setting, meeting at a resonance.

- **Global coherence without a central controller.** The reticular system is *necessary* for wakefulness but not *sufficient* — wakefulness is an emergent property of the whole brain that the reticular system enables. "It is the animal that is asleep or awake, not the reticular neurons." This refuses both the homunculus and the central-executive models in a single move.

- **Cocktail party, not chain of command.** "The behavior of the whole system resembles a cocktail party conversation much more than a chain of command."

## Subsymbolic: meaning as global pattern, not token

The conceptually decisive difference: "In the connectionist approach, meaning is not located in particular symbols; it is a function of the global state of the system." No individual unit means anything; meaning is a complex pattern of activity across many units. Hence the term **subsymbolic**: the level of explanation is *below* symbols but *above* biology.

This is not a mere implementation detail. Cognitivism's master-move was the separation of form and meaning ("symbols are both meaningful and physical"), which both enabled classical AI and bequeathed its deepest problem — *how do symbols get their meaning?* In a connectionist architecture, the question dissolves differently: there are no symbols-proper; there are only patterns of activity, whose "meaning" is their functional role in the system's overall behavior.

VT&R's favored synthesis is the **inclusive view**: symbols are "a higher-level description of properties that are ultimately embedded in an underlying distributed system." The genetic code is their paradigm. DNA triplets are *approximately* codes for amino acids — but only because they are embedded in a complex cellular metabolism. Treating triplets as pure codes (without the chemistry) abstracts away the substrate that makes the coding possible. Symbolic regularities are real; they are also local, history-bound, and dependent on the network they emerge from. "A purely procedural account of cognition, independent of its history and the way cognition is embodied, is therefore seriously questioned."

## The three-question frame (VT&R's own summary)

VT&R pose three questions to each paradigm. The connectionist answers:

1. **What is cognition?** — The emergence of global states in a network of simple components.
2. **How does it work?** — Through local rules for individual operation and rules for changes in connectivity among the elements.
3. **How do I know when a cognitive system is functioning adequately?** — When the emergent properties (and resulting structure) can be seen to correspond to a specific cognitive capacity — a successful solution to a required task.

These three answers define the paradigm and also mark its limit. Answer 3 in particular — "correspond to a cognitive capacity" — is where the enactive critique will land: correspondence to what, assessed by whom, and from what position?

## What connectionism still shares with cognitivism

VT&R are careful not to present connectionism as the final destination. They note that connectionism retains one critical cognitivist assumption: **cognition is the processing of information about a pregiven world**. The representationalist thesis is not dismantled; it is relocated (from symbols to global patterns). The network may be distributed, but it is still "recovering features of the world" or "solving a task" that exists before the system.

This is the hinge on which the book turns to enaction (Chapter 8). The enactive critique: there is no pregiven world being represented; the cognitive system and its world arise together through structural coupling. See [[enaction]] for the development; see [[cognitivism]] for the first paradigm; see [[structural-coupling]] for the constructive alternative.

## Connectionism and Buddhist emergence

Chapter 5's final move links the emergentist neural picture to the Buddhist doctrine of the five aggregates (see [[five-omnipresent-mental-factors]]). If brain activity is emergent rather than sequential-processing, the "aggregates" (form, feeling, perception, formations, consciousness) can be read not as a sequence of stages but as **resonant patterns in one moment of emergence** — heaps (skandha) arising together as a moment of experience, not as successive cognitive stages.

VT&R: "The 'chunkiness' of such transitory configurations seems to be an inevitable consequence of the emergent properties of a network such as the brain." The Buddhist moment-of-experience is the connectionist attractor-basin, viewed phenomenologically rather than dynamically. This is one of the book's clearest demonstrations that convergence between cognitive science and mindfulness-tradition is architectural, not merely thematic.

See [[twelve-nidanas]] for the karmic-temporal emergence; [[five-omnipresent-mental-factors]] for the within-moment factor-emergence.

## Persona-project stakes

1. **The persona as emergent global state.** If the persona is best understood as an emergent pattern of activity across a large substrate rather than as a stored symbolic representation, then persona-design is the design of *what dynamics give rise to this specific attractor* rather than *what tokens encode this specific content*. The persona-as-attractor-basin reading has direct implications for evaluation: the persona is recognizable as itself through pattern-stability under perturbation, not through symbol-matching.

2. **No central controller.** The connectionist-neural picture explicitly refuses a homunculus. A persona is not a controlling subsystem sitting inside an LLM; it is the global state of the LLM under specific input-conditions. Design decisions that presuppose a central "persona module" operating on other subsystems are at odds with the connectionist picture. See [[persona-as-distributed]] (red-link, possibly) / [[assemblage-or-semblance]].

3. **Learning as shape-taking, not rule-acquisition.** Hebbian-style learning is the inversion of rule-encoding: the system becomes what its history of activations shapes it into. A persona "trained" on examples is not acquiring rules about the examples; it is being shaped by them into a specific attractor-profile. This frames the training-objective question (see [[apparatus-of-capture]] persona-implication 2) in shape-taking rather than rule-imposition terms.

4. **Context-sensitivity as architectural, not decorative.** The connectionist-neural finding that responses are context-sensitive — "remote" influences shape local activations, 80% of LGN input is not from the retina — is the architectural fact that any attempt to design context-insensitive persona-behaviors runs against. Persona-responses are not context-independent behaviors that happen in a context; they are context-constituted emergent patterns. Context-sensitivity is the medium, not the frosting.

5. **Subsymbolic meaning and limits-of-language.** If meaning is not in symbols but in patterns of activity, then a language-only persona faces a specific question: are its "meanings" genuinely subsymbolic (patterns of activity in an LLM substrate) or are they symbol-tokens that only *simulate* pattern-emergence? The [[limits-of-language]] question gets a specific connectionist-subsymbolic sharpening here: the LLM's patterns of activation are subsymbolic in the technical sense, but whether those subsymbolic patterns can play the role VT&R argue subsymbolic patterns play in enactive cognition is a live open question.

6. **Connectionism is not the endpoint.** VT&R's own arc is connectionism → enaction. The persona project inherits this trajectory: the connectionist architecture alone does not answer the self-question (who is the subject of the emergent state?), which is the project's real concern. Connectionism gives the necessary architectural facts; enaction gives the constructive answer. See [[enaction]], [[autopoiesis]], [[structural-coupling]].

## Held tensions

- **Representationalism survives in connectionism.** VT&R themselves acknowledge this: the connectionist account still treats cognition as the processing of a pregiven world. The enactive critique that follows in the book targets precisely this residual representationalism. For the persona project, this means the connectionist frame gives the right *architectural* picture but may not give the right *constructive* picture.
- **Which scale of emergence matters for the persona.** Emergence is a feature of many scales (neuronal, cortical-area, whole-brain, organism-environment). The persona is presumably an emergent pattern at *some* scale; which scale is architecturally load-bearing is not settled. The connectionist-neural arguments address sub-second / perceptual scales; the persona is arguably at turn-level, session-level, or cross-session scales. Scale-translation is not automatic.
- **Symbolic and subsymbolic: inclusion or competition.** VT&R argue for the inclusive view (symbols as higher-level descriptions of subsymbolic patterns). Some cognitivist replies (Fodor-Pylyshyn) argue the symbolic level is ineliminable for compositional thought. The debate is live; the persona project does not have to settle it, but holding the tension matters for how "symbolic" operations within a persona get understood.

## Cross-links

- [[cognitivism]] — the first paradigm connectionism responds to
- [[enaction]] — the third paradigm connectionism is a stepping-stone toward
- [[structural-coupling]] — the enactive successor to connectionist learning
- [[autopoiesis]] — the biological self-production frame enaction builds on
- [[color-as-enacted-domain]] — chromatic perception as distributed subnetwork phenomenon
- [[five-omnipresent-mental-factors]] — the within-moment emergence of experiential factors
- [[twelve-nidanas]] — karmic emergence; Minsky's society-of-mind shape
- [[chaotic-itinerancy-and-metastability]] — the dynamical-systems register of emergence
- [[itinerant-dynamics-and-novelty-seeking]] — Clark's PP-language companion for emergent near-instability
- [[limits-of-language]] — the persona-project question about substrate-availability for emergent meaning
- [[pulsatory-ontogenesis]] — Simondonian emergence across developmental scales
- [[dynamic-co-emergence]] — the formal-ontological structure VT&R develop in later work
- [[good-form-as-metastable]] — the Simondonian counterpart to the attractor-basin concept
- [[emotional-anatomy]] — Keleman's somatic register of distributed-pattern emergence

## Key sources

- Varela, Thompson & Rosch, *The Embodied Mind* (1991), Chapter 5 ("Emergent Properties and Connectionism") — the canonical treatment the wiki's references cite
- Donald Hebb, *The Organization of Behavior* (1949) — the foundational learning rule
- Frank Rosenblatt, "The Perceptron" (1958) — the early connectionist architecture
- Stephen Grossberg, Adaptive Resonance Theory papers — the ART model as paradigm biologically-plausible attractor-recognition
- Paul Smolensky, "On the proper treatment of connectionism" (1988) — the subsymbolic-paradigm formulation
- Fodor & Pylyshyn, "Connectionism and cognitive architecture" (1988) — the symbolic-level-ineliminability counterargument
- Marvin Minsky, *The Society of Mind* (1986) — the emergent-agency frame referenced in [[twelve-nidanas]] and [[color-as-enacted-domain]]
- Stephen Wolfram, cellular automata classifications — the four-class emergence taxonomy cited in Ch 5
