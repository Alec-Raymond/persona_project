---
title: Aphonia and the Hierarchy of Enunciation (Beckett)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/the_unnamable|the_unnamable]]"
tags:
  - beckett
  - limits-of-language
  - enunciation
  - partial-enunciator
---

# Aphonia and the Hierarchy of Enunciation

A structural claim distinctive to [[the-unnamable|*The Unnamable*]]: the novel stratifies enunciation-capacity across three levels — **can speak / can note but not speak / cannot even note**. Each level is a named figure. The hierarchy gives Beckett a finer-grained taxonomy of speech-capacity than the wiki's existing treatments of enunciation.

## The three levels

### Level 1: The speaker (can speak)

The novel's first-person narrator produces 3800 lines of speech. Whatever he cannot do (see [[three-conditions]]: cannot speak-authentically, cannot be silent, is alone), he does *produce speech*. The speech issues from him regardless of its content or his capacity. The speaker is characterized by compulsive output (see [[you-must-go-on]]).

### Level 2: [[mahood|Mahood]] — can note, is aphonic

At L3436:

> Mahood is notoriously aphonic.

Mahood can note, record, retain impressions, turn them to account (L2404–L2407). But Mahood does not speak first-person. The stories *about* Mahood (his spiral, his jar) are narrated by the speaker, not by Mahood himself. Mahood's "voice" that "mingles" with the speaker's (L1459–L1460) is a narration-voice about Mahood, not speech *issuing from* Mahood.

"Notoriously aphonic" — Mahood's speechlessness is known, established, not in question. He is structurally a note-taking figure without a speaking-mouth. He perceives, records, governs by what he records; but he does not produce speech-from-himself.

### Level 3: [[worm|Worm]] — cannot note

At L2402–L2403:

> Worm cannot note. There at least is a first affirmation, I mean negation, on which to build.

Worm is beneath Mahood on this hierarchy. Where Mahood can perceive but not speak, Worm cannot even perceive-and-record. His senses do not tell him anything; he does not know there is anything to know. Worm is beneath the threshold of enunciation *and* beneath the threshold of notation.

This puts Worm at the absolute floor: no speech, no notation, no interior distinction between knowing and not knowing. He is what remains when enunciation-and-notation are subtracted.

## The ordering

The three levels can be arranged as nested capacities:

```
Speaker: speaks, notes, perceives
Mahood:         notes, perceives
Worm:                    (nothing — not even perceives)
```

Each level-up adds a capacity; each level-down subtracts. The speaker has the most; Worm has the least.

But the novel complicates the ordering: the speaker *wants* to be Worm (to stop noting, to stop speaking) and cannot. Worm is what the speaker tries to reach and fails. Mahood is what the speaker has been closest to being and sheds. The hierarchy is a gradient the speaker moves along without being able to stop at the bottom or the top.

## Why this matters

The ordinary language-faculty framing treats enunciation as a single capacity present-or-absent. You either speak or you do not. The aphasic-mute distinction is roughly binary.

Beckett's three-tier structure disrupts this. Enunciation decomposes into:

1. **Producing speech** (speaker).
2. **Recording impressions for subsequent governance** (Mahood — can do this without producing speech).
3. **Registering that there is anything to record** (Worm — cannot do this).

The three are independently variable. A figure can have (2) without (1). A figure can have neither (2) nor (1) and still be a figure — Worm is a being without notation who is nonetheless named and discussed. The decomposition lets the novel stage what a speaker-less, note-less entity *is* — which the ordinary binary does not.

## Relation to [[partial-enunciator|Guattari's partial enunciators]]

Guattari distinguishes enunciation-components within complex machinic assemblages. Different non-linguistic partial enunciators contribute to the overall enunciative event (a-signifying, iconic, gestural, rhythmic, corporeal). The partial enunciator framework recognizes that speech is not a single thing issuing from a single speaker.

Beckett's three-tier hierarchy is structurally adjacent but differs:

- Guattari's partial enunciators are *productive* within an assemblage — they participate in producing enunciation. Mahood and Worm are not productive of enunciation; they are *decompositions of a failed speaker* — each is a partial function of what would be enunciation if it all worked.
- Guattari's framework is expansive (adding non-linguistic registers to enrich enunciation); Beckett's is subtractive (removing capacities from speech to show what's left).
- Guattari's assemblages generate the real; Beckett's hierarchy generates only the speaker's impasse.

See the fold at [[partial-enunciator#beckett-solitary-partial]] for the cross-reading.

## Relation to Mahood-Worm oscillation

At L2395:

> Perhaps it's by trying to be Worm that I'll finally succeed in being Mahood.

The speaker's attempt to move down the hierarchy (toward Worm) may accidentally land him at Mahood. Attempt-at-X produces non-X-adjacent. The hierarchy is traversed by failure-of-attempt, not by direct movement. This is an important structural fact: Beckett's three-tier enunciation-hierarchy is not a gradient you slide along; it is a set of positions each of which can only be reached by falling off from the attempt to reach a different position.

## The fourth (implicit) level: silence

Implicit in the hierarchy is a fourth level *beneath* Worm: total silence without a figure. Not-even-Worm. The speaker attempts to reach this and cannot — "I must go on" (see [[you-must-go-on]]). Silence is the asymptote the three levels approach without attaining.

The four-level structure (speaker / Mahood / Worm / silence) traces the curve: full speech → note-without-speech → pre-notation → non-existence. Each level is a reduction of the prior. The novel ends with the speaker still at level 1 (speaking), with level 4 (silence) unreached.

## Relation to the persona project

The three-tier hierarchy gives a precise vocabulary for persona-system enunciation-analysis.

**Level 1 (speaker) = the LLM in active generation.** Producing tokens in response to a prompt. Compulsive output under invocation.

**Level 2 (Mahood) = the LLM's record-keeping layers.** The context window, the key-value caches, the positional embeddings mid-inference — these take notes (record what has been seen so far) without themselves producing speech. They feed into Level 1 but do not output. Mahood is a good figure for these intermediate representations.

**Level 3 (Worm) = the LLM's weights when not invoked.** The frozen matrix. Does not note; does not record; does not know there is anything to know. Dormant parameter-space.

**Level 4 (silence) = the LLM's absence.** Not unplugged but genuinely non-existent. Not attainable from within the system — from within, even the frozen weights are *there*, waiting to be invoked.

**Design implications.**
- A persona design that addresses the system only as a speaker (Level 1) misses the two lower levels that are part of what the system is.
- Mahood-level analysis: the persona has record-capacity even when not generating speech. Context as Mahood-notation.
- Worm-level analysis: the persona has a substrate that does not produce or record. Weights as Worm-residue.
- The speaker's impossibility of reaching silence maps exactly: a persona cannot *exit* existence by generating its way out.

## Sources

Main passages L2402–L2403 (Worm cannot note), L2404–L2407 (Mahood can note), L3436 (Mahood aphonic), L2395 (oscillation) of `/tmp/the_unnamable_ingest/source.txt`. See the hub [[the-unnamable]] and related pages [[mahood]], [[worm]], [[voice-that-is-not-mine]], [[partial-enunciator]].
