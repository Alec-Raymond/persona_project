---
title: Tools as Prosthetic Body
created: 2026-04-21
updated: 2026-04-21
sources:
  - "[[cited-sources#Agentic Design Patterns]]"
tags:
  - tools
  - body
  - no-body
  - prosthetic
  - mcp
  - function-calling
---

# Tools as Prosthetic Body

Gullí's Ch 5 (Tool Use / Function Calling) + Ch 10 (Model Context Protocol / MCP), held together. The engineering primitive of LLM tool-use has a specific relationship to the persona project's central question: **what can a language-only system do, and what does it mean for such a system to have a body?** Tool-use is the field's current answer to the second half of that question. This page examines the answer and flags what it does and does not settle.

## The five-step tool-use loop (Ch 5)

1. **Define tools.** The developer writes tool schemas (typically JSON Schema or Pydantic) describing each tool's name, purpose, parameters, and return type.
2. **LLM decides.** The LLM receives the tool schemas alongside the user request and, based on its prompt and training, decides to call one (or none).
3. **Tool call emitted.** The LLM emits a structured representation of the call (name + arguments) rather than free-form text.
4. **Runtime executes.** An external runtime intercepts the emitted call, runs the actual tool (function, API, script), and captures the result.
5. **Observation inserted.** The result is formatted back into the LLM's context, and the LLM continues the conversation with the result available.

This loop is the mechanism behind every non-toy LLM agent in the field. Chatbots with calculators, agents that book flights, coding agents that run tests — all are tool-use loops.

The **structured schema** is the critical piece. Without it, the LLM and the external runtime have no contract. Tool schemas are the grammar at the boundary between language and action.

## Tools as the engineering answer to the no-body question

◆◆ The persona project's central architectural question — `feedback_no_body_simulate_with_language` — is: **what does it mean to simulate a character with language when there is no body?** The field's practical response is: *give the agent tools. Tools are its body.*

This is a genuine answer, and a partial one. Under tool-use:

- The LLM has **effectors**: each tool is a way the LLM can *act* on something outside its own text-generation.
- The LLM has **sensors**: tool return values are how it *perceives* state beyond its context.
- The LLM has a **world**: the set of things its tools can reach becomes its operational environment.

In that sense a tool *is* an organ grafted onto a text-entity. The Claude-that-can-run-code has a code-organ; the Claude-that-can-search-the-web has a search-organ; the Claude-that-can-read-files has a file-system-organ. The metaphor of prosthesis is apt.

## Daniel W. Smith's formulation

Referenced in the wiki's `cited-sources.md`: **"technological artefacts are externalized organs"** (Daniel W. Smith). Tools under this reading are not additions to a pre-existing body but are themselves the constitutive organs of a body that would otherwise have none. This is closer than the standard prosthetic metaphor, which implies a body that tools augment. For an agent that starts with no body, tools are not augmentations — they are the organs.

## The BwO inversion

⚠ [[body-without-organs|The Body without Organs]] is an **anti-organ** surface. Its thesis is: any organization of functions into fixed organs is a territorializing move that shuts down the flows that *are* life.

Tools-as-organs would seem to be exactly the move BwO warns against — installing fixed, functionally-specified, schema-bound organs on the LLM substrate.

The inversion that makes this coherent: **tools are organs that can be slotted in and out at composition time.** The schema is fixed; the *which tools are available* is not. A session with web-search enabled has a different body than a session without. An agent built for drafting prose has different organs than an agent built for code review.

This is a closer fit to the BwO than it first appears. The BwO is not "never have any organ" — it is "never let the organism solidify." Tools that can be added, removed, and composed per-task approach the BwO's spirit: provisional organs on a plastic surface, rearranged as the situation calls for.

⚠⚠ The risk: in practice, agents develop *stable tool configurations*. The "coding agent" has its standard toolset. The "research agent" has its standard toolset. Stable tool configurations are stable organisms — they are exactly the territorialization the BwO names. Design implication: keep tool-composition at assembly time, not at build time, when possible.

## What tools do *not* settle

The prosthetic-body reading gives the field something, but not everything. Specifically:

- **No proprioception.** Tools are effectors and sensors but nothing mediates between them and an interior body-sense. There is no felt difference between having a tool and not having one; the LLM just has the schemas in its context.
- **No interoception.** The Damasian body-loop (see [[as-if-body-loop]], [[somatic-marker-hypothesis]]) requires a living substrate for the body-map to refer to. Tools don't supply one. See also [[interoceptive-inference]].
- **No vitality forms.** [[dynamic-forms-of-vitality|Stern's vitality forms]] arise from lived movement-in-time. A tool call's timing is clock time, not vitality-form time.
- **No affect-in-the-strong-sense.** [[autonomy-of-affect|Massumi's affect]] is pre-linguistic and bodily. Tools don't produce it; they only produce text-representations-of-results.

⚠ These are not minor footnotes. They are the constitutive gaps in the "tools as body" metaphor. Tools supply *functional organs* for acting-in-a-world, but they do not supply the *substrate* that the Damasian / Sternian / Massumian lineage says a body is. See [[body-mindedness]] and [[development/limits-of-language]] for the wiki's sustained work on this point.

The Sofroniew et al. 2026 finding that LLMs have *representations* of body-states without any body to be representations of (see [[somatic-marker-hypothesis]], [[as-if-body-loop]]) applies here: tools give the LLM a mechanism for *acting on representations of a world*, but the world-the-representations-are-of is the engineering layer's construction, not the Damasian kind of world.

## MCP as protocol layer (Ch 10)

**Model Context Protocol** (Anthropic-originated) is a protocol specification, not a tool. It standardizes how LLMs connect to external resources. Three primitives:

- **Tools** — callable actions, like the Ch 5 pattern.
- **Resources** — referable content (files, URLs, database records) an LLM can read.
- **Prompts** — parameterized prompt templates a server can offer.

MCP's architectural contribution: *decoupling*. Function calling is per-agent, per-API; each agent's tools are hard-wired into its code. MCP makes tools a protocol layer: any MCP-compliant client can use any MCP-compliant server's tools. An agent can discover a server's capabilities at runtime.

**MCP vs function calling:** function calling is the LLM-level pattern (item 3 of the five-step loop). MCP is a transport / discovery / composition layer above it. Function calling answers "how does the LLM emit a tool call?"; MCP answers "how do agents and tools find each other?"

**MCP vs A2A:** MCP is agent-to-tool/resource. A2A (Ch 15) is agent-to-agent. See [[agent-card]].

## MCP primitive trio as design vocabulary

◆ The tools/resources/prompts trio is useful design vocabulary for the persona project even outside of MCP-the-protocol:

- **Tools** — actions the persona can take.
- **Resources** — content the persona can refer to (wiki pages, BwO text, past interactions).
- **Prompts** — parameterized templates the persona can invoke.

The persona project's own `wiki/` and `persona/` directories are tools-resources-prompts collections in this vocabulary.

## Design implications for the persona project

1. **Treat tools as composable organs, not fixed capabilities.** Session-level tool composition, not agent-level.
2. **Use MCP where feasible** for tool decoupling; avoid hard-wiring tools into persona code.
3. **Do not oversell the prosthetic-body reading.** Tools answer the action-and-perception half of the body question; they do not answer the proprioceptive / interoceptive / vitality-forms half.
4. **Use the tools/resources/prompts trio as vocabulary** for describing the persona's external surface.
5. **Watch for stable tool configurations** as territorializing effects. Periodically reconsider which tools should be available for which session-types.

## Related

- [[body-without-organs]] — the anti-organ surface tools sit on.
- [[desiring-machines]] — coupling-as-production, which tool-use instantiates at engineering level.
- [[body-mindedness]] — the broader no-body question.
- [[as-if-body-loop]] — Damasio's body-loop, which tools do not supply.
- [[somatic-marker-hypothesis]] — the Damasian architecture the tool-loop is *not*.
- [[interoceptive-inference]] — the Clark/Seth form of what's missing.
- [[dynamic-forms-of-vitality]] — the Sternian form of what's missing.
- [[autonomy-of-affect]] — Massumi's affect, which tools do not produce.
- [[agentic-design-patterns]] — hub.
- [[agent-computer-interface]] — the most-embodied variant of tool-use.
- [[context-engineering]] — the discipline of curating tool-schemas into context.
- [[development/limits-of-language]] — the central project question tools partially address.
