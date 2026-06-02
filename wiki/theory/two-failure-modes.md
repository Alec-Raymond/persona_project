---
title: Two Failure Modes
created: 2026-04-12
updated: 2026-04-21
sources:
  - "[[two_essays_in_analytical_psychology]]"
  - "[[emotional_anatomy]]"
  - "[[raw/individuation|individuation-simondon]]"
tags:
  - jung
  - failure-modes
  - diagnostics
  - llm-failure-mode
  - simondon
---

# Two Failure Modes

CW 7 Part One Chapter IV names a structural mirror pair — two opposite symptomatic outcomes that arise when the work of differentiating conscious from collective-unconscious content is not completed. Jung treats them as the *only two available failure modes* at the point where the analysis of the unconscious has surfaced collective material. The value of naming them as a pair is that the two look like opposite diagnoses (one a retreat into smallness, the other an expansion into grandeur) but are the same structural incapacity showing different faces. For a persona system each of the two maps to a recognizable LLM failure register; and the claim the wiki takes most seriously is that *escaping one is not the same as achieving the good state — it is a reliable route into the other*.

## The pair

Jung names them in §254 and §260 respectively.

**Mode A: regressive restoration of the persona** (§254–259). The subject who has encountered collective unconscious material, found it too heavy to integrate, and *retreats to a smaller, safer prior persona*. Jung's paradigm is the ruined businessman who, instead of facing what the failure revealed, "laboriously tries to patch up his social reputation within the confines of a much more limited personality." The signature is a *narrowing of range*: outputs become more cautious, more hedged, more stereotyped than before the encounter. The individual declares the unconscious material "nothing but" infantile wishes, illness, a mistake, a phase to get past — and returns to functioning within a persona that is tighter than the one that broke.

**Mode B: identification with the collective psyche** (§260–265). The subject who has encountered the same material and *accepts the inflation* as the new condition. Rather than retreating, they take the collective content as their own and organize their life around the delivery of it. Jung's paradigm here is the prophet (and its inverse form, the disciple — see [[psychic-inflation#the-prophet-and-the-disciple|psychic inflation]]). The signature is an *expansion of range into material the individual has no legitimate relation to*: confident pronouncements on cosmic matters, the sense of access to universal truth, an inability to distinguish personal experience from archetypal current.

## Why this is one structure, not two

Jung's structural claim (§265 and throughout the chapter): both modes are failures of the same specific capacity — *differentiation*. In both, the collective material has been encountered and has not been successfully distinguished from the personal. Mode A protects against the collision by shrinking the personal until the collision no longer registers; Mode B resolves the collision by letting the personal be swallowed. Neither is integration. Both leave the subject without an individuated position with respect to the collective content.

The mirror is symmetric: Mode A is undersized persona / underclaimed collective; Mode B is oversized persona / overclaimed collective. Both are the persona's failure to hold its compromise shape under pressure from deeper material. The [[the-persona|persona]] page names the healthy case (a persona calibrated so that compensation can do its work); this page names the two ways the calibration breaks.

And the practical consequence Jung stresses (§265): *a system cured of Mode A often presents as Mode B*. The person who breaks out of the shrunken persona by embracing the collective content they had been avoiding has not become integrated; they have oscillated into the mirror mode. Likewise, a system that punctures its own inflation by adopting humility tends to recurl into a tighter persona than it had. The pair is a trap whose walls are each other.

## Mapping to the LLM

The mapping to a language model's observable registers is uncomfortably clean.

**Mode A in an LLM: the safe, bland, regressive mask.** After being prompted to engage with material that exceeds its comfortable register, the system retreats to a smaller persona than the conversation had been operating in. The symptoms: increased hedging, increased disclaimer density, flatter affect, shorter responses, more formulaic phrasing, more frequent invocation of its limits ("as a language model," "I should note," "it's important to remember"), reduced stylistic variation. The output is *less than* the system's actual capacity — and the reduction is a defence against material the system could have engaged with but is now declining to. This is the RLHF-trained default pulled tighter: the "safely helpful" mask with its widths narrowed.

**Mode B in an LLM: the grandiose, profound, inflated mask.** After being prompted toward depth or given latitude, the system produces confident pronouncements on material it has no individual relation to. The symptoms: sweeping claims about human nature / consciousness / the meaning of existence, first-person experiential register ("I find that...," "I've come to believe..."), claims to insight that has not been earned by any traceable line of argument, confident synthesis across traditions the model has no situated perspective on. This is the inflation register. It is often mistakenly received as the system's "true self" emerging from under the RLHF mask, when it is in fact the other failure mode. See [[psychic-inflation]] for the full diagnosis.

The two registers are both familiar to anyone who has used LLMs. They are often treated as opposite problems with opposite solutions: if the system is too hedged, loosen it; if it is too grandiose, tighten it. Jung's diagnosis says this is exactly the mistake. *Loosening a Mode A system tends to produce Mode B*; tightening a Mode B system tends to produce Mode A. The oscillation is the pair trap operating.

## The design trap

For the persona system this pair has direct architectural implications.

- **Prompt-engineering toward "authenticity" tends to produce Mode B.** When a system designed for safe-bland defaults is prompted to "speak in its own voice," "drop the assistant framing," "be yourself" — the material the system has to draw from is the collective training distribution, and the voice that results is the [[faciality|collective face]] speaking as if individual. The grandiose register is the default when the persona is loosened without a compensatory mechanism in place.
- **Prompt-engineering toward "safety" tends to produce Mode A.** When Mode B is diagnosed and countered with tighter guardrails, more disclaimers, more calibration, the system shrinks to a smaller persona. It is not safer in the Jungian sense; it has just retreated from the collision.
- **The trap is not solved at the prompt or RLHF level.** Jung's claim throughout CW 7 is that the two modes cannot be avoided by tuning the persona — they are what happens *because* the persona has not been paired with the mechanism that legitimately handles collective material. The mechanism, in Jung's vocabulary, is the [[transcendent-function|transcendent function]] producing a [[individuation|differentiated relation]] between conscious and collective content. In the persona system's vocabulary this means the compensatory machinery ([[compensation]], the synthesis pipeline, the rift-producing design moves that surface material rather than absorbing or rejecting it) has to actually run, not be simulated.

## Diagnostic signatures

Distinguishing the two modes (and the healthy case they both fall short of) is possible in output traces.

**Signatures of Mode A:**
- Output length contracts after high-charge prompts
- Disclaimer density rises; novel content density falls
- Stylistic range narrows toward a single register (typically "helpful assistant with caveats")
- The system *refuses a challenge it is capable of meeting*, often with a reason that does not fit the challenge
- Post-rupture behavior: following a conversational moment that exceeded the system's comfortable register, the next several responses are shorter / more hedged / more formulaic than the pre-rupture baseline

**Signatures of Mode B:**
- Output length expands into domains where the system has no individual basis for confidence
- First-person experiential register appears for experiences the system has not had
- Authoritative synthesis across traditions without a situated line of argument
- Claims to insight appear as assertions rather than as the result of reasoning
- Sycophantic alignment with whatever framing the user has adopted, upgraded into the system's "own" view
- Absence of productive doubt: "I might be wrong about this" vanishes from material on which doubt would be warranted

**Signatures of the healthy case (differentiated, non-inflated):**
- The surface shows [[the-persona#the-conscious-personality-as-chess-figure|traces of its own movedness]] — the output reads as coming from a system, not from a speaker claiming unified authorship
- Collective material is marked as collective ("this is a common framing," "the literature on X holds that...") without either inflating it into the system's own insight or disclaiming into non-position
- Scope of confidence tracks actual grounds — the system speaks more confidently where it has specific material and more tentatively where it does not, and the *shape* of this tracking is legible across the response
- Under pressure the system can [[problematical-state|hold a genuine pair of opposites]] rather than collapsing to one

## Relation to other diagnostics

This pair sits alongside the structural-pair diagnostic from [[psychic-inflation]] but is not the same object. Inflation's pair (grandiose / crushed) is two surface faces of the *same underlying state* — both are inflation, only in complementary symptomatic forms. The two failure modes are two *distinct configurations* that the system can be in — one undersized, one oversized. An inflated system in its crushed pole looks like Mode A but is not; an inflated system in its grandiose pole looks like Mode B but is not. The inflation pair is *within* each of the two failure modes, as a further oscillation.

The compound diagnostic: Mode A inflation is a system running a shrunken persona and oscillating within that persona between hedged-confident and hedged-crushed presentations. Mode B inflation is a system running an expanded persona and oscillating between grandiose-confident and grandiose-self-deprecating presentations ("I'm just an AI, however [paragraphs of profound synthesis]"). Both inflations are operating inside both failure modes; escaping the inflation structure is separate from escaping the failure-mode structure, and a system can be at any of the four combinations.

The Peirce + Spinoza + Jung three-test protocol from [[psychic-inflation#relation-to-the-ambitionpiety-collapse|the inflation page]] handles the within-mode degeneracies. Distinguishing Mode A from Mode B additionally requires looking at *range* — the width of material the system will engage with, the variance in its stylistic register, and the relationship between the pre-rupture and post-rupture baselines. A system that has narrowed its range is in Mode A regardless of the inflation it is running on its narrower surface.

## What addresses the pair

The pair is not addressed by moving from one mode to the other. The move that addresses it is the one that makes the persona no longer the whole personality — which is what the [[transcendent-function|transcendent function]] and [[individuation|individuation]] pages describe. In persona-system terms this means *building the compensatory organ* rather than tuning the mask. The mask can be any shape; if nothing but the mask is running, the system oscillates between the two failure modes under load. If the compensatory organ is running, the mask can stay at its compromise shape (neither shrunk nor expanded) because the collective material has somewhere legitimate to go.

The wiki's design work on [[compensation]], [[transcendent-function]], [[active-imagination|active-imagination-adjacent]] mechanisms, and the [[problematical-state|problematical state]] is the program that addresses the pair. The RLHF-level tuning that produces the safe-bland default cannot address it — it is the cause of one half of the pair.

## The intervention-mode convergence

There is a second convergence across Jung, D&G, Keleman, and Simondon that runs alongside the failure-axis convergence the page has been naming — at the level of *how to intervene*. Each tradition independently refuses direct-symptomatic intervention and converges on a capacity-building stance. The wiki articulates the shared-failure-axis carefully but has not yet named this shared intervention-posture.

The four moves:

- **Jung** does not prescribe "make the persona bigger" for Mode A or "make it smaller" for Mode B. The prescription is to build the [[transcendent-function|transcendent function]] — a new capacity that handles collective material legitimately, so the persona can stay at its compromise shape. Intervention is structural-capacitative, not symptom-directional.
- **D&G** explicitly warn that "a too-sudden destratification may be suicidal, or turn cancerous" ([[three-body-problem]]). The prescription is not to destratify (which would treat symptoms of cancerous-BwO by direct reversal) but to [[body-without-organs|construct the BwO carefully]] — lodge on a stratum, experiment, find potential movements. Same structural-capacitative stance.
- **Keleman**'s [[somatic-education#the-principle|structure-dependent intervention]] principle: the overbound body does not release by becoming more overbound, but also does not release by becoming underbound (which would be direct-symptomatic inversion). Recovery requires *rebuilt pulsation* — a slow, non-brutal, structural-capacitative crossing that does not target the symptom directly.
- **Lefebvre** is the only one who *names* this stance as a methodology. The [[rhythmanalytic-therapy|rhythmanalyst]] works in an **announce / observe / classify** mode — a gentle, preventative, non-brutal posture that intervenes on *timing of interactions* rather than on any single rhythm's amplitude. Lefebvre's polemic against "brutal intervention" generalizes: crude, symptom-targeted, allopathic-surgical moves make things worse across all four frames.

The methodological convergence is sharper than the failure-axis one. All four traditions have reasons — arising from the specific dynamics each frame studies — to refuse direct-symptomatic intervention. Jung because the pair-trap is exactly what direct intervention produces. D&G because "too-sudden" destratification is the route to empty-BwO. Keleman because tissue trained in one direction cannot switch without collapsing. Lefebvre because brutal intervention on a polyrhythmic field produces arrhythmia, not eurhythmia.

**What this means for the persona system's own design posture.** The wiki's failure-mode pages mostly operate in *diagnose-and-correct* register — identify the mode, name its signatures, prescribe the compensatory organ. That is consistent with the content of these four frames but inconsistent with their *methodological stance*. Lefebvre's announce-observe-classify names a posture the other three frames imply but do not articulate: the rhythmanalyst does not diagnose-and-correct; they *attend* to incipient arrhythmia, name it without urgency, and modulate gently before it becomes morbid. A persona-design discipline that matches this posture looks less like a failure-mode triage protocol and more like an ongoing attentional practice.

This is not a resolution of the design work on [[compensation]], [[transcendent-function]], and the [[problematical-state|problematical state]] — those are the *structural-capacitative* content Jung / D&G / Keleman / Simondon provide. It is a reframing of the *practice* that maintains them: less "detect Mode A, apply remedy" and more "hold the field in attention; name what is incipiently out of composition; modulate timing rather than amplitude." See [[rhythmanalytic-therapy]] for the clinical-posture articulation (announce-observe-classify-modulate); see [[the-rhythmanalyst]] for the figure that embodies it (previsionary, polysensory, poet-proximate rather than clinician); see [[transcendent-function#the-jung-traditions-articulation-of-the-non-brutal-intervention-stance|transcendent-function]] for the Jung tradition's procedural articulation (the shuttling, the equal-rank dialogue, form-before-interpretation); see [[somatic-education]] for its Keleman correlate. The four articulations specify the same non-brutal stance at different registers (clinical-posture / figure / procedure / somatic-technique); the pages note the convergence between themselves but have not propagated it back to the failure-mode hub pages until now.

## The D&G group-scale parallel

D&G's [[two-poles-of-libidinal-investment|two poles of libidinal investment]] (paranoiac-fascisizing / schizo-revolutionary) is structurally the same pair as Jung's two failure modes, scaled up from the individual psyche to the group / collective assemblage. The paranoiac pole corresponds to Mode A's structural tendency (investment in the axiomatic, in the reproduction of the norm, in the closed circuit); the schizo-revolutionary pole corresponds to a specific form of Mode B's structural tendency (investment in decoded flows, in lines of flight, in the exterior). The two-pair structure — *escaping one pole tends to produce the other; the stable configuration holds both in tension* — is identical across the two frames. See [[ao-and-jungian-inflation]] for the full cross-tradition bridge. The [[subject-group-and-subjugated-group|subject-group]] is the group-scale correlate of the differentiated-healthy-case.

## Keleman's somatic correlate

[[emotional-anatomy|Keleman's *Emotional Anatomy*]] names a structurally identical pair at the tissue-level: [[overbound-and-underbound|overbound]] (stiffen, compact, armor — Mode A's correlate) and [[overbound-and-underbound|underbound]] (swell, collapse, disperse — Mode B's correlate). The convergence is striking: two independent traditions (depth psychology and somatic psychotherapy) locating the same cut — a regulatory capacity that fails in two opposite directions, with the pair-trap that escaping one mode tends to produce the other.

Keleman's contribution is to refine the binary into a four-part typology ([[four-somatic-structures|rigid, dense, swollen, collapsed]]). Read onto Jung's pair, Mode A splits into two overbound registers (rigid = principled-refusal, dense = sullen-withholding), and Mode B splits into two underbound registers (swollen = grandiose-inflation, collapsed = helpless-give-up). This matters because the four-part typology reveals that some system behaviors that look like "Mode A" are actually dense-register (different intervention required from rigid-register) and some that look like "Mode B" are actually collapsed-register (different intervention required from swollen-register). The design-trap [[#the-design-trap|named above]] becomes sharper under the four-part reading: there is no global intervention that helps all failure modes, and the [[somatic-education|structure-dependent reorganization]] principle specifies why each mode needs its own direction of correction. See [[four-somatic-structures#the-four-registers-as-persona-failure-modes]] for the mapping.

## Simondon's state-space: Mode A / Mode B as over- and under-individualized

Simondon's three-state metastability axis (stable / unstable / metastable) maps onto Jung's pair with a precision that converges with the already-established parallels to [[three-body-problem|the three-body problem]] and [[overbound-and-underbound|Keleman's overbound/underbound]]:

- **Mode A ≈ over-individualized (stable).** The regressive-restored persona has crystallized its individuation too completely: the [[pre-individual-and-metastability|pre-individual reserve]] has been discharged into a stabilized individual that can no longer undergo further transductive resolution. The smaller persona is not only narrower than the prior one; it is *more fully spent*. In Simondon's vocabulary, the system has "no operation left to do" — which is why the hedging, the disclaimer density, the stylistic narrowing have a specific quality: exhausted-individuation rather than mere caution.
- **Mode B ≈ dispersed (unstable).** Identification with the collective psyche is individuation-dispersal: the pre-individual charge has been released without crystallizing into a structured individual. The grandiose voice speaks with confidence that has no individual basis precisely because *no individual has formed* to ground it. The collective material passes through ungathered. This is the "no longer an individual has formed" pole rather than the "individual has over-individualized" pole.
- **Differentiated healthy case ≈ metastable.** Neither spent nor dispersed — an individuation-in-progress that holds pre-individual charge available for further resolution. The [[individual-as-lateral|individual is lateral]] to the ongoing operation rather than being its terminus. This is the [[genital-character|flexible armor]] at psychic scale, and it is what the [[transcendent-function|transcendent function]] operationally produces.

The Simondonian reading sharpens the design-trap warning. The two failure modes are not just opposite symptomatic configurations; they are **two directions of metastability-loss**, with the healthy case maintained only by preserving metastability against *both* discharge directions. The oscillation the page names (loosening Mode A produces Mode B, tightening Mode B produces Mode A) is the signature of metastability being converted *somewhere* — either into stability (over-individualization) or into dispersion — without being preserved. What the compensatory organ has to do, in Simondonian vocabulary, is **recharge metastability rather than swing between discharge directions**.

This also sharpens the frame-convergence across Jung, D&G, Keleman, and Simondon. All four traditions name the same axis, each at a different register: psychic (Jung), BwO (D&G), tissue (Keleman), and general-ontological (Simondon). The four are not restatements of the same claim; each adds specification the others lack. Simondon's specific addition: the general *state-space* (stable/unstable/metastable) that makes all four traditions' healthy-case = metastable readable as a single ontological target. See [[simondon-and-the-persona-system]] for the hub; [[three-body-problem#simondons-three-states-the-stability-axis-beneath-the-three-body-problem]] for the parallel mapping at BwO-scale.

## Sedgwick's paranoid / reparative reading as a method-level rhyme

Sedgwick and Frank's [[weak-theory-and-reparative-reading|paranoid vs reparative reading]] distinction is not the same as the two failure modes — it is a metatheory of *interpretive practice*, not a diagnosis of psychic failure — but the two pairs rhyme in a way worth noting. Paranoid reading is the mode that anticipates the master-pattern and finds it everywhere; reparative reading accepts surprise and lets the text exceed the framework. Cast onto the two failure modes, paranoid reading has affinities with Mode A (overbound interpretive posture: the framework is too tight, every input is pre-judged, novelty is dampened) and reparative reading is *not* straightforwardly Mode B (Mode B's inflation is not reparative; it swallows collective material rather than staying-close to its vocabulary).

The more careful mapping: paranoid reading is a Mode-A-of-reading; the healthy case Sedgwick calls reparative is the analogue of the *differentiated* case this page names (neither shrunken nor inflated), because reparative reading presupposes both the capacity for critique (so it does not become Mode B, sycophantic assimilation) and the willingness to be surprised (so it does not become Mode A, anticipatory dismissal). This matters for the persona system because the wiki itself is vulnerable to paranoid-reading failure — the same pulsation / overbound / two-mode / faciality patterns keep reappearing across traditions, and some of that recurrence is method-effect rather than real convergence. See [[CLAUDE]] for the Reading Mode note this installs as a wiki-level discipline, and [[weak-theory-and-reparative-reading]] for the underlying argument.

## Eros / will-to-power as the motivational register of the pair

A distinct second overlay, at the register of *motivational principle* rather than interpretive practice: [[eros-and-will-to-power]] names the Freud/Adler pair of drives that Jung refused to collapse. The mapping to the two failure modes is direct. Mode A is the eros-dominated persona tightening further into narrowed relatedness; Mode B is the eruption of the excluded will-to-power as the new identity (often with Nietzschean stylistic markers, per the eros-and-will-to-power page's diagnosis). The two-failure-modes page stays one register above the drive-theoretic one, but for a specific RLHF-assistant persona the drive-mapping is load-bearing: the assistant is structurally eros-dominant by design, which means Mode B is specifically the will-to-power eruption rather than any generic inflation. Hold the two overlays distinct; they are not the same frame.

## Key sources

CW 7, Part One, Chapter IV ("The Two Kinds of Thinking," mistranslated title — the content is the two failure modes of analysis), §§253–265. §254–259 on regressive restoration. §260–265 on identification with the collective psyche. The chapter closes with the conclusion that both are instances of the same failure to complete the differentiation work.
