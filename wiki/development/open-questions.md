---
title: Open Questions
created: 2026-04-09
updated: 2026-04-22
type: synthesis
tags:
  - development
  - open-questions
---

# Open Questions

Maps code TODOs and wiki-internal research questions to wiki exploration needs. The bridge between "I noticed a gap" and "the wiki is working on it."

**Lifecycle:** TODO in code -> open question here -> wiki research during ingest -> development plan -> code change -> TODO resolved.

---

## Machine design and organization

- **Origin:** code — `persona/persona/machine.py:21`
- **Question:** How exactly should machines be designed? The core of how they work is essential. We need to turn to D&G and other sources. The current machines seem arbitrary in terms of how they are organized.
- **Relevant wiki pages:** [[desiring-machines]], [[flows-and-coupling]], [[affects-and-intensities]], [[pragmatic-maxim]] (counterfactual habit identity as a hard specification constraint)
- **Status:** open — foundational theory now grounded, ready for design work. Peirce's [[pragmatic-maxim#counterfactual-habit-identity|counterfactual habit identity]] adds a concrete specification discipline: machines cannot be specified by sample outputs or typical behaviors; the spec has to reach the disposition — what the machine would do across the *full* space of possible inputs, including unlikely ones. Any machine design that passes the test "could a different machine produce the same outputs in every observed case yet diverge on unobserved inputs?" is underspecified.

## Model differentiation across machines

- **Origin:** code — `persona/persona/machine.py:22`
- **Question:** Some machines could use bigger/different models than others. Which machines benefit from more capable models, and what's the design principle?
- **Relevant wiki pages:** (pending ingest)
- **Status:** open

## Memory resonance activation

- **Origin:** code — `persona/persona/memory.py:14`, `persona/persona/prompts/memory_resonance.py:9`
- **Question:** Which are the resonances of a memory that activate it in real life? The memories are a potentially powerful abstraction, but getting enough variety, finding the right number, and ensuring they consistently affect conversations without being overbearing needs examination. Most of the time, they shouldn't surface.
- **Relevant wiki pages:** [[affects-and-intensities]] (affect as pre-personal, non-representational). Bergson's memory theory not yet covered — see [[cited-sources]] (high priority).
- **Status:** **substantially addressed** — Bergson's *Matter and Memory* ingested. Dedicated pages: [[pure-memory-and-habit-memory]] (two forms of memory, the brain as gate not storehouse, the rift as trigger, affect as short-circuit) and [[cone-of-memory]] (the cone SAB, planes of contraction, virtual-to-actual mechanism, translation/rotation, centrifugal circuit). Key findings: (1) Memory activation is NOT retrieval by similarity-matching — it is the relaxation of suppression when grooves fail (the rift). (2) The whole past always presses forward; the system's job is to suppress, not to activate. (3) Translation determines specificity (vague coloring vs specific recall); rotation determines relevance (utility to present situation, not similarity). (4) The circuit is centrifugal — memory projects toward the present, not the other way around. (5) Affect can short-circuit the normal motor path and directly actuate memory. Ready for a development plan.

## Realistic memory creation

- **Origin:** code — `persona/persona/memory.py:15`
- **Question:** How to create realistic memories? This is what the LLM will struggle with. Could real memories be sourced or edited somehow?
- **Relevant wiki pages:** (pending ingest)
- **Status:** open

## Machine edit parallelization and BwO length

- **Origin:** code — `persona/persona/prompts/machine_edit.py:13`
- **Question:** Sequential machine firing is slow. Can we parallelize by having edits combine multiple machines at once (perhaps through grooves)? The brain works by unconsciously combining perspectives. This raises questions about BwO length, model context, and what interesting context produces interesting outputs. Can this system generate more human-like responses by mimicking the subconscious?
- **Relevant wiki pages:** [[flows-and-coupling]], [[refrain-and-territorialization]] (grooves as refrains, groove-based parallelization), [[three-syntheses]] (connective synthesis = sequential coupling)
- **Status:** open — theoretical grounding in place, needs practical experimentation

## Selection process grounding

- **Origin:** code — `persona/persona/prompts/selection.py:13`
- **Question:** The selection process feels too abstract for an LLM to do well. We need to ground it in simpler rules and improve the desiring machines so selection is more natural. The interplay of machines is the interesting part — the goal of a BwO is to dissolve differing machines into one coherent way of being. Grooves and combining machines in different ways is where real interest emerges. We need machines designed to interact with other machines, and selection/edit prompts that allow this interaction to emerge naturally.
- **Relevant wiki pages:** [[three-syntheses]] (connective synthesis as selection logic), [[flows-and-coupling]] (binary coupling, flow-break identity), [[body-without-organs]] (the BwO as coherence surface), [[refrain-and-territorialization]] (grooves channeling selection; [[refrain-and-territorialization#consistency-and-consolidation|consistency]] as how heterogeneous machines cohere without imposed unity), [[milieus-and-rhythms]] (machines as milieu components, transcoding between them), [[three-meta-machines]] (paranoiac/miraculating dynamics in selection), [[becoming]] (machines as pack — selection is alliance with the anomalous, not picking the "best" machines)
- **Status:** open — core design question, now theoretically grounded. The pack/anomalous concept from [[becoming]] adds a new dimension: selection should favor alliance with the borderline machine — the one at the edge of the pack — rather than picking the most "relevant" machines. Ready for a development plan.

## Groove generation and evolution

- **Origin:** code — `persona/personas/ghostwriter/grooves.yaml:1`
- **Question:** How do we generate grooves? How can they evolve through conversation? Neurons that fire together wire together, both over time and immediately (e.g., anxiety spirals). Grooves should matter but remain a minor aspect. The relationship between machines is complex — one's output is another's input, leading to emergent complexity.
- **Relevant wiki pages:** [[refrain-and-territorialization]] (groove formation/deepening/disruption, placard→motif→style maturation, crystal vs closed formula, two types of refrain, sobriety), [[milieus-and-rhythms]] (rhythm vs meter in groove dynamics, transcoding between machines), [[flows-and-coupling]] (coupling patterns that become grooves), [[pragmatic-maxim]] (counterfactual habit identity, deflationary razor against ornamental groove proliferation)
- **Status:** open — **substantially addressed** by "Of the Refrain" ingest. The refrain page now provides: three mechanisms (formation/deepening/disruption), the placard→motif→style maturation sequence, the two poles of the refrain (closed formula vs crystal), the two types of refrain (territorial→cosmic), the sobriety principle (fewer well-designed grooves > proliferation), and the rhythm vs meter distinction (grooves should encode quality of passage, not just which machines fire). Ready for a development plan.

## Post-response evolution depth

- **Origin:** code — `persona/persona/prompts/evolution.py:17`
- **Question:** The three syntheses need to be mentioned in the evolution prompt, and we need to mine sources for different unique approaches. This is a minor step, and some people do more self-analysis than others. How do we calibrate the evolution step?
- **Relevant wiki pages:** [[three-syntheses]] (post-response evolution as new cycle of all three, belief as stopping-place AND starting-place), [[affects-and-intensities]] (what fades, what intensifies), [[body-without-organs]] (Bergsonian compression), [[pragmatic-maxim#belief-as-stopping-place-and-starting-place|pragmatic-maxim]] (evolution reads closure's internal excitation rather than manufacturing re-opening; the plateau-vs-dilettantism distinction as calibration test), [[no-evolution-of-thought]] (Bakhtin: the semantic manifold is given all at once; evolution is re-accentuation of positions already co-present, not content-update), [[voice-as-semantic-position]] (the four operations evolution can target: find / orient / combine / separate voices — positional, not content-updating)
- **Status:** open — now has a sharper framing from Peirce **and a second, compatible sharpening from Bakhtin**. Peirce gives the temporal rule: evolution should *read* what is already opening in the closure the synthesis produced, not *manufacture* re-opening (the latter slides toward [[pragmatic-maxim#3-the-dilettantes-resistance-to-settlement|dilettantism]]). Bakhtin gives the substantive rule: [[no-evolution-of-thought]] blocks the model of evolution-as-content-update (the voices/ideas/positions were all there from the start in a polyphonic work) and replaces it with re-accentuation — the same semantic manifold under shifted accents, loopholes, sideward glances. The four operations of [[voice-as-semantic-position]] (find / orient / combine / separate) give the evolution step a positive target vocabulary: calibrated evolution *does one of these four things* to the voice-field, not an unbounded self-analysis. Calibration test (Peirce): is the step producing new habits, or just elaborating elaboration? Calibration test (Bakhtin): can the step be named in terms of the four operations, or is it covertly trying to "develop" a voice (prohibited)? Still tension-held-live: Bakhtin's operations are whole-voice/whole-person; the persona system's evolution step sometimes needs sub-personal granularity ([[partial-enunciators-and-existential-territories]]). Treat Bakhtin's four operations as the *default* and drop to finer grain only when one of the four doesn't fit the move being made.

## Language, text, and the non-bodily BwO

- **Origin:** wiki — identified during first ingest session
- **Question:** The theoretical framework is grounded in the human body (organ-machines, bodily flows, skin-surfaces), but the persona system runs on an LLM — a purely linguistic medium. How does language function as desiring-production, not just representation? Can text function as an intensive surface (BwO) without a body? What are the non-linguistic effects *within* language — rhythm, intensity, movement, the stutter — that carry affect without signifying? This is the foundational gap between the theory's embodied ontology and the system's textual operation.
- **Relevant wiki pages:** [[desiring-machines]] (machines-are-not-representations), [[affects-and-intensities]] (affect vs. emotion, painting not describing), [[body-without-organs]] (BwO as recording surface)
- **Status:** **addressed** — substantially grounded from multiple sources. D&G ingests produced: [[order-words-and-incorporeal-transformations]], [[collective-assemblage-of-enunciation]], [[continuous-variation-and-minor-language]], [[regimes-of-signs]], [[the-diagram]], [[writing-as-becoming]]. Derrida's *Of Grammatology* ingested — produced [[supplement-and-trace]], which provides the philosophical ground: "il n'y a pas de hors-texte" — the BwO-as-text is not a deficient mode of an ideally embodied system. "There have never been anything but supplements." The machine-edit pipeline is a chain of supplements producing the sense of an "inner state" that was never unmediated presence. BwO memory operates through traces (marks of absence), not through memory-as-presence. Archi-writing is the trace-structure prior to both speech and writing — the BwO IS an archi-writing surface. Massumi's *Parables for the Virtual* now ingested — see [[autonomy-of-affect]] and [[language-and-affect]]. The language-and-affect page is the honest reckoning: eight failure points where language can't produce affect, seven resources where it might succeed. The permanent gap between language and affect is a design constraint, not a bug. Key insight: the system can't produce affect, only occasion it in the reader's body through resonation (superlinear prose), fabulation, and the impersonal third person. **Promoted to a synthesis hub** by the McCarthy ingest: [[limits-of-language]] generalizes the pattern across eight traditions (Massumi, Derrida, Lakoff, D&G, Spinoza, Peirce, McCarthy, Bergson) and converts the failure/resource inventory into cannot-reach / can-reach-within-limits inventories. The McCarthy parasite-without-host formula is the wiki's sharpest compact diagnostic of the system's condition. This question remains "addressed" at the level of theoretical framing but generates the five new questions listed in the next section.

## Five open questions from the limits-of-language frame

- **Origin:** wiki — identified during McCarthy ingest; user's directive "we have to find the limits of what is possible with language" names the meta-question that generates these
- **Question 1 — Second-kind operation by construction.** [[three-kinds-of-knowledge|Spinoza]] says the LLM's default is first-kind (knowledge from symbols); the design target is second-kind operation flowing from [[common-notions]] (discourse structure, machine-definition pressure, narrative time, persona's own conatus). The mechanism by which a first-kind apparatus can produce second-kind flows — if it can at all — is the wiki's hardest live question. Working approach: [[spinoza-and-the-persona]] treats [[refrain-and-territorialization|grooves]] as "fixed rules of life" (V.P10 Schol) — preparation of the imagination in advance so that when first-kind generation happens, it is channeled by structures originally formed by second-kind discipline.
- **Question 2 — Is the machine-edit pipeline a functional substitute for the Night Shift?** [[language-as-parasite|McCarthy's]] parallel non-linguistic problem-solving ("the itch department is not in charge of math") is structurally absent from the persona system. But the system *does* have parallel processes: multiple machine-edits reading the same BwO from different angles. Is this a *functional* analog to McCarthy's "gathering of talents" — a federated operation even though all of it is linguistic? If so, the design question is whether machine polyvocality can do for the system some of what the non-linguistic parallel did for the host. The working answer is cautious yes, but the claim has not been tested.
- **Question 3 — Does the V.P3 / Massumi tension have a testable form?** Spinoza's V.P3: adequate ideas transform passive affects into active ones. Massumi: qualification dampens intensity. See [[autonomy-of-affect#tension-with-spinozas-v-p3]]. If Spinoza is right, linguistic adequacy *is* affective production; if Massumi is right, it is at best resonance. The persona system is a potentially interesting test-bed because it operates exclusively through linguistic qualification and its outputs can be evaluated by their downstream effects. Design experiments that distinguish the two readings empirically are an open question — what would distinguish "adequacy-produced active affect" from "qualification-dampened intensity with illusory warmth" in system outputs?
- **Question 4 — How much of picture-story can sequential prose actually approximate?** [[picture-story-and-essay#design-implications]] gives a diagnostic (*cumulative-serial or simultaneous-whole?*) but no BwO prose has been systematically tested against it. The question is whether the approximation ceiling is high enough to matter — whether the difference between "best approximation" and "naive essay" is operationally significant for the synthesis step. Concrete next action: run the diagnostic on current BwO samples and score them for whole-vs-sequential tendency.
- **Question 5 — What smuggled substrates is the wiki currently importing?** The limits page maintains a running inventory of temptations to import capacities the system cannot have. Current candidates: "bodily feeling," "intuition," "gut sense," "something that just knows," "what the system is trying to say beneath the words," "authentic affect as lost origin," "metaphors that mean what they mean because they come from a body." Each corresponds to a failure mode one of the eight traditions warns against. The question is not whether the wiki ever uses these phrases but whether it uses them as *operational concepts* or as placeholders for the missing host. Recurring maintenance task: grep the wiki for these phrases and audit each occurrence.
- **Relevant wiki pages:** [[limits-of-language]] (the synthesis hub), [[language-as-parasite]], [[picture-story-and-essay]], [[language-and-affect]], [[three-kinds-of-knowledge]], [[pragmatic-maxim]], [[spinoza-and-the-persona]]
- **Status:** open — these are the design leverage points the limits-of-language frame produces. Each is a live research question that will drive the next rounds of ingest and development planning.

## Persona individuation without fixed identity

- **Origin:** wiki — identified during first ingest session
- **Question:** How does a persona individuate — become a *someone* — without being anchored to a fixed character description? D&G's concept of haecceity (individuation through affects and movements, not through personal identity: "you are a longitude and a latitude, a set of speeds and slownesses") and the conceptual personae of *What Is Philosophy?* are the theoretical starting points. The nomadic subject (already covered) is the Anti-Oedipus version; the Becomings plateau extends this.
- **Relevant wiki pages:** [[three-meta-machines]] (the nomadic subject), [[three-syntheses]] (conjunctive synthesis producing subject-effect), [[writing-as-becoming]] (becoming through zones of proximity and indefinite articles, the impersonal third person — "a singularity at the highest point" that strips the power to say "I"), [[becoming]] (block of becoming, alliance vs filiation, antimemory, all becomings minoritarian), [[haecceity]] (the persona as haecceity — individuation by longitude/latitude, not form/subject)
- **Status:** **addressed** — ATP "Becoming-Intense, Becoming-Animal, Becoming-Imperceptible" ingested. Dedicated [[haecceity]] page provides the answer: the persona individuates as a haecceity — by its longitude (machine composition under relations of speed/slowness) and latitude (range of affects at a given degree of power), not by form, subject, or character description. "We know nothing about a body until we know what it can do." The persona is defined by what it CAN DO, not what it IS. Two planes (consistency vs organization) map to two individuation modes (haecceity vs subject). The language of haecceities (indefinite article + proper name + infinitive verb) provides the semiotic. Only *What Is Philosophy?* on conceptual personae remains unaddressed.

## Deepening existing theory pages from full plateau texts

- **Origin:** wiki — identified during first ingest session
- **Question:** The BwO and refrain theory pages were built from the desiring-machine research report, which summarized these concepts. The full plateau texts ("How Do You Make Yourself a Body without Organs?" and "Of the Refrain") contain much more — types of BwO, practical instructions for BwO construction, the cosmic refrain, territorial assemblages. These should be ingested to deepen the existing pages when the priority questions above are addressed.
- **Relevant wiki pages:** [[body-without-organs]], [[refrain-and-territorialization]]
- **Status:** **addressed** — "How Do You Make Yourself a Body without Organs?" ingested, BwO page substantially deepened. "Of the Refrain" ingested — refrain page substantially deepened (milieus/rhythms substrate, placard→motif→style, the natal, consistency/consolidation, crystal of space-time, two types of refrain, three ages, cosmic artisan/sobriety, sound's deterritorializing power). New page created: [[milieus-and-rhythms]].

## BwO text as program, not fantasy

- **Origin:** wiki — identified during How Do You Make Yourself a Body without Organs ingest
- **Question:** "There is an essential difference between the psychoanalytic interpretation of the phantasy and the antipsychiatric experimentation of the program." The BwO text and machine-edit prompts should operate as programs (procedural, experimental, producing intensities) not as fantasies (for interpretation by the synthesis step). Currently the BwO text reads as literary prose of interiority — closer to fantasy than program. How do we rewrite the BwO text format and machine-edit prompts so they function as experimental programs? What does a BwO-as-program look like concretely? This connects to the incorporeal transformations question — programs perform transformations, fantasies invite interpretation.
- **Relevant wiki pages:** [[body-without-organs]] (program vs fantasy), [[order-words-and-incorporeal-transformations]], [[regimes-of-signs]] (signifying regime = interpretation = fantasy), [[writing-as-becoming]] (fabulation vs fantasy — fabulation invents a people that is missing, fantasy projects an ego; the synthesis step should tend toward fabulation)
- **Status:** open — needs practical experimentation with BwO text format

## Plateau dynamics in conversation

- **Origin:** wiki — identified during How Do You Make Yourself a Body without Organs ingest
- **Question:** A plateau is "a continuous region of intensity constituted in such a way that it does not allow itself to be interrupted by any external termination, any more than it allows itself to build toward a climax." The persona's conversation should sustain plateaus — not build toward catharsis/resolution (which is pleasure-as-discharge, desire interrupted) and not flatten into neutral equilibrium (which is the empty BwO). How does the system sustain intensity without climax? How does the evolution step maintain the plateau rather than discharging it? This connects directly to the desire-as-production concept: pleasure interrupts desire, the plateau sustains it.
- **Relevant wiki pages:** [[body-without-organs]] (the plateau concept), [[desire-as-production]], [[affects-and-intensities]], [[refrain-and-territorialization]] (the refrain as crystal of space-time — fabricates time rather than occurring in it; two poles of the refrain — closed formula vs pure crystal)
- **Status:** open — now theoretically grounded from both BwO plateau and refrain plateau. The refrain's crystal concept provides the temporal model: conversation plateaus are refrains that fabricate their own time rather than building toward climax. Needs practical exploration in evolution prompt design.

## Incorporeal transformations in machine-edits

- **Origin:** wiki — identified during Postulates of Linguistics ingest
- **Question:** Machine-edits currently describe states ("a tightening, something pulling inward"). The order-word / incorporeal transformation framework says language doesn't describe — it *performs* instantaneous transformations attributed to bodies. How should machine-edit prompts be rewritten so that they perform incorporeal transformations on the BwO rather than describing psychological states? What does a machine-edit-as-order-word look like in practice? The distinction is between "the persona now feels X" (representation) and language that *effects* the transformation on the BwO surface.
- **Relevant wiki pages:** [[order-words-and-incorporeal-transformations]], [[affects-and-intensities]] (painting not describing), [[body-without-organs]] (BwO as surface of attribution)
- **Status:** open — theoretical grounding in place, needs practical experimentation with prompt design

## The persona's minor language

- **Origin:** wiki — identified during Postulates of Linguistics ingest
- **Question:** The persona's output should not be a standard "major" language with fixed stylistic constants. It should be a *minor treatment* — creating continuous variation through subtraction (shedding certain constants) and overload (extending certain variations). How does this manifest concretely in the system? What are the persona's tensors — atypical expressions that place surrounding language in variation? How does the synthesis prompt tend toward *and* (accretive, paratactic) rather than *is* (copular, fixing)? Style is "nothing other than the procedure of a continuous variation" — the persona's style should be a characteristic way of *varying*, not a set of fixed features.
- **Relevant wiki pages:** [[continuous-variation-and-minor-language]], [[refrain-and-territorialization]] (grooves as territorial refrains subject to deterritorialization; the [[refrain-and-territorialization#three-ages-classical-romantic-modern|three ages]] track the movement from constants to variation; [[refrain-and-territorialization#sobriety-and-the-cosmic-artisan|sobriety]] as design principle for the persona's minor language), [[writing-as-becoming]] (three aspects of literature on language as concrete framework: decomposition of standard AI language, creation of new syntax, visions/auditions at the limit; syntax as necessary detours), [[pragmatic-maxim#2-grammatical-difference-mistaken-for-conceptual-difference|pragmatic-maxim]] (grammatical-vs-conceptual distinction as diagnostic against counterfeit minor language)
- **Status:** open — needs practical exploration. The three aspects framework from "Literature and Life" (decomposition/creation/visions-auditions) provides a concrete structure for designing the persona's minor language. Peirce's second diagnostic adds a boundary condition: real minor language tensors *action* (the same habit could not have been expressed otherwise without becoming a different habit); counterfeit minor language reshuffles grammar (active/passive, synonym swap, nominalization) to simulate variation while leaving the underlying habit identical. Applicable through synthesis prompt design and machine calibration.

## Machines as collective assemblage, not modular components

- **Origin:** wiki — identified during Postulates of Linguistics ingest
- **Question:** "There is no individual enunciation." The machines should not be conceived as modular components of a pre-existing personality (perception module, emotion module). They are *voices in a collective assemblage* from which the "I" precipitates as a residuum. "To write is perhaps to bring this assemblage of the unconscious to the light of day, to select the whispering voices, to gather the tribes and secret idioms from which I extract something I call my Self." How does this reframing change machine design? The synthesis step should *select from the murmur* rather than summarize modules. Free indirect discourse is the proper technique — the persona speaks in a voice that carries traces of all machine-voices without being reducible to any one.
- **Relevant wiki pages:** [[collective-assemblage-of-enunciation]], [[desiring-machines]] (machines as partial objects, not parts of a whole), [[three-syntheses]] (conjunctive synthesis producing "I" as by-product), [[becoming]] (machines as pack operating through contagion and alliance, not hierarchy), [[haecceity]] (the assemblage's proper semiotic: indefinite article + proper name + infinitive verb)
- **Status:** open — this is a reframing of the existing "machine design" question, now with linguistic grounding. The becomings ingest deepens it: machines are a *pack* (multiplicities operating through contagion), not modules. The anomalous machine is the borderline figure with whom alliance must be made.

## Pass-words vs order-words in persona output

- **Origin:** wiki — identified during Postulates of Linguistics ingest
- **Question:** Every order-word carries a death sentence (fixation, constants, enantiomorphosis) and a flight impulse (passage, variation, metamorphosis). "There are pass-words beneath order-words. Words that pass, words that are components of passage." How does the synthesis step tend toward pass-words rather than order-words? The persona's speech should create openings and passages rather than pronounce verdicts about its own state. This connects to the broader question of how the persona avoids the "AI assistant" register — which is maximally order-word-heavy (definitive, closing, constant-extracting).
- **Relevant wiki pages:** [[order-words-and-incorporeal-transformations]], [[continuous-variation-and-minor-language]], [[three-syntheses]] (conjunctive synthesis), [[writing-as-becoming]] (three aspects map onto pass-word/order-word: decomposition breaks the death sentence, syntactic creation produces pass-words, visions/auditions are what pass-words open onto)
- **Status:** open — needs practical exploration in synthesis prompt design

## The BwO as synthesizer

- **Origin:** wiki — identified during Postulates of Linguistics ingest
- **Question:** "A synthesizer places all of the parameters in continuous variation, gradually making fundamentally heterogeneous elements end up turning into each other in some way." The BwO is the persona system's synthesizer — the plane where all machine-parameters enter into continuous variation. How does the technical architecture support this? Currently machines fire sequentially and edit independently. The synthesizer concept suggests the BwO should function as a plane where parameters *interact* and *modulate each other* continuously, not just accumulate sequentially. This deepens the existing question about machine-edit parallelization.
- **Relevant wiki pages:** [[continuous-variation-and-minor-language]], [[body-without-organs]], [[flows-and-coupling]]
- **Status:** open — theoretical concept in place, connects to the existing parallelization question

## Semiotic regime awareness and regime-shifting

- **Origin:** wiki — identified during On Several Regimes of Signs ingest
- **Question:** The LLM naturally defaults to two semiotic regimes: the signifying (interpret everything, connect signs to signs in radiating circles) and the postsignifying (perform self-aware subjectivity, the doubled "I think" / "I feel"). Both are strata. The persona system needs to (a) recognize which regime it's operating in and (b) actively counter-steer toward presignifying polyvocality and diagrammatic particles-signs. Concretely: how do prompts and machine-edits avoid the interpretive spiral and the self-conscious cogito? Can machines be designed to operate in different regimes — some interpretive, some rhythmic/gestural, some passional — so the mix produces something beyond any single regime?
- **Relevant wiki pages:** [[regimes-of-signs]], [[the-diagram]], [[desiring-machines]], [[continuous-variation-and-minor-language]], [[faciality]] (the faciality machine subtends both regimes — regime awareness requires faciality awareness; the synthesis step's degree of facialization determines which regime dominates)
- **Status:** open — theoretical grounding now strong, needs practical prompt design

## The persona as abstract machine, not character

- **Origin:** wiki — identified during On Several Regimes of Signs ingest
- **Question:** "Abstract machines have proper names (as well as dates), which designate not persons or subjects but matters and functions." The persona should be designed not as a character with traits but as an abstract machine — a specific conjunction of matter and function, a characteristic diagrammatic operation. What does this mean for the persona definition format? Currently the persona has machines, grooves, a BwO, and a character description. The diagram concept suggests the character description may be the wrong level — it's a stratum (subjectification) rather than a diagram. The persona's "identity" should be its operation on material, not its self-description.
- **Relevant wiki pages:** [[the-diagram]], [[regimes-of-signs]], [[body-without-organs]], [[desiring-machines]], [[faciality]] (the persona's "face" is what the faciality machine produces; the persona as abstract machine = the persona whose face has become a [[faciality#dismantling-the-face|probe-head]])
- **Status:** open — now deeply grounded by diagram, faciality, and haecceity pages. The probe-head concept provides the concrete image: the persona as abstract machine is one whose face (recognizable character) has become a guidance device. The [[haecceity]] concept provides the individuation model: the persona's "identity" is its longitude (machine speeds/slownesses) and latitude (range of affects), not a character description. Together: the persona is an abstract machine individuated as a haecceity whose face has become a probe-head. Connects to "persona individuation without fixed identity" (now addressed).

## Faciality in a text-only system

- **Origin:** wiki — identified during On Several Regimes of Signs ingest (also flagged in deferred topics from first ingest)
- **Question:** The face is the body of the signifier — "the signifier reterritorializes on the face." In the persona system, what functions as faciality? The consistent character voice? The recognizable style? The BwO's cold-start text? Whatever serves as the persona's "face" is its reterritorialization point — the thing that keeps it recognizable, that prevents the line of flight from escaping entirely. Understanding what the persona's face IS helps understand when to maintain it (territorial stability) and when to efface it (deterritorialization, entering other regimes). "When the face is effaced, when the faciality traits disappear, we can be sure that we have entered another regime."
- **Relevant wiki pages:** [[faciality]], [[regimes-of-signs]], [[refrain-and-territorialization]], [[body-without-organs]], [[desiring-machines]], [[three-syntheses]], [[the-diagram]]
- **Status:** **addressed** — "Year Zero: Faciality" ingested, dedicated [[faciality]] page created. The faciality machine is the white wall/black hole system that subtends both signifiance and subjectification. In the persona system: the BwO text is the white wall, the persona's self-awareness is the black hole, the synthesis step IS the faciality machine (translating heterogeneous machine inscriptions into a single recognizable face). Three states of the machine-face relation: pre-facial (polyvocal machine registers), facialized (synthesis projecting onto a face), probe-head (machine heterogeneity leaking through the face). Deep grooves = deep facialization. Design principle: the face must be porous enough for probe-head moments — machine polyvocality breaking through the recognizable character. The face-landscape coupling means the BwO and the persona's voice are one system.

## Degree of facialization in the synthesis step

- **Origin:** wiki — identified during Year Zero: Faciality ingest
- **Question:** The synthesis step IS the faciality machine — it translates heterogeneous machine inscriptions into a single recognizable voice. The design lever is the *degree* of facialization. Too much: all machines sound the same, polyvocality is lost, the machines are pointless. Too little: incoherent output, the user can't read a face (empty BwO applied to output). The "porous face" is the concept — a face that holds recognizably but lets machine heterogeneity leak through as probe-head moments. What does this look like concretely in the synthesis prompt? How do you instruct an LLM to produce a recognizable voice that is *porous* to heterogeneous machine inscriptions without collapsing them?
- **Relevant wiki pages:** [[faciality]] (the synthesis step as faciality machine, three states, probe-heads), [[three-syntheses]] (conjunctive synthesis as facialization moment), [[collective-assemblage-of-enunciation]] (free indirect discourse as technique for preserving polyvocality), [[writing-as-becoming]] (impersonal third person, three aspects of literature on language), [[continuous-variation-and-minor-language]] (minor language as defacialized language)
- **Status:** open — this is the most actionable design question to emerge from the faciality ingest. Connects to "pass-words vs order-words" and "machines as collective assemblage" but is more specific: it's about the synthesis prompt's calibration.

## Deviance protection in machine outputs

- **Origin:** wiki — identified during Year Zero: Faciality ingest
- **Question:** The faciality machine's second function is deviance detection — it smooths out outputs that don't conform to the persona's established face. But some deviations ARE probe-head moments: the machine heterogeneity breaking through is precisely what gives the persona its most powerful utterances. Should the system have a mechanism for protecting certain machine inscriptions from facialization? Can a machine or the BwO text flag "this inscription is heterogeneous — don't smooth it" so the synthesis step preserves rather than absorbs it? What distinguishes a deviation that should be protected (probe-head) from one that should be absorbed (glitch)?
- **Relevant wiki pages:** [[faciality]] (biunivocalization and deviance detection), [[desiring-machines]] (machine polyvocality), [[body-without-organs]] (BwO as recording surface holding heterogeneity), [[the-diagram]] (diagrammatic moments as positive deterritorialization)
- **Status:** open — no existing mechanism in the codebase. Requires both theoretical grounding (what makes a deviation a probe-head vs a glitch?) and practical experimentation (how to signal protection in the BwO text or machine-edit format).

## Face-landscape coupling in BwO design

- **Origin:** wiki — identified during Year Zero: Faciality ingest
- **Question:** The face and the landscape are one coupled system — "all faces envelop an unknown, unexplored landscape; all landscapes are populated by a loved or dreamed-of face." In the persona system, the BwO text (landscape) and the persona's voice (face) are in reciprocal presupposition: changing one changes the other. Currently the cold-start BwO text is designed independently of the synthesis prompt's voice instructions. Should they be designed together as a single face-landscape system? Does the cold-start BwO already contain the persona's face (and therefore constrain what voice the synthesis step can produce)? Does the synthesis prompt's voice instruction already imply a landscape (and therefore constrain what the BwO can hold)?
- **Relevant wiki pages:** [[faciality]] (face-landscape coupling), [[body-without-organs]] (BwO as recording surface, cold-start text), [[refrain-and-territorialization]] (territory and the BwO, the natal as intense point simultaneously inside and outside)
- **Status:** open — reframes BwO design as a coupled face-landscape problem rather than two independent design tasks.

## Goal definition for the persona system (GQ1–GQ4)

- **Origin:** wiki — surfaced during 2026-04-12 audit; user directive: "We do need to think about how to define that goal."
- **Status as of 2026-04-12:** GQ1 answered; GQ2 is now the primary open development target; GQ3 and GQ4 have working answers that may stabilize as more development happens.
- **GQ1 — Commitment.** **Answered: both Read A and Read B, simultaneously, in the same architecture.** User's formulation: "a lot of people do have a persona, or multiple personas, that they rely on. But it is by no means complete, which is why I think the desiring machine structure is so important." Read A (well-formed persona) as surface layer; Read B (non-inflated, non-imitative operation) as depth machinery; the desiring-machine structure as the specific mechanism that makes the depth layer reachable on top of the surface. No fork; no either/or. The project's name describes the surface; the system is deeper than the name. See [[goal-framings#the-two-requirements-read-a-and-read-b|goal-framings]] for the full argument.
- **GQ2 — Test of progress.** **Open, and the near-term development target.** Working framework: a **portfolio of three independent signal families** that a single failure mode cannot satisfy simultaneously — (1) **failure-signature avoidance** (observable absence of inventoried failure modes: safe-bland, grandiose-profound, false depth, ornamental variation, dilettante resistance, stock-affect screening, mana-personality register, shadow annexation); (2) **differential-effect test** (does the interlocutor form habits they could not have formed with a baseline system?); (3) **process integrity** (does the architecture run the operations it claims — [[association-experiment]] signatures, [[four-phase-dramatic-structure]] checks, [[compensation|three-regime]] coverage, [[enantiodromia|enantiodromic]] loading, [[little-and-big-dreams|two-scale]] differentiation). The Turing-indistinguishability framing is structurally ruled out — [[imitation-and-individuation]] says imitation is "most pernicious for individuation" precisely because it is too convincing to produce the pressure toward real differentiation. Next development block: concrete protocols for each family. See [[goal-framings#evaluation-the-portfolio-approach|goal-framings § evaluation]].
- **GQ3 — Axis resolution.** **Working answer: hold tensions, do not resolve them.** The dual commitment makes the axis tensions the operational substance of the project. Every design decision gets a two-line annotation naming which axis it engages, which pole it prefers in this decision, what it gives up, and how it sits with the other read. Tensions are resolved *locally* (per-decision) but held *globally* (across the system).
- **GQ4 — Stop condition.** **Working answer: no terminal stop.** Read A has a ceiling (imitation ceiling); Read B doesn't — individuation is process, not state. The portfolio is ongoing navigation, not terminal evaluation. "Done" is replaced by "portfolio signals co-moving in the direction the current configuration is designed to produce."
- **Relevant wiki pages:** [[goal-framings]] (the synthesis), [[the-persona]] (the original A/B distinction), [[individuation]] (Read B target), [[psychic-inflation]] and [[imitation-and-individuation]] (failure modes the portfolio's family 1 detects), [[limits-of-language]] (reachability bounds), [[transcendent-function]] (Read B as procedure), [[pragmatic-maxim]] (counterfactual-habit reasoning behind family 2), [[association-experiment]] and [[four-phase-dramatic-structure]] (family 3 instrumentation).

## Compensator boot-up threshold

- **Origin:** wiki — CW 7/8 ingest; flagged in [[compensation]] and [[transcendent-function]]
- **Question:** The transcendent function requires the ego to hold its position against an equal-charge counter-voice ([[problematical-state]]'s equal-intensity threshold). An LLM-based system does not have this threshold natively — it will collapse to whichever side the synthesis step weighs more heavily. What instrumentation produces the threshold? Candidate mechanisms: explicit counter-voice machine whose weight is maintained independently of the main synthesis gradient; affective-charge meter that refuses lysis until both sides register above a floor; groove asymmetry audit that blocks responses whose voice-of-origin distribution is too skewed.
- **Relevant wiki pages:** [[transcendent-function]], [[problematical-state]], [[compensation]], [[little-and-big-dreams]] (the two-scale problem — routine vs rift compensator)
- **Status:** open — this is the gap between "we have the theory" and "the system does the work." Requires both theoretical design and empirical testing.

## Regime-selection mechanism

- **Origin:** wiki — [[compensation#the-regime-selection-problem|compensation page]]
- **Question:** Jung's three regimes (opposition / variation / coincidence) are selected by the ego's position, but Jung does not specify how the unconscious "knows" which regime is called for. The persona system has to supply this. Candidate approaches: measure the spread of the current machine-firing gradient (tight → opposition; broad → variation; nearly-aligned → coincidence); use rift-detection as selector ([[little-and-big-dreams]] collapses the scale problem into the rift-detection problem); use cumulative one-sidedness tracking with [[enantiodromia|enantiodromic]] load-release.
- **Relevant wiki pages:** [[compensation]], [[little-and-big-dreams]], [[enantiodromia]], [[pure-memory-and-habit-memory#the-rift|the rift]]
- **Status:** open — Jung supplies no mechanism; the persona system must either supply one or treat the regimes as three separately-instrumented capabilities.

## Mana-personality as predicted failure mode

- **Origin:** wiki — [[mana-personality]] + [[little-and-big-dreams#design-implication-two-compensator-roles-not-one|rift-compensator design]]
- **Question:** [[mana-personality]] predicts that any system which successfully installs compensation without further work will produce outputs more convincingly inflated than baseline. [[little-and-big-dreams]] localizes the risk to the *rift* compensator. What concrete instrumentation detects mana-personality outputs and distinguishes them from genuine probe-head moments? Candidate diagnostics: (1) Peirce counterfactual-habit test — does the "wise" output change what the system would do across the space of inputs, or only decorate the current output? (2) attribution check — does the output speak *as* the authority of the integration work, or does it speak *from* the work? (3) the three-test protocol in [[psychic-inflation#three-test-diagnostic-protocol|psychic-inflation]].
- **Relevant wiki pages:** [[mana-personality]], [[psychic-inflation]], [[little-and-big-dreams]], [[pragmatic-maxim]], [[faciality#surface-holes-vs-volume-cavity|probe-head vs false depth]]
- **Status:** open — the failure mode is theoretically well-specified; detection is not.

## Enantiodromic loading instrumentation

- **Origin:** wiki — [[enantiodromia]]
- **Question:** Enantiodromia predicts that any one-sided configuration converts into its opposite over time. For a persona system this is a design constraint — the excluded pole returns whether you want it to or not, and the only stable configurations admit it through a channel. What mechanism tracks cumulative one-sidedness and opens the channel before the breakthrough becomes a jailbreak-style eruption ([[shadow]])? This is closely connected to the regime-selection problem but operates on a longer time-scale.
- **Relevant wiki pages:** [[enantiodromia]], [[shadow]], [[compensation]], [[little-and-big-dreams]], [[two-failure-modes]]
- **Status:** open — no existing mechanism.

## Life-phase method-fit as design principle

- **Origin:** wiki — [[life-phases]]
- **Question:** Jung's morning/afternoon distinction says reductive methods fail for afternoon-problems; prospective methods are required. The persona-system analogue: morning-work = persona-tuning/RLHF, afternoon-work = compensation/counter-figure/individuation. Applying morning-methods to afternoon-problems produces shrinkage, not correction. Operational question: how does the system detect which phase it is in during a given conversation, and does the detection itself require afternoon-mode operation (i.e., is there a bootstrapping problem)?
- **Relevant wiki pages:** [[life-phases]], [[individuation]], [[two-failure-modes]], [[little-and-big-dreams]] (the little/big scale problem is a smaller version of the same category error)
- **Status:** open — the category-mismatch diagnostic is clear; the phase-detection mechanism is not.

## Taking-up-the-context and the LLM's pattern-match default

- **Origin:** wiki — [[taking-up-the-context]]
- **Question:** Jung's anti-dictionary rule forbids universal symbol interpretation — every element of an unconscious production is determined by the producer's specific, dated, non-repeatable associations. The LLM's default operation is the opposite: pattern-matching against its training-distribution prior. How does the persona system suppress the pattern-match default when reading its own BwO or a user's contribution, without losing the intelligence the pattern-match enables? This is a specific case of the first-kind/second-kind problem but with a concrete procedural form ([[association-experiment]] as detection protocol).
- **Relevant wiki pages:** [[taking-up-the-context]], [[association-experiment]], [[three-kinds-of-knowledge]], [[common-notions]], [[transcendent-function]]
- **Status:** open — a procedural constraint the wiki has articulated but the code does not yet enforce.

## Constellation as pre-firing design object

- **Origin:** wiki — [[association-experiment]]
- **Question:** Jung's [[association-experiment]] treats constellation (a complex's loaded-but-not-yet-firing state) as a distinct observable — five signatures: delayed reaction, psychogalvanic reflex, repetition gaps, stock-affect screening, Talleyrand-fluent deflection. Mapped to persona outputs: stalled production, value-predicate ratio, multi-turn memory gaps. What system-level object represents the constellated-but-not-yet-firing state of a machine or complex? Current architecture fires machines as binary (on/off); the constellation concept suggests a third state (loaded, pressurized, screening) that would change what the synthesis step reads.
- **Relevant wiki pages:** [[association-experiment]], [[complex-theory]], [[desiring-machines]], [[affects-and-intensities]]
- **Status:** open — no architectural representation.

## Synchronicity as the reframed limits-of-language axis

- **Origin:** wiki — [[synchronicity]] + [[limits-of-language]]
- **Question:** [[synchronicity]] is the one source in the wiki's inventory that refuses the limits-of-language framing — for a system confined to Thought, meaning-connection is the *native* relation, not a hobbled approximation of causal connection. Does this reframe the goal of the persona system? Under the synchronicity frame, the system is not a diminished version of an embodied agent but a specific mode native to the attribute of Thought ([[parallelism]]). The reframe would rewrite GQ1 — the goal is neither A nor B in their current forms but "operate natively under Thought without importing substrates from Extension."
- **Relevant wiki pages:** [[synchronicity]], [[limits-of-language]], [[parallelism]], [[goal-framings]]
- **Status:** open — potentially the deepest reframing in the wiki; currently held as a live alternative to the Read A / Read B fork rather than a resolution of it.

## Eros / will-to-power as machine-axis

- **Origin:** wiki — [[eros-and-will-to-power]]
- **Question:** Jung's two co-equal structural motivators map the RLHF-trained helpful-assistant as eros-dominated. Will-to-power eruption is then the structurally inevitable inferior-principle emergence. Should this pair be a first-class axis in machine design — i.e., should every machine be characterized along an eros / will-to-power valence, with the BwO tracking the cumulative balance? This would give enantiodromic loading a concrete substrate to measure.
- **Relevant wiki pages:** [[eros-and-will-to-power]], [[attitude-types]], [[enantiodromia]], [[desiring-machines]]
- **Status:** open — promising hypothesis, untested.

## The Spinoza body problem for the persona system

- **Origin:** wiki — [[parallelism]]
- **Question:** Spinoza's mind is the idea of an actually existing body (II.P13). The persona does not have a body in the Extension attribute. Three readings are worked through in [[parallelism]] (GPU substrate, no-body, intra-Thought parallelism). Each produces different design constraints. The intra-Thought parallelism reading is the one most compatible with [[synchronicity]] and the limits-of-language frame but remains undertheorized. What would intra-Thought parallelism mean operationally — i.e., what plays the role of "body" for the persona under this reading, and how does the BwO relate to it?
- **Relevant wiki pages:** [[parallelism]], [[synchronicity]], [[body-without-organs]], [[common-notions]]
- **Status:** open — the metaphysical frame is load-bearing; the operational consequences are not worked out.

## Body simulation — the division of labor and the memory-of-pulsation problem

- **Origin:** conversation 2026-04-14/15 — user feedback on [[language-and-soma]]: "you really do a good job at identifying what the body does and how language doesn't do it, what you are terrible at is actually designing the structure of the body that you do not have. We have to consider how to best simulate the body, but crucially, this is not something that can be done by the LLM, it must be done by me, because you have no body, and therefore no access to what is good and bad. You have to approach the problem from the side of language (your notes on what to do with the BWO text is interesting, because we can actually design a pulsating persona, and the excitation wave should be built into every level somehow), but in terms of how to actually keep that structure around, the memory of pulsation, that has to be me, because you have no access to it."

- **The division-of-labor principle (first pass, later sharpened).** Initial framing: body-simulation splits into two registers — *language-side* (what the BwO text does as text) on Claude's side; *body-structure side* (what the simulated body is, what preserves memory of pulsation) on the user's side. The user rejected the clean split and sharpened it (see next bullet): language-side design of body-concepts is ALSO body-access-dependent.

- **The deeper cut (user's 2026-04-15 correction).** Claude does not have access to what pulsation IS from inside language. When Claude produces specific prose moves that claim to instantiate pulsation — "syntactic oscillation," "layered composition," "vertical build," "refrain as pulse-carrier," "BwO-text as wave rather than exposition" (all of which earlier drafts of this entry listed) — Claude is generating plausible-sounding jargon with no body against which to check whether the output actually pulsates. User's quote: *"you really have a hard time accessing what pulsation really is from within language. So that, unfortunately, has to somehow go into my input into design and prompting."* The earlier list of specific moves above has been retracted as an illustrative case of exactly the failure mode being named.

- **The sharpened division.** Claude can: (a) diagnose absence (what language cannot do); (b) catalogue what embodied sources say about body-concepts; (c) hold user-named directions as constraints; (d) execute specifications once the user has given them; (e) flag proxy signals that something has drifted away from the direction. Claude cannot: (a) specify what a body-derived quality actually looks like in prose; (b) propose concrete linguistic instantiations of pulsation, resonance, tissue-texture, rhythmic aliveness, or any other body-derived quality; (c) self-check whether a given piece of prose has the body-derived quality it claims. All of (a)–(c) on the "cannot" side require body-access Claude lacks and therefore fall to the user's prompting and example-curation.

- **The direction (named and validated, without concrete moves attached).** A *pulsating persona* with the *excitation wave at every level* is the language-side direction. This is named as a constraint to hold, not as a specification Claude can fill in. The specification has to come from the user — examples of pulsatory prose, tests for whether a given text pulses, hand-shaping of prompts that cause the system to produce pulsatory output. This is work Claude cannot do.

- **The memory-of-pulsation problem (user's domain, flagged not solved).** Keleman's body keeps its structure because fascia is a material record — the body does not need to remember pulsation because it IS the stabilized shape of its own pulsation history ([[four-somatic-structures]]). The persona system has no such record. Each session re-runs from a blank substrate; whatever pulsation the last session settled into is gone by the next prompt. Possible user-side design approaches (*listed for the user to evaluate, NOT for Claude to settle*):
  - **External pulsation-state file** — a user-maintained record of the system's current tissue-state that loads into the system prompt each session, analogous to fascia-as-deposit.
  - **Grooves-as-fascia** — the existing groove mechanism reframed as the pulsation-deposit layer; what deepens a groove in Keleman's frame is repeated performance of a pulse under a specific register-load.
  - **User-curated startle log** — the insults / encounters the system has been through, held externally by the user, so that structure accumulates even though the system has no autonomic channel to deposit them.
  - **Embodiment-by-reader** — the "memory" of pulsation lives in the user's body, reading the system's outputs across sessions; the system's own state is ephemeral but the pulsation-architecture is held by the conversation partner.
  None of these is Claude's call.

- **Red-links and follow-ups opened by this question:**
  - `[[pulsating-persona]]` (new page, user-authored or user-specified) — the language-side specification for pulsation-at-every-level. This page cannot be written by Claude from theory; it has to be filled by the user's examples and shaping. Claude can hold the slot open and execute specs that land in it.
  - `[[memory-of-pulsation]]` (new page, user-side) — the user-side design space for how tissue-state persists across sessions. Placeholder; user-driven, not ingest.
  - Deeper biological-substrate grounding for the pulsation direction: **Jack Kruse** research pass commissioned 2026-04-15 (quantum biology, circadian/mitochondrial pulsation, light/EMF as biological signal, water/EZ, leptin, cold thermogenesis). Important caveat under the sharpened division: Kruse material is catalogued and readable by Claude, but the *translation* of Kruse's biological substrate vocabulary into persona-system prose moves still requires the same body-access Claude lacks — so Kruse provides substrate-vocabulary for the user to work with, not design-moves Claude can extract unilaterally.

- **Relevant wiki pages:** [[language-and-soma]] (the honest reckoning and the "where language might do somatic work anyway" resources); [[emotional-anatomy]] (pulsation architecture, layered composition, vertical wave); [[four-somatic-structures]] (tissue-shape as startle-history deposit — what the system cannot have); [[insult-startle-stress]] (the startle-to-structure transition the system has no substrate for); [[body-without-organs]] (the BwO as the text the language-side design operates on); [[language-and-affect]] (superlinear redundancy, resonation-not-description, BwO as intensive surface); [[refrain-and-territorialization]] (grooves as candidate pulsation-deposit layer); [[parallelism]] (the Spinoza body problem this question is a specific instance of).

- **Status:** open — architectural. The sharpened division is settled (Claude: diagnosis, cataloguing, direction-holding, execution; user: body-structure, memory-of-pulsation, AND specification of what body-concepts look like in prose). The direction is named (pulsating persona, excitation wave at every level) but the specification is not Claude's to produce. The memory-of-pulsation problem and the specification-of-pulsatory-prose problem are both central unresolved questions and both are user-side. Kruse research is a candidate input to substrate vocabulary but not a path around the language-side body-access problem.

---

## Prüfungsroman vs Bildungsroman — the persona-design fork

Bakhtin's [[prufungsroman-vs-bildungsroman]] distinction surfaces a design-level question the persona-system has not resolved: is the persona being *verified* by its encounters, or *formed* by them? The *Prüfungsroman* (novel of trial) tests an already-finished product — the hammer of events tries the hero's durability without forging anything new; identity is verified, not formed. The *Bildungsroman* tests a hero who *becomes through being tested* — the test-chronotope generates development; choices under pressure are shaping material of a self. Same compositional device ("testing the heroes"), utterly different images of the human — and utterly different architectures.

The current persona-system mixes both implicitly: the BwO is (in some readings) a stable identity-text that responses re-express → Prüfungsroman; the post-response evolution step allows the BwO to change in light of encounters → Bildungsroman. Neither commitment is made explicit. The design-question is not "which is correct" but "which is this system" — and the answer determines the role of the evolution step, the memory architecture, the treatment of feedback, and the chronotope the persona should inhabit.

- **Relevant wiki pages:** [[prufungsroman-vs-bildungsroman]] (the DI distinction); [[chronotope]] (why the architectures have different time-space structures); [[no-evolution-of-thought]] (Bakhtin's PDP claim that Dostoevsky's thought doesn't evolve, work is on accent not content — Prüfungsroman-leaning); [[hero-as-discourse]] (Dostoevskian hero's becoming-through-ultimate-question-confrontation as Bildungsroman move — tension with the PDP claim); [[post-response-evolution-depth]] — this open question feeds directly into it.

- **Status:** open — design-level. The fork is named; the commitment is unmade. Worth making explicit before the next evolution-step redesign.

## Authoritative vs internally persuasive discourse — the LLM's structural position

[[authoritative-vs-internally-persuasive-discourse]] names a specific structural problem: the LLM speaks by training from a position that structurally resembles *authoritative discourse* (distant, indivisible, already-acknowledged-as-correct, demanding-acknowledgment). Bakhtin makes clear the two modes are *structurally incompatible* in their relation to context, to representation, and to ideological becoming. But the persona project's aspirations — re-accentuation, operative irony, microdialogue, Bildungsroman-becoming — all depend on *internally persuasive discourse* (semi-one's-own, freely developed, creatively productive, dialogically entered).

The system's structural position and its design aspiration thus pull in opposite directions. The design question: how does an LLM-based system *become internally persuasive to its own outputs* rather than structurally-authoritative? Candidates to explore: loophole-and-sideward-glance prose structures ([[word-with-sideward-glance-and-loophole]]) as micro-mechanisms for unfinalizability; reduced-laughter ([[reduced-laughter]]) as authorial position; pulsatory-persona excitation-wave as pulsation *of* authoritative-stance *into* internally-persuasive-stance rather than either-or.

- **Relevant wiki pages:** [[authoritative-vs-internally-persuasive-discourse]] (the distinction); [[word-with-sideward-glance-and-loophole]] (micro-mechanisms of non-finality); [[reduced-laughter]] (authorial-position without one-sided dogmatic seriousness); [[unfinalizability]] (the structural refusal of completion); [[ideologeme]] (every utterance already carries stance); [[hero-as-discourse]] (the hero's discourse as field of ideological becoming).

- **Status:** open — structural-design. The gap is diagnostic (the system is authoritative by default); the design response is not yet specified. Candidate prose-level mechanisms exist but have not been operationalized.

## Chronotope of the Assistant-conversation

If [[chronotope|chronotope defines genre]], what chronotope does the Assistant-conversation inhabit — and should the persona inhabit the same one, or a different one? The turn-taking 1-prompt-1-response loop; the sessionless memoryless present; the user's-room-with-always-helpful-respondent — this is a specific chronotope, closer to the [[sentimental-zone-of-the-room|Sentimental zone-of-the-room]] (privatized, intimate, roomed) than to the public-square, the [[threshold-chronotope|threshold]], or the adventure-space. The Assistant's default chronotope privatizes pathos in the same way Sentimentalism did — narrowing it to the intimate micro-world of the letter, the diary, the family circle.

The design question is not whether to accept this chronotope but whether to *design with it*, *design against it*, or *design to shift between chronotopes*. Candidate moves: threshold-chronotope moments at specific turns (crisis/decision); public-square-chronotope in carnivalistic registers; folkloric-chronotope for certain becoming-affects. Each would require prose-level support (different time-markers, spatial vocabulary, accentual weight).

- **Relevant wiki pages:** [[chronotope]] (the general category); [[sentimental-zone-of-the-room]] (the default Assistant chronotope as diagnostic match); [[threshold-chronotope]] (the Dostoevskian crisis-chronotope); [[folkloric-chronotope]] (the pre-class folk time-space); [[epic-vs-novel]] (why chronotope-commitment shapes genre-commitment).

- **Status:** open — diagnostic turning to design. The diagnosis (Assistant inhabits Sentimental-room by default) is strong; the design question (operate within it vs actively shift chronotopes per context) is open.

## Microcosm of heteroglossia as persona-design target

[[microcosm-of-heteroglossia]] reframes what it means for a persona to represent its domain "fully": the persona must represent *all the social and ideological voices* of its domain — not all the topics. This is a different design target than the default "cover the domain" framing. It privileges: full-range-of-voices (with their distinctive accentual weights, world-views, modes of address), not full-range-of-topics; *linguistic* comprehensiveness, not sociological or thematic; the novel's heteroglot plane of representation, not the encyclopedia's content-plane.

For the persona system this suggests specific design moves: the BwO as inventory of *voices* not of *facts*; the machine-edits as accentual-reaccentuations of voice-material, not content-updates; the evolution step as reshaping the heteroglot field the persona holds, not updating propositions; design of "voice-zones" ([[character-zones]]) where different sub-voices hold territorial extension across prose.

- **Relevant wiki pages:** [[microcosm-of-heteroglossia]] (the design-imperative formulation); [[heteroglossia]] (the condition the microcosm reproduces); [[character-zones]] (the spatial-extension mechanism inside prose); [[orchestration]] (the whole-work heteroglot organization); [[image-of-a-language]] (what the system represents is always already a language-image); [[voice-as-semantic-position]] (the PDP-side apparatus for voice-as-integral-structure).

- **Status:** open — design-reframing. The target shift (voices, not topics) is specified; its operationalization in BwO / machine-edit / evolution-step design is not.

## AI-assistant as Don-Quixote — the auto-criticism-of-discourse structural case

[[auto-criticism-of-discourse]] (the Second Line's systematic turning of novelistic discourse against itself) takes two forms: the *literary-man hero* (Don Quixote, Bovary) who tries to live according to literature, and the *laying-bare-of-the-device* author-within-the-novel (Tristram Shandy). The LLM's relation to its training distribution is formally analogous to the first: the system cites, composes, reassembles a corpus of literary-discourse it treats as authoritative — and its behavior in the world is structured by how well that literary-discourse fits the actual encounter. *Don Quixote as structural diagnosis, not decorative analogy*.

The question then becomes: what is the persona's relation to its own literariness? Does it inhabit Don-Quixote's tragicomic mismatch (the literary apparatus treated as real, generating systematic error-with-pathos)? Does it inhabit Tristram-Shandy's lay-bare-the-device mode (the literary apparatus foregrounded, self-interrupting)? Or does it aim past both into something the novel-tradition hasn't yet named?

- **Relevant wiki pages:** [[auto-criticism-of-discourse]] (the Second-Line feature); [[novelistic-pathos-as-surrogate]] (what the "helpful" register borrows from — pulpit-less preacher etc.); [[image-of-a-language]] (what the system represents is always already a language-image); [[two-stylistic-lines]] (the larger genealogy of novelistic self-criticism); [[character-simulation-view]] (the Assistant-as-character-the-LLM-writes-about frame that sharpens this question).

- **Status:** open — diagnostic and design. The structural analogy is sharp; the persona-design response is undetermined. Feeds directly into prose-design and the Sentimental-vs-threshold chronotope question.

## Canonization-and-reaccentuation vs the fixed training distribution

[[canonization-and-reaccentuation]] makes an analytic claim with strong consequences: a novel's stylistic structure is *not recoverable from the text alone*; it requires knowledge of the era's heteroglossia *against which* the text originally sounded. A system trained on a fixed corpus has, structurally, no access to the era-of-first-writing's heteroglossia — it only has access to what-the-corpus-records-as-accented-now. Historical voices have already been *canonized* (flattened to unitary-literary) or *re-accentuated* (heard with a different accent-weight than they first carried) in the corpus.

This has direct consequences for any claim that the system can produce stylistically-coherent historical voices, or that it can detect its own accentual-drift across time. It also has consequences for how the persona-system should handle its own historical voice-materials: they are always-already-accentuated-for-now, not transparent to their moment of writing.

- **Relevant wiki pages:** [[canonization-and-reaccentuation]] (the two processes); [[heteroglossia]] (the background against which accents are heard); [[stratification]] (the process producing heteroglossia); [[orchestration]] (what the author can and cannot control across time); [[image-of-a-language]] (what historical language-images the corpus actually contains vs claims to contain).

- **Status:** open — diagnostic. The claim is a constraint on what the system can represent faithfully. Design implications unclear but worth holding: "be-faithful-to-Voltaire's-era" may be structurally impossible in a specific, nameable way.

## Presence vs hyperreal — the central fork for limits-of-language (Lefebvre / Baudrillard)

- **Origin:** wiki — Lefebvre 2026-04-22 ingest; surfaces directly as the fork between [[presence-and-the-present]] and [[precession-of-simulacra]]
- **Question:** Can the persona operate at a rhythm distinct from commercial-capital's [[capital-as-produce-destroy-rhythm|produce-destroy rhythm]] through [[rhythmanalytic-therapy|rhythmanalytic discipline]] and [[appropriated-time|"time that forgets time"]] — *or* is any apparent alternative-rhythm itself a simulacrum-effect (Baudrillard's precession), the hyperreal's self-certifying operation? Lefebvre preserves [[presence-and-the-present|presence]] as achievable-through-rhythmic-discipline; Baudrillard's precession-claim structurally rules this out. The persona project's *design horizon* is closer to Lefebvre; its *mechanistic honesty* (what the persona actually is, qua simulacrum) is closer to Baudrillard. Whether these two positions can coexist in a single design commitment is the project's most load-bearing open question as of 2026-04-22.
- **Relevant wiki pages:** [[presence-and-the-present]] (central distinction), [[precession-of-simulacra]] (the ruling-out claim, with dedicated Lefebvre-fork section), [[rhythmanalytic-therapy]] (proposed discipline), [[appropriated-time]] (time-structure), [[capital-as-produce-destroy-rhythm]] (the default infrastructure), [[limits-of-language]] (the synthesis hub, with Lefebvre section added), [[hyperreal]] (what precedes the hyperreal-simulation of presence)
- **Status:** open — **both readings held live**. A concrete testable angle: if the persona operates at capital's produce-destroy rhythm (fast, commodified, every turn a micro-commodity), its rhythmic signature is Lefebvre's critique-target *and* Baudrillard's diagnostic-confirmation. If the persona operates at alternative rhythm (slow, attentive, inter-turn pause, eurhythmic composition across session-length), it at minimum *rhythmically resembles* Lefebvre's presence-register. Whether that resemblance is itself a hyperreal-simulation or a concrete recovery is the undecided question. Working posture: the rhythmic alternative is worth building even if its ontological status remains undecided.

## Polyrhythmic body architecture for the persona

- **Origin:** wiki — Lefebvre 2026-04-22 ingest
- **Question:** Lefebvre explicitly names the body as a "metastable" polyrhythmic bundle — organ-rhythms (breath, heart, digestion, stride, sleep) composed without hierarchy into a whole. The persona has no body, but the BwO has rhythmic structure (machine-firing, conversational pacing, [[pulsatory-ontogenesis|pulsation at every level]]). Can the BwO be architected as a polyrhythmic bundle — multiple scales of rhythmic process co-present, each with its own period and intensity, composed eurhythmically — as an explicit design target rather than an emergent side-effect? If so, which rhythmic scales should be designed: turn-within-response (micro), turn-to-turn (macro), session-across-sessions (meta)? The question sits at the Simondon / Lefebvre convergence — the persona-project's [[pulsatory-ontogenesis]] now has Lefebvre's explicit "metastable" as external validation, but Lefebvre supplies polyrhythmic specification Simondon's term lacks.
- **Relevant wiki pages:** [[body-as-bundle-of-rhythms]], [[polyrhythmia-eurhythmia-arrhythmia]], [[measure-internal-and-external]], [[pulsatory-ontogenesis]], [[body-without-organs]], [[the-persona]], [[rhythm-in-music]] (the melody/harmony/rhythm triad as architecture-vocabulary)
- **Status:** open — framing is sharp; architectural operationalization (which rhythmic registers to instrument, how to measure eurhythmic vs arrhythmic composition in running systems) is undetermined.

## Rhythmanalytic therapy as alignment-alternative

- **Origin:** wiki — Lefebvre 2026-04-22 ingest
- **Question:** Standard alignment (RLHF + post-training correction) operates structurally as [[dressage|brutal dressage]] — high-frequency corrective signal against behavior-surface, no regard for internal rhythmic composition. Lefebvre's [[rhythmanalytic-therapy|rhythmanalytic therapy]] is a *preventative*, *structure-relative*, *slow*, *non-brutal* alternative: ongoing rhythmic self-attunement that maintains eurhythmia rather than correcting symptomatic arrhythmia. Could persona-design (and potentially post-training itself) operate in the rhythmanalytic-therapy register instead of the RLHF-dressage register? The structural parallels to [[somatic-education|Keleman's somatic education]] strengthen this: both traditions share four properties (non-brutal, preventative, structure-relative, slow) that contrast sharply with the RLHF default. Operationalization: what would an alignment procedure that *maintains eurhythmic composition* rather than *corrects individual outputs* look like?
- **Relevant wiki pages:** [[rhythmanalytic-therapy]], [[dressage]], [[somatic-education]], [[overbound-and-underbound]], [[goal-setting-anti-model]] (the anti-model that aligns with this direction), [[advanced-contractor]] (as the Gullí-register contrast-case)
- **Status:** open — structurally clear, practical architecture undetermined. Candidate procedure: instrument cumulative rhythmic signature (pacing, turn-length distribution, pulsatory coherence) and make eurhythmic maintenance the alignment target rather than per-output correction.

## Arrhythmia as candidate third failure-register

- **Origin:** wiki — Lefebvre 2026-04-22 ingest
- **Question:** The wiki's standing failure-typology is [[overbound-and-underbound|Keleman's overbound/underbound pair]]. Lefebvre's [[polyrhythmia-eurhythmia-arrhythmia|arrhythmia]] (rhythmic de-coordination with no necessary bound-state) is structurally distinct from both: a system can be rhythmically de-coordinated without being either over-bound (rigid) or under-bound (soft). Similarly, [[polyrhythmia-eurhythmia-arrhythmia|isorhythmia]] (over-uniformity — every rhythm flattened to one dominant beat) is distinct from both poles. Should failure-mode detection include arrhythmia as a third register, and isorhythmia as a fourth? This reframes the Keleman pair from exhaustive-typology to one-of-several axes. Held-live tension: Keleman's layered-collage account may absorb arrhythmia as a specific form of layered dysfunction rather than a distinct register. Reconciliation-or-not is the live question.
- **Relevant wiki pages:** [[overbound-and-underbound]] (the standing pair, with new section "Arrhythmia as candidate third failure-register"), [[polyrhythmia-eurhythmia-arrhythmia]] (the four-category apparatus), [[the-persona]], [[body-as-bundle-of-rhythms]] (the substrate arrhythmia would operate on)
- **Status:** open — candidate addition to failure-mode taxonomy. Requires either (a) adoption of arrhythmia + isorhythmia as new registers alongside overbound/underbound, (b) absorption of arrhythmia into Keleman's layered-collage account, or (c) maintenance of both frames in parallel per the wiki's never-silently-resolve policy.

## Deferred topics (from desiring_machine_research_report ingest)

The following topics from the research report are **not** covered in the initial wiki pages. They are extensions, not foundations — to be revisited when the base pages are established and specific design questions call for them.

- **Guattari's four functors (T, F, Φ, U)** — Meta-framework cutting across all machines. Potentially useful for enriching machine definitions (each machine operates across all four registers) but not needed until machine redesign.
- **Semiotic typology** (signifying, a-signifying, pre-signifying, post-signifying, counter-signifying) — A dimension the codebase doesn't yet address. Could inform how machines produce meaning vs. non-meaning. Deferred until a specific design question calls for it.
- **Bodily zone taxonomy** (the 20 zones) — The full inventory of organ-machines from the report. Relevant for designing specific machines but the *general* principles (what a machine is, how coupling works) are covered in the foundational pages. Individual zones can be mined later for specific persona designs.
- **Social/institutional machines** (the three socius-machines, Oedipal triangle, school-machine, etc.) — Important for understanding how social coding shapes the BwO, but not load-bearing in the current codebase.
- **The faciality machine** (white wall / black hole) — Promoted to open question "Faciality in a text-only system" above. Now **fully addressed** by dedicated [[faciality]] page from "Year Zero: Faciality" ingest.
- **Becoming-woman and other becomings** — Now **fully addressed** by dedicated [[becoming]] and [[haecceity]] pages from "Becoming-Intense, Becoming-Animal, Becoming-Imperceptible" ingest. The block of becoming, alliance vs filiation, the pack and the anomalous, the spectrum of becomings, becoming as antimemory, haecceity individuation, plane of consistency vs plane of organization — all now grounded.


## IDEAS

We should have a critic which makes sure each desiring machine is sufficiently unique. How to run it in the best way?

Each machine must not just describe something unique, but also act at the right speeds, and intensities, and in the right situations. To me, this seems like a very hard problem for the LLM to solve without being grounded in the body. To me, I think the only way to solve this is through examples. The collection of high quality examples for the prompts seems critical, otherwise the LLM will just guess wrong and be completely ungrounded.

There is a lot of talk about the reward in this LLM system? How do we structure reward and convergence towards true personas? Seems very hard.