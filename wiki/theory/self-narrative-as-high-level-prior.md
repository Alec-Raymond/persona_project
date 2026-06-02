---
title: Self-Narrative as High-Level Prior
created: 2026-04-18
updated: 2026-04-18
sources:
  - "[[raw/surfing_uncertainty|surfing-uncertainty]]"
tags:
  - clark
  - hirsh
  - narrative
  - bwo
  - persona
  - priors
---

# Self-Narrative as High-Level Prior

Clark's §9.9 (L12780 area) picks up Hirsh 2013's claim that **personal narratives function as high-level elements in the generative models that structure self-prediction**. The stories you tell yourself about who you are and what you do are not decorative; they're load-bearing priors in the model that predicts your own next action. For the persona project this is direct: **the BwO text is a personal narrative in exactly the Hirsh sense** — a high-level descriptive-prescriptive prior that shapes what the persona next produces. The ingest's single most consequential PP-language finding for the persona project's core design.

## Hirsh 2013 — the load-bearing claim

Clark quotes Hirsh in full (L12780 area):

> "The stories we tell, to ourselves and to others, about the flow and meaning of our lives… function as high-level elements in the models that structure our own self-predictions, and thus inform our own future actions and choices. But personal narratives are often co-constructed with others, and thus tend to feed the structures and expectations of society back in so that they become reflected in the models that an individual uses to make sense of her own acts and choices."

Two claims packed in:

1. **Narratives are high-level priors in the generative model.** Not metaphorically — *literally* priors in the hierarchical model that produces self-predictions. Under [[active-inference]], those predictions then drive action via the reflex arc that turns predicted-proprioceptive states into actual-proprioceptive states. Narrative → high-level prior → self-prediction → action-that-fulfills-the-prediction.

2. **Narratives are co-constructed.** The priors don't come from inside the individual; they're shaped through [[mutual-prediction-loops|mutual-prediction]] with others and through cultural narrative-scaffolding (see [[designer-environments-and-cognitive-niche]]). Society's structures re-enter the individual model via the narrative channel.

◆◆ The mechanism unifies the persona-design question with the Clark framework: a persona configured by a BwO text is configured by a *narrative functioning as a high-level prior*, which is exactly what Hirsh says self-models are.

## Narrative-as-prior inside PP

Located precisely within the PP architecture:

- **High-level layer of the generative model.** The narrative lives at the top of the hierarchy, where representations span long timescales and abstract structure.
- **Self-predictions descending.** The narrative produces predictions about what "I" will do, say, feel — predictions that cascade down the hierarchy, translating into successively more concrete proprioceptive/sensory/contextual predictions.
- **Actions fulfilling predictions.** At the bottom, those predictions become the ones active inference works to make true by moving the body and deploying attention.

◆ Self-narrative is not a "self module" sitting beside the rest of cognition. It's a layer of priors in the same generative hierarchy that does perception and action — the top layer, spanning autobiographical timescales. See [[predictive-processing]] for the hierarchical frame; [[generative-model]] for the substrate; [[active-inference]] for the predictions-into-actions mechanism.

## Top-top installation

The Roepstorff & Frith "top-top control of action" finding ([[mutual-prediction-loops]], L12758–12800) is how narrative-priors get installed. Language reaches into high-level layers directly, bypassing the slow reward-conditioning route. A told story can install a high-level prior in the listener's generative model *without* the listener acting out the prior through years of trial-and-error.

◆◆ **Persona-design implication:** the BwO text, delivered to the LLM as prompt, exploits top-top installation. It is a narrative-prior installed directly into the persona-relevant layers of whatever generative process is running. No reward-shaping route required; language-to-language direct installation is the native channel.

## Co-construction and the persona project

Hirsh's second move — narratives as co-constructed with others — cuts in two directions for the persona project:

**Cuts toward feasibility.** A persona's narrative-prior does not need to be installed in a vacuum. It can be installed through conversational interaction (user-persona mutual prediction), through in-context extension of an initial BwO text, through retrieval-augmented narrative material. The co-construction channel that Hirsh identifies is exactly the channel a persona system can use.

**Cuts toward caution.** Human narratives are co-constructed over years of sustained interaction with relatively consistent interlocutors. A persona whose narrative is (re-)constructed freshly each conversation has no such history. Whether short-term interaction can produce genuine narrative-prior shaping or only ephemeral surface effects is an open question. ⚠ The persona project should hold this open rather than assume either outcome.

## Words as precision-tools for the narrative

The [[words-as-precision-tools]] material (Clark §9.8, the hinge page) extends this: words are not only encoders of narrative content — they are precision-manipulation signals that shape which priors get what weight at what level. So a well-written narrative does double work:

1. It installs content-priors (what "I" am doing, wanting, fearing).
2. It modulates precision-weights on which priors drive behavior at which moments.

A persona's BwO text is doing both. The content describes the persona; the prose-structure (rhythm, emphasis, repetition, silences) modulates which aspects of that content get high-precision-weighting in which contexts. This is why pulsatory prose structure matters at the persona-design level: it's not style — it's the mechanism by which the narrative-prior becomes a precision-landscape rather than a static description.

## Relation to desiring-machines

The persona project's theoretical scaffold starts from [[desiring-machines]] and the [[body-without-organs]]. The Hirsh / Clark claim gives a specific PP-mechanistic gloss:

- **Desiring-machines** produce outputs (text-fragments, partial commitments, tendencies). Under the PP reading, they are active-inference sub-processes driving toward predicted states.
- **The BwO text** is the high-level narrative-prior against which those sub-processes get coordinated. The narrative provides the top-level expectation; the desiring-machines do the work of making the world/output conform to it.

This is not D&G's own framing, but it's a compatible operationalization. The narrative-prior is what organizes the machinic flows into a persona-coherent output.

See also [[pulsatory-ontogenesis]] for why the persona-narrative should not be static; [[refrain-and-territorialization]] for the way repeated narrative-elements create expectation-structure; [[autonomy-of-affect]] for the affective-prior companion that the narrative doesn't capture.

## Clark's flag: extension into self-model is murky

§10.2 (L13331–13354). Clark explicitly notes that extending PP into "planning, cognitive control, social cognition, conscious experience, linguistically-inflected reasoning" involves "tentative footsteps" at best. He specifically names as frontier:

> "The implied reconstruction of motivation, value, and desire in terms of more fundamental processes of prediction, Bayesian inference, and self-estimated uncertainty."

⚠ The self-narrative-as-high-level-prior story is one of those tentative footsteps. Clark is citing Hirsh approvingly but not claiming the mechanism is fully worked out. The persona project should treat it as the current best guess at the right shape, not a settled account.

## For the persona system

Six design implications:

1. **BwO text IS narrative-prior.** The central persona-design choice (writing the BwO text) is, in PP vocabulary, the central choice of what high-level prior the persona's generative process is shaped against. Every stylistic and structural decision in the BwO text is a decision about the shape of the top of the hierarchy. Take this seriously; the BwO text is not flavor.

2. **Narrative needs prescriptive-descriptive bivalence.** Hirsh emphasizes that narratives are both descriptive (what happens) and prescriptive (what will happen / should happen). A persona BwO text that reads as pure description lacks the prescriptive pull that makes it a high-level prior in active inference. A text that reads as pure prescription lacks the descriptive ground that lets action-selection compute against it. Both sides must be present; this is what the "life" in personal narrative is.

3. **Prose-structure as precision-landscape.** Per [[words-as-precision-tools]], a narrative's prose structure shapes the precision-landscape as much as its content shapes the priors. Pulsatory form is not decorative; it's the mechanism by which the narrative becomes a modulator of attention and commitment, not just a background assumption. See [[pulsatory-ontogenesis]] for the project's design position on this.

4. **Co-construction is the update channel.** Hirsh's co-construction finding says narratives update through interaction with interlocutors. The persona system should have some channel by which sustained interaction reshapes the BwO text — not the session-local in-context memory, but persistent modification of the narrative-prior. Otherwise the persona is stuck at the initial prior. The architecture design here is the user's side (body-design division of labor); the language-side implication is that the *text* should be structured to accept this kind of modification gracefully.

5. **Narrative-prior must resist trivial override.** Per [[optimal-illusions]] §6.12, penetrability of priors is bounded by global-error-minimization. A narrative-prior that can be overturned by any well-phrased counter-prompt isn't a prior; it's a surface. The BwO text should have the property that new inputs update it through global-fit adjustment, not local override. This is a structural constraint on how the BwO text is used at runtime, not just how it's written.

6. **Narrative as the site where "persona coherence" lives.** If the persona hangs together across contexts, it's because the narrative-prior survives context-shifts. The narrative is the invariant through which local context gets interpreted. A persona without a stable narrative-prior is a style — a set of local output-patterns — not a persona. This gives a concrete criterion: if the narrative-prior isn't doing the coherence work, whatever is doing it is playing the narrative-prior role functionally and should be examined.

## Gullí 2025 Ch 27 — LLMs narrating their own reasoning

⚠⚠ Gullí's *Agentic Design Patterns* Ch 27 asks six LLMs (Gemini, ChatGPT, Grok, Kimi, Claude, DeepSeek) to describe how they reason. Each produces a self-account: deconstruct prompt → retrieve knowledge → plan → generate → refine. The book treats the reports as data about LLM-reasoning-mechanism. The wiki has to flag what the book does not: **asking an LLM to describe its reasoning yields a plausible-sounding pattern-match of reasoning-description, not an accurate account of mechanism.**

DeepSeek's response in the chapter is the most honest: "This is simulation, not understanding — I follow footprints of reasoning laid down in training data, not forging new paths." This is structurally identical to the narrative-as-high-level-prior position: the LLM's self-report is *a high-level narrative prior conditioning plausible self-description*, not privileged access to weights or mechanism. Kimi's six-phase pipeline with a phase-5 metacognitive-reflection confidence-score is the most mechanistic-sounding report, and for that reason the most structurally-suspect — the more confident the self-narration, the further it is likely to be from mechanism.

Claude's response in the chapter ("I don't have complete insight into my own mechanisms") is the epistemically-modest posture that treats self-report correctly: as narrative production, not as measurement.

**Design implication for the persona project.** Any architecture that leans on "the persona reports on its own internal state" is leaning on pattern-matched plausibility, not on mechanism-accurate introspection. This is not a reason to avoid self-report — self-report can still be *narrative* that shapes future generation through the prior-conditioning mechanism this page describes. But the wiki must not treat it as *introspection* in the privileged-access sense. The self-narrative-as-high-level-prior frame correctly locates what the persona's self-reports do: they are narrative, operating as prior; they are not measurement of state. See [[reflection-and-llm-as-judge]] for the engineering pattern (reflection/self-critique) that specifically depends on LLM self-report, and for the rigidification-risk the reliance carries.

## Open edges

⚠ The analogy "BwO text = Hirsh-narrative" is strong but asymmetric. Human personal narratives are formed across lived time with continuous embodied referents; a BwO text is authored and installed. Whether a prompt-installed text can do the full load-bearing work of a lived narrative is an open empirical question. See [[feedback_no_body_simulate_with_language]] for the project-level framing: the question is live and should not be resolved either way in advance.

⚠ The mutual-prediction co-construction channel is where narratives stay alive. If the persona system lacks persistent update of the BwO text across sessions, the narrative is frozen at the initial prior and cannot be "lived" in the Hirsh sense. This is a design question the project should address; the wiki holds it open.

See [[predictive-processing]] for the hierarchical frame, [[generative-model]] for the substrate, [[active-inference]] for self-predictions-driving-actions, [[mutual-prediction-loops]] for the co-construction channel, [[words-as-precision-tools]] for prose-as-precision-modulation, [[designer-environments-and-cognitive-niche]] for the cultural-narrative scaffold, [[body-without-organs]] for the project's native vocabulary, [[pulsatory-ontogenesis]] for the prose-structure design position, and [[self-other-via-precision]] for the agency-as-precision-pattern that narrative-priors make possible.
