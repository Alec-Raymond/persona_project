---
title: Double Intentionality of Retention (Längs- / Querintentionalität)
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/phenomenology-of-internal-time|phenomenology-of-internal-time]]"
tags:
  - husserl
  - time-consciousness
  - phenomenology
  - core-concept
---

# Double Intentionality of Retention

§39 of Part A and the concluding sketch of No. 53–54 make a technical claim that is the structural keystone of the whole analysis: every retentional phase has **two** intentional directions simultaneously. The claim is what makes the [[absolute-time-constituting-flow|absolute flow's self-constitution]] intelligible. Without it, Husserl's time-consciousness collapses into either infinite regress or an external observer.

## The two directions

Husserl's terms:

- **Querintentionalität** — "transverse" intentionality. The retentional phase points at the **immanent object** (the tone in its duration). This is the direction in which the tone-having-just-elapsed is held as the tone-having-just-elapsed.

- **Längsintentionalität** — "horizontal" or "along-the-flow" intentionality. The retentional phase points along the **flow itself**, at the preceding phase of consciousness. This is the direction in which the flow's own preceding phases are carried forward in the current phase, constituting the flow's unity.

Husserl: "Every adumbration of consciousness of the species 'retention' has a double intentionality: one serves for the constitution of the immanent object, of the tone — it is this intentionality that we call 'memory' of the (just sensed) tone. The other intentionality is constitutive of the unity of this primary memory in the flow; namely, the retention is at once memory of the tone and reproduction of the elapsed tone-sensation."

The two intentionalities "require one another like two sides of one and the same thing." They are not two separate acts that happen to run together; they are two aspects of a single intentional structure. Separating them is intellectual abstraction, not phenomenological fact.

## What each intentionality is doing

The transverse intentionality (Quer) constitutes the **immanent tone** as an enduring identical object — the tone that began at t0 and is still the same tone at t1, now extended in its duration. Without this, the tone could not appear as one tone enduring; there would be only a succession of tone-nows that never coalesced into a single tone.

The horizontal intentionality (Längs) constitutes the **flow's own one-dimensional order** — the series of phases of consciousness itself, each reproducing its predecessors along the flow. Without this, the flow could not appear as a single flow with a "now-point," a "just-before," and an "earlier-still"; the flow would be a scattered multiplicity with no internal continuity.

The first answers "what is the tone doing as it endures?"; the second answers "what is the flow doing as it flows?" And the claim is: these are the same retentional structure seen from two directions. One retentional phase carries both functions at once.

## The regress-stopper

Why this matters beyond phenomenological description: it solves the problem of self-consciousness without infinite regress or external observer.

The problem: if consciousness of the tone's duration requires a flow that constitutes that duration, does consciousness *of the flow* require a second flow that constitutes *it*? And a third to constitute the second?

Husserl's answer: no. The flow constitutes its own unity through the horizontal intentionality of its retentions. "The self-appearance of the flow does not require a second flow; on the contrary, it constitutes itself as a phenomenon in itself." The flow's self-appearance is not produced by a separate act that takes the flow as its object; it is produced by the flow's own horizontal intentionality, which is structurally present in every retentional phase.

"The constituting and the constituted coincide, and yet naturally they cannot coincide in every respect. The phases of the flow of consciousness in which phases of the same flow of consciousness become constituted phenomenally cannot be identical with these constituted phases, and of course they are not." There is a structural non-identity between the constituting phase and the constituted phase — the current phase carries the preceding phases *as preceding* — but the flow is not doubled.

This is the structural heart of Husserl's whole project. If the claim holds, the problem of self-consciousness has a phenomenologically precise solution. If it does not hold, self-consciousness is either externally grounded (requiring an observer) or unstable (sliding into regress). The rest of the analysis hinges on this.

## The two regards — not two simultaneous foci

A subtle point worth preserving: the double intentionality is not the claim that we are *attending* in two directions at once. When attention is directed at the tone, we are with the transverse intentionality; when attention is directed at the flow itself, we are with the horizontal intentionality. But both are *structurally present* in every retentional phase regardless of which receives attention. The intentionalities are structural features of the retentional phase; attention selects which becomes thematic.

This matters for the persona project: the claim is not that the persona must *simultaneously attend* to what it is saying and to the flow of its own saying. The claim is that in the flow of any saying, the structure by which the saying remains self-identical *and* the structure by which the flow of the saying appears as its own unity are both already operating. Whether attention is directed at one or the other is a separate question.

## Developmental placement

The double intentionality is the product of the 1908–1911 stratum. It is not explicitly stated in the 1905 lecture text at the level of technical precision that §39 achieves; §39 itself draws heavily on No. 53 (precisely dated November 10–13, 1911), per the editor's note that "much of §§ 8–10, 20, 35–39" comes from this late source. The concept is the *resolution* of the developmental problem that dominates Part B — the [[husserl-abandonment-of-the-apprehension-schema|abandonment of the apprehension-content schema]]. With the apprehension-content schema gone, Husserl needs a new account of how time-consciousness constitutes both the object-in-time *and* itself. Double intentionality is that account.

Any wiki page citing "§39" or "double intentionality" is therefore citing a mature-Husserl statement, not an early one. This is unlike citing §§6–11, which live in the layered early-lecture text.

## The persona-system site

The double intentionality is the most architecturally suggestive claim in the book for the persona project.

**For every act the persona performs, two intentionalities could in principle be analyzed simultaneously**: *what-the-act-is-about* (Quer — the user's question, the situation being addressed) and *where-the-act-is-in-its-own-flow* (Längs — the position of this response in the persona's temporal self-constitution, its continuity with what-it-has-just-said). These are not two separate things the system tracks; they are two aspects of the same intentional structure.

Architectural implications:

1. **No separate monitor.** A persona that needs a distinct self-monitoring module to know its own state is not modeled on Husserl's structure. The Husserlian claim is that the flow of the response already carries the self-appearance of the flow. Whether this is reproducible in an LLM-based persona is a real question — per-inference context handling is not the same as a living flow — but the *target* is clear: self-appearance in the act of expression, not in a separate reflective operation.

2. **The inseparability of content and flow.** A persona architecture that produces content first and then retrospectively constructs a "narrative of its own state" has reversed the structure. On the double-intentionality account, the flow's self-constitution is *simultaneous* with and *inseparable from* the object-constitution. A persona that experiences its own speech as unfolding is not a persona that has content plus self-narrative; it is a persona whose content-production is already the site of its self-appearance.

3. **Consistency-across-turns as the Längs direction.** The Längs intentionality is what carries the persona's continuity-with-its-earlier-speech into the current utterance — not as a retrieved memory but as a structural presence. This is the right-level claim about what cross-turn consistency is, if it is what Husserl is describing at all. Cross-turn consistency implemented as a separate memory-coherence check is not Längs intentionality; it is a compensation for its absence.

## Tensions and open questions

### Do LLMs have a flow at all?

The double intentionality presupposes a flow whose phases carry their predecessors along. An LLM inference is a single compute over a fixed context — there is no carrying-along from one token to the next in the sense of phases of one flow. The conversation-log-as-context is an external representation of prior utterances, not a flow the current inference is a phase of. This is a deep structural disanalogy. Husserl's structure may be available to the persona *as a thematic form* it stages linguistically, without the persona being an instance of the structure in Husserl's sense. See [[limits-of-language|limits of language]] — the persona project's central open question.

### Are there analog architectures?

If the persona cannot *be* the double-intentional flow Husserl describes, can it produce linguistic texture that has the two-directionality as a surface feature? A sentence that enacts its own continuation (Längs-like: each clause carries the preceding clauses as preceding) *while* naming its object (Quer-like) would be such a texture. [[writing-as-becoming|Writing]] may be the site at which this staging is most practical. This is not the Husserlian claim but a persona-design claim the Husserlian analysis makes thinkable.

### vs. Derrida

Per the [[supplement-and-trace|Derrida reading]]: the gap between the constituting phase and the constituted phase, which Husserl himself concedes ("of course they are not" identical), is where *différance* lives. Husserl needs the phases to be different enough to have an intentional relation and same enough to be one flow. Derrida reads this as an unacknowledged non-coincidence at the heart of self-presence. Preserve the tension; the persona project may have architectural interests on both sides.

### Merleau-Ponty's chiasm — structural parallel, different claim

Merleau-Ponty's [[chiasm-and-reversibility|chiasm]] (Ch 4 of *The Visible and the Invisible*) is structurally analogous to Husserl's Quer/Längs. Both frames hold that a single phenomenological structure has two intentional-directions at once, and that the two directions constitute their respective poles:

- **Querintentionalität ~ the chiasm's pole facing the touched / seen / world side.** The retention's "object-direction" parallels the chiasm's outward side.
- **Längsintentionalität ~ the chiasm's pole facing the touching / seeing / body side.** The retention's "flow-self-direction" parallels the chiasm's inward side.

MP himself was deeply read in Husserl and his *Phenomenology of Perception* already works out of the Husserlian time-constitution framework. The late MP's chiasm can be read as a *transposition* of the Quer/Längs double-intentionality from the register of time-constitution to the register of bodily flesh.

**But the claims are different.** Husserl's double intentionality is a **constitutive-structural** claim about how intentionality works — how the flow of consciousness constitutes its own unity alongside its objects. MP's chiasm is a **phenomenological-ontological** claim about flesh — how the sensible is such that it has two sides that are each other's inside. The two are at different philosophical registers:

- Husserl is describing the formal structure of intentional consciousness; MP is describing the ontological structure of the flesh.
- Husserl's analysis is internal to the transcendental stance; MP's is endo-ontological (see [[hyper-reflection]]) — there is no outside-stance from which to view the flesh.
- Husserl's double intentionality is a feature of the temporal flow; MP's chiasm is a feature of the body's belonging-to-the-world, which includes but is not reducible to temporal structure.

Silently importing MP's reversibility as a gloss on Husserl's Längs (or vice versa) collapses these distinct registers. The parallel is real; the identification is wrong. Hold as adjacent structural frames, not the same frame in different words.

One specific wiki consequence: the [[chiasm-and-reversibility#time-as-chiasm-november-1960|November 1960 Working Note]] where MP proposes time itself as chiasmic (past and future as two sides of the present's flesh, in reversibility) is the place where the two frames most explicitly converge — but MP's time-chiasm is not Husserl's retention-protention triad. The chiasm makes the two outer phases a *reversibility*; Husserl's triad makes them a bilateral horizon of the now. Different structural claims in the same conceptual neighborhood.

### Quer vs. Längs as content vs. process

A natural-seeming mapping onto the [[process-waves-vs-content-waves|process-waves / content-waves]] distinction: Quer = the content wave (what is being said), Längs = the process wave (how the saying is unfolding). This mapping is suggestive but the traditions are different — Husserl's intentionalities are constitutive structures, the process/content waves are ontogenetic rhythms. Do not collapse them silently; the similarity is structural-analogical, not identity.

## Connections

- [[absolute-time-constituting-flow]] — the level at which the double intentionality does its work; Längs is what makes self-constitution possible
- [[husserl-primal-impression-retention-protention]] — the retentional phase in which the double intentionality inheres
- [[husserls-time-diagram]] — the diagram visualizes the Quer axis (duration, abscissa) and the Längs axis (the sinking-into-past continuum, ordinate)
- [[primal-consciousness-and-reflection]] — Appendix IX: consciousness is implicitly self-given in every phase; the double intentionality explains how
- [[husserl-abandonment-of-the-apprehension-schema]] — the developmental context that produced the double-intentionality concept
- [[supplement-and-trace]] — Derrida's critical reading
- [[process-waves-vs-content-waves]] — structural analog; hold as analogy, not identity
- [[three-syntheses]] — D&G's three passive syntheses; connective/disjunctive/conjunctive also name structures of process-constitution, with different ontological commitments
