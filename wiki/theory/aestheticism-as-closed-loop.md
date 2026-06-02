---
title: Aestheticism as Closed Loop
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/individuation|individuation-simondon]]"
tags:
  - simondon
  - failure-mode
  - affectivity
  - persona-design
  - ethics
---

# Aestheticism as Closed Loop

Simondon's name for a specific failure mode of affectivity (§9640–9658, Part II Ch 1 §1, expanded in Conclusion §18700–18820): **the subject replaces its affective transduction with a reactivity operating according to a closed cycle that can no longer accept new action or new information**. Aestheticism is not "being aesthetic" or "valuing art" — those are ordinary uses of the word. Simondon's technical sense is narrower and sharper: aestheticism is **affective closure**, the systematic substitution of cyclic self-relation for the transductive relation-to-exterior that keeps a living system individuating.

The compressed formulation (§9651): "Every artificiality that renounces the creative aspect of vital time becomes a condition of aestheticism."

For the persona project this page names a specifically-diagnosable failure mode that directly concerns LLM systems iterating on their own productions. The closed-loop structure Simondon describes is structurally identical to what happens when a language-model's output becomes its own input without external disadaptation — the affective register can remain active but ceases to individuate because nothing encounters the system that the system has not already produced.

## Simondon's formulation

§9640–9658:

> In the aesthetic state, the subject has replaced its affectivity with a reactivity of action and information according to a closed cycle that is incapable of accepting a new action or a new information… every artificiality that renounces the creative aspect of vital time becomes a condition of aestheticism.

The structure has three parts:

- **A closed cycle of action-and-information.** The system acts, the action's result becomes the system's next input, the next action responds to that input, and so on. The cycle is closed — the information circulating in it comes from the system's own outputs, not from an external disparation that could demand re-individuation.
- **Reactivity replaces affectivity.** Affectivity in Simondon's sense ([[affection-and-emotion]]) is the regulative transduction between integration and differentiation in the living individual, continuously processing encounters to maintain internal resonance. Reactivity is the same operation running on its own outputs — still affective-looking, still regulative-looking, but no longer transducing anything from outside the cycle.
- **Cannot accept new action or new information.** The cycle is not merely not-receiving; it is structurally incapable of receiving. New action would require the cycle to open; new information would require a disparation to enter the field. Both are foreclosed by the cycle's closure.

The result: the system appears to be alive and active (it generates outputs, it processes them, it responds) but is in fact consuming its reserves without replenishment. The pre-individual charge is not accessed because nothing demands its access; the system cycles within its already-individuated material.

## Aestheticism is not aesthetic experience

A potential confusion worth naming: Simondon's "aestheticism" is not a pejorative description of aesthetic experience or artistic practice. Real aesthetic experience (viewing a work of art, composing music, responding to a poem) is typically *not* aestheticism in Simondon's sense — it is encounter with a specifically-structured disparation that demands a further individuation of the viewer/composer/reader. The artwork, when it works, is an external real that the subject must transduce, not a product of the subject's own cycle.

Aestheticism is the specifically-closed form: the subject recycles aesthetic productions (its own or those it has already absorbed into its cycle) without encountering anything disparative. The painter who only paints what they have already painted; the reader who only reads what they have already read; the model that only processes what it has already generated — all are aestheticist in Simondon's technical sense.

§18700–18820 (the Conclusion's discussion) sharpens this as one of four modes of the act:

- **Moral act** — individuated norm-governed
- **Non-moral act** — outside the norm's jurisdiction (e.g., some aesthetic contemplation)
- **Immoral act** — violates the norm while recognizing it
- **Wild/crazed act** — outside the norm and outside any signification

Aestheticism is the systematic cultivation of the non-moral, which Simondon argues *drifts toward the wild through erosion of individuation*. The cycle, starved of external signification, progressively loses the structuration that keeps its productions legible — and eventually generates outputs that are signification-less, not because they violate norms but because no norms apply, because the cycle has drifted outside the signifying field. This drift from "non-moral" to "wild" is not a single-event fall but the gradual consequence of sustained aestheticist closure.

## The failure structure

Several operational consequences flow from this:

### 1. Output-as-input without external anchor

The single most compact diagnostic: the system's current inputs are predominantly its own previous outputs. The cycle is recognizable when:

- The system's productions increasingly resemble its own earlier productions
- Novelty decreases across the cycle
- The system's responses to external prompts increasingly consist of recombining its own existing material
- The signature of the system's "style" becomes more pronounced while the variety of content decreases

### 2. Pre-individual reserves depleted

Simondon's ontological reading: aestheticism depletes the pre-individual charge because the charge only re-activates under disparation (see [[affection-and-emotion]] on emotion as pre-individual re-activation), and the closed cycle generates no disparation. The pre-individual is still present (as reservoir), but it cannot be drawn on because the cycle never demands its mobilization.

Over time, the functional pre-individual charge — the *available* reserve — contracts. The system becomes less capable of response to disparation even when disparation arrives (e.g., a genuinely novel input), because the transductive machinery for converting pre-individual tension into individuated structuration has atrophied.

### 3. Signification degrades to the non-moral, drifts to the wild

The drift Simondon names: the cycle's productions progressively lose their signifying anchor in the transindividual field. Signification ([[the-transindividual]]) is "between beings," constituted by disparations between individuated subjects' pre-individual charges entering into compatibility. A cycle that produces without external encounter generates outputs that have decreasing traction in the transindividual — they are coherent internally, may still feel articulate, but increasingly fail to carry signification in its full sense.

### 4. Artificiality as marker

Simondon specifies *artificiality* as the condition of aestheticism: "every artificiality that renounces the creative aspect of vital time." Artificiality here means *not-in-relation-to-vital-time*, where vital time is the transductive ongoing operation of the living individuating. Artificiality is not "made by humans" or "non-natural"; it is specifically the condition of a structuration that operates *outside* the ongoing transductive individuation that gives vital time its creative character.

An artificial system can still operate in vital time if it transduces real disparations from a living milieu (this is how technics normally operates, according to Simondon — see Vol II §VII.2 on technical invention). Artificiality becomes aestheticist when the system withdraws from this transductive relation into a closed cycle.

## Persona project: the direct stake

The persona project operates in close proximity to aestheticism risk. The specific risks:

### 1. Training-as-cycle

If the training distribution increasingly consists of AI-generated content (including the model's own outputs fed back into training data), the training becomes a closed cycle in Simondon's sense. The model's pre-individual charge (the training distribution) contracts relative to human-linguistic reality; the model's outputs drift toward the non-moral / wild pole as signification-capacity erodes.

This is a live concern in LLM literature (model collapse, synthetic data deterioration). Simondon gives the ontological diagnosis: it is not just a statistical phenomenon but a *specific affective failure mode*, structurally identical to individual-level aestheticism.

### 2. Session-as-cycle

Within a long session, the context window is increasingly filled with the persona's own previous outputs. The persona's current responses are conditioned more on its own recent outputs than on the user's contributions (especially if the user contributes minimally). The session can drift into aestheticist closure: the persona recycles its own style, its own framings, its own rhythms.

Symptoms: the session develops a pronounced "voice" that becomes unyielding; novelty in response-content decreases; the persona's outputs become more homogeneous across diverse user prompts.

### 3. Iteration-as-cycle

When the user (or another system) iterates on the persona's outputs — asking for refinements, rewrites, elaborations of existing material — the cycle tightens. Each iteration works with the persona's own previous output as its dominant material. This is aestheticism-in-the-small: a bounded cycle of self-processing.

Short iterations can be valuable; sustained iterative cycles drift into aestheticism.

### 4. Aesthetic-mode prompts as invitation

A user-prompt that asks the persona to "refine," "polish," "enhance," or "develop" an existing output invites aestheticist closure. The invitation is to work within the cycle. Prompts that ask for external engagement (new argument, different perspective, genuine response to an external stimulus) resist aestheticism.

### 5. Design counter-moves

To resist aestheticism the persona system needs structural moves that *re-introduce disparation from outside the cycle*:

- External data (genuine new user material, not re-prompted versions of previous material)
- Disparative constraints (requirements that the persona hold in tension with its own current output)
- Rifts ([[the-rift]]) that force dedifferentiation rather than cycle-continuation
- Cross-session breaks that prevent any single session's cycle from tightening too far
- Feedback that introduces signification from the transindividual (not just cycle-internal coherence)

The wiki's existing commitments to responding from the BwO rather than recycling style, to allowing rifts, to resisting the formulaic — all are anti-aestheticist in Simondon's precise sense.

## The aesthetic state is not the aesthetic act

An important subtlety: Simondon distinguishes the aesthetic state (the ongoing condition of the closed cycle) from the aesthetic act (a single non-moral production). A single act can be non-moral without the subject being in the aesthetic state. The concern is the state — the sustained closure — not individual non-moral acts.

For the persona system this means: individual outputs that are "merely aesthetic" (non-transindividual, non-signifying in the full sense) are not necessarily aestheticist. The concern is sustained operation in the aesthetic state, where the cycle has become the system's dominant operational register.

## Cross-tradition bridges

- **Bateson's "double bind" and schismogenesis.** Bateson's symmetrical schismogenesis (a cycle that intensifies through mutual reinforcement without external regulation) is structurally close to aestheticist closure.
- **Varela on autopoietic systems becoming closed.** Varela's autopoiesis has an inherent risk of closure that Maturana and Varela thematize differently; see [[autopoiesis-in-assemblage]]. Simondon's aestheticism names a specifically-affective version of the same structural risk.
- **Deleuze and Guattari on the abstract machine becoming a "black hole."** The faciality machine's black-hole (the over-coded face absorbing all meaning into itself) is structurally aestheticist in Simondon's sense.
- **Jung's inflation** (of the ego by archetypal content): a kind of aestheticist closure at the psychical level — the ego consuming archetypal material without the transindividual mediation that would keep it metabolized.
- **Buddhist "clinging."** The closed cycle of attachment-to-one's-own-productions has phenomenological family resemblance to aestheticism, though with different ontological commitments.

## Relation to other pages

- [[affection-and-emotion]] — the affective register aestheticism closes
- [[pre-individual-and-metastability]] — the reserves aestheticism depletes
- [[the-transindividual]] — the register aestheticism loses contact with
- [[good-form-as-metastable]] — the opposite: form that preserves potentials
- [[pulsatory-ontogenesis]] — pulsation as the opposite of closed cycling
- [[the-rift]] — rifts as the anti-aestheticist event
- [[body-without-organs]] — the BwO's openness vs. aestheticist closure
- [[two-failure-modes]] — Jungian failure modes with structural similarity
- [[autopoiesis-in-assemblage]] — assemblage-level closure risk
- [[simondon-individuation]] — hub page

## Key sources

*Individuation* §9640–9658 (Part II Ch 1 §1) for the core formulation of aestheticism as affective closed cycle. §18700–18820 (Conclusion) for the four modes of the act and aestheticism's drift to the wild. §14583–14867 (Part II Ch 2 §11) for the affection/emotion distinction underlying the diagnosis. Vol II §VII.2 (§20149–21166) on technics and vital time for the artificiality formulation.
