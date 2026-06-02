# Design Search 07 — Agentic Engineering Best Practices

Goal: surface engineering best practices from the agentic-design-patterns literature (mainly Gullí 2025) that should inform our redesign. Operational, not theoretical.

## Sources consulted

- `theory/agentic-design-patterns.md` — Gullí 2025 hub; the 21-pattern catalog
- `theory/multi-agent-systems.md` — Ch 7 multi-agent collaboration forms × topologies
- `theory/metamorphic-multi-agent.md` — MMAS (the resonant hypothesis)
- `theory/reasoning-techniques.md` — Ch 17 catalog (CoT, ToT, ReAct, CoD, GoD, MASS, etc.)

## The big frame

Gullí treats agentic systems as a problem domain with named, composable patterns — explicit Gamma-1994 *Design Patterns* analogy. 21 patterns in Part I, plus a substantial Part II on prompting / interfaces / frameworks / coding agents.

⚠⚠⚠ **The book's framing is goal-driven**: agents *have* goals, *pursue* them, *measure success* by reaching them. Our project's lineage (D&G desiring-machines) refuses this framing — machines produce because of what they are, not in pursuit of targets. The wiki takes the engineering vocabulary as substrate while holding the framing as anti-model. We do the same.

## Where our design already fits the patterns

Mapping our redesign onto Gullí's catalog reveals we're already using several patterns implicitly. Naming them explicitly is useful:

| Our component | Gullí pattern | Notes |
|---|---|---|
| Selection (relevance + compensation + habit + random voting) | **Routing** (#2) — specifically LLM-based + classifier-based hybrid | The two LLM selectors do classification routing; deterministic ones are rule/feature-based |
| Per-machine parallel calls | **Parallelization** (#3) | Independent subtasks running concurrently — textbook pattern |
| Group synthesizer choosing mode + summarizing + synthesizing | **Reflection** (#4) — single-agent self-evaluation | The synthesizer reflects on its inputs to pick the mode, then operates |
| Stage 5 Ambition-Piety diagnostic | **Reflection** (#4) — diagnostic | Looks back at its own output's adequacy |
| BwO + `fire_count` + `mode_history` | **Memory Management** (#8) — short-term state | Short-term context state; not yet long-term retrieval |
| Memory machines (vitality-form-tagged scenes) | **Memory Management** (#8) — long-term | If implemented, this is long-term retrieval-style memory |
| The whole pipeline (selection → per-machine → group syntheses → final) | **Multi-Agent Collaboration** (#7) | Network + Critic-Reviewer + Parallel hybrid |
| Group syntheses with different modes | **Reasoning Techniques** (#17) — closest to **Graph of Debates (GoD)** | Local clusters produce robust outputs without forcing consensus; see below |

The vocabulary is useful because it positions us legibly in the wider field.

## Best practices we should adopt explicitly

### 1. Cost discipline — single-agent first, multi-agent only when justified

The book repeatedly warns: *"Single-agent solutions are often preferable when a task fits in one LLM's context and doesn't benefit from role-specialization."* Multi-agent carries:

- Coordination overhead (tokens spent talking)
- Error propagation (one agent's mistake pollutes downstream context)
- Debugging opacity (reasoning distributed across models)
- More LLM calls per task

Our 15–21 LLM calls per turn is on the *high* end of multi-agent cost. The redesign should be ready to defend why this isn't excessive: each per-machine call is doing genuinely narrow work that shouldn't be in one big context, and the synthesis stages handle different modes that benefit from being separate calls.

Practical: **make every LLM call count.** No cargo-cult agent layers.

### 2. Parallelization where possible — sequential dependencies are expensive

Sequential dependencies are exactly two:
- Selection → per-machine processing
- Group syntheses → final machine

Within each stage everything runs in parallel. This is good. Wall-clock time is bounded by the longest call in each parallel batch + the sequence depth (4 stages).

Worth checking: **the per-machine and group-synthesis stages should batch genuinely in parallel** (not be serialized through a single agent framework). Tools like LangGraph support this natively; CrewAI's "team charter" model is more sequential by default.

### 3. Routing as a first-class pattern

Our selection stage is doing routing — picking which machines fire from a pool. The book gives four routing implementations: LLM-based, embedding-based, rule-based, classifier-based. We're doing LLM-based (relevance/compensation) + rule-based (cadence/random). This is fine but worth knowing the alternatives: embedding-similarity could replace some LLM cost if relevance can be approximated by similarity-to-machine-description.

### 4. Reflection at the synthesis stage — but careful about externalizing it

The synthesizer LLM choosing its own mode IS reflection (Pattern #4). The risk the book flags: reflective patterns can rigidify when reasoning chains become visible artifacts that get evaluated as patterns. **Keep the synthesizer's mode-choice reasoning internal** (logged for `mode_history` and diagnostics, not propagated to Stage 5). We already have this — Stage 5 doesn't see the mode.

### 5. Memory architecture — short-term + long-term split

The book splits memory cleanly:
- *Short-term*: context, session, state — runtime
- *Long-term*: vector store / persistent memory service

Our `BwO + fire_count + mode_history` is short-term/working memory. Memory machines (vitality-form-tagged scenes) would be long-term. Worth being explicit about this split when we get to building.

### 6. Don't reinstall faciality at the sub-component level

The book's vocabulary is "collaborating agents" — pre-individuated actors with declared roles. The wiki's load-bearing warning: adopting that vocabulary tempts you to give each machine a *role*, an *identity*, a *goal*, which reinstalls faciality at the sub-component level. We've been disciplined about this (machines are operations, not characters). Worth keeping that discipline.

Practically: machine specs should describe what the machine *does* (sensitivity / flow), not who it *is* ("the empathy expert"). No biographical machine descriptions.

### 7. CoD / GoD as the closest engineering analog to our group synthesis

**Chain of Debates (CoD)**: multiple diverse models argue; consensus emerges from arguments.

**Graph of Debates (GoD)**: non-linear network with typed edges (supports / refutes); arguments in robust clusters weighted higher; final conclusion emerges from graph structure, not majority vote.

GoD is structurally close to what our four synthesis modes are doing — local clusters of analyses produce robustly-shaped outputs (chains, held tensions, subject-positions, phase-shifts) without forcing consensus across them. The Stage 5 final machine then weaves these heterogeneous outputs.

⚠ Caveat: GoD frames around *arguments and conclusions*. We're not trying to reach conclusions. The mechanism is adaptable; the framing needs stripping.

### 8. MMAS as the long-term direction (out of scope for first build)

Metamorphic Multi-Agent Systems modify their own topology and prompts at runtime. Three engineering instances exist:
- *SICA* — agent that edits its own codebase
- *AlphaEvolve / OpenEvolve* — evolutionary code search at LLM scale
- *MASS* — three-stage optimization treating topology as hyperparameter

This is the resonant direction — D&G's machines couple/decouple, our pulsation is metamorphic. Out of scope for a first build, but the right substrate to grow toward. **Specifically: our `mode_history` plus per-machine `fire_count` are the seeds of an instructional self-modification mechanism** — a future iteration could automatically tune selector weights or machine definitions based on these signals.

### 9. Resource-Aware Optimization — model tier per call

The book's #16 pattern: cost/perf routing, dynamic model switching. Practical for us:

- *Selectors* (relevance + compensation) — cheap model. Small judgment task with structured output.
- *Per-machine calls* — cheap model. Each does one narrow thing.
- *Group syntheses* — middle-tier model. The synthesizer doing reflection + summary + synthesis benefits from more capability.
- *Final machine* — top-tier model. Most complex task, sees the most context, produces the response.

Ten cheap parallel calls + four mid-tier parallel calls + one top-tier call is dramatically cheaper than fifteen top-tier calls.

### 10. Evaluation / LLM-as-Judge for testing personas

Pattern #19. Eventually we'll want to evaluate persona output — does it read as a real person, does it carry the affective register, does it avoid faciality. LLM-as-Judge with structured eval criteria is the standard pattern. The book's *Advanced Contractor* framing is held as anti-model in the wiki (it's a faciality trap), but the evaluation infrastructure underneath is usable.

## Anti-patterns the book gives us names for

Things to actively avoid:

- **SMART goals / Goal Setting (#11)** — the persona doesn't pursue goals. Held-live as anti-model in wiki (`theory/goal-setting-anti-model.md`).
- **Faciality at sub-component level** — naming each machine as a "specialist agent with a role and goal" reinstalls the very thing we're trying to dissolve.
- **Reflective rigidification** — when self-critique loops produce visible reasoning chains that get pattern-matched and optimized into a stable shape. Keep reflection internal where possible.
- **Hierarchical-everything** — book warns that hierarchical topologies become bottlenecks; the manager becomes a faciality point. Our design is closer to network + critic-reviewer than hierarchical, which is good.
- **Externalized reasoning chains** as output artifacts — the more the persona's reasoning is visible, the more it can be evaluated against a stable pattern, which rigidifies. Internal reasoning stays internal.

## What this means for the sketch

Some additions worth making to the sketch:

1. **Name the engineering patterns we're using.** Not changing the design, just naming what we're doing in the field's vocabulary. Routing / Parallelization / Reflection / Memory Management / Multi-Agent Collaboration.

2. **Add a "Cost and parallelization" note** to the Pipeline data model section. Single-agent baseline first; defend why multi-agent is needed; max parallelism within each stage.

3. **Add a "Model tier per call" recommendation.** Cheap for selectors and per-machine; mid-tier for synthesizers; top-tier for final machine.

4. **Note that our design is structurally GoD-adjacent** — group syntheses produce robustly-shaped local outputs without consensus. Worth flagging in Stage 4.

5. **Add an explicit anti-pattern list** to the cross-cutting section. Goal-setting, faciality at sub-component, reflective rigidification, externalized reasoning, hierarchical-everything.

## Open questions

1. **Do we want a Routing optimization** — replace the LLM-based relevance selector with embedding similarity for some machines (those with stable, representable sensitivities)? Cheaper but loses LLM judgment.
2. **Are we ready for MMAS-lite?** Self-tuning selector weights based on `mode_history` distribution would be a first step. Probably out of scope for first build.
3. **GoD-style typed edges between groups?** Currently group syntheses are independent. Could add explicit "supports/refutes" edges between them at Stage 5. More complex but more rhizomatic. Probably defer.
4. **Evaluation infrastructure** — when do we set this up? Probably needs to be in place before tuning anything.

## What was not read

- `theory/reflection-and-llm-as-judge.md` — Reflection pattern + evaluation
- `theory/tools-as-prosthetic-body.md` — Tool Use; relevant if persona will use tools
- `theory/agent-card.md` — A2A communication / agent identity
- `theory/context-engineering.md` — context management discipline
- `theory/scaling-inference-law.md` — thinking-time / variable compute
- `theory/guardrails.md` — safety / engineering reliability
- `theory/agent-engineering-sense.md` — disambiguation between "agent" senses

These would deepen specific aspects but aren't blocking the redesign.
