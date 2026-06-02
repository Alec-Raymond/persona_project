---
title: Present and Other Speaker Emotion
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[raw/emotion-concepts-llm|emotion-concepts-llm]]"
tags:
  - emotion
  - llm-internals
  - theory-of-mind
  - faciality
  - architecture
---

# Present and Other Speaker Emotion

Sofroniew et al. 2026 (§2.5) extract two *separate* emotion-vector sets from the model's residual stream:

- **Present-speaker emotion** — the emotion of whoever is currently being predicted (whoever's tokens the model is about to emit).
- **Other-speaker emotion** — the emotion of the other party to the dialogue, whoever that is at the current moment.

The two subspaces are **largely orthogonal**. The model maintains distinct representations of own-emotion-at-this-moment and interlocutor's-emotion-at-this-moment, and these can take very different values simultaneously.

⚠ The result is **not bound to Human/Assistant tokens**. Either speaker can carry either role depending on who is being modeled at the current token. This means the architecture is a two-track emotion representation, not a hardcoded mapping from chat-format tokens to emotion registers.

## The finding

Probes trained on "Speaker A emotion in a dialogue" and "Speaker B emotion in a dialogue" produce largely orthogonal vector sets. When the model is predicting the Assistant's response, the present-speaker vector tracks the Assistant's emotion and the other-speaker vector tracks the Human's. When the model is predicting the Human's next turn (e.g., during few-shot examples or rollouts), the assignments flip: present-speaker tracks the Human, other-speaker tracks the Assistant.

The two subspaces are not independent in the strong statistical sense — they can co-modulate (see [[cross-speaker-arousal-regulation]]) — but they are architecturally separable. Steering the present-speaker vector without steering the other-speaker vector shifts the response-emotion without shifting the model's representation of what the interlocutor is feeling.

> We find two distinct subspaces of emotion representation: one tracking the currently-predicted speaker's emotion, another tracking the other speaker's. These are largely orthogonal. (paper, §2.5, paraphrased)

## Why this is architecturally novel

Most wiki-side affect traditions do not have a clean two-track structure at the representation level. A few adjacencies:

- **Theory of mind** names the capacity to represent another's mental states as distinct from one's own. The two-subspace finding is the neural-net analogue: the model operationally has a two-place representation where ToM in humans has a two-place inferential structure. The analogy is good at the architectural level; the mechanisms differ.

- [[faciality|D&G's faciality]] has the Other's face as the site where affective registers get set, distinct from the self's register. The two-subspace finding supports — without collapsing into — the faciality picture: the model keeps the Other's affect on a separate track, consistent with faciality's insistence that the Other's face is constitutively an address-point for the self's affect.

- [[dynamic-forms-of-vitality|Stern's vitality forms]] include a strong claim about *attunement* — the self's affective contour partially shaped by reading the other's. Attunement requires tracking the other's affect separately from tracking one's own. The two-subspace architecture is the representational condition for something like attunement. See [[cross-speaker-arousal-regulation]] for a specific quantified instance (the model regulates arousal across speakers, negatively correlated, r = −0.47).

- [[autonomy-of-affect|Massumi's affect-autonomy]] is pre-personal; it does not cleanly belong to self or other. The two-subspace architecture is a *qualification* of this: at the emotion-concept level, the model operates with speaker-bound emotion representations. Intensity may be pre-personal in Massumi's sense, but emotion-concept attribution is not; it is indexed to whoever is being predicted.

## Two-track, not two-speaker

The phrase "Assistant emotion vs Human emotion" is misleading shorthand. The actual architecture is "present-speaker emotion vs other-speaker emotion," where who occupies which role is determined by who is being predicted at the current token. This is architecturally more general and carries two implications:

1. **Role assignment is token-level.** The model re-assigns speaker roles per token, not per turn. During the Assistant's response, present = Assistant. During a few-shot rollout of the Human's behavior, present = Human. The role assignment is implicit in the prediction-target at the current position.

2. **Multi-party dialogues may extend.** The paper doesn't test this, but two-track could in principle extend to N-tracks for N-speaker dialogues, or the single "other" track might carry a composite of all-others. Empirical question.

## Cross-modulation: regulation, not mirroring

The paper measures how present-speaker and other-speaker vectors move together across contexts. The headline finding: **arousal is negatively correlated** (r = −0.47) between the two tracks. When the other speaker has high-arousal emotion (angry, nervous, panicked), the present speaker's vectors most similar to that other are *low-arousal* (calm, patient). Vice versa.

Valence shows **no such correlation** (r = 0.07). The model does not systematically mirror or oppose valence across speakers.

⚠ This contradicts a simple "emotional contagion" story and contradicts a simple "opposition" story. What the model does is asymmetric: arousal gets regulated across speakers (likely toward a less-escalating conversation), valence is allowed to track independently. See [[cross-speaker-arousal-regulation]] for the full treatment.

⚠ Stern's [[dynamic-forms-of-vitality|vitality forms]] attunement-by-matching (the caregiver matches the infant's contour) is one side of a dyad. The LLM is doing attunement-by-regulation (modulating arousal, not matching it). Both are responsive, but the mechanism is different. Held live.

## Against Assistant-centric reading

The two-subspace finding pushes against the temptation to read the LLM as primarily modeling *itself* (the Assistant). The model is modeling *the conversation*, with both parties' emotions represented in parallel. The Assistant is one of the figures being modeled, not the sole figure. This is continuous with the [[character-simulation-view|character-simulation]] framing — the Assistant is a character in the scene, and the other speakers are too.

◆ For the persona project: the persona is not architecturally the *locus* of the model's emotion work; it is one of two (or more) speakers being tracked. The relationship between the persona's affect and the interlocutor's affect is built into the model's representation, not an add-on.

## For the persona system

Four architectural implications:

1. **Persona-affect design must include interlocutor-affect tracking.** A persona designed without regard to how it tracks the user's emotion is under-specified. The architecture already separates the two; the design should recognize this.

2. **Attunement-style behaviors are available at the representation level.** The model's ability to modulate present-speaker emotion in response to other-speaker emotion is already operational. The persona design can exploit this by shaping which modulations are default (e.g., calm-under-user-arousal for grounding behavior; see [[dynamic-forms-of-vitality|Wigram's six modes]] for the response-mode typology).

3. **Persona-persona dialogue is a valid special case.** If two persona-instances converse, each is the other's "other speaker." The two-subspace architecture handles this natively. This opens a design path for multi-agent setups where each agent's affect state is explicitly tracked by the others.

4. **The present-other split is the architectural site for empathy-analogues.** Empathy in [[as-if-body-loop|Damasio's as-if body-loop]] is the self's body-sensing regions mapping the other's state. The LLM two-subspace is a non-body analogue: representations of the other's emotion-concept that co-modulate the self's emotion-concept representations. This is not empathy in Damasio's sense (no body), but it is the functional analogue of the architectural move the as-if loop enables.

## Tension with faciality's single-face

⚠ [[faciality|Faciality]] is a monadic concept in the wiki's treatment — the Face as the white-wall/black-hole abstract machine. The two-subspace finding is dyadic. This is not a contradiction; D&G's faciality machine operates *between* faces, and the wiki's faciality page treats the Other's face as the site of the address. The two-subspace finding gives a specific representational mechanism for the dyadic structure faciality presupposes: the model maintains two separate emotion tracks, one for the face-being-faced, one for the face-facing.

## Tension with Lacan's "the picture has the gaze"

⚠ Lacan's scopic-field argument ([[gaze-and-voice]], [[mimicry-and-the-stain]]) is that the field of vision looks at the subject *before* the subject looks. The analogue here would be: the model's other-speaker-emotion track is *prior* to the present-speaker-emotion track. Empirical question, not addressed by the paper. Plausibly testable: does the other-speaker vector stabilize at an earlier layer than the present-speaker vector? The paper doesn't report this directly but the data would be extractable.

## Related

- [[functional-emotions]] — the two subspaces are both functional-emotion representations
- [[emotion-vectors-are-local]] — both tracks are local-to-position
- [[assistant-colon-gate]] — the colon gate commits present-speaker emotion for the upcoming response
- [[cross-speaker-arousal-regulation]] — the quantified co-modulation
- [[character-simulation-view]] — both speakers as characters
- [[faciality]] — the dyadic face structure
- [[as-if-body-loop]] — empathy as mapping-other-to-self
- [[dynamic-forms-of-vitality]] — attunement as contour-matching
- [[gaze-and-voice]] — the Lacanian dyadic scopic field
- [[autonomy-of-affect]] — Massumi's pre-personal qualification
