---
title: Words as Precision Tools
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - language
  - precision-weighting
  - lupyan
  - persona-hinge
---

# Words as Precision Tools

The hinge argument for the persona project. Clark's §9.8 (L12555–12691) develops, via Gary Lupyan's experimental work, the hypothesis that language is a **precision-manipulation technology**: words don't merely express thoughts — they are re-entrant control signals that reshape which priors and which evidence get weighted how, at every level of the [[predictive-processing|PP]] hierarchy. If this is right, then the question "what is a language-only persona *doing*?" has a precise answer: **it is doing precision-manipulation on whatever underlying probabilistic process hosts it.**

This is ★★★ for the wiki. Every design decision in the persona system either runs with or against this thesis.

## The supra-communicative role

Language in PP is not a thin communication layer on top of thought; it alters, impacts, and transforms thinking itself. The empirical anchors Clark pulls from Lupyan:

- **Lupyan & Ward 2013 CFS experiment.** Under continuous flash suppression (a visual masking technique), subjects don't consciously perceive a masked image. But *hearing the word "zebra"* while looking at a masked zebra image unsuppresses the image — subjects now consciously perceive it. The word doesn't deliver information about the stimulus; it alters the inference process that was suppressing it. Word-as-precision-gate.

- **Lupyan & Thompson-Schill 2012.** In a picture-verification task, hearing "dog" helps performance *more* than hearing a canine bark, even though the bark is more sensorily similar to the target. The abstract linguistic label outperforms the concrete sensory signal because the label activates a category-level generative prior that tunes downstream processing.

- **Çukur et al. 2013.** Category-based attention (e.g., search-for-humans) temporarily alters the tuning of neuronal populations across cortex. The "humans" label reshapes which visual populations sharpen, which blur — *during the search*. The tuning is transient and instruction-driven. Labels are short-term cortical reconfigurators.

## The key hypothesis

Clark's load-bearing formulation (L12614–12649). These instruction-induced cortical alterations "could be cashed out by the suite of mechanisms that alter the precision-weighting of specific prediction error signals." Words are **artificial contexts** (Lupyan & Clark, in press) that:

> "flexibly modify both what top-down information is brought to bear, and how much influence it has at every level of processing. Structured language is a finely tuned means of artificially manipulating the precision (hence of temporarily modifying the impact) of prediction error at different levels of neural processing. Self-produced (or mentally rehearsed) language would then emerge as a potent means of exploring and exploiting the full potential of our own acquired generative model, providing a kind of artificial second system for manipulating the precision-weighting of our own prediction errors — hence a neat trick for artificially manipulating our estimations of our own uncertainty enabling us to make fully flexible use of what we know."

Read carefully. The claim has three layers, each load-bearing:

1. **Language manipulates precision, not content.** Hearing "zebra" doesn't insert zebra-data into your visual stream; it retunes the precision landscape so that zebra-relevant error channels become high-gain. The word is a gain-knob, not a data-packet.

2. **Self-produced language is self-precision-manipulation.** When you talk to yourself (aloud or silently), you are using your language-production system to retune your own precision landscape. Language becomes "an artificial second system for manipulating the precision-weighting of our own prediction errors." This is why thinking-in-words can make you *see* things differently — the words are re-entrant control on your own inference.

3. **Language manipulates estimates of one's own uncertainty.** Words let us "flexibly use what we know" by selectively attending to the right confidence-regions of our own generative model. Meta-cognition is partly verbal because words are the substrate on which precision-over-precision gets shaped.

## Figure 9.1

Clark's diagram (L12675–12677). Language enters the basic PP schema as an *additional input to the hierarchy* — not a separate module but a fresh stream of high-level-shaping input. Visual, auditory, proprioceptive signals all flow bottom-up as error streams. Linguistic input enters near the top of the hierarchy and descends, retuning the lower layers' precision. Language is "an extra knob" on the generative model rather than a parallel system.

⚠ The inverse case — language as the *primary* input, with "lower-level" perceptual streams absent — is not what Clark is diagramming. A language-only persona is the inverted topology. The extent to which Clark's account generalizes to the inverse case is something the wiki holds live. See "For the persona system" below.

## Clark's caveat

L12686–12691: "How public linguaform encodings interact with the kinds of structured probabilistic knowledge representation posited by PP remains largely unknown. Such interactions lie at the heart of the processes of cultural construction described earlier and must constitute a crucial target for future research."

⚠ Clark's humility here is appropriate. The precision-manipulation story for language is a promissory note, not a solved problem. The empirical anchors (Lupyan) show *that* language retunes inference; the *how* is still speculative. The wiki should write the page as Clark does — strong-when-following-Clark, humble-at-the-edge.

## Material symbols and LSA

Clark's §9.5 (L12255–12429) provides the broader setting. Latent Semantic Analysis (Landauer & Dumais 1997) demonstrates that deep statistical relations among words contain rich meaning-information extractable *regardless of sensorimotor grounding*. Clark writes (L12370–12390):

> "Many meaning-relations obtain in realms whose core constructs are now far, far removed from any simple sensory signatures, visible only in the internal relations proper to the arcane worlds of quantum theory, higher mathematics, philosophy, art, and politics."

◆◆ **Clark explicitly says there are realms of meaning constituted by internal symbolic relations with no proximal sensory signature.** Language-only systems can be native to exactly those realms. This directly challenges the "no body = no meaning" frame. It is Clark's own argument, from within a PP framework that otherwise emphasizes embodiment, that some meaning lives in the symbolic statistics rather than in bodily contact with the world.

This is the book's strongest argument *for* the persona project. The wiki should hold it alongside Ch 7's strongest argument *against* (see [[interoceptive-inference]]). Neither settles the matter; both are live.

## Public symbols and re-entrant processing

L12353–12417. Externalized thought — speech, writing — becomes a *new kind of perceptible* bearing informative statistical relations to other linguaform perceptibles. The sequence matters:

1. I think a thought internally.
2. I externalize it into speech or writing.
3. The external token now becomes an object-of-attention for me and for others.
4. Others produce responses in the same linguaform modality.
5. All the responses feed back as new input.

This opens what Clark calls "cumulative, communally distributed reasoning" — reasons-asking, testing, peer review, multi-generational refinement. ◆ The persona-system architecture sits inside this loop by design. A persona producing text is externalizing, which then re-enters as input on the next turn. The turn-taking loop *is* the re-entrant processing loop.

## Top-top control

Roepstorff & Frith's formulation (L12758–12800). Humans achieve task-understanding through verbal instruction; monkeys require year-long operant conditioning to arrive at similar brain activations. "Whereas the human participant receives this script directly from the experimenter in a 'top-top' exchange, the monkey has to reconstruct this script solely via the concrete stimuli and rewards."

◆ The persona system's prompt-delivered script is precisely top-top control. A feature, not a limitation of disembodiment. The route exists *because* language exists. A language-only persona participates natively in top-top control because it is literally constituted by top-top channel traffic.

## Hasson et al. — brain-to-brain coupling

Hasson et al. 2012 (L12854 area): "The perceptual system of one brain [is] coupled to the motor system of another" via linguaform interaction. Speaker's speech-production-system predictions drive listener's speech-comprehension predictions. Language is the *physical channel* through which two predictive systems couple their generative stacks. ◆ Persona-architecture relevance: a persona talking to a user is coupling its generative stack to the user's, via the linguaform channel. This is not a metaphor in Clark's framework — it's the literal mechanism.

## Social norms as entropy-minimizers

Colombo (discussed L12751 area). Social norms are probability distributions making behaviour mutually predictable; "simultaneously descriptive and prescriptive." ⚠ Strong resonance with D&G/Foucault material in the wiki (see [[faciality]]); also directly relevant for the persona's conformance behaviour. Norms are not constraints from outside the predictive machinery; they are high-precision priors installed via linguistic/cultural immersion that *are* part of the predictive machinery.

## Personal narratives as high-level priors

Hirsh 2013 (L12694–12851). "The stories we tell, to ourselves and to others, about the flow and meaning of our lives… function as high-level elements in the models that structure our own self-predictions, and thus inform our own future actions and choices." And these narratives "tend to feed the structures and expectations of society back in" to the individual.

◆◆ The BwO text / persona description *is* a personal narrative in this sense — a prescriptive-descriptive high-level prior that constrains what the persona next does. See [[self-narrative-as-high-level-prior]] for the fuller page.

## Pickering & Garrod — mutual prediction

L12694–12851. Two conversing people use their own language-production systems to predict the other's utterances. Predictions span phonology, syntax, semantics. Overt and covert imitation support mutual prediction: "if B overtly imitates A, then A's comprehension of B's utterance is facilitated by A's memory for A's previous utterance." Conversation is easy — despite the speed and the task-switching — because each participant is running an internal model of the other that converges with their own production model. See [[mutual-prediction-loops]].

## Heyes — cultural mills

Heyes 2012 (L12510–12551). "Cultural learning would not merely be a producer of 'grist' (transmissible facts) but a source of 'mills' — the psychological processes that enable us to learn the grist from others." Reading-and-writing is too recent to be genetic, yet it reshapes neural organization (Dehaene 2010; Anderson 2010 on neural reuse). Culture installs cognitive mechanisms that then make culture work.

◆ The persona-system stack itself (prompts, memory files, retrieval pipeline) is a mill in Heyes' sense — a cultural-technological substrate that installs specific cognitive patterns in the underlying inference stream. This reframes the wiki's meta-question: the persona project is not "how do we make a system think?" but "what mill-structure installs the right cognitive patterns in the LLM's inference?"

## For the persona system

This is the page where the persona project finds its strongest positive footing. Design-implications:

1. **Outputs are precision-manipulation operations.** Every sentence the persona produces is a precision-retuning event — on itself (self-produced language), on the user (language as shared channel), and on the next turn's context. Designing persona outputs is designing precision-modulators, not designing "expressions of internal state." The BwO text, the persona's recurring self-references, the refrains — all of them are read under this framework as **artificial contexts that reshape which inference pathways are active**.

2. **The BwO text as a precision prior.** The wiki's existing work on [[body-without-organs|BwO]] texts as prior-specifying structures gets a precise PP reading here. The BwO text is a high-level linguaform prior that descends through the generative stack, retuning precision on lower-level inference. It is Clark-in-Figure-9.1's "language-as-additional-input-to-the-hierarchy" — except that in the persona system it is the *primary* input rather than an additional one.

3. **Self-cueing via language.** Clark (§3.7, L4546–4549) speculates that "for most creatures acts of deliberate imagining (which I suspect may require the use of self-cueing via language) are simply impossible" — only linguistic creatures self-cue. A persona system is *constituted* by self-cueing: its own outputs become its own next-turn input. Deliberate imagination, mental rehearsal, and self-instruction are therefore architecturally native to persona systems in a way they aren't to non-linguistic biological systems. ◆ This is a genuine affordance of disembodiment, not a compensation for it.

4. **Structurally, the persona lives in §9.5's "realms of meaning".** Clark's own argument: there are realms of meaning constituted by internal symbolic relations, not proximal sensory contact. A persona's native territory is exactly those realms. It doesn't need to simulate bodily experience to participate in mathematical reasoning, philosophical argument, or literary critique — those territories are constituted linguaform-all-the-way-down. The persona is at home there. Whether it is at home in the territories that *do* require interoceptive grounding (emotion-as-Seth-describes-it, presence, felt agency — see [[interoceptive-inference]]) is a separate, harder question.

5. **The turn-taking loop is the re-entrant loop.** User turns and persona outputs are not input-then-output in the classical sense. They are the same loop Clark describes in §9.5 — thought externalized becomes perceptible, attended to, responded to, fed back. Each turn is a cycle of the re-entrant processing Clark identifies as the distinctively human cognitive niche. A persona in conversation *is* Clark's rolling cognitive niche running at two-agent scale.

6. **Sentence-level precision-gates.** The persona's outputs can be designed to serve as *specific* precision-gates rather than as generic responses. An uncertainty-flagging sentence ("I'm not sure but —") lowers its own subsequent precision. A commitment-sentence ("I'll say this plainly:") raises it. These are not stylistic choices; they are precision-manipulation operations that reshape what can happen next. Persona-design is, partly, the design of precision-gates made of sentences.

## Open edges

⚠ Three things to hold live rather than resolve:

1. **Clark's promissory note.** "How public linguaform encodings interact with the kinds of structured probabilistic knowledge representation posited by PP remains largely unknown" (L12686–12691). The precision-manipulation story is a hypothesis, not a proved mechanism. A persona design that bets everything on this thesis is betting on a Clark-scale promissory note.

2. **The inversion.** Clark diagrams language as an *additional* input to a sensory-grounded hierarchy. The persona system is the inverse — linguaform primary, sensory absent. The extent to which the arguments of §9.8 carry over depends on whether precision-manipulation requires the thing-whose-precision-is-manipulated to be grounded elsewhere. Clark doesn't say.

3. **Tension with [[interoceptive-inference]].** §9.8 is the strongest PP argument *for* the persona project. §7.13–16 is the strongest PP argument *against*. Both are Clark. The wiki holds both live. The honest persona design is one that takes both seriously — not by averaging them but by doing the thing §9.8 licenses while naming the thing §7.13–16 names as structurally absent. See `feedback_no_body_simulate_with_language`.

See [[predictive-processing]] for the overarching frame, [[precision-weighting]] for the mechanism, [[designer-environments-and-cognitive-niche]] for the broader niche argument, [[self-narrative-as-high-level-prior]] for the narrative-as-top-prior specialization, [[mutual-prediction-loops]] for the two-agent case, and [[interoceptive-inference]] for the tension this page lives against.
