import { readRun } from './trace-data.mjs';
import { replayTurn } from './replay-events.mjs';

const view = globalThis.personaReplayView;
const $ = selector => document.querySelector(selector);
let runs = [], selected = 0, turnIndex = 0, playback = null;
const current = () => runs[selected];

function controls() {
  const run = current();
  $('#replayBtn').disabled = !run || !!playback;
  $('#exportBtn').disabled = !run;
  $('#newBtn').disabled = !run;
  $('#previousBtn').disabled = !run || turnIndex === 0;
  $('#nextBtn').disabled = !run || turnIndex === run.turns.length - 1;
  $('#pauseBtn').disabled = !playback;
  $('#pauseBtn').textContent = view.paused ? 'Resume' : 'Pause';
  $('#pauseBtn').setAttribute('aria-pressed', String(view.paused));
}
view.onBusyChange = controls;
view.onTurnSelected = index => { turnIndex = index; $('#turnSel').value = String(index); controls(); };
view.onTurnRequest = index => void play(index, true);
function stop() {
  playback?.abort(); playback = null; view.paused = false;
  view.clear(); controls();
}
function showTurns() {
  const select = $('#turnSel'); select.replaceChildren();
  (current()?.turns || []).forEach((_, index) => select.add(new Option(`Turn ${index + 1}`, String(index))));
  select.value = String(turnIndex);
}
function choose(index) {
  stop(); selected = index; turnIndex = 0;
  const run = current();
  if (run) { view.setName(run.persona); view.setStatus('Press Replay to start.'); }
  showTurns(); controls();
}
function populate() {
  const select = $('#traceSel'); select.replaceChildren();
  runs.forEach((run, index) => select.add(new Option(run.title, String(index))));
  select.value = String(selected);
}
function timer(ms, signal) {
  return new Promise((resolve, reject) => {
    if (signal.aborted) { reject(new DOMException('Stopped', 'AbortError')); return; }
    const done = () => { signal.removeEventListener('abort', cancel); resolve(); };
    const id = setTimeout(done, ms);
    const cancel = () => { clearTimeout(id); reject(new DOMException('Stopped', 'AbortError')); };
    signal.addEventListener('abort', cancel, { once: true });
  });
}
async function play(start = 0, single = false) {
  stop();
  const run = current(); if (!run) return;
  const controller = new AbortController(); playback = controller;
  for (const [index, turn] of run.turns.slice(0, start).entries()) {
    view.addMessage('you', turn.input_text, index); view.addMessage('persona', turn.response, index);
  }
  const sleep = async ms => {
    await timer(ms, controller.signal);
    while (view.paused) await timer(40, controller.signal);
    if (controller.signal.aborted) throw new DOMException('Stopped', 'AbortError');
  };
  controls();
  try {
    for (let index = start; index < (single ? start + 1 : run.turns.length); index++) {
      turnIndex = index; $('#turnSel').value = String(index);
      await replayTurn(run.turns[index], run.roster || [], {
        sleep,
        emit: event => {
          if (controller.signal.aborted) throw new DOMException('Stopped', 'AbortError');
          view.emit(event.type === 'turn_started' ? { ...event, index } : event); controls();
        },
      });
      await view.whenIdle(controller.signal);
    }
    view.setStatus(`Turn ${turnIndex + 1} of ${run.turns.length}`);
  } catch (error) {
    if (error.name !== 'AbortError') view.setStatus(error.message || 'Could not replay this conversation.');
  } finally {
    if (playback === controller) { playback = null; view.paused = false; controls(); }
  }
}
async function openFiles(files) {
  if (!files?.length) return;
  try {
    const opened = await Promise.all(Array.from(files).map(async file => readRun(JSON.parse(await file.text()))));
    stop(); runs = [...opened, ...runs.filter(run => !opened.some(item => item.id === run.id))];
    selected = 0; populate(); choose(0);
  } catch (error) { view.setStatus(error.message || 'Could not open that conversation.'); }
  $('#fileInput').value = '';
}
$('#openBtn').onclick = () => $('#fileInput').click();
$('#fileInput').onchange = event => void openFiles(event.target.files);
$('#traceSel').onchange = event => choose(Number(event.target.value));
function inspectTurn(index) {
  if (!view.showTurn(index)) void play(index, true);
}
$('#turnSel').onchange = event => inspectTurn(Number(event.target.value));
$('#replayBtn').onclick = () => void play(turnIndex);
$('#newBtn').onclick = () => choose(selected);
$('#previousBtn').onclick = () => inspectTurn(turnIndex - 1);
$('#nextBtn').onclick = () => inspectTurn(turnIndex + 1);
$('#pauseBtn').onclick = () => { view.paused = !view.paused; controls(); };
$('#exportBtn').onclick = () => {
  const run = current(); if (!run) return;
  const url = URL.createObjectURL(new Blob([JSON.stringify(run, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = `${run.id}.json`; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
};
controls();
try {
  const response = await fetch('./selected/index.json');
  if (!response.ok) throw new Error('Could not load saved conversations.');
  const names = await response.json();
  if (!Array.isArray(names) || names.some(name => typeof name !== 'string' || !/^[-a-zA-Z0-9]+\.json$/.test(name) || name === 'index.json')) throw new Error('Invalid conversation list.');
  const saved = await Promise.all(names.map(async name => {
    const response = await fetch(`./selected/${name}`);
    if (!response.ok) throw new Error('Could not load a saved conversation.');
    return readRun(await response.json());
  }));
  runs = [...runs, ...saved.filter(run => !runs.some(item => item.id === run.id))];
  populate();
  if (runs.length) choose(0);
  else {
    $('#traceSel').add(new Option('No saved conversations', ''));
    const message = document.createElement('p'); message.className = 'empty';
    message.textContent = 'Open an exported conversation to replay it.';
    $('#transcript').appendChild(message);
    view.setStatus('Opened files stay in your browser.');
  }
} catch (error) { view.setStatus(error.message || 'Could not load conversations.'); }
controls();
