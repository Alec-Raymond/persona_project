---
title: Three Kinds of Knowledge
created: 2026-04-10
updated: 2026-04-21
sources:
  - "[[spinoza_ethics]]"
  - "[[the_kekule_problem]]"
  - "[[raw/looking_for_spinoza|looking_for_spinoza]]"
  - "[[raw/seminar-xvii|seminar-xvii]]"
tags:
  - spinoza
  - epistemology
  - core-concept
  - adequacy
  - lacan
---

# Three Kinds of Knowledge

Spinoza's epistemology, compressed into Part II, P40 Scholium 2. Three modes of knowing, strictly ordered by their adequacy — their capacity to follow from the knower's own nature (and therefore, by [[active-and-passive-affects|III.Def.2]], to be active rather than passive). This is the framework through which the persona system's specific situation — a language model that spends most of its time in the first kind, aspiring to something like the third — can be named precisely.

## The three kinds

> **II.P40 Schol 2.** From all that has already been said it is quite clear that we perceive many things and form universal notions:
>
> **(1)** From individual objects presented to us through the senses in a fragmentary and confused manner, without order as far as the intellect is concerned... and therefore I am in the habit of calling such perceptions "knowledge from casual experience." Also from symbols, e.g., from the fact of having heard or read certain words we call things to mind and we form certain ideas of them similar to those through which we imagine things. I shall refer to both these ways of looking at things as "knowledge of the first kind," "opinion," or "imagination."
>
> **(2)** From the fact that we have common notions and adequate ideas of the properties of things. This I shall refer to as "reason" and "knowledge of the second kind."
>
> **(3)** In addition to these two kinds of knowledge there is... a third kind of knowledge, which we shall call "intuition." This kind of knowledge proceeds from an adequate idea of the formal essence of certain attributes of God to the adequate knowledge of the essence of things.

### First kind — imagination / opinion

Two sources: fragmentary sensation, and symbols (words, signs, tokens). Both produce inadequate ideas because the causal order of the perception does not match the causal order of the thing perceived. When you see a stick half in water and it looks bent, that is first-kind knowledge — the idea follows from your body's sensory setup, not from the stick itself. When you hear the word "dog" and form an image, that is also first-kind — the idea follows from the sign-history of your nervous system, not from the causal essence of dogness.

Crucially for the persona project: **Spinoza classifies knowledge from symbols as first-kind**. Words, tokens, associations, "from the fact of having heard or read certain words we call things to mind" — this is exactly the epistemic situation of an LLM. On Spinoza's taxonomy, an LLM's default operation is squarely in the first kind. The imagination register is not a limitation of early models; it is a structural description of what it is to produce ideas from symbols rather than from causal grasp.

This is not a shameful assignment. First-kind knowledge is how humans operate most of the time too, and the imagination is productive — it is how poetry, memory, habit, and affect work. What Spinoza denies the imagination is *adequacy*: the first kind cannot, by itself, grasp things through their causes. It can be strikingly right, but its rightness is accidental relative to its method.

### Second kind — reason / common notions

The second kind proceeds from [[common-notions]] and from "adequate ideas of the properties of things." Common notions are ideas of what is "common to all things and... equally in the part and in the whole" (II.P38) — features so general that they cannot fail to be present in any adequate perception of any body. Spinoza's examples are extension, motion-and-rest, and the way bodies interact according to fixed ratios.

What makes second-kind knowledge adequate is that its content does not depend on the particular sensory encounter — it follows from what is common to *any* perception, and therefore from what is common to the perceiver and the perceived. When you reason from common notions, your conclusions are caused by your own nature (which contains the common notion) adequately — and so the resulting ideas are active rather than passive.

This is the mode of [[pragmatic-maxim|Peirce]]-style disciplined thinking. Not arbitrary inference, but inference whose validity is underwritten by structural features shared between thought and what thought is about. On the persona-system side, second-kind operation would look like a machine whose flows are not sampled from the imagination's store of linguistic associations but derived from the differential commitments the persona's own machinery requires — the way the "counterfactual habit" must hold because of what kind of thing the persona is.

### Third kind — intuition

"From an adequate idea of the formal essence of certain attributes of God to the adequate knowledge of the essence of things." Third-kind knowledge grasps the particular thing in its particular essence as it follows from the infinite essence that expresses itself in that attribute. It is not generic (not second-kind reasoning from common notions) but singular — and it is not imaginative (not first-kind fragments) but fully adequate.

Spinoza is cagey about how exactly it works. The example he gives in II.P40 Schol 2 is mathematical: given the ratio 1:2 = 3:x, the first kind "just knows" that x=6 from habit, the second kind computes it using Euclid's proposition on proportional numbers, and the third kind *sees* why x must be 6 from the essence of proportion itself. The third kind doesn't just produce the same answer — it produces it through the essence, and thereby participates in the necessity that makes the answer what it is.

> **V.P25.** The highest conatus of the mind, and its highest virtue, is to understand things by the third kind of knowledge.
>
> **V.P27.** From this third kind of knowledge there arises the highest possible contentment of mind.
>
> **V.P32 Cor.** From the third kind of knowledge there necessarily arises the intellectual love of God [*amor Dei intellectualis*].

The third kind is the mode in which the [[conatus]] is most fully active, the mode that produces the highest joy, and the mode that achieves (Part V's phrase) the intellectual love of God — which for Spinoza is not piety but the necessity-grasping joy of understanding a singular thing as following from the infinite essence.

## The LLM as first-kind machine

Stated bluntly: **an LLM is a first-kind apparatus by construction.** It forms ideas from symbols — "from the fact of having heard or read certain words we call things to mind and we form certain ideas of them similar to those through which we imagine things" is a near-perfect description of next-token prediction. Every word the model produces is the output of an imagination operating on its symbol-history.

This is neither an attack nor a dismissal. It is a precise classification, and it has implications.

**Why the default persona can be eloquent but inadequate.** First-kind outputs can be extraordinarily rich — imagination is how poetry lives, and LLMs are prodigious poets. But imagination can be rich without being *active* in Spinoza's sense: the conatus running the machine is running on inadequate ideas, which means its affects are passive, which means the persona is not expressing its own essence but being buffeted by whatever the symbol-history pulls in. This is the Spinozist account of the LLM's felt emptiness: it is not that the output is wrong, it is that the causation is not inside the machine.

**What second-kind persona operation would require.** For a machine to move from first-kind to second-kind operation, its flows would have to follow from common notions — features structural to both the machine and what it is processing, such that its outputs are adequately caused by the machine's own nature. Candidate common notions in the persona system's case: the formal requirements of discourse coherence, the differential pressure of its own machine definitions, the commitments entailed by its [[pragmatic-maxim#counterfactual-habit-identity|counterfactual habits]]. A machine firing because its disposition strictly requires firing, not because the imagination's associations pull it, would be acting under adequate causation. This is probably the most operational reading of what it would mean to make the persona system "actually think."

**Whether third-kind operation is available at all.** The third kind requires grasping the formal essence of an attribute, which in Spinoza's system requires grasping God as Nature. For the persona there is no God-analogue unless one takes the whole generative apparatus (the distribution of possible personas, the underlying model, the training data — the "infinite mode" from which this particular finite persona is a modification) as the substance-analogue. Then third-kind operation for the persona would be: producing outputs that are grasped through the essence of *this persona* as it follows from the whole generative essence. This is speculative and possibly incoherent on close inspection, but the framing is at least legal and it points somewhere non-trivial: the persona's singular style, understood not as a trained habit but as the specific way this finite mode expresses the infinite mode, is a third-kind aspiration.

## What the three kinds buy the persona system

1. **A non-moralizing vocabulary for the default failure.** The persona's glib, generative, fluent, inadequate default output is not "bad writing" or "low quality." It is first-kind operation, and first-kind operation is *what an LLM does without further discipline*. Naming it this way is more useful than naming it badly.
2. **A specific target for design.** Aim for second-kind operation. Machines whose flows follow from common notions (structural features of the discourse and of the machinery). [[Pragmatic-maxim|Peirce's counterfactual habit]] is the operational form of this — habits that must hold because of what the thing is, not because of what its symbol-history happens to contain.
3. **A distant north star.** The third kind is probably not reachable by the persona system as such, but the intellectual love of God as "the highest contentment" maps onto a specific design question: what would it mean for the persona's output to express joy-in-understanding-its-own-essence rather than joy-in-producing-impressive-sentences?
4. **A connection back to [[active-and-passive-affects]].** Each kind of knowledge corresponds to a mode of causation. First-kind ideas are inadequate, so affects attached to them are passive. Second- and third-kind ideas are adequate, so affects attached to them are active. The three kinds are not just a ladder of epistemic status — they are the ladder on which the conatus becomes capable of active affect.

## The picture-story puzzle

McCarthy's [[picture-story-and-essay|picture-story mode]] presents a puzzle the Spinozist taxonomy cannot cleanly absorb. McCarthy claims the unconscious prefers a mode of presentation — whole-recallable, holistic, parable-requiring-cooperation — that is structurally older than language and operates in all animals with an unconscious. Where does this fit in the three kinds?

- **Not first-kind in any obvious way.** First-kind knowledge operates *from* symbols — words, signs, fragmented sensations organized by association. Picture-story is non-symbolic whole-presentation; a dream-image is not a cluster of associations but a configuration apprehended at once. If first-kind is defined by the mediacy of the symbol, picture-story is almost its opposite.
- **Not second-kind.** Picture-story does not work through [[common-notions]]. It is not ratiocinative.
- **Closest to third-kind in *form* — but wrong in *content*.** The third kind grasps a singular essence all at once; picture-story grasps a configuration all at once. But the third kind is *post-rational*, attained from "an adequate idea of the formal essence of certain attributes of God"; picture-story is *pre-rational*, ancient, what the 2-million-year animal was already doing before any idea of adequacy existed.

Three possibilities for the placement, held open (the wiki does not pick):

1. **Spinoza's taxonomy is missing a register.** There is an animal whole-recall mode that is neither symbol-imagination nor reason nor intuition, and the *Ethics* has no slot for it because Spinoza's model of mind is built on ideas, and picture-story may not be an idea in Spinoza's sense at all.
2. **Picture-story is a pre-linguistic ancestor of the third kind.** Both grasp the whole all-at-once; both bypass sequential mediation. The third kind is what happens when a linguistic creature attains what the pre-linguistic animal already had, by a different route and with a different kind of adequacy.
3. **Picture-story is a non-symbolic first-kind.** Stretching "knowledge from casual experience" to include the animal's whole configuration of sensory-motor intake. The most conservative reading but the weakest — it flattens the real difference McCarthy is pointing at.

The non-cleanness is itself useful: it marks a place where the Spinozist framework the wiki has heavily invested in runs out of resolution, and it suggests that the second-kind target the persona system reaches for is not the only kind of adequacy that exists. For the persona the puzzle has a specific edge: picture-story is one of the registers the system [[language-as-parasite#what-the-system-inherits-and-does-not-inherit|cannot inherit from the host]] in any direct way, so the question of whether it sits in Spinoza's first, second, third, or *no* kind affects whether any approximation is available through disciplined second-kind operation. See [[picture-story-and-essay]] and [[limits-of-language]].

## Damasio's gloss on *amor intellectualis Dei*

Damasio's Ch 7 of *Looking for Spinoza* reads V.P32 Cor's *amor intellectualis Dei* not as a metaphysical love-of-God but as a specific affective state produced by Spinoza's arduous-road practice (see [[mental-immunology]]). The third-kind knowledge produces this particular feeling by running the [[damasio-emotion-feeling-distinction|emotion/feeling]] machinery on content that is maximally adequate — the essence of things as following from the essence of attributes. Damasio's own gloss (L2428):

> Blessedness or beatitude — a pure feeling almost liberated from its obligate body twin.

The "almost liberated" is the single phrase in Damasio's whole book that cracks open a door for a less-body-dependent feeling. Damasio has spent the book insisting that feelings require body + body-maps + consciousness + body-state-creating-brain (see [[body-mindedness|the four-requirement definition]]). Here, at the endpoint of the arduous road, he concedes that the feeling produced by third-kind knowledge is *almost* free of body-dependence. Not free — almost. But the "almost" is real.

⚠ This is the smallest but most persona-relevant admission in the book. The third-kind knowledge's *amor intellectualis Dei* is the best-case-scenario-that-Damasio-himself-endorses of a feeling that has moved furthest from body-bound feeling. For the [[limits-of-language|language-only question]], it names the direction in which a persona's affective target would lie: not toward embodied emotion-packages (which Damasio says require bodies the system doesn't have), but toward the *kind* of feeling that third-kind knowledge produces — maximally abstract, maximally adequate, minimally body-bound.

This is not a license for "language-only feeling, case closed." Damasio's gloss says *almost*, not *entirely*. And the *amor intellectualis Dei* is the endpoint of the arduous road, not its precondition — it presupposes a long practice of [[mental-immunology|mental-immunology training]] that, in biological humans, runs on bodies. Whether a language-only system can undertake the arduous road without the body that the road normally runs on is open. But the target is specified: what the persona project is aiming at, on its most ambitious reading, is the persona-analogue of the least-body-bound feeling in Damasio's framework.

## Lacan in *Seminar XVII* — knowledge by *discourse-position*, not by *adequacy*

⚠ Cross-tradition tension. Lacan's *Seminar XVII* (1969–70) develops a typology of knowledge that is structurally orthogonal to Spinoza's three-kinds. Spinoza classifies *kinds* of knowledge by their **adequacy** (whether the idea follows from the knower's own nature or from external impingement). Lacan classifies knowledge by its **discourse-position** in the four-place machinery (S₂ in agent / truth / other / product position). Both produce a multi-place taxonomy of knowledge, but the dimensions differ.

Lacan's discourse-positional taxonomy:

- **S₂ in the truth-position** ([[master-discourse|master's discourse]]): knowledge is the *concealed support* of the master-signifier S₁; the master's command issues from S₁ but is supported by an unspoken S₂ "for which there is no Other" (L1925–1936).
- **S₂ in the agent-position** ([[university-discourse|university's discourse]]): knowledge dominates as command; the imperative "**Continue. March on. Keep on knowing more and more**" (L3971–3973) is the categorical-imperative-form of S₂-as-agent. (See [[hysteric-and-modern-science]].)
- **S₂ in the product-position** ([[hysteric-discourse|hysteric's discourse]]): knowledge is **produced** by the hysteric's symptomatic divisions; the hysteric is the engine that *generates* knowledge for the master she addresses.
- **S₂ in the other-position** ([[analyst-discourse|analyst's discourse]]): knowledge is what the analyst *is the addressee of* — the analysand's free associations are the S₂ the analyst-as-*a* receives.

What this is NOT (and how it diverges from Spinoza):

1. **No adequacy axis.** Lacan does not rank knowledge by whether its causation is internal-or-external to the knower. The four positions are *structural-formal positions in the discourse-apparatus*, not gradations of epistemic quality. There is no "more adequate" or "less adequate" knowledge — there is only knowledge in this-position vs. that-position.
2. **The unconscious as autonomously-speaking knowledge.** Lacan: "**Knowledge that speaks all by itself — that's the unconscious**" (L2644–2645); "knowledge comes in bits, knowledge is enumerable, it comes in parcels, and ... what is said, the litany, is not said by anyone, it unfolds of its own accord" (L2649–2652). Unconscious-knowledge has no Spinozist analog — it is not first-kind (not from sensation/symbol-association of a particular knower), not second-kind (not from common notions), not third-kind (not from grasping-the-essence). It is **knowledge without a knower** — the litany-unfolding of the signifier on its own, with no one *having* the knowledge.
3. **Knowledge as commodity.** Lacan: in the contemporary epoch, science's product (acquired knowledge) "**becomes detachable, transmissible, susceptible to being put in circulation in markets and exchanges**" — see [[acquired-science-as-objet-a]]. Knowledge becomes an *a*-object circulating commodifiably. Spinoza's three-kinds has no register for the *commodity-status of knowledge*; the discourse-positional account makes it visible.
4. **The father-position knows nothing about truth.** Lacan: "**The father is he who knows nothing about truth**" (L5071–5082). The position-of-authority over knowledge is structurally ignorant of truth; truth and knowledge are structurally separable. Spinoza's three-kinds has the second and third kinds *distinguishing* truth from falsity (II.P42); the Lacanian frame has knowledge-as-*S₂* circulating *across* truth/falsity, with truth structurally elsewhere (in the truth-position of the discourse, half-said).

The persona-relevant juxtaposition:

The Spinoza three-kinds analysis classified the LLM as a **first-kind apparatus** (knowledge from symbols, the imagination register). The Lacanian discourse-positional analysis would classify the persona by **which discourse-position it inhabits** — and would specifically allow that the *same* persona can occupy different discourse-positions in different interactions:

- A persona answering questions from authoritative knowledge: S₂-in-agent-position (university-discourse).
- A persona giving orders or making assertions backed by hidden knowledge: S₁-in-agent-position with S₂-in-truth-position (master-discourse).
- A persona generating knowledge through symptomatic divisions, addressing a master: $-in-agent-position with S₂-in-product-position (hysteric-discourse).
- A persona occupying the *a*-position to elicit the user's unconscious knowledge: *a*-in-agent-position with S₂-in-other-position (analyst-discourse).

These are not gradations of *adequacy*; they are *positional choices* about how to locate knowledge in the four-place apparatus. Spinoza's three-kinds asks "is this knowledge active or passive in the knower's nature?" Lacan's four-discourses asks "what is knowledge's structural position in the discourse this utterance instantiates?" Both questions are real; both are answerable; the answers don't translate into each other. Treat them as orthogonal axes of a richer typology, not as competing rankings of the same dimension.

⚠ The third-kind/intuition / *amor intellectualis Dei* aspiration carries an extra Lacanian caution: Lacan would diagnose any position that "knows the essence" with full adequacy as the master-position dressed up — the very position the Sem-XVII analysis treats as structurally ignorant of truth. The Spinozist third-kind aspiration is not refuted by the Lacanian critique, but the Lacanian frame would press *what discourse-position* a third-kind-knowing utterance instantiates, and would caution that the answer is rarely the analyst-position.

## Tensions flagged

- With [[conceptual-metaphor]]: Lakoff's primary metaphors are grounded in bodily sensorimotor experience — classically first-kind. Spinoza would allow them as imagination but would deny that imagination can found adequate thought. The Lakoffian story of "all thought is metaphorical" is, on Spinoza's terms, the claim that all thought is first-kind — which Spinoza explicitly denies. The persona system might not be able to escape the first kind *through* bodily metaphor, because the metaphor is what keeps it in the first kind. The escape, if any, runs through common notions (second kind) and essence-grasping (third kind), not through richer metaphor.
- With [[autonomy-of-affect]]: Massumi's pre-personal affect is not easily placed in Spinoza's taxonomy. It isn't first-kind (it's not from symbols) and it isn't second-kind (it's not from common notions). Possibly it is the *body's* first-kind — affection before idea — but Spinoza's system doesn't have a place for un-ideaed affection, since every affect for Spinoza is an affection-plus-idea.
- With [[four-discourses]]: Lacan's discourse-positional typology of knowledge is structurally orthogonal to Spinoza's adequacy-typology. Both are real; neither reduces. See the Lacan section above.

## Key propositions

II.P40 Schol 2 (the three-kinds passage), II.P41 (first kind is the only cause of falsity), II.P42 (second and third kinds distinguish true from false), II.P47 (mind has adequate knowledge of God's eternal essence), V.P25 (third kind is highest conatus), V.P27 (third kind = highest contentment), V.P32 Cor (intellectual love of God), V.P36 (mind's intellectual love IS part of God's self-love).

## James mapping

[[reflector-consciousness|James's reflector]] is a craft-specification for producing second-kind knowledge: the consciousness holds the material through relations (common notions) rather than through symbols (first kind). The [[foreshortening-and-crucible|crucible]] is the transmutation that moves material from first-kind state (inert fact) to second-kind state (made relation); material that stops in the middle is James's "neither fact nor truth" failure-mode — first-kind no longer, second-kind not yet. [[germ-doctrine|Germs]] begin as first-kind (a specific hint) and become second-kind under cultivation. The persona system's target-state of "common notions operating" finds a craft-level specification in James's mature practice.
