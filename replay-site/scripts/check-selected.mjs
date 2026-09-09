import { readFile, readdir } from 'node:fs/promises';
import { readRun } from '../lib/trace-data.mjs';

const directory = new URL('../public/selected/', import.meta.url);
const selected = JSON.parse(await readFile(new URL('index.json', directory), 'utf8'));
if (!Array.isArray(selected) || selected.some(name => typeof name !== 'string' || !/^[-a-zA-Z0-9]+\.json$/.test(name) || name === 'index.json')) throw new Error('Invalid selected conversation list.');
if (new Set(selected).size !== selected.length) throw new Error('Duplicate selected filenames.');
const files = await readdir(directory);
for (const name of files) if (name !== 'index.json' && !selected.includes(name)) throw new Error(`Unselected file would be published: ${name}`);
const ids = new Set();
for (const name of selected) {
  const run = readRun(JSON.parse(await readFile(new URL(name, directory), 'utf8')));
  if (ids.has(run.id)) throw new Error(`Duplicate conversation ID: ${run.id}`);
  ids.add(run.id);
}
console.log(`${selected.length} selected conversations validated.`);
