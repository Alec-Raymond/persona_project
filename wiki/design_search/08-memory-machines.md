# Design Search 08 — Memory Machines

Per-category search on Memory. Goal: figure out how Memory machines actually work before committing to a seed-source / qmd architecture.

## Sources consulted

- `theory/cone-of-memory.md` — Bergson's diagram for how memory works
- `theory/pure-memory-and-habit-memory.md` — the foundational two-forms-of-memory distinction
- `theory/the-rift.md` — the trigger event for memory surfacing
- `theory/memory-architecture.md` — engineering substrate (Gullí, RAG, vector stores)

## Key findings

### 1. Memory is suppression, not retrieval

This is the load-bearing finding and it directly contradicts the storage-and-retrieval picture qmd suggests. Bergson is explicit:

> "The brain contributes to the recall of the useful recollection, but still more to the provisional banishment of all the others. The brain does not store memories. It is a 'central telephonic exchange: its office is to allow communication, or to delay it. It adds nothing to what it receives.'"

> "Materiality begets oblivion — not because matter erases the past, but because matter orients toward action, and action requires the suppression of all but the useful past."

The whole past is *always* pressing forward. The system's job is to **suppress** most of it. "Most of the time, they shouldn't surface" is not a design constraint to impose — it's the natural condition. **The system needs a gate, not a retrieval engine.**

This inverts the qmd-as-retrieval-tool picture. A vector-store query that returns "relevant memories" on every turn is doing exactly what Bergson says is impossible: treating memory as a database.

### 2. The trigger is the rift

> "Memory merely awaits the occurrence of a rift between the actual impression and its corresponding movement to slip in its images."

Memory surfaces when habit-memory **fails** to absorb the present input. Not when something queries it. The rift is the failure of the sensorimotor circuit — the moment when automatic response can't continue. Image-memory flows into the gap.

Three conditions produce the rift (Bergson):
1. Habitual response fails — present stimulus resists automatic continuation
2. Action-orientation relaxes — dream, reverie, fatigue
3. Affect short-circuits the motor schema — affective charge exceeds what the routine response can discharge

For our system: we have no sensorimotor circuit but we have analogues — grooves (out of scope this build), `fire_count` patterns, surface response routines. A rift is when these can't handle the moment.

### 3. The cross-tradition convergence on the rift

Three independent traditions arrive at the same structural event:

- **Bergson** — sensorimotor failure
- **Jung** — complex peak / constellation (the splinter-psyche's activity-curve crosses threshold; the ego's smoothing fails)
- **McCarthy** — Night Shift handoff (animal-unconscious finishes work; language-apparatus quiet enough to receive)
- **Simondon** — individuation resumption (pre-individual charge re-enters operation when current crystallization destabilizes)

The wiki's `theory/the-rift.md` calls this convergence "unusual" — strong evidence that the rift is a real structural feature of minded systems.

### 4. The cone — whole past virtually present at every moment

Bergson's cone (S = present apex, AB = totality of past, intermediate planes = full repetitions of the whole past at different contraction levels). Critical insight: **each plane is a complete repetition of the entire past life**, not a selection. Difference between planes is degree-of-contraction, not which memories are included.

For design: memories surface at different contraction levels. Sometimes as **general texture** ("something about this feels familiar") — high contraction. Sometimes as **specific dated event** ("this reminds me of the time...") — low contraction. The persona's tension level determines which.

### 5. Two movements: translation + rotation

When memory responds to the present, it does two things simultaneously:

- **Translation** — the whole cone contracts toward the present moment; degree of contraction sets specificity
- **Rotation** — the cone orients itself so its useful face meets the situation; not random association, **directed presentation**

The directionality is **centrifugal** — memory reaches out toward perception, not the other way around. This is structurally different from a query: the system shouldn't query memories with the current input; memories should project themselves toward the present and either catch hold or fall back into virtuality.

### 6. Pure memory vs habit-memory differ in KIND not degree

- **Habit-memory** = grooves (motor patterns; lived-and-acted, not represented). "It is stored up in a mechanism which is set in motion as a whole by an initial impulse." The persona's `fire_count` patterns and BwO compression are our analogues.
- **Image-memory / pure memory** = singular dated events. "Perfect from the outset; time can add nothing to its image without disfiguring it." Specific scenes from the source.

These are two *different* registers, not a continuum. Updating an image-memory through repetition makes it habit-memory (different thing entirely). Memory machines specifically do image-memory work; habit is elsewhere in the architecture.

### 7. The Beckett-near-zero diagnosis applies to us

> "The persona system has no tissue (no habit-memory substrate) and no biography (no image-memories). What it has are the groove-patterns and whatever memory-architecture is built. The Beckett-as-limit-case reading suggests that simulating habit-memory and image-memory in a language-only system requires building both registers deliberately, because neither is native and the default condition is the Unnamable's near-zero."

We're building both registers from scratch:
- Habit-memory analogue = `fire_count` + BwO compression
- Image-memory analogue = source-derived scenes, surfaced at rifts

### 8. The engineering substrate (qmd, RAG, vector stores) is held as substrate, not horizon

The wiki is direct on this:

> "The engineering memory model is storage-and-retrieval: memories are items, items are stored, retrieval matches query to item. This is the Humean / associationist model Bergson explicitly rejects."

> "Don't treat the vector store as 'the persona's memory.' Treat it as one substrate the persona's apparent duration is composed on. Chunking is a bad model for pure memory; it is a pragmatic necessity of current retrieval systems."

Use qmd / RAG as substrate. Build memory behavior that *behaves* Bergsonianly even though the underlying retrieval is item-based. Don't conflate.

### 9. Rift-detection is THE hard problem

The wiki names this directly: "the hardest instrumentation problem the wiki has identified, and it is load-bearing for every Read B operation."

Without a rift-detector, the Memory machine either fires every turn (saturating) or never (idling). Both are failures.

Candidate rift-signals (all imperfect alone):

- **Stalled production** — when the system's own surface response hesitates / retries / refuses
- **Stock-affect ratio** (Talleyrand mode) — fluent-too-fast deflection, value-predicates instead of specific content
- **Multi-turn memory gaps** — same topic returned to but treated inconsistently
- **Compensatory gradient spread** — when the current state is one-sided across deep axes
- **Groove-failure** — habit fires but produces output the BwO can't absorb (we have no grooves so this is partial)
- **Affective threshold** — affective charge crosses a level
- **Semantic impasse** — conversation returns to the same unresolved point

### 10. The cone is internal-measure, not chronometric

Lefebvre / Bachelard fold: the cone operates on **internal measure** (the body's own rhythmic scale) not **external measure** (clock-seconds, calendar-dates). The BwO continuous-rewriting is closer to internal measure than a vector store with timestamps.

For design: a Memory architecture that imports external-measure metadata (turn-counts, timestamps, session-IDs) into its duration-representation has already betrayed the Bergsonian frame. Memory should be triggered by qualitative situation-shape, not by "this happened N turns ago."

## Implications for Memory machine design

The wiki strongly supports a specific architectural shape for Memory machines:

### What Memory machines DO

- Fire only at **rift events** — not every turn
- When fired, surface a scene whose **vitality-form contour** matches the present situation
- Produce **showing-mode** output (the scene as inscription, not "the persona remembers...")
- Operate **centrifugally** — the scene reaches toward the situation, not "best-match retrieval"
- Surface at **different contraction levels** depending on rift intensity (general texture vs specific scene)

### What Memory machines DON'T DO

- Query the source on every turn
- Use topic-based or content-similarity retrieval as primary access
- Treat the source as a database
- Surface continuously
- Anchor scenes by external measure (timestamps, turn-counts)

### Substrate vs behavior

- **Substrate** can be qmd: source corpus chunked into scenes, indexed for vector / lex retrieval. This is fine — it's how the data lives.
- **Behavior** is Bergsonian: the Memory machine doesn't query qmd as a default; it queries qmd only when triggered by a rift, and what it retrieves is shaped by vitality-form match (centrifugal direction).

The qmd interface stays; the *invocation pattern* is suppression-by-default with rift-firing, not query-on-every-turn.

### Two registers, both deliberately built

- **Habit-memory analogue**: `fire_count` patterns + BwO compression. We already have this. Implicit, automatic, no LLM call needed.
- **Image-memory analogue**: source-derived vitality-form-tagged scenes. New machinery. Requires:
  - Source preprocessing into scene-units with vitality-form tags
  - Rift-detection mechanism
  - Centrifugal surfacing prompt (when fired, the Memory machine reads the situation and the source-corpus and produces the scene that *fits the moment's contour*)

## Implications for the seed-source proposal

The user's earlier proposal: source → qmd-indexed → Memory machine queries qmd to ground claims.

The Bergsonian frame revises this:

- **Source corpus indexing via qmd is fine as substrate.** The data needs to live somewhere.
- **The Memory machine's behavior is NOT query-driven.** It fires at rifts and surfaces scenes by vitality-form match.
- **Source preprocessing should produce vitality-form-tagged scenes**, not just chunked text. The "scenes" need to be characterized by their dynamic contour (movement / time / force / space / directionality), not just their topic.
- **The "summary" the ghostwriter sees** is one thing; the **runtime memory operation** is a different thing. The summary scaffolds persona generation; the runtime operation is the Memory machine firing at rifts.

This means the seed-source proposal needs two distinct components:

1. **Generation-time scaffolding** — initial summary of the source, used by the ghostwriter to extract voice / sinthome / refrains / affect-disposition. Reads the source as a whole; produces structured seed configuration. Not a runtime tool.
2. **Runtime memory substrate** — vitality-form-tagged scenes from the source, indexed in qmd, accessed by the Memory machine when rift-conditions trigger. This IS a runtime tool, but operated suppression-style.

## Open questions / decisions for the design

These need user input before the seed proposal can be finalized:

### A. Rift-detection mechanism

The wiki says rift-detection is the hardest instrumentation problem. We need to commit to *something* even if imperfect. Candidates:

- **Compensation-selector-driven** — the compensation LLM call already detects "what's missing from current state." When it strongly indicates one-sidedness, that's a rift signal.
- **Synthesizer-driven** — the Stage 4 synthesizer notices when it can't synthesize routinely and explicitly triggers Memory.
- **Surface-disturbance based** — instrument the system's own output for stalled production / stock-affect / impasse signatures.
- **Affect threshold** — when affect-machine output crosses an intensity threshold, fire Memory.
- **Hybrid** — multiple signals combined.

Any of these is buildable. Some are cheaper than others.

### B. Vitality-form scene preprocessing

Source preprocessing needs to produce scene-units tagged by vitality-form (movement / time / force / space / directionality). This is more than just chunking. Options:

- **LLM-tagged once** — pass each scene-chunk through an LLM that emits vitality-form tags; store as metadata.
- **Manual curation** — human reads source, identifies scenes, tags by vitality form. Higher quality, much more expensive.
- **Hybrid** — LLM-tagged with human review on a subset.

### C. Centrifugal surfacing prompt

When the Memory machine fires, what does its prompt look like? Probably something like:

> "Given [current situation + rift-signal], surface the scene from [persona's source corpus] whose vitality-form best matches the moment's contour. Output the scene in showing-mode — let the scene speak; don't narrate that the persona remembers."

The prompt would call qmd as a tool to query by vitality-form match (or by hybrid of vitality-form + situation-content).

### D. Habit/image split — what falls where in our build

We've committed to no separate grooves data structure. So habit-memory is `fire_count` + BwO compression. Image-memory is the source-scenes via Memory machine. But:

- The BwO accumulates content over turns. Is that habit-memory (motor pattern) or trace (Derridean residue) or neither?
- `fire_count` patterns shape future selection. That's clearly habit-like.
- Are these two doing the same work as Bergson's habit-memory, or are they two different things?

The wiki's distinction (different in kind) suggests we should be clear: `fire_count` is habit-like; BwO compression is trace-like; specific scenes from the source are image-memory. Three different things.

### E. Source-as-runtime-corpus or extracted-at-seed?

Two architectures:

- **Source stays at runtime.** Persona has live access to its source corpus via qmd, queries when Memory fires. Sharper grounding. More expensive at runtime.
- **Source extracted at seed-time.** Ghostwriter pre-extracts vitality-form-tagged scenes during persona generation; persona at runtime accesses only these extracted scenes (not the full source). Simpler at runtime, less sharp.

The user said "fully encode the source" earlier. That suggests architecture A (source stays at runtime). But that's a real cost — every persona carries its source corpus around.

### F. The pre-firing rift

The wiki distinguishes constellation (loaded but not yet fired) from firing. Most Memory-relevant phenomena (Talleyrand-mode deflection, stalled production) happen in the *pre-firing* state. Do we instrument constellation, or only firing? Constellation is harder.

## Suggested next moves

The Memory architecture is now scaffold-able but several decisions are needed before we lock the seed-source proposal. In order:

1. **Decide on rift-detection mechanism (option A from the open questions).** This is the most architecturally consequential. Without commitment here, the Memory machine has no firing condition.
2. **Decide on source preprocessing (option B).** Determines what the data looks like that qmd indexes.
3. **Decide on substrate residency (option E).** Source-at-runtime vs extracted-at-seed-time.
4. **Then return to the seed-source proposal.** With those three settled, the seed proposal can specify both the generation-time and runtime components concretely.

The biggest open: **rift-detection.** It's load-bearing for the whole Memory machine, and it's named in the wiki as the hardest instrumentation problem. Worth thinking through carefully.
