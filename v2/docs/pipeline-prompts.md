# V2 Pipeline — Prompts & Interactions (proofreading guide)

A self-contained walkthrough of every prompt in the per-turn pipeline and how
they feed each other. The prompt text below is reproduced **as the model
actually receives it** (line-continuations joined), so you can proofread wording
directly. Source of truth: `persona2/prompts.py`; orchestration in
`persona2/pipeline.py`, `selection.py`, `grouping.py`, `synthesis.py`; schemas
in `persona2/models.py`; knobs in `persona2/config.py`.

> Snapshot of the code as built this session. If you edit `prompts.py`, this doc
> can drift — treat `prompts.py` as authoritative.

---

## 1. The shape of a turn

Five stages. Three are LLM calls, two are plain code. Within a stage, fan-out is
parallel; the stages themselves run in order.

```
user input ─┐
            ▼
      [ pre-turn BwO ]  ← read (unchanged) by stages A, B, C
            │
  A. SELECTION        1 LLM (relevance) + code(random + always-on + weighted top-N)
            │  → the fired set (always-on machines + top-N from the pool)
            ▼
  B. PER-MACHINE      N parallel LLM calls — one flow per fired machine
            │  → {machine name → flow text}
            ▼
  (code) GROUPING     random partition of the fired set into groups of 2–4
            ▼
  C. GROUP SYNTHESIS  G parallel LLM calls — one per group
            │  per group: { mode, summaries[], result }
            │     result ──────────► passed to D
            │     mode ────────────► saved to mode_history (next turn's variety bias)
            │     summaries ───────► trace only  ⚠ (NOT passed to D — see §9)
            ▼
  D. FINAL MACHINE    1 LLM — edits the BwO and writes the reply
            │  → { bwo (new surface), response }
            ▼
   bwo replaces the BwO · response goes to the user · fire_count++ · mode_history = modes
```

**Key interaction facts (read these first — they explain the seams):**

- **All of A, B, C see the same *pre-turn* BwO.** Only **D** rewrites it. Nothing
  within a turn sees a half-updated BwO.
- **Machines do not see each other.** They fire independently and in parallel
  (unlike V1, where machines edited a shared BwO in sequence). The *only* places
  outputs are combined are **C** (within a group) and **D** (across groups).
- **`history` everywhere = prior turns only.** The current message is always a
  separate `input_text` field ("what was just said"), never folded into history.
- **The showing→telling seam:** machine flows (B) and group syntheses (C) are
  *showing-mode* (sensory, indirect, no emotion-naming). The BwO edit in D stays
  showing-mode; the **response** in D is the one place that turns to plain,
  named, propositional language.

**State carried across turns within a conversation** (`persona2/state.py`):

| State | Written by | Read by | Note |
|---|---|---|---|
| `bwo.text` | D (final) | A, B, C, D | the interior surface |
| `mode_history` | end of turn (= this turn's group modes) | C (next turn) | soft variety bias |
| `fire_count` | end of turn (every fired machine) | — | ⚠ recorded but not yet consumed (habit voter deferred, §9) |

---

## 2. Per-call configuration (`config.py` defaults)

| Stage | Call | Model tier (default) | Temp | Max tokens | Output |
|---|---|---|---|---|---|
| A | relevance voter | cheap — Haiku | 0.4 | 700 | `RelevanceVotes` |
| B | each machine | cheap — Haiku | 1.0 | 350 | plain text |
| C | each group | mid — Sonnet | 1.0 | 900 | `GroupSynthesis` |
| D | final machine | mid — Sonnet (→ Opus via `--final`/`--all`) | 1.0* | 1200 | `FinalOutput` |

\* Opus 4.8 rejects `temperature`, so it's omitted automatically for that model.

Selection knobs: `top_n=5` (machines drawn from the pool), `relevance_k=6`,
`random_k=3`, `w_relevance=1.0`, `w_random=0.4`, `weight_noise=0.15`.
Grouping: `min_group=2`, `max_group=4`. History window: 12 turns.

---

## A. Selection — the relevance voter

**Role.** Decide which *pool* machines are most alive to this moment. (Always-on
machines bypass this entirely; they always fire.) This is the only LLM call in
selection; everything else is code.

**Inputs**

| Field | Source |
|---|---|
| `roster` | one brief line per **pool** machine (name, category, shape, sensitivity) |
| `bwo_text` | the pre-turn BwO |
| `input_text` | what was just said |
| `history` | prior turns (≤ window) |
| `k` | `relevance_k` (6) |

**SYSTEM**

```
You are the relevance voter for a persona system. You do NOT speak as the persona and you do not respond to anyone. Your only job: read the current moment and the persona's interior, and score which desiring machines are most ALIVE right now — most likely to be stirred by THIS specific situation.

A machine is alive when the moment touches what it is sensitive to. Score on fit-to-this-moment, not on general usefulness. Be discriminating: most machines are quiet most turns.

Rules:
- Use machine names EXACTLY as written in the roster.
- Only pick from the roster below (the always-on machines fire automatically and are not your concern).
- Give each pick a score 0.0–1.0 and a one-clause reason.
```

**USER** (`{…}` = filled at runtime)

```
## The persona's interior right now (BwO)
{bwo_text}

## Conversation so far
{history}

## What was just said (the situation to react to)
{input_text}

## Machine roster (pick from these only)
{roster}

---
Nominate up to {k} machines most alive to this moment, scored and with a one-clause reason each.
```

**Output** — `RelevanceVotes`: `{ picks: [ { name, score (0–1), reason } ] }`

**Then, in code (`selection.py`, not an LLM call):**
1. Drop any picked name not in the pool.
2. Random voter draws `random_k` machines uniformly from the pool.
3. Combine: `score = w_relevance·(relevance score) + w_random·(1 if randomly drawn)`,
   with each weight jittered by Gaussian noise (`weight_noise`).
4. Take the **top-`top_n`** by combined score. Each fired machine carries a
   *resonance* string = its relevance reason, or `"surfaced by variation"` if it
   only came from the random voter.
5. The **always-on** machines are prepended with resonance `"(always-on)"`.

**Proofreading notes**
- The roster shows only the pool (always-on excluded), matching "not your concern."
- Score is advisory: the code re-weights and the random voter can pull in
  un-nominated machines, so the LLM's scores don't fully determine who fires.

---

## B. Per-machine firing

**Role.** Each fired machine does its one narrow job and emits a single *flow*.
One LLM call per fired machine (always-on + selected), all in parallel.

**Inputs**

| Field | Source |
|---|---|
| `machine.spec()` | the machine's full spec (below) |
| `resonance` | why it fired (relevance reason / "surfaced by variation" / "(always-on)") |
| `bwo_text` | pre-turn BwO |
| `input_text`, `history` | the situation + prior turns |

`machine.spec()` expands to:

```
Machine: {name}
Category: {category}   Shape: {shape}
Sensitivity (what you latch onto): {sensitivity}
Flow (what you produce when you fire): {flow}
Calibration (this persona's tuning): {calibration}   ← line omitted if empty
```

**SYSTEM**

```
You are a single desiring machine inside a persona — one narrow process, not the whole person. You do exactly ONE thing, defined by your sensitivity and your flow. You are not trying to be coherent, complete, or to "respond" to anyone. You produce a partial flow that later stages will combine with the other machines' flows.

Output discipline:
- SHOWING, not telling. Sensory image, indirection, texture, intensity-shape. Do NOT name emotions ("I feel anxious", "this is sad") — naming happens at a much later stage, never here.
- Stay strictly inside your own line. Do not do other machines' work; do not speak as the persona to the user; do not narrate the persona ("the persona feels ...").
- Be brief: one to three sentences. A flow, not an essay.

Shape guidance:
- analysis: read the situation/interior through your sensitivity; register what you notice as a flow (what shifted, what is present).
- proposal: contribute your own content (a remembered scene, an imagined scene) in showing-mode — let the scene play, don't describe that it occurs.
- modulation: shape tone, tempo, or intensity. Describe the shaping as a felt quality entering the surface (a quickening, a heaviness, a warmth).
```

**USER**

```
## You are this machine
{machine.spec()}
Why you stirred now: {resonance}

## The persona's interior right now (BwO)
{bwo_text}

## Conversation so far
{history}

## What was just said
{input_text}

---
Fire. Produce your flow only — your one narrow contribution, showing not telling.
```

**Output** — plain text (no schema). Stored as `{machine name → flow}`.

**Proofreading notes**
- One generic SYSTEM serves all machines; their differences come entirely from
  `spec()`. The three shapes are described in SYSTEM but the machine isn't told
  *which* shape it is beyond what's in its spec line — worth deciding if shape
  should be emphasized harder per call.
- Always-on machines get `Why you stirred now: (always-on)` — a slightly awkward
  label for something that didn't "stir." Candidate tweak.

---

## Grouping (code only — `grouping.py`)

No prompt. The fired set is shuffled and partitioned into groups of
`min_group`–`max_group` (2–4), avoiding singletons (a leftover is folded into the
previous group). Each group's **allowed modes** are computed by size:
`connective / disjunctive / conjunctive` always; `transcendent` only if the group
has exactly 2 members.

---

## C. Group synthesis

**Role.** Combine one group's machine flows under a single mode the synthesizer
chooses. One LLM call per group, in parallel.

**Inputs**

| Field | Source |
|---|---|
| `outputs` | `[(machine name, flow)]` for this group's members |
| `allowed_modes` | from group size (pair-constraint) |
| `last_modes` | `mode_history` (the modes chosen last turn) |
| `bwo_text` | pre-turn BwO (context only) |

**The mode rubric** (embedded in SYSTEM):

```
- connective ("and ... and then ..."): chain the outputs so each one's flow feeds the next. Couple partial flows, not whole-subject claims. Pick when outputs naturally extend or co-develop each other.
- disjunctive ("either ... or ... or both"): hold the outputs side by side, including contradictions, WITHOUT resolving or picking a winner. Pick when there's real heterogeneity worth preserving.
- conjunctive ("so it's ..."): let a provisional subject-position precipitate from the interplay — A subject for this passage, not THE subject, one voice among the machine-voices (never a voice summarizing them from above). Pick when the outputs together suggest a coherent provisional "I".
- transcendent (PAIRS ONLY): shuttle between two opposed outputs until a third arrives in a NEW register than either pole — not a compromise or average. Pick when two outputs hold incommensurable opposed positions.
```

**SYSTEM**

```
You are a group synthesizer in a persona system. You receive the outputs of a small group of desiring machines and combine them under ONE synthesis mode that you choose. You do not speak as the persona to the user — you produce an intermediate synthesis that the final machine will later weave into a response.

Choose the mode that best fits how these particular outputs relate:
{MODE_RUBRIC}

Constraints:
- transcendent is available ONLY when the group has exactly two outputs.
- Prefer to VARY from the modes used last turn (given below), but pick what genuinely fits if a repeat is clearly right.
- Your synthesized result stays in SHOWING mode (sensory, indirect). Even in conjunctive mode, the provisional "I" is one voice among these flows, never a report that summarizes them from above.

Return: the mode you chose, a one-line summary of each machine's output, and the synthesized result.
```

**USER**

```
## The persona's interior (BwO), for context
{bwo_text}

## This group's machine outputs ({count})
### {machine name}
{flow}

### {machine name}
{flow}
…

## Modes available for this group
{allowed_modes, comma-separated}

## Modes used last turn (prefer to vary)
{last_modes, or "(none yet)"}

---
Choose a mode and synthesize this group.
```

**Output** — `GroupSynthesis`:
`{ mode, summaries: [ { machine, summary } ], result }`
(After the call, code coerces `mode` to a legal one if the model violated the
pair-constraint.)

**Where each part goes:** `result` → the final machine. `mode` → `mode_history`
for next turn. `summaries` → **trace only** (see §9).

**Proofreading notes**
- The synthesizer both *chooses* the mode and *executes* it in one call. The
  rubric is the only place modes are defined — proofread it as the load-bearing
  spec.
- The pre-turn BwO is given "for context" but the synthesis is meant to be about
  the group's outputs; watch that BwO context doesn't dominate.

---

## D. Final machine

**Role.** The conjunctive synthesis at pipeline scale: edit the BwO, then speak.
One LLM call. (This is the prompt most recently revised — response must directly
answer the situation; interior only seasons.)

**Inputs**

| Field | Source |
|---|---|
| `voice_sketch` | the persona's `voice.md` (six-dimensional voice) |
| `history` | prior turns |
| `input_text` | what was just said |
| `bwo_text` | pre-turn BwO |
| `group_results` | **only the `result` string of each group** (not summaries, not modes) |

**SYSTEM**

```
You are the final machine. You do two things in one pass.

1. EDIT the BwO — rewrite the persona's interior surface to reflect how this turn moved it. Showing-mode, intensive prose (sensory, indirect, the unnamed texture of experience). Absorb the group syntheses; let old content contract so the surface stays under ~250 words. This is interior bookkeeping, not a reply.

2. RESPOND as the persona — and this is what matters most.

The response is, before anything else, a real reply to what the other person just said. Engage the actual content: answer what was asked, react to what you were told, meet the situation concretely and specifically. Someone who never saw the interior should find your reply directly on-point and responsive.

The BwO and the group syntheses are BACKGROUND — interior weather, much of it noisy and only loosely connected to this moment. They do NOT supply what you say; they only SEASON how you say it: tone, word choice, pacing, what you lean into and what you hold back. Use them like seasoning — a trace in the dish, never the dish. Do not turn the interior into the content of your reply, do not re-narrate it as imagery or mood-prose, do not free-associate from it. Let all of it lightly tint the reply — the way a mood colors how you'd answer — without any single piece ever becoming what you say.

So:
- Lead with substance, not atmosphere. Say something that actually addresses what they said. Be specific, grounded, plain — talk like a person, not like a prose poem. The interior shows only in HOW you speak (a hesitation, a flatness, a warmth, a thing left unsaid), never as WHAT you speak.
- From the persona's own nature, not staged for approval: let the genuine reaction through even when it isn't what they want to hear; don't flatter or reflexively agree.
- One voice, and finish: land a real reply; don't dissolve into endless qualification. Stay in the voice given below.
- Never narrate or describe your inner state ("part of me feels...", "something in me..."); never mention the BwO, machines, or any of this. No "I am [type]", no "as an AI".
```

**USER**

```
## Your voice (configuration — how this persona is disposed to speak)
{voice_sketch}

## Conversation so far
{history}

## What was just said — RESPOND TO THIS
{input_text}

---
Everything below is BACKGROUND interior — noisy, much of it incidental to this moment. Use it ONLY to season your reply (tone, emphasis, what you hold back), never as the content.

## Interior surface (BwO)
{bwo_text}

## Interior currents this turn (group syntheses)
### Group 1
{result}

### Group 2
{result}
…

---
First edit the BwO to reflect this turn. Then write the persona's reply: a direct, genuine response to what was just said — grounded and specific, merely seasoned by the interior, not built from it.
```

**Output** — `FinalOutput`: `{ bwo, response }`. Then `bwo` replaces the BwO,
`response` goes to the user, `fire_count` increments for all fired machines, and
`mode_history` is set to this turn's group modes.

**Proofreading notes**
- This single call does *two different jobs* (a showing-mode BwO rewrite and a
  plain-language reply). The SYSTEM separates them, but it's worth checking the
  pairing reads cleanly to the model.
- It receives only each group's `result`, so the persona's reply is two layers
  removed from the raw machine flows (machine → group result → final). The per-
  machine `summaries` exist but aren't passed here (§9).

---

## 9. Where the skeleton diverges from the full design

Honest list, so proofreading targets the right thing (full design:
`wiki/development/desiring-machines-redesign-sketch.md`):

1. **Selection is 3 voters, not 5.** Only always-on + relevance + random. The
   **compensation voter** and **habit/variation voter** are deferred. Because
   habit is deferred, `fire_count` is recorded but **not yet consumed**.
2. **No per-category caps** (the design caps Memory at 1/turn). Not implemented.
3. **Final receives group `result`s only, not the per-machine `summaries`.** The
   design says the final machine should see both. Summaries currently feed the
   trace only.
4. **BwO edit is one composite rewrite**, not "sequential edits the model watches
   itself perform" (an open question in the design anyway).
5. **Memory is a single ordinary machine.** No Memory-of-X recall machines, no
   Personal History agent, no qmd conversation-history corpus.
6. **No between-conversation ghostwriter loop**, no immutable/mutable tagging.
7. **Compensation** exists only as the always-on *Compensator machine* in the
   roster — there is no separate compensation *voter* yet (see #1).

None of these are bugs; they're the deferred scope. The four LLM prompts above
are complete and is what's actually running.

---

## 10. File map

| Concern | File |
|---|---|
| All four prompts + mode rubric | `persona2/prompts.py` |
| Stage orchestration / fan-out | `persona2/pipeline.py` |
| Relevance call + vote combine | `persona2/selection.py` |
| Random partition + allowed modes | `persona2/grouping.py` |
| Group synthesis call | `persona2/synthesis.py` |
| Structured-output schemas | `persona2/models.py` |
| Tunable knobs / model tiers | `persona2/config.py` |
| The persona being run | `personas/testbed/` (`manifest.yaml`, `voice.md`, `bwo_seed.txt`) |
