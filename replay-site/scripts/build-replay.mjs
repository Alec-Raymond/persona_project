import { readFile, writeFile, mkdir, cp, rm } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const root = new URL('../', import.meta.url);
const source = await readFile(new URL('../viewer/live.html', root), 'utf8');
const marker = '// ---- wiring ----';
if (source.split(marker).length !== 2) throw new Error('The shared replay wiring marker changed.');
let html = source.slice(0, source.indexOf(marker));
html = html.replace('<title>Sam · Conversation</title>', '<title>Conversations</title>');
html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="icon" href="./favicon.svg">');
html = html.replace('<h1 id="pname">Sam</h1>', '<h1 id="pname">Conversations</h1>');
html = html.replace('<button id="newBtn">New chat</button>', '<button id="newBtn">Restart</button>');
html = html.replace('>Export conversation</button>', '>Export</button>');
html = html.replace('  <div id="transcript"></div>', `  <div id="turnBar"><button id="previousBtn" aria-label="Previous turn">←</button><select id="turnSel" aria-label="Turn"></select><button id="nextBtn" aria-label="Next turn">→</button><button id="pauseBtn">Pause</button></div>\n  <div id="transcript"></div>`);
html = html.replace(/  <div id="composer">[\s\S]*?<\/div>/, `  <div id="composer"><button id="send" hidden></button><button id="openBtn">Open file</button><input id="fileInput" type="file" accept=".json,application/json" multiple hidden><a href="https://github.com/Alec-Raymond/persona_project">GitHub</a></div>`);
html = html.replace('</style>', `\n#turnBar{display:flex;gap:6px;padding:8px 16px;border-bottom:1px solid var(--line)}
#turnBar button,#turnBar select{font:inherit;font-size:12px;padding:4px 10px;border:1px solid var(--line);border-radius:4px;background:#fff;cursor:pointer}
#turnSel{flex:1;min-width:0}#composer{align-items:center;justify-content:space-between;min-height:60px}
#composer button{padding:9px 18px}#composer a{font-size:13px;color:var(--muted)}
#transcript .empty{margin:auto;color:var(--muted);font-size:14px;padding:20px 0}
@media(max-width:760px){body{grid-template-columns:1fr;grid-template-rows:44vh 56vh}#chat,#pipe{height:100%;min-height:0}#pipe{padding:18px 16px}.groupcol{min-width:min(320px,100%)}}
</style>`);
html += `
</script>
<script type="module" src="./replay-page.js"></script>
</body>
</html>\n`;
const output = new URL('dist/client/', root);
await rm(output, { recursive: true, force: true });
await mkdir(output, { recursive: true });
await cp(new URL('public/', root), output, { recursive: true });
for (const name of ['trace-data.mjs', 'replay-events.mjs', 'replay-page.mjs']) {
  const code = await readFile(new URL(`lib/${name}`, root), 'utf8');
  await writeFile(new URL(name.replace('.mjs', '.js'), output), code.replaceAll('.mjs\'', '.js\''));
}
await writeFile(new URL('index.html', output), html);
await writeFile(new URL('.nojekyll', output), '');
console.log(`Built shared machine replay at ${fileURLToPath(output)}`);
