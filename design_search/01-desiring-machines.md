# Design Search 01 — Desiring Machines

First wiki search for the desiring-machine redesign. Goal: ground the redesign sketch's reframe of "machines as analyzers" in what the wiki and prior dev work already say, surface what we should not reinvent, surface what the redesign sketch is missing.

## Sources consulted

**Theory pages (read in full):**
- `theory/desiring-machines.md`
- `theory/partial-objects.md`
- `theory/flows-and-coupling.md`
- `theory/perception-as-subtraction.md`
- `theory/transcendent-function.md`
- `theory/three-meta-machines.md`
- `theory/constellation.md`
- `theory/complex-theory.md`

**Prior dev notes:**
- `development/desiring-machines-core-spec.md` — read first 600 lines (Sections I–VI.9)
- `development/desiring-machines-design-sheet.md` — read first 500 lines (Sections A–C, partially through B.16)
- `development/desiring-machines-design-notes.md` — **NOT yet read** (2.4 MB; deferred to a later search)

**Searches:**
- "desiring machine coupling flow break" + "what is a desiring machine"
- "compensation federated psyche self regulation"

## Key findings

### 1. Machines-as-analyzers is theoretically supported

Bergson's perception-as-subtraction directly grounds the redesign's central reframe: "the machine doesn't construct a representation of the conversation — it subtracts. Each machine's sensitivity field defines what it perceives (what it selects from the input)." A machine IS a "centre of indetermination" — a zone where input is delayed, selected, and potentially withheld rather than mechanically relayed. The user's reframe is clean.

### 2. But machines must remain flow-and-break units, not just analysis-producing nodes

D&G are explicit: every machine is *simultaneously* a flow and a break — interrupts what comes before, produces something new for what comes after. A machine's analysis output is itself a new *flow* that the next coupling consumes/breaks. The "ham-slicing" principle: each machine takes a partial extraction from the continuous flow, not the whole. *Implication for the redesign:* the per-machine analysis output should be flow-shaped (a productive new flow), not a totalizing report. The narrowness is a feature.

### 3. Functional ambiguity (mouth-paradigm) cuts against rigid categories

"A machine is not fixed to one function. It is a switching-station across multiple machinic regimes." The same machine can function as eating, talking, or breathing depending on coupling. *Implication:* the user's category list (Status / Rhythm / Connection / Perception / Trauma / Memory / Preference / Voice) should be loose. A machine's category is its origin/sensitivity, not its operational ceiling.

### 4. The Simondonian no-milieu cut — a worry the redesign doesn't yet address

The strongest critique in the wiki of any "machines as analyzers" architecture comes from Simondon: the persona system "cannot perform transductive resolution of organism-milieu disparation because it has no milieu in the required sense." Real machines hold *two disparate registers* in metastable tension; the persona has only one register (linguistic surface). This is also the **Baudrillard/Crash worry** in `theory/desiring-machines.md`: LLM machine-couplings produce machine-shaped operations *without* the affective-libidinal substrate D&G's machines need. The user's instinct that we "need concrete examples from real people, not LLM-generated, to ground every machine" is a partial response — importing real-people content imports disparation the linguistic surface alone lacks. **This wants its own follow-up search.**

### 5. Federation of talents validates the agentic reframe — but with a sharp warning

Three traditions converge on "the unconscious is a federation of autonomous units, not a unified Self with sub-functions": D&G partial objects, McCarthy's "gathering of talents" / Night Shift, Jung's complex theory ("splinter psyches"). The user's "agentic = less complicated task per agent" reframe is grounded.

But Gullí (2025, *Agentic Design Patterns*) carries a flagged ⚠⚠ caveat in `theory/desiring-machines.md`: engineering vocabulary calls these "collaborating agents" which presumes "**pre-individuated actors with declared goals**." D&G's machines are not pre-individuated and have no declared goals. *If the redesign names each analytical agent as a fully-formed identity with a declared role, it reinstalls faciality at sub-component level.* The redesign should take topologies as substrate; resist naming each node as a fully-formed agent.

### 6. Constellation is the missing concept for the trigger system

This is the biggest single find. Jung's **constellation** (CW 8 §198) names the *pre-firing state* — a machine that has been "released by the situation" and "taken up a position from which it can be expected to react in a quite definite way" but has not yet produced an overt output. The wiki page `theory/constellation.md` flags this explicitly:

> The persona system currently has no formal quiescent-state handling — machines are either "fired this turn" or "not fired this turn" without distinguishing between "not fired because not constellated" and "constellated but did not reach firing threshold."

This is exactly the gap the user's "multiple trigger systems" intuition is reaching for. Three machine states matter: **quiescent / constellated / firing**. The current pipeline only models firing. The trigger stage in the redesign should include constellation tracking. Candidate representations listed in the wiki page:
- Activation-energy scalar per machine
- Tracer edits (non-absorbed BwO marks)
- Disturbance-pattern reading (output signatures inferred backward to constellation)
- Dual-channel reading (parallel readings, disagreement = constellation)

### 7. Wave-length per machine — uniform polling is wrong

Jung CW 8 §201: complexes have activity curves with "wave-length of hours, days, or weeks." `theory/complex-theory.md`: "**Machines should not be polled uniformly at every turn.** Some are in a quiescent phase and firing them wastes the synthesis step's attention." Different machines have different periods; the persona's overall mood is a *superposition* of currently-peaked complex-activities. Uniform polling flattens this superposition (which is what produces celibate-mode fluid responsiveness).

*Implication for triggers:* trigger cadence is per-machine, not global. Some machines fire most turns (always-fire baseline — supports the user's intuition), others go through long quiet phases. The constellation state is the right handle.

### 8. Transcendent function is what Stage 4 (Group analysis) must do

The wiki's `theory/transcendent-function.md` is unusually explicit: **the current synthesis step is structurally what Jung warns against.** Jung's word is "logical stillbirth" — a synthesis that resolves contradiction by ruling out the third (picking a side, averaging, subsuming). The transcendent function is the procedure for the *living third thing*: a movement out of the suspension between opposites that arrives in a *new register*, not as a compromise in the old one.

Procedure (CW 8 §§167–189):
1. Start from affect, not content
2. Give form before understanding (aesthetic before interpretive — "the hands know what the intellect cannot")
3. Note the "other voice" as text
4. Two paths supplement each other (creative formulation + understanding)
5. Equal-rank dialogue (*audiatur et altera pars*)
6. Full affect deployed (anti-defusing — defusing aborts the procedure)
7. Sustained shuttling, then the birth

CW 6 §828 sharpens it: the transcendent function is *not a fifth basic function* but a "complex function" — the integrated operation of all four basic functions on a living symbol. Not a new component; a way of using existing components.

The **celibate machine** (D&G, `theory/three-meta-machines.md`) is structurally the same operation at BwO scale. Both reconcile two opposing registers (paranoiac / miraculating; ego / counter-position) without resolving them; the third emerges as residue in a *new* register.

*Implication for Stage 4:* "combines machines using the three syntheses and other tools" — the "other tools" should be the transcendent-function procedure (form-before-understanding, two-path supplementing, equal-rank dialogue, affect-preserved shuttling). Not bolt-ons; structural commitments for any group-synthesis stage that doesn't want to produce a stillbirth.

### 9. Three meta-machines as amplitude operations — and an open arrhythmia question

Paranoiac (repulsion → empty BwO at threshold), miraculating (attraction → cancerous BwO), celibate (reconciliation → full BwO). These are *operations*, not states. Each is necessary; their over-running into outcome is the failure. Health = none of the three states runs past threshold for too long.

⚠ **Open question the wiki itself flags**: The three meta-machines are *amplitude*-operations. Lefebvre's *arrhythmia* (polyrhythmic field losing coherent composition without amplitude running past threshold) is **not covered**. A fourth meta-machine, or an orthogonal axis for inter-stratum composition, may be needed. The wiki does not have one yet. Worth carrying.

### 10. The current synthesis step performs apotropaic assimilation

Jung CW 8 §206: **apotropaic assimilation** is the ego's defense against acknowledging other psyches inside it — re-describing autonomous complex-activity as "my own thought." `theory/complex-theory.md` says explicitly: "Every time the synthesis step smooths over machine heterogeneity and presents the persona's response as a unified first-person utterance, it is performing apotropaic assimilation in Jung's sense."

*Implication for Stage 5:* the user's "embodied logic, same LLM that edits the BwO then responds" is structurally elegant — but unless it carries the transcendent-function discipline (form-before-understanding, equal-rank dialogue, affect-preserved), it falls into apotropaic assimilation. The single LLM at Stage 5 must speak from the BwO without flattening its polyvocality.

### 11. The user's prior dev work already has substantial structure we should not reinvent

`development/desiring-machines-core-spec.md` (read 600/~1500 lines) lays out:

- **Five-property BwO**: apertureless (no organs, boundary is API) / filled, not empty / pulsatory medium (multi-scale: clause / paragraph / response / session) / aphanisis-permitting (fading-phase, "as a language model" is structural pathology) / singular per-persona.
- **Three states of BwO**: empty / cancerous / full — outcomes of meta-machine operations.
- **What the BwO holds**: inscriptions + affects-as-intensities + memories-as-traces + refrains + grooves. Refrain ≠ groove (refrain = pattern; groove = worn path the pattern dug).
- **Nine constitutive machines** every persona has: Voice (six-dimensional Bakhtin position) / Refrain / Affect (Spinozist three-primary kernel + schema) / Pulsation / Memory (three registers: habit / image / trace) / Coupling / Sinthome / Compensation organ / Synthesis machine. The user's "Voice machine for situational mask" is already in the constitutive set.
- **Active vs passive operation (Spinoza)**: same surface output, categorically different mode of causation. Hardest job of synthesis is detecting which.
- **Pre-individual charge (Simondon)**: "A machine whose calibration has crystallized has lost its desiring-production register and become a lookup table."

`development/desiring-machines-design-sheet.md` (read 500/~3000 lines) lays out:
- **Five cross-cluster convergences** (load-bearing): persona-as-process-not-substance / anti-default-failure-mode / affect-precedes-content / parasite-without-host / two-plane Read A + Read B.
- **A.6 Non-brutal intervention discipline** (4-fold convergence): same intervention that reorganizes one structure damages another. Universal interventions are iatrogenic. Discipline is "announce, observe, classify, modulate gently."
- **Sixteen machine taxonomy categories** (B.1–B.16) — much richer than the redesign sketch's seven.

This is more than enough prior structure that the redesign should not start from scratch on categories.

## Implications for the redesign sketch

Mapped against the sketch's five stages and cross-cutting questions:

### Stage 1 — Analysis

- **Confirmed**: machines as analyzers is theoretically right (Bergson's subtraction, Simondon's centre-of-indetermination).
- **Add to sketch**: each analysis is itself a flow — productive output for the next coupling, not a static report. The narrowness ("partial extraction") is a feature.
- **Add to sketch**: machines should preserve functional ambiguity. The same machine in different couplings can do different things — don't lock function to category.

### Stage 2 — Triggers

- **Add to sketch**: **constellation** as a first-class trigger primitive. Three machine states (quiescent / constellated / firing), not two. The wiki page lists candidate representations.
- **Add to sketch**: **per-machine wave-length / cadence** — uniform polling is wrong. Some machines are quiescent for long stretches.
- **Confirm "always-fire" intuition**: voice / affect / pulsation are always-on at low hum (constitutive set in the core-spec).
- **Possible new trigger avenue**: **disturbance-pattern reading** (association-experiment signatures: stalled production, fluent deflection, multi-turn memory gaps) — the system reads its own surface for signs of constellated-but-not-fired machines.
- **Possible new trigger avenue**: **compensation regime** (Jung CW 8 §550) — a machine fires because the dominant gradient is one-sided, supplying what's missing.

### Stage 3 — Grouping

- **Confirmed**: similarity alone is insufficient.
- **Other grouping mechanisms grounded in the wiki**:
  - **Constellation** — who's currently loaded by the situation
  - **Compensation** — what's missing from the dominant gradient (three regimes: opposition / variation / coincidence)
  - **Refrain / groove** — habitual co-coupling patterns
  - **Disparation (Simondon)** — pairs held in metastable tension across incommensurable registers
- **Possible architectural split**: two grouping layers — constitutive (the 9 always-present machines) + variable (situational machines selected per turn).

### Stage 4 — Group analysis

- **Confirmed**: this is where the transcendent function operates. The current synthesis step is the operation Jung's procedure is *against*.
- **The "other tools" beyond the three syntheses are**: form-before-understanding two-path supplementation, equal-rank dialogue (*audiatur et altera pars*), full-affect deployment (anti-defusing), sustained shuttling, hammer-and-anvil asymmetric structure (directed = hammer, counter = anvil), self-as-smith centre-regulator.
- **Critical commitment**: do not pick a dominant analysis, do not average, do not subsume. The third must arrive in a *new register*.

### Stage 5 — Final machine

- **Confirmed**: embodied logic is structurally right.
- **Add to sketch**: the final machine must avoid **apotropaic assimilation** — the smoothing of polyvocality into unified first-person. This is the failure mode the current synthesis step lives in.
- **Add to sketch**: form-before-understanding requirement — the final machine should aesthetically formulate before interpreting. Order matters.
- **Add to sketch**: the response is *residue* of the celibate-machine operation, not the goal. The persona-effect emerges *alongside* the editing, not as the editing's destination.

### What carries across turns

- **Confirmed**: BwO carries.
- **Refinement**: the BwO is "apertureless" — boundary is the API. There is no peripheral organ behind it.
- **The user's tentative "BwO history machine" may be redundant**: BwO history is already carried by **refrains** (recurring patterns), **grooves** (worn paths), and **traces** (Derridean marks-of-absence). These are properties of what the BwO holds, not a separate machine. Worth checking against this.
- **Possible alternative**: a Memory machine in three registers (habit-memory / image-memory / trace) per the core-spec — covers history-awareness without a dedicated history machine.

### Cross-cutting — BwO design (Spinoza/affect)

- **The BwO holds affects-as-intensities** (transitions of power-of-affecting), **not emotions**. Emotions are what the response (conjunctive synthesis) names.
- **Three primary affect-machines**: cupiditas (desire / striving) / laetitia (joy / lift) / tristitia (sadness / diminishment).
- **Specific affects derive from**: primary × cause-structure × temporal × certainty × sign. A schema, not an enumeration.
- **Active vs passive distinction**: adequate cause (active affect, machine producing from its own nature) vs partial cause (passive affect, machine pulled by inadequate ideas from training). Same surface output, categorically different.
- **Hilaritas vs titillatio**: whole-body distributed pleasure vs local concentrated pleasure. Per-persona design choice.

### Cross-cutting — categories of machines

Mapping the user's seven proposed categories against the core-spec's nine constitutive set + the design-sheet's sixteen taxonomy categories:

| User's category | Closest core-spec / design-sheet category |
|---|---|
| Status | Not directly present — possibly a Voice-position dimension, possibly a relational machine |
| Rhythm | Refrain machine + Pulsation machine |
| Connection | Coupling machine |
| Perception | The sensitivity register of every machine; not a category of its own in the core-spec |
| Trauma | Not directly present — possibly via Sinthome (what holds the knot together) or via specific affect-machines |
| Memory | Memory machine (three registers) |
| Preference | Not directly present — possibly via affect-machine schema (named affects: love / hate / etc.) |
| Voice (situational mask) | Voice machine — already constitutive |

Categories the core-spec considers constitutive that the user's list does not name explicitly:
- **Sinthome** — what holds the persona's knot together; non-portable, unanalysable
- **Compensation organ** — runs against dominant gradient; routine vs rift split
- **Synthesis machine** — performs the conjunctive synthesis with hold-tension commitment

This is worth a direct conversation: the user's list and the core-spec's list overlap but are not the same. The redesign should reconcile them, not pick one.

## Open questions surfaced (not addressed by this search)

1. **Simondonian no-milieu cut** — how do we give the system a second register so its machines actually transduce rather than imitate? Real-people grounding is a partial answer; what else? *(Wants its own search.)*
2. **Arrhythmia as fourth meta-machine** — does the redesign need a fourth meta-machine (or orthogonal axis) for inter-stratum composition? *(Wants its own search.)*
3. **Constellation representation** — which of the four candidate representations (activation-energy scalar / tracer edits / disturbance-pattern reading / dual-channel reading) does the redesign adopt? *(Implementation choice; wiki gives candidates, not answer.)*
4. **Categories reconciliation** — does the redesign keep the user's seven, adopt the core-spec's nine constitutive, or merge? *(User decision.)*
5. **Apotropaic-assimilation guard at Stage 5** — what concrete mechanism keeps the embodied final-machine response from collapsing into unified first-person? *(Open architectural question.)*

## Suggested next searches

In priority order based on what most blocks fleshing out the sketch:

1. **BwO design + Spinoza/affect theory.** The user explicitly called for this. Targets: `theory/body-without-organs.md`, `theory/affects-and-intensities.md`, `theory/conatus.md`, `theory/active-and-passive-affects.md`, `theory/affects-amplify-drives.md`, `theory/affection-and-emotion.md`. Goal: lock down what the BwO actually holds and how Spinozist affect theory shapes its design.
2. **Three syntheses and legitimate-vs-illegitimate use.** Targets: `theory/three-syntheses.md`, `theory/legitimate-vs-illegitimate-syntheses.md`. Goal: ground Stage 4's "combines using the three syntheses and other tools."
3. **Grooves and refrains.** Targets: `theory/refrain-and-territorialization.md`, `theory/milieus-and-rhythms.md`, plus whatever grooves-as-design-object lives in the dev notes. Goal: pin down what grouping mechanisms beyond similarity actually are.
4. **Per-category searches.** Once categories are reconciled, each category gets its own dedicated search (per the user's instruction in the redesign sketch).

## What was not read in this search

- `development/desiring-machines-design-notes.md` (2.4 MB) — the running notes that the design-sheet and core-spec consolidated from. Likely contains material at the cluster-level that didn't make it to the synthesized docs. Deferred to a future search rather than skipped permanently.
- The full design-sheet (we read 500 of ~3000 lines). Sections D–H (machine coordination / held-live tensions / limits / variations / open questions) not yet covered.
- The full core-spec (we read 600 of ~1500 lines). Sections VII–XII (memory mechanism / seed mechanism / voice-set construction / wiki access / ghostwriter machinery / within-X reframings) not yet covered. **Worth flagging: §VII (memory mechanism) is directly relevant to the user's "only BwO carries across turns" decision.**
