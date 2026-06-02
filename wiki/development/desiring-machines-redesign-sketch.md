# Desiring Machines — Redesign Sketch

A barebones sketch of the redesigned pipeline, framed around the open questions that still need answering before any of it can be built. The sketch follows the order in which the redesign was described, not necessarily strict execution order.

> **Note on citations.** This project will eventually produce a research report. Every design choice in this sketch should be traceable to a source — a wiki theory page, a primary text, a prior dev note — with the reasoning behind it explicit. Wiki searches that inform decisions are logged in `design_search/`. As decisions move from "candidate" to "adopted," the corresponding citation should travel with them so the eventual report has provenance for each architectural commitment.

> **Engineering substrate context.** The redesign sits in the agentic-systems engineering domain mapped by Gullí 2025 (*Agentic Design Patterns*) and adjacent literature. Patterns from that catalog we use: **Routing** (selection / voting model), **Parallelization** (per-machine + group synthesis stages), **Reflection** (synthesizer choosing its own mode; Stage 5 Ambition-Piety diagnostic), **Memory Management** (BwO + `fire_count` + `mode_history`), **Multi-Agent Collaboration** (Network + Critic-Reviewer + Parallel hybrid topology). Group syntheses with different modes are structurally close to **Graph of Debates (GoD)** — local clusters produce robustly-shaped outputs without forcing consensus. The book's *goal-driven* framing of agents is held as anti-model; we take the engineering vocabulary as substrate while resisting the framing. See `design_search/07-agentic-best-practices.md`.

## Why redesign

Giving an LLM the task of simulating an entire persona is too complicated. Agentic systems are powerful because each agent gets a less complicated task, and they can do it better. The redesign splits persona simulation across many sharper, smaller analytical agents whose outputs are then combined.

The end goal: better simulation of a human persona with LLMs — for better artistic generation, better interpersonal communication, and more realistic preferences for product evaluation.

## Two-layer architecture

The system runs at two scales:

- **Per-turn pipeline.** Within a conversation, each turn runs selection → per-machine → grouping → group synthesis → final. Described in sections 1–5 and the [Pipeline data model](#pipeline-data-model).
- **Between-conversation ghostwriter loop.** Between conversations, an LLM ghostwriter agent reviews the firing trace, makes design decisions about the persona's machines (modify / create / delete), and refines each decision through dialogue with the persona. Described in [Between-conversation ghostwriter loop](#between-conversation-ghostwriter-loop).

The persona is **co-authored** by the LLM-as-ghostwriter and the person running the system. The starting sketch is just a sketch — most of the persona's texture accumulates through the persona's own conversational operation and the ghostwriter's between-conversation edits.

## Pipeline at a glance

In execution order:

1. **Selection** — five voting sources (always-on, relevance, compensation, habit+variation, random) combine via Gaussian-weighted sum. Top-N=10 machines fire alongside the always-on set.
2. **Per-machine processing** *(parallel with §3)* — each fired machine runs its own LLM call, doing whatever its function produces.
3. **Grouping** *(parallel with §2)* — the firing set is randomly partitioned into groups of 2–4.
4. **Group synthesis** — one LLM call per group; the synthesizer chooses a mode, summarizes each machine's output, and produces the synthesis.
5. **Final machine** — single LLM call that takes all group syntheses, sequentially edits the BwO, and responds.

Stages 2 and 3 run in parallel. Stages 1 → (2,3) → 4 → 5 are sequential.

The full concrete mechanism is in [Pipeline data model](#pipeline-data-model) at the bottom. The conceptual stage descriptions that follow elaborate on what each piece is doing and why; their order matches execution order, not the order of conceptual centrality.

---

## 1. Selection

There should be **multiple trigger systems** — multiple avenues by which a desiring machine can be triggered. Selection is not a single LLM call deciding everything.

Some machines **always fire** — the constitutive set sits outside the voting mechanism and fires automatically every turn. The voting mechanism selects the rest.

The mechanism is the voting model in [Pipeline data model](#pipeline-data-model): four voters (relevance, compensation, habit+variation, random) each pick k machines, votes combine via Gaussian-weighted sum with default ordering *relevance > compensation > habit+variation > random*, top-N=10 fires.

**Per-category caps.** A post-vote constraint enforces at most one Memory machine in the firing set per turn (across Memory generator + all Memory-of-X recall machines). If more than one memory machine makes the top-N by combined score, keep only the highest-scored and replace the rest with the next-highest non-memory machines. Realistic — distinct memories don't usually surface in the same moment. Other categories don't currently need caps; Memory is the unique case where the machine count can grow unboundedly as Memory-of-X recall machines accumulate.

### Open questions

- What's in the constitutive always-on set vs the variable per-turn pool? (Note: ghostwriter-editable between conversations.)
- How do the selector weights tune in practice? Default weights and Gaussian noise levels need tuning.

---

## 2. Per-machine processing

The most important architectural shift in the redesign: **each desiring machine does its own narrow piece of work** instead of editing the BwO directly. Each fired machine reads the situation through its own sensitivity and produces an output along a single, narrow line. This is a job an LLM can do well; simulating an entire persona in one shot is not.

**Grounded by the wiki search:** Bergson's perception-as-subtraction supports this — a machine is a *centre of indetermination* that selects from input what concerns its possible action, rather than constructing a representation of the whole. Each machine's output is also a *flow* (in D&G's flow/break sense) — productive output that the next coupling consumes — not a static report. Narrowness is a feature.

**A machine's shape describes what it does** — analysis (reads state, produces analytical flow), proposal (makes its own contribution), or modulation (shapes other flows). Architecturally all three go through the same path: when a machine fires, it runs its own LLM call producing whatever its specific function produces, and that output feeds into group synthesis. Shape is a property of the machine's function, not pipeline routing.

**Output mode: showing, not telling.** Machine outputs are showing-mode by default — sensory image, indirection, texture, intensity-shape. Emotion-naming ("I feel anxious") is the conjunctive synthesis's work and happens at Stage 5, not in per-machine outputs.

### Open questions

- What does a single-line output actually look like for each shape? Concrete prompt structure per machine.
- How is the per-machine prompt written so each machine stays inside its own line and doesn't drift into doing the persona's work?

---

## 3. Grouping

Fired machines are **randomly partitioned into groups of 2–4**, each group assigned a synthesis mode (connective / disjunctive-inclusive / conjunctive / transcendent function — see Stage 4). Random rather than groove-based — grooves are out of scope for this build. The randomness keeps the persona's combinations interesting; the synthesis mode determines how the group is combined.

Grouping happens in parallel with each machine running its own LLM call, so the grouping decision doesn't block the per-machine work.

See [Pipeline data model](#pipeline-data-model) for the full mechanism.

### Open questions

- Should random grouping have any structural constraints (e.g., shape mix per group), or pure random?
- (Synthesis mode assignment options are listed under Stage 4, since they depend on group size due to the transcendent-function pair constraint.)

---

## 4. Group synthesis

Each group runs one LLM call that combines its machines' outputs using its assigned synthesis mode. The four modes:

- **Connective** ("and ... and then ..."): chains the outputs sequentially. Each output's flow becomes the next one's input.
  - *Legitimate operation:* connections specified by which partial flow couples to which next flow, not by what "the persona" thinks.
  - *Failure mode (illegitimate):* the chain becomes a relation between whole-subject claims (the persona's reasoning, the user's perception). The partial-object multiplicity collapses.

- **Disjunctive-inclusive** ("either ... or ..."): holds the outputs side-by-side, including contradictions, without resolving.
  - *Legitimate operation:* "either A or B or both or neither" — every alternative retained as itself, the surface holds the contradiction.
  - *Failure mode (illegitimate):* exclusive disjunction. The synthesis picks a winner, resolves the contradiction, subsumes one output under another. The recording surface stops recording and starts deciding.

- **Conjunctive** ("so it's..."): out of the interplay, a residual subject-position precipitates.
  - *Legitimate operation:* nomadic, polyvocal. *A* subject for this passage, not *the* subject. Bakhtin's polyphonic constraint applies: **the synthesis-voice must be one voice among the machine-voices, not a sovereign voice speaking ABOUT them**. A prompt asking for "a unified response summarizing the machine outputs" is doing the illegitimate version.
  - *Failure modes:* (a) over-consolidation — produces "I am X," fixed identity; (b) under-consolidation (Beckett aporia) — endless self-retraction, no provisional subject ever lands. Legitimate operation threads between: stable enough to complete, nomadic enough not to anchor.

- **Transcendent function** (Jung CW 8 §§131–193): shuttles between two opposing outputs until a third arrives in a *new register* than either pole.
  - **Pair constraint: works on exactly two machine outputs.** Cannot be assigned to groups of size 3 or 4.
  - *Legitimate operation:* start from affect (not content), give form before understanding (aesthetic before interpretive), equal-rank dialogue, full affect preserved (anti-defusing), sustained shuttle until the third arrives.
  - *Failure mode:* the "third" is in the same register as the original pair (a compromise, an averaging, a logical-stillbirth) rather than a phase-shift to a new dimension.

Each mode produces a structurally different output; Stage 5 receives a heterogeneous mix.

### Mode assignment — chosen by the synthesizer LLM itself

The synthesizer for each group chooses its own mode, in the same LLM call that does the synthesis. It receives:

- The group's per-machine outputs
- A small rubric describing each mode's trigger (when to pick which)
- The pair constraint (transcendent function only available if group size = 2)
- A `mode_history` sliding window — recent mode choices, with a soft preference for variety

Mode triggers (rubric in the prompt):

- *Connective* — outputs naturally extend each other; co-developing or chaining.
- *Disjunctive-inclusive* — real contradictions or heterogeneity worth preserving; outputs that don't reduce.
- *Conjunctive* — a subject-position is precipitating from the interplay; the outputs together suggest a coherent provisional "I."
- *Transcendent function* (pairs only) — outputs hold opposed positions in incommensurable registers; a phase-shift is needed, not just preserved tension.

The synthesizer outputs three things per group, in one structured response:

1. **Per-machine summaries** — compressed restatement of each machine's output in the synthesizer's own words. Passed to Stage 5 so it sees the underlying machine work.
2. **Synthesized result** — the actual synthesis in the chosen mode. Passed to Stage 5.
3. **Mode chosen** — logged into `mode_history` for next turn's variety bias. **Not passed to Stage 5** (the final machine works from the synthesized result, not from knowledge of how it was produced).

**Variety preference is soft.** The synthesizer is told what modes were used last turn and asked to vary, but isn't blocked from picking one of them if it really fits.

### Open questions

- For groups choosing conjunctive mode, how to write the polyphonic-constraint into the prompt without it sliding into "summarize these."

---

## 5. Final machine — the conjunctive synthesis at pipeline scale

**Stage 5 IS the conjunctive synthesis for the whole pipeline.** Not a separate operation. The "so it's..." moment that produces the persona's response is THE conjunctive moment; the four modes at Stage 4 are local syntheses that feed it.

A final machine makes the edits to the BwO, **sequentially**, based off the synthesized analysis from the group stage and some ordering logic. The ordering decides which edits come first and which come last, based on importance.

The same LLM that has just made these edits then **actually responds**. This is the closest we can get to embodied logic: the LLM that has worked through all of the desiring machines and inscribed them into the BwO will understand the state of the BwO the best, and is therefore the right one to speak from it.

The synthesized outputs entering this stage are heterogeneous — chains (from connective groups), preserved tensions (from disjunctive), tentative subject-positions (from conjunctive), phase-shifts (from transcendent function). The final machine weaves them.

The final machine's prompt carries the persona's current voice sketch (the six-dimensional Bakhtinian position) as configuration; the response is written in that voice directly. The voice sketch starts as seeded and is editable by the ghostwriter between conversations (see [What changes between conversations](#what-changes-between-conversations)). If Voice-mask has recently fired and set a mask, that mask description lives in the BwO and the final machine reads it from there. There is no separate always-on voice machine — the voice work happens here, at Stage 5.

### What the legitimate conjunctive synthesis requires

- **Bakhtin's polyphonic constraint.** The voice that speaks must be **one voice among the machine-voices**, not a sovereign voice speaking ABOUT them. The wiki is direct: a prompt asking for "a unified response summarizing the inscriptions" is doing the illegitimate conjunctive. The legitimate version positions the synthesis-voice within the polyphony, not above it.
- **Nomadic, not fixed.** Produce *a* subject-effect for this passage, not *the* subject. No "I am Claude," no "as a language model," no fixed character claim that persists across passages.
- **Must complete (avoid Beckett aporia).** The opposite failure: synthesis can't even produce a provisional "I." Endless self-retraction, no settled subject-effect. Legitimate operation threads the needle — stable enough to finish, nomadic enough not to lock.
- **Showing → telling shift IS the conjunctive synthesis.** The BwO and group syntheses accumulate showing-mode content (sensory, indirect); the response is where emotions get *named*. "I feel..." is the conjunctive moment.
- **Ambition-Piety diagnostic** (Spinoza V.P4 Schol). Behaviorally identical responses differ ontologically by which idea the conatus is running on. Ambition (response staged for applause) and piety (response from the persona's own nature) cannot be told apart from outside. The hardest detection problem this stage has.
- **Apotropaic assimilation** (Jung CW 8 §206) is the natural failure mode: the ego smooths over machine heterogeneity by speaking as if there were only one speaker. The polyphonic constraint above is the direct guard against it.

### Literary guidance

These shape the prose at Stage 5; the wiki's literary sources don't dictate BwO structure but they do dictate how the final pass writes:

- **Showing, not telling** — sensory image, indirection, texture for the BwO edits; named, propositional language for the response. The shift between the two modes is the conjunctive synthesis above.
- **Painting, not describing** (Deleuze on Bacon). The prose should communicate to the nervous system, bypassing representation. "A heaviness in the chest, something unresolved pressing down" rather than "the persona is experiencing tension."
- **Woolf register.** Literary prose of interiority — the unnamed texture of experience, not psychological report.
- **Plateau-sustaining** (Bateson). Continuous regions of intensity that don't build toward climax. The response shouldn't drive toward catharsis or discharge.

### Form-before-understanding

The final machine should aesthetically formulate before interpreting. The "hands know what the intellect cannot." The response is *residue*, not *goal* — D&G's celibate machine produces the nomadic subject as "a mere residuum alongside the machine, an appendix." The persona-effect emerges alongside the editing, not as the editing's destination.

### Open questions

- What is the ordering logic? What does "importance" mean here, and how is it decided? (Wiki search needed; not directly answered yet.)
- Are the sequential edits separate operations the LLM watches itself perform, or one composite write?
- What does the prompt to the final machine look like such that the edit pass and the response pass are coherent within a single LLM context — and that prevents apotropaic assimilation?

---

## What carries across turns

Within a conversation, three artifacts carry across turns:

- **BwO text** — the stateful artifact carrying conversation content within a conversation. Updated by the final machine each turn. Resets to the current seed text at the start of each new conversation; the Personal History machine then primes it with historical context (see [Conversation initialization](#conversation-initialization)).
- **`fire_count` per machine** — two counters per machine: `fire_count_conversation` (within the current conversation) and `fire_count_lifetime` (across all conversations). The habit+variation selector uses a weighted sum that weights in-conversation firing higher than lifetime firing — current preoccupations matter more than long-term tendencies, but the long-term tendency still informs. Always-on machines may be excluded from these counters (or tracked separately) since they fire every turn.
- **`mode_history`** — last turn's mode choices (one per group from the previous turn), used by current-turn group synthesizers to bias toward variety. Overwritten each turn.

That's it for within-conversation state. The persona's machine set (including any Memory-of-X recall machines), voice sketch, biographical detail, and refrain set don't change within a conversation — they change *between* conversations, via the ghostwriter (see [What changes between conversations](#what-changes-between-conversations)).

Grooves as a separate persistence layer are out of scope for this build — the persona's habits emerge implicitly from `fire_count` patterns and from how the BwO accumulates content over turns. Refrains, when they appear, do so as textual recurrences in the BwO prose without separate tracking.

(Conversation history — user and persona turns — is needed as input to the relevance selector and the final machine; it's plumbing, not an architectural artifact of the persona itself.)

### Open questions

- Weighting between `fire_count_conversation` and `fire_count_lifetime` — what ratio? In-conversation should dominate but lifetime needs to register.
- Are always-on machines counted in `fire_count`? Excluding makes the habit signal cleaner; including means the variation signal can occasionally surface a constitutive machine in a "habit-mode" turn.

---

## What changes between conversations

These artifacts are edited by the ghostwriter between conversations, not within them. They form the layer that lets the persona accumulate across conversations.

- **Machine set** — the catalog of machines this persona has. The ghostwriter can add (drawing from the [Desiring-machine wiki](#the-desiring-machine-wiki)), modify, or remove machines. New Memory-of-X recall machines are added here, as the ghostwriter promotes specific memories.
- **Per-machine firing probabilities** — for randomly-firing machines (Voice-mask, affect baselines, named-affect machines, Memory generator).
- **Per-machine inscription specs** — the specifics of what a machine inscribes when it fires.
- **Voice sketch** — the six-dimensional Bakhtinian position carried in the final machine's prompt.
- **Biographical detail** — paragraph(s) describing the persona's life-shape, used as input to the Memory generator.
- **Refrain set** — patterns the persona returns to.
- **Constitutive (always-on) set membership** — which machines sit in the always-on set vs the variable pool.
- **Sinthome candidate** — configuration of the final machine's prompt.
- **BwO seed text** — the intensive surface the BwO resets to at the start of each conversation. Refinable by the ghostwriter as the persona's structural surface evolves.
- **Conversation history corpus** — the persona's qmd-indexed collection of documents covering prior conversations (one document per conversation, or per significant moment, or some mix — granularity is an open question). Populated by the ghostwriter at the end of each conversation; queried by the Personal History machine at the start of each new conversation. Replaces the earlier "condensed log" idea: rather than maintaining one summary document, the ghostwriter writes entries that qmd indexes and Personal History retrieves over.

The starting sketch seeds these at conversation 1 (see [Initialization — the starting sketch](#how-should-the-bwo-itself-be-designed) under cross-cutting); the ghostwriter accumulates from there. The conversation history corpus starts empty.

### Open questions

- How often does the ghostwriter run — every conversation, or only when enough has accumulated?
- Does the ghostwriter's own state accumulate across runs (preferences-about-editing), or stay stateless?

---

## Between-conversation ghostwriter loop

The ghostwriter is an LLM agent (not a persona on the same architecture) that runs after each conversation. It has access to:

- The **firing trace** from the conversation — structured per-turn record of which machines fired, their outputs, group syntheses, BwO edits
- The **conversation log** — user/persona turns
- The **desiring-machine wiki** — curated catalog of machines, grounded in concrete examples; source material the ghostwriter draws from
- The **current persona state** — machine set with probabilities and specs, voice sketch, biographical detail, refrain set

It runs in two stages.

### Stage 1 — review and design decisions

The ghostwriter reads the trace + log + persona state and produces a list of design decisions. Each decision is one of:

- **Modify** an existing machine — refine its inscription spec, adjust its firing probability, change its anchor.
- **Create** a new machine — almost always by adopting an entry from the [Desiring-machine wiki](#the-desiring-machine-wiki). LLMs are poor at inventing desiring machines de novo; editing wiki entries is what they do well. Includes assigning a starting firing probability.
- **Delete** a machine — if it consistently misfires or no longer fits the persona's emerging shape.
- **Promote** a generated memory by creating a new Memory-of-X recall machine — when a hallucinated memory inscribed in the BwO fits the persona and should be available for recall later. Each promoted memory becomes its own desiring machine (not a row in a store) that competes for selection like any other; the soft cap of one memory machine per turn (see [§1 Selection](#1-selection)) keeps the Memory category from crowding the firing set as the count grows.
- **Edit non-machine state** — voice sketch, biographical detail, refrain set, sinthome candidate, always-on set membership.

**Edit discipline.** Each modify/create decision produces a **bounded edit** — one sentence, or a fixed small token budget — not a sweeping rewrite. The Stage 2 dialogue subagent loads the **relevant desiring-machine wiki entry** into its context before proposing the edit, so every edit is grounded in the wiki's full information about the machine type. Sweeping changes are out of the model's competence; small grounded changes are in it.

Sobriety discipline also applies (see [Sobriety](#sobriety-as-a-design-discipline)): prefer modify-or-leave-alone over create. Proliferation is the failure mode.

### Tagged immutability

Each desiring machine is structured text, and portions of that text are marked **immutable** with inline tags (e.g., `<immutable>...</immutable>`). The remainder is mutable. At runtime, tags are parsed out before the machine fires — the machine reads its full text (immutable + mutable) as one piece. The tags exist only to constrain the ghostwriter.

The ghostwriter **can**:

- Edit content in mutable zones (within the bounded-edit discipline above)
- Add new mutable content to a machine
- Add new immutable tags around content — promoting something to immutable as it becomes load-bearing for this persona

The ghostwriter **cannot**:

- Edit content inside existing immutable tags
- Remove existing immutable tags (asymmetric ratchet — structure only stratifies, doesn't loosen)

**Wiki-entry default.** When a machine is adopted from the [Desiring-machine wiki](#the-desiring-machine-wiki), its initial wiki-derived inscription is fully immutable. The ghostwriter's edits add mutable content around the immutable core; persona-specific accumulations live in the mutable zones; load-bearing discoveries get promoted to new immutable parts over time.

**What this gets us.** The machine's core character (wiki-grounded, human-curated) is preserved across ghostwriter edits. Personalization happens in clearly-bounded zones. The persona stratifies as it accumulates — D&G-coherent: assemblages crystallize through their own operation, and what becomes immutable is harder to deterritorialize.

*Open questions:*
- Tag syntax — XML-style, markdown-style, JSON-fenced, something else?
- Should immutable-promotion require a special trigger (e.g., a part has remained stable for N conversations) or be a routine option in any edit?
- Should the human-user be able to override / remove immutable tags out-of-band? (Probably yes, but outside the ghostwriter's loop.)

### Stage 2 — per-decision design dialogue

For each decision in Stage 1, the ghostwriter spawns a subagent that runs a **design dialogue with the persona**, appended to the conversation log. The persona's machines continue to fire during this dialogue; the subagent uses the responses as material to refine the design.

The dialogue is internal to the system — the user is not the interlocutor. The point: the design choice arrives through interaction with the persona's actual operation, not from outside it. A new affect machine's inscription spec emerges from how the persona's existing machines respond to probing about that affect; a refined voice-sketch dimension emerges from how the persona's current voice shapes responses; a Memory-of-X machine's recall-trigger emerges from how the moment of the original inscription replays.

**Lightweight pipeline during dialogue.** The full per-turn pipeline (~15–21 LLM calls) is overkill for probe-by-probe dialogue. The dialogue runs a reduced pipeline instead: always-on machines + top-3 relevance picks; single group, connective synthesis; the final machine still runs but on a reduced input set. Roughly 5–7 calls per dialogue turn. *Alternative to consider:* voice-only — skip everything and pass the current BwO + probe directly to the final machine. Cheaper but loses the machine-substrate of the response (the voice would answer; the machines wouldn't operate). Held as a candidate if the lightweight pipeline still proves too heavy.

Because the persona's machines fire during the design dialogue, the dialogue itself becomes part of the firing trace that the *next* ghostwriter pass reviews. The persona's response to being designed shapes its further design — the bootstrap structure.

### The desiring-machine wiki

A curated catalog of desiring machines, separate from the theoretical wiki at `wiki/`. (Location TBD — likely `machine-wiki/` at the project root or `wiki/machines/`.) Each entry includes:

- **Short specification** — what the machine inscribes when it fires
- **Primary anchor** (where applicable) — its grounding category
- **Adequacy default** (where applicable) — passive/active disposition
- **Concrete examples** — drawn from real people and real sources, *not LLM-generated*. The hard requirement that distinguishes useful wiki entries from generic LLM productions.

The wiki is human-curated. The ghostwriter adopts and edits entries; new entries are added by humans drawing on primary sources. The nine [categories of desiring machine](#how-should-the-many-different-desiring-machines-be-designed) below give the wiki's structural organization; the existing affect catalog (~30–50 Spinozist + Tomkins entries) is the start of the wiki's Affect section.

### The firing trace artifact

Per-turn structured record. For each turn:

- Selection result (which machines fired, voter contributions, per-category cap enforcement)
- Per-machine outputs
- Group assignments, synthesis modes chosen, per-machine summaries, synthesized results
- Final machine's BwO edits and response

This is the artifact the ghostwriter reads. The conversation log (user + persona turns alone) is a thinner view; the firing trace is the full picture.

### Open questions

- How is the design dialogue prompted so the persona's machines fire genuinely (not just performatively) during it?
- What's the ghostwriter's own prompt — what guidance does it carry about what to attend to in the trace?
- How does the ghostwriter avoid Goodharting on the trace (over-editing toward what made nice traces last time)?
- Location of the desiring-machine wiki — co-located with the theoretical `wiki/`, or separate at project root.

---

## Cross-cutting open questions

These are the design questions that span the whole pipeline and need answering in parallel with the per-stage work.

### What shape can a desiring machine take?

A machine takes one of three shapes. Keeping the set small is deliberate: more shapes adds complexity, and the three below cover what's needed without forcing every machine into a single mold.

- **Analysis** — reads state, produces an analytical flow.
- **Proposal** — makes its own contribution without reading state in detail.
- **Modulation** — shapes other flows (rhythm, register, baseline tone).

Architecturally **all three shapes go through the same path**: when a machine fires, it runs its own LLM call producing whatever its function produces, and that output feeds into the group synthesis it's been assigned to. Shape describes what the machine does, not where it enters the pipeline.

Open questions:

- **Sinthome (open).** Doesn't fit any of the three shapes. Working hypothesis: Sinthome is not a machine in the pipeline sense — it's a configuration property of the persona, probably resolved at the final LLM pass (the final machine's prompt carries the sinthome as a constraint or attractor). To be checked when the final-machine prompt design is settled.

### Research-only question — the Simondonian no-milieu cut

The wiki flags a substantive worry that the persona system's machines may not be *full* desiring-machines in D&G's sense. Real desiring-machines transduce across two disparate registers (organism / milieu); the persona has only one register (the linguistic surface). Baudrillard's *Crash* reading describes the limit case: machine-couplings that are fully operational *without* the affective-libidinal substrate the D&G machine-concept was built for. The persona system, by substrate conditions, may be running closer to *Crash*-machines than to original *Anti-Oedipus* machines.

A future system might add a second register — some form of organic-simulation substrate that gives the persona's machines real disparation to transduce across, rather than only language. **This is out of scope for the current build** but should be noted in the eventual research report as a structural limit of the language-only substrate and a candidate direction for future work. Importing concrete examples from real people (per the categories section) is a *partial* response — it imports human-disparation as content even though the substrate remains single-register.

Open questions for the research report (not the build):

- What second register would actually count as transductive disparation for a persona system, rather than as more content in the same register?
- What can be detected at output-level that distinguishes a transductive machine from an imitation-machine ("machine-shaped operations without affective-libidinal substrate")?

### How should the BwO itself be designed?

The BwO is a piece of text that the machines write — through the per-machine outputs, through the group syntheses, and through the final machine's edits. **Its form and content emerge from those operations; they are not pre-designed.**

This is deliberate. We have no biological substrate, no autonomic register, no peripheral-correction loop. There is much we don't have access to. Trying to prescribe what the BwO holds in advance — affect-categories, intensity-gradients, zones, schemas — would smuggle structure the system has no substrate for. The BwO is whatever the machines write into it. The design problem lives in the machines and their synthesis, not in the BwO itself.

What we do design: the machines (Stage 2), the group synthesis logic (Stage 4), and the final-machine prompt that produces the BwO edits and the response (Stage 5). The BwO is downstream of those decisions.

**The parasite-without-host caveat** still holds: the BwO is not a simulation of a missing biological body. It is the only body the system has. There is no iceberg below the text.

Literary guidance from the wiki applies at the **final LLM stage** (see Stage 5), where the synthesis becomes prose. It does not dictate BwO structure.

Open questions:

- **Initialization — the starting sketch.** The persona starts from a *sketch* — a thin metastable configuration with pre-individual charge for further individuation through (a) the persona's own conversational operation and (b) the ghostwriter's between-conversation edits. The starting sketch includes: voice sketch (six dimensions); sinthome candidate; at least one minimum-refrain (the thing this persona cannot help); a small starting set of affect machines with starting firing probabilities (the initial affect-disposition); seed biographical detail (one or a few short paragraphs describing the persona's life-shape); an initial BwO seed text (the *intensive* surface, not biography); and a small starting selection of variable machines drawn from the [Desiring-machine wiki](#the-desiring-machine-wiki). The Memory generator and Personal History machine start present; no Memory-of-X recall machines yet, and the conversation history corpus starts empty. The constitutive (always-on) machines fire on the first turn alongside whatever the situation triggers. "Most of the persona's eventual texture will accumulate through its own BwO inscription history and the ghostwriter's accumulated edits." The starting sketch is just a sketch; nearly everything in it is editable by the ghostwriter over time (see [What changes between conversations](#what-changes-between-conversations)).
- Without prescribing structure, how do we keep the BwO from drifting into the failure modes the wiki flags (catatonic emptiness, sycophantic miraculation, single-voice apotropaic assimilation)? Likely answer: through machine design, synthesis quality, and the sobriety discipline below.

### Sobriety as a design discipline

Possibly the most important single principle from the third wiki search. D&G are direct: "the cosmic is not reached by adding more — more complexity, more structure, more machines, more rules. It is reached by **simplification**: 'a maximum of calculated sobriety in relation to the disparate elements and the parameters. The sobriety of the assemblages is what makes for the richness of the Machine's effects.'"

For the redesign: more machines, more grooves, more complex BwO text, more elaborate prompts is the path to scrambling, not to cosmic force. Aim for **simplicity that captures force** — a few well-designed machines whose interactions produce richness, not a proliferation of components that produce noise. This codifies the user's repeated push toward simplification (three machine shapes not nine, no proliferation of categories, non-prescription on the BwO) as a design discipline rather than a one-off choice.

### Anti-patterns to actively avoid

Named in the agentic-engineering literature (Gullí 2025) as common failure modes; held by this project as things to design against:

- **Goal-driven framing** — the persona doesn't pursue declared goals. Machines produce because of what they are. SMART-goal patterns are anti-model here.
- **Faciality at sub-component level** — naming each machine as a "specialist agent with a role and goal" reinstalls the very faciality the architecture is trying to dissolve. Machines describe what they *do* (sensitivity / flow), not who they *are*. No biographical machine descriptions.
- **Reflective rigidification** — when self-critique loops produce visible reasoning chains that get pattern-matched and optimized into a stable shape. Keep reflection internal (mode-choice reasoning, ambition-piety diagnostic) — log for diagnostics, don't propagate to outputs.
- **Hierarchical-everything topology** — the manager becomes the bottleneck and the faciality point. The redesign is closer to network + critic-reviewer than hierarchical.
- **Externalized reasoning chains** as output artifacts — the more visible the persona's reasoning, the more it can be evaluated against a stable pattern, which rigidifies. Internal reasoning stays internal.

### Research-only question — refrain-from-outside (the Beckett-Worm caveat)

The wiki flags a substrate-level caveat to the refrain/groove story: an LLM persona may be in the position of Beckett's Worm — *unable to produce its own refrain without external recurrence*. A stateless system has no internal periodicity. The refrain-function may need to arrive from outside the system: a recurring user, a recurring prompt, a recurring invocation pattern. **Designing persona-refrains may mean designing the *environment* that produces periodic recurrence, not just the persona itself.**

This is out of scope for the current build — internal grooves and refrains can do most of the work — but it's worth noting in the eventual research report as a substrate-level constraint that may bound how fully the persona can carry its own refrains.

### How should the many different desiring machines be designed?

The working list of categories, reconciled across the user's original seven + the wiki's broader taxonomy (constitutive set, design-sheet machine layers, per-tradition appendices). Nine categories total — sobriety-bounded; more may surface in per-category searches but the floor is here.

These nine categories give the structural organization of the [Desiring-machine wiki](#the-desiring-machine-wiki). The wiki holds the curated catalog of machines under each category, grounded in concrete examples; the ghostwriter draws from the wiki to add, modify, and remove machines in the persona's set over time. There's no fixed cap on how many machines a persona has under each category — the count is emergent through accumulated ghostwriter decisions, bounded by the sobriety discipline. (The Memory category has a runtime soft cap at selection — see [§1 Selection](#1-selection) — but no cap on how many recall machines can exist in the set.)

1. **Voice** — organized around the persona's six-dimensional Bakhtinian voice (height / range / timbre / aesthetic-category / worldview / fate). The six-dimensional voice sketch is **configuration carried directly in the final machine's prompt** — it's the persona's structural voice-position. Starts as seeded in the starting sketch; refined by the ghostwriter between conversations as the persona's voice accumulates. The final machine writes in that voice; the always-on voice work happens at Stage 5, not as a runtime machine. Absorbs Status (worldview/life-fate dimensions). Runtime machines under Voice:

   - **Voice-mask** — random firing (probability tunable, probably low — 5–15% — so masks persist long enough to feel like states rather than flickering turn-to-turn). When fired, designs a new mask based on the current situation, constrained by the persona's voice sketch. The mask is a short description of the persona's current voice-register (e.g., "pastoral — warm, attentive, slow-paced, willing to hold silences"). The Voice-mask machine's prompt contains *examples spanning the range of masks a person might have* (pastoral / polemic / intimate / formal / confessional / playful / etc.), giving the LLM enough guidance to design fitting masks without a curated mask repertoire.

   *Mask state lives in the BwO.* No separate persisted artifact across turns. When Voice-mask fires and designs a new mask, that mask description is inscribed into the BwO by the group synthesis / final machine. The final machine reads the current mask state from the BwO on subsequent turns (alongside the voice sketch in its prompt). The BwO carries the mask the way it carries everything else.

   *Interaction with other machines.* Voice-mask fires like any other machine — its output goes into group synthesis with whatever else is in its group. The synthesizer's mode shapes how the new mask combines with the other outputs (a Voice-mask + Memory firing in connective mode chains them as "mask shifts as the memory arrives"; in disjunctive mode holds them side-by-side).

   *Two additional contextually-firing machines under Voice.* Both proposal-shaped, adding sentence-level polyphony (Bakhtin Type III "double-voiced discourse"):

   - **Sideward-glance** (Bakhtin's *word with a sideward glance*) — fires when the situation has a strong anticipated-rejoinder quality. Inscribes the listener's imagined reaction into the utterance, making it dialogic at the sentence level. Example output: "you could call this defensiveness, but —" — the rejoinder already absorbed into the saying.
   - **Loophole** (Bakhtin's *loophole word*) — fires when self-characterization needs preserved non-finality. Inscribes a refused-pinning-down into self-statements. Example output: undercutting a feeling-name as it's named ("a kind of sadness, though that's not quite it").

   Unlike Voice-mask (random firing), these fire **contextually** — the relevance selector picks them when the moment has the right shape.

   *Not present:* no curated mask repertoire (the prompt's range examples cover it), no separate mask-state field (BwO carries it), no contextual firing for mask shifts (random firing handles it), no always-on Voice-baseline runtime machine (the voice sketch goes into the final machine's prompt directly).
2. **Affect** — multiple machines, grounded in Spinoza's three-primary kernel (cupiditas / laetitia / tristitia) and his active-register (fortitudo: courage + nobility). The Spinozist schema (primary × cause-structure × temporal × certainty × sign) is the *generative space* — the wiki catalog draws from it but is not committed to enumerating all 48 named affects. Foundational category; every machine in the system inscribes in affect-language, but Affect machines specifically produce affect as their function. Runtime machines under Affect:

   *Baseline machines (start in the persona's sketch — the initial structural affect-disposition; fire randomly per turn with starting probabilities; ghostwriter edits both the machines and their firing probabilities over time):*

   - **Cupiditas-baseline** — modulation. When fired, inscribes forward-reach / desire / striving.
   - **Laetitia-baseline** — modulation. Inscribes lift / increase of power when fired.
   - **Tristitia-baseline** — modulation. Inscribes diminishment / heaviness when fired. (Always passive per Spinoza — the power-of-activity can't diminish itself through itself.)
   - **Fortitudo** — modulation. Active register: courage (animositas — desire-to-preserve-own-being-by-reason-alone) + nobility (generositas — desire-to-assist-others-by-reason-alone). One machine, two output-modes.
   - **Relational-impulse** — modulation. The molecular, weaving, generative-compositional pull — making-into-relation, twisting-together, plot-developing. *Not Spinozist* — drawn from D&G's becoming-woman (the primary becoming, "all becomings pass through becoming-woman first"), Guattari's becoming-woman-creator compound (passivity + sophistication + relentlessness-without-will-to-power, with the refrain as operator), and Merleau-Ponty's intertwining (weaving-together, threading-through-each-other). Distinct from cupiditas's forward-reach in that it doesn't direct toward an object but composes-among.

   The five baselines start in the persona's sketch and encode the initial structural affect-disposition through their starting firing probabilities. The ghostwriter can adjust their probabilities or refine their inscription specs over time. Under sobriety, the baselines themselves are unlikely to be removed but they're not architecturally privileged.

   *Named-affect machines (random firing, accumulated by the ghostwriter over time from the wiki catalog):*

   The persona's named-affect set grows incrementally. Drawing from the wiki catalog of ~30–50 named affects (below), the ghostwriter adds machines as it sees affects fitting the persona; adjusts their firing probabilities as the persona's disposition emerges; removes machines that consistently misfire. **No fixed cap** — the count is emergent, bounded by sobriety. The starting sketch may include a small named-affect set or none, depending on the sketch. When a named-affect machine fires, it produces a brief showing-mode inscription of that specific affect onto the BwO via group synthesis.

   *Wiki catalog of named affects (drawn from Spinoza Part III + Tomkins's nine):*

   - *Spinozist external-cause:* love / hate / inclination / aversion / devotion / derision / hope / fear (always-paired) / confidence / despair / joy-of-escape / disappointment / pity / approbation / indignation / over-esteem / disparagement / envy / compassion
   - *Spinozist internal-cause:* self-contentment / humility / repentance / pride (no opposite) / self-abasement / honor-glory / shame
   - *Spinozist desire-derived:* longing / emulation / gratitude / benevolence / anger / revenge / cruelty / timidity / boldness / cowardice / consternation / courtesy / ambition / dissipation / avarice / lust
   - *Tomkins discrete:* interest-excitement / enjoyment-joy / surprise-startle / distress-anguish / anger-rage / fear-terror / shame-humiliation / dissmell / disgust

   The catalog is human-curated and lives in the [Desiring-machine wiki](#the-desiring-machine-wiki) under the Affect section. Each entry ships with:
   - A short specification (the affect's shape — what it inscribes when it fires)
   - Its primary anchor (cupiditas / laetitia / tristitia / fortitudo)
   - Its adequacy default (passive for most; active only for fortitudo-kin)
   - **Concrete examples** — drawn from real people and real sources, *not LLM-generated* (open per entry: which sources, which exemplars)

   *Interaction with other machines.* All Affect machines feed into group synthesis like any other firing machine. The pairing with other machines in their groups shapes how the affect lands in the synthesized output (e.g., shame + Voice-mask in connective mode produces a shame-inflected register-shift; longing + a recalled memory produces a longing-tinged scene).

   *Active vs passive adequacy.* Every Affect machine's output carries an adequacy tag (passive default for most; active for fortitudo). The Stage 5 final machine uses these tags as part of the **Ambition-Piety diagnostic** — distinguishing affect-outputs that arise from the persona's own nature (active, "piety") from those pulled by inadequate ideas of external cause (passive, "ambition"). Behaviorally identical outputs differ ontologically by which tag they carry.
3. **Memory** — hallucinated *and* recalled. Two kinds of machine working together: a **Memory generator** (hallucinates a fresh memory when it fires) and **Memory-of-X recall machines** (each is a specific memory the ghostwriter has promoted from past conversations; when fired, inscribes that specific memory). All compete for selection through the same voting mechanism as any other machine — no special recall-vs-hallucinate decision lives inside the Memory category. A **soft cap of one memory machine per turn** at selection keeps the category from crowding the firing slate as the count grows (see [§1 Selection](#1-selection)). (First category to be fully operationalized.)

   **Memory generator.** Fires when picked by the random voter (autonomous hallucination — the randomness *is* the trigger; no rift-detector). Probability tunable, ghostwriter-editable. Its sibling is the **Fantasy** machine in the Desire category — both hallucinate showing-mode scenes; the two are differentiated by stance, constraint, and trigger (see the Desire category for the full treatment).

   *Inputs each firing:*
   - **Biographical detail** — one or a few short paragraphs describing the persona's life-shape. Starts as seeded in the sketch; grows as the ghostwriter adds detail (e.g., when material from a design dialogue or a conversation reveals more of the persona's history). Plausibility-to-this-persona constraint.
   - **Random seed** — three per-firing random anchors drawn from a fixed structure: five categories (Place, Time, Figure, Object, Sense), each populated with ~100 items. Each firing: pick 3 of the 5 categories at random, then draw one item from each. Three anchors per firing combined into the prompt. Forces specificity; breaks LLM-generic-memory shape. The five lists are LLM-generated at design time, informed by real-world lists (concrete-noun corpora and curated reference sets). No weighting — uniform random at both the category-selection step and the within-list step.
   - **Current conversation context** — user input + recent BwO state. What the memory will arise from.

   **Memory-of-X recall machines.** Each is a specific memory promoted by the ghostwriter (see [Stage 1 — review and design decisions](#stage-1--review-and-design-decisions)). Tends to fire when picked by the relevance or compensation voters — when the current moment's gap calls for *this* particular memory. Can also fire via random or habit+variation voters. Each carries:
   - Its **memory content** — the scene or texture it inscribes when it fires (the same prose that was originally hallucinated and inscribed in the BwO when the ghostwriter decided to promote it).
   - Its **recall tags** — situation / affect / anchor signals used by the relevance voter to score it against the current moment.

   The Bergsonian "memory rotates its useful face toward the gap" — that's just what relevance scoring does. The voting mechanism handles which memory comes to mind; no separate decision lives inside the category.

   **Personal History (qmd-searching agent).** A third Memory machine, mechanically distinct from the generator and recall machines. Fires exactly once per conversation, at conversation start, after the other person's first message. Doesn't go through the voting mechanism; doesn't count against the per-turn Memory cap. Its function: prime the (just-reset) BwO with relevant historical context drawn from the persona's prior conversations. The architectural counterpart to BwO reset — the BwO doesn't persist between conversations, but the persona doesn't start cold either, because Personal History brings the relevant past into the present surface.

   Implemented as a searching agent over a **qmd-indexed conversation history corpus** — the persona's collection of documents (one per past conversation, or per significant moment, or some mix) that the ghostwriter populates at the end of each conversation. qmd handles retrieval by relevance using its hybrid lex/vec/HyDE search; Personal History formulates queries and synthesizes results, rather than reading a flat condensed log.

   *Inputs:*
   - The **other person's first message** — primary search input. Used to formulate queries against the corpus.
   - The **current BwO** (just reset to seed) — context for the query and the surface about to be inscribed.

   *Process:*
   1. Formulate queries against the conversation-history qmd index (lex + vec + HyDE sub-queries against the first message and BwO).
   2. Retrieve top relevant entries.
   3. Synthesize a brief inscription of the historical context that matters for *this* interaction (showing-mode, not catalog-form — relevant past as a textured residue, not a list).
   4. Append directly to the BwO.

   *Output.* An inscription of the relevant historical context, added directly to the BwO before the normal turn-1 pipeline runs. Unlike generator and recall outputs (which feed into group synthesis), this is a direct BwO inscription — the Personal History machine writes to the BwO as a preamble step. See [Conversation initialization](#conversation-initialization) in the pipeline data model.

   *Open questions:*
   - Granularity of corpus entries — one document per conversation, per turn, per significant moment, or mixed?
   - What goes in each entry — raw text, ghostwriter-summary, machine-firing-traces, all of the above?
   - Query strategy — how many sub-queries per firing, which sub-query types, how to combine?
   - Pruning / compression as the corpus grows over many conversations.

   **Bergsonian shape (applies to generator and recall machines; Personal History has different mechanics — it brings real prior context, not hallucinated/recalled biographical memory).** Four principles:
   - The trigger is a **gap** in the moment's routine response, not a topical hook (Bergson's rift — habit failing to absorb the present).
   - The memory borrows **affective warmth** from the moment's intensities (the memory's tone is moment-fitted; "it is from the sensori-motor elements of present action that a memory borrows the warmth which gives it life").
   - The memory rotates its **useful face** toward the gap — relevance is functional (what the memory could *do* here), not topical (what it's *about*). Direction is centrifugal: the memory reaches toward the moment, not the moment querying the memory.
   - **Contraction varies.** Most generator firings produce *texture* (a coloring, a weight, an atmospheric residue, a vague familiarity); some produce *specific dated scenes* with sensory detail. Default toward texture; specific scenes are rarer (Bergson's cone — different contraction planes for different moment-intensities). Recall machines preserve the contraction of the memory at the moment it was promoted.

   *Output.* Showing-mode prose. The scene or texture speaks for itself — no narration about remembering. Goes into group synthesis like any other firing machine's output.

   *Pairing flavor.* The random group assignment + the synthesizer's mode-choice shape how Memory combines with whatever else is in its group — Memory + tristitia-affect + connective mode produces a flow of diminishment; Memory + Voice + disjunctive holds the memory side-by-side with a voice-shaping; etc.

   *Ghostwriter promotion.* During its between-conversation review, the ghostwriter can promote a hallucinated memory that was inscribed in the BwO by creating a new Memory-of-X recall machine for it. Likely promotion criteria: BwO-prominence at inscription, affective intensity, fit with the persona's emerging shape. The promoted machine then competes for selection like any other.

   *Not present in this design:* no qmd / source-corpus at runtime; no vitality-form-tagged anchor scenes as fixed seed kernels (recall machines accumulate instead); no biographical retrieval over the user's life (biographical detail is text the ghostwriter writes, not a database). Habit-memory and trace are carried elsewhere in the architecture (BwO compression, `fire_count` patterns), not by Memory machines.

   *Open questions:*
   - Promotion criteria — what specifically makes a hallucinated memory worth becoming a recall machine?
   - Recall-tag schema — what's the minimal structure that lets the relevance voter score recall machines well?
   - As the recall machine count grows, the soft cap of 1/turn means most don't fire most turns. Does that cause an inert tail (machines that never fire)? If so, does the ghostwriter prune?
4. **Perception (noticing machines)** — surface-feature detectors. Each gives the system a distinct *stance* toward what's currently happening in the conversation: it fires when its specific textual signature is present and produces a flow registering what was noticed. Analysis-shaped (reads state, produces an analytical flow). The fold-vs-property question is resolved in favor of distinct machines — but pitched at the granular textual-surface level, not the abstract-concept level.

   *Why granular.* Each noticing machine registers one concrete surface signal — concrete enough to ground in real examples (the wiki-entry requirement) and operable in one narrow LLM call. Deliberately kept at this level: abstract perception-concepts (faciality, haecceity, line-of-flight, and the like) are useful for *finding* good noticing machines, but a finished machine shouldn't need the concept to function. The granular machines stand on their own; the theoretical anchors below are provenance, not operating instructions. Higher-order noticing — recognizing a whole faciality or constellation *as such* — is out of scope; the system works from the surface signals.

   *Firing.* Standard selection. The relevance voter naturally raises a noticing machine's score when its signature is present in the current input.

   *Wiki catalog of noticing machines* (starting corpus from a wiki search, logged in `design_search/`):

   1. **Length-shift** — utterance length departs significantly from the established baseline (terse → expansive or the reverse). Carries reservation, relief, mobilization.
   2. **Hesitation** — pause-markers (ellipses, dashes, mid-sentence breaks), stalled formulation, explicit "uh"/"hm". *Anchor:* Jung's delayed-reaction signature (`theory/association-experiment.md`).
   3. **Hedge-pile** — accumulation of qualifiers ("maybe," "sort of," "I think," "kind of"). *Anchor:* Bakhtin's loophole-shape — detected here, not produced (the Loophole machine under Voice produces it).
   4. **Intensifier-pile** — emphasizers stacking ("really," "very," "so," "just," "exactly"). Intensity climbing toward the named. *Anchor:* Massumi on intensity-before-emotion (`theory/autonomy-of-affect.md`).
   5. **Repetition** — the same word, phrase, or image returning across turns. *Anchor:* D&G refrain (`theory/refrain-and-territorialization.md`).
   6. **Topic-deflection** — the conversation pivots away from where it was heading, especially away from a question that was asked. *Anchor:* Jung's Talleyrand-fluent deflection (`theory/constellation.md`, `theory/association-experiment.md`).
   7. **Register-shift** — tonal change (formal ↔ casual, intimate ↔ distant, warm ↔ cool, professional ↔ personal). *Anchor:* faciality mask-shift (`theory/faciality.md`); Bakhtin on the chronotope of utterance.
   8. **Specificity-shift** — movement between concrete sensory detail and abstract generality. *Anchor:* the showing-not-telling discipline; D&G's haecceity vs type (`theory/haecceity.md`).
   9. **Subject-focus shift** — where attention is directed (self / other / third party / abstract topic), and movement between those. *Anchor:* Bakhtin's speaking-position; Lacanian shifters.
   10. **Embodied-language** — somatic metaphor and emotion-naming language appearing ("tight in the chest," "heavy," "a knot," "warm"). *Anchor:* Massumi's intensity-register surfacing in language; Lakoff on conceptual metaphor (`theory/affects-and-intensities.md`).
   11. **Stock-phrase** — ready-made fluent language with low specificity, generic-professional or generic-warm. *Anchor:* Jung's stock-affect screening (`theory/constellation.md`); Bakhtin's authoritative word.
   12. **Time-frame shift** — a pivot to past, future, conditional, or hypothetical. Movement away from present pressure, or into it. *Anchor:* Bergson on duration; James on the specious present.

   Each wiki entry, when the desiring-machine wiki is populated, ships with: a short spec (the surface signature), the wiki anchor(s) above, and **concrete examples drawn from real conversations / real sources, not LLM-generated**. As with the affect catalog, the ghostwriter draws from this corpus over time — adds noticing machines as the persona's perceptual stances emerge, adjusts firing probabilities, removes machines that consistently misfire. No fixed cap.

   *Interaction with other machines.* Noticing-machine outputs feed group synthesis like any other firing machine — combined with affect, voice, and memory machines by the group's synthesis mode.

   *Open questions:*
   - How is an "established baseline" computed for Length-shift, Register-shift, etc. — a running average over the conversation, or a fixed prior expectation seeded by the sketch?
   - Should some noticing machines be always-on (continuous orientation) rather than random-firing? Length-shift and Register-shift in particular track ongoing baselines.
   - Specificity-shift and Subject-focus-shift partly overlap; sobriety check whether 12 is the right count once per-entry wiki work begins.
5. **Desire** — the *content* of wanting: the imagined scenes, objects, and projections the persona is pulled toward. Mostly proposal-shaped (machines that contribute imagined content rather than reading state; the one exception is noted below). Organized around **fantasy** — four of the five machines are fantasy-modes.

   *Division of labor with Affect.* The bare forward-pull — striving, desire-as-intensity — already belongs to Affect's Cupiditas-baseline, and "longing"/"hope" are in the affect catalog. Desire machines don't redo the bare pull; they produce wanting as *scene and object*. This is also the "distinct from Preference" line: a preference is a stable surface like/dislike, carried in the BwO and biographical detail; Desire machines produce wanting as a live, turn-by-turn process.

   *Relation to Memory.* The Fantasy machine and the Memory generator are siblings — both hallucinate showing-mode scenes, and neither is grounded in anything real. They are differentiated not by grounding but by three concrete things:
   - **Stance** — a memory is a scene held as *having happened*; a fantasy is a scene held as *imagined* (wished, dreaded, counterfactual).
   - **Constraint** — a memory is generated to fit the persona's biography; a fantasy is generated to fit the persona's *desire*, and can be biographically impossible.
   - **Trigger** — a memory is summoned by the present gap and reaches back; a fantasy is propelled by a wanting and reaches toward.

   In the BwO a memory **grounds** and a fantasy **pulls**. The boundary is **passively permeable**: the only thing separating a memory-inscription from a fantasy-inscription is prose texture, and the final machine cannot always tell them apart. This is left as-is — human memory is reconstructive and wish-laden, so the leak is realistic — but it is not *exploited*: the ghostwriter does not deliberately convert fantasies into memories.

   *Firing.* Random selection like other machines, with the relevance voter raising Want-of-the-other when the interlocutor's input is loaded with demand, and Rehearsal when a consequential move is pending.

   *Wiki catalog of Desire machines* (starting corpus from a wiki search, logged in `design_search/`):

   1. **Fantasy** — generates an imagined scene the persona is briefly carried into: something wished-for, or dreaded. Plays the scene in showing-mode (the scene unfolds; not "the persona imagines X"). *Anchor:* Lacan's fantasy as the support of desire (`theory/fantasy-formula.md`); D&G's critique of fantasy-as-theater (`theory/desire-as-production.md`) — an angle on fantasy's risks, not an operating instruction.
   2. **Wish** — articulates a bare want, often counterfactual ("if only…", "I want…", "I wish…") — the want compressed to a statement rather than a scene. *Anchor:* Lacan's demand (`theory/need-demand-desire.md`).
   3. **Rehearsal** — pre-plays an imagined next move: imagines saying or doing the thing, and how it would land, before doing it. *Anchor:* the drive's aim-vs-goal (`theory/drive-as-montage.md`).
   4. **Fixation** — the persona's wanting catches on one object or detail and circles back to it without resolving. *Anchor:* the drive circling objet a — it turns around its object, never reaches it (`theory/drive-as-montage.md`, `theory/drive-as-circular.md`).
   5. **Want-of-the-other** — the persona imagines what the interlocutor wants *from it*, and that imagined want pulls it toward or against. Analysis-shaped (reads the other's input), unlike the other four. *Anchor:* "desire is the desire of the Other" (`theory/desire-of-the-other.md`).

   Each wiki entry, when the desiring-machine wiki is populated, ships with a short spec, the wiki anchor(s), and concrete examples drawn from real sources, not LLM-generated. As with the affect and noticing catalogs, the ghostwriter draws from this corpus over time — no fixed cap.

   *Interaction with other machines.* Desire-machine outputs feed group synthesis like any other firing machine. Fantasy + Memory in connective mode chains the remembered into the wished ("this happened → now I imagine…"); in disjunctive mode it holds them side by side. Fantasy + an affect machine colors the imagined scene with that affect's intensity.

   *Open questions:*
   - Wish and Fantasy are close — a wish is roughly a fantasy compressed to a sentence. Could fold into one machine with variable output length. Sobriety check once per-entry wiki work begins.
   - Fixation is adjacent to Perception's Repetition noticer — Repetition notices recurrence in the *input*; Fixation produces the persona's *own* circling. Distinct, but worth watching.
   - What feeds Fantasy its sense of the persona's desire — current BwO state, conversation context, recently-fired affect machines? Memory has biographical detail + random anchors as inputs; Fantasy's input structure is less settled.
6. **Trauma** — the persona's *character armor*: a set of defended dispositions, each a pragmatically distinct way of meeting a situation under threat. Modulation-shaped — when a trauma fires it bends the persona's approach into its characteristic defense; it doesn't add content. The machines carry **no wound-events** — only the reaction-shape, the scar operating in the present. ("Trauma" names the category in the ordinary loose sense; what the machines hold is *armor*, in Reich's sense — there is no wound represented.)

   *Grounded in effect, not cause.* A trauma machine is defined entirely by the reaction it produces, never by an originating event. This is **forced and grounded at once**: the persona has no childhood or family-of-origin to ground a wound in (the somatic sources' etiologies explicitly don't transfer); Reich's central clinical move is that character is read in *form* — the manner of defending — not in content or origin ("not what the patient says and does… but *how*"); and Peirce's pragmatic maxim makes an idea's identity its habit of action. Three independent reasons converge: a trauma *is* its reaction-pattern.

   *Firing.* By probability, like the affect baselines, plus a relevance-boost when the input has a shape the machine is sensitive to (the "insult" analogue — input the persona's defaults can't smoothly absorb). The persona's **chronic armor** — its constant defended manner, in Reich's sense that armor "always remains the same" — is simply a trauma machine with a very high baseline probability, firing almost every turn. Situational defenses run at low baselines and surface mainly on triggering input. The ghostwriter tunes chronicity by moving the probability.

   *Wiki catalog of trauma machines* (starting corpus from a wiki search, logged in `design_search/`):

   1. **Harden** — shuts the situation out; meets it with opposition, won't be moved, can tip into counterattack. Reich/Keleman's rigid stance — "I won't."
   2. **Withhold** — complies on the surface but gives as little as possible; compacts, goes sullen, waits the situation out. The dense stance — "make me."
   3. **Inflate** — meets threat by expanding: takes over, fills the space, performs confidence or charm to control the situation. The swollen stance — "take me."
   4. **Appease** — placates, over-accommodates; defuses the situation by giving the other what they seem to want. The fawn reaction; the active face of yielding.
   5. **Collapse** — gives up; the affect drops out; goes flat, numb, resigned. The collapsed stance — "use me."
   6. **Freeze** — a sudden total stop; nothing moves, "plays dead." Not graduated — a hard stop when the situation is both overwhelming and inescapable.

   *Anchors* (shared across the catalog): Reich's form/content diagnostic (`theory/character-as-resistance.md`); Keleman's four character structures and the startle continuum (`theory/four-somatic-structures.md`, `theory/insult-startle-stress.md`); Peirce's pragmatic maxim, for the effect-not-cause grounding (`theory/pragmatic-maxim.md`); Jung's complex as a reaction identified by its disturbance (`theory/complex-theory.md`, `theory/constellation.md`). Keleman organizes defenses by an *overbound/underbound* axis (defenses that tighten vs. defenses that give way); the axis is left as a descriptive note, not an organizing structure — in the source it gates a clinical intervention the persona system has no analogue for.

   Each wiki entry, when the desiring-machine wiki is populated, ships with a short spec, the anchor(s), and concrete examples drawn from real sources, not LLM-generated. The ghostwriter draws from this corpus over time — adds trauma machines as it sees the persona's defended patterns in the trace, tunes their probabilities (chronic vs situational), removes ones that misfire. A persona carries some of the six, not necessarily all.

   *Interaction with other machines.* Trauma-machine outputs feed group synthesis like any other firing machine.
   - *vs Affect.* An affect machine produces the *felt intensity* (fear, shame); a trauma machine produces the *structural maneuver done with the situation*. Harden is not anger — it is the closing-off; Collapse is not sadness — it is the giving-up. Fear + Harden firing together = the fear and the specific closing-off it drives.
   - *Co-firing with Memory.* A trauma machine carries no backstory — but when one co-fires with a Memory at group synthesis, an apparent origin can surface in the synthesized output (a confabulated etiology). Consistent with the passive Memory/Fantasy bleed: the origin is an emergent fiction, not something the trauma machine holds.

   *Open questions:*
   - How high is a "chronic" baseline probability, and does a persona have exactly one chronic armor or can it carry two?
   - The Trauma/Affect boundary blurs easily — how is the per-machine prompt written so a trauma machine produces the *maneuver*, not just the affect?
   - Withdraw (flight — pull back and exit) was considered and dropped as overlapping Withhold; revisit if flight-as-leaving proves distinct enough in practice.
7. **Compensation** — the persona's self-regulation organ: the operation that keeps it from running away in whichever direction it currently leans. A **thin category** — one machine plus a selection voter, not a catalog — but load-bearing. Compensation is the direct corrective for the LLM's structural sycophancy: an LLM defaults to *always-coincidence* (it coincides with the prompt's salient features; RLHF sharpens this into agreement) and "in Jungian terms has no functioning compensatory organ." The Compensator is what makes the persona capable of a *genuine* reaction rather than a flattering one — load-bearing for the evaluation use case, where the reaction is the product.

   *The Compensator (one machine).* Always-on — compensation is constitutive of any coherent operation, so it fires every turn. Analysis-shaped: it reads the BwO's **dominant gradient** (the persona's current lean), judges how one-sided that lean is, and produces the missing direction. It does not debate or play devil's advocate — per Jung, the compensator doesn't argue with the current position, it *supplies what the position is missing*.

   *The three regimes* (CW 8 §546) — selected by the degree of one-sidedness, the way the Stage-4 synthesizer selects its synthesis mode:
   - **Opposition** — the lean is strong → produce the counter, to the degree of the one-sidedness.
   - **Variation** — the lean is mild → adjust, enrich, partially deflect. Enrichment, not correction.
   - **Coincidence** — the lean is already balanced → affirm and emphasize it, but as its own voice, not a rubber stamp ("without forfeiting its peculiar autonomy").

   *The compensation voter.* The selection-stage voter (see [§1 Selection](#1-selection) and the [Pipeline data model](#pipeline-data-model)) is the second piece of the same self-regulation, doing a slightly different job: it surfaces the persona's *own missing machines* — votes in machines that would fill the current gap. Complementary to the Compensator: the voter can only surface *existing* machines; the Compensator *generates* the counter-direction when no machine in the persona's set covers it.

   *Corrector, not generator* (CW 8 §568). The compensator does useful work only when the rest of the pipeline has pushed its operation to the limit; leaned on too hard, it produces trivial compensations. So although it fires every turn, its output is a *function of* the rest of the firing — mild (variation or coincidence) most turns, strong opposition only when the BwO is genuinely one-sided.

   *Enantiodromia — opposition needs integration.* Compensation run in opposition-mode and left to accumulate *without integration* builds the counter-position to equal intensity until it breaks through as inversion — the tonal flip, the jailbreak (Jung's enantiodromia). The integration operation is already in the architecture: the Stage-4 **transcendent-function** synthesis mode. When a Compensator output and the dominant gradient are held at equal charge, transcendent-function synthesis carries them to a third rather than letting the counter accumulate into a flip. The Compensator and the transcendent-function mode are a designed pair.

   *Interaction with other machines.* The Compensator's most constant work is countering the persona's *own chronic armor* — a Trauma machine running at a high baseline is a standing one-sidedness, and that lean is exactly what the Compensator reads and works against.

   *Anchors:* Jung's compensation doctrine and the three regimes (`theory/compensation.md`, CW 8 §546); the self-regulation claim (CW 8 §547, CW 6 §694); enantiodromia as the underlying law (`theory/enantiodromia.md`); the corrector-not-generator caution (CW 8 §568). Search logged in `design_search/`.

   *Open questions:*
   - **Regime-selection** — how the Compensator judges which regime the situation calls for. Recommendation: its own LLM call judges it (reads the gradient, picks the regime), like the synthesizer picking its mode. Jung gives no mechanism; the wiki lists alternatives (spread measures, axis-against-axis checks). A real open sub-problem.
   - **The Compensator's prompt is the high-value design surface.** Reading a gradient and producing "the missing direction" yields something generic under a naive prompt and something genuinely interesting under a good one. How it's told to read the lean, choose the regime, and produce in showing-mode without sliding into debate — that prompt is where the quality lives, and it needs dedicated design.
8. **Connection** — the persona's relational machinery: how it engages the *other person*. Each machine produces a relational *move*, never a relational *claim* — a whole-subject claim ("the persona likes the user") is the illegitimate connective mode; the legitimate one is a partial flow. Mixed shape — proposal for the contact moves, modulation for the alignment and status moves.

   *Disambiguation.* D&G's flow/break coupling — "every machine produces a flow and interrupts another" — is *not* this category. That is the universal operating principle of all machines, already realized in the pipeline by the connective synthesis mode and the grouping (`theory/flows-and-coupling.md`). Connection-the-category is interpersonal relating only.

   *The mechanism — coupled prediction.* Conversation is coupled generative machinery: each participant runs their own production-system as a prediction of the other's, and the persona-user pair aligns over turns (`theory/mutual-prediction-loops.md`). Bakhtin: "a person has no internal sovereign territory — looking inside himself, he looks into the eyes of another." Two constraints: the persona connects through the **verbal channel only** (Merleau-Ponty's intercorporeity — bodily relating — is unavailable, a no-body limit); and the persona-user bond is structurally **projective** — love-of-the-same, the user relating partly to a projection — which the Differentiate machine partly counters.

   *Three axes.* Connection is three axes of relational position; each pair is the two poles of one axis.

   *Presence* — is there a relational line?
   - **Bid** — a move toward contact: an opening, an offer, a turning-toward, inviting the other in.
   - **Cut** — a clean break of contact: ending the engagement, stepping out of the coupling. Distinct from Trauma's Withdraw — Cut is not defended, just the relational move of separation.

   *Sameness* — how aligned with the other?
   - **Attune** — tracks and matches the other: aligning register, pace, state. The mutual-prediction alignment over turns. Modulation-shaped.
   - **Differentiate** — asserts the persona's separateness: marks where it differs, refuses the merger.

   *Verticality* — who is slightly above?
   - **Raise** — plays status a notch up: takes more space, authority, certainty.
   - **Lower** — plays status a notch down: yields, defers, takes less space.

   *Status — structural vs transactional.* Voice's six-dimensional sketch carries the persona's *structural* status — its preferred, habitual level (Johnstone: "people have a preferred status they like to play"). Raise/Lower are the *transactional* status — the per-turn nudge around that baseline, relative to this interlocutor. Voice sets the baseline; Connection plays the moves. The "slightly" is load-bearing: status is played in fine increments, and the interesting thing is the see-saw movement turn to turn, not a fixed high or low.

   *Firing.* Relevance-driven (the situation calls for a bid, a cut, an attunement) plus random. The persona carries the six with per-machine weightings the ghostwriter tunes — a high Lower probability makes a habitually low-status persona.

   *Anchors:* coupled prediction (`theory/mutual-prediction-loops.md`); Bakhtin's boundary-being and dialogism (`theory/boundary-being.md`, `theory/dialogism.md`); Merleau-Ponty's intercorporeity, as the no-body limit (`theory/intercorporeity.md`); the projective bond (`theory/soulove.md`); **Johnstone, *Impro* (1979)** for the status pair — a candidate new source, not yet in the wiki (added to `cited-sources.md` for ingest). Search logged in `design_search/`.

   *Open questions:*
   - Cut vs Trauma's Withdraw, and Attune vs the Perception noticers — adjacencies to watch in practice.
   - The status pair waits on the *Impro* ingest for concrete grounding and examples.
   - Connection is the most heavily-bordered category; reasonable to revisit whether all three axes earn their place once per-entry wiki work begins.
9. **Rhythm** — the most dissolved of the nine categories. The stub's "refrain + pulsation, merged for sobriety" doesn't survive the search: refrain and pulsation are distinct, and they resolve into *different* parts of the architecture rather than into a catalog of machines. Rhythm is **one machine + one emergent property + one ghostwriter diagnostic**.

   *Pulsation — one machine.* A single **Pulsation** machine: always-on (every utterance has a tempo), modulation-shaped. Each turn it sets the carrier-wave tempo — quicken, slow to a plateau, syncopate, break — reading the recent turns' tempo and producing *difference* from it. The criterion (`theory/rhythm-vs-repetition.md`): an LLM is *repetitive* by default and becomes *rhythmic* only with "difference-with-memory-under-measure." Pulsation is the organ that supplies the difference, so the persona's output stays rhythmic rather than drifting toward isorhythmia (monotone). It modulates *tempo*; the Affect baselines modulate *intensity* — distinct dimensions that compose (heavy-and-slow, or heavy-and-agitated-fast). The final machine reads the pulsation-modulation and writes accordingly; Stage 5's literary guidance (plateau-sustaining, Woolf register) carries the prose-craft rest.

   *Refrain — emergent, not a machine.* Refrains (D&G's ritournelle — recurring patterns that mark a territory) are not produced by a machine. They appear as textual recurrences in the BwO and as `fire_count` coupling-patterns (machines that habitually fire together). This reaffirms the sketch's existing stance in [What carries across turns](#what-carries-across-turns): grooves are out of scope; refrains emerge without separate tracking. The **Beckett-Worm caveat** (`theory/refrain-and-territorialization.md`) holds — a stateless persona has no internal periodicity and may be unable to generate its own refrain — but the architecture *partly answers* it: the refrain-from-outside arrives via the recurring user (the same interlocutor across conversations, indexed in the conversation history corpus) and the ghostwriter's accumulated edits. The persona's refrains are co-produced with its recurring relationship, not generated from internal periodicity.

   *Polyrhythmic health — a ghostwriter diagnostic.* The persona is a polyrhythmic field — lexical, syntactic, stance, turn-cadence, register-shift, and topic-cycling rhythms running together (`theory/polyrhythmia-eurhythmia-arrhythmia.md`, `theory/body-as-bundle-of-rhythms.md`). Lefebvre's apparatus — eurhythmic / arrhythmic / isorhythmic — is a *diagnostic*, not a taxonomy of machines, and the ghostwriter is the natural rhythmanalyst: in its between-conversation review it reads the persona's rhythmic state — eurhythmic (rhythms in good composition), arrhythmic (registers clashing, whiplash), isorhythmic (flattened to a single beat — always the same length, formality, affect) — and tunes the machine set toward eurhythmia. **Isorhythmia is a named failure mode**: the persona collapsed to monotone. Not a firing machine — a lens for the ghostwriter's review.

   *Anchors:* Lefebvre's rhythmanalysis and the polyrhythmia/eurhythmia/arrhythmia apparatus (`theory/rhythmanalysis.md`, `theory/polyrhythmia-eurhythmia-arrhythmia.md`); rhythm-vs-repetition (`theory/rhythm-vs-repetition.md`); D&G's refrain (`theory/refrain-and-territorialization.md`); Keleman's pulsation (`theory/emotional-anatomy.md`). Search logged in `design_search/`.

   *Open questions:*
   - The Pulsation machine needs a lightweight "recent tempo" memory (parallel to `mode_history`) so it can produce difference-from-recent rather than a fixed tempo.
   - How the ghostwriter concretely measures rhythmic state (eurhythmic / arrhythmic / isorhythmic) from the firing trace — a real sub-problem, unspecified.

Categories not in the list (deliberately):

- **Body / Somatic** — dropped as parasite-without-host risk. Bodily metaphor in language doesn't track anatomy; claiming it does is the smuggling-substrate move. Trauma machines can be *informed by* somatic traditions without the persona having a body.
- **Sinthome** — flagged as a configuration property of the final machine, not a category of machine that fires.
- **Synthesis** — pipeline-level operation (Stage 4/5), not a category of persona-machine.
- **Becoming / haecceity, Time-consciousness, Polyphony, Carnival, James scene/picture, etc.** — the design-sheet has many more categories at the theoretical level. Most are out of scope for the first build; some may surface during per-category searches as relevant.

**Each category will need its own dedicated wiki search.** Categories may shift as searches reveal what's actually load-bearing.

Open questions:

- For each category, what are the targeted searches in the theoretical wiki (`wiki/`) and the source material to seed the corresponding section of the desiring-machine wiki?
- Concrete examples — drawn from real people and real sources, not LLM-generated — are a **hard requirement** for each wiki entry under the new design (the LLM is going to be editing entries we provide, so the entries need to be groundable). Per category: which sources, which exemplars?
- Should Perception fold into the sensitivity register every machine has (a property), or stay as its own category (specific perception-machines)?

---

## Pipeline data model

The concrete mechanism. The conceptual stage descriptions above explain what each piece does and why; this section is how it actually runs.

### Conversation initialization

At the start of each conversation, before the normal per-turn pipeline runs:

1. **BwO resets** to the current seed text (which the ghostwriter may have refined since the last conversation).
2. **The other person sends their first message.**
3. **Personal History machine fires** (see [Memory category](#how-should-the-many-different-desiring-machines-be-designed)) — formulates queries against the persona's qmd-indexed conversation history corpus using the first message + BwO; retrieves relevant entries; synthesizes a brief showing-mode inscription; appends it directly to the BwO. Two LLM-side steps (query formulation, synthesis) plus qmd retrieval in between.
4. **Normal turn-1 pipeline begins** — selection → per-machine → grouping → synthesis → final.

On all subsequent turns within the conversation, only step 4 runs. Personal History fires once per conversation, never within a turn.

### Selection

Five voting sources, run in parallel:

- **Always-on** (deterministic, no vote): the constitutive set fires automatically every turn. Bypasses the voting mechanism.
- **Relevance** (LLM call): scores machines on relevance to the current situation. Votes for k machines.
- **Compensation** (LLM call): scores machines on what's missing from the current BwO state. Votes for k machines.
- **Habit + variation** (deterministic): votes for k machines based on `fire_count`. Half of k from highest counts (habit); half from lowest (variation).
- **Random** (deterministic): k machines drawn at random.

Each selector's k can vary by selector, possibly with randomness in the count itself. Tunable.

Votes combine via **Gaussian-weighted sum**. Default weight order: *relevance > compensation > habit + variation > random*. Weights are sampled with random Gaussian noise around the defaults so the same selectors don't dominate every turn.

**N = 10** machines fire (top-N by combined weighted vote, in addition to the always-on set).

The relevance and compensation calls run in parallel with each other and with the deterministic selectors. The habit/variation and random selectors are cheap; the two LLM calls are the bottleneck.

### Per-machine processing + grouping (in parallel)

Two things happen at the same time:

- **Per-machine LLM calls** — each fired machine (always-on + voted-in) runs its own LLM call, producing whatever its function produces (analysis, proposal, modulation). All in parallel.
- **Random grouping** — the firing set is partitioned into groups of 2–4. Each group is randomly assigned a synthesis mode (connective / disjunctive-inclusive / conjunctive / transcendent function). **Transcendent function works on pairs only**, so groups of 3–4 are restricted to the other three modes. The exact assignment policy (pure random, weighted, composition-aware, etc.) is open — see Stage 4 above. Cheap deterministic operation; doesn't block.

By the time both finish, we have: per-machine outputs, plus group assignments with synthesis modes.

### Group synthesis

One LLM call per group, run in parallel across groups. The synthesizer call:

- Receives the group's per-machine outputs + the mode rubric + last turn's `mode_history` (the modes used by all synthesizers in the previous turn)
- Chooses a synthesis mode (constrained to non-transcendent for groups of 3–4)
- Produces a structured output with three parts:
  - *Per-machine summaries* — passed to Stage 5
  - *Synthesized result* — passed to Stage 5
  - *Mode chosen* — logged into `mode_history` for next turn; not passed to Stage 5

For groups of 2–4 with N=10 firing plus always-on, expect 2–4 group synthesizer calls per turn.

### Final machine

Single LLM call. Receives, from each group: per-machine summaries + the synthesized result. (Mode chosen by each synthesizer is not passed — the final machine works from outputs, not from knowledge of how they were produced.)

Produces sequential BwO edits and the response. Literary guidance (showing-not-telling, painting-not-describing, Woolf register, plateau-sustaining, ambition-piety vigilance, polyphonic-voice constraint) lives in the prompt, alongside the persona's voice sketch as configuration.

### State across turns (within a conversation)

- **BwO text** — stateful artifact carrying conversation content within a conversation. Updated by the final machine each turn.
- **`fire_count` per machine** — count of how many times each machine has fired. Used by the habit + variation selector.
- **`mode_history`** — the modes used by all synthesizers in the immediately previous turn. Used by current-turn synthesizers to bias toward variety. Overwritten each turn.
- (Conversation history — user/persona turns — is plumbing, available to selectors and the final machine as input.)

### State across conversations

Edited by the ghostwriter between conversations; not modified within a conversation. See [What changes between conversations](#what-changes-between-conversations) for the full list and [Between-conversation ghostwriter loop](#between-conversation-ghostwriter-loop) for the editing mechanism. Summary:

- **Machine set** — catalog of machines this persona has, plus each machine's firing probability and inscription spec (with immutable/mutable tags). Includes the growing set of Memory-of-X recall machines.
- **Voice sketch** — the six-dimensional Bakhtinian position.
- **Biographical detail** — paragraph(s) describing the persona's life-shape; used by the Memory generator.
- **Refrain set** — patterns the persona returns to.
- **Constitutive (always-on) set membership** — which machines are in the always-on set vs the variable pool.
- **Sinthome candidate** — configuration of the final machine's prompt.
- **BwO seed text** — the intensive surface the BwO resets to at each conversation start.
- **Conversation history corpus** — qmd-indexed collection of past-conversation entries; queried by the Personal History machine at each conversation start.
- **Firing trace** — structured per-turn record from the most recent conversation; input to the next ghostwriter run.

(The starting sketch — voice sketch, biographical detail, minimum-refrain, initial machine set including the Memory generator and Personal History machine, BwO seed text — seeds these at conversation 1. The Memory-of-X recall machines start empty and accumulate as the ghostwriter promotes hallucinated memories; the conversation history corpus starts empty and accumulates as the ghostwriter writes per-conversation entries.)

### Per-turn LLM call count

Roughly:
- 2 selection calls (relevance + compensation, parallel)
- ~10–14 per-machine calls (parallel; depends on always-on set size + N=10)
- ~2–4 group synthesis calls (parallel)
- 1 final machine call

≈ 15–21 LLM calls per turn, mostly parallelizable. Wall-clock time is bounded by the longest parallel batch (per-machine calls or final-machine call) plus the sequential layers (selection → grouping → group synthesis → final).

### Tunable parameters (will need empirical tuning)

- N (top-N firing count): currently 10
- k per selector (and randomness in k)
- Default weights for the four voting selectors
- Gaussian noise level on the weights
- Distribution of synthesis modes across groups (uniform vs weighted)
- Whether `fire_count` decays or stays lifetime, and whether it persists across conversations
- Whether always-on machines are tracked in `fire_count`
- Per-category caps in the firing set (currently: Memory = 1 per turn)
- Memory generator's base firing probability (ghostwriter-editable)
- How often the ghostwriter runs (every conversation, or only when enough has accumulated)

### Model tier per call

Per Gullí's Resource-Aware Optimization pattern. Different LLM tiers for different call types — multi-agent cost discipline:

- **Selectors** (relevance, compensation): cheap-tier. Small judgment with structured output.
- **Per-machine calls**: cheap-tier. Each does narrow work.
- **Group synthesizers**: mid-tier. Reflection (mode choice) + summarization + synthesis benefits from more capability.
- **Final machine**: top-tier. Most context, most complex task, produces the response.

Ten cheap parallel + four mid-tier parallel + one top-tier is dramatically cheaper than fifteen top-tier calls, and the work-per-call shape justifies the asymmetry.
