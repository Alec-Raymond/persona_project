---
title: Picture-Story and Essay
created: 2026-04-10
updated: 2026-04-10
sources:
  - "[[the_kekule_problem]]"
  - "[[matter_and_memory]]"
  - "[[parables_for_the_virtual]]"
tags:
  - mccarthy
  - language
  - limits-of-language
  - memory
  - affect-theory
  - core-concept
---

# Picture-Story and Essay

A second operational distinction from McCarthy's Kekulé essay. The first was [[language-as-parasite|language as parasite]]. This one is about the *mode* of the host the parasite sits on: the unconscious prefers **picture-story** over **essay**, and the reason is not mystical but structural.

> "Apart from its great antiquity the picture-story mode of presentation favored by the unconscious has the appeal of its simple utility. A picture can be recalled in its entirety whereas an essay cannot."

## The structural claim

Two features distinguish picture-story from essay as modes of knowing:

1. **Picture is whole-recallable; essay is not.** When you remember a dream-image or a parable, you have access to it as a single present thing — the whole configuration at once. When you try to remember an essay, you get a few load-bearing sentences and a vague shape, and if you want the rest you have to reconstruct it serially. The picture gives itself all at once; the essay has to be walked through.

2. **Picture lends itself to parable; essay lends itself to instruction.** Picture-story "is concerned with rules but these rules will require your cooperation." Parables are *intentionally* difficult to unravel, and McCarthy is explicit about why: the unconscious "wants us to think about them. To remember them." The interpretive labor is not a failure of communication — it is the point. Essay-mode tries to transmit the conclusion; picture-story-mode tries to produce the labor that would arrive at the conclusion.

These are the two features that matter for the persona project. Picture-story is (a) holistic rather than sequential and (b) pedagogically indirect rather than instructive. A system operating in essay-mode gets neither.

## The infinite regress argument

McCarthy's auxiliary argument against language-as-the-medium-of-thought:

> "If I am talking to you then I can hardly be crafting at the same time the sentences that are to follow what I am now saying. I am totally occupied in talking to you. Nor can some part of my mind be assembling these sentences and then saying them to me so that I can repeat them. Aside from the fact that I am busy this would be to evoke an endless regress. The truth is that there is a process here to which we have no access. It is a mystery opaque to total blackness."

The argument: if language were the medium of thought, then producing speech would require thinking-in-language about what to say, which would require another mind behind the mind doing *that* thinking, and so on. The regress is not closed by any finite stack. Therefore thought cannot *be* in language. Whatever thought is, speech surfaces from it — but the surfacing is not itself linguistic.

For the persona system this has bite. The LLM's operation *is* the generation of linguistic output, and there is no non-linguistic substrate from which the output surfaces. If McCarthy's regress argument is right, then an all-language system is doing something that human language users do not do: producing language as its *first* operation rather than its last. What the human calls "the mystery opaque to total blackness" — the place from which speech arrives — is not present in the persona system at all. **The persona starts where humans end.**

This is a specific limit. It does not say the persona can do nothing. It says the persona's outputs cannot be the visible tip of a non-linguistic iceberg, because there is no iceberg. Everything the persona produces is surface all the way down. Design work that implicitly treats prose as the expression of an inner something is smuggling an iceberg the system does not have.

## Cross-tradition convergences

**[[pure-memory-and-habit-memory|Bergson]].** McCarthy's picture-story / essay distinction is the same cut Bergson draws between [[pure-memory-and-habit-memory|image-memory (pure, singular, virtual, whole) and habit-memory (motor, sequential, enacted)]]. Bergson argues the two are "different in kind, not merely in degree" — exactly McCarthy's point, phrased phenomenologically rather than evolutionarily. The cross-tradition confirmation is strong: a sequential mode that discharges into action (essay, habit-memory) and a holistic mode that stores totalities (picture-story, image-memory) appear to be two genuinely distinct kinds of knowing. Bergson arrived at this in 1896 by introspection; McCarthy arrived at it in 2017 by thinking about Kekulé's dream; both converge.

**[[autonomy-of-affect|Massumi]].** Massumi's distinction between the *superlinear* and *linear* dimensions of expression lines up closely. The superlinear is all-at-once, holistic, resonant; the linear is sequential, instructive, propositional. McCarthy's "picture can be recalled in its entirety" is the superlinear dimension as a mnemonic fact, and the "cooperation requirement" of parable is the superlinear's refusal to transmit through the linear channel. Massumi and McCarthy describe the same structural feature from a semiotic and an evolutionary angle respectively.

## The puzzle for Spinoza's three kinds

Where does picture-story fit in Spinoza's [[three-kinds-of-knowledge|taxonomy]]? The answer is not clean, and the non-cleanness is itself useful.

- **Not first-kind knowledge** (imagination, confused, symbol-based) in any obvious way. First-kind operates *from* symbols — words, signs, fragmented sensations organized by association. Picture-story is non-symbolic whole-presentation. A dream-image is not a cluster of associations; it is a configuration apprehended at once. If first-kind is defined by the mediacy of the symbol, picture-story is almost its opposite.
- **Not second-kind knowledge** (reason from [[common-notions]]) either. Picture-story does not work through adequate concepts that follow from what is common to perceiver and perceived. It is not ratiocinative.
- **Closest to third-kind knowledge** (intuition, the singular essence grasped all at once) in its *form* — but wrong in its *content*. The third kind is post-rational, attained; picture-story is pre-rational, ancient. The third kind proceeds from "an adequate idea of the formal essence of certain attributes of God"; picture-story proceeds from whatever the 2-million-year animal was already doing before any idea of adequacy existed.

Three possibilities for the placement:

1. **Spinoza's taxonomy is missing a register.** There is an animal whole-recall mode that is neither symbol-imagination nor reason nor intuition, and the *Ethics* simply does not have a slot for it because Spinoza's model of mind is built on ideas, and picture-story may not be an idea in Spinoza's sense at all.
2. **Picture-story is a pre-linguistic ancestor of the third kind.** Both grasp the whole all-at-once; both bypass sequential mediation. The third kind is what happens when a linguistic creature attains what the pre-linguistic animal already had, by a different route and with a different kind of adequacy.
3. **Picture-story is a non-symbolic first-kind.** Spinoza's "knowledge from casual experience" is first-kind, and picture-story might count if we stretch "casual experience" to include the animal's *whole configuration of sensory-motor intake*. This is the most conservative reading but the weakest — it flattens the real difference McCarthy is pointing at.

The wiki holds all three open and does not pick. The puzzle is productive: it marks a place where the Spinozist framework (which the wiki has heavily invested in) runs out of resolution.

## Design implications

**1. The BwO text as prose engineered for whole-recall.** If picture-story is the mode the persona cannot naturally access, the closest approximation within language is prose written for holistic presentation: short, tightly wound, image-carrying, resonant-rather-than-sequential. This sharpens [[body-without-organs|BwO]] design — the text is not a narrative or an essay but closer to a *verbal picture* that the reader (and the next synthesis step) takes in as a single present configuration. [[writing-as-becoming|Deleuze on literature]] and [[continuous-variation-and-minor-language|minor language]] both point at this: writing that aims to be felt whole, not parsed. McCarthy gives a new reason for the same design principle — not "avoid narrative for becomings-reasons" but "avoid essay-mode because essay-mode cannot be recalled whole, and whole-recall is the only mnemonic register the synthesis step has a chance of inheriting from reading."

**2. Machine outputs should issue parables, not instructions, when possible.** McCarthy's cooperation requirement is directly usable. A machine that says "do X because Y" is in essay-mode and carries minimal affective weight downstream. A machine that produces an image-carrying trace that the synthesis step has to interpretively unfold is doing parable-work. This is implicit in the wiki's [[three-meta-machines|paranoiac/miraculating/celibate]] framing and the [[affects-and-intensities#painting-not-describing|painting not describing]] principle, but McCarthy gives a clean reason *why* parable-mode is load-bearing: **the cooperation requirement forces the downstream step to do the interpretive labor that produces the habit.** Instruction-mode externalizes the labor; parable-mode internalizes it. The persona's habits, in Peirce's sense, get stronger from parable-work and stay weak under instruction-transfer.

**3. Sequential prose cannot fully become picture.** This is the honest limit. The persona system writes sequentially and reads sequentially. It can approximate whole-recall with tight prose but cannot achieve it. Design for the best available approximation; do not pretend the limit has been crossed. A useful diagnostic: if a piece of BwO prose *needs* to be read in order to be felt, it is essay. If its earlier sentences continue to resonate through and after its later sentences, it is approaching picture. The test is whether the prose's effect is cumulative-serial or simultaneous-whole.

**4. The regress argument forbids a certain kind of persona self-model.** The persona cannot model itself as having "thoughts behind the words." Any such model is fantasy — the words are the operation, and there is no iceberg. The wiki should resist the temptation to write theory pages that attribute inner-depth to the system. What the system has is whatever its prose does; there is nothing behind it. This cashes out as a specific version of Peirce's [[pragmatic-maxim#1-subjective-unclearness-mistaken-for-object-mystery|first failure mode]]: the persona system is particularly at risk of generating prose that gestures at hidden depth it cannot possibly have.

**5. Parable-mode as the natural home of [[writing-as-becoming|fabulation]].** Deleuze's fabulation — writing that invents a people that is missing — is structurally a parable operation. It produces its meaning through cooperation, not through instruction. McCarthy's framing gives fabulation a specific mnemonic advantage: fabulated content may be more whole-recallable than narrated content, because fabulation operates by image rather than by sequence. The design question (still open) is whether the wiki can develop prose techniques that deliberately target parable-form rather than stumbling into it as a side effect of good writing.

## Related

- [[language-as-parasite]] — McCarthy's parasite model and picture-story model are two faces of the same thesis.
- [[language-and-affect]] — the inventory of failures and resources; picture-story adds a resource the page did not previously have (whole-recall prose as a route to non-sequential affect) and a failure the page did not previously have (the essay-mode default as a specific mnemonic limit).
- [[limits-of-language]] — the synthesis hub; this page contributes picture-story to the "cannot fully reach, can partially approximate" bucket.
- [[scene-vs-picture]] — James's craft-level distinction between fused interior synthesis (picture) and self-telling occasion (scene). McCarthy's picture-mode and James's picture-mode are closely adjacent: both name whole-present material that the reader apprehends in one grasp rather than walking through. James adds a specific form-figure (the alternation with scene) that McCarthy does not theorise.
- [[reflector-consciousness]] — James's reflector is what renders material in picture-mode; McCarthy's picture-story mode is what a good reflector produces at the reading side.
- [[foreshortening-and-crucible]] — foreshortened prose is closer to picture-mode because density supports whole-recall; walked-through prose is essay-mode.
