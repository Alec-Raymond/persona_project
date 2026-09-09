// Browser counterpart of Session._replay_turn in persona2/live.py.
// Keep event order, word chunks, and delays identical to the tuned local replay.
export function pythonJSON(value) {
  const json = JSON.stringify(value);
  let output = '', quoted = false, escaped = false;
  for (let i = 0; i < json.length; i++) {
    const character = json[i];
    if (character.charCodeAt(0) > 127) {
      output += '\\u' + character.charCodeAt(0).toString(16).padStart(4, '0');
      continue;
    }
    output += character;
    if (escaped) { escaped = false; continue; }
    if (quoted && character === '\\') { escaped = true; continue; }
    if (character === '"') quoted = !quoted;
    else if (!quoted && (character === ':' || character === ',')) output += ' ';
  }
  return output;
}

export async function replayTurn(turn, roster, { emit, sleep }) {
  async function streamParallel(streams, words = 2) {
    const tokens = new Map(streams.map(([id, text]) => [id, text.match(/\S+\s*/gu) || []]));
    const positions = new Map(streams.map(([id]) => [id, 0]));
    while (true) {
      let alive = false;
      for (const [id, wordsForCall] of tokens) {
        const position = positions.get(id);
        if (position >= wordsForCall.length) continue;
        alive = true;
        emit({ type: 'call_delta', id, text: wordsForCall.slice(position, position + words).join('') });
        positions.set(id, position + words);
      }
      if (!alive) break;
      await sleep(30);
    }
  }
  const byName = new Map(roster.map(machine => [machine.name, machine]));
  emit({ type: 'turn_started', input: turn.input_text, bwo: turn.bwo_before, replay: true });
  emit({ type: 'stage_started', stage: 'selection' });
  await sleep(800);
  emit({ type: 'selection_done', fired: (turn.fired || []).map(([name, shape, resonance]) => ({
    name, category: byName.get(name)?.category || shape,
    sensitivity: byName.get(name)?.sensitivity?.trim() || '', resonance,
  })) });
  await sleep(800);
  emit({ type: 'stage_started', stage: 'machines' });
  const machineStreams = Object.entries(turn.machine_outputs || {}).map(([name, output]) => {
    const id = `machine/${name}`;
    emit({ type: 'call_started', id, stage: 'machine', label: name, model: '', schema: false });
    return [id, output];
  });
  await streamParallel(machineStreams);
  for (const [id, output] of machineStreams) emit({ type: 'call_done', id, output });
  await sleep(1200);
  const groups = turn.groups || [];
  emit({ type: 'stage_started', stage: 'synthesis' });
  emit({ type: 'groups_assigned', groups: groups.map(group => group.members || []) });
  await sleep(1000);
  const synthStreams = groups.map(group => {
    const label = (group.members || []).join(' + '), id = `synthesis/${label}`;
    emit({ type: 'call_started', id, stage: 'synthesis', label, model: '', schema: true });
    return [id, pythonJSON({ mode: group.mode ?? null, thinking: group.thinking ?? '', result: group.result ?? '' })];
  });
  await streamParallel(synthStreams);
  groups.forEach((group, index) => {
    const members = group.members || [], id = `synthesis/${members.join(' + ')}`;
    emit({ type: 'call_done', id, output: group });
    emit({ type: 'synthesis_done', group: index + 1, members, mode: group.mode ?? null,
      thinking: group.thinking ?? '', result: group.result ?? '' });
  });
  await sleep(800);
  emit({ type: 'stage_started', stage: 'editor' });
  const editor = (turn.calls || []).find(call => call.label === 'interior-editor')?.output || {};
  const editorId = 'final/interior-editor';
  emit({ type: 'call_started', id: editorId, stage: 'final', label: 'interior-editor', model: '', schema: true });
  await streamParallel([[editorId, Object.keys(editor).length ? pythonJSON(editor) : '']], 3);
  emit({ type: 'call_done', id: editorId, output: editor });
  emit({ type: 'editor_done', bwo: turn.bwo_after || '', edits: turn.edits || [],
    response: turn.draft_response || '', justification: turn.justification || '', revised: false });
  await sleep(800);
  emit({ type: 'stage_started', stage: 'armor' });
  for (const review of turn.fit_reviews || []) {
    const round = review.round ?? 1, id = round === 1 ? 'final/armor' : `final/armor-${round}`;
    emit({ type: 'call_started', id, stage: 'final', label: 'armor', model: '', schema: false });
    await streamParallel([[id, review.response || '']], 3);
    emit({ type: 'call_done', id, output: review.response || '' });
    emit({ type: 'fit_round', round, response: review.response || '', fits: review.fits ?? null,
      explanation: review.explanation || '' });
    await sleep(600);
  }
  await sleep(600);
  emit({ type: 'turn_done', response: turn.response || '', bwo_after: turn.bwo_after || '' });
}
