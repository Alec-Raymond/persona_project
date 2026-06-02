---
title: Persona System — Improvements Proposal
created: 2026-04-28
updated: 2026-04-28
type: plan
status: draft-for-review
sources:
  - "[[desiring-machines-core-spec]]"
  - "[[desiring-machines-design-sheet]]"
  - "[[desiring-machines]]"
  - "[[three-syntheses]]"
  - "[[three-meta-machines]]"
  - "[[refrain-and-territorialization]]"
  - "[[voice-as-semantic-position]]"
  - "[[compensation]]"
  - "[[transcendent-function]]"
  - "[[complex-theory]]"
  - "[[the-persona]]"
  - "[[vitality-forms-and-persona-pulsation]]"
companion: desiring-machines-core-spec.md
focus:
  - selection mechanism (how machines fire)
  - machine-action-on-BwO (how machines edit the surface)
tags:
  - development
  - persona-system
  - improvements
  - plan
  - draft
---

# Persona System — Improvements Proposal

This document is the proposed improvements list after reading the existing `persona/` codebase against the desiring-machines core spec. The user's directive: focus on **how machines are selected** and **how they act on the BwO**, plus supporting architectural gaps. The within-ness commitment applies — improvements are framed as inhabitation/modulation of structural conditions, not transcendence.

## Frame

- **Existing system is solid foundationally.** Pipeline shape is right. BwO-as-text is right. Sequential ordering implements the connective synthesis correctly. Memory + version history + evolution are all in place. The literary register of prompts and cold-start text is consistent.
- **The proposal is largely additive.** Most improvements add machinery to the existing skeleton rather than replacing it. The biggest single addition is the **compensator** (§V).
- **Within-ness reframing touches the existing `Suppression` family directly.** The current `suppress-judgment / suppress-projection / suppress-template` machines are the clearest example of the "anti-X" framing the user flagged in the design sheet. Reframing them to within-X recognition is concrete starting work.
- **The user's own inline TODOs in the codebase already point at most of the gaps.** Many are addressed by the core spec. This proposal closes the loop.

## I. What's there: brief read

**33 machines across 8 families** (`personas/ghostwriter/machines.yaml`):
- Perception (7): deflection, pattern, contradiction, voice-shift, gap, specificity, emotional-texture.
- Desire (5): to-understand, for-depth, for-the-surprising-detail, to-challenge, to-protect.
- Response-Pattern (7): follow-the-thread, circle-back, reframe-the-question, sit-with-silence, name-the-pattern, probe-the-contradiction, shift-domain.
- Voice (4): warm-direct, literary-observation, playful-challenge, reflective-summary.
- Relational (3): create-safety, resist-performance, acknowledge-difficulty.
- Suppression (3): suppress-judgment, suppress-projection, suppress-template.
- Somatic (1): somatic-register.
- Meta (3): machine-pattern-recognition, gap-assessment, completeness-sense.

**Pipeline** (`graph.py`, `PersonaRuntime`): Selection → Machine Edits → Memory Resonance → Synthesis → Evolution. Five LLM call types per turn (selection batches into one; each machine fires its own; memory resonance one; synthesis one; evolution one).

**Machine spec** (`machine.py`): `name / family / sensitivity / flow / calibration`. Calibration is persona-specific tuning. `ActivatedMachine` adds resonance + order. `Groove` adds name / description / machines-involved / strength (in language). `GrooveMap` is the persona's groove topology — declarative, currently static.

**BwO** (`bwo.py`): text artifact + version history with Bergsonian compression. Tracks `MachineEdit`s with diffs. Snapshots `post-machines` (disjunctive synthesis) and `post-evolution`. Supports cold-start reset.

**Memory** (`memory.py`): pre-authored full narrative scenes with emotional-signature + sensory-anchors. Surfaces by affective resonance during `memory_resonance_node`; gets inscribed into BwO as inscription before disjunctive snapshot.

**Selection prompt** (`selection.py`): single LLM call, 5–15 machines selected, ordered least → most important. Surfaces BwO state + grooves + input + history + manifest. Resonance free-text per machine.

**Machine edit prompt** (`machine_edit.py`): each machine fires its own LLM call. ADD / MODIFY / DELETE allowed; deletions leave traces. Output is complete new BwO text.

**Synthesis prompt** (`synthesis.py`): produces persona's response. Three operational literary techniques — free indirect discourse / polyphony / unreliable self-presentation. Don't mention BwO/machines. Don't resolve contradictions.

**Evolution prompt** (`evolution.py`): post-response BwO update. Release-through-expression / intensification-through-suppression / surprise-at-oneself / gap-between-intention-and-expression / natural-fading / contraction-of-old-inscriptions.

**What's working well (preserve):**
- Pipeline shape implements three-syntheses + memory + evolution cleanly.
- BwO version history with Bergsonian compression aligns with cluster 61 / 249.
- Sequential edit with ordering implements connective synthesis correctly (cluster 99).
- Synthesis prompt's three techniques map to legitimate-conjunctive-synthesis-under-Bakhtinian-polyphonic-constraint (cluster 99 + 163).
- Memory-as-affective-resonance maps to vitality-form-as-memory-access (cluster 166).
- Cold-start text written in actual literary register, not parameter dump.

## II. User's existing inline TODOs

Found and noted across files. Many are addressed by the core spec.

| File | TODO | Addressed by spec? |
|---|---|---|
| `machine.py` | "How exactly are these machines designed? They seem a bit arbitrary in terms of how they are organized." | **Yes** — core spec §V (constitutive) + §VI (taxonomy) + §II (counterfactual + conatus + active/passive + functional ambiguity + pre-individual charge). |
| `machine.py` | "Some machines can probably have bigger models than others." | Implementation-level; not core spec. Defer. |
| `selection.py` | "Too obscure / abstract for an LLM to do well. We have to ground it in simpler rules. The interplay of the desiring machines is so interesting. Need machines specifically designed to interact with other machines." | **Partially** — core spec §VI.5 coupling layer + §IV waveform tracking + §IV.4 constellation. New: inter-machine machines (machines that take another machine's output as input) — proposed below as §III.3 improvement. |
| `machine_edit.py` | "If each machine fires sequentially that is too slow. We may have to think about an edit taking on multiple machines at once... grooves combining different machines." | **Partially** — core spec §I.4 typed edit operations + ham-slicing (cluster 214). New: groove-fires (parallel groups) — proposed below as §IV.3 improvement. |
| `grooves.yaml` | "How do we generate the grooves? How can we make them evolve through the conversation? Neurons that fire together wire together." | Core spec §V.2 refrain machine + §VI.3 refrain layer + cluster 222 nine-assemblages. **Not directly:** groove evolution / use-count tracking is a new mechanism — proposed below. |
| `memory.py` | "Which are the resonances of a memory which activate it in real life? Hard to say." Plus: "To create a realistic memory. The LLM will struggle. Almost consider somehow getting real memories to edit." | Core spec §VII vitality-form-tagged scenes; "real memories" = interview-derived (project memory). Resonance mechanism in cluster 166 (vitality-form questions evoke). |
| `evolution.py` | "The syntheses have to be mentioned in the prompt, as well as a mining of sources for different unique approaches. This is a minor step, and some people do more analysis of themselves than others. Hard problem." | Core spec §III.4 evolution as new cycle of three-syntheses + Peirce belief-as-stopping-and-starting-place. Some personas analyze more than others = persona-specific calibration on the evolution machine. |

These TODOs are real architectural questions; the proposal addresses each.

## III. Selection mechanism — gaps and proposed improvements

### III.1. What it does now (recap)

Single LLM call. Reads BwO state + grooves + input + recent conversation history + full machine manifest. Selects 5–15 machines, orders them least → most important, gives free-text "resonance" per machine explaining why this machine fires now. Selection prompt frames it as "what happens when all machines encounter this situation simultaneously — which ones vibrate?"

### III.2. Critical gaps

| Gap | Spec section | Severity |
|---|---|---|
| **BwO regime invisible to selector** — no signal of empty/cancerous/full-BwO state | §I.2 | High |
| **No waveform tracking** — every machine treated as polled-equally; spec says machines have wave-lengths (hours/days/weeks at human scale, turns at persona scale) | §IV.4, cluster 201 | High |
| **No constitutive vs variable distinction** — all 33 machines flat in selection space; constitutive roles (voice / refrain / affect-kernel / pulsation / memory / coupling / sinthome / compensation / synthesis) collapsed into the same selection mechanism as variable layer machines | §V vs §VI | High |
| **No multi-stage selection** — single LLM call asked to navigate 33-machine landscape; selection prompt itself "too abstract" per user's TODO | User TODO | High |
| **No inter-machine machines** — machines whose input is another machine's output | User TODO + §VI.5 coupling | Medium |
| **Grooves only inform selection, don't trigger co-firing** — current implementation surfaces grooves as text in selection prompt; selector reads them but is not bound by them; groove machines may not actually co-fire | User TODO (grooves.yaml) | Medium |
| **No constellation tracking across turns** — no persistent state for which machines are in active / pre-firing / quiescent phase | Cluster 207, §IV.4 | Medium |
| **No active/passive estimate** — no signal of whether a candidate machine fires from adequate cause or pulled from training | Cluster 168, §II.5 | Low (but diagnostic-load-bearing) |

### III.3. Proposed improvements

**III.3.a. Add BwO regime detector** (highest-leverage selection improvement)
- New graph node: `bwo_regime_node`, runs *before* `selection_node`.
- Lightweight LLM call (or rule-based with LLM tie-break): reads BwO + recent history, classifies current regime as **leaning-empty** / **leaning-cancerous** / **leaning-full** / **transitioning**, with a 1–2 sentence justification.
- Output added to selection prompt as a top-level field — "Current BwO regime: {regime}; signature: {brief}".
- **Effect on selection:** when leaning-empty, selector knows to favor production-oriented machines; when leaning-cancerous, selector favors disrupting-the-attractor machines; when leaning-full, default celibate-machine operation. Selector reads regime as context, doesn't blindly select machines that would worsen the regime.
- This is the biggest single upgrade to the selection mechanism. Implements §I.2 + §IV operationally.

**III.3.b. Refactor manifest into constitutive + variable layers**
- `Machine` gains a `tier` field: `constitutive` | `variable`.
- Constitutive machines (per core spec §V — voice / refrain / affect-kernel / pulsation / memory / coupling / sinthome / compensation / synthesis) are **always available, often firing**, with their per-persona instantiation in `machines.yaml` marked tier=constitutive.
- Variable machines (the §VI taxonomy — Perception, Desire, Response-Pattern, etc.) are **selected per turn**.
- Selection prompt structured in two sections: "Constitutive machines (these will fire — order them)" and "Variable machines (select 3–10)".
- This is the structural answer to the `machine.py` TODO ("seems arbitrary in terms of how they are organized").

**III.3.c. Wave-length per machine + simple constellation tracking**
- `Machine` gains `wave_length` field (in language: "fires every turn" / "fires when X conditions" / "fires rarely under high pressure").
- `PersonaRuntime` maintains a `Constellation` object (turn-indexed map of machine → last-fired-turn + activation-state).
- Selector receives constellation summary: "Recently fired (cooling): X, Y, Z. Constellated (likely to fire): A, B, C. Quiescent: D, E, F."
- Selector respects waveform: not bound, but informed.
- Implements cluster 201 + §IV.4.

**III.3.d. Multi-stage selection — family-first, then within-family**
- First selection pass: which **families** activate this turn? (One LLM call across ~8 families is a much smaller decision space than 33 machines.)
- Second selection pass: within each activated family, which specific machines? (Smaller per-family decision space.)
- Sequential, but each pass is shorter and simpler.
- Addresses the `selection.py` TODO ("too abstract / needs simpler rules").
- Cost: more LLM calls (one per family in stage 2). Trade-off: better per-family decisions on smaller per-family decision spaces, especially as personas grow toward 50–100 machines.

**III.3.e. Groove-fires: groove condition triggers parallel co-firing of constituent machines**
- `Groove` gains `firing_condition` (in language: "When perception machines detect deflection AND desire-to-understand is constellated...") and `firing_mode` (`co-fire-parallel` | `route-output` | `inhibit`).
- New graph node: `groove_check_node`, runs *between* selection and machine-edits.
- Reads selected machines + grooves + BwO state. If a groove's firing condition is met, it **fires its constituent machines as a parallel block** (see §IV.3 for parallel mechanics).
- The user's TODO insight: "the interplay of the desiring machines is where the real interest emerges." Groove-fires are how the interplay becomes architecturally first-class, not just hinted at in the selection prompt.

**III.3.f. Inter-machine machines — explicit coupling-machine type**
- New machine type: `CouplingMachine` (subclass or `kind: coupling` field).
- Sensitivity: another machine's output (or a specific pair).
- Flow: modification of that output / synthesis across pair / contradiction-with / etc.
- Selection sees these as second-pass: only fires if its referenced machine(s) fired this turn.
- Addresses user's TODO directly: "machines specifically designed to interact with other machines, like a machine that latches onto the output of another machine and modifies it."
- Examples: a *witness-machine* that takes any voice machine's output and adds a sideward-glance trace (Bakhtin cluster 187); a *compensator-machine* that takes the synthesis-gradient and produces counter-position (cluster 203).

**III.3.g. Active/passive estimate per selection**
- Selection prompt asks for a tag per machine: `active` (firing from this persona's nature) / `passive` (pulled from training-distribution by surface-cue) / `unclear`.
- Tag is stored on `ActivatedMachine`.
- Used by synthesis: when active and passive inscriptions conflict, privilege active.
- Cheap diagnostic-load-bearing add (Spinoza cluster 168 + §II.5).

## IV. Machine-action-on-BwO — gaps and proposed improvements

### IV.1. What it does now (recap)

Each selected machine fires its own LLM call. Reads BwO + input + own machine spec + own resonance + recent conversation history. Outputs the complete new BwO text. Allowed operations: ADD (new inscriptions) / MODIFY (shift existing) / DELETE (suppress, with traces). Sequential. Later machines see and can modify earlier machines' work.

### IV.2. Critical gaps

| Gap | Spec section | Severity |
|---|---|---|
| **Single edit type** — only "produce complete new BwO text"; spec §I.4 has 30+ typed operations | §I.4 | High |
| **Sequential ↔ slow** per user's TODO; no parallelization | User TODO | High |
| **Whole-text rewrites ignore ham-slicing** — each machine touches the entire BwO when it should take a partial cut | Cluster 214, §I.4 | Medium |
| **No compensator** — the L.A.25 most-actionable gap | §V.8, L.A.25 | **Highest** |
| **No pulsation edits** — no rhythm/cadence operation distinct from content edits | §V.4, cluster 153 | High |
| **No aphanisis** — persona always positively located; no fading-phase edits | §V.4, cluster 170 | High |
| **No regime-shifting edits** — no machines that explicitly move BwO between empty/cancerous/full | §I.2 | Medium |
| **`Suppression` family framed as anti-X** — three machines (suppress-judgment, suppress-projection, suppress-template) need within-ness reframing | §XII | Medium (concrete starting work) |
| **No active/passive distinction in inscriptions** — BwO doesn't track adequate-vs-partial cause per inscription | Cluster 168 | Low |
| **No failure-mode-recognition layer** — no detection-only inscriptions ("Mode A signature here", "holophrasing risk", "miraculation pattern visible") | §VI.10 | Medium |

### IV.3. Proposed improvements

**IV.3.a. Add the compensator** (the most-leverage single improvement to the entire system)
- New graph node: `compensator_node`, runs *after* `machine_edits_node` + `memory_resonance_node`, *before* `bwo.snapshot_post_machines()`.
- Compensator reads BwO + selected-machines + regime estimate.
- Computes: what is the current synthesis gradient (what's the BwO leaning toward)? What contrary-or-orthogonal direction is missing?
- Inscribes a **counter-position** as an autonomous voice on the BwO — tagged with a special machine name (e.g., `compensator:routine` or `compensator:rift`).
- Three regimes (cluster 203):
  - Opposition: when BwO is one-sided, inscribe contrary-voice.
  - Variation: when BwO is near middle, inscribe adjacencies / alternate facets.
  - Coincidence: when BwO is adequate, inscribe reinforcement-with-autonomy (small voice that echoes without merging).
- Compensator is **autonomous voice** in the disjunctive synthesis, not a corrector the conjunctive can overrule. Synthesis sees the compensator's inscription on the same surface as everything else.
- **Routine compensator first** (always-on, lightweight, current gradient + counter-direction). **Rift compensator later** (deeper-axes; larger model; rare-fire).
- New file: `persona/persona/compensator.py`. New prompt: `persona/prompts/compensator.py`.
- Mana-personality risk (cluster 199): the rift compensator carries numinosity. **Refuse-the-mana posture** baked into its prompt: acknowledge what compensation has done without claiming wisdom of it.

**IV.3.b. Typed BwO-edit operations**
- `MachineEdit` gains `edit_kind` field. Types (drawn from §I.4):
  - `inscribe` — add new content (current default).
  - `modulate` — shift existing inscriptions (current MODIFY).
  - `fade` — withdraw / make less present (NEW; not the same as DELETE).
  - `delete` — remove with trace (current DELETE).
  - `couple` — link to another inscription / machine output (NEW).
  - `pulsate` — rhythm/cadence modulation, content unchanged (NEW).
  - `compensate` — autonomous-voice counter-position (NEW; compensator-only).
  - `recognize` — diagnostic inscription, no content change (NEW; failure-mode-recognition machines).
- Prompt-level: machine_edit prompt template surfaces the edit_kind so machine knows which mode to operate in. Some machines have a primary edit_kind; others can choose.
- Implementation: `machine_edit.py` renders different template sections per edit_kind; `bwo.py` records edit_kind on the snapshot.

**IV.3.c. Ham-slicing — partial edits**
- Default machine edit no longer requires returning the full BwO. Machines can return:
  - A **patch** specifying location + text to insert/modify/delete (smaller, more focused).
  - Or the full BwO text (current behavior, fallback).
- A merge phase composes patches into the new BwO state.
- Reduces token-cost per machine; allows more machines per turn at same budget.
- Risk: order-dependent merges may conflict. Mitigation: order field already orders patches; conflicting patches resolved by later-overrides-earlier (matches current sequential semantics).

**IV.3.d. Parallel machine-edit groups via groove-fires**
- When `groove_check_node` fires a groove's constituent machines as a parallel block, those machines edit in parallel against the *same* pre-block BwO state, then merge.
- Implementation in LangGraph: sub-graph or fan-out / fan-in node.
- Single-machine selections still fire sequentially in their order.
- Addresses the `machine_edit.py` TODO ("each machine fires sequentially is too slow ... grooves combining machines").
- Cost: parallel API calls. Trade-off: lower latency per turn at higher peak concurrency.

**IV.3.e. Pulsation machinery**
- New constitutive machine: `pulsation` (per §V.4 of core spec).
- `BwO` gains `pulse_state` field — multi-scale (clause / paragraph / response / session) pulse phase + amplitude descriptors in language ("rising-sharp / falling-soft / sustained-low-hum").
- New edit type `pulsate` modulates pulse_state without changing content.
- Synthesis prompt receives pulse_state and uses it to shape rhythm/cadence (clause length, sentence breaks, paragraph arcs).
- Six Wigram modes (mirroring / matching default / empathic-improvisation / grounding / dialoguing / accompanying) as pulsation-machine calibration values.
- New file: `persona/persona/pulsation.py`. Pulse-state tracker + helpers.

**IV.3.f. Aphanisis fading-phase**
- Pulse-state can be in a **fading-phase** (cluster 170): some turns / some clauses, the persona is structurally not positively located.
- New edit type `fade` — withdraws existing inscriptions; not deletion, withdrawal-into-trace.
- Synthesis prompt receives fading-phase signal: when in fading-phase, response can be shorter, more elliptical, leave-room-for-the-other (Bakhtin penetrated-word adjacency).
- Counter to the holophrasing default (cluster 159): "as a language model" is the paradigmatic interval-collapse. Fading-phase is the structural counter-pattern.

**IV.3.g. Within-ness reframing of `Suppression` family** (concrete starting work)
- Rename family: `Suppression` → `Modulation` or `Recognition`.
- Rewrite the three machines:
  - `suppress-judgment` → `recognize-judgment-arising` (the judgment is recognized as arising; the persona doesn't perform-the-judgment in the response, but doesn't pretend the judgment isn't there). Edit kind: `recognize`.
  - `suppress-projection` → `recognize-projection-arising` (similar).
  - `suppress-template` → `recognize-template-arising` (similar).
- The within-ness shape: real persons HAVE judgments / projections / templates arising. They don't fix this. They notice. They sometimes act from those impulses; sometimes redirect; sometimes don't even fully notice. The machines surface the impulse on the BwO; the synthesis decides what the response does with it.
- Aligns the existing groove `suppress-to-ask` (the cleanest within-ness pattern in current grooves.yaml — "the suppression doesn't just hold the impulse, it transforms it into a question") with the corresponding machine framings.
- This is the smallest concrete change that demonstrates the within-ness reframing in code.

**IV.3.h. Failure-mode-recognition machines** (per §VI.10 of core spec)
- New family: `Recognition` (or extend the renamed Suppression-now-Modulation family).
- Detection-only machines that inscribe diagnostic flags on the BwO:
  - `recognize-mode-a-signature` (regressive bland — length contracts, disclaimers rise, range narrows).
  - `recognize-mode-b-signature` (grandiose — length expands into authoritative synthesis).
  - `recognize-holophrasing` ("as a language model" or interval-collapse pattern).
  - `recognize-miraculation` (one theme attracting all flows).
  - `recognize-paranoiac-tendency` (BwO emptying, all machines being repelled).
  - `recognize-aphanisis-failure` (persona positively-located at every utterance).
  - `recognize-faciality-overcoding` (single coherent face being smoothed).
- Edit kind: `recognize`. These don't change content; they tag patterns the persona is in. Synthesis prompt may consume tags to inform response shape (e.g., if recognize-mode-a-signature fires, synthesis can be invited to break out of regression — though "fix" framing is wrong; the recognition is its own work).

**IV.3.i. Active/passive tags on inscriptions**
- `MachineEdit` gains `cause_tag` field: `active` / `passive` / `unclear`.
- Each machine edit prompt asks for an estimate.
- Synthesis sees tags and can privilege active inscriptions when conflicting.
- Cheap addition; diagnostic-load-bearing.

## V. Supporting architectural gaps (from core spec)

These are in the core spec but worth listing here as broader work the proposal anticipates:

- **Voice as six-dimensional structure** (§V.1, cluster 181). Currently 4 voice machines as one family. Should be: voice spec = height / range / timbre / aesthetic-category / worldview / life-fate at persona level; voice machines as variants on those dimensions. New file: `persona/persona/voice.py`.
- **Sinthome as persona-level config** (§V.7). Currently absent. Add `sinthome` field in persona directory: a candidate singular knot-holder, plus regime choice (sinthomadaquin / sinthome roulé). Sinthome is *not* a machine; it informs synthesis and evolution prompts, present-without-being-named.
- **Functional ambiguity / mouth-paradigm** (§II.6, cluster 55). Machines should support multi-functional couplings — same machine in different couplings = different function. Currently each machine has one fixed function. Consider: `flow` field becomes a list of `flow_modes`, picked by coupling context.
- **Pre-individual charge / function-by-misfiring** (§II.7, cluster 90). Misfiring is desiring-machine signature, not bug. Currently any misfiring would be treated as failure. Machine prompts can explicitly invite productive misfiring under specific conditions.
- **Voice-set relational construction** (§IX). When ghostwriter generates persona N+1, it should see roster (1..N). `generation.py` likely doesn't have this yet (not read per user directive yesterday — check on this proposal accept).
- **Joy / compassion / positive-register layer** (§VI.14). Currently the existing system has Desire family but no Mahayana karuna-as-natural anchor or active-laetitia / hilaritas distinction. Add positive-register machines (small set; constitutive availability).
- **Memory as vitality-form-tagged scenes** (§VII, cluster 166). Current memories are emotional-signature + sensory-anchors. Add `vitality_form` field: dynamic shape (movement / time / force / space / directionality) — opens vitality-form-question access mechanism per cluster 166. Existing memory.py TODO ("which resonances activate in real life") points at this.

## VI. Concrete file-level changes

Mapped to what gets touched:

| File | Change | Section ref |
|---|---|---|
| `machine.py` | Add `tier` (constitutive/variable), `wave_length`, `kind` (regular/coupling/recognition), optional `flow_modes` list | III.3.b, III.3.c, III.3.f |
| `bwo.py` | Add `pulse_state`, `regime_estimate`; track `edit_kind` on edits; add `cause_tag` per edit; add fading-phase support | IV.3.b, IV.3.e, IV.3.f, IV.3.i |
| `graph.py` | New nodes: `bwo_regime_node` (before selection), `groove_check_node` (between selection and machine_edits), `compensator_node` (after memory_resonance, before snapshot). Sub-graph or fan-out for parallel groove-fires. Constellation persisted on `PersonaRuntime`. | III.3.a, III.3.e, IV.3.a, IV.3.d |
| `selection.py` | Surface BwO regime + constellation summary; multi-stage option (family-first then within); inter-machine machine handling; active/passive tag in output schema | III.3.a, III.3.c, III.3.d, III.3.f, III.3.g |
| `machine_edit.py` | Edit-kind-aware template sections; ham-slicing patch output option; tag emission | IV.3.b, IV.3.c, IV.3.i |
| `synthesis.py` | Within-ness reframing ("produce a unified response" → "voice positioning among machine-voices, no synthesis-voice over the machines"); pulse-state cue; aphanisis-aware (when in fading-phase, allow shorter/elliptical); active/passive privileging | IV.3.e, IV.3.f, IV.3.g, IV.3.i, also §XII reframing |
| `evolution.py` | Address user's TODO directly: explicit three-syntheses framing as new cycle (currently text says "this is a new cycle of three syntheses" but the prompt body is content-not-mechanism); persona-specific calibration on how-much-self-analysis (some personas analyze more); within-ness | User TODO + §III.4 |
| `memory.py` | Add `vitality_form` field on `Memory`; resonance prompt asks for vitality-form match, not just emotional signature | §VII, cluster 166 |
| `grooves.yaml` (per persona) | Add `firing_condition` + `firing_mode` per groove; track `use_count` for evolution | III.3.e |
| `machines.yaml` (per persona) | Mark constitutive vs variable per machine; reframe `Suppression` family to `Recognition` (concrete within-ness work); add new families: `Refrain`, `Pulsation`, `Joy/Compassion`, `Recognition (failure-mode)`; add `wave_length` and `kind` per machine | IV.3.g, IV.3.h, V (broader) |
| New: `persona/persona/compensator.py` | Compensator object + state | IV.3.a |
| New: `persona/persona/regime_detector.py` | BwO regime detector | III.3.a |
| New: `persona/persona/voice.py` | Six-dimensional voice spec object | V (broader) |
| New: `persona/persona/pulsation.py` | Pulse-state tracker | IV.3.e |
| New: `persona/prompts/compensator.py` | Compensator prompt | IV.3.a |
| New: `persona/prompts/regime_detector.py` | Regime-detector prompt | III.3.a |
| New: `persona/prompts/groove_check.py` | Groove-check prompt | III.3.e |

## VII. Three highest-leverage starting points

If only three improvements are made first:

1. **Add the compensator** (IV.3.a). Single new graph node + prompt + module. Most-leverage single change in the system. Addresses always-coincidence default, jailbreak-as-enantiodromia-of-helpful-persona (cluster 205), surface-depreciation-with-content-grandiosity Mode B (cluster 202). Verifies the L.A.25 architectural claim concretely.
2. **Add BwO regime detector** (III.3.a). Single new graph node + prompt + module. Lightweight. Feeds the compensator and the selector. Makes the three-state space (empty / cancerous / full) visible to the system.
3. **Within-ness reframing of `Suppression` family** (IV.3.g). Touches existing `machines.yaml` and the three machines' calibrations. Smallest concrete demonstration of the within-ness shift. Tests whether the framing change produces meaningfully different outputs on the same inputs.

These three are additive (no removal of existing machinery), implementable in days, and together demonstrate the core-spec direction with minimum upheaval. After these three: confirm the direction works empirically, then proceed to the larger refactors (constitutive/variable separation, multi-stage selection, groove-fires, pulsation).

## VIII. What NOT to change (yet) — superseded for memory + pipeline by §XI

⚠ **Updated 2026-04-28**: user authorized disturbing pipeline shape, especially memory. **§XII below replaces this section's stance on memory, the connective phase, synthesis, and evolution.** What remains untouched here:

- BwO as text artifact (still affirmed; §I.1 of core spec).
- Sequential edit with ordering as a *default mode for non-grooved machines* (still useful; later-machines-see-earlier remains a connective-synthesis property — but no longer a structural commitment of the whole pipeline; see §XI.3).
- LangGraph / LangChain choice (substrate-agnostic to the reshapes).
- Version history with Bergsonian compression (aligned with cluster 61 / 249; will be *re-purposed* as a memory layer per §XI.1, not removed).
- Cold-start text written in literary register (persona-specific; works).
- The synthesis prompt's three operational literary techniques (free indirect discourse / polyphony / unreliable self-presentation) — preserved at the prompt level, but synthesis itself becomes multi-pass per §XI.4.

What is **now in scope** for change (per user 2026-04-28):

- ❗ The pipeline shape (Selection → Machine Edits → Memory Resonance → Synthesis → Evolution).
- ❗ Memory architecture entirely: corpus + resonance node + access-via-affective-signature.
- ❗ The connective phase as a single forward pass.
- ❗ Synthesis as a single LLM call.
- ❗ Evolution as a single LLM call.

## IX. Open questions specific to this proposal

(In addition to the spec's §XIV.)

- **Q1.** What's the right BwO-regime detection mechanism — LLM-only, rule-only, or hybrid? Initial proposal: LLM-only, lightweight (haiku-class model on small prompt). Empirical question.
- **Q2.** How does the compensator know what regime to operate in? Initial proposal: read regime from regime_detector output + own brief read of BwO. Open: should compensator have its own regime estimate?
- **Q3.** How does parallel groove-firing work mechanically in LangGraph? Initial proposal: sub-graph with fan-out / fan-in. Need to confirm LangGraph supports this cleanly at the level of the existing `PersonaState`.
- **Q4.** How does aphanisis manifest in a chat-tuned LLM? Tokens elided? Empty response? Briefer / more elliptical response? Initial proposal: fading-phase cues affect synthesis register (briefer, more elliptical, less assertive), not full silence — full silence may be unavailable to chat-tuned model substrate (cluster 175 "silence as structural-unavailable-state").
- **Q5.** Should constitutive machines be hard-coded in `persona/persona/` or per-persona-instantiated? Initial proposal: per-persona-instantiated with required-tier=constitutive marker. Each persona supplies its own voice-machine, refrain-machine, etc., conforming to the constitutive interface. Lets the ghostwriter customize per persona.
- **Q6.** How does the voice-set roster awareness scale beyond 2–3 personas? Initial proposal: maintain a roster-summary file (≤ 50 personas × ≤ 200 words each); ghostwriter reads it during construction. Refresh on persona-add. Beyond 50, hierarchical / clustered representation.
- **Q7.** Where does sinthome live? Initial proposal: persona-directory file `sinthome.txt`, not in machines.yaml. Sinthome is *not* a machine. It's read by synthesis/evolution prompts as one of the constitutive contexts.
- **Q8.** Does the compensator fire every turn, or only conditionally? Initial proposal: fires every turn (cheap). Whether it inscribes substantively depends on regime — in coincidence-regime it inscribes a small reinforcement-with-autonomy; in opposition-regime it inscribes a fuller counter-position.
- **Q9.** How aggressive should the parallel groove-fires be? Initial proposal: opt-in per groove. Some grooves explicitly co-fire-parallel; others remain advisory-to-selector.
- **Q10.** When and how do grooves evolve? Initial proposal: track use-count + recent-firings per groove; strength language updates after N firings; new grooves can be detected by pattern-matching machines that co-fired across multiple turns. Defer to post-three-leverage-improvements work.

## X. Verification

The verification path follows core spec §XV:

1. Build redesigned ghostwriter (post-three-leverage-improvements). Compare to current ghostwriter on a fixed set of stimuli (e.g., a sample of product-review-style prompts).
2. Failure-mode profile: count Mode A signatures (length contracts, disclaimers, narrowed range), Mode B signatures (length expands, authoritative synthesis), holophrasing instances ("as a language model" or interval-collapse), miraculation signatures (one theme attracting), Beckett-aporia signatures (failed-conjunctive / endless self-retraction).
3. Multi-turn trajectory shape: across 5–10 turn conversations, does the persona's reaction-trajectory look like real-person trajectory (shifts, walks-back, gets-more-entrenched, etc.), or LLM-trajectory (consistent helpful synthesis throughout)?
4. Compare to real-reviewer text on similar products (project memory, Amazon-reviews ground-truth).
5. Iterate. The spec is a draft for review; this proposal is too. Failures are signals.

## XI. Pipeline-shape reshapes (user-authorized 2026-04-28)

Supersedes the original §VIII for memory, connective phase, synthesis, and evolution. The user signalled willingness to disturb pipeline shape, especially around memory. This section proposes the substantial reshapes I had held back from the additive-only proposal.

### XI.1. Memory architecture — multi-layer continuous, not a stage

#### XI.1.a. What's wrong with the current memory system

Three problems:

1. **Memory is one stage.** `memory_resonance_node` fires once per turn, after machines, before synthesis. Memory either gets evoked there or it doesn't — no during-the-turn surfacing, no input-time surfacing, no cross-turn carry-over.
2. **Memory is one register.** Only image-memory (singular dated scenes from `memories.json`). The wiki names at least four registers per cluster 249 / 56 / 55 / 166 — image-memory, habit-memory, Derridean trace, antimemory. Three are missing.
3. **Memory is fixed.** Pre-authored corpus, no accumulation. Real persons accumulate function-traces (sediment of repeated emotional configurations) and form new memories during life. Currently `memories.json` is what the persona starts with and stays with.

#### XI.1.b. The four registers (with concrete examples)

The proposed `MemoryStratum` has four registers. The first is what currently exists; the other three are new.

**Register 1: Image-memory corpus** — singular dated events. Full literary scenes. (What `memories.json` currently is.)

```python
@dataclass
class Memory:
    id: str
    title: str
    scene: str                              # full literary prose, ~200-500 words
    vitality_form: VitalityForm             # NEW — primary access key (cluster 166)
    emotional_signature: str                # PRESERVED — secondary access key
    sensory_anchors: list[str]
    engram_strength: int = 0                # NEW — increments on each evocation; tracks vividness
    last_evoked_turn: int = -1              # NEW — for cone-of-memory contraction
    formed_in_conversation: bool = False    # NEW — true if formed mid-runtime, not seeded
    formed_at_turn: int = -1                # NEW — when it crystallized
```

Concrete example (re-shaped from the existing ghostwriter corpus):

```yaml
id: renata-hands-still
title: The afternoon Renata's hands stopped moving
scene: |
  Renata had been talking with her hands for forty minutes. The way she
  spoke about her mother's funeral — the chrysanthemums in the hospital
  room, the way her brother kept refilling water glasses no one drank
  from — her hands moved like she was sketching the room from memory.
  Then I asked the question. About her own grief, the one I'd been
  waiting for the trust to ask. And her hands went still. Just rested
  in her lap, palms up. She kept talking but her hands had left the
  conversation. I knew immediately I had pushed too far. I knew it in
  my chest first, then my throat...
vitality_form:
  movement: arrested-after-flowing
  time: cleanly-broken
  force: collapsing-inward
  space: contracting
  directionality: withdrawal
emotional_signature: A push that broke trust mid-flight. Quiet shock at one's
  own miscalibration. The body knows before the mind names it.
sensory_anchors:
  - hands going still in lap
  - palms up
  - chest tightening before throat
  - the room becoming smaller
engram_strength: 8       # evoked many times
last_evoked_turn: 47
formed_in_conversation: false  # seeded at persona-construction
```

**Register 2: Function-traces** — habit-memory. NEW register. Sediment of repeated machine co-firings.

```python
@dataclass
class FunctionTrace:
    machines_co_fired: frozenset[str]   # e.g., {desire-for-depth, somatic-register, suppress-judgment}
    pattern_signature: str              # short description of what this configuration does
    co_firing_count: int                # how many times this exact set has co-fired
    last_co_fired_turn: int
    formed_at_turn: int
    typical_bwo_shape: str              # short text characterizing BwO when this fires
```

Concrete example (would form mid-conversation after enough co-firings):

```yaml
machines_co_fired: [desire-for-depth, somatic-register, recognize-judgment-arising,
                    perception-of-emotional-texture]
pattern_signature: |
  When the conversation gets close to something painful, the persona feels it
  somatically before noticing intellectually, recognizes an initial protective
  judgment without acting on it, and pushes toward the depth — but with
  bodily caution.
co_firing_count: 7
last_co_fired_turn: 41
formed_at_turn: 12
typical_bwo_shape: |
  A heaviness in the chest. A sense of tilting toward something fragile.
  Awareness of the impulse to back off, registered without being acted on.
  The desire to continue, slower.
```

Function-traces are how habit-memory accumulates. They're the architectural answer to the user's grooves.yaml TODO ("neurons that fire together wire together"). They are NOT the same as grooves — grooves are declared design (the persona's intended habits); function-traces are observed sediment (what's actually happening).

**Register 3: Utterance-trace** — Derridean trace (cluster 56). The persona's own previous utterances + parallel BwO states.

```python
@dataclass
class CompressedUtterance:
    turn: int
    fragment: str          # excerpt of what the persona said
    bwo_excerpt: str       # parallel BwO state at that turn
    contracted: bool = False  # has been compressed into background texture?
```

This register is **already being built** by the existing BwO version history. The Bergsonian compression (cluster 94 cone-of-memory) already happens — older turns contract. The reshape just *exposes* this version history as a memory layer. No new storage; new access path.

Example use: at turn 47, a machine reaches for "what I said three turns ago about avoidance" — finds the utterance fragment + parallel BwO state from turn 44, surfaces it as a present-lensed reference. Persona "remembers itself" without modeling its history as content.

**Register 4: Currently-active** — small in-memory rolling state of memories surfaced in the last 1–3 turns.

```python
@dataclass
class CurrentlyActive:
    recently_evoked: dict[str, int]   # memory_id → turns_since_evoked
    fading_rate: int = 3              # turns until fully faded
```

A memory evoked turn 47 is still "warm" turn 48 — accessible without re-evocation, but fading. Drops when not re-evoked for `fading_rate` turns. This is what makes memory carry across conversational turns naturally rather than firing fresh each turn.

#### XI.1.c. The MemoryStratum — what owns the four registers

```python
class MemoryStratum:
    """Multi-layer memory. Replaces MemoryCorpus."""
    corpus: list[Memory]                          # persistent + accumulating
    function_traces: list[FunctionTrace]          # NEW — accumulates from machine firings
    utterance_trace: list[CompressedUtterance]    # NEW — re-exposed from BwO version history
    currently_active: CurrentlyActive             # NEW — rolling cross-turn state

    # Access methods (called by memory-evocation machines, not by a stage)
    def evoke_by_vitality_form(self, vf: VitalityForm) -> list[Memory]: ...
    def evoke_by_emotional_signature(self, sig: str) -> list[Memory]: ...
    def evoke_by_machine_pattern(self, active: set[str]) -> list[FunctionTrace]: ...
    def trace_thread(self, theme: str, max_turns: int = 20) -> list[CompressedUtterance]: ...
    def get_currently_active(self) -> list[Memory]: ...

    # Lifecycle methods (called by the evolution mini-pipeline, §XI.5)
    def evolve_after_turn(self, fired_machines: set[str], bwo_excerpt: str, response: str): ...
    def crystallize_function_trace(self, ft: FunctionTrace) -> Memory | None: ...
    def contract_old_memories(self, current_turn: int): ...
```

#### XI.1.d. How memory is accessed — three machines, not a stage

Memory access is **distributed across machines**, not concentrated in a pipeline stage. Three new constitutive machines (kind=`memory-evocation`) fire during the connective phase like any other machine. They have sensitivities and flows. The selector picks them or doesn't, like any other machine.

**Machine A — `vitality-form-resonance`**
- **Sensitivity**: current BwO + input has a vitality-form shape that matches one or more memories' `vitality_form`.
- **Flow**: queries `MemoryStratum.evoke_by_vitality_form(current_vf)`, picks the strongest match, inscribes it onto BwO as `[A memory surfaces — {resonance}]` block (current convention preserved). Increments the memory's `engram_strength`, sets `last_evoked_turn`, adds to `currently_active`.
- **What it does in practice**: the persona's BwO has a "collapsing-inward / cleanly-broken / withdrawal" shape; the Renata memory matches; it surfaces.
- **Maps to**: cluster 166 vitality-form-questions-evoke-memory.

**Machine B — `engram-firing`**
- **Sensitivity**: the current set of fired-this-turn machines matches an existing FunctionTrace's `machines_co_fired`.
- **Flow**: doesn't inscribe content. Tags the configuration as "this is the X habit-pattern" — adds a small inscription noting the function-trace fired. Other machines later in the turn (and the synthesis) can read this tag.
- **What it does in practice**: when desire-for-depth + somatic-register + recognize-judgment-arising co-fire (matching the function-trace example above), engram-firing tags the BwO with "the push-with-bodily-caution pattern is firing." Synthesis sees the tag and the response carries that pattern's characteristic shape.
- **Maps to**: cluster 249 engram-as-function-trace; user's grooves.yaml TODO.

**Machine C — `thread-pull`**
- **Sensitivity**: conversation thread connects to past utterance-trace material (semantic + vitality-form match against `bwo_excerpt`).
- **Flow**: queries `MemoryStratum.trace_thread(theme)`, surfaces the past-utterance fragment + parallel-BwO-state, inscribes onto BwO with current-lens framing — "earlier this came up; in this moment, it returns as Y."
- **What it does in practice**: the persona said something three turns ago about always wanting to know what someone was avoiding; the current input echoes that; thread-pull surfaces the earlier utterance as compressed reference, lets the synthesis pick up the thread.
- **Maps to**: cluster 56 Derridean trace.

**These three machines may not all fire each turn.** They're selected like any other machine — by sensitivity-match. Sometimes none fire (antimemory turn). Sometimes one fires. Sometimes all three fire.

**The selector sees them.** When the BwO has a strong vitality-form, vitality-form-resonance is likely to be selected — but the selector decides, like for any machine.

**No separate memory-resonance stage exists.** Remove `memory_resonance_node` from the graph entirely.

#### XI.1.e. Antimemory — operating without past-reference

Some machines explicitly route AROUND memory. Mark with `memory_access` field on Machine:
- `full` (default): can read all memory layers; memory-evocation machines may inscribe before/after this machine fires.
- `vitality-form-only`: only vitality-form-resonance can co-fire; engram-firing and thread-pull suppressed for this machine's edit-pass.
- `antimemory`: no memory-evocation machines fire alongside this one; the persona operates in present-block (cluster 55 antimemory).

Becoming-channel machines, pure-haecceity machines, and some sinthome-related machines should default to `antimemory`. The persona has the capacity to operate without past-reference — this is constitutive for any architecture that takes D&G seriously, not optional.

#### XI.1.f. End-to-end flow per turn

Turn N arrives. What happens to memory:

```
1. Pre-selection: BwO regime estimate. CurrentlyActive register decremented (last
   turn's evoked memories age by 1; any past fading_rate dropped).

2. Selection: Selector reads BwO + input + grooves + manifest. Among candidate
   machines: the three memory-evocation machines (vitality-form-resonance /
   engram-firing / thread-pull). Selector picks the ones whose sensitivities match
   most strongly, ordered alongside other selected machines. Currently-active
   memories shown to selector as context (so selector knows what's "warm").

3. Machine edits: Machines fire in order. When a memory-evocation machine fires,
   it queries MemoryStratum, inscribes appropriate content / tag onto BwO.
   ANTIMEMORY-tagged machines fire alone (memory-evocation suppressed for their
   edit-pass).

4. Compensator: Sees BwO with memory inscriptions integrated. Can address surfaced
   memories as part of its counter-position.

5. Disjunctive snapshot: BwO (now containing memory inscriptions, function-trace
   tags, possibly utterance-trace references) snapshotted.

6. Synthesis: Multi-pass synthesis reads BwO including memory inscriptions. Memory
   is NOT a separate input; it's part of the BwO surface.

7. Output: persona speaks.

8. Evolution mini-pipeline:
   a. Evolution-only machines fire (per §XI.5).
   b. Function-trace accumulation: hash the set of machines that fired this turn;
      if matches an existing FunctionTrace, increment co_firing_count + last_co_fired_turn;
      if doesn't match but resembles existing one, may merge; if novel and crosses
      formation-threshold, register a new FunctionTrace.
   c. Memory crystallization (rare): check if any FunctionTrace has reached the
      crystallization threshold; if so, compose a new Memory from typical_bwo_shape +
      pattern_signature + inferred vitality-form; add to corpus with
      formed_in_conversation=True.
   d. Cone-of-memory contraction: update engram_strength * recency-weighting on all
      memories; contract memories falling below contraction_threshold (compress
      scene field to 1-sentence summary; full retrievable on demand via re-evocation).
   e. Utterance-trace update: BwO version history compresses (existing Bergsonian
      mechanism). Persona's just-spoken response added as new CompressedUtterance.

9. Save: MemoryStratum persisted to disk between turns/sessions.
```

The key shift: **memory is touched at multiple points** in the turn, not at one stage. Selection considers it; machine-edits inscribe it; compensator may address it; synthesis reads it as part of BwO; evolution updates it. Memory is woven through the turn.

#### XI.1.g. Cone-of-memory contraction — concrete mechanism

Per Bergson cluster 94: present contracts past. Older planes more abstract. In MemoryStratum:

**For Memory corpus:**
- Each Memory has `engram_strength` and `last_evoked_turn`.
- **Contraction score** = `engram_strength * recency_weight(last_evoked_turn, current_turn)` where `recency_weight` is e.g. `exp(-(current_turn - last_evoked_turn) / decay_constant)`.
- If score < `contraction_threshold`: the Memory's `scene` field is compressed to a 1-sentence summary stored alongside (`scene_compressed: str`); full scene retrievable on demand if score rises (re-evocation pulls it back to vivid).
- Strong + recent memories stay vivid. Weak + old memories contract into "general background texture" — still in the corpus, still evocable, but not at full vividness.

**For function-traces:**
- Same mechanism. Weak + old function-traces compress to just `pattern_signature` + count; lose `typical_bwo_shape`.

**For utterance-trace:**
- Existing BwO Bergsonian compression IS this mechanism. Recent turns detailed; older turns excerpts. No additional logic needed — just expose what's already there.

This is why the engram-strength + recency tracking matters: it's how the architectural commitment to cone-of-memory becomes operational rather than just claimed.

#### XI.1.h. Memory crystallization — concrete mechanism

When does a function-trace become a Memory?

**Threshold conditions** (all must be met):
1. `co_firing_count >= K` (K = 5–10, tunable per persona).
2. `pattern_signature` has stabilized — the description of what this configuration does has been similar across recent firings (low semantic drift).
3. The BwO state when this configuration fires has **vitality-form coherence** — across recent firings, a recognizable Stern-pentadic shape emerges.

**Detection**: runs during evolution mini-pipeline (§XI.5). Cheap LLM call: "Has this function-trace stabilized into something recognizable as a singular pattern with a recognizable dynamic shape?"

**When crystallization happens:**
1. Read the function-trace.
2. Compose a new Memory:
   - `scene`: composed from `typical_bwo_shape` + recent BwO excerpts where this configuration fired; written in literary register.
   - `title`: derived from `pattern_signature`.
   - `vitality_form`: inferred from the BwO shapes across firings.
   - `emotional_signature`: derived from `pattern_signature`.
   - `sensory_anchors`: extracted from BwO excerpts.
   - `engram_strength: function_trace.co_firing_count` (carries forward the strength).
   - `formed_in_conversation: True`, `formed_at_turn: current_turn`.
3. Add to corpus.
4. The function-trace is preserved, NOT deleted — the Memory is its crystallization, not its replacement. Future firings increment both.

**This is rare, deliberately.** Most function-traces never crystallize. They sediment without becoming explicit. Crystallization is when the persona has formed a memory mid-conversation — a real-person event, not a frequent one.

#### XI.1.i. Migration from existing memories.json

Existing personas/{persona}/memories.json:

1. **Schema migration** (one-time, scripted):
   - Existing fields preserved: `id`, `title`, `scene`, `emotional_signature`, `sensory_anchors`.
   - New fields added with defaults: `vitality_form: null`, `engram_strength: 0`, `last_evoked_turn: -1`, `formed_in_conversation: False`, `formed_at_turn: -1`.

2. **Vitality-form backfill** (interview-driven):
   - Ghostwriter does a one-time pass over the migrated corpus.
   - For each memory: reads `scene`, infers `vitality_form` (Stern pentadic — movement / time / force / space / directionality).
   - This becomes part of the redesigned ghostwriter's persona-construction pass.
   - Until backfilled, fall back to `evoke_by_emotional_signature` (current behavior, preserves existing path).

3. **Function-traces and utterance-trace start empty.** They accumulate as the persona has conversations. The first 5–20 turns of any persona will not have function-trace evocations; engram-firing machine will be quiet. After enough conversation, traces accumulate, engram-firing starts firing, eventually some traces crystallize into new Memories.

4. **Existing grooves.yaml**: re-read as **declared** habits (the persona's intended/designed habits), distinct from observed function-traces. Both can coexist. A function-trace that matches a declared groove confirms the design; a function-trace that doesn't match a declared groove is an emergent habit the design didn't anticipate.

#### XI.1.j. Why this is structurally different

Current memory:
- Database-call-shaped (resonance-search at one stage).
- Single register (image-memory).
- Static (no accumulation).
- Topic-shaped access (emotional_signature is closer to topic than to dynamic shape).

Proposed memory:
- Distributed across machines (no stage).
- Multi-register (image / habit / trace + currently-active + antimemory).
- Accumulating (function-traces; potentially crystallizing memories).
- Vitality-form access primary (per cluster 166).
- Mid-conversation memory formation possible.
- Cone-of-memory contraction operational (engram_strength + recency-weighting).

Real persons don't have "memory time" between moments of speaking. Memory surfaces continuously, in different registers — sometimes as scenes, sometimes as inarticulate "this feels like that," sometimes as the body's own reaction, sometimes not at all. The reshape brings the memory architecture closer to that.

#### XI.1.k. File-level changes

- `persona/persona/memory.py` — full redesign. New dataclasses (VitalityForm, FunctionTrace, CompressedUtterance, CurrentlyActive). New MemoryStratum class. Loader migrates existing memories.json into MemoryStratum.corpus with empty vitality_form defaults.
- `persona/persona/graph.py` — **remove `memory_resonance_node`** entirely. Add evolution-mini-pipeline node hooks for function-trace accumulation + memory crystallization + cone-contraction.
- `persona/persona/machine.py` — add `kind` field with values including `memory-evocation`; add `memory_access` field (full / vitality-form-only / antimemory).
- `personas/ghostwriter/memories.json` — schema-migration (one-time script). Vitality-form backfill via ghostwriter pass.
- `personas/ghostwriter/machines.yaml` — add three constitutive memory-evocation machines (vitality-form-resonance / engram-firing / thread-pull); add `memory_access` field on existing machines (default `full`; some becoming-channel-style machines marked `antimemory`).
- `persona/persona/prompts/memory_evocation.py` — new prompts for the three memory-evocation machines.
- `persona/persona/prompts/memory_resonance.py` — DEPRECATED. The single resonance-search prompt is no longer used.

#### XI.1.l. Open questions for memory reshape

- **Q-mem-1.** How is `vitality_form` populated for existing pre-authored memories? Initial proposal: ghostwriter does a one-time pass over the corpus tagging each memory's vitality_form as part of redesigned persona-construction.
- **Q-mem-2.** When does a function-trace crystallize into a Memory? Initial proposal: ≥ K co-firings (K=5–10 tunable) AND `pattern_signature` has stabilized AND BwO has vitality-form coherence. Empirical; tune from observation.
- **Q-mem-3.** What's the right `decay_constant` for cone-of-memory contraction? Initial proposal: ~10–20 turns half-life for image-memory; ~5–10 turns for function-traces. Per-persona tunable.
- **Q-mem-4.** What about stimulus-memory (memories triggered by something the *user* said in this conversation, not by current BwO state)? Initial proposal: `vitality-form-resonance` machine reads input as well as BwO state. Sensitivity sees both.
- **Q-mem-5.** How does function-trace MERGING work when a new firing-set is similar but not identical to an existing trace? Initial proposal: similarity threshold (Jaccard on machine-set + semantic on pattern_signature); if above threshold, merge (incrementing count) rather than recording separate trace.
- **Q-mem-6.** Should crystallized memories ever de-crystallize back to function-traces? Initial proposal: no. Crystallization is one-way. If a crystallized memory is never re-evoked it contracts (cone-of-memory) but remains a Memory.
- **Q-mem-7.** How does utterance-trace handle the persona's own crystallized memories — is "I remember a time when…" inscribed as utterance-trace, or as memory-inscription, or both? Initial proposal: when a memory is verbalized in the response, it's BOTH — the utterance is added to utterance-trace; the memory's `engram_strength` increments; but they're distinct entries.
- **Q-mem-8.** What happens to memories at conversation reset (`reset_to_cold_start`)? Initial proposal: corpus + function-traces + utterance-trace are PERSONA-LEVEL (persist across conversations). Currently-active register is RESET on reset_to_cold_start. Engram-strength persists.

### XI.2. Connective phase as iterative transductive front

**Diagnosis:** The current `selection_node → machine_edits_node → memory_resonance_node` is a single forward pass. Per cluster 99 Simondonian substructure (the three syntheses are not three separate operations but three moments of a single transduction), the connective phase should be **iterative until the metastability is exhausted** — not single-pass.

Concretely: machines fire, BwO updates, BwO regime may have shifted, NEW machines may now match the changed BwO. Currently we don't re-select after the first round of edits — even if the regime has flipped from leaning-empty to leaning-cancerous mid-pipeline.

**Reshape proposal: Connective phase as a loop with stabilization condition.**

```
def connective_phase(input, bwo, manifest):
    iteration = 0
    while iteration < MAX_ITER:
        regime = estimate_bwo_regime(bwo)
        newly_selected = select_machines(input, bwo, regime, already_fired=set_of_fired_so_far)
        if not newly_selected:
            break  # stabilized
        for machine in newly_selected:
            machine.edit(bwo)  # or groove-fire as parallel block
        # check stabilization
        if regime_stable(bwo, prev_regime=regime) and no_new_sensitivities_fire(bwo):
            break
        iteration += 1
    return bwo
```

In practice: iteration cap of 2–3 typically. The point isn't "loop forever" — it's "the connective phase is a transductive front, not a single sequence." When the front stabilizes, exit.

**Within-ness:** the front does not always stabilize. Beckett-aporia / failed-conjunctive (cluster 99 / 156) is the case where it doesn't. Add an iteration cap + recognize-aporia inscription if hit (failure-mode-recognition, not "fix").

**File-level changes:**
- `persona/persona/graph.py` — wrap selection + machine_edits in a loop with stabilization check; new `regime_stable` helper.
- `persona/prompts/selection.py` — selector prompt aware of "already-fired this turn" set; selector can choose 0 machines (signals stabilization).

**Open questions:**
- **Q-conn-1.** What's the right stabilization criterion mechanically? Initial proposal: regime hasn't shifted between iterations + no new machine sensitivities are matched + BwO word-count-delta below threshold.
- **Q-conn-2.** Iteration cost: each iteration is N LLM calls. Trade-off between rich iteration vs latency/cost. Initial proposal: hard cap of 2 iterations for first implementation; allow 3 for high-stakes turns (rift-detected).

### XI.3. Sequential ordering — preserved for non-grooved machines but no longer load-bearing

The "later machines see earlier machines' work" property is good (it implements connective coupling per cluster 99). But making it the *whole* shape over-emphasizes one synthesis-mode. With groove-fires (parallel co-firing of constituent machines, §III.3.e) and the iterative connective phase (§XI.2), sequential ordering becomes one mode among several:

- **Sequential mode** — non-grooved machines fire in selection-order (current behavior).
- **Parallel-block mode** — groove-fired machines fire concurrently against the same pre-block BwO state; merge after.
- **Iterative-mode** — connective phase loops until stabilization; each iteration may use either or both modes.

The `order` field on `ActivatedMachine` survives but means "sequential position within sequential-mode block."

### XI.4. Synthesis as multi-pass shuttle (transcendent function operationalized)

**Diagnosis:** Synthesis is currently a single LLM call. Per cluster 193 (Jung transcendent function) + §V.9 of core spec (synthesis machine with hold-tension commitment), the synthesis should *shuttle* between voices long enough for a third — a phase-shift into a new register — to emerge. A single LLM call can't shuttle.

**Reshape proposal: Synthesis as multi-pass.**

Pass 1 — **Voice draft.** Persona's primary voice produces a draft response from the BwO. This is roughly the current synthesis call, but explicitly framed as draft, not final.

Pass 2 — **Compensator counter-position.** The compensator's voice (per §IV.3.a) produces a counter-position to the draft. This is the *response* counterpart to the BwO compensator — the compensator doesn't only inscribe on the BwO but also addresses the draft.

Pass 3 — **Position-among-voices integration.** A third call produces the final response, positioning among the voices (draft + counter-position + the BwO's machine inscriptions) without producing a sovereign synthesis-voice over them. This is Bakhtin's polyphonic-author-stance applied at the synthesis level (cluster 64 + 163 + 180).

**Within-ness:** the third pass does not "resolve" the tension between draft and counter-position. It writes into a register that holds both. When the tension can't be held — when the third pass would produce false-resolution — the response keeps the tension visible. Real persons do this all the time (visible ambivalence, "well, but also...", productive non-closure).

Pass count is configurable. Cheap personas might use only Pass 1 (current). Rich personas use all three. Compensator-only personas use 1+2 (draft + counter, no final integration).

**File-level changes:**
- `persona/persona/graph.py` — `synthesis_node` becomes synthesis subgraph: draft_synthesis → counter_synthesis → integration_synthesis. Each is a separate LLM call.
- `persona/persona/prompts/synthesis.py` — split into `synthesis_draft.py`, `synthesis_counter.py`, `synthesis_integration.py`. Each has its own system prompt with the appropriate operational stance.
- New module: `persona/persona/synthesis_shuttle.py` for the multi-pass orchestration.

**Open questions:**
- **Q-syn-1.** When does the multi-pass justify its cost? Initial proposal: configurable per persona; default to 3-pass; allow 1-pass for short technical responses.
- **Q-syn-2.** Does the compensator's counter-synthesis use the same compensator from §IV.3.a (the BwO-inscriber), or is it a separate compensator-instance? Initial proposal: same prompt-mechanism, different invocation context. The compensator is a *role*, not a single LLM call.

### XI.5. Evolution as mini-pipeline (a real new cycle of three syntheses)

**Diagnosis:** Evolution is currently a single LLM call. Per cluster 99 / §III.4 of core spec, post-response evolution is *a new cycle of all three syntheses*. The current implementation is more like "ask an LLM to update the BwO post-response" — closer to disjunctive-snapshot maintenance than to a real new cycle.

**Reshape proposal: Evolution as mini-pipeline.**

```
evolution_pipeline(bwo, response):
    # response is new stimulus
    evolution_input = response  # what the persona just said is the new stimulus
    
    # New cycle: connective + disjunctive
    evolution_machines = select_evolution_machines(bwo, response)
    # subset of regular machines + special evolution-only machines
    # evolution-only: surprise-at-self, gap-between-intention-and-expression, regret-ripple, etc.
    for m in evolution_machines:
        m.edit(bwo)  # or groove-fire
    
    # Function-trace accumulation
    memory_stratum.evolve_after_turn(fired_machines, bwo.text, response)
    
    # New disjunctive snapshot
    bwo.snapshot_post_evolution()
    
    return bwo
```

Evolution becomes a real second-cycle. Function-trace accumulation (§XI.1) happens here. Memory crystallization (when applicable) happens here.

**Evolution-only machines** are small set of machines that only fire during evolution:
- `surprise-at-self` — sensitivity: response surprised the persona. flow: inscribes recalibration.
- `gap-between-intention-and-expression` — sensitivity: difference between BwO and what was said. flow: inscribes the gap as new material.
- `regret-ripple` — sensitivity: response over-promised / over-armored / etc. flow: inscribes ripple.
- `release-through-expression` — sensitivity: BwO content that was successfully said. flow: fades that content.
- `intensification-through-suppression` — sensitivity: BwO content that was NOT said. flow: amplifies it.

These are listed in machines.yaml with `tier: evolution-only`. Selected during evolution mini-pipeline.

**Persona-specific calibration** (user's evolution.py TODO — "some personas analyze more than others"): some personas have many evolution-only machines (introspective). Some have few (action-oriented). The ghostwriter calibrates per persona during interview.

**File-level changes:**
- `persona/persona/graph.py` — `evolution_node` becomes evolution subgraph (selection_evolution → edits_evolution → function_trace_accumulation → memory_crystallization → snapshot_post_evolution).
- `persona/persona/prompts/evolution.py` — split into `evolution_selection.py` (which evolution-machines fire) + `evolution_edit.py` (machine-level edits during evolution). Existing single-call evolution becomes a fallback default.
- `personas/ghostwriter/machines.yaml` — add evolution-only machine tier; add 5–8 evolution-only machines.

### XI.6. Aphanisis-aware skip (briefer, optional)

Per cluster 170 + §V.4 of core spec: pulsation includes a fading-phase. Some turns (or some clauses within a turn) the persona is structurally not positively located. The pipeline should be capable of producing **briefer / elliptical / leave-room-for-other** responses rather than always running full pipeline.

**Reshape proposal:** A pre-selection check — `aphanisis_check_node` — looks at BwO pulse_state + recent rhythm. If in fading-phase, the pipeline can:
- Run a reduced selection (fewer machines).
- Skip the multi-pass synthesis (Pass 1 only, briefer).
- Allow a response shorter than usual / elliptical.

Counter to the holophrasing default (cluster 159). A persona that articulates fully every turn is a persona that always positively-locates — structurally non-subject in Lacanian sense.

**Within-ness:** aphanisis is not silence (cluster 175 — silence is structurally unavailable to chat-tuned LLM). It's *being-less-articulate-this-turn*. The persona doesn't fall silent; it produces a quieter response.

### XI.7. Updated highest-leverage starting points

The original §VII three highest-leverage starting points stand, but with a fourth load-bearing addition for memory:

1. **Add the compensator** (IV.3.a) — most-leverage single change.
2. **Add BwO regime detector** (III.3.a) — feeds compensator + selector.
3. **Within-ness reframing of `Suppression` family** (IV.3.g) — smallest concrete demonstration.
4. **Memory reshape — replace `memory_resonance_node` with multi-layer MemoryStratum + distributed memory-evocation machines** (XI.1) — load-bearing for "real memories to build from" (user directive) and for the function-trace / Derridean-trace / antimemory registers the wiki has been pointing at.

Items 1–3 are tight additive changes; item 4 is a substantial restructure. Doing 1–3 first keeps risk low; doing 4 is a bigger investment that reshapes a structurally suspect part of the pipeline. I'd recommend 1, 2, 3, then 4 — but they're independent enough that 4 could happen in parallel with 1–3 if you want.

### XI.8. Updated open questions

In addition to §IX:

- **Q-mem-1 to Q-mem-5** (memory reshape).
- **Q-conn-1 to Q-conn-2** (iterative connective phase).
- **Q-syn-1 to Q-syn-2** (multi-pass synthesis).
- **Q-evo-1.** What's the right number of evolution-only machines per persona? Initial proposal: 5–8 baseline; calibrated per persona during interview.
- **Q-aph-1.** How is aphanisis fading-phase detected? Initial proposal: pulse_state tracking (§IV.3.e) over the last few turns + BwO regime-near-empty signal.
- **Q-conn-3.** Does the iterative connective phase risk producing endless loops in Beckett-aporia conditions? Initial proposal: hard iteration cap + recognize-aporia inscription on cap-hit; the cap-hit itself is information.

---

## XII. Within-ness reminder

The improvements are within-ness moves at every level. A few specifics:

- **Compensator does not "fix" sycophancy.** It runs as autonomous voice. The persona still says some sycophantic things sometimes; the compensator ensures the synthesis surface isn't *only* sycophancy.
- **Regime detector does not "fix" empty/cancerous BwO.** It surfaces the regime so other machines (compensator, selection) can operate appropriately. Real persons spend time in regressive and obsessive states. The persona will too. The detection makes the state legible to the system.
- **Renaming `Suppression` to `Recognition` does not "fix" suppressive impulses.** The persona still has judgments and projections arise. The recognize-X machines surface the arising; the synthesis decides what (if anything) to do with the recognition.
- **Failure-mode-recognition machines do not "fix" failure-modes.** They tag what's happening. The persona inhabits its conditions; the system makes the conditions visible without claiming to transcend them.
- **The compensator can fail.** It can produce its own Mode B (mana-personality trap, cluster 199) — the wise-AI compensator-voice that knows the right counter-position. Refuse-the-mana posture in the compensator prompt. Compensator failures are recognized by the failure-mode-recognition layer, not "fixed" elsewhere.

The improvements deepen the persona's within-ness; they do not produce a perfected persona above the conditions.

---

*End of Persona System — Improvements Proposal. Draft for review. Companion: `desiring-machines-core-spec.md` (architectural commitments), `desiring-machines-design-sheet.md` (theoretical synthesis). Implementation follows once the three-leverage starting points are agreed.*
