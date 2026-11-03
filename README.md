# Masa site

Static product site for Masa (Turkish and English), built with a small Python script. No framework, no trackers, no cookies.

```
python3 build.py              # writes ./public, noindex
INDEXABLE=1 python3 build.py  # indexable build (robots, sitemap, meta robots)
MASA_VERSION=0.1.9 python3 build.py
```

- `mock.py` draws the app window in HTML and CSS (no screenshots).
- `css/site.css`, `js/site.js`: styles and the small interactions.
- Font: Switzer (Fontshare, free licence). Download `Switzer-Regular` and `Switzer-Medium` as woff2 from fontshare.com and place them as `fonts/switzer-400.woff2` and `fonts/switzer-500.woff2`. The files are not stored in this repo.
- Downloads are served from `/download/` on the host (symlinks to the release files).
