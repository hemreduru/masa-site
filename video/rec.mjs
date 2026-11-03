import { chromium } from '/srv/projeler/masa/node_modules/playwright/index.mjs'
const lang = process.argv[2] || 'tr'
const b = await chromium.launch({ executablePath: process.env.CHROME_PATH })
const ctx = await b.newContext({ viewport: { width: 1280, height: 800 }, recordVideo: { dir: `/tmp/vid-${lang}`, size: { width: 1280, height: 800 } } })
const page = await ctx.newPage()
await page.goto(`http://127.0.0.1:8099/video/scene-${lang}.html`)
await page.waitForFunction('window.__done===true', null, { timeout: 40000 })
await page.waitForTimeout(500)
await page.screenshot({ path: `/tmp/vid-${lang}/last.png` })
await ctx.close(); await b.close()
console.log('rec done', lang)
