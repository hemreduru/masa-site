"""Writes video/scene-<lang>.html: the Masa window playing one real flow, driven by a timeline. Recorded by rec.mjs."""
import sys, html
sys.path.insert(0, '..')
import mock
e = html.escape
COPIED = {"tr": "Kopyalandı", "en": "Copied"}

def page(lang):
    m = mock.M[lang]
    plans = "".join(
        f'<div class="pl{" mid" if i == 1 else ""} v-in"><b>{e(n)}</b><strong>{e(p)}<small>{e(m["per"])}</small></strong>' + "".join(f"<span>{e(f)}</span>" for f in fs) + "</div>"
        for i, (n, p, fs) in enumerate(m["plans"]))
    tabs = "".join(f'<span class="{"on" if i == 2 else ""}">{e(v)}</span>' for i, v in enumerate(m["versions"]))
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<link rel="stylesheet" href="/css/mock.css">
<style>
@font-face{{font-family:"Switzer";src:url("/fonts/switzer-400.woff2") format("woff2");font-weight:400}}
@font-face{{font-family:"Switzer";src:url("/fonts/switzer-500.woff2") format("woff2");font-weight:500}}
html,body{{margin:0;background:#97aaf6;font-family:"Switzer",system-ui,sans-serif;height:100%}}
.mock{{aspect-ratio:auto;height:100vh;border-radius:0;position:relative}}
.mock .win{{font-size:15.5px}}
.hid{{opacity:0;transform:translateY(10px)}}
.show{{opacity:1;transform:none;transition:opacity .45s cubic-bezier(.2,.7,.2,1),transform .45s cubic-bezier(.2,.7,.2,1)}}
.mock .th{{justify-content:flex-start}}
.mock .as{{gap:.7em}}
.pane{{flex:0 0 0;width:0;overflow:hidden;background:#f6f6f5;transition:flex-basis .9s cubic-bezier(.2,.7,.2,1);display:flex}}
.pane.open{{flex-basis:50%}}
.pane .ap{{min-width:0;width:100%;flex:none}}
.pane .pv{{flex:1;display:flex;align-items:center;justify-content:center;padding:1.6em;min-width:0}}
.pane .pg{{display:grid;grid-template-columns:repeat(3,1fr);gap:.8em;width:100%}}
.v-in{{opacity:0;transform:translateY(16px);transition:opacity .5s cubic-bezier(.2,.7,.2,1),transform .5s cubic-bezier(.2,.7,.2,1)}}
.v-in.on{{opacity:1;transform:none}}
.caret{{display:inline-block;width:2px;height:1.1em;background:#2a2a28;vertical-align:-.2em;margin-left:1px;animation:b 1s steps(2) infinite}}
@keyframes b{{50%{{opacity:0}}}}
.cursor{{position:absolute;left:0;top:0;width:22px;height:30px;z-index:9;pointer-events:none;transition:transform .8s cubic-bezier(.4,.1,.2,1);transform:translate(40%,90%)}}
.cursor::before{{content:"";position:absolute;inset:0;background:#111;clip-path:polygon(0 0,0 85%,24% 66%,40% 100%,56% 92%,40% 60%,72% 60%);}}
.cursor::after{{content:"";position:absolute;inset:1.5px;background:#fff;clip-path:polygon(0 0,0 85%,24% 66%,40% 100%,56% 92%,40% 60%,72% 60%);z-index:-1;transform:scale(1.18);transform-origin:0 0}}
.bt.press{{transform:scale(.94);transition:transform .12s}}
.mock .th .us{{white-space:pre-wrap}}
</style></head><body>
<div class="mock" id="m"><div class="win">
<div class="tb"><i class="lg"></i><b>Masa</b><span id="ttl">{e(m['proj'])}</span></div>
<div class="bd">
{mock._sidebar(m, 0).replace('class="on"', 'class=""', 1)}
<div class="mn" id="main"><div class="mh"><b id="ct">{e(m['new'])}</b><span class="chip">{e(m['chip'])}</span></div>
<div class="th" id="th"></div>
<div class="cp"><p id="inp"><span style="color:#8a8a85">{e(m['ph'])}</span></p><div class="cr"><span class="pill">+</span><span class="pill">{e(m['think'])}</span><span class="pill">{e(m['web'])}</span><span class="md">{e(m['model'])}</span></div></div></div>
<div class="pane" id="pane"><div class="ap"><div class="ah"><b>{e(m['art_h'])}</b><span class="vs">{tabs}</span><span class="bt s" id="cpy">{e(m['copy'])}</span><span class="bt s">{e(m['save'])}</span></div><div class="pv"><div class="pg" id="pg">{plans}</div></div></div></div>
</div><i class="cursor" id="cur"></i></div></div>
<script>
const Q={m['q']!r}, A1={m['a1']!r}, A2={m['a2']!r}, CARD={m['art_card']!r}, META={m['art_meta']!r}, TITLE={m['chat_title']!r}, COPIED={COPIED[lang]!r};
const $=id=>document.getElementById(id), sleep=ms=>new Promise(r=>setTimeout(r,ms));
function moveTo(el,dx=.5,dy=.5){{const r=el.getBoundingClientRect(),b=$('m').getBoundingClientRect();$('cur').style.transform=`translate(${{r.left-b.left+r.width*dx}}px,${{r.top-b.top+r.height*dy}}px)`}}
async function type(el,txt,cps){{for(let i=1;i<=txt.length;i++){{el.innerHTML=txt.slice(0,i).replace(/</g,'&lt;')+'<span class="caret"></span>';await sleep(1000/cps+(Math.random()*18))}}}}
async function stream(p,txt){{const w=txt.split(' ');let s='';for(const x of w){{s+=(s?' ':'')+x;p.textContent=s;await sleep(55)}}}}
(async()=>{{
 window.__go=false;
 await sleep(500); moveTo($('inp'),.3,.5); await sleep(900);
 const inp=$('inp'); await type(inp,Q,24); await sleep(500);
 inp.innerHTML='<span style="color:#8a8a85">{e(m['ph'])}</span>';
 const th=$('th');
 const us=document.createElement('p'); us.className='us hid'; us.textContent=Q; th.appendChild(us); $('ct').textContent=TITLE; $('ttl').textContent=TITLE;
 requestAnimationFrame(()=>us.classList.add('show')); await sleep(700);
 const as=document.createElement('div'); as.className='as'; th.appendChild(as);
 const p1=document.createElement('p'),p2=document.createElement('p'); as.append(p1,p2);
 await stream(p1,A1); await sleep(250); await stream(p2,A2); await sleep(350);
 const ac=document.createElement('div'); ac.className='ac hid'; ac.innerHTML='<i class="gl"></i><span><b>'+CARD+'</b><small>'+META+'</small></span>'; as.appendChild(ac);
 requestAnimationFrame(()=>ac.classList.add('show')); await sleep(900);
 moveTo(ac,.5,.5); await sleep(900); ac.style.background='#fff'; await sleep(250);
 $('pane').classList.add('open'); await sleep(1000);
 [...document.querySelectorAll('#pg .pl')].forEach((c,i)=>setTimeout(()=>c.classList.add('on'),i*160));
 await sleep(1700);
 const cp=$('cpy'); moveTo(cp,.5,.5); await sleep(1000); cp.classList.add('press'); await sleep(150); cp.classList.remove('press'); cp.textContent=COPIED; await sleep(2300);
 window.__done=true;
}})();
</script></body></html>"""

for lang in ("tr", "en"):
    open(f"scene-{lang}.html", "w").write(page(lang))
print("ok")
