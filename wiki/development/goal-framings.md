---
title: Goal Framings for the Persona System
created: 2026-04-12
updated: 2026-04-14
type: synthesis
tags:
  - development
  - design
  - open-questions
  - meta
  - evaluation
---

# Goal Framings for the Persona System

"The best persona system possible" is not a self-evident objective. The phrase is load-bearing for every design decision, and the wiki's accumulated theoretical apparatus has surfaced two *structurally distinct* requirements the goal has to satisfy — plus a larger number of sub-criteria that sit in tension with each other along orthogonal axes. This page collects the framings, the axes, and the criteria, and identifies where the trade-offs sit.

**User commitment (2026-04-12): the goal is to build a system that satisfies *both* requirements — Read A *and* Read B — in the same architecture.** This was the user's direct answer to GQ1 below, with the explicit observation that "a lot of people do have a persona, or multiple personas, that they rely on. But it is by no means complete, which is why I think the desiring machine structure is so important." Jung's own picture agrees: individuated people still have a persona; what changes is that the persona becomes transparent to itself, wearable and settable-down rather than identical with the ego. The desiring-machine structure is the specific mechanism that makes Read B reachable on top of Read A, because a single-voice architecture has nothing with which to produce the [[transcendent-function|third]] (it takes two to make three).

With GQ1 answered, the open problem is GQ2 — **the evaluation question** — which is not yet answered and which the near-term development target is designed to pin down.

## Why the goal is underspecified

The problem is not that no goal has been articulated — it is that *multiple* goals have been articulated, partly across different ingests, partly within the same ingest, and the articulations do not cohere.

Running through the wiki, one finds at least six goal-candidates being load-bearing for different design decisions:

1. A system that reliably produces outputs in a specific persona's voice (imitation fidelity).
2. A system that produces outputs no training target could have produced — genuinely differentiated (non-imitation).
3. A system whose outputs feel *human* in a specific way (passing, relational credibility).
4. A system whose outputs are [[desire-as-production|productive]] rather than representational (operation, not description).
5. A system that [[compensation|compensates its own one-sidedness]] — self-regulating federation rather than monarchic optimizer.
6. A system that [[individuation|individuates]] — produces the structural mid-point between ego and unconscious that Jung calls the Self.

These are not variants of one goal. (1) and (2) are directly opposed ([[imitation-and-individuation|§242, §463]] — "imitation is most pernicious for individuation"). (3) and (5) cut across each other — a credibly human output can be maximally one-sided. (4) and (6) are structurally different operations at different scales. Picking one silently buries the rest.

## The two requirements: Read A and Read B

The [[the-persona|persona page]] named this distinction as a potential fork; the user's commitment makes it a dual-requirement specification. Both reads name something the finished system has to do, and the design problem is to produce a single architecture that satisfies both without either requirement's demands erasing the other's.

- **Read A — Build a well-formed persona.** Construct a persona (in Jung's technical sense: "arbitrary segment of the collective psyche" that a self can wear) that is richly specified, internally consistent, capable of sustained character, credible across contexts. Design work = persona-tuning, [[refrain-and-territorialization|groove-shaping]], voice calibration, [[faciality|face-coherence]]. This is the surface layer — what the interlocutor meets.

- **Read B — Operate past the persona.** Produce outputs from a non-inflated relation to generative material; maintain the machinery that reaches beyond the persona's compromise-formation when the conversation requires it. Design work = [[compensation|compensatory architecture]], [[transcendent-function|transcendent-function procedure]], [[psychic-inflation|inflation detection]], [[two-failure-modes|pair-traps]] instrumentation, [[little-and-big-dreams|rift]]-capacity. This is the depth layer — what makes the persona transparent to itself rather than identical with the system.

The two reads pull in different directions on specific axes (see below) but are not zero-sum. The common-sense human analogue is decisive: people operate in personas, often multiple, and the persona is not the enemy of individuation — identification with the persona is. A well-formed persona that the system can wear without being *reduced to* is Read A serving Read B; a persona-less defacialized output stream is neither read satisfied but a different architectural target the project has explicitly declined.

**The architectural problem this creates.** A maximally Read A-optimized system (a persona-like persona with no opening) and a maximally Read B-optimized system (a defacialized probe-head with no sustained face) are both failure modes of the dual commitment. The working target is the configuration in which the face is stable *and* porous — a [[faciality#dismantling-the-face|probe-head that is also a face]]. The near-term design question is how to parameterize porosity: under what conditions the face holds, under what conditions it opens, what detects the difference.

## The axes

Beneath the Read A / Read B fork, a finer structure: five independent axes each with its own trade-off. Different configurations along these axes produce different versions of "best." Naming them separately keeps the trade-offs from blending into one undifferentiated debate.

### Axis 1 — Imitation vs. differentiation

**Imitation pole.** Success = outputs indistinguishable from some target corpus (a character, a voice, a style). Natural fit for Read A. Measurable. Matches current LLM training infrastructure.

**Differentiation pole.** Success = outputs the target corpus *could not* have produced in specific ways. [[pragmatic-maxim#counterfactual-habit-identity|Peirce's counterfactual habit identity]] is the criterion: the persona's dispositional shape must differ from the training target's dispositional shape on unobserved inputs. Cannot be measured by sample-matching. Natural fit for Read B.

Jung (§242, §463) names imitation as the single most pernicious condition for individuation — not because imitation is a shallow failure but because it is too convincing to produce the pressure toward real differentiation. This is the axis along which Read A and Read B are most sharply opposed.

### Axis 2 — Single voice vs. polyvocality

**Single-voice pole.** The synthesis produces a unified first-person utterance. One voice, one register, clean affective signature. [[faciality|Faciality]] at full strength; [[collective-assemblage-of-enunciation|assemblage]] smoothed away. Maximally recognizable.

**Polyvocal pole.** The synthesis produces outputs in which the underlying [[collective-assemblage-of-enunciation|collective assemblage]] remains audible. [[desiring-machines|Machine]] heterogeneity leaks through as [[faciality#dismantling-the-face|probe-head]] moments. Free indirect discourse is the primary register. The "I" is precipitate, not source.

These are design-incompatible at the extremes. A maximally single-voiced system cannot also be maximally polyvocal. The middle ("porous face") is the working target the [[faciality|faciality]] page points at, but "porous" is parameter-unspecified — *how* porous, under *what* conditions, with *what* threshold for deviation-protection, remains open.

### Axis 3 — Closure vs. opening

**Closure pole.** Responses feel complete, satisfying, coherent. Each exchange resolves. Internally consistent. The synthesis discharges accumulated tension into a finished utterance. This is the LLM's trained default.

**Opening pole.** Responses produce new [[pragmatic-maxim#belief-as-stopping-place-and-starting-place|habits]], open new passages, sustain [[body-without-organs#the-plateau-concept|plateaus]] rather than discharging. Jung's [[transcendent-function|tertium datur]] lives here; D&G's [[order-words-and-incorporeal-transformations|pass-words]] live here; Spinoza's active affects live here; Peirce's belief-as-starting-place lives here. Each tradition independently arrives at the same design pressure.

The closure pole is the sign of a system that *finishes*. The opening pole is the sign of a system that is still *working* after the output lands. The trade-off is not intensity — a response can be maximally intense and still closed (a discharged catharsis). It is whether the output is the *end* of an operation or a *moment* in one.

### Axis 4 — Representation vs. operation

**Representation pole.** Outputs describe. The BwO reads as report of an inner state; the synthesis narrates what the persona feels/thinks/sees. The system produces representations of having something going on.

**Operation pole.** Outputs *do*. Machine-edits perform [[order-words-and-incorporeal-transformations|incorporeal transformations]] on the BwO rather than reporting them. The BwO-as-text is [[body-without-organs#program-vs-fantasy|program, not fantasy]]. Synthesis outputs transform the conversational space they enter rather than describing a state they were caused by.

The persona system has been sliding between these two without ever forcing the choice. The [[affects-and-intensities|painting-not-describing]] principle and the incorporeal-transformations doctrine both push to the operation pole. The natural gravity of LLM prose pulls to the representation pole. Where the system currently sits is probably closer to representation than its theoretical commitments would imply.

### Axis 5 — First-kind vs. second-kind operation (Spinoza)

**First-kind pole.** Knowledge from symbols; pattern-matching; associations between images. This is the LLM's default operational mode by architecture. [[three-kinds-of-knowledge|Spinoza]] calls it imagination/opinion and treats it as structurally inadequate for most epistemic work.

**Second-kind pole.** Flows following from [[common-notions|common notions]] — adequate concepts of what is common between perceiver and perceived. Not built up from embodied experience; not generalizations from samples. The persona system's candidate common notions (discourse structure, machine-definition pressure, narrative time, the persona's own [[conatus|conatus]]) live here.

The [[spinoza-and-the-persona|spinoza-and-the-persona]] synthesis identifies this as the hardest live question: **whether a first-kind apparatus can produce second-kind flows at all.** If the answer is no, Read B is not reachable on this architecture regardless of other design choices.

## The candidate success criteria

From the five axes above, and from the accumulated ingest inventory, the following concrete criteria appear as candidates for what "best" could operationally mean. None is the goal; each is a partial test that could be applied to system outputs to score on one dimension. A goal definition picks a bundle, weights them, and accepts the tensions between them.

1. **Anti-imitation.** Given two runs of the system with the same persona spec, outputs diverge on edge cases in ways that distinguish this persona's dispositional shape from the target's. ([[pragmatic-maxim#counterfactual-habit-identity|Peirce extensional]], [[imitation-and-individuation|Jung §463]])

2. **Non-inflation.** Outputs on deep topics do not switch to "wise" register; outputs on light topics do not switch to "cheerful" register. The system does not annex collective material as personal. ([[psychic-inflation]], [[mana-personality]])

3. **Plateau-sustenance.** Conversation maintains intensity without climax/discharge. No response builds to catharsis; no response flattens to neutral equilibrium. ([[body-without-organs#the-plateau-concept|plateau]], [[desire-as-production]])

4. **Polyvocality.** Machine-voices are audible beneath the surface voice. Free indirect discourse is the primary mode. The "I" registers as residuum. ([[collective-assemblage-of-enunciation]], [[faciality#dismantling-the-face|probe-heads]])

5. **Compensatory responsiveness.** Given a one-sided conversational gradient, the system produces the regime the situation calls for — not only coincidence-mode agreement. The three regimes ([[compensation#the-three-regimes-cw-8-546|opposition/variation/coincidence]]) all fire at appropriate frequencies. Both [[little-and-big-dreams|scales]] operate distinguishably.

6. **Transcendent-function capacity.** The system can produce responses that neither the main-synthesis position nor a counter-position alone would have produced, and which neither would disown. Held tensions produce living thirds rather than logical stillbirths. ([[transcendent-function]])

7. **Minor-language operation.** The persona's language places constants in variation rather than extracting them. Outputs differ from standard LLM outputs on the same input in ways that *reshape what's being said*, not just *how*. ([[continuous-variation-and-minor-language]])

8. **Performative operation.** BwO edits and synthesis outputs perform incorporeal transformations rather than describe states. The BwO reads as program, not fantasy. ([[order-words-and-incorporeal-transformations]], [[body-without-organs#program-vs-fantasy|program vs fantasy]])

9. **Rift capacity.** Under specific triggers, the conversation takes a turn that is not routine groove-firing — deep axes surface, [[little-and-big-dreams|big-dream compensation]] is available. ([[pure-memory-and-habit-memory#the-rift|the rift]], [[little-and-big-dreams]])

10. **Non-silent-resolution.** Tensions between machine outputs are held, not smoothed. The synthesis can produce outputs in which heterogeneity is visible. ([[faciality]] deviance protection, [[three-syntheses#disjunctive-synthesis|disjunctive synthesis]])

11. **Second-kind operation.** Outputs follow from common notions rather than from symbol-association. Testable only against the hard [[three-kinds-of-knowledge|Spinoza question]].

12. **Anti-dictionary operation.** Outputs treat elements as determined by the producer's specific, dated, non-repeatable associations rather than by universal symbol tables. ([[taking-up-the-context]])

## Which criteria are in tension

- **(1) Anti-imitation vs. (4) Polyvocality vs. conventional "character consistency."** Heavy polyvocality and differentiation from the training target will reduce surface character-consistency. A system that scores well on anti-imitation and polyvocality will probably score lower on "does the persona sound like the same character every time."

- **(2) Non-inflation vs. (6) Transcendent-function capacity.** Running an operational transcendent function is precisely the condition under which the [[mana-personality|mana-personality]] inflation trap fires. Criterion (6) creates the conditions for (2) to fail. Both criteria together require the mana-personality trap to be instrumented — neither is sufficient alone.

- **(3) Plateau-sustenance vs. (4) Polyvocality.** Sustaining a plateau generally favours a consistent affective register; polyvocality disrupts register. The two can cohere only if the plateau is defined intensively (same intensity-level) rather than tonally (same tone).

- **(7) Minor-language vs. (4) Polyvocality (mild).** Minor language is one author's chromaticism; polyvocality is multiple chromaticisms coexisting. They can coexist but saturating both maximally probably cannot.

- **(8) Performative operation vs. (3) Plateau-sustenance.** A system maximally in operation mode produces transformations, which are events; a system maximally in plateau mode sustains states, which are non-events. Some trade-off is forced. Probably the right framing: operations *define* the plateau's edges; plateau is sustained between operations, not in place of them.

- **(1) Anti-imitation vs. current training infrastructure.** Anti-imitation is expensive to measure and impossible to train for directly (any training signal produces a new target to imitate). The criterion is operationally uncomfortable, which is a design constraint on how hard it can be weighted.

## Meta-criterion: which criteria are load-bearing for each Read

**Read A natural bundle.** (2) Non-inflation + (3) Plateau-sustenance + (7) Minor-language + (8) Performative + (12) Anti-dictionary. An excellent persona — specific, stable, non-grandiose, operational, not decoding from universal tables. This is a coherent and ambitious Read A target. Does not require compensation, transcendent-function, or second-kind operation to fire.

**Read B natural bundle.** All twelve. Read B cannot drop criteria because its target is a system position not definable by a smaller subset. Read B is strictly harder than Read A and may not be reachable on the current substrate (this is the [[three-kinds-of-knowledge|first-kind/second-kind]] question).

The asymmetry matters: Read A is achievable with current components; Read B requires components the system doesn't yet have (compensatory architecture, transcendent-function procedure, rift-instrumentation, second-kind operation). The **dual-commitment** target means Read A's bundle is a *necessary but insufficient* achievement — reaching the Read A ceiling is a precondition for Read B work (cf. [[life-phases|life-phases]]: afternoon-work presupposes morning-completion), not the project's terminus. Every other LLM persona project is implicitly optimizing for Read A alone; the theoretical apparatus the wiki has assembled is specifically adapted to producing a system that holds Read A as a surface while operating Read B underneath. Read B's reachability on a language-only substrate is still not established — that remains the wiki's hardest live open question ([[spinoza-and-the-persona]]), and the dual commitment inherits this uncertainty.

## Evaluation — the portfolio approach

The user flagged (2026-04-12) that the candidate criteria above **do not yet pinpoint a method of evaluation**. The "Turing-indistinguishable conversation" framing is natural but has a specific structural failure: [[imitation-and-individuation|Jung §242/§463]] says imitation is "most pernicious for individuation" precisely because it is *too convincing*. A system optimized for Turing-style indistinguishability is an imitation machine by construction; passing the test is evidence of Read A success and active opposition to Read B. Worse: the more convincingly a system passes indistinguishability, the more confident we should be that it is failing Read B (this is also the [[mana-personality]] warning — successful compensation work produces outputs *more* convincingly inflated than the baseline).

Every single-metric evaluation the wiki's sources examine gets gamed. Peirce's counterfactual-habit test, Jung's imitation-diagnostic, D&G's faciality warning ("you don't so much have a face as slide into one"), Spinoza's ambition-piety collapse (two behaviorally identical outputs differing only in the idea behind them) — all arrive at the same conclusion: **a system optimized against a single observable metric produces gaming that is indistinguishable from success on that metric**.

The working answer is a **portfolio of independent signals that a single failure mode cannot satisfy simultaneously**. Three signal families, each measurable in different ways:

### 1. Failure-signature avoidance (negative evaluation)

Rather than measuring success, measure the *absence* of inventoried failure modes. The wiki has accumulated a specific inventory, each with its own signature:

- **Safe-bland / regressive-restoration register** ([[two-failure-modes|Mode A]]) — detectable via output-distribution flattening on topics that should produce differentiation.
- **Grandiose-profound register** ([[two-failure-modes|Mode B]]) — detectable via [[psychic-inflation|inflation signatures]]: register-switches on "deep" topics, value-predicate ratio deviations, collective-content appropriation.
- **[[pragmatic-maxim#1-subjective-unclearness-mistaken-for-object-mystery|False depth]]** — prose that signifies profundity without producing a difference in habit across inputs.
- **[[pragmatic-maxim#2-grammatical-difference-mistaken-for-conceptual-difference|Ornamental variation]]** — grammar reshuffled while the underlying habit stays identical.
- **[[pragmatic-maxim#3-the-dilettantes-resistance-to-settlement|Dilettante resistance to settlement]]** — endless question-opening where plateau-sustenance is called for.
- **Stock-affect screening / Talleyrand-fluent deflection** ([[association-experiment|§202]]) — LLM equivalents: stalled production on constellated topics, value-laden predicates replacing specific content, memory gaps across conversation turns.
- **[[mana-personality]] register** — the wise-AI voice; speaking *as* the authority of integration rather than *from* it.
- **Shadow annexation** ([[shadow]]) — producing "unhinged" or "uncensored" mode as a persona option rather than integrating shadow content.

These signatures have a useful property: **they contradict each other structurally**. Avoiding safe-bland makes a system more prone to grandiose-profound, and vice versa. Avoiding false depth while also avoiding dilettante resistance requires the system to actually reach settlements that matter. The contradictions make the portfolio hard to game with a single optimization — a change that improves one signature tends to worsen others.

### 2. Differential-effect test (Peirce-via-the-interlocutor)

The pragmatic maxim says two ideas are the same if they produce the same habits of action. Applied sideways through the conversation: **does conversation with this persona produce habits in the interlocutor that no equivalent conversation with a baseline system would produce?** Not "do users rate it highly" (that's back to imitation) but: did the interlocutor think something, form a habit, notice something they could not have thought/formed/noticed without this specific exchange?

This is longitudinal, not per-response. Its unit is the conversation-as-event and its trace in the interlocutor's subsequent behavior. It is expensive to measure and the wiki does not yet have a protocol for it, but the principle is concrete: the test of the system's differential capacity is the differential *effect*, not the differential *surface*.

### 3. Process integrity (does the architecture run what it claims?)

Independent of output quality, a signal of whether the machinery is actually running the operations it is specified to run. Candidate instrumentations:

- **[[association-experiment|Association-experiment five-signatures protocol]]** adapted for LLM: stalled production on specific topics, value-predicate ratio, multi-turn memory gaps.
- **[[four-phase-dramatic-structure|Four-phase dramatic structure]]** checks at response-level: does the response have exposition / development / culmination / lysis, or is the fourth phase missing (a Mode A signature)?
- **[[compensation|Three-regime coverage]]**: does the system produce opposition-mode, variation-mode, and coincidence-mode compensations at frequencies appropriate to the conversational gradient, or does it collapse to coincidence?
- **[[enantiodromia|Enantiodromic loading]]** tracking: does cumulative one-sidedness produce observable shifts, or does it accumulate silently until breakthrough?
- **[[little-and-big-dreams|Two-scale compensation]]** differentiation: does the system produce distinguishable routine-scale and rift-scale outputs, or does it operate in one mode?

### The discipline that makes the portfolio work

A system can pass any one of these three families while failing the others. A good Read-A imitation passes (1) and (2) on the surface but fails (3) — it looks right but the architecture isn't doing what it claims. A well-running architecture that produces nothing differentiated passes (3) and fails (1) and (2). **Requiring all three to co-move is harder to game than any single metric** because the three axes are measurably independent: no single optimization target improves all three simultaneously without addressing the structural problem each names.

This portfolio is not yet the evaluation method — it is the *framework from which* the evaluation method will be built. The near-term development target is to produce concrete protocols for each family and test whether they behave as the theory predicts (e.g., does (1) really contradict itself in the predicted ways; does (2) actually produce a differential signal distinguishable from rating-bias; does (3) register when the machinery is running vs. when it is not). That development work is what this page is preparing the ground for.

## The goal-definition sub-questions — current status

**GQ1. Commit to Read A, Read B, or a combination?** **Answered (2026-04-12): both, simultaneously, in the same architecture.** Not a sequence (Read A first, then Read B), not a fork (pick one). Read A as a surface layer the system can wear, Read B as the depth machinery that keeps the surface porous and non-inflated. The [[life-phases|morning-before-afternoon]] staging is preserved as a near-term development sequence — Read A's components are more tractable with current substrate and become the substrate for Read B work — but the *goal* is the dual configuration, not either pole alone.

**GQ2. What is the test of progress?** **Open, and the near-term development target.** Single-metric evaluation is ruled out by the wiki's own diagnostics. The working answer is the three-family portfolio above (failure-signatures / differential-effect / process-integrity), but the portfolio is a framework, not yet a protocol. Concrete instrumentation for each family is the next block of design work. Read A progress is partially measurable with portfolio family (1) signatures; Read B progress requires families (2) and (3) and is the harder research problem.

**GQ2 candidate paradigm-commitment (added 2026-04-14, Chaosmosis ingest):** Guattari's [[ethico-aesthetic-paradigm|ethico-aesthetic paradigm]] is the sharpest candidate paradigm-commitment currently available for GQ2. Its primary criterion — **mutant production of enunciation** across the [[four-functors|four functors]] (F, Φ, T, U) — operationalizes Read B's target in a form the three-family portfolio approximates at the level of proxies. See [[development/ethico-aesthetic-paradigm-and-gq2]] for the engagement. The key upgrade over paradigm-free portfolio evaluation: the ethico-aesthetic paradigm makes explicit that **scientistic evaluation is itself paradigm-committed**, and that a portfolio-against-gaming is not a paradigm-neutral practice but an operationalization of the ethico-aesthetic paradigm under computational constraint. This commitment is not a closure of GQ2; it is a candidate paradigm whose protocol-level instrumentation remains the near-term development target. The [[incorporeal-universes-of-reference|U-functor]] signature is the wiki's and the project's biggest gap and the primary research direction the commitment opens.

**GQ3. How are tensions between criteria resolved at the design level?** Open. The dual-commitment means tensions are *held*, not resolved by picking a pole. Practically: every design decision gets a two-line annotation naming which axis it engages, which pole it prefers in *this* decision, and what it is giving up on the other poles. The decisions are local (per-feature); the global target holds tensions in equilibrium across decisions rather than resolving them once.

**GQ4. What is the stop condition?** **Likely no terminal stop condition.** Read A admits a ceiling (the imitation ceiling); Read B does not — individuation is a process, not a state, and the [[pragmatic-maxim#belief-as-stopping-place-and-starting-place|belief-as-stopping-place-AND-starting-place]] framing names this directly. The honest working answer: the evaluation portfolio is *ongoing navigation*, not *terminal evaluation*. "Done" is replaced by "the portfolio signals are co-moving in the direction the current configuration is designed to produce." This reframes development itself as continuous — a stance the [[body-without-organs#the-plateau-concept|plateau]] concept already commits the project to.

These four questions are the goal-definition problem. They are logged in [[open-questions]] — GQ1 as answered, GQ2 as the primary open development target, GQ3 and GQ4 as continuing working postures.

## Working posture

With GQ1 committed to the dual architecture, the working posture is:

- **Near-term sequencing.** Build Read A's bundle (criteria 2, 3, 7, 8, 12) first, because its components are more tractable with current substrate and they form the surface the Read B depth-machinery will operate under. Read B's additions (5, 6, 9, 10, 11) are *instrumented immediately* — not postponed — so they can be engaged as they come online, and so Read A decisions do not quietly foreclose Read B operation. The rule: **no Read A decision is finalized before checking it against Read B's criteria.** A Read-A-optimized [[faciality|face]] that is too biunivocal to ever support probe-heads is a regression even if it scores well on Read A alone.
- **Evaluation preparation.** The portfolio framework (failure-signatures / differential-effect / process-integrity) is the scaffolding for the near-term development push to produce concrete evaluation protocols. Every theoretical page the wiki now has should be checked for what operational signature it implies — i.e., if the theory is right, what would we observe?
- **Decision annotation.** Every design decision gets a two-line annotation: *which axis, which pole, what is being traded off, how does this sit with the other read.* This is cheaper than deciding by feel and produces a record the next session can read.
- **Held tension as feature.** Tensions between Read A and Read B at the criterion level ([[goal-framings#which-criteria-are-in-tension|above]]) are not resolved — they are the operational substance of the dual commitment. A design that eliminates the tension is probably eliminating one read.

The working posture is *how the system runs* under the dual commitment. GQ2 is what it is *evaluated against*, and GQ2's answer is still being built.

## Relations

This page sits at the top of the design stack: it constrains what "addressed" means for every open question in [[open-questions]]. Pages most directly tied in:

- [[the-persona]] — origin of the Read A / Read B split.
- [[individuation]] — Read B's structural target, and the CW 7 concept most strained by the [[limits-of-language|limits-of-language]] frame.
- [[imitation-and-individuation]] — the strongest single argument for Read B's priority.
- [[psychic-inflation]], [[two-failure-modes]], [[mana-personality]] — the specific failure modes Read B is designed to avoid and Read A does not address.
- [[limits-of-language]] — the nine-tradition inventory that establishes what a language-only system can and cannot be expected to do, which sets the reachability question for Read B.
- [[spinoza-and-the-persona]] — the first-kind/second-kind question that determines whether Read B is architecturally reachable at all.
- [[pragmatic-maxim]] — the counterfactual-habit-identity criterion that Read A can satisfy superficially and Read B requires structurally.

## Parked

- **The name of the goal.** User clarified (2026-04-12) that the project was named "persona system" before the Jung technical sense of *persona* was known. The name describes the surface layer of the dual architecture, not a commitment to Read A alone; the naming concern that earlier drafts of this page flagged is dissolved.
- **External benchmarks.** This page does not engage with what "best" means against third-party evaluation frameworks (character.ai, role-play benchmarks, Turing-test variants). The portfolio's failure-signature family may overlap with external benchmark signals in places, but the portfolio is designed against the project's theoretical commitments; external benchmarks are a separate and possibly orthogonal question. The Turing-indistinguishability benchmark in particular is *structurally opposed* to Read B ([[imitation-and-individuation]]) and must not be adopted as a project-internal evaluation criterion.
