"""Build the five localized browser demos from one original app case."""
from html import escape as e
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DOMAIN = 'https://donalupa.com'
COPY = json.loads((ROOT / 'content/demo-copy.json').read_text())
PUZZLE = json.loads((ROOT / 'content/demo-case.json').read_text())
START, END = '<!-- case-demo:start -->', '<!-- case-demo:end -->'
people = PUZZLE['suspects'] + [PUZZLE['victim']]

def portrait(person):
    if person['id'] == 'case_item':
        return '<span class="lunch-piece" data-portrait aria-hidden="true">🥡</span>'
    return f'<img src="/assets/demo/sus_{person["id"]}.png" alt="" width="46" height="46" data-portrait>'

for locale, c in COPY.items():
    c = {**c, 'store': c['store'] + '?pt=1201782&ct=donalupa_web_demo&mt=8'}
    canonical = DOMAIN + c['path']
    alternates = ''.join(f'<link rel="alternate" hreflang="{other["lang"]}" href="{DOMAIN}{other["path"]}">' for other in COPY.values())
    alternates += f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/play/">'
    languages = ''.join(f'<a href="{other["path"]}" lang="{other["lang"]}" hreflang="{other["lang"]}"' + (' aria-current="page"' if key == locale else '') + f'>{key.upper()}</a>' for key, other in COPY.items())
    schema = {'@context': 'https://schema.org', '@graph': [
        {'@type': 'WebPage', '@id': canonical + '#page', 'url': canonical, 'name': c['title'], 'description': c['description'], 'inLanguage': c['lang'], 'isAccessibleForFree': True, 'dateModified': '2026-09-13'},
        {'@type': 'BreadcrumbList', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Doña Lupa', 'item': DOMAIN + c['home']},
            {'@type': 'ListItem', 'position': 2, 'name': c['heading'], 'item': canonical}]}]}
    tray = ''.join(f'<button type="button" class="piece-choice" data-person="{person["id"]}" aria-pressed="false">{portrait(person)}<span>{e(c["characters"][i])}</span></button>' for i, person in enumerate(people))
    board = []
    for row in range(PUZZLE['size']):
        for col in range(PUZZLE['size']):
            zone = next(z['id'] for z in PUZZLE['zones'] if [row, col] in z['cells'])
            room = c['rooms'][next(i for i, z in enumerate(PUZZLE['zones']) if z['id'] == zone)]
            scenery = next((s for s in PUZZLE['scenery'] if s['row'] == row and s['col'] == col), None)
            blocked = scenery and not scenery['occupiable']
            label = c['scenery'][scenery['key']] if scenery else c['empty']
            image = f'<img class="cell-scenery" src="/assets/demo/obj_{scenery["key"]}.png" alt="" width="64" height="64">' if scenery else ''
            contents = f'<span class="cell-coordinate" aria-hidden="true">{row + 1}·{col + 1}</span>{image}<span class="cell-piece" data-piece></span>'
            if blocked:
                board.append(f'<div class="case-cell is-blocked zone-{zone}" role="img" aria-label="{e(c["row"])} {row + 1}, {e(c["col"])} {col + 1}. {e(room)}. {e(label)}. {e(c["blocked"])}">{contents}</div>')
            else:
                board.append(f'<button type="button" class="case-cell zone-{zone}" data-cell="{row},{col}" data-room="{e(room)}" data-label="{e(label)}" aria-label="{e(c["row"])} {row + 1}, {e(c["col"])} {col + 1}. {e(room)}. {e(label)}">{contents}</button>')
    legend = ''.join(f'<span><i class="zone-{zone["id"]}" aria-hidden="true"></i>{e(c["rooms"][i])}</span>' for i, zone in enumerate(PUZZLE['zones']))
    clues = ''.join(f'<li data-clue>{e(clue)}</li>' for clue in c['clues'])
    accusations = ''.join(f'<button type="button" class="accuse-choice" data-accuse="{person["id"]}">{e(c["characters"][i])}</button>' for i, person in enumerate(PUZZLE['suspects']))
    solution = ''.join(f'<li>{e(step)}</li>' for step in c['solution'])
    data = json.dumps({'puzzle': PUZZLE, 'copy': c}, ensure_ascii=False).replace('<', '\\u003c')
    html = f'''<!doctype html>
<html lang="{c['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(c['title'])}</title><meta name="description" content="{e(c['description'])}"><link rel="canonical" href="{canonical}">{alternates}
<meta property="og:type" content="website"><meta property="og:url" content="{canonical}"><meta property="og:title" content="{e(c['title'])}"><meta property="og:description" content="{e(c['description'])}"><meta property="og:image" content="{DOMAIN}/assets/{'es-' if locale == 'es' else ''}gameplay.jpg">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{e(c['title'])}"><meta name="twitter:description" content="{e(c['description'])}"><meta name="twitter:image" content="{DOMAIN}/assets/{'es-' if locale == 'es' else ''}gameplay.jpg">
<meta name="apple-itunes-app" content="app-id=6801481670"><meta name="theme-color" content="#f4ecd7"><link rel="icon" href="/assets/app-icon.png"><link rel="stylesheet" href="/_style.css?v=20260826-4"><link rel="stylesheet" href="/demo.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c')}</script>
<script id="case-data" type="application/json">{data}</script><script type="module" src="/demo.mjs"></script>
<script defer src="/_vercel/insights/script.js"></script></head>
<body><div class="container"><header class="play-nav"><a class="brand" href="{c['home']}" aria-label="{e(c['back'])}"><img src="/assets/app-icon.png" width="44" height="44" alt=""><span>Doña Lupa</span></a><nav class="play-languages" aria-label="Languages">{languages}</nav></header>
<main><header class="play-hero"><p class="eyebrow">{e(c['eyebrow'])}</p><h1>{e(c['heading'])}</h1><p>{e(c['intro'])}</p></header>
<noscript><p class="play-card">{e(c['nojs'])}</p></noscript>
<div class="case-game" data-case-game>
  <div class="play-card" hidden data-needs-js>
    <div class="case-tray" role="group" aria-label="{e(c['pieces'])}">{tray}</div>
    <p class="current-clue" data-current-clue>{e(c['clues'][0])}</p>
    <div class="board-heading"><span>{e(c['board'])}</span><span class="case-progress" data-progress aria-hidden="true">0 / 4</span></div>
    <div class="case-board" role="group" aria-label="{e(c['board'])}">{''.join(board)}</div><div class="room-legend">{legend}</div>
    <div class="game-tools"><button type="button" data-hint>{e(c['hint'])}</button><button type="button" data-undo>{e(c['undo'])}</button><button type="button" data-reset>{e(c['reset'])}</button></div>
    <p class="game-status" role="status" aria-live="polite" aria-atomic="true" data-status>{e(c['choose'])}</p>
  </div>
  <aside class="play-card"><p class="eyebrow">{e(c['badge'])}</p><h2>{e(c['cluesTitle'])}</h2><ol class="case-clues">{clues}</ol>
    <div class="case-rules"><h2>{e(c['rulesTitle'])}</h2><p>{e(c['rules'])}</p></div>
    <section class="case-accusation" data-accusation hidden><h2>{e(c['accuse'])}</h2><div class="accuse-options">{accusations}</div><p class="game-status" role="status" aria-live="polite" data-accusation-message></p></section>
    <section class="case-result" data-result hidden><h2 tabindex="-1">{e(c['solved'])}</h2><p>{e(c['reveal'])}</p><a class="button button-primary" href="{e(c['store'])}">{e(c['cta'])}</a></section>
  </aside>
</div>
<details class="case-solution"><summary>{e(c['solutionTitle'])}</summary><ol>{solution}</ol></details><p class="case-source">{e(c['source'])}</p>
<footer class="play-footer"><a class="button button-primary" href="{e(c['store'])}">{e(c['cta'])}</a><p>{e(c['access'])}</p></footer>
</main></div></body></html>'''
    target = ROOT / c['path'].strip('/') / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html + '\n')
    home = ROOT / c['home'].strip('/') / 'index.html'
    source = home.read_text()
    preview = f'''{START}
<section class="container case-preview"><div><p class="eyebrow">{e(c['badge'])}</p><h2>{e(c['homeTitle'])}</h2><p>{e(c['homeBody'])}</p></div><a class="button button-primary" href="{c['path']}">{e(c['homeLink'])}</a></section>
{END}'''
    if START in source:
        source = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: preview, source, flags=re.S)
    else:
        marker = re.search(r'<section class="section container" id="[^"]+">', source)
        assert marker, locale
        source = source[:marker.start()] + preview + '\n\n    ' + source[marker.start():]
    # The secondary hero CTA is the direct route to the playable demonstration.
    source, count = re.subn(r'(<div class="cta-row">.*?<a class="text-link" href=")[^"]+("[^>]*>).*?</a>', lambda m: m[1] + c['path'] + m[2] + e(c['homeLink']) + ' <span aria-hidden="true">→</span></a>', source, count=1, flags=re.S)
    assert count == 1, locale
    if 'href="/demo.css"' not in source:
        source = source.replace('</head>', '<link rel="stylesheet" href="/demo.css">\n</head>', 1)
    home.write_text(source)

sitemap = (ROOT / 'sitemap.xml').read_text()
for c in COPY.values():
    if f'<loc>{DOMAIN}{c["path"]}</loc>' not in sitemap:
        alternates = ''.join(f'<xhtml:link rel="alternate" hreflang="{other["lang"]}" href="{DOMAIN}{other["path"]}"/>' for other in COPY.values())
        alternates += f'<xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/play/"/>'
        node = f'  <url><loc>{DOMAIN}{c["path"]}</loc><lastmod>2026-09-13</lastmod>{alternates}</url>\n'
        sitemap = sitemap.replace('</urlset>', node + '</urlset>')
(ROOT / 'sitemap.xml').write_text(sitemap)
print(f'Built {len(COPY)} playable cases and homepage links.')
