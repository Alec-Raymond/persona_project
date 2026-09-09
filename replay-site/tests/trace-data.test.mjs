import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readRun } from '../lib/trace-data.ts';

function sample() {
  return { format: 'persona-trace-run-v1', id: 'example', title: 'Example', persona: 'effusive', model: 'gpt-6-astra',
    turns: [0, 1].map(index => ({ input_text: `message ${index}`, response: `reply ${index}`,
      bwo_before: String(index), bwo_after: String(index + 1), calls: [{ model: 'gpt-6-astra' }] })) };
}

test('preserves a full, continuous Astra conversation', () => assert.deepEqual(readRun(sample()), sample()));
test('rejects a single turn', () => { const run = sample(); run.turns.pop(); assert.throws(() => readRun(run), /at least two/); });
test('checks every call instead of trusting the run label', () => { const run = sample(); run.turns[1].calls.push({ model: 'claude-sonnet-5' }); assert.throws(() => readRun(run), /every recorded call/); });
test('rejects absent call records', () => { const run = sample(); run.turns[1].calls = []; assert.throws(() => readRun(run), /every recorded call/); });
test('rejects turns from different conversations', () => { const run = sample(); run.turns[1].bwo_before = 'other'; assert.throws(() => readRun(run), /does not continue/); });
test('rejects malformed conversation text', () => { const run = sample(); run.turns[0].response = null; assert.throws(() => readRun(run), /missing conversation/); });
