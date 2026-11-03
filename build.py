#!/usr/bin/env python3
"""Static generator for the Masa site (TR + EN). Output: ./public"""
import os, json, shutil, datetime, html
import mock

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
BASE = "https://masa.hursit.me"
INDEXABLE = os.environ.get("INDEXABLE", "0") == "1"
TODAY = datetime.date.today().isoformat()
VERSION = os.environ.get("MASA_VERSION", "0.1.9")
EMAIL = "contact@hursit.me"

e = html.escape

COPY = {
    "tr": {
        "lang": "tr", "prefix": "", "alt_prefix": "/en",
        "title": "Masa: her modelle konuşan masaüstü sohbet uygulaması",
        "desc": "Masa, Windows ve Linux için masaüstü sohbet uygulaması. Kendi API adresini gir, modellerini seç; projeler, artifact önizlemesi, dosya araçları ve MCP hazır.",
        "nav": [("#neler", "Neler var"), ("#sss", "Sorular"), ("#indir", "İndir")],
        "tagline": "Her modelle konuşan masaüstü sohbet uygulaması. Windows ve Linux için.",
        "cta": "İndir",
        "hero_alt": "Masa uygulamasında bir proje sohbeti: solda projeler ve sohbetler, ortada karşılama, altta mesaj kutusu",
        "feat_h": "Neler var",
        "feats": [
            ("models", "Kendi adresin, kendi modellerin.",
             "OpenAI uyumlu herhangi bir adresi ve anahtarı gir. Masa modelleri kendisi getirir; hangisinin varsayılan olacağını sen seçersin.",
             "Ayarlar ekranı: API adresi, anahtar ve model listesi"),
            ("hero", "Projeler konuyu hatırlar.",
             "Bir projeye talimat yaz, dosya ya da klasör ekle. O projedeki her sohbet aynı bağlamla başlar.",
             "Proje içindeki bir sohbet"),
            ("artifact", "Ürettiği şeyi hemen görürsün.",
             "HTML, React, SVG ve Mermaid çıktıları kutulu bir önizlemede açılır. Sürümler arasında gezer, kopyalar, kaydedersin.",
             "Bir fiyat tablosu artifact olarak üretilmiş"),
            ("mcp", "Araçlar ve MCP sunucuları.",
             "Dosya oluşturma, web sayfası okuma ve isteğe bağlı web araması hazır. Mevcut MCP ayarını içe aktar, sunucuların modele araç olarak açılsın.",
             "MCP sunucuları ekranı ve örnek ayar"),
            ("update", "Kendini güncel tutar.",
             "Yeni sürüm çıkınca arka planda iner. Bittiğinde tek düğmeyle yeniden başlatıp kurarsın.",
             "Güncellemeler ekranı"),
        ],
        "ask_h": "Sormadan yazmaz.",
        "ask_p": "Model bir dosya oluşturmak ya da değiştirmek istediğinde Masa önce sana sorar. İzin verirsin, o sohbet için hep izin verirsin ya da reddedersin. Ayarlardan “sormadan yap” da seçebilirsin. Aşağıdaki kart gerçek istemin aynısı: bir düğmeye bas.",
        "ask_title": "Masa bir dosya işlemi yapmak istiyor",
        "ask_what": "Dosya oluştur / üzerine yaz: notlar.txt",
        "ask_btns": ("İzin ver", "Bu sohbette hep izin ver", "Reddet"),
        "ask_files": "Klasör",
        "ask_wait": "notlar.txt: karar bekleniyor",
        "ask_ok": "notlar.txt: yazıldı",
        "ask_always": "notlar.txt: yazıldı, bu sohbette sormayacak",
        "ask_no": "notlar.txt: yazılmadı",
        "ask_reset": "Yeniden dene",
        "how_h": "Üç adım",
        "how": [
            ("Önce, kur.", "Windows'ta indirdiğin dosyayı çalıştır. Linux'ta tek komut:",
             "code", "sudo apt install ./masa_amd64.deb", None),
            ("Sonra, adresi gir.", "Ayarlar, Sağlayıcılar ve modeller. Adres ve anahtar yeter.",
             "field", "https://api.example.com/v1", "models"),
            ("Sonra, iste.", "Ne istediğini yaz. Cevap bir artifact ise yanında açılır.",
             "field", "3 sütunlu bir fiyat tablosu yap", "artifact"),
        ],
        "how_copy": "Kopyala", "how_copied": "Kopyalandı",
        "faq_h": "Sorular",
        "faq": [
            ("Hangi modellerle çalışır?",
             "OpenAI uyumlu bir sohbet adresi olan her model ve sağlayıcıyla. Adresi ve anahtarı Ayarlar'a girersin, model listesini Masa getirir."),
            ("Sohbetlerim nerede duruyor?",
             "Sohbetler, projeler ve artifact'lar bu bilgisayardaki yerel bir veritabanında saklanır. Masa yalnızca senin girdiğin adrese istek atar. Güncelleme denetimi de güncelleme sunucusuna gider."),
            ("Hangi sistemlerde çalışır?",
             "Windows 10 ve üzeri ile Linux (Debian ve Ubuntu için .deb paketi). macOS sürümü henüz yok."),
            ("Windows neden “bilinmeyen yayıncı” uyarısı veriyor?",
             "Kurulum dosyası henüz imzalı değil. Uyarıda “Daha fazla bilgi”, sonra “Yine de çalıştır” dersen kurulur."),
            ("Ücretli mi?",
             "Şu an erken sürüm olarak indirilebiliyor. Fiyatlandırma kararı henüz yok; olursa buradan duyurulur."),
            ("Güncellemeler nasıl geliyor?",
             "Masa yeni sürümü arka planda indirir. Ayarlar'daki Güncellemeler ekranından elle de denetleyebilirsin."),
        ],
        "cta_q1": "Windows", "cta_or": "ya da", "cta_q2": "Linux?",
        "cta_win": "Windows için indir", "cta_lin": "Linux için indir",
        "cta_note": f"Sürüm {VERSION}. Kurulumdan sonra uygulama kendini günceller.",
        "foot_what": "Masaüstü sohbet uygulaması",
        "foot_links": [("/gizlilik/", "Gizlilik"), (f"mailto:{EMAIL}", "İletişim")],
        "foot_right": "Gizlilik",
        "priv_title": "Gizlilik | Masa",
        "priv_desc": "Masa hangi veriyi nerede tutar, neye istek atar ve ne toplamaz.",
        "priv_h": "Gizlilik",
        "priv_blocks": [
            ("Bu bilgisayarda kalanlar", "Sohbetler, projeler, artifact'lar ve ayarların bu bilgisayardaki yerel bir veritabanında saklanır. Masa bunları kendi sunucusuna göndermez."),
            ("Dışarıya giden istekler", "Mesajların, yalnızca senin Ayarlar'a girdiğin API adresine gider. Web aracını açarsan model istediğinde ilgili web sayfasına, web aramasını açarsan seçtiğin arama sağlayıcısına istek atılır. Bir de güncelleme denetimi vardır: yalnızca sürüm dosyası okunur."),
            ("Toplamadıklarımız", "Masa kullanım istatistiği, çökme raporu ya da reklam kimliği göndermez. Bu siteyi de çerez ve izleyici olmadan sunuyoruz."),
            ("İletişim", f"Soru ya da silme talebi için: {EMAIL}"),
        ],
        "priv_home": "Ana sayfa",
        "alt_label": "English", "alt_path": "/en/", "self_path": "/",
        "priv_path": "/gizlilik/", "alt_priv_path": "/en/privacy/",
        "og_alt": "Masa uygulama ekranı",
        "ld_desc": "Windows ve Linux için masaüstü sohbet uygulaması. OpenAI uyumlu herhangi bir adresle çalışır; projeler, artifact önizlemesi, dosya araçları ve MCP içerir.",
        "menu": "Menü",
        "skip": "İçeriğe geç",
    },
    "en": {
        "lang": "en", "prefix": "/en", "alt_prefix": "",
        "title": "Masa: a desktop chat app that talks to any model",
        "desc": "Masa is a desktop chat app for Windows and Linux. Enter your own API address, pick your models; projects, artifact preview, file tools and MCP are built in.",
        "nav": [("#features", "Features"), ("#faq", "Questions"), ("#download", "Download")],
        "tagline": "A desktop chat app that talks to any model. For Windows and Linux.",
        "cta": "Download",
        "hero_alt": "A project chat in Masa: projects and chats on the left, a greeting in the middle, the message box below",
        "feat_h": "What's inside",
        "feats": [
            ("models", "Your address, your models.",
             "Enter any OpenAI-compatible address and key. Masa fetches the models itself; you choose which one is the default.",
             "Settings screen: API address, key and model list"),
            ("hero", "Projects remember the topic.",
             "Write instructions for a project, add files or a whole folder. Every chat in it starts with the same context.",
             "A chat inside a project"),
            ("artifact", "See what it makes, right away.",
             "HTML, React, SVG and Mermaid output opens in a sandboxed preview. Step through versions, copy, save.",
             "A pricing table generated as an artifact"),
            ("mcp", "Tools and MCP servers.",
             "File creation, reading web pages and optional web search are ready. Import an existing MCP config and its servers become tools for the model.",
             "The MCP servers screen with a sample config"),
            ("update", "Keeps itself current.",
             "New versions download in the background. When it is done, one button restarts and installs.",
             "The updates screen"),
        ],
        "ask_h": "It asks before it writes.",
        "ask_p": "When a model wants to create or change a file, Masa asks you first. Allow it, allow it for the whole chat, or refuse. You can pick “don't ask” in Settings. The card below is the real prompt: press a button.",
        "ask_title": "Masa wants to do a file action",
        "ask_what": "Create / overwrite file: notes.txt",
        "ask_btns": ("Allow", "Always allow in this chat", "Deny"),
        "ask_files": "Folder",
        "ask_wait": "notes.txt: waiting for your decision",
        "ask_ok": "notes.txt: written",
        "ask_always": "notes.txt: written, will not ask again in this chat",
        "ask_no": "notes.txt: not written",
        "ask_reset": "Try again",
        "how_h": "Three steps",
        "how": [
            ("First, install it.", "On Windows, run the file you downloaded. On Linux, one command:",
             "code", "sudo apt install ./masa_amd64.deb", None),
            ("Then, enter the address.", "Settings, Providers and models. An address and a key are enough.",
             "field", "https://api.example.com/v1", "models"),
            ("Then, ask.", "Type what you want. If the answer is an artifact, it opens next to it.",
             "field", "Make a 3-column pricing table", "artifact"),
        ],
        "how_copy": "Copy", "how_copied": "Copied",
        "faq_h": "Questions",
        "faq": [
            ("Which models does it work with?",
             "Any model or provider that offers an OpenAI-compatible chat address. Enter the address and key in Settings and Masa fetches the model list."),
            ("Where are my chats stored?",
             "Chats, projects and artifacts live in a local database on this computer. Masa only sends requests to the address you entered. The update check goes to the update server."),
            ("Which systems does it run on?",
             "Windows 10 and later, and Linux (a .deb package for Debian and Ubuntu). There is no macOS build yet."),
            ("Why does Windows show an “unknown publisher” warning?",
             "The installer is not signed yet. Choose “More info”, then “Run anyway” and it installs."),
            ("Does it cost anything?",
             "It is available as an early release for now. There is no pricing decision yet; if there is one, it will be announced here."),
            ("How do updates arrive?",
             "Masa downloads the new version in the background. You can also check by hand on the Updates screen in Settings."),
        ],
        "cta_q1": "Windows", "cta_or": "or", "cta_q2": "Linux?",
        "cta_win": "Download for Windows", "cta_lin": "Download for Linux",
        "cta_note": f"Version {VERSION}. After installing, the app updates itself.",
        "foot_what": "Desktop chat app",
        "foot_links": [("/en/privacy/", "Privacy"), (f"mailto:{EMAIL}", "Contact")],
        "foot_right": "Privacy",
        "priv_title": "Privacy | Masa",
        "priv_desc": "What data Masa keeps and where, what it sends requests to, and what it does not collect.",
        "priv_h": "Privacy",
        "priv_blocks": [
            ("What stays on this computer", "Your chats, projects, artifacts and settings are stored in a local database on this computer. Masa does not send them to its own servers."),
            ("Requests that leave", "Your messages go only to the API address you entered in Settings. If you turn on the web tool, a request goes to the page when the model asks for it; if you turn on web search, to the search provider you picked. There is also an update check, which only reads a version file."),
            ("What we do not collect", "Masa sends no usage statistics, crash reports or advertising IDs. This site is served without cookies or trackers."),
            ("Contact", f"For questions or deletion requests: {EMAIL}"),
        ],
        "priv_home": "Home",
        "alt_label": "Türkçe", "alt_path": "/", "self_path": "/en/",
        "priv_path": "/en/privacy/", "alt_priv_path": "/gizlilik/",
        "og_alt": "Masa app screen",
        "ld_desc": "A desktop chat app for Windows and Linux. Works with any OpenAI-compatible address; includes projects, artifact preview, file tools and MCP.",
        "menu": "Menu",
        "skip": "Skip to content",
    },
}

ROBOTS_META = '<meta name="robots" content="index, follow, max-image-preview:large">' if INDEXABLE else '<meta name="robots" content="noindex, nofollow">'


def head(c, title, desc, path, alt_path, extra_ld=None, og=True):
    canon = BASE + path
    alt = BASE + alt_path
    tr_url = BASE + (path if c["lang"] == "tr" else alt_path)
    en_url = BASE + (alt_path if c["lang"] == "tr" else path)
    ld = json.dumps({"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": BASE + "/#org", "name": "Masa", "url": BASE + "/",
         "logo": BASE + "/img/icon-512.png", "email": EMAIL},
        {"@type": "WebSite", "@id": BASE + "/#site", "name": "Masa", "url": BASE + "/",
         "inLanguage": ["tr", "en"], "publisher": {"@id": BASE + "/#org"}},
    ] + (extra_ld or [])}, ensure_ascii=False)
    return f"""<!DOCTYPE html>
<html lang="{c['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
{ROBOTS_META}
<meta name="theme-color" content="#97aaf6">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="tr" href="{tr_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{tr_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Masa">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{'tr_TR' if c['lang']=='tr' else 'en_US'}">
<meta property="og:image" content="{BASE}/img/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(c['og_alt'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{BASE}/img/og.png">
<link rel="icon" type="image/png" sizes="32x32" href="/img/favicon-32.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/switzer-600.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css?v={VERSION}">
<link rel="stylesheet" href="/css/mock.css?v={VERSION}">
<script type="application/ld+json">{ld}</script>
</head>
"""


def mockup(lang, key, alt):
    if key == "update":
        return mock.update(lang, alt, VERSION)
    if key == "hero":
        return mock.project(lang, alt)
    return mock.BUILDERS[key](lang, alt)


H1 = {"tr": "Masa her modelle konuşur.", "en": "Masa talks to any model."}
# chapter colour and layout per feature, in page order (never two alike side by side)
CHAPTERS = [("models", "c2", "fa"), ("hero", "c3", "fb"), ("artifact", "c4", "fa"), ("mcp", "c1", "fb"), ("update", "c2", "fa")]


def nav(c, links=None):
    home = c["self_path"]
    if links is None:
        links = "".join(f'<a href="{home}{h}">{e(t)}</a>' for h, t in c["nav"][:2])
    other = "en" if c["lang"] == "tr" else "tr"
    return f"""<header class="nav">
<a class="brand" href="{home}"><img src="/img/icon-192.png" width="26" height="26" alt="">Masa</a>
<nav aria-label="{e(c['menu'])}">{links}<a href="{c['alt_path'] if links.count('<a') < 2 else c['alt_path']}" hreflang="{other}" lang="{other}">{e(c['alt_label'])}</a></nav>
</header>"""


def footer(c, cls=""):
    links = "".join(f'<a href="{h}"{" class=mail" if h.startswith("mailto") else ""}>{e(t)}</a>' for h, t in c["foot_links"])
    return f"""<footer class="foot{cls}">
<p>{e(c['foot_what'])}</p>
<p class="foot-links">{links}</p>
<p>{datetime.date.today().year}</p>
</footer>"""


def home(c):
    lang = c["lang"]
    home_path = c["self_path"]
    faq_ld = {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
    app_ld = {"@type": "SoftwareApplication", "@id": BASE + "/#app", "name": "Masa",
              "applicationCategory": "BusinessApplication", "operatingSystem": "Windows, Linux",
              "softwareVersion": VERSION, "description": c["ld_desc"], "url": BASE + home_path,
              "image": BASE + "/img/icon-512.png", "inLanguage": ["tr", "en"],
              "publisher": {"@id": BASE + "/#org"}}
    crumb = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Masa", "item": BASE + home_path}]}
    out = head(c, c["title"], c["desc"], home_path, c["alt_path"], [app_ld, faq_ld, crumb])
    feats = {f[0]: f for f in c["feats"]}
    fid = "neler" if lang == "tr" else "features"
    faqid = "sss" if lang == "tr" else "faq"
    dlid = "indir" if lang == "tr" else "download"

    chapters = ""
    for i, (k, col, lay) in enumerate(CHAPTERS):
        _, h, p, alt = feats[k]
        anchor = f' id="{fid}"' if i == 0 else ""
        chapters += f"""<section class="ch {col} feat {lay}"{anchor} aria-labelledby="f-{k}">
<h2 class="hd" id="f-{k}">{e(h)}</h2>
<div class="fp"><p>{e(p)}</p></div>
<div class="fm">{mockup(lang, k, alt)}</div>
</section>
"""

    how = ""
    for i, (lead, sub, kind, text, resp) in enumerate(c["how"]):
        if kind == "code":
            call = f"""<div class="call"><div class="in"><pre><code id="cmd">{e(text)}</code></pre><button type="button" class="copy" data-copy="#cmd" data-done="{e(c['how_copied'])}">{e(c['how_copy'])}</button></div></div>"""
        else:
            call = f"""<div class="call"><div class="in"><span>{e(text)}</span></div></div>"""
        how += f"""<li class="ex"><p class="ex-num" aria-hidden="true">{i+1}</p>
<p class="ex-lead">{e(lead)}</p>
<p class="ex-sub">{e(sub)}</p>
{call}
</li>
"""

    faq = ""
    for q, a in c["faq"]:
        faq += f"""<div class="qa"><h3>{e(q)}</h3><p>{e(a)}</p></div>
"""

    b1, b2, b3 = c["ask_btns"]
    out += f"""<body>
<a class="skip" href="#main">{e(c['skip'])}</a>
{nav(c)}
<main id="main">
<section class="ch c1 hero">
<h1>{e(H1[lang])}</h1>
<div class="hero-text"><p>{e(c['tagline'])}</p><a class="btn" href="#{dlid}">{e(c['cta'])}</a></div>
<div class="hero-shot"><div class="vid">
<video id="heroVid" width="1280" height="800" muted loop playsinline preload="metadata" poster="/media/masa-{lang}-poster.webp" aria-label="{e(c['hero_alt'])}">
<source src="/media/masa-{lang}.mp4" type="video/mp4">
</video>
<button type="button" class="vp" id="vidBtn" aria-pressed="false" data-play="{'Oynat' if lang == 'tr' else 'Play'}" data-pause="{'Duraklat' if lang == 'tr' else 'Pause'}">{'Duraklat' if lang == 'tr' else 'Pause'}</button>
</div></div>
</section>

{chapters}
<section class="ch ink ask" aria-labelledby="ask-h">
<div class="ask-text">
<h2 id="ask-h">{e(c['ask_h'])}</h2>
<p>{e(c['ask_p'])}</p>
</div>
<div class="ask-card-wrap">
<div class="ask-card" id="askCard" data-ok="{e(c['ask_ok'])}" data-always="{e(c['ask_always'])}" data-no="{e(c['ask_no'])}" data-wait="{e(c['ask_wait'])}">
<p class="ask-w">{e(c['ask_what'])}</p>
<p class="ask-t">{e(c['ask_title'])}</p>
<div class="ask-b">
<button type="button" data-a="ok">{e(b1)}</button>
<button type="button" data-a="always">{e(b2)}</button>
<button type="button" data-a="no" class="ghost">{e(b3)}</button>
</div>
</div>
<p class="ask-out" id="askOut" role="status" aria-live="polite">{e(c['ask_wait'])}</p>
<button type="button" class="again" id="askReset" hidden>{e(c['ask_reset'])}</button>
</div>
</section>

<section class="ch c3 how" aria-labelledby="how-h">
<h2 class="hd" id="how-h">{e(c['how_h'])}</h2>
<ol class="exs">
{how}</ol>
</section>

<section class="ch paper faq" id="{faqid}" aria-labelledby="faq-h">
<div class="qa"><h2 id="faq-h">{e(c['faq_h'])}</h2></div>
{faq}</section>

<section class="ch ink cta" id="{dlid}" aria-labelledby="cta-h">
<h2 class="cta-q" id="cta-h"><span>{e(c['cta_q1'])}</span><span>{e(c['cta_q2'])}</span></h2>
<div>
<div class="cta-row">
<a class="btn" href="/download/Masa-Setup.exe" download>{e(c['cta_win'])}</a>
<span class="or">{e(c['cta_or'])}</span>
<a class="btn" href="/download/masa_amd64.deb" download>{e(c['cta_lin'])}</a>
</div>
<p class="cta-note">{e(c['cta_note'])}</p>
</div>
{footer(c)}
</section>
</main>
<script src="/js/site.js?v={VERSION}" defer></script>
</body>
</html>
"""
    return out


def privacy(c):
    path = c["priv_path"]
    blocks = "".join(f"<h2>{e(h)}</h2><p>{e(p)}</p>" for h, p in c["priv_blocks"])
    crumb = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Masa", "item": BASE + c["self_path"]},
        {"@type": "ListItem", "position": 2, "name": c["priv_h"], "item": BASE + path}]}
    out = head(c, c["priv_title"], c["priv_desc"], path, c["alt_priv_path"], [crumb])
    other = "en" if c["lang"] == "tr" else "tr"
    out += f"""<body class="plain">
<a class="skip" href="#main">{e(c['skip'])}</a>
<header class="nav"><a class="brand" href="{c['self_path']}"><img src="/img/icon-192.png" width="26" height="26" alt="">Masa</a><nav><a href="{c['alt_priv_path']}" hreflang="{other}" lang="{other}">{e(c['alt_label'])}</a></nav></header>
<main id="main" class="priv">
<h1>{e(c['priv_h'])}</h1>
{blocks}
</main>
{footer(c)}
</body>
</html>
"""
    return out


def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for d in ("css", "js", "fonts", "img", "media"):
        src = os.path.join(ROOT, d)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(OUT, d))
    tr, en = COPY["tr"], COPY["en"]
    write("index.html", home(tr))
    write("en/index.html", home(en))
    write("gizlilik/index.html", privacy(tr))
    write("en/privacy/index.html", privacy(en))

    urls = [("/", "/en/"), ("/en/", "/"), ("/gizlilik/", "/en/privacy/"), ("/en/privacy/", "/gizlilik/")]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for u, a in urls:
        tr_u = u if not u.startswith("/en") else a
        en_u = a if not u.startswith("/en") else u
        sm.append(f"<url><loc>{BASE}{u}</loc><lastmod>{TODAY}</lastmod>"
                  f'<xhtml:link rel="alternate" hreflang="tr" href="{BASE}{tr_u}"/>'
                  f'<xhtml:link rel="alternate" hreflang="en" href="{BASE}{en_u}"/>'
                  f'<xhtml:link rel="alternate" hreflang="x-default" href="{BASE}{tr_u}"/></url>')
    sm.append("</urlset>")
    write("sitemap.xml", "\n".join(sm) + "\n")

    bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot",
            "PerplexityBot", "Perplexity-User", "Google-Extended", "Applebot-Extended", "CCBot"]
    if INDEXABLE:
        rb = "User-agent: *\nAllow: /\nDisallow: /download/\n\n"
        for b in bots:
            rb += f"User-agent: {b}\nAllow: /\nDisallow: /download/\n\n"
        rb += f"Sitemap: {BASE}/sitemap.xml\n"
    else:
        rb = "User-agent: *\nDisallow: /\n"
    write("robots.txt", rb)

    llms = f"""# Masa

> Masa is a desktop chat app for Windows and Linux. It works with any OpenAI-compatible API address, and includes projects, artifact preview, file tools with approval, and MCP servers. Current version: {VERSION}.

## Pages
- [Home (Turkish)]({BASE}/): what Masa is, features, questions, downloads
- [Home (English)]({BASE}/en/): the same in English
- [Gizlilik]({BASE}/gizlilik/): privacy, in Turkish
- [Privacy]({BASE}/en/privacy/): what stays on the computer and what is sent

## Key facts
- Platforms: Windows 10 and later (installer), Linux (.deb for Debian and Ubuntu). No macOS build yet.
- Models: any provider with an OpenAI-compatible chat endpoint; the user enters the address and key.
- Data: chats, projects and artifacts are stored in a local database on the user's computer.
- Updates: new versions download in the background and install after a restart.
- Languages: Turkish and English interface.
- Contact: {EMAIL}
"""
    write("llms.txt", llms)
    write("site.webmanifest", json.dumps({
        "name": "Masa", "short_name": "Masa", "start_url": "/", "display": "browser",
        "background_color": "#f7f7f5", "theme_color": "#97aaf6",
        "icons": [{"src": "/img/icon-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, indent=2))
    write("404.html", f"""<!DOCTYPE html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>404 | Masa</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/css/site.css?v={VERSION}"></head><body class="plain"><main id="main" class="priv"><h1>404</h1><p><a href="/">Masa</a></p></main></body></html>""")
    print("built", OUT, "indexable" if INDEXABLE else "noindex")


if __name__ == "__main__":
    main()
