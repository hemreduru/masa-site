import { chromium } from '/srv/projeler/masa/node_modules/playwright/index.mjs'
import fs from 'node:fs'
const only = process.argv[2] ? process.argv[2].split(',') : ['models','project','artifact','mcp','update']
const b = await chromium.launch({ executablePath: process.env.CHROME_PATH })
for (const sc of only) for (const lang of ['tr','en']) for (const [v, w, h] of [['d',1280,800],['m',540,600]]) {
  const dir = `/tmp/rec/${sc}-${lang}-${v}`; fs.rmSync(dir, { recursive: true, force: true })
  const ctx = await b.newContext({ viewport: { width: w, height: h }, recordVideo: { dir, size: { width: w, height: h } } })
  const p = await ctx.newPage(); const errs = []
  p.on('pageerror', e => errs.push(String(e))); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()) })
  await p.goto(`http://127.0.0.1:8099/video/s-${sc}-${lang}.html${v === 'm' ? '?m=1' : ''}`)
  try { await p.waitForFunction('window.__done===true', null, { timeout: 45000 }) } catch (e) { errs.push('TIMEOUT') }
  await ctx.close()
  console.log('rec', sc, lang, v, errs.length ? 'ERR ' + errs.join('|').slice(0, 200) : 'ok'); 
}
await b.close(); console.log('ALLREC')
