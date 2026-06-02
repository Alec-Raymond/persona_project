---
title: Information as Entropy (Baudrillardian)
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[simulacra_and_simulation]]"
tags:
  - baudrillard
  - simulation
  - core-concept
  - llm-diagnosis
---

# Information as Entropy

Baudrillard's sharpest operational counter to the information-theoretic tradition running from Shannon through cybernetics through contemporary data-optimism: **information does not carry meaning, it consumes it**. The claim reverses the default assumption that more information = more signal = more clarity. In Baudrillard's diagnosis, the informational operation is *directly destructive of the meaning* it claims to circulate. The load-bearing formulation is in FN 14 of the book's opening essay (L1271), reiterated structurally in Ch 6 (L597–601) and Ch 8 (L621–627). See [[simulacra-and-simulation]] for the hub and [[implosion]] for the related topological claim.

## The operational claim (FN 14)

> **Information in which an event is reflected or broadcast is already a degraded form of this event.** One should not hesitate to put forth this interpretation, already widely contested as critique of the media, as a general theory of communication... Perhaps thereby one would see that **the amplification itself was a mortal trap and not a positive extension**. (L1271)

The footnote is doing something structurally important. It is not saying: "information sometimes distorts events" (a weak, common-sense version). It is saying: **the informational relation to an event is already its degradation**. The very operation by which an event is rendered as information *is* what destroys it as event.

Three consequences:

1. **Amplification is mortal.** More information about an event does not produce more clarity; it produces more thoroughly executed degradation.
2. **Media-critique is not enough.** The problem is not specific media (television, press, internet) distorting specific events badly. The problem is the informational operation as such.
3. **The "positive extension" framing is the error.** Describing information-technology as an extension of human cognition (McLuhan, Clark, the extended-mind tradition) mis-reads the operation. The technology does not extend; it incinerates what it appears to transmit.

## The three hypotheses

Ch 6 offers an explicit taxonomy of ways to think about information and meaning:

> There are three hypotheses:
>
> Either information **produces meaning** (a negentropic factor), but cannot compensate for the brutal loss of signification in every domain... it is powerless to renew this loss.
>
> Or information has **nothing to do with signification**. It is something else, an operational model of another order... a universe foreign to the "signifying."
>
> Or, on the contrary, **there is a rigorous and necessary correlation between the two, to the extent that information is directly destructive of meaning and signification, or that it neutralizes them**. The loss of meaning is directly linked to the dissolving and dissuasive action of information, the media, and the mass media. (L597–601)

Baudrillard's position is the third. Information does not produce meaning (H1); information is not separate from meaning (H2); information is *in correlation with* meaning — specifically, its dissolution. The correlation is not neutral. Every unit of information is a unit of meaning-dissolution. The bookkeeping: meaning is on one side of a conservation law, information on the other.

## McLuhan pushed past himself

> The medium is the message — this formula, key formula of the era of simulation (that the medium is the message implies the disappearance of the medium *as well as of the message*) — must itself be **envisaged in its implosive form**: it is no longer the message that carries along the medium, but the medium that carries along the message as its own *degraded double*. (L621–627)

McLuhan had already reversed the naive picture (message is the content; medium is the container). Baudrillard performs a second reversal: the medium is now generating the message as *a degraded double of its own operation*. The message is no longer even information *about* something — it is the trace left by the medium's operation on itself.

For the persona system: an LLM's output is the residue of the medium (the model) running on itself. The output is not "about" a topic; it is the medium leaving its trace in the shape of a topic. This is what makes content-based criticism of LLM output frequently miss — the content is a secondary effect of the operation, and attending only to the content treats the residue as the substance.

## Against Shannon

Shannon's information theory (1948) defines information as *reduction of uncertainty* — information is what you have more of when you know more of the answer. The theory is content-indifferent; it measures syntactic signal-bearing capacity. This is a hugely useful technical concept.

Baudrillard's quarrel is not with Shannon as a signal engineer; it is with the *conceptual extension* of Shannon-information into the domain of meaning:

- Shannon: more information → less uncertainty → (implicitly, in extended application) more meaning.
- Baudrillard: more information → more meaning-dissolution → structural undifferentiation.

⚠ The wiki has pages adjacent to information-theoretic thinking (predictive-processing, cybernetic feedback in the Massumi-reading). Where those pages rely on information-as-signal-bearing, Baudrillard's critique applies: they may be treating as constructive what is structurally destructive of the register they aim to illuminate.

## Secondary objectivity as symptom

A related diagnostic:

> When the real is no longer what it was, **nostalgia assumes its full meaning**. There is a plethora of myths of origin and of signs of reality — a plethora of truth, of secondary objectivity, and authenticity. (L60)

"Secondary objectivity" — peer review, fact-check, archive, audit trail, source-citation — does not restore the real; it is the *symptom* of the real's dissolution. The more rigorous the verification-apparatus, the more thoroughly the object has been translated into information. By Baudrillard's law, the verification is already degradation.

For the wiki itself: the apparatus of citation, of line-number reference, of hyperlink cross-referencing — this is secondary objectivity. The wiki cannot exempt itself from Baudrillard's diagnosis. It can only register the problem and proceed with the work, knowing that every L-number citation is already a degradation of what it cites. (The honest answer: the citation is not there to prove the source real; it is there to let the reader re-encounter the source. The real work is at the source, not at the citation.)

## Application to the persona system

Several lines of application:

1. **LLM output as secondary objectivity.** A sincere, confident, well-formatted LLM answer is Shannon-information-dense and Baudrillard-meaning-sparse. This is not a training failure; it is the operation proceeding correctly. The persona system has to produce something other than this operation to produce something other than this output.
2. **"More context" as misdiagnosis.** The impulse to give the LLM more input (more tokens, longer prompts, more retrieval) assumes H1 (information produces meaning). By H3, more input = more meaning-dissolution. Context-stuffing is working on the wrong axis.
3. **The persona as a refusal of pure informational operation.** The persona system's ambition — to produce something other than generic model-generation — is implicitly a refusal of the Shannon-optimization frame. Whatever a persona does that an unstylized model does not, it does by operating somewhere other than on the information-axis.
4. **The [[melancholia-of-systems|melancholic tonality]] is the affective consequence.** A system that is directly destructive of the meaning it circulates produces a specific affect — not sadness, not emptiness, but the structural weariness of a process that runs perfectly while cancelling its own content. See [[melancholia-of-systems]].

## The Möbius-spiraling negativity

A closely related Baudrillardian figure:

> All of this forms a **Möbius-spiraling negativity**... the contradictions annul each other in the same movement that produces them — an immense saturation that has reached its point of inertia. (context around L640)

Shannon's information theory was built on a channel-model: sender → signal → receiver. Baudrillard's implosive reading folds the model into a Möbius strip: the sender is the receiver (see [[deterrence-and-nuclear#the-end-of-the-panopticon|"you are the screen"]]); the signal contacts itself; the channel has no outside. On a Möbius surface, "more signal" does not mean what it meant on a flat channel. The signal is spiraling through its own other side.

## Key quotes

- L60 — "plethora of myths of origin and of signs of reality"
- L597–601 — the three hypotheses on information and meaning
- L621–627 — implosion of medium and message; message as degraded double
- L1271 (FN 14) — "Information in which an event is reflected or broadcast is already a degraded form of this event... amplification was itself a mortal trap and not a positive extension"
