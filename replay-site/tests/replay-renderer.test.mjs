import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { JSDOM } from 'jsdom';
import { replayTurn } from '../lib/replay-events.mjs';

const html = await readFile(new URL('../../viewer/live.html', import.meta.url), 'utf8');
const renderer = html.split('<script>')[1].split('// ---- wiring ----')[0];

function player(t) {
  const dom = new JSDOM(html, { runScripts: 'outside-only' });
  t.after(() => dom.window.close());
  const { window } = dom;
  let draw, frames = [];
  window.setInterval = callback => { draw = callback; return 1; };
  window.requestAnimationFrame = callback => frames.push(callback);
  window.eval(renderer);
  const view = window.personaReplayView;
  const $ = selector => (window.document.querySelector('.turn-view:not([hidden])')?.querySelector(selector) || window.document.querySelector(selector));
  function tick(count = 1) {
    for (let i = 0; i < count; i++) {
      draw(); const pending = frames; frames = []; pending.forEach(callback => callback());
    }
  }
  function until(predicate) {
    for (let i = 0; i < 10000; i++) {
      if (predicate()) return;
      tick();
    }
    assert.fail('Replay did not finish drawing.');
  }
  return { view, $, tick, until, document: window.document };
}

function fixture(index = 1) {
  const analysis = 'A complete analysis. '.repeat(100);
  const product = 'The complete product. '.repeat(60);
  const thinking = 'The complete synthesis analysis. '.repeat(50);
  const result = 'The complete synthesis result. '.repeat(40);
  const editor = { thinking: 'The full editor analysis. '.repeat(120),
    bwo: `State ${index}`, response: 'Draft reply', justification: 'A reason' };
  return {
    input_text: `Question ${index}`, response: `Final reply ${index}`,
    bwo_before: `State ${index - 1}`, bwo_after: editor.bwo,
    draft_response: editor.response, justification: editor.justification,
    edits: [{change: 'A concrete state change', driven_by: ['Group 1'], why: 'The group raised a specific concern.'}],
    fired: [['A', 'analysis', 'selected'], ['B', 'analysis', 'selected']],
    machine_outputs: { A: `ANALYSIS\n${analysis}\nPRODUCT\n${product}`, B: 'ANALYSIS\nShort analysis\nPRODUCT\nShort product' },
    groups: [{ members: ['A', 'B'], mode: 'conjunctive', thinking, result }],
    calls: [{ label: 'interior-editor', output: editor },
      { label: 'fit-check-1', output: { explanation: 'The full review. '.repeat(80), fits: false } },
      { label: 'redraft-1', output: 'The full redraft. '.repeat(60) }],
    fit_reviews: [
      { round: 1, response: 'First candidate. '.repeat(60), fits: false, explanation: 'The full review. '.repeat(80) },
      { round: 2, response: `Final reply ${index}`, fits: true, explanation: 'Fits.' },
    ],
  };
}

async function enqueue(view, turn) {
  await replayTurn(turn, [], { emit: view.emit, sleep: async () => {} });
}

test('every phase finishes before regrouping, refinement, or the final reply', async t => {
  const p = player(t), turn = fixture();
  await enqueue(p.view, turn);
  p.tick();
  assert.ok(p.$('[data-name="A"] .ana').textContent.length > 0);
  assert.ok(p.$('[data-name="B"] .ana').textContent.length > 0, 'machines stream in parallel');
  assert.equal(p.$('.grouprow'), null, 'regrouping waits for the long machine');
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply'), null);

  p.until(() => p.$('.grouprow'));
  assert.equal(p.$('[data-name="A"] .prod').textContent, turn.machine_outputs.A.split('PRODUCT\n')[1]);
  assert.equal(p.$('[data-name="A"] .ana').textContent.trimEnd(), turn.machine_outputs.A.split('\nPRODUCT')[0].trimEnd());
  assert.equal(p.$('.bubble.typing'), null, 'call completion is not overwritten by other callbacks');
  assert.equal(p.$('.bubble.shrunk'), null, 'regrouping does not hide the phases');
  assert.equal(p.$('[data-name="A"] details').open, true);
  p.tick();
  assert.equal(p.$('.synth .think').textContent, '', 'group motion finishes before synthesis starts');

  p.until(() => p.$('.editor'));
  assert.equal(p.$('.synth .think').textContent, turn.groups[0].thinking);
  assert.equal(p.$('.synth .result').textContent, turn.groups[0].result);
  assert.equal(p.$('.synth details').open, true);

  p.until(() => p.$('.card .panel.reply:not(.editor .reply)'));
  assert.equal(p.$('.editor .think').textContent, turn.calls[0].output.thinking);
  assert.equal(p.$('.editor .surface').textContent, turn.bwo_after);
  assert.equal(p.$('.editor .reply').textContent, turn.draft_response);
  assert.equal(p.$('.editor details.th').open, true);
  assert.equal(p.$('.edit-reason').textContent, turn.edits[0].why);

  p.until(() => p.$('.verdict'));
  assert.equal(p.$('.review').textContent, turn.fit_reviews[0].explanation);
  assert.equal(p.$('.review').parentElement.open, true);
  assert.equal(p.$('.review').closest('.card').querySelector('.reply').textContent, turn.fit_reviews[0].response);

  p.until(() => p.$('.turn-view:not([hidden]) .finalreply'));
  assert.equal(p.$('.redraft').textContent, turn.calls[2].output, 'the recorded redraft completes');
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, turn.response);
});

test('back-to-back turns show the first complete reply before clearing its pipeline', async t => {
  const p = player(t);
  await enqueue(p.view, fixture(1));
  await enqueue(p.view, fixture(2));
  p.until(() => p.$('.turn-view:not([hidden]) .finalreply'));
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 1');
  p.tick(20);
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 1', 'completed turn remains visible during its hold');
  p.until(() => p.$('.turn-view:not([hidden]) .finalreply')?.textContent === 'Final reply 2');
  assert.equal(p.document.querySelectorAll('.msg.them').length, 2);
  const earlier = p.document.querySelector('.msg[data-turn="0"]');
  earlier.click();
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 1');
  assert.equal(earlier.getAttribute('aria-pressed'), 'true');
  assert.equal(p.$('.editor .surface').textContent, 'State 1');
  p.document.querySelector('.msg[data-turn="1"]').click();
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 2');
});

test('inspecting an older message does not interrupt the current turn', async t => {
  const p = player(t);
  await enqueue(p.view, fixture(1));
  p.until(() => p.$('.finalreply'));
  p.tick(30);
  await enqueue(p.view, fixture(2));
  p.tick(10);
  p.document.querySelector('.msg[data-turn="0"]').click();
  p.until(() => p.document.querySelector('.turn-view[data-turn="1"] .finalreply'));
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 1');
  p.document.querySelector('.msg[data-turn="1"]').click();
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply').textContent, 'Final reply 2');
  assert.equal(p.$('.editor .surface').textContent, 'State 2');
});

test('pause freezes text and transitions; completion waits for the display', async t => {
  const p = player(t);
  await enqueue(p.view, fixture());
  let finished = false;
  const idle = p.view.whenIdle().then(() => { finished = true; });
  p.tick(10);
  const partial = p.$('#pipe').innerHTML;
  p.view.paused = true;
  p.tick(100);
  assert.equal(p.$('#pipe').innerHTML, partial);
  await Promise.resolve();
  assert.equal(finished, false);
  p.view.paused = false;
  p.until(() => p.$('.turn-view:not([hidden]) .finalreply'));
  p.tick(30);
  await idle;
  assert.equal(finished, true);
});

test('reset cancels queued stages and manual collapse stays under user control', async t => {
  const p = player(t);
  await enqueue(p.view, fixture());
  p.tick(10);
  const button = p.$('[data-name="A"] .collapse');
  button.click(); p.tick(10);
  assert.equal(button.getAttribute('aria-expanded'), 'false');
  button.click();
  assert.equal(p.$('[data-name="A"]').classList.contains('shrunk'), false);
  p.$('[data-name="A"] details').open = false;
  p.tick(10);
  assert.equal(p.$('[data-name="A"] details').open, false);
  const controller = new AbortController();
  const idle = p.view.whenIdle(controller.signal);
  controller.abort(); p.view.clear(); p.tick(1000);
  await assert.rejects(idle, { name: 'AbortError' });
  assert.equal(p.$('#pipe').children.length, 0);
  assert.equal(p.$('#transcript').children.length, 0);
});

test('opening analysis in a finished group does not collapse the machine box', async t => {
  const p = player(t);
  await enqueue(p.view, fixture());
  p.until(() => p.$('.finalreply'));
  const bubble = p.$('[data-name="A"]');
  const analysis = bubble.querySelector('details');
  analysis.open = false;
  analysis.querySelector('summary').click();
  assert.equal(analysis.open, true);
  assert.equal(bubble.classList.contains('shrunk'), false);
  assert.equal(bubble.querySelector('.collapse').getAttribute('aria-expanded'), 'true');
  analysis.querySelector('summary').click();
  assert.equal(analysis.open, false);
  assert.equal(bubble.classList.contains('shrunk'), false);
});

test('completed outputs without deltas still draw in full before the reply', t => {
  const p = player(t);
  const output = 'ANALYSIS\nAnalysis without deltas\nPRODUCT\nProduct without deltas';
  [
    { type: 'turn_started', input: 'Question', replay: true },
    { type: 'selection_done', fired: [{ name: 'A', category: 'analysis' }] },
    { type: 'call_done', id: 'machine/A', output },
    { type: 'turn_done', response: 'Reply' },
  ].forEach(p.view.emit);
  assert.equal(p.$('.turn-view:not([hidden]) .finalreply'), null);
  p.until(() => p.$('.turn-view:not([hidden]) .finalreply'));
  assert.equal(p.$('.prod').textContent, 'Product without deltas');
});

test('stage subtitles and agent descriptions stay short and contain no em dashes', async t => {
  const p = player(t), turn = fixture();
  const names = ['Compensator', 'Situation', 'Pulsation', 'Laetitia', 'Cupiditas',
    'Tristitia', 'Hope', 'Glory', 'Fear', 'Shame', 'Longing', 'Implication',
    'Memento', 'Hesitation', 'Register-shift', 'Memory-generator', 'Fantasy',
    'Inflate', 'Appease', 'Withhold'];
  turn.fired = names.map(name => [name, 'analysis', 'selected']);
  turn.machine_outputs = Object.fromEntries(names.map(name => [name, 'ANALYSIS\nAnalysis\nPRODUCT\nProduct']));
  turn.groups[0].members = names;
  await enqueue(p.view, turn);
  p.until(() => p.$('.finalreply'));
  const descriptions = [...p.document.querySelectorAll('.stage > .sub, .sens')];
  assert.equal(descriptions.length, 26);
  for (const node of descriptions) {
    assert.ok(node.textContent.length <= 55, node.textContent);
    assert.ok(!node.textContent.includes('—'), node.textContent);
  }
});
