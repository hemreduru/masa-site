"""Motion-graphics scenes: the Masa window plays one flow with camera moves and call-out tags.
Writes s-<scene>-<lang>.html. Recorded by rec2.mjs (desktop 1280x800, phone 960x900)."""
import sys, json, html
sys.path.insert(0, '..')
import mock
e = html.escape

T = {
 "tr": {"models": ["OpenAI uyumlu herhangi bir adres", "Modeller kendiliğinden gelir", "Varsayılanı sen seçersin"],
        "project": ["Her sohbet bu talimatla başlar", "Dosyalar projeye bağlı", "Sohbetler bir arada"],
        "artifact": ["Üç sürüm, tek tıkla gez", "Panoya kopyalandı", "Dosyaya kaydedildi"],
        "mcp": ["Mevcut MCP ayarını içe aktar", "Sunucular modele araç olur"],
        "update": ["Arka planda iner", "Tek düğmeyle kurulur"],
        "dl": "İndiriliyor", "copied": "Kopyalandı", "saved": "Kaydedildi", "restarting": "Yeniden başlıyor…", "count": "araç", "conn": "bağlı"},
 "en": {"models": ["Any OpenAI-compatible address", "Models load by themselves", "You choose the default"],
        "project": ["Every chat starts with this brief", "Files belong to the project", "Chats stay together"],
        "artifact": ["Three versions, one click apart", "Copied to the clipboard", "Saved to a file"],
        "mcp": ["Import your existing MCP config", "Servers become tools for the model"],
        "update": ["Downloads in the background", "Installs with one button"],
        "dl": "Downloading", "copied": "Copied", "saved": "Saved", "restarting": "Restarting…", "count": "tools", "conn": "connected"},
}

LIB = r"""
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)],sleep=ms=>new Promise(r=>setTimeout(r,ms));
const stage=$('#stage');
const K=()=>stage.getBoundingClientRect().width/stage.offsetWidth;
function pos(el,fx=.5,fy=.5){const r=el.getBoundingClientRect(),s=stage.getBoundingClientRect(),k=K();return{x:(r.left-s.left+r.width*fx)/k,y:(r.top-s.top+r.height*fy)/k}}
function cam(el,z=1.55,fx=.5,fy=.5){if(document.body.classList.contains('mob'))z=1;const W=stage.offsetWidth,H=stage.offsetHeight;if(!el||z===1){stage.style.transform='translate(0px,0px) scale(1)';return}
 const p=pos(el,fx,fy);let tx=W/2-p.x*z,ty=H/2-p.y*z;tx=Math.min(0,Math.max(W-W*z,tx));ty=Math.min(0,Math.max(H-H*z,ty));stage.style.transform=`translate(${tx}px,${ty}px) scale(${z})`}
function cur(el,fx=.5,fy=.5){const p=pos(el,fx,fy);$('#cur').style.transform=`translate(${p.x}px,${p.y}px)`}
async function press(el){el.classList.add('press');await sleep(170);el.classList.remove('press')}
function tag(el,txt,fx=0,fy=0,dx=0,dy=-58){const p=pos(el,fx,fy),t=document.createElement('div');t.className='tag';t.textContent=txt;t.style.left=(p.x+dx)+'px';t.style.top=(p.y+dy)+'px';stage.appendChild(t);{const W=stage.offsetWidth,H=stage.offsetHeight,w=t.offsetWidth,h=t.offsetHeight;const m=/translate\((-?[\d.]+)px,\s*(-?[\d.]+)px\)\s*scale\(([\d.]+)\)/.exec(stage.style.transform)||[0,0,0,1];const z=+m[3],vx0=-m[1]/z,vy0=-m[2]/z,vx1=vx0+W/z,vy1=vy0+H/z;let l=p.x+dx,tp=p.y+dy;if(l+w>vx1-14)l=vx1-14-w;if(l<vx0+14)l=vx0+14;if(tp<vy0+14)tp=vy0+14;if(tp+h>vy1-14)tp=vy1-14-h;t.style.left=l+'px';t.style.top=tp+'px'}requestAnimationFrame(()=>requestAnimationFrame(()=>t.classList.add('on')));return t}
function untag(t){t.classList.remove('on');setTimeout(()=>t.remove(),500)}
async function type(el,txt,cps=26){for(let i=1;i<=txt.length;i++){el.innerHTML=txt.slice(0,i).replace(/</g,'&lt;')+'<span class="caret"></span>';await sleep(1000/cps+Math.random()*14)}el.textContent=txt}
const show=(el,d=0)=>setTimeout(()=>el.classList.add('on'),d);
async function boot(){if(location.search.includes('m=1'))document.body.classList.add('mob');await document.fonts.ready;stage.style.opacity=0;await sleep(250);stage.style.opacity=1;await sleep(500)}
async function finish(){cam(null);cur($('.win'),.5,.9);await sleep(1500);stage.style.opacity=0;await sleep(600);window.__done=true}
"""

CSS = """
@font-face{font-family:"Switzer";src:url("/fonts/switzer-400.woff2") format("woff2");font-weight:400}
@font-face{font-family:"Switzer";src:url("/fonts/switzer-500.woff2") format("woff2");font-weight:500}
html,body{margin:0;height:100%;background:#ececea;font-family:"Switzer",system-ui,sans-serif;overflow:hidden}
.mock{aspect-ratio:auto;height:100vh;border-radius:0;position:relative;background:#ececea}
#stage{position:absolute;left:0;top:0;width:100%;height:100%;transform-origin:0 0;transform:translate(0,0) scale(1);transition:transform 1.35s cubic-bezier(.5,0,.15,1),opacity .5s;font-size:19px}
.mock .win{font-size:19px}
body.mob #stage,body.mob .mock .win{font-size:15px}
body.mob .sb{display:none}
.v-in{opacity:0;transform:translateY(14px);transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}
.v-in.on{opacity:1;transform:none}
.caret{display:inline-block;width:2px;height:1.1em;background:#2a2a28;vertical-align:-.2em;margin-left:1px;animation:b 1s steps(2) infinite}
@keyframes b{50%{opacity:0}}
.cursor{position:absolute;left:0;top:0;width:24px;height:32px;z-index:9;pointer-events:none;transition:transform .85s cubic-bezier(.4,.1,.2,1);transform:translate(40%,90%)}
.cursor::before{content:"";position:absolute;inset:0;background:#111;clip-path:polygon(0 0,0 85%,24% 66%,40% 100%,56% 92%,40% 60%,72% 60%)}
.press{transform:scale(.93)!important;transition:transform .12s!important}
.tag{position:absolute;z-index:8;background:#fed878;color:#0d0d0d;font:500 1em/1 "Switzer",sans-serif;padding:.7em 1em;border-radius:.8em;box-shadow:0 0 0 2px #0d0d0d;white-space:nowrap;opacity:0;transform:scale(.85) translateY(8px);transform-origin:0 100%;transition:opacity .35s,transform .45s cubic-bezier(.2,.9,.3,1.2)}
.tag.on{opacity:1;transform:none}
.mock .fd{min-height:2.4em}
.mock .ml li{transition:background .3s}
.mock .ml li.hl{background:#fff}
.mock .pb i{transition:width 3.2s linear}
.mock .bt.s{transition:background .2s}
"""

SCENES = {}

SCENES["models"] = r"""
const t=T.models, fds=$$('.fd'), addr=fds[0], key=fds[1], btn=$('.mn .bt'), fn=$('.fn'), rows=$$('.ml li');
const A=addr.textContent, KY=key.textContent; addr.textContent=''; key.textContent='';
fn.style.opacity=0; fn.style.transition='opacity .5s'; rows.forEach(r=>r.classList.add('v-in'));
rows.forEach(r=>r.classList.remove('on')); const em=document.createElement('em'); em.textContent=DEF; 
(async()=>{await boot();
 cam(addr,1.5,.5,.5);cur(addr,.1,.5);await sleep(1100);
 const t1=tag(addr,t[0],0,0,0,-64); await type(addr,A,24); await sleep(900); untag(t1);
 cur(key,.15,.5);await sleep(900);await type(key,KY,22);await sleep(500);
 cam(btn,1.5,.5,.2);cur(btn);await sleep(1300);await press(btn);fn.style.opacity=1;
 await sleep(500);cam($('.ml'),1.5,.5,.4);rows.forEach((r,i)=>show(r,i*260));await sleep(1000);
 rows[0].classList.add('on');rows[0].append(em);const t2=tag($('.ml'),t[1],0,0,0,-66);await sleep(1700);untag(t2);
 cur(rows[1],.4,.5);await sleep(1000);await press(rows[1]);rows[0].classList.remove('on');em.remove();rows[1].classList.add('on');rows[1].append(em);
 const t3=tag(rows[1],t[2],.45,0,0,-64);await sleep(1900);untag(t3);
 await finish()})();
"""

SCENES["project"] = r"""
const t=T.project, fd=$('.fd.tall'), lists=$$('.ml'), files=lists[0], chats=lists[1], TXT=fd.textContent;
fd.textContent=''; [...files.children,...chats.children].forEach(r=>r.classList.add('v-in'));
(async()=>{await boot();
 cam(fd,1.55,.5,.5);cur(fd,.12,.4);await sleep(1100);
 const t1=tag(fd,t[0],0,0,0,-64);await type(fd,TXT,26);await sleep(1100);untag(t1);
 cam(files,1.5,.5,.4);cur(files.children[0],.5,.5);await sleep(1200);
 [...files.children].forEach((r,i)=>show(r,i*320));const t2=tag(files,t[1],0,0,0,-64);await sleep(1900);untag(t2);
 cam(chats,1.5,.5,.3);cur(chats.children[0],.4,.5);await sleep(1200);
 [...chats.children].forEach((r,i)=>show(r,i*320));await sleep(800);
 const t3=tag(chats,t[2],0,0,0,-64);chats.children[0].classList.add('hl');await sleep(900);chats.children[0].classList.remove('hl');chats.children[1].classList.add('hl');await sleep(1100);chats.children[1].classList.remove('hl');untag(t3);
 await finish()})();
"""

SCENES["artifact"] = r"""
const t=T.artifact, cards=$$('.pl'), tabs=$$('.vs span'), btns=$$('.ah .bt.s'), vs=$('.vs');
cards.forEach(c=>c.classList.add('v-in'));
async function deal(){cards.forEach(c=>c.classList.remove('on'));await sleep(220);cards.forEach((c,i)=>show(c,i*170))}
function pick(i){tabs.forEach((x,j)=>x.classList.toggle('on',j===i))}
(async()=>{await boot();pick(0);
 cam($('.pv'),1.25,.5,.5);cur($('.pv'),.8,.3);await sleep(900);await deal();await sleep(1500);
 cam(vs,1.7,.7,.5);cur(tabs[1]);await sleep(1200);const t1=tag(vs,t[0],.2,0,-120,-64);
 await press(tabs[1]);pick(1);await deal();await sleep(1100);
 cur(tabs[2]);await sleep(900);await press(tabs[2]);pick(2);await deal();await sleep(1300);untag(t1);
 cam(btns[0],1.7,.9,.5);cur(btns[0]);await sleep(1300);await press(btns[0]);btns[0].textContent=COPIED;const t2=tag(btns[0],t[1],.5,0,-130,-64);await sleep(1800);untag(t2);
 cur(btns[1]);await sleep(900);await press(btns[1]);btns[1].textContent=SAVED;const t3=tag(btns[1],t[2],.5,0,-110,-64);await sleep(1800);untag(t3);
 await finish()})();
"""

SCENES["mcp"] = r"""
const t=T.mcp, rows=$$('.ml li'), btn=$('.mn .bt'), mn=$('.mn.pad');
const cd=document.createElement('div');cd.className='cd';cd.style.cssText='overflow:hidden;max-height:0;padding-top:0;padding-bottom:0;margin-top:0;transition:max-height .7s,padding .7s,margin .7s';cd.textContent='';btn.after(cd);
const ems=rows.map(r=>r.querySelector('em')),counts=ems.map(x=>parseInt(x.textContent.split('·')[1])); ems.forEach(x=>x.textContent='…');
rows.forEach(r=>r.classList.add('v-in'));
async function count(i){for(let n=0;n<=counts[i];n++){ems[i].textContent=CONN+' · '+n+' '+TOOLS;await sleep(110)}}
(async()=>{await boot();
 cam(btn,1.45,.5,.5);cur(btn);await sleep(1300);const t1=tag(btn,t[0],0,0,0,-64);await press(btn);
 cd.style.maxHeight='20em';cd.style.padding='.9em 1.1em';cd.style.marginTop='.8em';await sleep(500);
 cam(cd,1.5,.5,.5);await type(cd,CFG,90);await sleep(900);untag(t1);
 cd.style.maxHeight='0';cd.style.padding='0 1.1em';cd.style.marginTop='0';await sleep(800);
 cam($('.ml'),1.5,.5,.5);rows.forEach((r,i)=>show(r,i*400));
 for(let i=0;i<rows.length;i++){await sleep(i?200:600);await count(i)}
 const t2=tag($('.ml'),t[1],0,0,0,-66);await sleep(2000);untag(t2);
 await finish()})();
"""

SCENES["update"] = r"""
const t=T.update, uc=$('.uc'), pb=$('.pb i'), small=$('.uc small'), restart=$('.bt.acc'), sw=$('.sw'), b=uc.querySelector('b');
pb.style.width='0%';small.textContent='';restart.style.opacity=0;restart.style.transition='opacity .5s';sw.style.opacity=.35;sw.style.transition='opacity .5s';
(async()=>{await boot();
 cam(uc,1.5,.5,.5);cur(uc,.7,.3);await sleep(1000);
 const t1=tag(uc,t[0],0,0,0,-64);small.textContent=DL+' 0%';pb.style.width='100%';
 const t0=Date.now();const iv=setInterval(()=>{const p=Math.min(100,Math.round((Date.now()-t0)/3200*100));small.textContent=p<100?DL+' '+p+'%':DLDONE},120);
 await sleep(3500);clearInterval(iv);small.textContent=DLDONE;untag(t1);
 restart.style.opacity=1;await sleep(900);const t2=tag(restart,t[1],0,0,0,-64);cur(restart);await sleep(1300);
 await press(restart);restart.textContent=RESTARTING;await sleep(1700);untag(t2);
 cam(sw,1.7,.5,.5);sw.style.opacity=1;cur(sw);await sleep(1600);
 await finish()})();
"""

BUILD = {"models": mock.models, "project": mock.project, "artifact": mock.artifact, "mcp": mock.mcp,
         "update": lambda lang, alt: mock.update(lang, alt, "0.1.9")}

def page(scene, lang):
    m = mock.M[lang]; t = T[lang]
    s = BUILD[scene](lang, "")
    s = s.replace('<div class="win" aria-hidden="true">', '<div id="stage"><div class="win">', 1)
    i = s.rfind('</div>')
    s = s[:i] + '<i class="cursor" id="cur"></i></div>' + s[i:]
    s = s.replace(' role="img" aria-label=""', '')
    consts = (f"const T={json.dumps(t, ensure_ascii=False)};const DEF={json.dumps(m['default'], ensure_ascii=False)};"
              f"const COPIED={json.dumps(t['copied'], ensure_ascii=False)},SAVED={json.dumps(t['saved'], ensure_ascii=False)},"
              f"RESTARTING={json.dumps(t['restarting'], ensure_ascii=False)},DL={json.dumps(t['dl'], ensure_ascii=False)},"
              f"DLDONE={json.dumps(m['dl_done'], ensure_ascii=False)},CONN={json.dumps(t['conn'], ensure_ascii=False)},"
              f"TOOLS={json.dumps(t['count'], ensure_ascii=False)},CFG={json.dumps(chr(10).join(mock.CONFIG), ensure_ascii=False)};")
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><link rel="stylesheet" href="/css/mock.css"><style>{CSS}</style></head><body>{s}<script>{consts}{LIB}{SCENES[scene]}</script></body></html>"""

for sc in SCENES:
    for lang in ("tr", "en"):
        open(f"s-{sc}-{lang}.html", "w").write(page(sc, lang))
print("ok", len(SCENES) * 2)
