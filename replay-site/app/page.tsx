'use client';

import { useEffect, useRef, useState } from 'react';
import { readRun, type Run } from '../lib/trace-data';

function Text({ value }: { value: unknown }) {
  return <pre>{typeof value === 'string' ? value : JSON.stringify(value, null, 2)}</pre>;
}

export default function Home() {
  const [runs, setRuns] = useState<Run[]>([]);
  const [selected, setSelected] = useState(0);
  const [turnIndex, setTurnIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const input = useRef<HTMLInputElement>(null);
  const run = runs[selected];
  const turn = run?.turns[turnIndex];

  useEffect(() => {
    let active = true;
    async function load() {
      try {
        const response = await fetch('/selected/index.json');
        if (!response.ok) throw new Error('Could not load the selected conversations.');
        const paths: unknown = await response.json();
        if (!Array.isArray(paths) || paths.some(path => typeof path !== 'string' || !/^[-a-zA-Z0-9]+\.json$/.test(path))) {
          throw new Error('The conversation list is invalid.');
        }
        const saved = await Promise.all(paths.map(async path => {
          const response = await fetch(`/selected/${path}`);
          if (!response.ok) throw new Error('A selected conversation could not be loaded.');
          return readRun(await response.json());
        }));
        if (active) setRuns(current => [...saved, ...current.filter(run => !saved.some(item => item.id === run.id))]);
      } catch (error) {
        if (active) setError(error instanceof Error ? error.message : 'Could not load conversations.');
      } finally {
        if (active) setLoading(false);
      }
    }
    void load();
    return () => { active = false; };
  }, []);

  useEffect(() => {
    if (!playing || !run) return;
    if (turnIndex >= run.turns.length - 1) { setPlaying(false); return; }
    const timer = setTimeout(() => setTurnIndex(index => index + 1), 3000);
    return () => clearTimeout(timer);
  }, [playing, run, turnIndex]);

  async function openFiles(files: FileList | null) {
    if (!files?.length) return;
    setError('');
    try {
      const opened = await Promise.all(Array.from(files).map(async file => readRun(JSON.parse(await file.text()))));
      setRuns(current => [...opened, ...current.filter(run => !opened.some(item => item.id === run.id))]);
      setSelected(0); setTurnIndex(0); setPlaying(false);
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Could not read the conversation.');
    }
    if (input.current) input.current.value = '';
  }

  function move(index: number) { setPlaying(false); setTurnIndex(index); }

  return (
    <main>
      <header>
        <div><h1>Persona traces</h1><span className="meta">Astra · multi-turn conversations</span></div>
        <div className="header-actions">
          <a href="https://github.com/Alec-Raymond/persona_project">Project</a>
          <button onClick={() => input.current?.click()}>Open conversation</button>
          <input ref={input} type="file" accept=".json,application/json" multiple hidden onChange={event => void openFiles(event.target.files)} />
        </div>
      </header>
      {error && <p className="error" role="alert">{error}</p>}
      {!run ? <section className="empty">
        <h2>{loading ? 'Loading conversations…' : 'No conversations selected yet'}</h2>
        <p>Record a conversation in the local chat, then use <strong>Export conversation</strong> after at least two turns.</p>
        <button className="primary" onClick={() => input.current?.click()}>Open exported conversation</button>
        <p className="meta">Opened files stay in this browser tab. They are not uploaded or published.</p>
      </section> : <>
        <section className="toolbar" aria-label="Replay controls">
          <label>Conversation
            <select value={selected} onChange={event => { setSelected(Number(event.target.value)); move(0); }}>
              {runs.map((run, index) => <option key={run.id} value={index}>{run.title}</option>)}
            </select>
          </label>
          <div className="steps">
            <button disabled={turnIndex === 0} onClick={() => move(turnIndex - 1)}>Previous</button>
            <span aria-live="polite">Turn {turnIndex + 1} of {run.turns.length}</span>
            <button disabled={turnIndex === run.turns.length - 1} onClick={() => move(turnIndex + 1)}>Next</button>
            <button onClick={() => { if (turnIndex === run.turns.length - 1) setTurnIndex(0); setPlaying(!playing); }}>
              {playing ? 'Pause' : 'Replay'}
            </button>
          </div>
        </section>
        <div className="workspace">
          <section className="conversation" aria-label="Conversation transcript">
            <h2>Conversation <span className="meta">{run.persona}</span></h2>
            {run.turns.slice(0, turnIndex + 1).map((turn, index) => <article key={index} className={index === turnIndex ? 'exchange current' : 'exchange'}>
              <button className="turn-link" onClick={() => move(index)}>Turn {index + 1}</button>
              <div className="utterance"><span className="speaker">You</span><p>{turn.input_text}</p></div>
              <div className="utterance persona"><span className="speaker">{run.persona}</span><p>{turn.response}</p></div>
            </article>)}
          </section>
          {turn && <section className="inspection" aria-label="Turn details" key={`${run.id}-${turnIndex}`}>
            <h2>Inside turn {turnIndex + 1}</h2>
            <p className="meta">{turn.calls.length} model calls · {Math.round(turn.totals?.elapsed_s ?? 0)} seconds · gpt-6-astra</p>
            <details><summary>Selected machines</summary><Text value={{ fired: turn.fired, relevance_picks: turn.relevance_picks, random_picks: turn.random_picks, selection_scores: turn.selection_scores }} /></details>
            <details><summary>Machine outputs</summary>{Object.entries(turn.machine_outputs ?? {}).map(([name, output]) => <section className="item" key={name}><h3>{name}</h3><Text value={output} /></section>)}</details>
            <details><summary>Group syntheses</summary><Text value={turn.groups} /></details>
            <details><summary>State before and after</summary><h3>Before</h3><Text value={turn.bwo_before} /><h3>After</h3><Text value={turn.bwo_after} /><h3>Edits</h3><Text value={turn.edits} /></details>
            <details><summary>Draft and fit checks</summary><h3>Draft</h3><Text value={turn.draft_response} /><h3>Fit checks</h3><Text value={turn.fit_reviews} /></details>
            <details><summary>Recorded model calls</summary><p className="meta">Application prompts and returned outputs. Additional Codex context is not recorded here.</p>{turn.calls.map((call, index) => <details className="call" key={index}><summary>{index + 1}. {call.stage} · {call.label}</summary><Text value={call} /></details>)}</details>
          </section>}
        </div>
      </>}
    </main>
  );
}
