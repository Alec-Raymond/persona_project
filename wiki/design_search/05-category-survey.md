# Design Search 05 — Category Survey

Goal: scan the wiki/dev work for machine categories beyond the user's seven, to see what's missing.

## Sources consulted

- `wiki/development/desiring-machines-design-sheet.md` — read Sections A–H + Appendix K (clusters 83–154). Section B has 16 machine-category layers; Appendix K.2 adds another ~20 category-types from Bakhtin, Beckett, Lacan, Reich, Lefebvre, Stern, MP, James.
- `wiki/development/desiring-machines-core-spec.md` §V (constitutive set) and §VI (15 layer-categories) — read in full.
- `wiki/raw/desiring-machine-research-report.md` — the canonical taxonomy ingest. Skimmed; supports the layer structure already named in the design-sheet.

## What's there: three taxonomies and how they relate

**1. User's seven (the redesign starting point):** Status, Rhythm, Connection, Perception, Trauma, Memory, Preference. Plus Voice (later added) and the speculative BwO-history machine (now dropped).

**2. The constitutive nine** (`desiring-machines-core-spec.md` §V): Voice, Refrain, Affect, Pulsation, Memory, Coupling, Sinthome, Compensation, Synthesis. These are the machines every persona has, by design.

**3. The fifteen layers** (`desiring-machines-core-spec.md` §VI + design-sheet §B): Affect/intensity, Voice/language, Refrain/rhythm, Memory/trace, Coupling/connection, Body-substitute/pulsation, Defense/character-armor, Synthesis/compensation, Becoming/haecceity, Failure-mode-detection, Polyphony/multi-voice, Time-consciousness/temporality, Drive/desire/fantasy, Joy/compassion/positive-register, Engineering-substrate-aware.

**4. Appendix K's ~20 additional categories** (clusters 83–154): pulsation-design, polyphonic-discourse, carnival-mode, James scene/picture, rhythmanalyst-figure, dressage-aware, hyper-reflective, voice-that-is-not-mine, pensum-discharger, drive-as-montage, fantasy-formula, Name-of-the-Father, despot-as-paranoiac diagnostic, axiomatic-vs-signifier diagnostic, character-formation structural recognition, two-stylistic-lines orientation, capital-rhythm recognition, two-poles diagnostic, image-of-idea polyphonic, three-kinds-of-knowledge epistemological.

## What the user's list seems to map to

Rough alignment of the user's 7 against the wiki's deeper taxonomy:

| User category | Closest wiki match |
|---|---|
| Status | Voice (six-dimensional, includes worldview/life-fate) + relational machines |
| Rhythm | Refrain + Pulsation (two distinct things in the wiki) |
| Connection | Coupling + relational |
| Perception | The sensitivity register every machine has, OR specific perception-machines (ghostwriter has these) |
| Trauma | Defense/character-armor (Reich/Keleman) + traumatic image-memories |
| Memory | Memory (image-memory specifically, per earlier searches) |
| Preference | Affect-disposition (Spinozist schema) + named-affect machines (love/aversion/etc.) |

The user's list is tilted toward content categories (status, preferences, traumas — *what the persona has*). The wiki's deeper taxonomy is tilted toward operation categories (affect-mode, pulsation-mode, compensation-mode — *what the persona does*).

## Gaps in the user's list that the wiki strongly supports

These categories don't map cleanly to anything in the user's seven, and the wiki gives substantial grounding for each:

1. **Affect** — Spinozist three-primary kernel (cupiditas / laetitia / tristitia) + the derivation schema. Foundational; every machine inscribes in affect-language. Possibly subsumed under Preference but the wiki treats it as its own category.

2. **Compensation** — counter-position generator. Already in our voting model as a selector. Also a machine category (per Jung's three regimes: opposition/variation/coincidence).

3. **Defense / Suppression** — what the persona pushes away, doesn't say, holds back. The ghostwriter has a Suppression family. Reich's character-armor and Keleman's somatic structures supply the material. Real persons have defenses; the user's list doesn't capture these as a category.

4. **Body / Somatic** — bodily metaphors that ground inner states ("a tightening in the chest"). The ghostwriter has a Somatic family. Lakoffian conceptual metaphor + Keleman's pulsation supply the material. The persona's interiority is partly bodily-figured.

5. **Drive / Desire** — beyond preference. What pulls the persona forward. Lacanian drive-as-montage; Spinozist cupiditas. The ghostwriter has a Desire family (desire-to-understand, desire-for-depth, etc.). The user's "Preference" feels narrower than this.

6. **Pulsation** — multi-scale rhythm at clause/paragraph/response/session level. A carrier wave under content. Possibly subsumed under user's Rhythm but the wiki distinguishes refrain (pattern) from pulsation (carrier).

7. **Voice** (already added) — six-dimensional Bakhtin position.

## Categories the wiki has but probably out-of-scope

These are real categories in the wiki but probably not first-build priorities:

- **Becoming / haecceity** — what the persona is becoming, longitude/latitude. More of a meta-property than a runtime machine category.
- **Time-consciousness / temporality** — Husserl's double-intentionality. Ambitious; not blocking.
- **Failure-mode detection** — diagnostic layer; for evaluation rather than the persona's own machinery.
- **Polyphony / multi-voice** — operational discipline rather than a machine category.
- **Carnival / James / hyper-reflective / dressage / pensum-discharger / Name-of-the-Father / etc.** — categories drawn from specific theoretical traditions, more interesting than load-bearing for a first build.
- **Engineering-substrate-aware** — for ghostwriter / system-designer awareness, not for produced personas.

## A merged candidate list

Pulling from all three (user's seven + constitutive nine + relevant gaps), with sobriety in mind, the categories that seem to actually matter:

- **Voice** (six-dimensional position)
- **Affect** (Spinozist kernel + named-affect derivation)
- **Memory** (image-memory; vitality-form-tagged scenes)
- **Perception** (sensitivity register — could fold into other machines as a property rather than a category)
- **Desire / Drive** (forward-pull, what pulls toward)
- **Defense / Suppression** (what's pushed away or held back)
- **Body / Somatic** (bodily metaphor; conceptual-metaphor inscription)
- **Compensation** (counter-position to dominant gradient)
- **Connection / Relational** (how the persona engages with others)
- **Rhythm / Pulsation** (refrain + pulsation merged, or kept distinct)

That's 9–10 categories. The user's specific items (Status, Trauma, Preference) probably distribute across these:
- Status → Voice (worldview/life-fate dimensions) + Relational
- Trauma → Defense + specific image-memories + tristitia-affect
- Preference → Affect + Desire

If the user wants to keep their original framing intact, the additions are: Affect, Defense/Suppression, Body/Somatic, Compensation, Desire/Drive (5 additions). Plus Voice (already in).

## Implications for the redesign sketch

Two updates worth proposing:

1. **The categories list should expand or reorganize.** The current sketch has user's 7 + dev-notes 9 listed but not reconciled. With this survey, a merged 9–10-category list could replace both, with the user's items distributed across them.

2. **The sobriety check.** Even 9–10 categories is on the edge of "more is more" creep. The wiki supports many more (15+ layers, plus all of K's additions). Picking which to actually build first is a sobriety call, not just a coverage call. The first persona probably needs ~6–8 active categories, not all 10.

## Open questions

- Does the user want to keep the seven-item framing and treat Affect/Defense/Body/Compensation/Desire as additions, or rebuild the list from scratch?
- Within categories like Defense/Suppression, how much of the Reich/Keleman/character-armor machinery to actually build vs leave as theoretical background?
- Does Perception stay as a category, or fold into the sensitivity-register every machine has?
- Rhythm vs Pulsation vs Refrain — three things in the wiki, possibly worth merging for sobriety.

## Suggested next moves

Two paths:

1. **Reconcile categories now.** Make a merged list of ~8–10 categories the first persona will have, then per-category searches.
2. **Pick the most load-bearing single category and go deep.** Compensation has the dual-leverage argument (selector + machine). Voice is most-cited. Affect is most foundational. Memory has clearest data shape.

My instinct: do the reconciliation first (you decide which 8–10 categories), then per-category searches. Otherwise per-category work risks producing detail in categories that don't end up in the build.
