export function readRun(value) {
  if (!value || typeof value !== 'object') throw new Error('Choose an exported conversation JSON file.');
  const run = value;
  if (run.format !== 'persona-trace-run-v1' || typeof run.id !== 'string' ||
      typeof run.title !== 'string' || typeof run.persona !== 'string') {
    throw new Error('Choose a conversation exported from the local chat.');
  }
  if (!Array.isArray(run.turns) || run.turns.length < 2) {
    throw new Error('A conversation needs at least two turns.');
  }
  run.turns.forEach((turn, index) => {
    if (!turn || ['input_text', 'response', 'bwo_before', 'bwo_after'].some(key => typeof turn[key] !== 'string')) {
      throw new Error(`Turn ${index + 1} is missing conversation or state text.`);
    }
    if (!Array.isArray(turn.calls) || !turn.calls.length || turn.calls.some(call => !call || call.model !== 'gpt-6-astra')) {
      throw new Error(`Turn ${index + 1} must use Astra for every recorded call.`);
    }
    if (index && turn.bwo_before !== run.turns[index - 1].bwo_after) {
      throw new Error(`Turn ${index + 1} does not continue the previous turn's state.`);
    }
  });
  return { ...run, model: 'gpt-6-astra' };
}
