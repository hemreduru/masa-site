"""HTML/CSS mockups of the Masa app window. No screenshots, no personal data."""
import html

e = html.escape

M = {
    "tr": {
        "new": "Yeni sohbet", "search": "Ara", "projects": "Projeler", "artifacts": "Artifacts",
        "proj": "Atlas", "chats": ["Dashboard tasarımı", "Panel renkleri"], "loose": "Sohbetler", "free": "Serbest sohbet",
        "chat_title": "Dashboard tasarımı", "chip": "Proje: Atlas",
        "q": "Panel için 3 sütunlu bir fiyat tablosu yapar mısın?",
        "a1": "Yaptım. Üç plan, aylık ve yıllık fiyat; en ortadaki öne çıkıyor.",
        "a2": "Renkleri projedeki talimata göre sade tuttum.",
        "art_card": "Fiyat tablosu", "art_meta": "HTML · sürüm 3",
        "ph": "Atlas içinde yeni sohbet...", "think": "Düşünme", "web": "Web", "model": "Varsayılan model",
        "set_nav": ["Genel", "Sağlayıcılar ve modeller", "MCP sunucuları", "Güncellemeler"],
        "prov_h": "Sağlayıcılar ve modeller", "addr": "API adresi", "key": "Anahtar", "fetch": "Modelleri getir",
        "found": "3 model bulundu", "default": "Varsayılan",
        "p_instr": "Talimatlar", "p_instr_t": "Cevapları kısa tut. Arayüz kodu React ve TypeScript olsun.",
        "p_files": "Dosyalar", "p_folder": "src/", "p_folder_m": "klasör · 42 dosya", "p_chats": "Sohbetler",
        "art_h": "Fiyat tablosu", "copy": "Kopyala", "save": "Kaydet", "versions": ["v1", "v2", "v3"],
        "plans": [("Başlangıç", "₺0", ["1 proje", "Temel araçlar"]), ("Takım", "₺190", ["Sınırsız proje", "Ortak klasör"]),
                  ("İşletme", "₺490", ["Her şey dahil", "Öncelikli destek"])], "per": "/ ay",
        "mcp_h": "MCP sunucuları", "mcp_import": "Ayarı içe aktar", "connected": "bağlı", "tools": "araç",
        "servers": [("files", "5"), ("fetch", "2"), ("git", "8")],
        "up_h": "Güncellemeler", "ver": "Sürüm", "ready": "Yeni sürüm hazır", "dl_done": "İndirildi",
        "restart": "Yeniden başlat ve kur", "bg": "Güncellemeleri arka planda indir", "check": "Şimdi denetle",
    },
    "en": {
        "new": "New chat", "search": "Search", "projects": "Projects", "artifacts": "Artifacts",
        "proj": "Atlas", "chats": ["Dashboard design", "Panel colours"], "loose": "Chats", "free": "Free chat",
        "chat_title": "Dashboard design", "chip": "Project: Atlas",
        "q": "Can you make a 3-column pricing table for the panel?",
        "a1": "Done. Three plans with monthly and yearly prices; the middle one stands out.",
        "a2": "I kept the colours plain, following the project instructions.",
        "art_card": "Pricing table", "art_meta": "HTML · version 3",
        "ph": "New chat in Atlas...", "think": "Thinking", "web": "Web", "model": "Default model",
        "set_nav": ["General", "Providers and models", "MCP servers", "Updates"],
        "prov_h": "Providers and models", "addr": "API address", "key": "Key", "fetch": "Fetch models",
        "found": "3 models found", "default": "Default",
        "p_instr": "Instructions", "p_instr_t": "Keep answers short. UI code in React and TypeScript.",
        "p_files": "Files", "p_folder": "src/", "p_folder_m": "folder · 42 files", "p_chats": "Chats",
        "art_h": "Pricing table", "copy": "Copy", "save": "Save", "versions": ["v1", "v2", "v3"],
        "plans": [("Starter", "$0", ["1 project", "Basic tools"]), ("Team", "$19", ["Unlimited projects", "Shared folder"]),
                  ("Business", "$49", ["Everything included", "Priority support"])], "per": "/ mo",
        "mcp_h": "MCP servers", "mcp_import": "Import config", "connected": "connected", "tools": "tools",
        "servers": [("files", "5"), ("fetch", "2"), ("git", "8")],
        "up_h": "Updates", "ver": "Version", "ready": "A new version is ready", "dl_done": "Downloaded",
        "restart": "Restart and install", "bg": "Download updates in the background", "check": "Check now",
    },
}

MODELS = ["coder-large", "chat-fast", "reason-pro"]
CONFIG = ['{', '  "mcpServers": {', '    "files": {', '      "command": "npx",', '      "args": ["-y", "files-server"]', '    }', '  }', '}']


def _titlebar(m, title=""):
    return f'<div class="tb"><i class="lg"></i><b>Masa</b><span>{e(title)}</span></div>'


def _sidebar(m, active_chat=0):
    chats = "".join(f'<li class="{"on" if i == active_chat else ""}">{e(c)}</li>' for i, c in enumerate(m["chats"]))
    return f"""<aside class="sb">
<div class="nw"><span>+</span>{e(m['new'])}<kbd>Ctrl N</kbd></div>
<ul class="nv"><li><i class="gl c"></i>{e(m['search'])}<kbd>Ctrl K</kbd></li><li><i class="gl"></i>{e(m['projects'])}</li><li><i class="gl"></i>{e(m['artifacts'])}</li></ul>
<p class="sh">{e(m['projects'])}</p>
<p class="pj">▾ {e(m['proj'])}</p>
<ul class="ch">{chats}</ul>
</aside>"""


def _settings_nav(m, active):
    items = "".join(f'<li class="{"on" if i == active else ""}">{e(t)}</li>' for i, t in enumerate(m["set_nav"]))
    return f'<aside class="sb st"><ul class="ch">{items}</ul></aside>'


def _composer(m):
    return f"""<div class="cp"><p>{e(m['ph'])}</p><div class="cr"><span class="pill">+</span><span class="pill">{e(m['think'])}</span><span class="pill">{e(m['web'])}</span><span class="md">{e(m['model'])}</span></div></div>"""


def _wrap(alt, cls, title, body):
    return f'<div class="mock {cls}" role="img" aria-label="{e(alt)}"><div class="win" aria-hidden="true">{_titlebar(None, title)}<div class="bd">{body}</div></div></div>'


def chat(lang, alt, cls=""):
    m = M[lang]
    body = f"""{_sidebar(m)}<div class="mn"><div class="mh"><b>{e(m['chat_title'])}</b><span class="chip">{e(m['chip'])}</span></div>
<div class="th"><p class="us">{e(m['q'])}</p>
<div class="as"><p>{e(m['a1'])}</p><p>{e(m['a2'])}</p>
<div class="ac"><i class="gl"></i><span><b>{e(m['art_card'])}</b><small>{e(m['art_meta'])}</small></span></div></div></div>
{_composer(m)}</div>"""
    return _wrap(alt, cls, m["chat_title"], body)


def models(lang, alt, cls=""):
    m = M[lang]
    rows = "".join(f'<li class="{"on" if i == 0 else ""}"><i class="rd"></i><span>{e(n)}</span>{"<em>" + e(m["default"]) + "</em>" if i == 0 else ""}</li>' for i, n in enumerate(MODELS))
    body = f"""{_settings_nav(m, 1)}<div class="mn pad"><h4>{e(m['prov_h'])}</h4>
<label>{e(m['addr'])}</label><div class="fd">https://api.example.com/v1</div>
<label>{e(m['key'])}</label><div class="fd">••••••••••••••3f9a</div>
<div class="bt">{e(m['fetch'])}</div>
<p class="fn">{e(m['found'])}</p><ul class="ml">{rows}</ul></div>"""
    return _wrap(alt, cls, m["prov_h"], body)


def project(lang, alt, cls=""):
    m = M[lang]
    chats = "".join(f"<li>{e(c)}</li>" for c in m["chats"])
    body = f"""{_sidebar(m, 0)}<div class="mn pad"><h4>{e(m['proj'])}</h4>
<label>{e(m['p_instr'])}</label><div class="fd tall">{e(m['p_instr_t'])}</div>
<label>{e(m['p_files'])}</label><ul class="ml"><li><i class="gl"></i><span>{e(m['p_folder'])}</span><em>{e(m['p_folder_m'])}</em></li><li><i class="gl"></i><span>brief.md</span></li></ul>
<label>{e(m['p_chats'])}</label><ul class="ml">{chats}</ul></div>"""
    return _wrap(alt, cls, m["proj"], body)


def artifact(lang, alt, cls=""):
    m = M[lang]
    tabs = "".join(f'<span class="{"on" if i == 2 else ""}">{e(v)}</span>' for i, v in enumerate(m["versions"]))
    plans = "".join(
        f'<div class="pl{" mid" if i == 1 else ""}"><b>{e(n)}</b><strong>{e(p)}<small>{e(m["per"])}</small></strong>' + "".join(f"<span>{e(f)}</span>" for f in fs) + "</div>"
        for i, (n, p, fs) in enumerate(m["plans"]))
    body = f"""<div class="ap"><div class="ah"><b>{e(m['art_h'])}</b><span class="vs">{tabs}</span><span class="bt s">{e(m['copy'])}</span><span class="bt s">{e(m['save'])}</span></div>
<div class="pv"><div class="pg">{plans}</div></div></div>"""
    return _wrap(alt, cls, m["chat_title"], body)


def mcp(lang, alt, cls=""):
    m = M[lang]
    rows = "".join(f'<li><i class="dot"></i><span>{e(n)}</span><em>{e(m["connected"])} · {c} {e(m["tools"])}</em></li>' for n, c in m["servers"])
    code = "\n".join(CONFIG)
    body = f"""{_settings_nav(m, 2)}<div class="mn pad"><h4>{e(m['mcp_h'])}</h4><ul class="ml">{rows}</ul>
<div class="bt">{e(m['mcp_import'])}</div></div>"""
    return _wrap(alt, cls, m["mcp_h"], body)


def update(lang, alt, version, cls=""):
    m = M[lang]
    body = f"""{_settings_nav(m, 3)}<div class="mn pad"><h4>{e(m['up_h'])}</h4><p class="fn">{e(m['ver'])} {e(version)}</p>
<div class="uc"><b>{e(m['ready'])}</b><div class="pb"><i></i></div><small>{e(m['dl_done'])}</small><div class="bt acc">{e(m['restart'])}</div></div>
<div class="tg"><i class="sw"></i><span>{e(m['bg'])}</span></div><div class="bt">{e(m['check'])}</div></div>"""
    return _wrap(alt, cls, m["up_h"], body)


BUILDERS = {"chat": chat, "models": models, "hero": project, "artifact": artifact, "mcp": mcp, "update": update}
