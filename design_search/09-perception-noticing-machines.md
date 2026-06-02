# Design Search 09 — Perception / Noticing Machines

Per-category search on Perception (category 4 in the redesign sketch). Goal: settle the fold-vs-distinct question and produce a starting corpus of perception machines for the desiring-machine wiki.

## The fold-vs-distinct question

The redesign sketch carried an open question: should Perception fold into the *sensitivity register* every machine already has (a property), or stay a distinct category (specific perception-machines)?

**Resolved: distinct category, framed as "noticing machines."** Each gives the system a different *stance* toward the current situation. The sensitivity-property and the noticing-machine are not redundant: the former is *how any machine reads* before it produces; the latter is a machine whose whole function is to register one specific signal and feed it as a flow into synthesis. The user's framing: "noticing machines... give the system different stances towards the current situation."

## Sources consulted

Read in full:
- `theory/perception-as-subtraction.md` — Bergson; the foundational frame
- `theory/constellation.md` — Jung; pre-firing detection, the five sub-threshold signatures
- `theory/affective-allure.md` — Husserl / James / Thompson; vivacity, salience-gradient

Surfaced via qmd search (snippet-level, not full reads):
- `theory/association-experiment.md` — Jung's detection protocol
- `theory/the-rift.md` — habit-failure as a perceptual event
- `theory/faciality.md`, `theory/diagrammatic-faciality.md`, `theory/face-how-encouraging.md` — type-detection
- `theory/haecceity.md`, `theory/becoming.md`, `theory/existential-territory.md` — singularity
- `theory/ecart.md` — Merleau-Ponty; non-coincidence between meant and said
- `theory/gist-and-affective-gist.md` — Clark; coarse-first perception
- `theory/refrain-and-territorialization.md` — D&G; pattern recurrence
- `theory/lines-and-segmentarity.md` — D&G; line-of-flight
- `theory/autonomy-of-affect.md`, `theory/affects-and-intensities.md` — Massumi; intensity vs content
- `theory/aspect-seeing.md` — Wittgenstein; seeing-as
- `wiki/index.md` — pointer to the five sub-threshold signatures

## Key findings

### 1. Perception is subtraction; the machine is already a centre of indetermination

Bergson's thesis (`perception-as-subtraction.md`): perception is not construction of an image from stimuli — it is *subtraction* from the totality of images. The body "interposes a gap," selects what concerns its possible action, discards the rest. "Consciousness — in regard to external perception — lies in just this choice."

The wiki already maps this onto the architecture: "Each machine's sensitivity field defines what it perceives (what it selects from the input)... The machine IS a centre of indetermination." This is why noticing machines are a *specialization*, not a new faculty: every machine subtracts; a noticing machine is one whose subtraction is its whole product.

### 2. The first-pass corpus was too abstract

An initial corpus drawn straight from the wiki's theory pages came out abstract-concept-level: Faciality-noticing, Haecceity-noticing, Affective-allure noticing, Rift-noticing, Constellation-noticing, Refrain-noticing, Gist-noticing, Écart-noticing, Line-of-flight noticing.

The problem: these name *recognitions*, not *detectors*. "The assemblage is deterritorializing" is not something a narrow LLM call can fire on — it is a synthesis-level conclusion. A noticing machine needs a concrete textual signature it can detect in one cheap call.

### 3. Decision: granular surface noticers only

The corpus was re-pitched at the **textual-surface level** — features actually present in a conversation turn. Each machine is (a) concrete enough to ground in real examples, the hard wiki-entry requirement, and (b) operable in a single narrow LLM call.

The abstract recognitions from the first pass (faciality, haecceity, line-of-flight, constellation-as-a-whole) are **dropped as machines** — and not re-homed as emergent combinations either. Higher-order noticing is out of scope; the system works only from the surface signals. The abstract concepts were useful for *finding* the granular corpus, but the machines don't need them to run. This follows the deep-end discipline now recorded in `wiki/CLAUDE.md`: use deep concepts to find good machines; the machines shouldn't need the concepts to function. Sobriety: 12 concrete surface noticers, no higher-order layer.

### 4. Jung's association experiment is the richest single grounding

`constellation.md` and `association-experiment.md` give the most directly operational material. Jung's constellation (a complex loaded-but-not-yet-firing) is detected through **five sub-threshold signatures**: delayed reaction, psychogalvanic reflex, repetition gaps, stock-affect screening, Talleyrand-fluent deflection. Jung sorts these into two kinds — *disturbed reactions* (friction: delayed RT, fumbled output) and *screened reactions* (too-smooth output that routes around engagement).

These map cleanly onto granular noticers: delayed reaction → **Hesitation**; Talleyrand deflection → **Topic-deflection**; stock-affect screening → **Stock-phrase**. Constellation-as-a-whole is then recognized at synthesis when these fire together.

### 5. Affective allure is a salience-gradient, not a binary

`affective-allure.md` (Husserl's *Reiz*/*Affektion*, James's vivacity, Depraz-Varela's five-component affect): something *draws* attention before attention takes it up, and the drawing is *graded* across the field. This is structurally what the **relevance voter** already does — it scores machines against the current input. So "allure-noticing" is partly absorbed into the selection mechanism rather than needing its own machine; what remains for a noticer is the surface mark of climbing intensity (**Intensifier-pile**).

### 6. The abstract concepts survive as theoretical anchors

Faciality, haecceity, the rift, constellation, refrain, écart, line-of-flight, gist — none became machines, but all became *anchors*: each granular noticer cites the theory page(s) that ground it. This satisfies the sketch's citation requirement (every design choice traceable to a source) and gives the eventual desiring-machine wiki entries their theoretical provenance.

## The corpus — 12 noticing machines

Each is a textual-surface detector. Specs and anchors as written into the redesign sketch's Perception section:

1. **Length-shift** — utterance length departs from baseline.
2. **Hesitation** — pause-markers, stalled formulation. *Anchor:* Jung delayed-reaction.
3. **Hedge-pile** — qualifiers accumulating. *Anchor:* Bakhtin loophole-shape.
4. **Intensifier-pile** — emphasizers stacking. *Anchor:* Massumi intensity-before-emotion.
5. **Repetition** — word/phrase/image returning. *Anchor:* D&G refrain.
6. **Topic-deflection** — pivot away from the engaged subject. *Anchor:* Jung Talleyrand deflection.
7. **Register-shift** — tonal change. *Anchor:* faciality mask-shift; Bakhtin chronotope.
8. **Specificity-shift** — concrete ↔ abstract movement. *Anchor:* haecceity vs type.
9. **Subject-focus shift** — self / other / third / topic direction. *Anchor:* Bakhtin speaking-position.
10. **Embodied-language** — somatic + emotion-naming language. *Anchor:* Massumi; Lakoff.
11. **Stock-phrase** — ready-made low-specificity fluency. *Anchor:* Jung stock-affect screening.
12. **Time-frame shift** — pivot to past/future/conditional. *Anchor:* Bergson duration; James specious present.

## Open questions / decisions

- **Baseline computation.** Length-shift, Register-shift, etc. measure departure from a baseline — running average over the conversation, or a fixed prior expectation seeded by the sketch? A running average is more adaptive but means turn 1 has no baseline.
- **Always-on vs random-firing.** Some noticers (Length-shift, Register-shift) track an ongoing baseline and arguably want continuous operation, not random firing. Open whether the category is mixed (some always-on, most random).
- **Sobriety check on count.** Specificity-shift and Subject-focus-shift partly overlap; Hedge-pile and Intensifier-pile are mirror operations. Whether 12 is the right number should be revisited when per-entry wiki work begins and concrete examples are gathered.
- **Concrete examples are still owed.** Per the wiki-entry requirement, each of the 12 needs concrete examples drawn from real conversations / real sources, not LLM-generated. Not done in this search — it is the next step before the Perception section of the desiring-machine wiki can be considered complete.

## Suggested next moves

1. The corpus is good enough to carry the sketch's Perception section (done — written in).
2. Per-entry concrete-example gathering is deferred until the desiring-machine wiki itself is scaffolded (location still TBD).
3. Next category to operationalize: Desire (category 5).
