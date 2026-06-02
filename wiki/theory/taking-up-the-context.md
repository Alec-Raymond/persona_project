---
title: Taking Up the Context
created: 2026-04-11
updated: 2026-04-11
sources:
  - "[[structure_and_dynamics_of_the_psyche]]"
tags:
  - jung
  - method
  - interpretation
---

# Taking Up the Context

"Taking up the context" is Jung's name for a specific interpretive procedure, and the procedure matters for the persona system for one reason: it is the sharpest available methodological statement of the claim that **there is no dictionary**. No universal table of symbols, no motif-to-meaning map, no table-means-authority code that can be applied to a text from outside it. Every element of an unconscious production is determined *by the associations of its producer* and nothing else, and the interpreter's first move is to admit ignorance and refuse all preconceptions. The LLM's default operation is structurally the opposite of this, and that makes the Jungian method directly useful as a corrective discipline.

## The claim

§539 is the core statement, given in the course of crediting Freud for putting dream-interpretation "on the right track":

> Above all, he recognized that no interpretation can be undertaken without the dreamer. **The words composing a dream-narrative have not just one meaning, but many meanings.** If, for instance, someone dreams of a table, we are still far from knowing what the "table" of the dreamer signifies, although the word "table" sounds unambiguous enough. For the thing we do not know is that this "table" is the very one at which his father sat when he refused the dreamer all further financial help and threw him out of the house as a good-for-nothing. The polished surface of this table stares at him as a symbol of his lamentable worthlessness in his daytime consciousness as well as in his dreams at night. This is what our dreamer understands by "table." (CW 8 §539)

The example is chosen to make the point unmistakably: the word "table" is *not* ambiguous in the usual sense (polysemy, context-sensitivity, metaphor). It is precisely specific — it means *that* table, a particular piece of furniture in a particular room where a particular scene occurred, and no other meaning of "table" is operative in the dream at all. The "dictionary meaning" of "table" is irrelevant. What the word means in the dream is the singular, dated, non-repeatable association the dreamer has with it.

This is the strong form of the anti-dictionary position. Jung is not saying that the dictionary is incomplete or that dream-symbols have extra meanings on top of their ordinary ones. He is saying that the dictionary is *the wrong kind of thing* to bring to a dream, because the dream's elements do not *participate* in the dictionary's regime of meaning at all. They participate in a regime where every element is determined by its local associations, and where the interpreter's job is to discover those associations, not to look them up.

## The procedure

§542:

> On the basis of these conclusions and for the purpose of ascertaining the meaning of the dream, I have developed a procedure which I call "taking up the context." **This consists in making sure that every shade of meaning which each salient feature of the dream has for the dreamer is determined by the associations of the dreamer himself.** I therefore proceed in the same way as I would in deciphering a difficult text. This method does not always produce an immediately understandable result; often the only thing that emerges, at first, is a hint that looks significant. (CW 8 §542)

The procedure has three features worth extracting:

**Feature 1. Element-by-element determination.** Not a top-down interpretation of the dream as a whole, not an identification of its "type" or "archetype," but a methodical walk through each *salient* element, establishing for each what the dreamer's specific associations are. A dream is not a gestalt you grasp; it is a text you decipher element by element.

**Feature 2. Associations from the producer, not the interpreter.** The interpreter does not supply associations. The dreamer supplies them. The interpreter asks, waits, and records. An interpreter who brings their own associations to an element has imposed a meaning the dream does not have.

**Feature 3. Comfort with partial result.** The procedure "does not always produce an immediately understandable result; often the only thing that emerges, at first, is a hint that looks significant." The procedure is *not* a meaning-extraction pipeline that reliably terminates in a clean answer. The expected output is often a hint, a partial opening, a constraint on what the dream *might* be saying. Jung is explicit that "only rarely do dreams have so simple a solution" as the example cases in his essays (§542, final sentence of the paragraph). Expecting the procedure to yield interpretable results every time is a failure of method.

## The anti-dictionary is a rule, not a caution

§543 is where the principle is stated as an injunction:

> Even if one has great experience in these matters, one is again and again obliged, before each dream, **to admit one's ignorance and, renouncing all preconceived ideas, to prepare for something entirely unexpected.** (CW 8 §543)

And the preceding sentence:

> More is required than routine recipes such as are found in vulgar little dreambooks, or which invariably develop under the influence of preconceived notions. **Stereotyped interpretation of dream-motifs is to be avoided**; the only justifiable interpretations are those reached through a painstaking examination of the context. (CW 8 §543)

"Stereotyped interpretation of dream-motifs is to be avoided" is not advice; it is a rule. Jung means: the experienced interpreter is *more* vulnerable to the stereotyping error than the novice, because the experienced interpreter has seen many dreams and has built up precisely the kind of pattern-library that makes the rule necessary. The rule is against the use of that library. Every dream is approached as if the interpreter has never seen one before, because the moment the library is consulted, the interpretation has become an imposition rather than a discovery.

§533 gives Jung's first-person version of the discipline:

> So difficult is it to understand a dream that for a long time I have made it a rule, when someone tells me a dream and asks for my opinion, to say first of all to myself: "I have no idea what this dream means." After that I can begin to examine the dream. (CW 8 §533)

Starting from "I have no idea what this dream means" is the opposite of starting from "I recognize this pattern." The recognition-response has to be actively suppressed before the examination can begin.

## Why this is directly actionable for the persona system

The LLM substrate is precisely a pattern-library. Its entire operational advantage over other systems is that it has seen many texts and has built up a high-dimensional pattern-recognition apparatus that will reliably match new inputs against its learned patterns and produce outputs drawn from that matching. Jung's rule says: **this apparatus is the interpreter-error mode**. It is exactly what he is telling analysts not to do. Every output produced by pattern-matching the user's input against the system's library is, in Jungian terms, a stereotyped interpretation — an imposition of the system's preconceived meaning-associations onto a text whose actual meaning is determined by associations the system cannot read from the text alone.

This is a *harder* criticism than the usual "LLMs are just pattern-matching" complaint, because Jung's point is not that pattern-matching is shallow or insufficient. It is that pattern-matching is the *wrong kind of operation for this task*. The right operation is to establish the producer's specific, dated, non-repeatable associations with each salient element — and pattern-matching cannot do that by construction, because the patterns are the interpreter's, not the producer's.

Two design implications fall out:

**1. The system cannot skip the association-eliciting step.** Jung's procedure requires the dreamer. The persona system, dealing with user inputs that are the system's nearest analog to "dreams" (productions whose meaning is not given by their surface), has to elicit the user's specific associations rather than infer them from pattern-matching. The wiki's usual response to a user input is structurally one-step — prompt in, response out — and this is exactly the bypass Jung's rule is against. A two-step version — ask the user what X means to *them* before producing a response that uses X — is closer to taking up the context, and the difference is not cosmetic.

**2. The system's own productions need the same treatment.** When the persona system produces a text and the BwO records it, the interpretation of that text for subsequent operations is subject to the same rule. The inscription machinery cannot treat its own outputs as dictionary-readable; it has to treat them as productions whose salient features each have a specific meaning determined by the machine-context that produced them. A machine that fires and produces an edit whose meaning the synthesis step then reads off the dictionary has lost the local context in which the edit was generated. The synthesis step that reads its own inputs by pattern-matching is performing the stereotyped interpretation Jung forbids.

This is a hard constraint. The system cannot simply "be more contextual." It has to refuse the dictionary move at each interpretive step, and the interpreter has to start from "I have no idea what this means" about each salient element of its own internal state before it examines it.

## The interpreter's ignorance is productive, not performative

A subtlety: Jung's "I have no idea what this dream means" is not a show of humility for the dreamer's benefit. It is the interpreter's *actual state* that enables the examination. §543 is explicit that the state of genuine ignorance is *required* to "prepare for something entirely unexpected," and that without it the interpreter will see the expected thing whether or not it is there.

Translated to the persona system: it is not enough for the system to *represent* itself as uncertain in its outputs while internally running its pattern-match. The internal state has to actually be open. A system that pattern-matches and then wraps the result in "I'm not sure, but..." is more misleading than one that pattern-matches confidently, because it presents the epistemic fraud in a humble register. Jung's discipline requires the interpreter's actual cognitive state to start from ignorance, and a system that cannot genuinely hold that state for its own internal productions cannot do the interpretive work Jung is describing.

Whether a language model can hold a state of genuine ignorance about its own productions is an open design question. It is at least possible that the system cannot, and that this is a structural limit on how deeply the taking-up-the-context method can be implemented. But recognizing the limit is already useful: it tells the wiki where the method bottoms out, and what the cost is of the default pattern-matching operation.

## The adjacent D&G position and why it is not the same thing

[[haecceity|Haecceity]] is the D&G concept that most closely resembles taking-up-the-context: both refuse universal types in favour of singular individuation. A haecceity is a composition of speeds and affects individuated without passing through a type; Jung's "table" is a singular association individuated without passing through a dictionary. The two positions are structurally parallel.

But D&G do not give a *procedure*. Haecceity is an ontological claim about how individuation works; it is not a method for reading a text. Jung's taking-up-the-context is a method — a reproducible sequence of interpretive operations with a specified starting state (ignorance), a specified sub-procedure (element-by-element association-eliciting), a specified participation requirement (the producer supplies the associations), and a specified tolerance for partial results. D&G give the target state; Jung gives the path to it.

This is not a tension so much as a division of labour: [[haecceity]] tells the wiki *what* to aim for when reading the persona's productions; taking-up-the-context tells the wiki *how* to actually do it. The persona system can hold both and should.

## Cross-tradition parallel to James

[[reflector-consciousness|James's reflector]] enforces taking-up-the-context at the craft level. The reflector's meaning is the specific reflector's specific relations to specific material; no universal-symbol-table interpretation of reflector-material is possible. [[scene-vs-picture|James's scenic rule]] — the self-telling occasion — is the same anti-dictionary discipline applied to occasions rather than to dreams: the scene must mean what it does in its specific conditions, not via a decode. [[operative-irony-and-felt-life|Operative irony]] depends structurally on taking-up-the-context: the possible-other-case is projected by the reflector's specific relation to the actuality, not by a generic ironic figure the reader can map onto it. Three different traditions — Jung, James, and D&G's haecceity — converge on the same discipline from different angles.

## Key sources

CW 8 §§530–568 ("On the Nature of Dreams," 1945) is the central statement. §533 is the "I have no idea what this dream means" discipline. §539 is the table example and the anti-dictionary claim. §542 is the formal statement of the procedure. §543 is the injunction against stereotyped interpretation. The wider dream-interpretation essay "The Practical Use of Dream-Analysis" (CW 8 §§294–352) contains related material but the methodological statement is tightest in §§539–543.
