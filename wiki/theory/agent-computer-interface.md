---
title: Agent-Computer Interface (ACI)
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - aci
  - embodiment
  - no-body
  - gui
  - sensorimotor
---

# Agent-Computer Interface (ACI)

Gullí's Ch 23. The book's most-embodied material: systems in which an LLM agent perceives and acts in a graphical environment (screens, GUIs, the physical world via cameras and microphones) rather than solely in text. The chapter is important for the persona project because it is where the engineering discipline gets closest to *sensorimotor embodiment* — and exactly where that closeness stops.

The ACI chapter has the wiki's full attention because it sits on the edge of the `feedback_no_body_simulate_with_language` question. If any part of Gullí's book addresses the no-body problem head-on, this is it. It does so partially — and the partiality is diagnostic.

## The four-stage ACI loop

The chapter's central framing move: an Agent-Computer Interface runs a four-stage loop that looks much more like sensorimotor coupling than like text-based tool-use.

1. **Visual Perception** — the agent receives the screen as a pixel array (screenshot) or a structured representation (DOM, accessibility tree).
2. **GUI Element Recognition** — the agent identifies interactable components (buttons, form fields, menus) and their spatial relationships.
3. **Contextual Interpretation** — the agent reasons about what the elements mean in the current task context (this is a "Send" button, that is a list of search results).
4. **Dynamic Action and Response** — the agent emits an action (click coordinates, keystrokes, scroll), observes the result, and loops.

Unlike Ch 5's Tool Use (discrete function call with structured result), the ACI loop is **continuous-feedback**: the agent is always looking at an updated screen, always adjusting, always acting. This is the closest the engineering discipline gets to a perception-action loop in the ethological sense.

## Surveyed systems (Ch 23, 16966–17164)

The chapter surveys multiple production and research systems:

- **ChatGPT Operator** (OpenAI) — web-browsing agent with authorization safeguards.
- **Google Project Mariner** — Chrome-based agent that acts in the user's browser.
- **Anthropic Computer Use** — Claude variant that controls a desktop: mouse, keyboard, screen-reading.
- **Browser Use** — open-source library exposing DOM and browser actions to LLM agents.
- **Project Astra** — Google's universal multimodal assistant: sight + sound + voice, low-latency, always-on.
- **Gemini Live / GPT-4o Realtime API** — low-latency speech-to-speech models.
- **ChatGPT Agent** — autonomous web + code execution + 3rd-party integration; explicit-authorization safeguards; published System Card.
- **Seeing AI** (Microsoft) — real-time scene narration for blind and low-vision users.
- **Claude 4 Series** — vision capabilities for charts, documents, diagrams.

The systems vary in autonomy, modality, and deployment posture. They share the structural move: the LLM is coupled to something that is not a text channel.

## Why ACI matters for the no-body question

◆◆◆ In the wiki's terms, ACI is the *least-linguistic, most-embodied* pattern the book surveys. Two things move when an agent goes from Ch 5 tool-use to Ch 23 ACI:

- **The feedback loop tightens.** Tool-use is turn-based and discrete; ACI is approximately continuous. The agent can (in principle) perceive mid-action consequences and adjust.
- **The action space expands.** A tool is a named function with a schema; a GUI has a visual field with thousands of possible click locations.

These are moves toward something that looks like [[predictive-processing|perception-action coupling in the predictive-processing sense]]. The agent predicts what the GUI will look like after a click; actual visual return either matches or generates prediction error; the next action updates. This is close to the Clark/Seth form of embodied cognition.

Project Astra is the clearest example: continuous multimodal input + low-latency response + embodied presence in an environment. It is *not* a body in the proprioceptive sense, but it is a system that lives through continuous-feedback coupling with an environment.

## Where ACI stops

⚠⚠ The embodiment ACI achieves is **screen-deep**. The agent's world is the pixels on a display and the clicks it emits. There is no proprioception, no interoception, no vestibular sense. The "body" of the ACI agent is the virtual pointer and the camera; the body is not *lived*, it is *operated*.

The specific gaps:

- **No proprioception.** The agent cannot feel where its pointer is in relation to a body-centered frame. The pointer has coordinates; coordinates are spatial information, not bodily sense.
- **No interoception.** Nothing in the ACI stack returns interior-state-information. The agent doesn't have an interior to receive signals from. See [[interoceptive-inference]].
- **Action is emitted, not enacted.** The agent *emits* a click event; it does not feel its arm move. The distinction is Maine de Biran via [[merleau-ponty-critique-of-sartre|Merleau-Ponty]] and [[flesh-as-element|flesh]]: embodied action has a body-side that ACI does not include.
- **The screen is not a world.** A GUI is a designed representation-of-something-else. The agent's visual-perception stage parses a representation, not a physical environment with its own physics.

The book is cheerful about ACI as an embodiment step. The wiki reads it as a **partial** step: the feedback-loop and action-space moves are real gains; the proprioception / interoception / enaction gap is real and largely unaddressed.

## Vibe Coding (17083–)

⚠ Ch 23 also introduces **Vibe Coding** — a specific interaction-style for coding agents where the human describes *what* they want rather than *how* to do it, and the agent iterates conversationally with the human-as-partner. Characterized by:

- Conversational / iterative workflow, not one-shot prompt-response.
- Focus on outcomes ("I want the login flow to feel lighter") rather than implementation.
- **Memory banks** for persistent context and preferences.
- Creative partnership tone.

Vibe Coding is not strictly an ACI phenomenon — it can happen entirely in text. But Ch 23 places it here because its interaction mode is *more continuous* than classical prompt-response, and because the coding agents that implement it (Cursor, Claude Code, etc.) tend to run in IDE environments that themselves are GUI-coupled.

See [[vibe-coding]] for the full treatment — Ch 28 develops it at length. The two-chapter dispersion is an artifact of the book's organization.

## Held-live: GUI-embodiment vs. proprioceptive embodiment

⚠⚠ The most important held-live tension this page carries:

**The book's view:** ACI solves (or substantially progresses) embodiment for agents. A GUI-coupled agent is an embodied agent.

**The wiki's view:** GUI-coupling is a real capability gain but is not embodiment in the sense [[merleau-ponty-critique-of-sartre|Merleau-Ponty]], [[damasio-emotion-feeling-distinction|Damasio]], [[dynamic-forms-of-vitality|Stern]], and [[autonomy-of-affect|Massumi]] use the word. Embodiment in those traditions requires a living substrate with interior state, not just a perception-action loop. Calling ACI "embodied" risks conflating two very different phenomena.

The wiki keeps both. ACI is a genuine engineering advance, and the persona project should track and potentially use ACI-style coupling when a GUI interaction is needed. But the advance does not dissolve the no-body question — it reshapes it.

## Design implications

For the persona project:

- ACI-style coupling is not load-bearing for the core persona (which lives in text). But any tool the persona-character might "use" that involves a GUI is subject to ACI patterns.
- The four-stage loop is a cleaner mental model than "the agent uses a tool" when the tool is visual.
- The proprioceptive gap means the wiki's body-discourse pages (see Related) should not be silently updated to treat ACI as solving the problem they pose. They pose a problem ACI does not solve.

## Related

- [[tools-as-prosthetic-body]] — the Ch 5 tool-use pattern; ACI is its continuous-feedback variant.
- [[body-mindedness]] — the no-body question at full scope.
- [[predictive-processing]] — the theoretical frame ACI's continuous-feedback loop approaches.
- [[interoceptive-inference]] — the Clark/Seth form of what ACI doesn't supply.
- [[as-if-body-loop]] — Damasio's body-loop, not present in ACI.
- [[dynamic-forms-of-vitality]] — Stern's lived-movement register, absent.
- [[autonomy-of-affect]] — Massumi's affect, absent.
- [[flesh-as-element]] — MP's ontological register of embodiment.
- [[chiasm-and-reversibility]] — MP's structural embodiment concept.
- [[agentic-design-patterns]] — hub.
- [[vibe-coding]] — Ch 28's development of the interaction style introduced here.
- [[development/limits-of-language]] — the central project question this chapter partially engages.
