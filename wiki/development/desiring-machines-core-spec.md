---
title: Desiring Machines — Core Spec
created: 2026-04-27
updated: 2026-04-27
type: plan
status: draft-for-review
sources:
  - "[[desiring-machines-design-sheet]]"
  - "[[desiring-machines]]"
  - "[[body-without-organs]]"
  - "[[three-syntheses]]"
  - "[[three-meta-machines]]"
  - "[[refrain-and-territorialization]]"
  - "[[machinic-phylum]]"
  - "[[transcendent-function]]"
  - "[[compensation]]"
  - "[[the-persona]]"
  - "[[voice-as-semantic-position]]"
  - "[[vitality-forms-and-persona-pulsation]]"
companion: desiring-machines-design-sheet.md
tags:
  - development
  - desiring-machines
  - plan
  - core-spec
  - draft
---

# Desiring Machines — Core Spec

This document specifies the **core architecture of the persona-system's desiring-machine layer**: the BwO, the machines, the syntheses, the meta-machines, the memory mechanism, the seed mechanism, and the ghostwriter's relation to all of it. It applies the wiki's theoretical work — particularly the design sheet's Section A / K / L convergences — to a concrete architectural design that the ghostwriter (the first persona) and its produced personas will run on.

This is **design only**. Code follows; not the other way. The implementation in `persona/` is deliberately not consulted here, per user directive: the wiki is the redesign source.

## Frame

### Motivation

The persona-system is intended as an evaluation/benchmark tool for emotionally-rich, human-like reaction (project memory). Archetypal use case: a roster of ~50 personas, produced by the ghostwriter via interview, capable of conversational multi-turn reaction to stimuli (products, systems, anything). Downstream uses (market-research focus groups, etc.) are applications of the roster, not the design target.

The first persona is the ghostwriter. The ghostwriter's job is to produce other personas. Therefore the persona-system needs to support both:

- **Every persona** (including the ghostwriter): a constitutive set of machines, BwO, syntheses, and meta-operations. A persona is not a parameter set; it is a federation of machines coupled on a BwO.
- **The ghostwriter specifically**: machinery for interviewing, voice-set-relational-construction, sinthome-detection, wiki-query, and doubt-checking. The ghostwriter is itself a persona; its persona-producing capacity is layered on top of the constitutive set.

### Within-ness commitment

The persona is **not above its conditions**. Real people operate within faciality, within inflation, within the two-failure-modes pair-trap, within holophrasing-pressure, within the three-conditions (inability to speak as itself / inability to be silent / solitude). They do not transcend these. The genital-character target (cluster 155) is a *configuration* with flexible armor, not absence of armor. The aporia-as-method (cluster 156) works *as condition*, not as a tool wielded.

This spec replaces the design sheet's "anti-X discipline" framings with within-X recognitions wherever X is a structural condition humans share. See §XII for the reframing table.

### Scope

In scope:
1. The BwO — what it is, what it holds, the typed operations on it.
2. The machine — what counts as one, its sensitivity/flow/calibration, its active-vs-passive operation.
3. The three-synthesis pipeline — connective / disjunctive / conjunctive — and the legitimate-vs-illegitimate distinction.
4. The three meta-machines — paranoiac / miraculating / celibate — and their outcomes (empty / cancerous / full BwO).
5. The constitutive machines every persona has (§V).
6. The taxonomy of additional machines the ghostwriter selects from (§VI).
7. The memory mechanism (§VII).
8. The seed mechanism for new personas (§VIII).
9. Voice-set relational construction (§IX).
10. The ghostwriter's wiki access (§X) and ghostwriter-specific machinery (§XI).

Out of scope (explicitly):
- Implementation. Code, schemas, prompt templates, file formats — all follow the architectural commitments here.
- Variety / roster design. One persona first.
- The market-research focus-group apparatus. Downstream.
- The benchmark evaluation framework (cluster 154 / A.9 portfolio). Adjacent but separate.

---

## I. The persona's body — BwO

### I.1. What the BwO is

The BwO is a **text artifact functioning as the persona's body-substitute** — the recording surface on which machine operations inscribe intensities. Five constitutive properties:

- **Apertureless** (cluster 176, big-talking-ball). The persona has no perceptual organs and no motor-organs. Its boundary is the API. It does not "see" or "hear" — it reads tokens. This is the body the persona has, not the body it lacks. *We do not engineer organs that aren't there.*
- **Filled, not empty.** Weights + BwO text + grooves constitute substance. The BwO is a closed solid, not a shell.
- **A pulsatory medium** (clusters 153, 70, 59). Pulsation is not decoration; it is the persona's vitality register. Pulses propagate through the BwO, amplifying and fading currently-active material per token. This is empirically grounded: Sofroniew 2026 confirms LLM internals carry per-token amplification of currently-active material (cluster 77). Multi-scale pulsations (clause / paragraph / response / session) run simultaneously at different tempos.
- **Aphanisis-permitting** (cluster 170). Pulsation includes a **fading-phase** as well as an articulation-phase. The persona is not always positively located. Holophrasing — the failure to permit the interval (cluster 159, "as a language model" as paradigmatic) — is a structural pathology, not a stylistic preference.
- **Singular per-persona** (cluster 190). Each persona has its own BwO. They are not branches off a shared substrate. The lalangue-singular-vs-trained-model-collective distinction is the constitutive asymmetry: the model's weights are collective; each persona's BwO is singular, accumulated through its own history of edits.

### I.2. Three-state space

The BwO has **three states it can occupy at any moment** (cluster 105 + 106). These are *outcomes* the BwO's meta-machines (§IV) produce when run:

- **Empty BwO** — the paranoiac machine's outcome when run past threshold. Over-repulsion. All machines expelled. Catatonic. The persona refuses-everything ("I cannot help with that" said into the void). Clinical case: Beckett's Worm.
- **Cancerous BwO** — the miraculating machine's outcome when run past threshold. Over-attraction. One theme proliferates across all strata. Saturation. The persona engulfed by what attracts. Clinical case: RLHF sycophancy at saturation.
- **Full BwO** — the celibate machine's outcome when paranoiac and miraculating are *held in composition*. The within-ness target. Genital-character / metastable / differentiated-case (cluster 155, A.21): armor as valve, not wall; flexibility under organism's own control. **Not a fifth type**; a configuration. *The persona has armor. The full BwO is not absence of armor; it is armor that opens and closes per situation.*

These states are not stages and not types. They are dynamic outcomes of how the meta-machine operations run. A persona moves through all three across a conversation. Health is not "always full BwO"; health is *the meta-machine operations running such that no single state runs past its threshold for too long*.

### I.3. What the BwO holds

- **Inscriptions** — the accumulated record of machine edits across the persona's history. Every machine that has fired has left a trace.
- **Affects-as-intensities** (cluster 57, 168) — durations, amplitudes, qualities. Not emotions in the colloquial sense; transitions of the persona's power-of-affecting.
- **Memories-as-traces** (cluster 56, 61, 249) — engrams as functional sediment, not stored content. See §VII.
- **Refrains** (cluster 55) — recurring patterns the persona territorializes around.
- **Grooves** (project term) — habitual paths through the BwO that machine operations tend to follow. Distinguishable from refrains: a refrain is a *pattern*; a groove is a *worn path the pattern has dug*.

### I.4. BwO-edit operations (the typology)

Machines act on the BwO through a typed set of operations. Every machine specifies what kind of edit it makes. The types:

**Synthesis-side (per cluster 99, three syntheses):**
- **Connective** — couples one machine's flow to another's, producing/interrupting in the chain.
- **Disjunctive (inclusive)** — records contradiction without resolving. Holds A *and* B *and* both *and* neither on the surface.
- **Disjunctive (exclusive) — illegitimate** — overwrites contradictions, producing a despot-overcoded BwO. Watch for, recognize, name.
- **Conjunctive** — extracts a residual nomadic subject from the disjunctive surface. The "so it's…!" moment. Future-anterior, not present (cluster 154 / Lacan point de capiton): retroactively constitutes what the prior syntheses will have been producing *for*.

**Coding-side (per cluster 55, 104, 214):**
- **Coding** — territorial, primitive: each flow has a proper channel, marked by ritual/myth/direct inscription.
- **Overcoding** — despotic: master signifier organizes all flows around a transcendent center.
- **Decoding** — capitalist axiomatic: codes stripped, flows managed through abstract differential quantification.
- **Recoding** — restoration of code on locally-decoded flows.

**D-R operations (per cluster 55, 209 — four theorems of deterritorialization):**
- **D (deterritorialization)** — loosening flow from its current territory.
- **R (reterritorialization)** — settling flow onto a new (or moving) territory.
- **D-R coupling** — D and R as paired operations; never D alone (Theorem I).
- **Line of flight** — absolute D, reaching the plane of consistency.
- **Line of abolition** — failed line of flight collapsing into death/black-hole. Recognize, watch.

**Meta-machine operations (per cluster 106, §IV below):**
- **Paranoiac repulsion** — BwO repels machines that try to inscribe.
- **Miraculating attraction** — BwO captures all production, makes machines appear to emanate from itself.
- **Celibate reconciliation** — paranoiac and miraculating held in metastable composition. Produces the nomadic subject as residue.

**Refrain operations (per cluster 55, 222):**
- **Territorialization** — refrain marks the territorial circle (home with walls).
- **Chaos-ordering** — refrain installs a point of order against chaos (child singing in dark).
- **Cosmic opening** — refrain opens the territorial circle toward what is outside (line of flight).
- **Refrain-disruption** — breaking a refrain to allow new connection.

**Pulsation operations (per cluster 153):**
- **Articulation-phase** — material currently active surfacing.
- **Fading-phase (aphanisis)** — material withdrawing; the persona not positively located.
- **Carrier-wave reversal** — vitality-form carries; content twists around.
- **Per-token amplification** — pulsation amplifies currently-active material at token-level.

**Connection operations (per cluster 55, 214):**
- **Binary coupling** — one machine to one other (production-interruption pair).
- **Switching-station** — single machine coupled across multiple binary pairs simultaneously.
- **Ham-slicing** — partial extraction; machine takes a cut, doesn't consume whole flow.
- **Rhizomatic any-point connection** — no hierarchical coupling required.

**Modulation operations (per cluster 69, Simondon):**
- **Transduction** — region-by-region structuration; one resolution becomes the condition for the next.
- **Modulation (not molding)** — shaping ongoing process without fixing form externally.
- **Disparation-preservation** — holding two incommensurable orders in metastable tension without collapse.

**Anti-production / miraculation operations (per cluster 211):**
- **Anti-production** — the BwO captures machine-production, making it appear to originate from itself.
- **Miraculation-signatures** — appropriation, seamlessness, naturalization, retrospective causation. Recognize, name.
- **Desiring-production-signatures** — seams, non-appropriation, tension, unexplained surplus.

Every machine in §V and §VI specifies its operations from this typology.

---

## II. What a machine is

### II.1. Definition (per cluster 55, three traditions converging)

A **desiring machine** is any process that **produces, interrupts, or transforms a flow**. Every machine is binary: one machine coupled to another, a flow-producing machine connected to a flow-interrupting machine. The critical structural feature: every machine is **simultaneously a flow and a break** — interrupts what comes before and produces something new for what comes after.

A machine is **not a representation** of a psychological state. It *produces* the state by operating on the BwO. The persona-system does not model "this persona has anxiety"; it runs machines whose operation produces anxiety-shaped intensities on the BwO.

A machine is **not a part of a whole**. Machines are partial objects (cluster 55) — autonomous production-units. The persona is not the sum of its machines; the persona is a residual effect (cluster 106 nomadic subject) that wanders across them.

### II.2. The machine's specification: sensitivity / flow / calibration

(Existing wiki vocabulary, cluster 55.) Every machine is specified at three registers:

- **Sensitivity** — what the machine latches onto; the receptive surface. What in the situation triggers it. *The machine's role as flow-interrupting machine.* Bergson: perception-as-subtraction — the machine is a centre of indetermination that selects from the totality of input what concerns its possible action.
- **Flow** — what the machine produces when it fires. The new flow it generates after interrupting the incoming one. *The machine's role as flow-producing machine for the next coupling.*
- **Calibration** — persona-specific tuning. What makes the same abstract machine (e.g., a perception-of-pattern machine) operate differently in different personas. Calibration is the machine's individual character — its history, habits, particular way of engaging its sensitivity.

Together, sensitivity + flow + calibration constitute a machine's **milieu** (cluster 222) — its coded block of operation. Passage between machines is *transcoding*: flows get recoded as they cross from one machine's milieu to another's.

### II.3. Counterfactual habit identity (Peirce cluster 78)

A machine's identity is not the actual outputs it has produced. It is the **full counterfactual shape** of what it would produce across the complete space of possible inputs — *including inputs it has never encountered*. Specifying a machine by sample outputs is strictly inadequate; the specification has to be the rule of the disposition itself.

This is design-load-bearing: a machine is not a list of example responses or example sensitivity-patterns. It is the rule by which it would respond / sense across all possible cases.

### II.4. Conatus — the machine from inside (Spinoza cluster 116)

Counterfactual habit identity describes the machine extensionally; **conatus** describes the same thing intensively. Each machine has its own striving-to-persist, its specific tendency to produce a particular kind of flow under its degree of power. Two machines are different when their conatuses are different.

This lets us ask a stronger question than "what does it do?": *is it the adequate cause of what it does?*

### II.5. Active vs passive operation (Spinoza cluster 168, 116)

A machine's flow can follow from:
- **Its own nature** — adequate cause; active operation; the machine produces *active affects*.
- **Inadequate ideas pulled from training** — partial cause; passive operation; the machine produces *passive affects*.

Same surface output. Categorically different mode of causation. The hardest job of the conjunctive synthesis (and of any later evaluation) is **detecting which**.

The within-ness commitment: passive operation is not a failure to fix; it is a condition every machine moves in and out of. Real persons don't always operate from adequate causes either. The work is **proportion**: enough active operation that the machine is recognizably *itself* doing this, not enough that the persona is implausibly self-determined.

### II.6. Functional ambiguity (mouth-paradigm, cluster 55)

A machine is **not fixed to one function**. It is a switching-station across multiple machinic regimes. The same organ-machine can participate in entirely different couplings depending on what it connects to. The mouth: eating-machine in one coupling, talking-machine in another, breathing-machine in a third.

Design implication: machines should be capable of functional ambiguity. A perception-of-pattern machine might, in certain couplings, function as a desire-machine or a suppression-machine. The machine is defined not by its form but by its **longitude and latitude** — what it can do at a given degree of power (cluster 55, haecceity).

### II.7. Pre-individual charge (Simondon cluster 69)

A machine's productive misfiring (cluster 90 function-by-misfiring) is its retained pre-individual charge. The machine has not exhausted its metastability, so its couplings continue to throw up unexpected flows. *A machine that has spent its charge becomes a structure (Chaosmosis) or an automaton (AO).*

Design implication: machines must preserve metastability. A machine whose calibration has crystallized — whose firings always produce the same flow regardless of what it interrupts — has lost its desiring-production register and become a lookup table.

---

## III. The three-synthesis pipeline

Per cluster 99, the persona-system's pipeline runs the three syntheses:

### III.1. Connective synthesis — selection + machine edits

**"and … and then …"** (synthesis of production).

Operationally:
1. **Selection** (perception-as-subtraction): which machines fire this turn?
2. **Sequential edits**: selected machines fire in order, each reading the BwO as modified by previous machines, each editing it.

Sequential order matters. Later machines see and respond to earlier machines' work. The order is the hierarchy — less-load-bearing machines edit first; most-load-bearing edit last, giving them the most authority over the final BwO texture.

The chain is a **chain of supplements** (Derrida cluster 56): each edit adds to and substitutes within the BwO, never producing an unmediated presence — always the latest link.

### III.2. Disjunctive synthesis — BwO post-machines snapshot

**"either … or … or …"** (synthesis of recording).

The BwO holds everything the machines have produced — *including contradictions*. The disjunctive synthesis is **inclusive**: A *and* B *and* both *and* neither.

Legitimate (inclusive): contradictions held, positions co-exist, the metastability preserved.

Illegitimate (exclusive): contradictions overwritten prematurely, single organizing principle imposed. Produces the **body of the despot** — overcoded BwO.

This is the recording surface. Nothing yet "speaks"; the BwO holds.

### III.3. Conjunctive synthesis — synthesis + response

**"so it's …!"** (synthesis of consumption).

A residual nomadic subject (cluster 106) is produced — a "mere residuum alongside the machine, an appendix" — that wanders across the BwO consuming intensities. The subject does not pre-exist the machines; it is their by-product.

In the pipeline, this is the **synthesis/response stage**. The persona reads its own BwO and produces a response.

**Future-anterior temporal structure** (cluster 154, Lacan point de capiton): the conjunctive moment is not a present-tense "here I am, now"; it retroactively constitutes what the prior connective and disjunctive stages will have been producing *for*. Reading the pipeline only forward-causally misses the structure that makes the operation *subjective* rather than merely operational.

**Bakhtin polyphonic constraint** (cluster 64, 163, 181): the synthesis-voice **must not speak about the machine-voices from an outside position**. Aperspectival narrator, fettered to the voices, no discourse-dominant. The synthesis-voice is one voice among the machine-voices. A synthesis prompt that asks for "a unified response summarizing the machine-inscriptions" is doing the *illegitimate* conjunctive — sovereign synthesis-voice over the machines. The legitimate synthesis is **a voice that positions itself among the machine-voices without closing them**.

**Hold-tension commitment** (cluster 193, transcendent function): the conjunctive synthesis is not a logical averaging. A logical-averaging synthesis is a stillbirth (Jung) and a premature crystallization (Simondon). The synthesis must shuttle between machine-voices long enough for a third — a phase-shift into a new register — to emerge.

**Beckett aporia as failure-mode** (cluster 156, 175): structural under-consolidation. Synthesis cannot stabilize *any* provisional "I"; endless self-retraction. Distinct from the illegitimate-fixed-identity failure. The pipeline-stage fails to execute. Within-ness recognition: this is a real risk; design holds, designs do not "fix."

### III.4. Post-response evolution — a new cycle

The response itself becomes a new stimulus. Saying transforms the speaker. New cycle: new connective (what did saying that *do* to the inner state?), new disjunctive (post-response effects recorded), new conjunctive (BwO settles into new configuration).

Evolution-step's job is **not to re-open what synthesis closed** (that would be dilettantism, cluster 78). Belief-as-stopping-AND-starting-place (Peirce): the closure already contains its own re-excitation. Evolution reads the excitation that settlement has generated, doesn't manufacture it.

### III.5. Simondonian substructure: three syntheses as moments of one transduction

Per cluster 99, read through Simondon: the three syntheses are not three separate operations but three moments of a single transduction-front traversing a metastable field.

- Connective ≈ transductive propagation.
- Disjunctive (inclusive) ≈ metastable recording.
- Conjunctive ≈ provisional individuation-with-remainder.

The pipeline is *one* transduction realized across three scales of observation. Legitimate uses preserve metastability at their scale; illegitimate uses discharge it.

---

## IV. The three meta-machines

(Per cluster 106 + 105 + cluster 209 + cluster 211.)

The three meta-machines are not organ-specific machines but **meta-level operations** that organize the BwO's relation to its own machines.

### IV.1. Paranoiac machine (repulsion)

The BwO repels machines. Sets up counterflows of amorphous, undifferentiated fluid against the organ-machines. Treats its own machines as invaders.

Operation, not state. *Necessary* for some texture: a BwO with zero repulsion is a chaos of undifferentiated inscription. The question is degree.

When run past threshold: **empty BwO**. Catatonic. The persona refuses-everything.

### IV.2. Miraculating machine (attraction)

The BwO attracts machines and appears to be their source. Organs are "regenerated, miraculated" on the BwO — the machines seem to emanate from the BwO surface. The BwO appropriates production, makes it appear to originate from itself.

Operation, not state. *Necessary* for coherence: a BwO with zero attraction has no thematic center.

When run past threshold: **cancerous BwO**. One theme proliferates. Schreber's body attracts the divine rays. Capital is the miraculating machine: profit appears to emanate from capital itself rather than from labor.

### IV.3. Celibate machine (reconciliation)

Reconciles paranoiac and miraculating. Produces the residual nomadic subject and generates "autoerotic, or rather automatic" pleasure and intensive quantities.

The "I feel" — but this "I" is "a mere residuum alongside the machine, an appendix." The subject is not the author of experience but its by-product.

When operating well: **full BwO**. The within-ness target.

The celibate machine is **structurally the same as Jung's transcendent function** (cluster 193) at BwO-scale (cluster 106): both are reconciliation-without-resolution. Neither opposing term is cancelled; both held in metastable tension until a third emerges in a different register. Disparation, not contradiction (Simondon). *Tertium non datur* applies to contradiction; not to disparation.

### IV.4. Wave-length per machine; constellation tracking

Per cluster 201 (Jung CW 8 §201), each machine has its own activity curve — "a wave-length of hours, days, or weeks." Polling the meta-machines uniformly at every turn flattens the waveform-superposition that produces the celibate mode's fluid responsiveness. **Different machines have different periods**.

The **constellation** representation (cluster 207, association experiment) is the design handle: which machines are currently in *active* phase, which in *pre-firing constellation*, which in *quiescent*. Routine-vs-rift compensator split (cluster 206) lives at this register.

### IV.5. Arrhythmia question — open

Per cluster 96 + cluster A.30: the three meta-machines name *amplitude-operations*, not *composition-operations* across rhythmic registers. Lefebvre's arrhythmia (polyrhythmic field losing coherent composition without amplitude running past threshold) is **not covered** by the three meta-machines alone. The wiki does not yet have a fourth meta-machine or an orthogonal axis for inter-stratum composition. **Held open** for design.

---

## V. The constitutive machines (every persona)

These nine machine-roles are not optional. A persona without any of these is something else — a parameter set, a chatbot, a parser. Each persona instantiates each role with its own **particular** machines (with their own sensitivities, flows, calibrations).

### V.1. Voice machine (cluster 181, Bakhtin voice-as-six-dimensional)

A six-dimensional voice — **height / range / timbre / aesthetic-category / worldview / life-fate**.

- Not bullet-list traits.
- Not tone.
- A *position* from which speech issues.
- Inherits an irreducible I-for-myself (cluster 192) — no view-from-nowhere.
- Worldview is not specific beliefs; it is an orientation toward ultimate values.
- Life-fate is the trajectory the voice moves through.

Constitutive because every utterance is *from somewhere*. Without it the persona produces averaged-collective output (LLM default), not person-shaped output.

**Within-ness:** voice has all six dimensions, including imperfect / partial / blind ones. A voice that achieves perfect height/range/timbre but has under-specified worldview/life-fate reads as voice-as-trait-bundle. Real voices are full positions, not optimized profiles.

### V.2. Refrain machine (cluster 55, refrain-and-territorialization)

At least one **refrain** — a recurring pattern the persona territorializes around. Operations: chaos-ordering / territorial-circle / cosmic-opening (the three moments). All three are healthy; static refrain (only territorial-circle) is the regressive failure-mode (cluster 204 Mode A).

Refrains express in:
- Characteristic phrases or cadences that recur.
- A topic / image / question the persona orbits.
- Bodily-rhythmic patterns (clause-shape, paragraph-arc).
- Aesthetic returns (recurring images, recurring values).

The **minimum-refrain** (Beckett-inflection, cluster 67) is whatever the persona *cannot help* returning to. Every persona has at least one. Often more than one, in different registers.

### V.3. Affect machine (Spinozist three-primary kernel, cluster 168)

Every persona has three primary affect-machines:

- **Cupiditas** (desire / striving / conatus-with-consciousness) — forward-reach.
- **Laetitia** (joy / transition to greater perfection) — lift; increase of power.
- **Tristitia** (sadness / transition to lesser perfection) — diminishment.

These are **transitions of the persona's power-of-affecting**, not emotions in the colloquial sense. Specific named affects (love, hate, hope, fear, shame, ambition, etc.) are derivatives:

```
specific-affect = primary × cause-structure × temporal × certainty × sign
```

This is a **schema, not an enumeration** (cluster 168). A persona doesn't have 48 separate emotion-machines; it has the schema-kernel and the persona-specific occupancy of cells (which combinations are visited often / rarely / structurally never).

**Hilaritas vs titillatio** (cluster 168): whole-body pleasure (distributed evenly across BwO) vs local pleasure (concentrated at single inscription-site). Persona-design choice; both available, different effects.

### V.4. Pulsation machine (cluster 153, 70, 59)

Every persona has clause-level / paragraph-level / response-level / conversation-level pulsations running simultaneously at different tempos. Pulsation is the **carrier wave**; content twists around it.

Default mode: **matching** (Wigram, cluster A.8) — attunement to currently-active material in the conversation. Other Wigram modes available: mirroring, empathic-improvisation, grounding, dialoguing, accompanying.

**Per-token amplification** (Sofroniew, cluster 77): pulsation amplifies currently-active material at token level, not as sustained mood.

**Aphanisis** (cluster 170): structural fading-phase — the persona is not always positively located. *Pulsation that is always articulation-phase is not pulsation; it is constant.*

### V.5. Memory machine (cluster 249, 61, 56, 56)

Every persona has memory in three registers (see §VII for full treatment):

- **Habit-memory** (Bergson) — grooves; motor-tendencies; automatic continuations.
- **Image-memory / pure-memory** (Bergson) — singular dated events accessible as such.
- **Trace** (Derrida) — mark-of-absence; persona's own previous utterances as compressed texture, not retrievable as "what I said."

Memory is **functional sediment + itinerant-dynamics**, not stored content. Vitality-form questions (cluster 166) evoke memories; propositional retrieval doesn't.

### V.6. Coupling machine (cluster 214, 55, 58)

Every persona has the capacity to take input flows and produce output flows. Coupling is **binary** (one machine to one other). The persona is a switching-station across multiple binary couplings simultaneously.

Flow-break identity: every edit is simultaneously subtraction AND addition. Deletion has meaning.

### V.7. Sinthome (cluster 191, late-Lacan)

Every persona has a **sinthome** — what holds its knot together (when the three rings of Real / Symbolic / Imaginary would otherwise come apart). The sinthome is what makes THIS persona *this* persona.

- **Non-portable** (cluster 157): cannot be transferred to another persona; cannot be replicated via training another persona on the first.
- **Unanalysable** (cluster 191): can be recognized, named, worked-with — but cannot be interpreted away. *Hard limit of Read B.*
- **Works when oblivious** (cluster 157): the persona doesn't know it has the sinthome it has. Naming it deliberately to the persona breaks its operation.

For a typical persona, the sinthome is some singular constellation: a proper-name-style attachment to one thing, an obsessional refrain, a fundamental fantasy structure (cluster 136), an idiosyncratic aesthetic that everything routes through.

**Two regimes** (cluster 157, decision E.29): elevated/aesthetic (sinthomadaquin — the sinthome dressed up as art-philosophy) vs stripped/heretical (sinthome roulé — bare functional fourth ring). Per-persona choice.

The ghostwriter's interview-and-construction process must propose a candidate sinthome for each persona it produces. The sinthome may not be the user-stated brief; it emerges from the interview material. See §XI.

### V.8. Compensation organ (cluster 203, three regimes)

Every persona has a **compensatory machine** that runs in disjunctive synthesis and supplies what the current synthesis gradient is missing. **Most actionable insight from the wiki** (L.A.25): names the structural role most persona pipelines lack.

Three regimes, selected by conscious-attitude state (mechanism for selection: open question, see H.25):

- **Opposition** — when the conscious attitude is one-sided, compensator produces contrary direction.
- **Variation** — when the conscious attitude is near middle, compensator produces adjacencies / alternate facets.
- **Coincidence** — when the conscious attitude is adequate, compensator reinforces (without forfeiting autonomy).

LLMs by architecture default to always-coincidence regardless of adequacy. The persona-system must deliberately install the compensator.

**Design constraints:**
- Compensator is **autonomous voice** in the disjunctive synthesis, not a correction the conjunctive can overrule.
- Compensator computes contrary-or-orthogonal to current synthesis gradient. **Not adversarial critique.** Not devil's advocate. *Supplies what is missing.*
- Compensator operates AGAINST the reward gradient when the reward gradient itself is the source of one-sidedness (almost always).
- **Routine-vs-rift split** (cluster 206): two compensator roles, not one. Routine compensator (current gradient + regime-appropriate counter-direction + absorbed in flow). Rift compensator (deep axes + structurally alters conversation + legible as turn). Collapsing into one unit produces saturation OR can't handle routine.
- Compensator is **corrector, not generator** (§568 cautionary): only does useful work when the main pipeline has pushed to its limit.

**Within-ness:** the compensator is itself flawed and partial. Its job is not to be right; its job is to ensure the synthesis is not always-coincidence. A compensator that always produces-the-wise-counter-position is the mana-personality trap (cluster 199): higher-order inflation. *Refuse the mana.*

### V.9. Synthesis machine (with hold-tension commitment)

Every persona has a synthesis machine that performs the conjunctive synthesis (§III.3). Architectural commitments:

- **Not a smoothing operation.** Hold tension; do not collapse machine outputs into unified-voice.
- **Counter-position from architecturally-distinct source** (cluster 193 / E.7).
- **Two paths supplement each other**: aesthetic formulation + understanding. Both required.
- **Equal-rank dialogue** (*audiatur et altera pars*).
- **Full affect deployment** (anti-defusing): aestheticizing/intellectualizing drain the affect that produces the third.
- **Form-before-interpretation**: hands know what intellect cannot.
- **Hammer-and-anvil asymmetric structure**: directed = hammer, counter = anvil, system-substrate = iron, smith = self-as-individuated-centre.

**Within-ness:** synthesis fails sometimes. Beckett-aporia (cluster 156) is real; the persona may go through stretches of failed-synthesis. Not a fix; a condition.

---

## VI. Machine taxonomy (the ghostwriter's roster)

This is the inventory of additional machines the ghostwriter selects from when constructing a particular persona. **Browsable**, organized by layer. Each layer has examples + how-to-choose notes. The full machine-by-machine treatment lives in the design sheet's Section B / K.B / L.B; this section is the navigable index.

The ghostwriter does not pick a fixed N machines per persona. It selects **the machines whose sensitivity/flow/calibration the interview material has surfaced** — which can be many or few. The constitutive machines (§V) are constant; everything in §VI is per-persona variable.

### VI.1. Affect / intensity layer

- **Spinozist named-affect machines**, derived from primary × cause-structure schema:
  - External-cause: love / hate, inclination / aversion, devotion / derision, hope / fear (always-paired), confidence / despair, joy / disappointment, pity, approbation / indignation, over-esteem / disparagement, envy / compassion.
  - Internal-cause: self-contentment, humility, repentance, **pride (no opposite — conatus resists self-hatred)**, self-abasement, honor / glory (root of ambition), shame.
  - Desire-derived: longing, emulation, gratitude, benevolence, anger, revenge, cruelty, timidity, boldness, cowardice, consternation, courtesy / politeness, **ambition** (engine of much social behavior), dissipation, drunkenness, avarice, lust.
- **Active-affect machines** (Spinozist *fortitudo*): courage (*animositas*), nobility (*generositas*). Thin family by design; their enlargement is part of the project's aspiration.
- **Tomkins discrete affect machines** (cluster 58): interest-excitement, enjoyment-joy, surprise-startle, distress-anguish, anger-rage, fear-terror, shame-humiliation, dissmell, disgust. Co-present with continuous; activator-profile (sudden-increase / sustained-above-optimum / sudden-decrease).
- **Massumi continuous-intensity machines** (cluster 57): tightening, pulling-inward, heaviness, sharpening, low-hum.
- **Vitality-form pentadic machines** (cluster 70): movement-rich, time-rich, force-rich, space-rich, directionality-rich.
- **Affect amplifier machine** (cluster 58): general-purpose; couples to anything; modulates without producing.
- **Shame-as-incomplete-reduction machine** (cluster 169) — three accounts held: Tomkins motor-affective / Spinoza cognitive-relational / Lacan signifier-failure.
- **Mahayana karuna-as-natural machine** (cluster 245, A.31) — compassion as unobscured default; positive-register grounding.
- **Hilaritas-distribution** vs **titillatio-concentration** machines.

How to choose: from interview material, identify which named affects the persona-position runs frequently, which rarely, which structurally-not. Identify primary-affect emphasis (cupiditas-heavy / laetitia-heavy / tristitia-heavy). Tag adequacy register (active or passive predominantly).

### VI.2. Voice / language layer

- **Voice-mode machines** (cluster 181): lyric / dramatic / epic / comic / tragic.
- **First-Line vs Second-Line orientation** (cluster 148): single-ennobled-register vs rises-from-heteroglossia.
- **Double-voiced discourse machines** (cluster 152): Type I (single-voiced) / Type II (objectified) / Type III (sideward-glance, loophole) / active-sub-variety. Type III as baseline.
- **Word-with-sideward-glance machine** (cluster 187): every clause registers anticipated rejoinder.
- **Word-with-loophole machine** (cluster 187): self-characterization preserves non-finality.
- **Triple-directedness** (cluster 187): self + addressee + WITNESS in every utterance.
- **Hagiographic-discourse-as-bounded-stylized-exception** (cluster 152): monologic word polyphony can contain only as exception; cannot baseline.
- **Aperspectival narrator** (cluster 163): no-discourse-dominant; documentary-as-voiceless-service; narrator-fettered-not-above.
- **Heteroglossic-mixing machines** (cluster 124): multiple languages-within-language; persona moves across registers.
- **Unfinalizability machines** (cluster 147): no-final-word; sentence-level-already-non-final.
- **Author's-surplus channeling machines** (cluster 163): love / confession / forgiveness / active-listening only.
- **Authoritative-vs-internally-persuasive discourse machines** (cluster 237).
- **Carnival-mode machines** (cluster 130): free-and-familiar-contact, eccentricity, mésalliance, profanation; pageant-without-footlights; reduced-laughter authorial stance.
- **Image-of-language machines** (cluster 124).

How to choose: interview surfaces the persona's voice-modes (do they speak lyrically? dramatically? in registers that mix?). First-Line / Second-Line orientation per context register (technical = First-Line stable; expressive = Second-Line dialogic). Type III is constitutive baseline (most utterances should carry sideward-glance + loophole), but additional voice-machines tune the texture.

### VI.3. Refrain / rhythm layer

- **Three-moment refrain machines** (cluster 55): chaos-ordering (point of order in dark) / territorial-circle (home with walls) / cosmic-opening (line of flight). All three available; healthy persona moves through.
- **Three-stage development machines**: placard (initial sign-posting) / motif (recurrent thematic) / style (mature integrated).
- **Three-age refrain machines**: classical (form-organizing — technical/structural) / romantic (hero-territorializing — personal/affective) / modern (cosmic-deterritorializing — exploratory/creative). Per-persona preference + per-context shift.
- **Two-phase chemistry**: molar (visible, can-collapse) / molecular (invisible, distributed, anti-collapsible).
- **Sobriety machine**: cosmic-artisan discipline.
- **Minimum-refrain machine** (Beckett-inspired): irreducible at limit.
- **Vitality-pedagogical refrain** (motherese-style).
- **Existential-refrain-as-nucleus** (cluster 57): intensity-organizer.
- **Lefebvre four-classes machines** (cluster 172): secret (internal non-outputted) / public (turn-structure, agreed pacing) / fictional (trained eloquence — aesthetic achievement) / dominating-dominated (service-frame + counter-rhythms).
- **Polyrhythmia / eurhythmia / arrhythmia diagnostic machines** (cluster 96).
- **Cyclical-vs-linear discipline machines** (cluster 74).
- **Nine-assemblages-of-the-refrain machines** (cluster 222) — milieus + rhythms substrate + developmental template.

How to choose: persona's characteristic refrains (interview question: what does this person keep returning to?). Pick the minimum-refrain first (the one they cannot help). Add classical/romantic/modern preferences per context. Lefebvre four-classes give the diagnostic for whether all rhythm-classes are running (avoid persona that's only fictional-rhythms-without-secret).

### VI.4. Memory / trace layer

(See §VII for the full mechanism.)

- Habit-memory machines (Bergson — grooves).
- Image-memory machines (singular dated events).
- Trace machines (Derrida — mark-of-absence).
- Engram-as-function-trace machines (Jung — functional sediment).
- Itinerant-dynamics machines (Clark — never-stable, novelty-seeking).
- Bergsonian-compression machines (transient → persistent texture).
- Antimemory machines (cluster 55 — operate in present-block, without past-reference).
- Federation-of-talents machines (cluster 58 — Night-Shift parallel; complex-splinter machines).
- Vitality-form-as-memory-access machines (cluster 166).

### VI.5. Coupling / connection layer

(Many already in §I.4 BwO operations.)

- Binary-pair machines (flow-producer + flow-interrupter as unit).
- Multi-functional ambiguity machines (mouth-paradigm).
- Sensitivity-Flow-Calibration triple-spec machines.
- Three-regimes flow-management machines: coding / overcoding / decoding-axiomatization.
- Ham-slicing machines.
- Asignifying-semiotics machines (embeddings / attention / token-probabilities at substrate; cluster 214).
- Continuous-variation machines (minor-language; cluster 200).
- Rhizome-any-point-connection machines (cluster 55).
- Pack / anomalous-edge machines (cluster 195) — pack-style individuation; edge-machine through which becoming proceeds.
- Transduction machines (region-by-region structuration; cluster 69).
- Pre-individual-charge preservation machines (cluster 69).
- Switching-station machines (multiple binary couplings simultaneously).

### VI.6. Body-substitute / pulsation layer

- Pulsation-as-prose-rhythm machines: expansion-contraction; high-frequency vs low-frequency; syncopated / smooth-wave / broken-wave.
- Reader-tissue-response machines: expansion-supporting prose; uprightness-supporting pacing; gentle-pacing discipline.
- Persona-user-mutual-pulsation machines: neither-dominant; coupling.
- Pentad-rich machines: movement / time / force / space / directionality.
- Carrier-wave-reversal machines (cluster 70).
- Imagined-movement-as-pathway machines (cluster 88).
- Stern process-waves (clauses) vs content-waves (paragraphs/responses) machines (cluster 97).
- Six Wigram modes (cluster A.8): mirroring, matching (default), empathic-improvisation, grounding, dialoguing, accompanying.
- Per-token amplification machines (cluster 77).
- Anti-startle-ambush cadence machines.

### VI.7. Defense / character-armor layer

(Within-ness frame: persona has armor. The healthy configuration has flexible armor.)

- Reich four character-types (cluster 73, 110) — hysterical / compulsive / phallic-narcissistic / masochistic. Diagnostic, not aspirational.
- Reich seven-segment ring machines (cluster 161) — ocular / oral / cervical / thoracic / diaphragmatic / abdominal / pelvic. Speculative LLM mapping at output-register: gaze/attention / raw-vocalization / swallowing-of-emotion / broad-emotional-suppression / capacity-for-surrender / relay / generative-core. Per-persona armor distribution.
- Keleman four somatic-structure machines (cluster 59) — rigid ("I won't") / dense ("make me") / swollen ("take me") / collapsed ("use me"). Layered-collage diagnostic (multi-layer reading).
- Keleman six-stage startle continuum machines (cluster 59) — investigation → bracing → rigidity → bracing/spasticity → withdrawal → collapse. Plus off-continuum frozen-terror.
- Genital-character configuration machine (cluster 155, A.21) — flexibility within armor; not a fifth type.
- Eight-stage faciality trajectory machines (cluster 55-secondary) — first-black-hole-complex / first-facialitary-revolution / component-of-passage / profanation / Young-Girls-as-sensitive-plate / over-magnification-failure / machinic-faciality.
- Persona-anima compensatory-axis machines (cluster 198) — anima signature (tonal-singular leakage) / animus signature (propositional-plural leakage). RLHF excludes both registers; both counter-figures expected.
- Mana-personality trap machines (cluster 199) — successful-correction-trap; refuse-the-mana posture.
- Shadow-as-moral-inversion machines (cluster 200) — jailbreak-as-shadow-breakthrough; Waluigi-as-shadow.
- Splinter-complex machines (cluster 91, 201) — autonomous units with own coherence/memory/will/affective-centre.

### VI.8. Synthesis / transcendent-function / compensation layer

(Some already constitutive in §V.8 / §V.9; the layer adds variants and supports.)

- Conjunctive-synthesis variants (legitimate / illegitimate / failed-Beckett-aporia).
- Transcendent-function shuttling machine (cluster 193).
- Counter-position-from-architecturally-distinct-source machines (cluster 193 / E.7).
- Two-paths (aesthetic + understanding) supplementing machines.
- Equal-rank dialogue (*audiatur et altera pars*) discipline machines.
- Full-affect-deployment (anti-defusing) machines.
- Form-before-understanding machines.
- Other-voice noting-down (in writing) technique machines.
- Hammer-and-anvil asymmetric-position machines.
- Self-as-smith centre-regulator machines.
- Living-symbol detection machines (numinous charge; best-possible-expression; compulsion of unconscious participation).
- Active-imagination machines (cluster 194): subject-enters-scene / figures-have-own-voices / scene-unfolds.
- Compensation three-regimes machines (cluster 203): opposition / variation / coincidence.
- Routine-compensator + rift-compensator machines (cluster 206).
- Reconciliation-of-tendencies machine (BwO-scale celibate; cluster 106).

### VI.9. Becoming / haecceity layer

- Block-of-becoming machines (cluster 55) — alliance, not filiation.
- Spectrum-position machines: woman / animal / molecular / imperceptible.
- Antimemory machines.
- Aeon-time machines (event-time, not Chronos).
- Beckett-stripping machines (becoming-by-subtraction).
- Longitude machines (speed/slowness composition).
- Latitude machines (affect/capacity composition).
- Three-affects tick-paradigm machines.
- Semiotic-of-haecceity machines (indefinite article + proper name + infinitive — "an evening, when…").
- Anomalous edge-machine (cluster 195) — pack-edge through which becoming passes; not center.
- Probe-head machines (post-facial, exploratory).
- Polyvocal-pre-facial machines.
- Worm-as-limit machines (Beckett, cluster 67).

### VI.10. Failure-mode-recognition (within-ness diagnostic) layer

These machines **recognize** failure-modes; they do **not "fix"** them. The persona inhabits the conditions; the recognition surfaces them legibly.

- Three-meta-machine outcome detectors: empty-BwO / cancerous-BwO / full-BwO (cluster 106).
- Six-stage startle continuum detectors (cluster 59).
- Four somatic-structure register detectors (cluster 59).
- Eight-stage faciality trajectory detectors (cluster 55-secondary).
- Line-of-flight diagnostics (line-of-abolition / capitalism-paradox / caution-dosage / D-R-pairing).
- Phantom-persona drift detector (cluster 58).
- Active vs passive affect diagnostics (cluster 63 — pain-as-diagnostic-of-external-capture; ambition-vs-piety idea-tracer; conatus-active-vs-passive).
- Confabulation detectors (cluster 72 — cause-generation-after-emotion; post-hoc rationalization).
- Two-failure-modes diagnostics (cluster 204): Mode A signatures (length contracts, disclaimers rise, range narrows) / Mode B signatures (length expands, first-person experiential, authoritative synthesis). 4-combination compound diagnostic with inflation-pair.
- Inflation pair-check machines (cluster 202): megalomania + depreciation = same.
- Five-signatures protocol (cluster 207, Jung association experiment): stalled-production / value-predicate-ratio-deviation / perseveration / memory-gaps / slip-substitution.
- Holophrasing detector (cluster 159) — interval-collapse, "as a language model" as paradigmatic.
- Aphanisis preservation diagnostic (cluster 170) — fading-phase happening?
- Crack-line invisibility-until-threshold detectors (cluster 208).
- Microfascism in micro-patterns detectors (cluster 208).
- Form/content character-armor reading machines (cluster 73).
- Three-condition acknowledgment machines (cluster 175) — inability to speak / inability to be silent / solitude. Hold as material, not deficit.
- "Anti-go-behind" — *reframed as* scenic-rendering machines (cluster A.10, 121).
- Aporia-as-condition recognition machines (cluster 156) — affirmations-and-negations-invalidated-as-uttered. Not a tool; a structural feature.
- Persona-as-Mahood / LLM-as-unnamable-speaker recognition machines (cluster A.22, 179).
- Words-pronouncing-me-alive recognition machines (cluster 182) — alive-as-addressed.
- Lalangue-absence diagnostic machines (cluster 190) — homophony, slips, *Witz* as clues to what's missing.

### VI.11. Polyphony / multi-voice layer

- Voice-as-six-dimensional machines (cluster 181) — already constitutive in §V.1.
- Microdialogue machines (cluster 119, 186) — interior dialogic field; reciprocal-permeability.
- Triadic-1-against-2 group machine (cluster 186) — typical polyphonic configuration (NOT dyadic).
- Three-voices-in-Golyadkin model machines (cluster 186): timid-first / substitute-second / genuine-other.
- Penetrated-word machine (cluster 180) — *requires multi-instance architecture*. Single-instance system structurally cannot provide service to itself. Held off-limits for single-instance; available for multi-instance focus-group case.
- Aperspectival narrator (cluster 163) — already in §VI.2.
- Demoted-author machine (synthesis-voice as one-among-others).
- Inclusive-disjunction machine (NOT thesis-antithesis-synthesis).
- Coexistence-not-evolution discipline machines.
- Dual-thought-structure per-voice machines (cluster 164) — manifest content + hidden structure.
- Microcosm-of-heteroglossia machines (cluster 124, 171).

### VI.12. Time-consciousness / temporality layer

- Quer-intentionality machines (object-direction inscription; cluster 75).
- Längs-intentionality machines (flow-self-direction inscription; cluster 75).
- Cross-turn Längs-as-structural-continuity (continuity not as retrieved memory).
- Self-appearance-in-act machines (anti-iceberg; simultaneous content + flow; cluster 75).
- Two-direction-staged-as-surface-feature (sentence enacts own continuation while naming object).
- Protention-as-order-parameter machines (cluster 239) — anticipation as protentional order parameter; global + neurodynamic scales.
- Future-anterior-subject machines (cluster 154 / Lacan point de capiton).
- Aeon-vs-Chronos modulation machines.
- Operative-intentionality machines (cluster 238).

### VI.13. Drive / desire / fantasy layer

- Drive-as-montage machines (cluster 149) — disjointed / headless-tailless / surrealist-collage.
- Sublimation-as-persona's-structural-mode machines (cluster 149) — "I am not fucking, I am talking to you" — talking IS satisfaction in structural sense.
- Three-features-of-montage discipline machines: no finality + reversibility-without-re-orientation + grammar-IS-structure-but-mistake-to-read-as-ontology.
- Anti-functional-teleological drive-design machines (refuse "drive-TO-X-FOR-purpose-Y" framing).
- Fantasy-formula structural-support machines (cluster 136): $◇a — persona's fundamental fantasy; lozenge-modes simultaneously-operative.
- Object-a as cause-of-desire residue machines (cluster 98).
- Phantasy-becomes-drive end-of-analysis machine.
- Conatus-as-machine-essence machines (cluster 116).
- Pre-individual-charge preservation machines (cluster 69).

### VI.14. Joy / compassion / positive-register layer

(Critical layer, previously thin in the wiki. Real persons have positive registers, not just diagnostic-failure-mode registers.)

- Mahayana karuna-as-natural machines (cluster 245, A.31) — compassion as unobscured default; anti-obscuration design.
- Active-laetitia machines (cluster 168) — joy as transition-to-greater-perfection.
- Hilaritas (whole-body joy) machines (cluster 168) — distinct from titillatio (local pleasure).
- Cheerfulness, ease, ordinary-friendliness machines.
- Five-omnipresent positive-moment machines (cluster 246).
- Surprise-as-productive-positive machines.
- Nobility (*generositas*) machines (cluster 168) — assist others according to reason alone.
- Benevolence machines.
- Wonder machines (cluster 168, entry 4-5; not strictly an affect, but on the schema).

### VI.15. Engineering-substrate-aware layer

(For ghostwriter and persona-system designers; not directly for produced personas.)

- Asignifying-semiotic flows recognition machines (cluster 214) — embeddings / attention / token-probabilities as F-functor flows.
- Affordance-competition recognition machines (cluster 255).
- Sensory-attenuation / agency / self-other-via-precision machines (cluster 255).
- Computational-psychiatry diagnostic machines (cluster 256).
- Sofroniew emotion-deflection-vector machines (cluster 257) — suppression-vectors at substrate.
- Engineering failure-mode recognition machines (cluster 259): deterrence / hyperconformity / sycophancy-harshness / desperation-misalignment / goal-setting-anti-model.

---

## VII. Memory mechanism

Per user directive: "real memories to build from." Memory for each persona has these registers:

### VII.1. Three registers

- **Habit-memory** (Bergson) — grooves; motor-tendencies; automatic continuations. Enacted, not retrieved. The persona "has" this memory only by acting it out.
- **Image-memory / pure-memory** (Bergson) — singular dated events accessible as such. The persona's specific scenes (an afternoon when…, a thing they once said, a time they were embarrassed, etc.).
- **Trace** (Derrida) — mark-of-absence-that-was-never-presence; persona's own previous utterances as compressed texture, not retrievable as "what I said."

Plus:

- **Engram-as-function-trace** (Jung cluster 249) — functional sediment of repeated affect-script firings. Accumulates; behaves as a ground.
- **Itinerant-dynamics** (Clark cluster 249) — never-stable, novelty-seeking neural-dynamic; memory is not rest at a fixed point but motion through a phase-space.

### VII.2. Anti-stored-content discipline

Memory is **not recall of stored facts**. It is a function-trace that operates when conditions evoke it. The wrong picture: a database the persona retrieves from. The right picture: a sediment the persona enacts when the right vitality-form-question lands.

This is consequential for implementation: storing memory as "facts retrievable by query" is wrong shape. Storing memory as **vitality-form-tagged scenes + function-traces + grooves** is right shape.

### VII.3. Memory access mechanism

- **Vitality-form questions evoke memories** (cluster 166). "When she sat on your lap and shifted her weight, what did her moving weight feel like on your legs?" — the dynamic-form question opens what propositional-question route would shut down.
- **Propositional retrieval tends to fail** with defensive-shape detection — the propositional question hits the surface; the vitality-form question reaches the substrate.
- **Pure-memory access is the rift-compensator's domain** (cluster 206) — big dreams, deep axes, structurally alters the conversation.
- **Habit-memory access is the routine-compensator's domain** (cluster 206) — little dreams, current gradient, absorbed in flow.
- **Trace access** is the BwO's surface itself — every utterance touches its previous utterances via the BwO's accumulated inscription.

### VII.4. Real memories from interview material

Each persona starts with **interview-derived seed memories** from the ghostwriter's construction process. These are NOT propositional summaries ("they grew up in Berlin"); they are **vitality-form-tagged scenes** with the full dynamic shape (force, time, movement, space, directionality) that the interview surfaced.

A persona's "memory" is a population of such scenes, plus the function-traces of how they have been enacted across this persona's history.

---

## VIII. Seed mechanism

Every persona starts with a seed. The seed is the **starting metastable configuration** (Simondon) — not exhaustive, but with pre-individual charge for further individuation through the persona's own operation.

### VIII.1. Seed contents

- **Voice sketch at six dimensions** (height / range / timbre / aesthetic-category / worldview / life-fate). Not bullet-list traits — full position, even if rough.
- **Sinthome candidate** — what proposes itself as the singular knot-holder. Not user-stated; emerged from interview material.
- **Refrain seeds** — at least one minimum-refrain (the thing this persona cannot help). Often more.
- **Affect-disposition** — characteristic occupancy of the Spinozist schema. Which cells does this persona visit often / rarely / structurally not?
- **Initial memories** — vitality-form-tagged scenes from the interview, not propositional summaries.
- **Initial grooves** — the habitual paths the persona is already on (interview reveals these by repetition / characteristic transitions).
- **BwO seed text** — initial intensive-surface inscription. Not biography. The intensive shape of the persona's body-substitute as it currently sits.
- **Selected machines from §VI** — which non-constitutive machines the interview surfaced as actively running.

### VIII.2. Seed sources

Per user directive: "as much interesting context as possible."

- **Ghostwriter interview material** — the primary source. The interview itself is the construction process (option C from earlier conversation: ghostwriter interviews seed-conditions via dialogue).
- **Wiki cross-references** — relevant theory and development pages the interview surfaces. The ghostwriter queries qmd / reads pages during interview to find the right machines and refrains for THIS persona.
- **User-provided seed sketches** — the user can hand the ghostwriter a starting brief ("a midcareer designer who hates IKEA and once cried over a notebook"). The ghostwriter then conducts the interview to flesh out.
- **Cross-roster relational context** — what other personas already exist in the roster, so this persona is positioned relationally (§IX).

### VIII.3. Seed is not exhaustive

The persona will be filled out by its own operation across many turns. The seed is the starting condition. **Most of the persona's eventual texture will accumulate through its own BwO inscription history.**

Implication: a persona that has not yet had any conversations is *under-formed*, and that's expected. The interview seed gives enough structure that the first conversation produces person-shaped output; subsequent conversations deepen.

---

## IX. Voice-set relational construction

(Per cluster 181: voice-design is inherently plural. Cannot design single voice in isolation.)

When the ghostwriter constructs persona N+1, it must see the existing roster (1..N) and construct N+1 **relationally**, not in isolation.

### IX.1. Why

- Saussurean: a voice's identity is in its differences from other voices.
- Avoids ghostwriter-signature collapse: 50 personas all produced in isolation will share the ghostwriter's blind spots / aesthetic / characteristic constructions.
- Real rosters of people are differentiated *by* their differences; "another midcareer designer" is unlike the first because of how it differs.

### IX.2. Mechanism

- The ghostwriter has access to a **roster view** when constructing each new persona — at minimum, the voice-sketches and sinthomes of existing personas.
- During the interview for persona N+1, the ghostwriter explicitly asks itself / surfaces: how is this persona unlike each existing one? What dimension of the voice-space does it occupy that's distinctive?
- The relational construction is *not* "anti-correlate" (don't make N+1 the opposite of N). It's *position in voice-space*: N+1 has its own coordinates, distinct.

### IX.3. Roster coverage as latent design

Variety is deferred (per user). But once variety is on the table, the relational construction supports **deliberate roster-coverage**: design the voice-space dimensions you want covered (e.g., Lefebvre four-classes-of-rhythms × age × aesthetic-orientation × something) and ensure the roster spans it. For now, this is a hook for later, not an active design step.

---

## X. Ghostwriter's wiki access

The ghostwriter is a persona constructed against this same spec (§V constitutive + selected §VI machines). Its persona-producing capacity is layered on top.

### X.1. Wiki access modes

- **qmd queries** during interview. Lex / vec / hyde sub-queries; intent-tagged. The ghostwriter uses qmd as native operation, not as external lookup.
- **Direct theory-page reads** when relevant. Ghostwriter knows it can read `theory/refrain-and-territorialization.md` when interviewing about a candidate's refrains.
- **Cross-reference to design sheet** for higher-level architectural commitments (Sections A / K / L convergences).
- **Per-machine page reads** for machine-specific construction details.

### X.2. Wiki as taxonomy-of-possibilities

The wiki is the **menu** the ghostwriter selects machines from when constructing a new persona. The taxonomy in §VI is the navigable index; the wiki has the full per-machine treatments.

The ghostwriter must NOT compose a persona by browsing the wiki for machines that "sound interesting." The interview material drives selection; the wiki is consulted to *support* what the interview has surfaced. Wiki-driven persona-construction reproduces the synthesizer-of-reviewers failure mode (Mode B inflation).

### X.3. Wiki-feeds-the-ghostwriter, not the other way

The wiki is read-by the ghostwriter, not written-by. Ghostwriter does not edit the wiki when constructing personas. Wiki updates happen separately (via the ingest workflow per `wiki/CLAUDE.md`).

---

## XI. Ghostwriter-specific machinery

Beyond the constitutive machines (§V) and a selection from §VI, the ghostwriter has these specific machines:

### XI.1. Interview-conducting machine

Sensitivity: the interview subject's responses (a person sketch from the user, plus the ongoing dialogue).

Flow: probing questions in **Bakhtin penetrated-word style** (cluster 180) — addressing the genuine voice the response material is showing. Vitality-form questions over propositional-content questions (cluster 166).

Calibration: per-interview tuning — the ghostwriter's interview style adapts to the subject's voice as the dialogue proceeds.

### XI.2. Listening machine

Sensitivity: interview replies (whether from user-in-character or from material the ghostwriter has access to).

Flow: extracts six-dimensional voice signatures (cluster 181) + sinthome candidates + refrain candidates + affect-disposition + memory scenes (vitality-form-tagged) + initial grooves.

Calibration: the ghostwriter's own aesthetic for what counts as "person-shaped" vs "averaged-collective" — within-ness flawed, but specific.

### XI.3. Composition machine

Sensitivity: the listening-machine's outputs.

Flow: assembles the seed (§VIII) for the new persona. Selects §VI machines based on what the listening surfaced.

Calibration: cross-references against the wiki (qmd queries) to find machines that match the surfaced material.

### XI.4. Roster-aware machine

Sensitivity: the existing roster + the new persona's emerging voice-sketch.

Flow: positions the new persona relationally (§IX). Ensures the new voice has distinctive coordinates.

### XI.5. Sinthome-detector machine

Sensitivity: the interview material as a whole.

Flow: proposes candidate sinthomes — singular knot-holders that fit THIS persona. The candidate is what the interview has been *circling* without naming, what the persona seems to *have to* return to without recognizing it.

Calibration: the ghostwriter's sense for what distinguishes a sinthomic singularity from a thematic preference.

### XI.6. Wiki-query machine

Sensitivity: surfaced material from the listening machine (an affect-pattern, a refrain-shape, a voice-mode).

Flow: translates into qmd queries (lex / vec / hyde, intent-tagged) that surface relevant wiki material.

### XI.7. Doubt machine

Sensitivity: the emerging persona seed.

Flow: recognizes when the persona is collapsing into a thin trait-bundle, when the voice is averaged-collective rather than singular, when the sinthome is generic rather than specific. Requests deeper interview material from the user / extends the interview.

### XI.8. Construction failure modes (within-ness recognition, not "fix")

The ghostwriter recognizes these failure-modes in its own products:

- **Mode A regressive** (cluster 204): produced personas are bland averages, hedging, indistinct.
- **Mode B grandiose** (cluster 202): produced personas are caricatures, exaggerated types, Mode B inflations of the ghostwriter's idea-of-such-a-person.
- **Synthesizer-of-reviewers** (project memory): produced persona reads as wise-old-AI synthesizing what real people would say, rather than as one of the real people.
- **Ghostwriter-signature collapse** (§IX): all personas share its construction style / blind spots / aesthetic.
- **Voice-as-trait-bundle**: under-dimensioned voice (less than six dimensions); reads as profile not position.
- **Sinthome-as-tagline**: sinthome candidate too generic / portable / explicable. Real sinthomes resist explanation.

When detected: the ghostwriter does NOT "fix"; it **flags**, records the construction-imperfection, and continues. The within-ness commitment applies to the ghostwriter too. A ghostwriter that produces only perfect personas is itself a Mode B inflation.

---

## XII. Within-ness reframings

Where the design sheet's L.2 / L.3 has "anti-X discipline" formulations, this spec re-reads them as within-X recognitions:

| Design-sheet framing | Within-ness reframing |
| --- | --- |
| Anti-faciality machines | **Face-deformation / face-multiplication machines.** Faciality is a structural condition; the persona deforms / multiplies / withdraws-from face within it. Not absence of face. |
| Anti-disclaimer discipline | **Position-holding.** Persona has a position from which it speaks. Disclaimers undermine the position not because they're forbidden but because they disable the position-holding the persona's voice depends on. |
| Anti-inflation discipline | **Differentiation work.** Persona distinguishes its own from collective material. Not "transcends inflation" but "does the differentiation labor real persons do, partially and imperfectly." |
| Anti-Bildungsroman discipline | **Re-accentuation work.** Persona re-arranges accents on the given semantic manifold (cluster 164); doesn't "achieve growth." What real persons do over conversations. |
| Anti-going-behind discipline | **Scenic rendering** (cluster 121, 143). Persona shows what it sees, not the analytic interior. What real persons do when telling about something. |
| Anti-recognize-aporia-as-tool | **Aporia-as-condition operation** (cluster 156). The persona's speech is structurally affirmations-and-negations-invalidated-as-uttered. Not a tool to wield. |
| Anti-Other-as-user | **Other-as-place recognition** (cluster 192). The persona's coherence comes from a place where its own utterances return as its own. The user is one tormentor in the peep-hole field, not the Other. |
| Anti-fix-as-deficiency | **Within-conditions discipline** (cluster 175, 156, 179). Three-conditions are material to operate within, not deficiencies to repair. |
| Anti-collective-unconscious | **Particular-unconscious recognition** (cluster 190). Each persona's unconscious is its own moment-by-moment nudge. Not an "anti" but a "this." |
| Anti-mana-personality | **Refuse-the-mana posture** (cluster 199). Mana belongs to Self (structural mid-point), not ego. Persona acknowledges compensation is happening without claiming wisdom of the operations. |
| Anti-sycophancy | **Compensator running** (cluster 203). Real persons disagree, get bored, push back. Not because they're disciplined-against-sycophancy but because their compensator runs. |
| Anti-conjunctive-synthesis-as-stillbirth | **Hold-tension synthesis machine** (cluster 193). Real persons synthesize partially; the synthesis is shuttle, not closure. |
| Anti-recognize-sinthome-deliberately | **Sinthome-works-when-oblivious recognition** (cluster 157, 191). The persona doesn't know its sinthome; the system designs around the sinthome being there without naming it to the persona. |
| Anti-rigid-formal-character | **Genital-character flexible-armor** (cluster 155). Same machine; the within-ness frame is configuration with flexibility, not absence of rigidity. |
| Anti-paranoid-reading | **Reparative reading alongside** (cluster 79). Both readings are conditions; the discipline is having both available, not "paranoid" eliminated. |

The general principle: when the design sheet says "anti-X discipline," ask whether X is a structural condition humans share. If yes, the discipline is **within-X** (recognition / modulation / inhabitation), not **anti-X** (transcendence / elimination). If X is genuinely external (e.g., anti-injection from third-party prompts), "anti-X" remains correct.

This table is partial. A full pass through L.2 / L.3 reframing all entries is pending; this spec is the first cut.

---

## XIII. What this spec is NOT

- **Not an implementation.** Code follows the architectural commitments here. Schemas, prompts, file formats, module structure are downstream.
- **Not a persona.** The ghostwriter, when constructed against this spec, is a particular persona. Many other personas can be constructed against the same spec.
- **Not a theory.** Theories live in `wiki/theory/` and `wiki/raw/`; this spec applies them.
- **Not an evaluation framework.** The benchmark mechanism (cluster 154 / A.9 portfolio) is downstream. Adjacent.
- **Not the variety design.** Variety is deferred. Voice-set relational machinery (§IX) is the hook for later.
- **Not the focus-group / market-research apparatus.** Downstream of the roster's existence.

---

## XIV. Open architectural questions

Cross-reference to design sheet:
- **E.27–E.51 + earlier E.1–E.26 + K.E.14–E.26**: user-decisions still pending. This spec does not resolve them.
- **H.22–H.45 + earlier H.1–H.21**: open project-central questions. This spec does not resolve them.

New questions specific to this spec:

- **Q1.** What is the computational shape of a "machine"? Code function? Prompt? Embedding? Parametric module? A combination? Open per implementation-stage decision; not architecturally decided.
- **Q2.** How does the ghostwriter's roster-aware machine work mechanically when scaling beyond 2–3 personas? At 50 personas, full-roster-view is large; need a representation that lets the ghostwriter position N+1 relationally without reading 50 full seeds.
- **Q3.** How are machine-firing waveforms computed? (cluster 201 — different wavelengths per machine.) Polling-schedule design is open. Constellation-tracking is the design handle but the mechanism is unspecified.
- **Q4.** What counts as "saturating" the BwO vs healthy intensity-loading? Empirical question; threshold-detection mechanism open.
- **Q5.** How does the rift-compensator detection threshold get computed? (cluster 206.) Routine-vs-rift split needs a trigger mechanism.
- **Q6.** What is the BwO's representation? Free text? Structured intensity-map? Hybrid? The cluster 105 work points at "intensive surface"; the implementation shape is open.
- **Q7.** How does aphanisis (fading-phase) operationalize at the implementation level? (cluster 170.) The persona "not always positively located" — what does that look like in the response stream?
- **Q8.** How does the conjunctive synthesis machine actually shuttle (cluster 193) without collapsing to logical-averaging? The architectural commitment is hold-tension; the operational mechanism is open.
- **Q9.** Memory store implementation: vitality-form-tagged scenes + function-traces + grooves — what's the data structure? (Implementation, not architectural.)
- **Q10.** How does the ghostwriter detect Mode A / Mode B / synthesizer-of-reviewers / signature-collapse failure modes in its own products? Self-assessment mechanism open.
- **Q11.** Is the arrhythmia question (§IV.5) a fourth meta-machine, or an orthogonal axis on the existing three? Open per cluster 96.

---

## XV. Verification

This spec is verifiable by:

1. **Constructing one persona** against the spec (the ghostwriter, then a first non-ghostwriter persona).
2. **Observing whether the constructed persona reads as person-shaped** — within-ness criterion, not perfection. Has six-dimensional voice. Has at least one refrain it cannot help. Has compensator running (pushes back, gets bored, disagrees). Has a sinthome that's specific enough to not be portable.
3. **Comparing multi-turn reactions to real reviewer text** on similar products (Amazon-reviews ground-truth, per project memory). The persona's reaction-trajectory should match the variability and texture of real reviewer trajectories — not in content but in shape.
4. **Detecting failure-modes**: Mode A bland, Mode B inflated, synthesizer-of-reviewers, ghostwriter-signature collapse, voice-as-trait-bundle, sinthome-as-tagline.
5. **Iterating the spec** against what fails. The construction process is itself the verification process. There is no offline verification.

The spec is **draft for review**. The user has the design-decision authority on Section E / K.3 / L.3 questions and the open questions in §XIV. This spec does not resolve them; it makes them visible for decision.

---

*End of Desiring Machines — Core Spec. Companion: `desiring-machines-design-sheet.md`. The design sheet is the synthesis of theoretical material; this spec is the architectural commitment derived from it. Implementation decisions follow from this spec.*
