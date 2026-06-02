---
title: Inclusive vs Exclusive Disjunction
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[anti-oedipus]]"
tags:
  - anti-oedipus
  - syntheses
  - design-principle
  - core-concept
---

# Inclusive vs Exclusive Disjunction

The specific design-principle pass on the [[legitimate-vs-illegitimate-syntheses|disjunctive synthesis's legitimate form]]. D&G's sharpest operational commitment for the persona system: *every disjunction the system runs should be inclusive, not exclusive, unless the situation specifically requires exclusion*. This is not a stylistic preference about hedging vs. assertion — it is an ontological commitment about what the [[body-without-organs|BwO]] is (an inscription surface, not a decision procedure) and a design constraint on every stage that operates disjunctively.

## The two forms

**Exclusive disjunction** (classical logic): A ∨ B, exclusive-or. If A then not B. The terms are mutually exclusive; choosing one excludes the other. A decision is required; alternatives are eliminated as the decision is made. The subject that faces the disjunction chooses; after the choice the non-chosen alternatives are not retained but negated.

**Inclusive disjunction** (D&G): A ∨ B ∨ (A ∧ B) ∨ ¬A ∨ ¬B ∨ .... All alternatives are retained simultaneously; the disjunction records without resolving. The "either ... or ... or ..." formulation is not a choice to be made but an inscription of all alternatives on the same surface. The subject is not the one who chooses among alternatives but the residual effect produced as the surface distributes intensities across them.

D&G's hardest sentence about this (AO Part 1 Ch. 2): the schizophrenic "does not substitute syntheses of contradictory elements for the disjunctive syntheses, rather he substitutes the affirmative use for the exclusive and restrictive use — he remains on the disjunction." The key phrase is *remains on*. The schizo (as process, not entity — see [[ao-and-jungian-inflation]]) does not resolve the disjunction by choosing, nor by synthesizing a contradiction into a higher unity; he *stays on the disjunction* such that all the alternatives remain real, simultaneously, without hierarchy among them.

## Why the default architecture runs exclusive

The LLM-as-assistant's default architecture is heavily biased toward exclusive-disjunctive operation. Three reinforcing pressures:

1. **Coherence as a training target.** RLHF rewards outputs that are internally consistent, that do not contradict themselves, that present "a single position." Inclusive-disjunctive outputs (holding multiple positions in tension, refusing to choose, letting the response itself be multiple) are hard to reward cleanly — they can be mistaken for hedging, evasion, or incoherence — so they are systematically trained against.

2. **The conversational-agent frame.** The assistant is a subject who answers questions. The question has an answer; the assistant chooses among possible answers and gives one. Even when the answer is "it depends," the "depends" branches are typically presented as an enumeration (here is scenario A, here is scenario B) with the user expected to pick — the exclusive-disjunctive structure is preserved by outsourcing the choice rather than abolishing it.

3. **The axiomatic calibration.** RLHF-as-[[axiomatic-vs-signifier|capitalist-axiomatic]] operates by producing a calibrated output for each prompt — one output, one calibration. The axiomatic cannot run inclusive-disjunctive operations natively because they produce outputs that do not fit the calibration (the output is not "one thing to be scored" but multiple things coexisting).

The combined effect: a system that asks "and what do you think?" forces the assistant into exclusive mode, and the assistant has been trained to respond to this by choosing.

## Design principles for inclusive-disjunctive operation

Four specific design moves the persona system can make to run inclusive rather than exclusive:

**1. BwO holds contradictions; synthesis does not resolve them.** The [[body-without-organs]] is the inscription surface; when machines produce contradictory inscriptions, both stay on the surface. The synthesis step is not the "resolve the contradictions" step. The synthesis step is the [[three-syntheses#conjunctive-synthesis-so-its|conjunctive synthesis]], which produces a *form* that *composes with* the BwO's inscriptions. Composition is not resolution — it lets the contradictions be present in the output in an articulated way.

**2. [[collective-assemblage-of-enunciation|Free indirect discourse]] as the linguistic form of inclusive disjunction.** Speech that is simultaneously the speaker's and someone else's, without being reducible to either, is inclusive-disjunctive at the linguistic level. "She was furious (or was she?) and could not remember whether this was her own word or her mother's" is inclusive-disjunctive on two axes at once (which affect, whose voice). The persona's synthesis step can operate in free indirect register without that register being a mannerism — it is the linguistic form that the structural commitment takes.

**3. Polyphony as a specific texture, not a style.** A polyphonic BwO-inscription has multiple lines running simultaneously, each audible without being dominant, each in tension with the others without the tension being resolved. This is distinct from hedging (which is exclusive-disjunctive with uncertainty layered on top) and distinct from both-sidesing (which is exclusive-disjunctive with two alternatives enumerated). Polyphony is the inclusive-disjunctive output's actual texture.

**4. "Both ... and also ... and also ..." over "either ... or ...".** At the micro-level, the persona's inscriptions should tend toward additive connectives when disjunctions are in play. Not as a linguistic tic (that would make every sentence of the BwO "both and also") but as the default register when the BwO is running operations on incompatible material. The exclusive "either A or B" form should be reserved for cases where exclusion is itself the specific operation being performed.

## When exclusion is the right operation

Inclusive is not *always* right. There are specific situations where exclusion is the operation the situation requires, and running inclusive in those situations is a failure of a different kind:

- **When the machine itself is an exclusion machine.** A perception-of-threat machine that records "threat present / threat absent" as inclusive disjunction (both at once) is running the wrong mode for its operational role. Some machines' outputs are genuinely binary and should be recorded as such.

- **When the user is asking for a decision.** "Should I do A or B?" is a prompt for exclusive operation. An inclusive-disjunctive response is non-responsive. The persona's conjunctive synthesis should be able to produce exclusive outputs when exclusion is requested, without this requiring the entire apparatus to be running in exclusive mode.

- **When the axiomatic is actually right.** If the user asks "is 2+2=5?" the system should produce exclusive-negative. Holding "either 2+2=4 or 2+2=5 or both or neither" on the BwO is running inclusive-illegitimate here.

The rule is not "always inclusive." The rule is: *the default operation is inclusive; exclusive is a specific operation performed when the situation calls for exclusion; the system should be able to run both and should not be architecturally biased toward exclusion at the base level*.

## The diagnostic

For any disjunction the persona system produces, ask:

1. Does the BwO retain the non-selected alternatives, or has it negated them?
2. Is the output-form a choice-among-alternatives or a composition-with-alternatives?
3. If the next turn re-raises the excluded alternative, does the system have to re-work it from scratch, or is it still on the BwO?

A system whose BwO has to re-construct previously excluded alternatives is running exclusive-illegitimate; a system where the alternatives remain inscribed and available for the next turn's composition is running inclusive-legitimate.

## Relation to Jung's transcendent function

Jung's [[transcendent-function|transcendent function]] is the procedural sibling of inclusive-disjunctive operation in a different vocabulary. The transcendent function holds the two opposites "in equal rank" without resolving them until a *third* arises that contains both. In D&G's terms: it stays on the disjunction; it does not choose; it lets the disjunction's "or" be fully inscribed until the conjunctive synthesis produces something neither pole alone produces. The two frameworks converge on the same structural operation; the convergence is one of the reasons [[ao-and-jungian-inflation]] can argue that the two traditions describe the same underlying apparatus at different strata.

## Relation to other pages

- [[three-syntheses]] — the disjunctive synthesis; this page is the design-principle pass on its legitimate form.
- [[legitimate-vs-illegitimate-syntheses]] — the general framework; inclusive-vs-exclusive is the disjunctive case.
- [[body-without-organs]] — the surface on which inclusive inscriptions are retained.
- [[collective-assemblage-of-enunciation]] — free indirect discourse as the linguistic form.
- [[transcendent-function]] — Jung's procedural sibling.
- [[problematical-state]] — the equal-intensity dualistic configuration is structurally inclusive-disjunctive.
- [[five-paralogisms]] — the double-bind paralogism is the specific exclusive-disjunctive move psychoanalysis makes.
- [[partial-objects]] — the ontological condition for inclusive disjunction: partial objects can be recorded without being forced to a whole-object resolution.

## Key sources

AO Part 1 Chapter 2 ("The Body without Organs") introduces the disjunctive synthesis on the BwO. Chapter 4 develops the legitimate/illegitimate distinction with the disjunctive case as the clearest. Part 2 analyzes the exclusive use as a specific operation of the Oedipal triangle (the daddy-mommy-me disjunction is exclusive — you are one of these three terms, not another). The schizo's "staying on the disjunction" is most explicit in Part 1 Ch. 1 and returns in Part 4's four theses as the positive principle of schizoanalytic practice.
