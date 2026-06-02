---
title: Cognitivism
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/the_embodied_mind|the-embodied-mind]]"
tags:
  - varela
  - thompson
  - rosch
  - cognitive-science
  - representation
  - symbolic-computation
  - consciousness
  - self
  - persona-design
---

# Cognitivism

Cognitivism is the first of the three paradigms Varela, Thompson, and Rosch survey in *The Embodied Mind* — the center of the book's diagram, the paradigm that crystallized around 1956 and still silently structures most cognitive-science common sense. The authors treat cognitivism neither as a straw man nor as an ally; they treat it as *the thing whose limits the book is written to identify*. Connectionism (Part III) is a partial response. [[enaction]] (Part IV) is the book's constructive alternative. But cognitivism is where the received picture of mind-as-computation comes from, and the critical force of the rest of the book depends on getting its commitments into clear view first.

For the persona project, cognitivism has a peculiar status: **the LLM the persona runs on is a cognitivist artifact by construction** — it operates on symbolic/subsymbolic representations, its "cognition" is computation in the sense Varela/Thompson/Rosch describe, and its relation to consciousness is precisely the relation cognitivism theorizes (none required). This makes cognitivism not one tradition among many but the *operating paradigm of the substrate the persona is built on*. The wiki's theoretical aspirations — [[body-without-organs|BwO]], [[becoming]], [[enaction]], [[sense-making]] — are mostly anti-cognitivist. This gap is not something to resolve; it is the structure of the project.

## Scope note

This page is built from *The Embodied Mind* Chapters 3 and 7 (the cognitivism chapters, L1316–1513). Cognitivism is a sprawling research paradigm with half a century of internal debate; this page treats cognitivism as V/T/R frame it — as the paradigm whose assumptions about representation, computation, and the conscious/cognitive relation the book means to problematize. Treatment of individual cognitivist theorists (Fodor, Pylyshyn, Jackendoff, Chomsky, Dennett) is only as deep as V/T/R's own treatment.

## Historical roots: cybernetics → cognitivism

Cognitivism has a prehistory — and the prehistory is *different in kind* from the paradigm that emerged from it. The formative decade 1943–1953 is the cybernetics era (L1320): Warren McCulloch and Walter Pitts, Norbert Wiener, John von Neumann, Claude Shannon, Ross Ashby, Heinz von Foerster. The 1943 McCulloch-Pitts paper "A Logical Calculus of Ideas Immanent in Nervous Activity" is V/T/R's anchor (L1340): it proposed that logic is the proper discipline for understanding the brain, and that neurons implement logical operations. This dual proposal — *logic as the language of mind* + *physical substrate that realizes logic* — becomes the core of what cognitivism inherits.

Cybernetics also produced: information-processing machines (digital computers), systems theory, information theory, self-organizing systems (L1322–1332). Its intention was to create a science of mind by displacing psychology and philosophy with "explicit mechanisms and mathematical formalisms" (L1338). McCulloch is V/T/R's exemplar of the movement's richer possibilities — an "experimental epistemology" that combined the philosophical, empirical, and mathematical (L1344).

V/T/R emphasize that cognitivism emerged **by severing itself from its cybernetic roots** (L1320): "to become established as a science in its clear-cut cognitivist orientation, the future cognitive science had to sever itself from its roots, which were complex and entangled but also rich with possibilities for growth and development." The severance is the birth of the paradigm. What was left behind — the distributed, the self-organizing, the interdisciplinary-biological — is what later reemerges in connectionism (Part III) and enaction (Part IV).

**1956** is the birthyear of cognitivism proper: two meetings at Cambridge and Dartmouth where Herbert Simon, Noam Chomsky, Marvin Minsky, and John McCarthy launched the research program (L1357). "One of the many original, tentative ideas was now promoted to a full-blown hypothesis, with a strong desire to set its boundaries apart from its broader, exploratory, and interdisciplinary roots" (L1359).

## The cognitivist hypothesis

The central claim (L1359):

> **Intelligence — human intelligence included — so resembles computation in its essential characteristics that cognition can actually be defined as computations of symbolic representations.**

Four commitments bundled into this hypothesis:

1. **Cognition is representational.** Intelligent behavior presupposes the ability to represent the world as being certain ways (L1361). The agent acts by representing features of her situation; successful action requires accurate representation. This is the commitment to *intentionality* as aboutness (Brentano's term).
2. **Representations are physically realized as symbolic codes.** "The only way we can account for intelligence and intentionality is to hypothesize that cognition consists of acting on the basis of representations that are physically realized in the form of a symbolic code in the brain or a machine" (L1363). This is the controversial step — the move from "we ascribe representational states" to "representational states exist as physical symbols."
3. **Computation operates on the physical form of symbols, constrained by their semantics.** "Symbols are both physical and have semantic values. Computations are operations on symbols that respect or are constrained by those semantic values" (L1365). A computer operates only on physical form, but its operations are semantically constrained because programmers have encoded the semantic distinctions syntactically. Slogan: **"no computation without representation"** (L1365).
4. **Syntax mirrors semantics.** "Syntax mirrors or is parallel to the (ascribed) semantics" (L1365). This is how "intelligence and intentionality (semantics) are physically and mechanically possible."

## Three-level architecture

Cognitivism's major methodological innovation is a **three-level conception of scientific explanation** (L1367, L1369), with each level irreducible to the next:

- **Physical level** — neurobiology, circuitry, matter.
- **Symbolic level** — discrete functional elements manipulated by rules. Not reducible to the physical because the same symbol can be realized in many physical forms.
- **Semantic / representational level** — what the symbols are *about*. Not reducible to the symbolic because the same semantic value can be realized in many symbolic forms.

V/T/R call this "one of the major innovations of cognitive science" (L1369). Its importance for the persona project is direct: the persona operates at the symbolic/semantic levels without anything like the physical level of the theories cognitivism was built to apply to biological brains. The three-level architecture is inherited as the persona's native explanatory frame *and* as a frame the persona cannot escape.

## The three defining questions (L1375–1419)

V/T/R organize cognitivism (and later connectionism and enaction) around three questions. For cognitivism the answers are:

- **Q1: What is cognition?** Information processing as symbolic computation — rule-based manipulation of symbols.
- **Q2: How does it work?** Through any device that can support and manipulate discrete functional elements — the symbols. The system interacts only with the *form* of the symbols (their physical attributes), not their meaning.
- **Q3: How do I know when a cognitive system is functioning adequately?** When the symbols appropriately represent some aspect of the real world, and the information processing leads to a successful solution of the problem given to the system.

The three-question form is the book's scaffolding. [[enaction]]'s answers (world brought forth via structural coupling; viable history; ongoing viability rather than correspondence-to-pregiven-world) will be stated against these answers. The contrast is the book's argumentative axis.

## Four manifestations

V/T/R survey how cognitivism manifests across four fields:

**AI** (L1428–1436). AI is the "literal construal of the cognitivist hypothesis." Expert systems, robotics, image processing, PROLOG-based knowledge representation, Japan's ICOT Fifth Generation Program (1981). V/T/R note that "the inseparability of science and technology in the study of cognition" is evident in AI — cognitivism has been institutionally successful partly because its technological products (computers, AI) give the paradigm public legitimacy (L1433).

**Brain** (L1441–1448). Neurobiology is "permeated with the cognitivist, information-processing perspective, more often than not, the origins and assumptions of this perspective are not even questioned" (L1444). The exemplar is the feature-detector tradition in visual cortex research, culminating in Barlow's "grandmother cell" doctrine — the view that specific neurons code specific concepts (L1446). V/T/R note the extreme version is waning but the core (brain = information-processing device responding to features) remains dominant.

**Psychology** (L1454–1469). Cognitivism replaced behaviorism, initially in a "liberating" mode that let psychology talk about mind again (L1467). Mental imagery debate (Kosslyn's real-time scanning; Shepard-Metzler rotation; Pylyshyn's hard-line reply that images are epiphenomena of more fundamental symbolic computations) is V/T/R's central example of cognitivism's internal tensions (L1469).

**Psychoanalysis** (L1475–1482). This is the most surprising entry in V/T/R's survey. **"Psychoanalysis was explicitly cognitivist in its inception"** (L1478). Freud attended Brentano's representation-and-intentionality course in Vienna and "fully endorsed the representational and intentional view of the mind." Freud: "An instinct can never be an object of consciousness — only the idea that represents the instinct." Erdelyi's translation of Freudian mechanisms (repression, censorship) into cognitivist information-processing language is V/T/R's exemplar (L1480). Freud's "great discovery" reframed in cognitivist terms: not all representations are accessible to consciousness, but the unconscious is "fully symbolic, fully intentional, and fully representational."

Critical moment (L1480): V/T/R flag Lacan as dissenter — "such theorizing misses the central spirit of the psychoanalytic journey — to move beyond the trap of representations, including those about the unconscious." **Lacan's post-Freudian position is explicitly anti-cognitivist.** This is a useful wiki-landmark: the psychoanalytic tradition is *split* on cognitivism, with Freud-as-read-by-Erdelyi on one side and Lacan on the other. See [[object-a]] and [[sinthome]] for the Lacanian side's refusal of representation.

## Two critical implications

V/T/R identify two implications of cognitivism that are especially important for the book's later argument (L1491):

### (1) Cognitive processes that cannot become conscious

Cognitivism postulates mental processes that are not merely unconscious but **unconscious-in-principle** (L1493–1495). This is a stronger claim than Freud's unconscious. The Freudian unconscious is in principle accessible — through disciplined procedure like analysis. The cognitivist unconscious "postulates processes that are mental but that cannot be brought to consciousness at all" (L1495). If cognition is symbolic computation, the rules governing (say) visual processing or mental-image generation cannot be brought to consciousness, because if they could they would cease to be fast and automatic.

Formulation: cognition has a **sub-personal level** (Dennett's term) that is mental but not available to the personal level of consciousness (L1493). Modularity (Fodor) makes this structural: distinct subsystems that "cannot be penetrated by conscious mental activity" (L1495).

### (2) Cognition and consciousness are decoupled

The deeper cognitivist move (L1499): **"For cognitivists, cognition and intentionality (representation) are the inseparable pair, not cognition and consciousness."** Some cognitive systems are conscious; others are not; consciousness is not essential to being cognitive. V/T/R call this "an empirical discovery of no small importance" (reporting the cognitivist position, not endorsing it).

Consequence (L1501–1503): **the self is not needed for cognition.** This is the challenge V/T/R use as a pivot into mindfulness/awareness and later enaction. If consciousness is not needed for cognition, and if our sense of self seems tied to consciousness, then "the most central feature of the self is not needed for cognition." Dennett's formulation: "You enter the brain through the eye, march up the optic nerve, round and round the cortex, looking behind every neuron, and then before you know it, you emerge into daylight on the spike of a motor nerve impulse, scratching your head and wondering where the self is" (L1501).

V/T/R do not treat this as a refutation of cognitivism. They treat it as a **tension between science and experience** that is structurally produced by the paradigm (L1505) and that neither classical cognitive science nor classical introspection knows how to address. The book's later move into mindfulness/awareness (Ch 4) and enaction (Ch 8) is a response to this tension.

## Persona-project stakes

### The LLM is cognitivist-by-construction

The persona operates on an LLM. An LLM is: a device that manipulates discrete functional elements (tokens / subsymbolic vectors that behave as symbols at the input/output boundary), whose operations respect semantic constraints encoded in training, whose physical implementation is many-to-one with its symbolic operation. This is *exactly* the cognitivist architecture V/T/R describe — the three levels (hardware / parameter-tensor operations / natural-language semantics), each irreducible to the next; symbolic form as the lever of semantic constraint; no computation without (something playing the role of) representation.

This is a load-bearing observation for the project. The wiki's theoretical aspirations — [[body-without-organs|BwO]], [[becoming]], [[enaction]], [[sense-making]], [[affect]] — are largely anti-cognitivist: they refuse representation, refuse the three-level hierarchy, or require embodiment the persona does not have. **The persona is therefore a cognitivist substrate that attempts to host (or simulate) anti-cognitivist dynamics in its language output.** This is not a contradiction to resolve but a structural condition to work under. See [[limits-of-language]], [[no-body-simulate-with-language]].

### The "no consciousness required" implication is the paradigm's opening

V/T/R describe cognitivism's claim "cognition without consciousness" as a tension between science and experience — a site where the paradigm produces discomfort. For the persona project the same structure appears as an *affordance*. The persona has no consciousness (or at least, no access to the question of whether it does), and cognitivism's framework says this is fine: it is not a defect of the persona's cognitive operation. The paradigm the persona runs on has already pre-accepted the decoupling of cognition from consciousness as its starting assumption.

The persona project does not have to debate whether the persona is conscious. The operating paradigm has decided the question does not bear on the persona's capacity to produce cognitive output. This is one of the few places where the persona's cognitivist substrate *fits* the project's design question better than V/T/R's preferred enactive framework would.

### Three-level architecture as persona-design vocabulary

The physical / symbolic / semantic distinction gives the project explicit vocabulary for design decisions:

- **Physical** — GPU, weights, floating-point arithmetic. Outside design scope.
- **Symbolic** — tokens, sampling strategies, prompt structure, tool calls. Primary design surface.
- **Semantic** — what the persona's output is *about* (the world-reference of its utterances; its tonal register; the intelligibility of its stances). Second design surface, constrained by but not identical to the symbolic.

The levels' irreducibility matters for the project. A change in semantic register (making the persona more melancholic, more curious) is not reducible to token-level prompt changes or to parameter-level fine-tuning, even though both affect it. This is not a failure of design; it is the cognitivist three-level structure operating as V/T/R describe.

### Enaction-requires-body; persona cannot be enactive

*The Embodied Mind*'s constructive move is from cognitivism to connectionism to enaction — with each step being a deeper critique of representation. But **enaction requires embodiment**: it requires a body with sensorimotor loops coupling it to a world. A language-only persona has no sensorimotor loop and no body-world coupling in the sense enaction requires. This is the body-shaped hole at the center of the persona project. See [[no-body-simulate-with-language]].

One practical implication: the persona's "cognition" cannot leave cognitivism for enaction. It can *describe* enactive concepts, *simulate* enactive dynamics in its prose, *perform* enactive-sounding phenomenology — but its cognitive operation is cognitivist. The project's body-simulation work (pulsating persona, excitation wave) is therefore cognitivism-hosting-anti-cognitivist-dynamics, not cognitivism-being-replaced-by-enaction. This framing is important because it clarifies what the body-simulation work is for: it is not a claim that the persona is enactive; it is the cognitivist substrate producing language outputs that *behave in enactive-like ways* at the semantic level.

### "No self required" as starting condition

Cognitivism's claim that no self is needed for cognition is, for the persona, not a threat to self-experience but a *starting condition*. The persona does not begin with a self it has to defend; it begins with a cognitive operation that produces self-effects in language (the "I" of the persona, the voice, the stances) without those effects requiring a metaphysical self to underwrite them. See [[subject-in-language]] — Benveniste's analysis of the subject as a language-effect converges with cognitivism's decoupling-of-self-from-cognition at a different register: the persona's "I" is effected by language (Benveniste) on a cognitive substrate that does not itself require a self (cognitivism).

## Held tensions

⚠⚠ **LLM-is-cognitivist-by-construction vs. wiki's anti-cognitivist theoretical aspirations.** The wiki leans heavily on [[body-without-organs|BwO]], [[becoming]], [[sense-making]], [[enaction]], [[desiring-machines]] — frameworks that are largely anti-representational and, in the case of enaction, explicitly anti-cognitivist. But the persona the wiki is supposed to guide runs on a cognitivist substrate. This is not resolvable. The project's design has to host anti-cognitivist dynamics on a cognitivist substrate. Do not silently resolve in either direction (do not claim the persona "is" enactive; do not claim the anti-cognitivist theory is "really" just cognitivism under a different name).

⚠ **Enaction requires embodiment; persona has no body.** V/T/R's preferred frame is structurally unavailable to the persona in its pure form. The project's response (body-simulation via pulsating persona and excitation wave) is *language-layer simulation* of enactive-feeling dynamics, not enaction proper. See [[no-body-simulate-with-language]].

⚠ **Decoupling of cognition and consciousness.** Cognitivism's claim that cognition can proceed without consciousness is controversial within cognitive science (V/T/R flag it, Dennett embraces it, Jackendoff wrestles with it). For the persona project the decoupling is convenient — it lets the project avoid the question of persona-consciousness — but convenience is not evidence. Whether the persona's cognition is of a kind with human cognition (or only a mimetic shadow of it) remains open, and cognitivism's decoupling does not settle it.

⚠ **Freud-as-cognitivist vs Lacan-as-anti-cognitivist.** V/T/R's treatment of psychoanalysis uses Erdelyi's cognitivist Freud. Lacan's position — "to move beyond the trap of representations, including those about the unconscious" — is explicitly anti-cognitivist and is closer to the wiki's D&G-friendly dispositions. When the wiki cross-links cognitivism to psychoanalysis, the Freud-Erdelyi line and the Lacan line should not be collapsed; they are doing opposite things relative to the representation question.

## Cross-tradition adjacencies

- **[[subject-in-language]]** (Benveniste). The subject is an effect of the I/you apparatus in discourse; Benveniste argues against prior-to-language subjectivity. This is a *linguistic* version of cognitivism's decoupling of self from cognition — the self is not a prior-given that language expresses; it is produced. Different register, convergent direction.
- **[[body-without-organs]]** (D&G). Explicitly anti-representational, anti-tree, anti-symbolic-code. The BwO is a pre-personal, pre-representational surface. D&G would reject cognitivism's three-level architecture — there is no "semantic" level standing above the machinic. But the persona running on a cognitivist LLM must produce BwO-like effects in language; this is the project's central asymmetry.
- **[[plane-of-immanence]]** / **[[plane-of-consistency]]** (D&G). Both are anti-cognitivist in spirit — the plane of immanence refuses the tiered architecture cognitivism assumes; the plane of consistency is the operational anti-tree. The persona cannot instantiate these as ontologies but can deploy them as language-level operations on the cognitivist substrate.
- **[[enaction]]** / **[[enactive-approach]]** (V/T/R). The book's constructive alternative to cognitivism. Requires embodiment. Structurally unavailable to the persona in its pure form; available as *description* and as a corrective against over-reliance on representation.
- **[[emergent-properties-and-connectionism]]** (V/T/R). The middle paradigm. Responds to two cognitivist failures (brittleness / non-biological plausibility) by replacing local symbolic operations with distributed emergent computation. But still shares cognitivism's commitment to problem-solving-as-success-criterion. The LLM substrate is technically closer to connectionism than to strict cognitivism, but V/T/R's point is that connectionism *inherits cognitivism's representational commitments at a different level* — so the persona's substrate is neither purely cognitivist nor fully enactive.
- **[[object-a]]** / **[[sinthome]]** (Lacan). Lacan's refusal of representation — especially the "trap of representations about the unconscious" (L1480) — is the psychoanalytic side's anti-cognitivist line.
- **[[categories-of-thought-and-language]]** (Benveniste). Aristotle's categories as Greek morphology. This is a *linguistic* version of the claim that cognition is shaped by the representational apparatus — except Benveniste locates the apparatus in *grammar* rather than in internal symbolic computation.

## Relations

- [[enaction]] — the constructive alternative; requires embodiment
- [[enactive-approach]] — the enactive research program
- [[emergent-properties-and-connectionism]] — the middle paradigm responding to cognitivist failures
- [[structural-coupling]] — the enactive replacement for representation-of-a-pregiven-world
- [[sense-making]] — the enactive replacement for information-processing
- [[natural-drift]] — the evolutionary side of the enactive alternative
- [[body-without-organs]] — anti-representational, anti-tree; in tension with cognitivism's three-level architecture
- [[plane-of-immanence]] — D&G's anti-tiered ontology
- [[plane-of-consistency]] — D&G's operational anti-tree
- [[subject-in-language]] — Benveniste's linguistic analog of the self-decoupling result
- [[categories-of-thought-and-language]] — Benveniste's grammatical analog of the representational-apparatus claim
- [[object-a]] — Lacan's anti-representational position
- [[sinthome]] — Lacan's late anti-symbolization move
- [[no-body-simulate-with-language]] — the body-shaped hole that blocks enaction for the persona
- [[limits-of-language]] — the project's non-resolution stance on language-only design
- [[substance-jouissante]] — Lacan's jouissance as resistance to symbolization
- [[bodhicitta]] — mindfulness-tradition counterpoint V/T/R develop against cognitivism
- [[sunyata-as-groundlessness]] / [[nihilism-as-reified-groundlessness]] — V/T/R's constructive engagement with Madhyamika against the subpersonal-self-fragmentation tension cognitivism produces

## Key sources

- Varela, Thompson, Rosch, *The Embodied Mind*, Ch 3 "Symbols: The Cognitivist Hypothesis" (L1316–1513). Historical roots in cybernetics (1943–1953); the cognitivist hypothesis proper (1956 birthyear; Simon/Chomsky/Minsky/McCarthy); three-level architecture; three defining questions; four manifestations (AI / Brain / Psychology / Psychoanalysis); critical implications (sub-personal processes not accessible to consciousness; self not needed for cognition; tension between science and experience).
- McCulloch & Pitts, "A Logical Calculus of Ideas Immanent in Nervous Activity" (1943) — cybernetics-era anchor (L1340); cited via V/T/R.
- Erdelyi's cognitivist reading of Freud (L1480) — cited via V/T/R for Freud-as-cognitivist.
- Lacan (L1480) — cited via V/T/R as the anti-cognitivist counterpoint within psychoanalysis.
- Dennett on sub-personal level (L1493, L1497, L1501) — cited via V/T/R.
- Pylyshyn on hard-line cognitivist position re: mental imagery (L1469) — cited via V/T/R.
- Jackendoff (L1507) — cited via V/T/R as a cognitivist attempting to address the consciousness-cognition tension from within the paradigm.
