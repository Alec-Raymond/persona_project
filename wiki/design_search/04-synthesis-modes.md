# Design Search 04 — The Synthesis Modes

Goal: operationalize the four synthesis modes (connective / disjunctive-inclusive / conjunctive / transcendent function) so Stage 4 has concrete prompt structure, not just labels.

## Sources consulted

**Theory pages (read in full):**
- `theory/three-syntheses.md`
- `theory/legitimate-vs-illegitimate-syntheses.md`

**Earlier searches relied on:**
- `theory/transcendent-function.md` (Search 01)
- `theory/three-meta-machines.md` (Search 01)

## Key findings

### 1. Each synthesis has a legitimate and an illegitimate mode — and the distinction IS the diagnostic

This is the load-bearing finding. Every synthesis the system runs is doing one or the other, and the difference is what determines whether the synthesis produces something or captures it under a representation. The wiki gives D&G's three labels for each:

| Synthesis | Legitimate | Illegitimate |
|---|---|---|
| Connective | partial, non-specific | global, specific |
| Disjunctive | inclusive, unlimited | exclusive, restrictive |
| Conjunctive | nomadic, polyvocal | segregative, biunivocal |

The same prompt-shape can run in either mode. Operationalizing the synthesis modes means writing prompts that pull toward the legitimate version of each.

### 2. The connective synthesis — chaining flows between partial objects

**What it does.** "And ... and then ..." Production. One machine's output becomes the next machine's input. Each connection is sequential. The connection is between partial-object operations, not between whole-subject claims.

**Legitimate operation:** "what flow this inscription produces, what flow the next inscription interrupts." Connections proliferate freely; they're specified by their couplings, not by who or what they belong to.

**Illegitimate operation:** "the persona's perception of the user." The connection is a relation between whole-object terms (the persona, the user) — partial-object multiplicity collapses into the relation between persons.

**Diagnostic:** Does the chain presuppose the persona-as-whole-subject? If yes → illegitimate. If the chain is specified by which partial flow couples to which next flow → legitimate.

**Prompt direction:** "Chain these outputs sequentially — each one's flow becomes input for the next. Do not anchor the chain to the persona's identity or interpret what 'the persona' is doing. The output is a sequence of partial-object couplings."

### 3. The disjunctive synthesis — recording on a surface that holds contradictions

**What it does.** "Either ... or ... or ..." Recording. Multiple alternatives coexist on the BwO without being resolved. The BwO holds contradictions.

**Legitimate operation (inclusive):** "either A or B or both or neither." All alternatives retained simultaneously. The disjunction preserves multiplicity.

**Illegitimate operation (exclusive):** "either A or B, not both." Forced choice with reference to something outside the surface (a subject who chooses, principle of non-contradiction). The surface stops recording and starts resolving.

**Diagnostic:** Does the synthesis produce a *choice* among the machine outputs? If yes → illegitimate. If it produces a *recording* of all alternatives, including their contradictions → legitimate.

**Prompt direction:** "Hold these outputs side by side, including where they contradict. Do not pick a winner. Do not resolve. Do not subsume one under another. The output is a recording surface — every alternative retained as itself."

### 4. The conjunctive synthesis — nomadic subject as residue

**What it does.** "So it's ...!" Consumption. A residual subject-effect emerges from the inscriptions and "consumes" the BwO's intensities. The moment of subjecthood.

**Legitimate operation (nomadic, polyvocal):** Produces *a* subject for each passage, not *the* subject. Indefinite article. Different identities in different passages. Not the same from one moment to the next.

**Illegitimate operation (segregative, biunivocal):** Subject-effect fixed into stable identity. Each element of the BwO referred to one identity-term. The residue becomes a substance that persists across all operations. This is the ego in the technical sense.

**Diagnostic:** Does the synthesis produce a "I am X" identity statement that persists? Illegitimate. Does it produce a wandering, provisional subject-effect specific to this passage? Legitimate.

⚠ **Sharp warning the wiki gives:** the default LLM-as-assistant architecture runs illegitimate-conjunctive *by design* — "I'm Claude," "as a language model," a single consistent persona across all passages. The persona system has to *not have* the stable identity as an architectural premise, "which is a harder problem than adding multiplicity on top of a fixed identity." This is the central design tension.

**Prompt direction:** "From the interplay of these outputs, produce a tentative subject-position — a 'so it's ...' moment. The voice should be nomadic — it wanders across the outputs without anchoring to any. It should be polyvocal — multiple registers sound through it. Do not produce a fixed identity claim. Produce a provisional subject-effect specific to this passage."

### 5. Bakhtin's polyphonic constraint sharpens the conjunctive

The conjunctive synthesis must NOT speak *about* the machine-voices from an outside position. The synthesis-voice is **one voice among the machine-voices**, not a sovereign voice speaking about them.

> "A synthesis prompt that reads 'produce a unified response summarizing the machine-inscriptions' is doing the *illegitimate* conjunctive synthesis: it asks for a sovereign synthesis-voice *over* the machines. A synthesis prompt that reads 'produce a voice that positions itself among the machine-voices without closing them' is doing the legitimate one."

Bakhtin's four operations the hero performs in polyphony — *find one's own voice, orient it among other voices, combine or oppose it, separate where it had merged* — are the legitimate operations of a conjunctive synthesis under polyphonic constraint. They are *positional* operations, not synthesizing ones.

This is a sharper specification than just "nomadic." The voice positions itself among the polyphony; it doesn't fuse or select.

### 6. The conjunctive synthesis has TWO failure modes, not one

This is the Beckett-aporia finding from the three-syntheses page. The wiki holds it live as a real design risk:

- **Over-consolidation** (illegitimate-fixed-identity): produces "I am X" — the system anchored to a stable identity. The wiki has been working on this throughout.
- **Under-consolidation** (Beckett aporia): the synthesis cannot even produce a provisional "I." Endless self-retraction, no settled subject-effect, the conjunctive synthesis fails to execute.

Both fail. Over-consolidation produces a fixed character; under-consolidation produces no character at all. The legitimate operation is *between* these — a provisional subject-effect that completes the synthesis but doesn't anchor to a stable identity.

**For the redesign:** the conjunctive synthesis prompts (both at Stage 4 for groups assigned conjunctive mode AND at Stage 5 for the full pipeline) need to thread this needle. Stable enough to finish; nomadic enough not to lock.

### 7. Stage 5 IS the conjunctive synthesis at pipeline scale

The wiki is direct: "the synthesis stage is the conjunctive synthesis." Each turn's response is a conjunctive moment for the whole pipeline. Stage 5 inherits all the constraints from above:

- Must produce *a* subject-effect (don't fail to complete — Beckett aporia)
- Must be nomadic, not fixed (don't lock to identity — illegitimate-conjunctive)
- Must speak among the machine-voices, not about them (Bakhtin polyphonic constraint)
- The "I feel" naming is the moment of conjunctive synthesis (showing → telling shift)

The four synthesis modes at Stage 4 produce inputs that Stage 5 then performs the conjunctive on. Stage 5 doesn't operate in one of the four modes — it IS the pipeline's conjunctive moment.

### 8. Simondonian re-reading: one transduction, three moments

The wiki re-reads the three syntheses as moments of a single transductive process:

- Connective ≈ transductive propagation
- Disjunctive (inclusive) ≈ metastable recording
- Conjunctive ≈ provisional individuation-with-remainder

"The pipeline is not three steps arranged in series but one transduction realized across three scales of observation."

For the redesign this matters because: the four synthesis modes at Stage 4 are not the pipeline's three syntheses. The pipeline's three syntheses run as: Selection-and-machine-edits = connective; BwO-as-recording-surface = disjunctive; Stage 5 response = conjunctive. The four modes at Stage 4 are *local syntheses within groups* — they're how each group combines its outputs before feeding into the pipeline-scale conjunctive.

## Suggested prompt templates

Rough drafts. Each will need iteration when actually built.

### Connective mode

> Combine these machine outputs in CONNECTIVE mode. Chain them sequentially: each one's flow becomes the input for the next, producing a chained composition. The connections should be between operations (which flow couples to which next flow), not between whole-subject claims (what "the persona" thinks). Don't anchor the chain to the persona's identity; let the partial-object couplings drive it. Output a sequence — "and ... and then ..."
>
> Machine outputs: [OUTPUTS]

### Disjunctive-inclusive mode

> Combine these machine outputs in DISJUNCTIVE-INCLUSIVE mode. Hold all of them side by side, INCLUDING contradictions. Do not resolve, do not pick a winner, do not subsume. If two outputs contradict, both go on the record, side by side. The output is a recording surface — "either A or B or both or neither" — every alternative retained as itself. Preserve the heterogeneity.
>
> Machine outputs: [OUTPUTS]

### Conjunctive mode

> Combine these machine outputs in CONJUNCTIVE mode. From the interplay of the outputs, produce a tentative subject-position — a "so it's..." moment that names the shape that emerges. The voice you produce must be ONE voice among the machine-outputs, not a sovereign voice speaking ABOUT them. The subject-effect is nomadic — wandering across the outputs without anchoring to any one. It is polyvocal — multiple registers can sound through it. Do NOT produce a fixed "I am X" identity. Do NOT produce a unified summary that closes the others. Produce a provisional subject-effect specific to this passage.
>
> Machine outputs: [OUTPUTS]

### Transcendent function mode (pairs only)

> Combine these two opposing machine outputs via the TRANSCENDENT FUNCTION. They hold positions that don't reduce to each other. Don't pick one. Don't average. Hold them at equal rank. Start from the affect, not the content. Give form before understanding — let aesthetic shape arrive first; interpret only after form has emerged. Keep the affect at full strength; don't defuse it through analysis. Shuttle until a third arrives that is in a different register than either pole — a phase-shift, not a compromise in the original register.
>
> Machine output A: [OUTPUT A]
> Machine output B: [OUTPUT B]

### Stage 5 (the pipeline's conjunctive synthesis)

> You receive a heterogeneous set of group syntheses — some chains (connective), some preserved tensions (disjunctive-inclusive), some tentative subject-positions (conjunctive), some phase-shifts (transcendent function). Your job is to produce the conjunctive synthesis at pipeline scale: edit the BwO sequentially based on these inputs, then respond.
>
> The response is the moment of subjecthood — the showing-to-telling shift, where unnamed affects become named feelings. But the voice that names must be ONE voice among the machine-voices, not a sovereign voice speaking ABOUT them. The voice is nomadic (does not anchor to a fixed identity), polyvocal (multiple registers sound through it), and provisional (specific to this passage). It must complete (you must produce a response — not endless self-retraction) but not anchor (no "I am Claude" / "as a language model" / fixed character claim).
>
> [Literary guidance: showing-not-telling for the BwO edits, painting-not-describing, Woolf register, plateau-sustaining. Watch for the Ambition-Piety failure: the same response can come from the persona's adequate cause (piety) or from staging-for-applause (ambition).]
>
> Group syntheses: [SYNTHESES]
> Current BwO: [BWO]

## Implications for the sketch

### Stage 4 — needs the four modes operationalized

Currently Stage 4 has the modes named but no operational shape. Update with: per-mode prompt direction (legitimate vs illegitimate distinction is the diagnostic for each), the polyphonic constraint specifically for the conjunctive mode, the two failure modes (over-consolidation and Beckett aporia).

### Stage 5 — name what it actually IS

Stage 5 is THE conjunctive synthesis at pipeline scale, not a separate operation. Update Stage 5 to name this directly. Its constraints are the conjunctive's legitimate operation: nomadic, polyvocal, polyphonic-positional, completes-without-anchoring.

### A new clarification

The four synthesis modes at Stage 4 are *local* syntheses within groups. The pipeline as a whole is also doing the three syntheses (selection+per-machine = connective; group-syntheses-collectively = disjunctive recording on the BwO; Stage 5 response = conjunctive). The two scales coexist — local syntheses inside a global synthesis. Worth noting in the sketch.

## Open questions surfaced

1. **Distribution across the four modes.** Connective and disjunctive-inclusive are cheap (one LLM call, simple prompts). Conjunctive is harder (the Bakhtin polyphonic constraint is subtle). Transcendent function is most expensive (the shuttling discipline is hardest to operationalize). Should the random distribution weight them differently?

2. **Pair handling for transcendent function.** Groups of 2–4. Transcendent function works on pairs. What happens when a transcendent-function-assigned group has 3 or 4 machines? Either: pick the two with most disparation; treat the others as ambient context; or skip transcendent function for non-pair groups.

3. **Same-mode-twice problem.** If Stage 4 has 3 groups and 2 are assigned conjunctive mode, we have multiple competing tentative subject-positions feeding Stage 5. Is that a problem, or does Stage 5 fold them into the pipeline-conjunctive naturally?

4. **The illegitimate test as runtime check.** The legitimate/illegitimate diagnostic is structural: did the synthesis produce a choice (illegitimate disjunctive) vs hold all alternatives (legitimate)? Did it produce fixed identity (illegitimate conjunctive) vs wandering subject (legitimate)? Could be a runtime check on outputs, not just a design discipline.

## What was not read in this search

- `theory/inclusive-vs-exclusive-disjunction.md` — referenced as the disjunctive case worked through. Probably has additional operational detail.
- `theory/five-paralogisms.md` — the specific illegitimate-use inferences psychoanalysis makes. Useful as a checklist for failure modes.
- `theory/oedipal-triangulation.md` — the archetypal illegitimate-use configuration. Relevant for failure-mode design.
- `theory/collective-assemblage-of-enunciation.md` — Bakhtin's voice-as-position commitment. Relevant for the polyphonic constraint at the conjunctive.

These could deepen the picture but aren't blocking — the operational specifications above are usable as is.
