#!/usr/bin/env python3
"""Build a self-contained HTML viewer for a run of firing traces.

    python viewer/build_viewer.py traces/effusive-20260601-170224

Writes viewer/<run-name>.html — one file, no server, no dependencies beyond
PyYAML (already a project dep). Open it in a browser.

The viewer shows every field the trace carries: the full machine roster with
selection scores, each machine's flow, the random grouping and its syntheses,
a word-level diff of the interior surface, the reply, a reconstructed timeline,
and the raw prompt/response of all thirteen model calls.
"""

from __future__ import annotations

import difflib
import html
import json
import re
import sys
from pathlib import Path

import yaml

# Eleven hues, assigned by roster position. Distinguishable, all legible on paper.
PALETTE = [
    "#B4522A", "#2E7D8C", "#7B6A1F", "#5B4B8A", "#3F7A42", "#A03A5E",
    "#26666B", "#8A5A20", "#4A5FA5", "#6E7A2A", "#8C3F70",
]

STAGE_ORDER = ["selection", "machine", "synthesis", "final"]


# --- loading -----------------------------------------------------------------

def load_run(run_dir: Path) -> tuple[list[dict], dict, str]:
    turns = [json.loads(p.read_text()) for p in sorted(run_dir.glob("turn-*.json"))]
    if not turns:
        sys.exit(f"no turn-*.json files in {run_dir}")

    persona_name = run_dir.name.rsplit("-", 2)[0]
    manifest_path = run_dir.parent.parent / "personas" / persona_name / "manifest.yaml"
    manifest = yaml.safe_load(manifest_path.read_text()) if manifest_path.exists() else {"machines": []}
    return turns, manifest, persona_name


def roster_of(manifest: dict) -> list[dict]:
    out = []
    for i, m in enumerate(manifest.get("machines", [])):
        out.append({
            "name": m["name"],
            "category": m.get("category", ""),
            "shape": m.get("shape", ""),
            "always_on": bool(m.get("always_on", False)),
            "sensitivity": (m.get("sensitivity") or "").strip(),
            "flow": (m.get("flow") or "").strip(),
            "calibration": (m.get("calibration") or "").strip(),
            "color": PALETTE[i % len(PALETTE)],
        })
    return out


# --- word-level diff ---------------------------------------------------------

def word_diff(before: str, after: str) -> str:
    """Word-level diff rendered as spans. Deletions and insertions both shown."""
    a = re.findall(r"\S+\s*", before)
    b = re.findall(r"\S+\s*", after)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    parts = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            parts.append(html.escape("".join(b[j1:j2])))
        else:
            if tag in ("replace", "delete"):
                parts.append(f'<del>{html.escape("".join(a[i1:i2]))}</del>')
            if tag in ("replace", "insert"):
                parts.append(f'<ins>{html.escape("".join(b[j1:j2]))}</ins>')
    return "".join(parts)


def diff_counts(before: str, after: str) -> tuple[int, int]:
    a = re.findall(r"\S+", before)
    b = re.findall(r"\S+", after)
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    added = removed = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("replace", "delete"):
            removed += i2 - i1
        if tag in ("replace", "insert"):
            added += j2 - j1
    return added, removed


# --- timeline ----------------------------------------------------------------

def timeline(calls: list[dict]) -> tuple[list[dict], float]:
    """Reconstruct a gantt from stage order plus each call's measured latency.

    Start times are inferred, not recorded: stages run in sequence, and every
    call within a stage starts when that stage starts. Latencies are measured.
    """
    by_stage: dict[str, list[dict]] = {s: [] for s in STAGE_ORDER}
    for c in calls:
        by_stage.setdefault(c["stage"], []).append(c)

    bars, cursor = [], 0.0
    for stage in STAGE_ORDER:
        group = by_stage.get(stage, [])
        if not group:
            continue
        for c in group:
            bars.append({
                "stage": stage,
                "label": c["label"],
                "model": c["model"].replace("claude-", ""),
                "start": cursor,
                "dur": float(c.get("latency_s") or 0.0),
            })
        cursor += max((float(c.get("latency_s") or 0.0) for c in group), default=0.0)
    return bars, cursor


# --- html helpers ------------------------------------------------------------

def esc(s: str) -> str:
    return html.escape(s or "")


def para(s: str) -> str:
    """Preserve paragraph breaks without a markdown dependency."""
    blocks = [b.strip() for b in re.split(r"\n\s*\n", (s or "").strip()) if b.strip()]
    return "".join(f"<p>{esc(b)}</p>" for b in blocks) or "<p class='muted'>(empty)</p>"


CSS = """
*{box-sizing:border-box}
body{margin:0;font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,sans-serif;
  color:#1c2024;background:#f7f6f3}
.wrap{max-width:1180px;margin:0 auto;padding:24px 20px 80px}
h1{font-size:19px;margin:0 0 2px}
h2{font-size:12px;letter-spacing:.09em;text-transform:uppercase;color:#6b7280;
  margin:34px 0 10px;padding-bottom:6px;border-bottom:1px solid #e2ded4}
h2 .note{float:right;text-transform:none;letter-spacing:0;font-weight:400;color:#9aa1ab}
.mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px}
.muted{color:#8b929b}
.sub{color:#6b7280;font-size:13px;margin:0 0 18px}
header{border-bottom:2px solid #1c2024;padding-bottom:12px;margin-bottom:6px}

/* turn tabs */
nav{display:flex;gap:6px;flex-wrap:wrap;margin:14px 0 0}
nav button{font:inherit;font-size:13px;padding:5px 13px;border:1px solid #d5d0c4;
  background:#fff;border-radius:3px;cursor:pointer}
nav button[aria-selected=true]{background:#1c2024;color:#fff;border-color:#1c2024}
.turn[hidden]{display:none}

/* card + panel */
.card{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:14px 16px}
.said{background:#fff;border-left:3px solid #1c2024;padding:12px 16px;border-radius:0 4px 4px 0}
.said p,.reply p{margin:0 0 .6em}
.said p:last-child,.reply p:last-child{margin:0}
.reply{background:#fff;border:2px solid #1c2024;border-radius:4px;padding:16px 18px;font-size:16px}

/* roster table */
table{width:100%;border-collapse:collapse;font-size:13px;background:#fff;
  border:1px solid #e2ded4;border-radius:4px;overflow:hidden}
th{text-align:left;font-size:11px;letter-spacing:.06em;text-transform:uppercase;
  color:#6b7280;font-weight:600;padding:8px 10px;border-bottom:1px solid #e2ded4;background:#faf9f6}
td{padding:8px 10px;border-bottom:1px solid #f0ede6;vertical-align:top}
tr:last-child td{border-bottom:none}
tr.quiet{color:#a8aeb6;background:#fbfaf8}
tr.quiet .swatch{opacity:.3}
.swatch{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:7px;
  vertical-align:baseline}
.tag{display:inline-block;font-size:10px;letter-spacing:.05em;text-transform:uppercase;
  padding:1px 6px;border-radius:2px;background:#eeeae0;color:#5c6672;white-space:nowrap}
.tag.on{background:#1c2024;color:#fff}
.num{text-align:right;font-family:ui-monospace,Menlo,monospace;font-size:12px;white-space:nowrap}

/* machine grid */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(268px,1fr));gap:12px}
.m{background:#fff;border:1px solid #e2ded4;border-top:3px solid;border-radius:4px;padding:12px 14px}
.m h3{margin:0;font-size:14px;display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.m .why{font-size:12px;color:#6b7280;margin:6px 0 9px;padding-left:9px;border-left:2px solid #eae6dc}
.m .out p{margin:0 0 .55em}
.m .out p:last-child{margin:0}

/* wires: machines -> groups, drawn from measured layout */
.flow{position:relative}
.wires{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:1}
.wires path{fill:none;stroke-width:1.6;opacity:.45}
.flow .grid,.flow .groups,.flow h2{position:relative;z-index:2}
.gap{height:46px}

/* the final call */
.final{display:grid;grid-template-columns:1fr auto 1fr;gap:14px;align-items:center}
.io{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:11px 13px}
.io h4{margin:0 0 7px;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#8b929b}
.io ul{margin:0;padding:0;list-style:none;font-size:13px}
.io li{padding:4px 0;border-bottom:1px solid #f4f1ea;display:flex;gap:7px;align-items:baseline}
.io li:last-child{border-bottom:none}
.io .k{font-family:ui-monospace,Menlo,monospace;font-size:11px;color:#8b929b;white-space:nowrap}
.node{background:#1c2024;color:#fff;border-radius:4px;padding:14px 16px;text-align:center;
  font-size:13px;white-space:nowrap}
.node span{display:block;font-family:ui-monospace,Menlo,monospace;font-size:10.5px;
  color:#9aa1ab;margin-top:3px}

/* edit log */
.edits{width:100%;border-collapse:collapse;font-size:13px;background:#fff;
  border:1px solid #e2ded4;border-radius:4px;overflow:hidden;margin-top:12px}
.edits td{padding:9px 11px;border-bottom:1px solid #f0ede6;vertical-align:top}
.edits tr:last-child td{border-bottom:none}
.prov{display:inline-block;font-size:11px;padding:2px 8px;border-radius:10px;
  background:#eeeae0;color:#3f4855;white-space:nowrap;margin:0 4px 3px 0}
.prov.grp{background:#1c2024;color:#fff}
.absent{background:#fff;border:1px dashed #d5d0c4;border-radius:4px;padding:12px 14px;
  font-size:13px;color:#6b7280}

/* groups */
.groups{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:12px}
.g{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:12px 14px}
.g header{border:none;margin:0 0 9px;padding:0;display:flex;align-items:center;
  justify-content:space-between;gap:8px;flex-wrap:wrap}
.chips{display:flex;gap:5px;flex-wrap:wrap}
.chip{font-size:11px;padding:2px 8px;border-radius:10px;color:#fff;white-space:nowrap}
.mode{font-size:11px;letter-spacing:.06em;text-transform:uppercase;padding:2px 8px;
  border:1px solid #1c2024;border-radius:2px}
.sums{margin:0 0 10px;padding:0;list-style:none;font-size:12px;color:#4b5563}
.sums li{padding:3px 0 3px 9px;border-left:2px solid;margin-bottom:2px}
.res{border-top:1px solid #f0ede6;padding-top:9px}
.res p{margin:0 0 .55em}.res p:last-child{margin:0}

/* diff */
.diff{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:14px 16px;line-height:1.7}
ins{background:#dcefdc;text-decoration:none;box-shadow:inset 0 -1px 0 #8dbf8d}
del{background:#f6dcdc;color:#8a5252}
.legend{font-size:12px;color:#6b7280;margin:8px 0 0}
.legend b{font-weight:400;padding:1px 5px;border-radius:2px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}

/* timeline */
.tl{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:12px 14px}
.row{display:grid;grid-template-columns:150px 1fr 52px;gap:10px;align-items:center;
  font-size:12px;padding:2px 0}
.track{background:#f2efe8;border-radius:2px;height:15px;position:relative}
.bar{position:absolute;height:100%;border-radius:2px;background:#1c2024;opacity:.82}
.stagerule{grid-column:1/-1;font-size:10px;letter-spacing:.08em;text-transform:uppercase;
  color:#9aa1ab;margin:7px 0 1px}

/* calls */
details{background:#fff;border:1px solid #e2ded4;border-radius:4px;margin-bottom:7px}
summary{cursor:pointer;padding:9px 13px;font-size:13px;display:flex;gap:10px;align-items:baseline}
summary::-webkit-details-marker{display:none}
summary:before{content:"›";display:inline-block;width:9px;color:#9aa1ab}
details[open] summary:before{transform:rotate(90deg)}
details[open] summary{border-bottom:1px solid #f0ede6}
.calltxt{padding:0 13px 13px}
pre{white-space:pre-wrap;word-break:break-word;font-family:ui-monospace,Menlo,monospace;
  font-size:11.5px;line-height:1.5;background:#faf9f6;border:1px solid #f0ede6;
  border-radius:3px;padding:10px;margin:8px 0 0;max-height:340px;overflow:auto}
.calltxt h4{margin:12px 0 0;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#8b929b}
.totals{font-size:12px;color:#6b7280;margin-top:10px}
@media(max-width:720px){.cols,.grid,.groups{grid-template-columns:1fr}
  .row{grid-template-columns:110px 1fr 46px}}
"""

JS = """
// Wires from each machine card to the group that consumed it. The edge is real:
// grouping.partition() put that machine in that group, and the group's synthesis
// call received its output. Geometry is measured after layout, so this survives
// reflow and needs no fixed positions.
function drawWires(flow) {
  const svg = flow.querySelector('.wires');
  const base = flow.getBoundingClientRect();
  svg.setAttribute('viewBox', `0 0 ${base.width} ${base.height}`);
  const cards = {};
  flow.querySelectorAll('[data-m]').forEach(el => cards[el.dataset.m] = el);
  let d = '';
  flow.querySelectorAll('[data-members]').forEach(g => {
    const gb = g.getBoundingClientRect();
    g.dataset.members.split('|').forEach(name => {
      const card = cards[name];
      if (!card) return;
      const cb = card.getBoundingClientRect();
      const x1 = cb.left + cb.width / 2 - base.left, y1 = cb.bottom - base.top;
      const x2 = gb.left + gb.width / 2 - base.left, y2 = gb.top - base.top;
      const mid = y1 + (y2 - y1) / 2;
      d += `<path d="M${x1} ${y1} C${x1} ${mid}, ${x2} ${mid}, ${x2} ${y2}"
             stroke="${card.dataset.color}"/>`;
    });
  });
  svg.innerHTML = d;
}
function redraw() { document.querySelectorAll('.turn:not([hidden]) .flow').forEach(drawWires); }

// Turn tabs. Plain show/hide — no animation, so this works with Reduce Motion on.
document.querySelectorAll('nav button').forEach(b => b.addEventListener('click', () => {
  document.querySelectorAll('nav button').forEach(x => x.setAttribute('aria-selected', x === b));
  document.querySelectorAll('.turn').forEach(t => t.hidden = t.dataset.turn !== b.dataset.turn);
  window.scrollTo(0, 0);
  redraw();
}));
addEventListener('resize', redraw);
addEventListener('load', redraw);
redraw();
"""


# --- rendering ---------------------------------------------------------------

def render_selection(turn: dict, roster: list[dict]) -> str:
    reasons = {n: (s, r) for n, s, r in turn["relevance_picks"]}
    fired = {n: res for n, _, res in turn["fired"]}
    shapes = {n: sh for n, sh, _ in turn["fired"]}
    randoms = set(turn["random_picks"])
    scores = turn["selection_scores"]

    rows = []
    # Fired first, in firing order; then everything that stayed quiet.
    order = [m for n, _, _ in turn["fired"] for m in roster if m["name"] == n]
    order += [m for m in roster if m["name"] not in fired]

    for m in order:
        n = m["name"]
        did = n in fired
        rel = reasons.get(n)
        why = fired.get(n, "") if did else (rel[1] if rel else "")
        rows.append(f"""<tr class="{'' if did else 'quiet'}">
  <td><span class="swatch" style="background:{m['color']}"></span>{esc(n)}</td>
  <td><span class="tag{' on' if m['always_on'] else ''}">{'always-on' if m['always_on'] else esc(m['category'])}</span></td>
  <td class="mono">{esc(m['shape'] or shapes.get(n, ''))}</td>
  <td class="num">{f'{rel[0]:.2f}' if rel else '<span class="muted">—</span>'}</td>
  <td class="num">{'✓' if n in randoms else '<span class="muted">—</span>'}</td>
  <td class="num">{f'{scores[n]:.2f}' if n in scores else '<span class="muted">—</span>'}</td>
  <td class="num">{'<b>fired</b>' if did else '<span class="muted">quiet</span>'}</td>
  <td>{esc(why) or '<span class="muted">not nominated</span>'}</td>
</tr>""")

    n_fire, n_pool = len(turn["fired"]), len(roster)
    return f"""<h2>Selection <span class="note">{n_fire} of {n_pool} machines fired ·
  always-on bypass the vote · combined score = relevance + random, plus noise</span></h2>
<table><thead><tr>
  <th>Machine</th><th>Category</th><th>Shape</th><th>Relev.</th><th>Rand.</th>
  <th>Score</th><th></th><th>Why it fired, or why it was nominated</th>
</tr></thead><tbody>{''.join(rows)}</tbody></table>"""


def render_machines(turn: dict, colors: dict[str, str]) -> str:
    cards = []
    for name, shape, why in turn["fired"]:
        out = turn["machine_outputs"].get(name, "")
        c = colors.get(name, "#1c2024")
        cards.append(f"""<div class="m" data-m="{esc(name)}" data-color="{c}"
     style="border-top-color:{c}">
  <h3>{esc(name)}<span class="mono muted">{esc(shape)}</span></h3>
  <div class="why">{esc(why)}</div>
  <div class="out">{para(out)}</div>
</div>""")
    return f"""<h2>Machines fire <span class="note">in parallel · none can see the others ·
  each reads only the pre-turn interior</span></h2>
<div class="grid">{''.join(cards)}</div>"""


def render_groups(turn: dict, colors: dict[str, str]) -> str:
    cards = []
    for i, g in enumerate(turn["groups"]):
        chips = "".join(
            f'<span class="chip" style="background:{colors.get(m, "#1c2024")}">{esc(m)}</span>'
            for m in g["members"]
        )
        sums = "".join(
            f'<li style="border-left-color:{colors.get(mn, "#ccc")}"><b>{esc(mn)}</b> — {esc(s)}</li>'
            for mn, s in (g.get("summaries") or [])
        )
        sums_block = f'<ul class="sums">{sums}</ul>' if sums else ""
        think = (g.get("thinking") or "").strip()
        think_block = (
            f'<details><summary class="mono muted">synthesizer thinking '
            f'(free association — travels downstream)</summary>{para(think)}</details>'
            if think
            else ""
        )
        cards.append(f"""<div class="g" data-members="{esc('|'.join(g['members']))}">
  <header><div class="chips"><span class="prov grp">Group {i + 1}</span>{chips}</div>
    <span class="mode">{esc(g['mode'])}</span></header>
  {sums_block}
  {think_block}
  <div class="res">{para(g['result'])}</div>
</div>""")
    return f"""<h2>Grouping and synthesis <span class="note">the partition is random, not semantic ·
  groups of 2–4 · one synthesis call each</span></h2>
<div class="groups">{''.join(cards)}</div>"""


def render_final(turn: dict) -> str:
    """What the final stage received and wrote — both recorded in the trace.

    Two trace formats: old runs have one composite "final" call; new runs
    have three separate calls (bwo-edit ∥ draft → armor) with disjoint
    inputs — the editor never sees the voice, the draft never sees the
    interior, the armorer bends the draft with the interior.
    """
    finals = [c for c in turn["calls"] if c["stage"] == "final"]
    by_label = {c["label"]: c for c in finals}
    v3 = "interior-editor" in by_label
    split = v3 or bool({"bwo-edit", "draft", "armor"} & set(by_label))
    final_call = finals[0] if finals else None

    groups_recv = "".join(
        f'<li><span class="k">group {i + 1}</span><span>Synthesis result — '
        f'{esc(g["mode"])}, from {esc(", ".join(g["members"]))}</span></li>'
        for i, g in enumerate(turn["groups"])
    )

    if v3:
        def model_of(label: str) -> str:
            c = by_label.get(label)
            return esc(c["model"].replace("claude-", "")) if c else "—"

        n_edits = len(turn.get("edits") or [])
        cards = f"""<div class="groups">
<div class="card"><h3 class="mono muted" style="margin:0 0 8px">INTERIOR-EDITOR
  <span class="note">{model_of('interior-editor')} · thinks 500w, then writes</span></h3>
<h4>Received</h4><ul>
<li><span class="k">history</span><span>Conversation so far</span></li>
<li><span class="k">said</span><span>What the other person just said</span></li>
<li><span class="k">bwo</span><span>Interior surface before the turn
  ({len(turn['bwo_before'].split())} words)</span></li>
{groups_recv}
<li><span class="k">voice</span><span>Voice sketch — governs only the reply</span></li>
</ul>
<h4>Produced</h4><ul>
<li><span class="k">thinking</span><span>500w free association (trace-only)</span></li>
<li><span class="k">bwo</span><span>Rewritten interior surface
  ({len(turn['bwo_after'].split())} words)</span></li>
<li><span class="k">edits</span><span>{n_edits} edit
  note{"" if n_edits == 1 else "s"} — why the surface changed</span></li>
<li><span class="k">reply</span><span>The initial, deliberately over-full reply</span></li>
<li><span class="k">why</span><span>Justification — the reply explained from the surface (trace-only)</span></li>
</ul></div>
<div class="card"><h3 class="mono muted" style="margin:0 0 8px">ARMOR
  <span class="note">{model_of('armor')} · selects the spark, cuts the chaff</span></h3>
<h4>Received</h4><ul>
<li><span class="k">history</span><span>Conversation so far — its rhythm sets the size</span></li>
<li><span class="k">draft</span><span>The initial reply</span></li>
<li><span class="k">said</span><span>What the other person said</span></li>
<li><span class="k">bwo</span><span>Interior surface after the turn — tunes what survives</span></li>
<li><span class="k">voice</span><span>Voice sketch</span></li>
</ul>
<h4>Produced</h4><ul>
<li><span class="k">response</span><span>What the persona actually says</span></li>
</ul></div>
</div>"""
        header = """<h2>The final stage <span class="note">interior editor thinks,
  rewrites the surface, and drafts · the armor selects the spark and sizes it
  to the conversation's ramp</span></h2>"""
    elif split:
        def model_of(label: str) -> str:
            c = by_label.get(label)
            return esc(c["model"].replace("claude-", "")) if c else "—"

        n_edits = len(turn.get("edits") or [])
        cards = f"""<div class="groups">
<div class="card"><h3 class="mono muted" style="margin:0 0 8px">BWO-EDIT
  <span class="note">{model_of('bwo-edit')} · never sees the voice</span></h3>
<h4>Received</h4><ul>
<li><span class="k">history</span><span>Conversation so far</span></li>
<li><span class="k">said</span><span>What was just said</span></li>
<li><span class="k">bwo</span><span>Interior surface before the turn
  ({len(turn['bwo_before'].split())} words)</span></li>
{groups_recv}</ul>
<h4>Produced</h4><ul>
<li><span class="k">bwo</span><span>Rewritten interior surface
  ({len(turn['bwo_after'].split())} words)</span></li>
<li><span class="k">edits</span><span>{n_edits} edit
  note{"" if n_edits == 1 else "s"} — why the surface changed</span></li>
</ul></div>
<div class="card"><h3 class="mono muted" style="margin:0 0 8px">DRAFT
  <span class="note">{model_of('draft')} · never sees the interior</span></h3>
<h4>Received</h4><ul>
<li><span class="k">voice</span><span>Voice sketch — how this persona is disposed to speak</span></li>
<li><span class="k">history</span><span>Conversation so far</span></li>
<li><span class="k">said</span><span>What was just said</span></li>
</ul>
<h4>Produced</h4><ul>
<li><span class="k">draft</span><span>The reply as pure conversation-continuity</span></li>
</ul></div>
<div class="card"><h3 class="mono muted" style="margin:0 0 8px">ARMOR
  <span class="note">{model_of('armor')} · bends the draft, lightly</span></h3>
<h4>Received</h4><ul>
<li><span class="k">draft</span><span>The draft reply</span></li>
<li><span class="k">said</span><span>What was just said</span></li>
<li><span class="k">voice</span><span>Voice sketch</span></li>
<li><span class="k">bwo</span><span>Interior surface after the turn</span></li>
{groups_recv}</ul>
<h4>Produced</h4><ul>
<li><span class="k">response</span><span>What the persona actually says</span></li>
</ul></div>
</div>"""
        header = """<h2>The final stage <span class="note">three separate calls ·
  the voice never touches the interior · the draft never reads it ·
  the armor lets little of it land</span></h2>"""
    else:
        received = [
            ("voice", "Voice sketch — how this persona is disposed to speak"),
            ("history", "Conversation so far"),
            ("said", "What was just said"),
            ("bwo", f"Interior surface before the turn ({len(turn['bwo_before'].split())} words)"),
        ]
        items = "".join(
            f'<li><span class="k">{esc(k)}</span><span>{esc(v)}</span></li>' for k, v in received
        ) + groups_recv
        produced = "".join([
            f'<li><span class="k">bwo</span><span>Rewritten interior surface '
            f'({len(turn["bwo_after"].split())} words)</span></li>',
            f'<li><span class="k">edits</span><span>{len(turn.get("edits") or [])} edit '
            f'note{"" if len(turn.get("edits") or []) == 1 else "s"} — why the surface changed</span></li>',
            '<li><span class="k">response</span><span>What the persona says</span></li>',
        ])

    edits = turn.get("edits") or []
    if edits:
        rows = "".join(
            f"""<tr>
  <td style="width:38%"><b>{esc(e.get('change', ''))}</b></td>
  <td style="width:22%">{''.join(
      f'<span class="prov{" grp" if d.lower().startswith("group") else ""}">{esc(d)}</span>'
      for d in e.get('driven_by', []))}</td>
  <td>{esc(e.get('why', ''))}</td>
</tr>"""
            for e in edits
        )
        edit_block = f"""<h2>Why the surface changed <span class="note">the final call's own
  record of which input drove each edit — instrumentation, not the persona speaking</span></h2>
<table class="edits">{rows}</table>"""
    else:
        edit_block = """<h2>Why the surface changed</h2>
<div class="absent">Not captured in this run. The edit log was added after these traces were
recorded, so the interior editor was never asked to log its edits. Re-run the conversation to
populate it.</div>"""

    if split:
        return f"""{header}
{cards}
<p class="legend">Not received anywhere: the per-machine flows and the group summaries — those
reach the trace only. The draft and the final reply are recorded separately, so the armoring's
effect is visible below.</p>
{edit_block}"""

    withheld = "the per-machine flows and the group summaries — those reach the trace only"
    return f"""<h2>The final call <span class="note">one model call · reads the pre-turn surface
  and every group result · writes both outputs</span></h2>
<div class="final">
  <div class="io"><h4>Received</h4><ul>{items}</ul></div>
  <div class="node">final<span>{esc(final_call['model'].replace('claude-', '')) if final_call else ''}</span></div>
  <div class="io"><h4>Produced</h4><ul>{produced}</ul></div>
</div>
<p class="legend">Not received: {withheld}. The reply and the surface are written in the same
pass, so the reply's provenance is not decomposed — the edit log below covers the surface only.</p>
{edit_block}"""


def draft_block(turn: dict) -> str:
    """The pre-armoring draft and the editor's justification, when recorded."""
    draft = (turn.get("draft_response") or "").strip()
    just = (turn.get("justification") or "").strip()
    out = ""
    if draft and draft != turn["response"].strip():
        out += f"""<h2>Initial reply, before armoring <span class="note">spoken from the
  surface the editor just wrote — deliberately uncut</span></h2>
  <div class="reply" style="opacity:.65">{para(draft)}</div>"""
    if just:
        out += f"""<h2>Why the reply <span class="note">the editor's own account, grounded
  solely in the surface — instrumentation, not the persona speaking</span></h2>
  <div class="card">{para(just)}</div>"""
    fits = turn.get("fit_reviews") or []
    if fits:
        rows = "".join(
            f"""<div class="card" style="margin-bottom:10px"><h3 class="mono muted"
  style="margin:0 0 6px">round {r.get('round')} — {'FITS' if r.get('fits') else 'DOES NOT FIT'}</h3>
  <div class="reply" style="opacity:.75">{para(r.get('response', ''))}</div>
  {para(r.get('explanation', ''))}</div>"""
            for r in fits
        )
        out += f"""<h2>Blind fit checks <span class="note">a reader with only the situation
  and the conversation — no interior — judges each armored candidate; a failed verdict
  goes back to a redraft</span></h2>{rows}"""
    return out


def render_bwo(turn: dict) -> str:
    before, after = turn["bwo_before"], turn["bwo_after"]
    added, removed = diff_counts(before, after)
    wb, wa = len(before.split()), len(after.split())
    return f"""<h2>Interior surface, edited <span class="note">
  {wb} → {wa} words · +{added} / −{removed}</span></h2>
<div class="diff">{word_diff(before, after)}</div>
<p class="legend"><b style="background:#dcefdc">green</b> added this turn ·
  <b style="background:#f6dcdc">red</b> removed ·
  the surface is rewritten whole by the final call, so the diff is reconstructed, not recorded</p>
<div class="cols" style="margin-top:12px">
  <div class="card"><h3 class="mono muted" style="margin:0 0 8px">BEFORE</h3>{para(before)}</div>
  <div class="card"><h3 class="mono muted" style="margin:0 0 8px">AFTER</h3>{para(after)}</div>
</div>"""


def render_timeline(turn: dict) -> str:
    bars, total = timeline(turn["calls"])
    if not bars or total <= 0:
        return ""
    rows, seen = [], None
    for b in bars:
        if b["stage"] != seen:
            seen = b["stage"]
            rows.append(f'<div class="stagerule">{b["stage"]}</div>')
        left, width = 100 * b["start"] / total, max(100 * b["dur"] / total, 0.4)
        rows.append(f"""<div class="row">
  <span class="mono">{esc(b['label'])[:22]}</span>
  <span class="track"><span class="bar" style="left:{left:.2f}%;width:{width:.2f}%"></span></span>
  <span class="mono muted">{b['dur']:.1f}s</span>
</div>""")
    t = turn["totals"]
    return f"""<h2>Timeline <span class="note">stage order is known, per-call latency is measured,
  start times within a stage are inferred</span></h2>
<div class="tl">{''.join(rows)}</div>
<p class="totals mono">{t['calls']} calls · {t['input_tokens']} in ·
  {t['output_tokens']} out · {t['elapsed_s']}s wall clock ·
  {sum(b['dur'] for b in bars):.1f}s of model time, so the fan-out saves
  {sum(b['dur'] for b in bars) - t['elapsed_s']:.1f}s</p>"""


def render_calls(turn: dict) -> str:
    items = []
    for c in turn["calls"]:
        out = c["output"]
        out = json.dumps(out, indent=2) if not isinstance(out, str) else out
        items.append(f"""<details>
  <summary><b>{esc(c['stage'])}</b> <span class="mono">{esc(c['label'])}</span>
    <span class="mono muted" style="margin-left:auto">{esc(c['model'].replace('claude-',''))} ·
    {c['input_tokens']}→{c['output_tokens']} tok · {float(c.get('latency_s') or 0):.1f}s</span></summary>
  <div class="calltxt">
    <h4>System prompt</h4><pre>{esc(c['system'])}</pre>
    <h4>User message</h4><pre>{esc(c['user'])}</pre>
    <h4>Output</h4><pre>{esc(out)}</pre>
  </div>
</details>""")
    return f"""<h2>Every model call <span class="note">exact prompt sent and text returned —
  the surface for hand-editing prompts</span></h2>{''.join(items)}"""


def render_turn(turn: dict, idx: int, roster: list[dict], colors: dict[str, str]) -> str:
    return f"""<section class="turn" data-turn="{idx}" {'hidden' if idx else ''}>
  <h2>What was said</h2>
  <div class="said">{para(turn['input_text'])}</div>
  {render_selection(turn, roster)}
  <div class="flow"><svg class="wires" preserveAspectRatio="none"></svg>
    {render_machines(turn, colors)}
    <div class="gap"></div>
    {render_groups(turn, colors)}
  </div>
  {render_final(turn)}
  {render_bwo(turn)}
  {draft_block(turn)}
  <h2>What the persona said back <span class="note">the only stage that speaks in plain,
    named language</span></h2>
  <div class="reply">{para(turn['response'])}</div>
  {render_timeline(turn)}
  {render_calls(turn)}
</section>"""


def build(run_dir: Path) -> Path:
    turns, manifest, persona = load_run(run_dir)
    roster = roster_of(manifest)
    colors = {m["name"]: m["color"] for m in roster}

    tabs = "".join(
        f'<button data-turn="{i}" aria-selected="{str(i == 0).lower()}">Turn {i + 1}</button>'
        for i in range(len(turns))
    )
    body = "".join(render_turn(t, i, roster, colors) for i, t in enumerate(turns))
    always = sum(1 for m in roster if m["always_on"])

    doc = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(persona)} — firing trace</title>
<style>{CSS}</style></head><body><div class="wrap">
<header>
  <h1>{esc(persona)} — firing trace</h1>
  <p class="sub">{len(turns)} turn{'s' if len(turns) != 1 else ''} ·
    {len(roster)} machines in the roster, {always} always-on ·
    run <span class="mono">{esc(run_dir.name)}</span></p>
</header>
<p class="sub">Each turn runs five stages. A relevance vote and a random draw pick which machines
fire; the fired machines run in parallel and cannot see each other; a random partition groups them
and each group is synthesized under one mode; a final call rewrites the interior surface and writes
the reply. Nothing records which current produced which clause of the reply, so no arrow is drawn
into the last stage.</p>
<nav>{tabs}</nav>
{body}
</div><script>{JS}</script></body></html>"""

    out = Path(__file__).parent / f"{run_dir.name}.html"
    out.write_text(doc, encoding="utf-8")
    return out


def build_index(built: list[tuple[Path, int, str]]) -> Path:
    rows = "".join(
        f"""<li><a href="{esc(p.name)}">{esc(p.stem)}</a>
  <span class="mono muted">{n} turn{'s' if n != 1 else ''} ·
  {p.stat().st_size / 1024:.0f} KB{' · edit log' if has_edits else ''}</span></li>"""
        for p, n, has_edits in built
    )
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Firing traces</title><style>{CSS}
ul.runs{{list-style:none;padding:0;margin:0}}
ul.runs li{{background:#fff;border:1px solid #e2ded4;border-radius:4px;padding:11px 14px;
  margin-bottom:7px;display:flex;justify-content:space-between;gap:12px;align-items:baseline}}
ul.runs a{{color:#1c2024;font-weight:600;text-decoration:none}}
ul.runs a:hover{{text-decoration:underline}}</style></head><body><div class="wrap">
<header><h1>Firing traces</h1>
<p class="sub">{len(built)} run{'s' if len(built) != 1 else ''} · rebuild with
<span class="mono">python3 viewer/build_viewer.py traces/</span></p></header>
<ul class="runs">{rows}</ul></div></body></html>"""
    out = Path(__file__).parent / "index.html"
    out.write_text(doc, encoding="utf-8")
    return out


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = Path(sys.argv[1]).resolve()
    runs = (
        sorted(d for d in target.iterdir() if d.is_dir() and any(d.glob("turn-*.json")))
        if not any(target.glob("turn-*.json"))
        else [target]
    )
    if not runs:
        sys.exit(f"no runs found under {target}")

    built = []
    for run in runs:
        turns, _, _ = load_run(run)
        p = build(run)
        has_edits = any(t.get("edits") for t in turns)
        built.append((p, len(turns), has_edits))
        print(f"wrote {p.name}  ({p.stat().st_size / 1024:.0f} KB)")
    if len(built) > 1:
        print(f"wrote {build_index(built).name}")
