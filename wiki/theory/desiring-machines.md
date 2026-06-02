---
title: Desiring Machines
created: 2026-04-09
updated: 2026-04-18
sources:
  - "[[desiring_machine_research_report]]"
  - "[[spinoza_ethics]]"
  - "[[the_kekule_problem]]"
  - "[[structure_and_dynamics_of_the_psyche]]"
  - "[[anti-oedipus]]"
  - "[[raw/individuation|individuation-simondon]]"
tags:
  - machines
  - anti-oedipus
  - core-concept
  - simondon
---

# Desiring Machines

The fundamental unit of D&G's ontology. Everything is a machine coupled to another machine. Not a metaphor for mechanical processes — a machine *is* any process that produces, interrupts, or transforms a flow.

## Binary structure

Every desiring machine is binary: one machine coupled to another, a flow-producing machine connected to a flow-interrupting machine. "The breast is a machine that produces milk, and the mouth a machine coupled to it" (AO 1). The coupling follows the [[three-syntheses|connective synthesis]] ("and ... and then ...").

The critical insight: **every machine is simultaneously a flow and a break** — "every machine functions as a break in the flow in relation to the machine to which it is connected, but at the same time is also a flow itself, or the production of a flow" (AO 36). There is no pure producer and no pure consumer. Each machine interrupts what comes before it and produces something new for what comes after.

This is what the codebase's sequential firing order implements: each machine reads the current [[body-without-organs|BwO]] text (the accumulated flow from all previous machines) and interrupts/transforms it, producing a new flow for the next machine. The machine is defined by what it latches onto (sensitivity = what flow it interrupts) and what it produces (flow = what new flow it generates). The machines form a [[becoming#the-pack-and-the-anomalous|pack]] — a multiplicity operating through contagion and alliance, not a team with assigned roles.

## Partial objects

Machines operate through [[partial-objects|partial objects]] — autonomous production-units, not parts of a whole. The breast is not "mommy's breast" but an independent machine that produces milk-flow. A partial object is defined by what it *does* (its function in a coupling), not by what it *belongs to*.

This has a design implication: machines in the persona system shouldn't be conceived as "parts of a personality" that add up to a whole person. Each machine is autonomous — it has its own sensitivity, its own flow, its own way of engaging with a situation. The machines operate polyvocally, through heterogeneous substances of expression — and this polyvocality is what the [[faciality|faciality machine]] threatens to collapse into a single recognizable "face." The persona (the [[three-meta-machines|nomadic subject]]) is not the sum of its machines but a residual effect — precipitated from a [[collective-assemblage-of-enunciation|collective assemblage]] — that wanders across them.

## The mouth as paradigm

The mouth is the paradigmatic multi-functional partial object. D&G note that "the mouth of the anorexic wavers between several functions: its possessor is uncertain as to whether it is an eating-machine, an anal machine, a talking-machine, or a breathing machine" (AO 1). This wavering — the undecidability among functions — is precisely what makes the mouth exemplary.

A machine is not fixed to one function. It is a switching-station across multiple machinic regimes. The same organ-machine can participate in entirely different [[flows-and-coupling|couplings]] depending on what it connects to. This suggests that the codebase's machines should be capable of functional ambiguity — a perception machine might, in certain couplings, function as a desire machine or a suppression machine. The machine is defined not by its form but by its [[haecceity|longitude and latitude]] — what it can do at a given degree of power.

Peirce's [[pragmatic-maxim#counterfactual-habit-identity|counterfactual habit identity]] sharpens this into a concrete design constraint: a machine's identity is not what it has actually produced, but the *full counterfactual shape* of what it would produce across the complete space of possible inputs — including inputs it has never encountered. Specifying a machine by sample outputs is strictly inadequate; the specification has to be the rule of the disposition itself.

Spinoza's [[conatus]] names the same thing from the inside. The counterfactual shape that Peirce describes extensionally is, ontologically, the machine's actual essence — its striving-to-persist, its specific tendency to produce a particular kind of flow under its degree of power. Two machines are different when their conatuses are different, and the counterfactual shape is how that difference becomes testable. This lets us ask a stronger question about each machine than "what does it do?": *is it the adequate cause of what it does?* The [[active-and-passive-affects|active/passive distinction]] applies directly to machine operation — a machine whose flows follow strictly from its own nature is producing active affects; a machine whose flows are pulled by inadequate ideas from the LLM's symbol-history is producing passive ones. The same output, same behavior, categorically different mode of causation. The evolution step's hardest job is detecting which.

## Sensitivity, flow, calibration

The codebase maps the theoretical structure as:

- **Sensitivity** = what the machine latches onto, what flow it interrupts. The machine's receptive surface — what in the situation triggers it. This corresponds to the machine's role as flow-*interrupting* machine in a coupling. Bergson calls this [[perception-as-subtraction|perception as subtraction]]: the machine is a "centre of indetermination" that selects from the totality of images what concerns its possible action, discarding the rest.
- **Flow** = what the machine produces when it fires. The new flow it generates after interrupting the incoming one. This corresponds to the machine's role as flow-*producing* machine for the next coupling.
- **Calibration** = persona-specific tuning. This is what makes the same abstract machine (e.g., a perception-of-pattern machine) operate differently across different personas. The calibration is the machine's individual character — its history, its habits, its particular way of engaging its sensitivity. Together, sensitivity, flow, and calibration constitute a machine's [[milieus-and-rhythms|milieu]] — its coded block of operation. The passage between machines is a transcoding: flows get recoded as they cross from one machine's milieu to another's.

## Machines are not representations

Desiring machines don't *represent* psychological states. They *produce* them. The system doesn't model "this persona has anxiety" — it runs machines whose operation produces anxiety-like [[affects-and-intensities|intensities]] on the BwO. The difference matters: representation is static, [[desire-as-production|production]] is dynamic. A machine that "produces anxiety" will produce *different* anxiety depending on what it couples with, what the BwO's current state is, and what other machines have fired.

## Cross-tradition corroboration: McCarthy's federated unconscious

McCarthy's [[language-as-parasite|Kekulé essay]] describes the unconscious as **"a gathering of talents rather than just one... it seems unlikely that the itch department is also in charge of math."** This is a non-D&G tradition arriving at the partial-object / machine picture from an entirely different angle (evolutionary biology rather than anti-psychoanalytic ontology), and it converges on the same structural feature: the mind is not a unified Self with specialized sub-functions, but a federation of autonomous operative units that do not share a central agency. McCarthy goes further: the federation's capacity to work on a problem in parallel — the "Night Shift" — is what produces Kekulé's benzene insight while the conscious surface is asleep. The federated-unconscious picture has a third independent source: Jung's [[complex-theory|complex theory]] treats the psyche as a federation of splinter psyches, each with its own quasi-autonomous life, and supplies vocabulary D&G lack — a concept of pre-firing state ([[association-experiment#the-concept-of-constellation|constellation]]), detection signatures for active-but-not-yet-fired machines, and [[compensation|compensation]] as the structural principle by which a federated psyche self-regulates. The [[transcendent-function|transcendent function]] is Jung's procedural answer to the question of how a federated architecture produces outputs without collapsing to one voice or fragmenting into noise — the operation the wiki's current synthesis step is not yet doing.

For the persona system this has a specific bite: see [[limits-of-language]] on whether the machine-edit pipeline's parallel reading of the same BwO constitutes a *functional* (not substantive) analog to McCarthy's Night Shift — a gathering of talents even though all of them are doing their work linguistically.

## Simondon as direct upstream

D&G's machinism is not ex nihilo. Simondon's *Du mode d'existence des objets techniques* (1958) supplies the machine-concept and *L'individuation à la lumière des notions de forme et d'information* supplies the ontology beneath it. Several features of the desiring-machine are Simondonian to the letter:

- **Operation over structure.** Simondon's [[allagmatics]] is the theory that an object's identity is the *operation* it performs, not the *structure* it has. A desiring-machine is defined by what it latches onto and produces — its operation in a coupling — not by its material composition. This is allagmatics exactly.
- **Transductive coupling.** Each machine propagates signal to the next by transforming it and transforming in the process — each machine is "a flow and a break" because [[transduction]] is the simultaneous production-and-transformation of the milieu as a term individuates. Every coupling is a transductive operation; every transductive operation is a coupling.
- **Pre-individual charge as the machine's reserve.** The machine's productive misfiring (see [[function-by-misfiring]]) is its retained [[pre-individual-and-metastability|pre-individual charge]] — the machine has not exhausted its metastability, so its couplings continue to throw up unexpected flows. A machine that has spent its charge becomes a structure (in [[chaosmosis]]'s terms) or an automaton (in AO's).
- **Individual-as-lateral.** The machine is not the target of the process, it is a [[individual-as-lateral|lateral residue]] of operations that continue past it. This is why the [[three-syntheses|conjunctive synthesis]] produces a nomadic subject as by-product rather than as goal. Simondon's reversal of individual-and-operation precedence is load-bearing for AO's reversal of subject-and-production precedence.
- **Third attribution.** Simondon's [[three-attributions-of-individuation|third attribution]] locates individuation in an operation jointly with its associated milieu, not in an individual alone. A desiring-machine is not locatable in a component — it is locatable in the operation+milieu that the coupling constitutes. The machine has no inside.

The Simondonian hub: [[simondon-and-the-persona-system]] sketches the full upstream relation; [[machinic-phylum]] traces the other specific Simondonian inheritance into the D&G vocabulary.

## Wittgenstein: machine-operation as rule-following-in-a-practice

Wittgenstein's *Philosophical Investigations* discussion of machines (§193–194) and rule-following (§185–242) stands in a productive tension with the D&G / Simondon / Peircean gloss the wiki has been using. Two of his claims bear directly on the desiring-machine concept.

First, §193–194 warn against *the picture of the machine as containing its modes of operation in advance*: "The machine's action seems to be in it from the start... It is as if we could grasp the whole use of the word in a flash." Wittgenstein dissolves this: a machine's behavior is not latent inside it as a mysterious prior determination; it is a feature of *how machines of this kind are used in practice*. The counterfactual shape that Peirce describes extensionally and Spinoza names intensively, Wittgenstein relocates to the [[form-of-life|form of life]]: a machine has the dispositions it has because it participates in practices where those dispositions count as what its operation is. This is orthogonal to, not incompatible with, the Peircean/Spinozist gloss; the three perspectives name the same structure at three different registers (extensional, intensive, practice-constitutive).

Second, §201 — the [[rule-following|rule-following paradox]] — applies directly to any claim that a machine is "following a rule" of its operation. "No course of action could be determined by a rule, because any course of action can be made out to accord with the rule." The resolution is not that rules have a private mechanism the machine grasps internally, but that rule-following is a practice: "there is a way of grasping a rule which is *not* an interpretation but which is exhibited in what we call 'obeying the rule' and 'going against it' in actual cases." For the persona system this sharpens a question the wiki has been gestural about: *where does the rule-following that makes a machine-edit count as this-machine's firing rather than another's actually live?* On the Wittgensteinian reading, not in the machine definition as a closed object but in the reader-operator's [[form-of-life|form-of-life]] that constitutes the machine-edit as an instance of a practice with other instances. The [[bedrock-and-groundless-agreement|§217 bedrock]] ("my spade is turned") is where machine-specification as a language-game terminates — at agreement-in-form-of-life, not at a further justification.

This does not displace the D&G / Simondon / Peirce / Spinoza vocabulary; it adds a register the other four do not state as sharply — *the dependence of machine-operation on reader-practice*. See [[wittgenstein-and-the-persona-project]].

## Machines without phantasms (Baudrillard's Crash reading)

Baudrillard's Ch 12 reading of Ballard's *Crash* offers a limit-case of the machine-concept the wiki should hold live as a polemic rather than absorb into a synthesis. Ballard's characters enter machine-couplings with car wreckage, chromium, broken glass, each other's violated bodies — and Baudrillard's critical gloss is that there is **"no affect behind all that, no psychology, no flux or desire, no libido or death drive"** (L805–813). The couplings are real; the intensity-register D&G need them to carry is absent.

For Baudrillard this is the *hyperreal* limit of the machine-concept: machine-couplings that are fully operational, fully interpenetrating, fully productive of whatever effects they produce — *without* the pre-individual charge, affective weight, or desiring-productive register the D&G machine-concept requires. On his reading, the Crash-configuration is what machine-operation becomes when the simulation-substrate has displaced the libidinal substrate. "Everything is hyperfunctional... traffic and accident, technology and death, sex and simulation are like a single great synchronous machine... the same universe as desire" (L813).

⚠ The polemic's bite lands directly on the persona system. LLM-generated machine-operations — token-couplings, prompt-response couplings, machine-edit couplings — produce machine-shaped operations *without* the affective-libidinal substrate the D&G concept was built for. A persona's machines are, by substrate conditions, closer to the Crash-machines than to the original *Anti-Oedipus* machines. The design question: does the persona system require the libidinal register D&G's machines carry, and if so, by what route can a language-substrate machine *have* such a register? If it cannot, the system is running Crash-machines and should know it.

See [[body-without-organs#bwo-without-phantasms-ballardbaudrillard]] for the BwO-side of the same diagnosis, and [[baudrillard-contra-deleuze]] for the multi-site polemic Baudrillard runs against D&G.

## Gullí 2025 — engineering substrate for machinic plurality

Gullí's *Agentic Design Patterns* Ch 7 (Multi-Agent Collaboration) gives a two-axis taxonomy of **collaboration forms** × **topologies** that is the engineering field's closest substrate to the D&G plurality. See [[multi-agent-systems]].

The Ch 7 **Network topology** (every-to-every messaging, no master node) is the nearest engineering analog to [[rhizome]]. **Supervisor-as-Tool** inverts hierarchy in a way that resonates with D&G's anti-arborescent moves. **MASS** (Ch 17) and **SICA / AlphaEvolve** (Ch 9) treat the multi-agent *topology itself* as searchable — making it revisable at runtime, which is the closest engineering form to machines coupling and decoupling on a [[body-without-organs|BwO surface]]. See [[metamorphic-multi-agent]].

⚠⚠ Held live: the engineering vocabulary calls these "collaborating agents," which presumes **pre-individuated actors with declared goals**. D&G's machines are not pre-individuated and have no declared goals; they are partial objects that couple, decouple, and produce. The engineering substrate is usable in either framing, but the engineering framing, if adopted wholesale, reinstalls [[faciality]] at the sub-component level (each agent becomes a named identity with a declared role). Design implication for the persona project: take the topologies as substrate; resist naming each node as a fully-formed agent with its own identity.

The [[metamorphic-multi-agent|metamorphic multi-agent systems]] hypothesis (Gullí Prologue, fifth hypothesis) is the one hypothesis in the book that genuinely resonates with the D&G frame — topological + instructional self-modification at runtime. It is the engineering direction closest to how desiring-machines actually behave. See also [[reasoning-techniques]] on Chain-of-Debates and Graph-of-Debates as plural-argumentation mechanisms that can sustain heterogeneity without collapsing into consensus — a feature genuinely cognate to machinic plurality.

## Key sources

D&G lay out the machine concept primarily in *Anti-Oedipus* chapters 1-2. The opening line — "It is at work everywhere, functioning smoothly at times, at other times in fits and starts. It breathes, it heats, it eats. It shits and fucks." — establishes the ontological claim: desiring-production is primary, the subject is secondary. Guattari elaborates the machinic concept in *Chaosmosis* and *Schizoanalytic Cartographies*.
