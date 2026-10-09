#!/usr/bin/env python3
"""Build figma-exports/mng-ads-export/ from raw Figma extraction files.

Usage: python3 build-ads-export.py <raw_dir> <out_dir> [export-date]

raw_dir holds the results of the three calls in extract.js (copy each saved tool result in as-is):
  specs.json     Ad Blocks component set (517:4304): every variant's layer tree, plus the base "Advertizment Template" frame
  usage.json     every non-nested instance of each variant in WordPress Elements, with its full frame path
  previews.json  base64 PNG per variant id (1x) plus 'SET' (the whole set at 0.5x)
Scope: the Ad Blocks set only. RevContent (506:3865) is excluded on purpose (not built to production).
"""
import json, re, os, sys, base64, collections, html, shutil

RAW, OUT = sys.argv[1], sys.argv[2]
DATE = sys.argv[3] if len(sys.argv) > 3 else '2026-10-09'

def load(name):
    d = json.load(open(os.path.join(RAW, name)))
    d = d.get('result', d)
    d.pop('pad', None)
    return d

SPECS, USAGE, PREV = load('specs.json'), load('usage.json')['out'], load('previews.json')['out']
SET = SPECS['set']
FILE_KEY, FILE_NAME, PAGE = SPECS['fileKey'], SPECS['fileName'], SPECS['page']
SLUG = 'ad-blocks'
ITEM_DIR = f'components/01-{SLUG}'

def slug(s):
    s = s.lower().replace('&', 'and').replace('+', '')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def url(nid):
    return f'https://www.figma.com/design/{FILE_KEY}/?node-id={nid.replace(":", "-")}'

# ----------------------------------------------------------------- breakpoints
BREAKPOINTS = [  # key, viewport, homepage template, bucket
    ('340', '≤639px (XS-Fold, built 340)', '340 HomePage', 'XS-Fold'),
    ('360', '≤639px (SM-Mobile, built 360)', 'Mobile HomePage', 'SM-Mobile'),
    ('768', '640–799px (MD-TabletV)', '768 HomePage', 'MD-TabletV'),
    ('1024', '800–1039px (LG-TabletH, built 1009)', '1024 HomePage', 'LG-TabletH'),
    ('1100', '≥1040px (XL-Desktop, built 1085)', '1100 HomePage', 'XL-Desktop'),
    ('1280', '≥1040px (XL-Desktop, built 1280)', 'Desktop HomePage', 'XL-Desktop'),
]
BP_KEYS = [b[0] for b in BREAKPOINTS]
TPL2BP = {b[2]: b[0] for b in BREAKPOINTS}

def bps_from_component(comp):
    """Breakpoints implied by the parent component variant an ad is nested in (Masthead, TOP ZONE Block, ...)."""
    v = comp.split(' / ', 1)[1] if ' / ' in comp else comp
    m = re.search(r'Device=([^,]+)', v)
    d = m.group(1) if m else v
    if 'XS-Fold' in d or d.startswith('Fold'): return ['340']
    if 'SM-Mobile' in d: return ['360']
    if d.startswith('Mobile'): return ['340', '360']
    if 'MD-TabletV' in d or d in ('Tablet', 'TabletV'): return ['768']
    if 'LG-TabletH' in d or d in ('1024', 'TabletH'): return ['1024']
    if d == '1100': return ['1100']
    if 'XL-Desktop' in d: return ['1100', '1280']
    if d == 'Desktop': return ['1280'] if comp.startswith(('TOP ZONE', 'Upcoming')) else ['1100', '1280']
    return []

# ----------------------------------------------------------------- production slot names
# GPT slot names, as written in the homepage template layer names and the Ads page labels
# (matched to the Ad Team's WordPress Ad Map on 2026-10-02).
SLOT = [
    ('Sponsorship 1', 'sponsorship_1'), ('Sponsorship 2', 'sponsorship_2 (also sponsorship_3 / sponsorship_4)'),
    ('Top Leaderboard', 'top_leaderboard'), ('Bottom Leaderboard', 'bottom_leaderboard'),
    ('Mobile Adhesion', 'mobile_adhesion (sticky, dismissible)'), ('Cube 1 RRail ATF', 'cube1_rrail_atf'),
    ('Cube 2 RRail Mid', 'cube2_rrail_mid'), ('Cube 3 RRail Lower', 'cube3_rrail_lower'),
    ('Cube Article', 'cube_article'), ('Outstream Video', 'outstream_video'),
    ('Sidebar Rectangle', '— (generic 300x250; also the CitySpark ad inside Upcoming Events)'),
    ('Mid-Article Banner', '— (no matching article slot found; see Status open item 8b)'),
    ('PLACE HOLDER', '— (not an ad unit)'),
]
def unit_and_size(name):
    m = re.match(r'(.*?)\s+(\d+)x(\d+)$', name)
    return (m.group(1), int(m.group(2)), int(m.group(3))) if m else (name, None, None)
def slot_for(unit):
    for k, v in SLOT:
        if unit.startswith(k): return v
    return '—'

# ----------------------------------------------------------------- usage per variant
def summarize_usage(vname):
    insts = USAGE.get(vname, [])
    tpl, nested, other, slots = collections.Counter(), collections.Counter(), collections.Counter(), []
    bps = set()
    for i in insts:
        names = [p['n'] for p in i['path']]
        if i['inComp']:
            nested[i['inComp']] += 1
            bps.update(bps_from_component(i['inComp']))
            continue
        hp = next((n for n in names if n in TPL2BP), None)
        if hp:
            tpl[f'Homepage ▸ {hp}'] += 1
            bps.add(TPL2BP[hp])
            lab = next((n for n in reversed(names) if re.search(r'(sponsorship_|bottom_leaderboard|mobile_adhesion|cube\d_rrail|landing-three-one)', n)), None)
            if lab: slots.append((TPL2BP[hp], lab))
            continue
        named = next((n for n in reversed(names) if re.search(r'Template|Home Page Sections', n)), None)
        if i['page'] in ('Section Front', 'Article Page') and named:
            tpl[f'{i["page"]} ▸ {named}'] += 1
        elif i['page'] == 'Article Page':
            tpl['Article Page ▸ Article Page Templates'] += 1
        elif i['page'] == 'Section Front':
            tpl['Section Front ▸ Section Front Templates'] += 1
        else:
            other[f'{i["page"]} ▸ {" ▸ ".join(names) or "(page top level)"}'] += 1
    return dict(count=len(insts), templates=dict(tpl), nestedIn=dict(nested), other=dict(other),
                breakpoints=[b for b in BP_KEYS if b in bps], homepageSlots=sorted(set(slots), key=lambda x: (BP_KEYS.index(x[0]), x[1])))

# ----------------------------------------------------------------- variants
def text_node(v): return next(c for c in v['children'] if c['type'] == 'TEXT')
def has_close(v): return any(c['name'] == 'Close Button BG' for c in v['children'])

variants = []
for v in SET['variants']:
    vp = v['variantProperties']
    unit, w, h = unit_and_size(vp['Name'])
    t = text_node(v)
    fname = f"{SLUG}--{slug(vp['Device'])}-{slug(vp['Name'])}.png"
    variants.append(dict(v=v, label=v['name'], device=vp['Device'], name=vp['Name'], unit=unit, w=v['w'], h=v['h'],
                         slot=slot_for(unit), close=has_close(v), text=t, preview=fname, usage=summarize_usage(v['name'])))
# Display order: grouped by unit family, then width, then height
FAMILY_ORDER = ['Sponsorship 1', 'Top Leaderboard', 'Sponsorship 2', 'Cube 1 RRail ATF', 'Cube 2 RRail Mid', 'Cube 3 RRail Lower',
                'Cube Article', 'Sidebar Rectangle', 'Outstream Video', 'Mid-Article Banner', 'Bottom Leaderboard', 'Mobile Adhesion', 'PLACE HOLDER']
def fam_idx(u): return next((i for i, f in enumerate(FAMILY_ORDER) if u.startswith(f)), 99)
variants.sort(key=lambda x: (fam_idx(x['unit']), -x['w'], -x['h']))

# ----------------------------------------------------------------- known issues (automatic + curated)
issues = []
unused = [x['name'] for x in variants if x['usage']['count'] == 0]
if unused:
    issues.append(f"{len(unused)} variants have no instances anywhere in WordPress Elements: " + ', '.join(unused) +
                  ". The 300x50 / 970x90 sizes and Bottom Leaderboard 320x50 come from the Ad Team's map (added 2026-10-02) but aren't placed in any template; the article-page units (Cube Article, Outstream Video, Mid-Article Banner 300x250) wait for the article-page pass.")
for x in variants:
    d = x['v'].get('componentDescription') or ''
    if x['unit'].startswith('Mobile Adhesion') and 'top-of-page leaderboard' in d:
        issues.append(f"`{x['label']}`: its description was copied from Top Leaderboard 728x90 (talks about the top-of-page leaderboard). It should describe the sticky mobile_adhesion unit at 768.")
adh = [x for x in variants if x['unit'].startswith('Mobile Adhesion')]
noclose = [x['name'] for x in adh if not x['close']]
if noclose:
    issues.append(f"Mobile Adhesion variants without the close (×) button that the other adhesion variants have: {', '.join(noclose)}.")
for x in variants:
    st = x['text']['styles'][0]
    if st['size'] != 16:
        issues.append(f"`{x['label']}`: the label is {st['size']}px (not bound to a size token) instead of 16px, and still wraps mid-word (\"ADVERTISEM / ENT\") in the {x['w']:.0f}px box.")
issues.append("The green fill (`#85FF9B`) is not bound to a variable, and neither are the close button's colors (`#141414` circle, `#FFFFFF` ×). The border, diagonals and label are bound to `color/gray/min`; the label halo to `color/gray/600`.")
issues.append("`PLACE HOLDER` (300x250, Device=All) isn't an ad unit and has no instances; it's a generic stand-in.")
issues.append("Device values are loose: some `Device=All` units only appear at one width (e.g. Sponsorship 1 320x50 only in the XL-Desktop Masthead), and `Top Leaderboard 970x250` (Device=Desktop) is also used in the LG-TabletH (1024) Masthead. Use the per-variant breakpoints below, not the Device value, to pick a unit.")
issues.append("Ads and Sponsored page housekeeping (not part of the component): the size-label column next to the set (`Frame 11705`) still says \"Footer Banner\" and \"Floating Anchor\" (renamed Bottom Leaderboard / Mobile Adhesion on 2026-10-02) and has no labels for the 12 newer variants; a loose `Ad Blocks` instance (`3383:46993`) and a `TEMP_PREVIEW` frame sit on the page.")
issues.append("`Mid-Article Banner` has no matching production slot (Status open item 8b); its only uses are in the Section Front templates.")

# ----------------------------------------------------------------- tokens
VARS = collections.OrderedDict()
def walk(n, f):
    f(n)
    for c in n.get('children', []): walk(c, f)
colors = collections.Counter()
def collect(n):
    for key in ('fills', 'strokes'):
        for p in n.get(key) or []:
            if p.get('hex'):
                colors[(p['hex'], p.get('variable'))] += 1
                if p.get('variable'): VARS[p['variable']] = p['hex']
    for st in n.get('styles', []):
        for p in st.get('color') or []:
            colors[(p['hex'], p.get('variable'))] += 1
            if p.get('variable'): VARS[p['variable']] = p['hex']
for x in variants: walk(x['v'], collect)
def cssname(var): return '--' + var.split('/', 1)[1].replace('/', '-') if '/' in var else '--' + slug(var)
TOKENS_CSS = {cssname(k): v for k, v in VARS.items()}
TOKENS_CSS['--ad-placeholder-fill'] = '#85FF9B'
TYPE_VARS = sorted({f"{k}: {v}" for x in variants for k, v in (x['text'].get('vars') or {}).items()})

# ----------------------------------------------------------------- HTML skeleton
def esc(s): return html.escape(str(s))
def skeleton_html():
    secs = []
    for x in variants:
        t = x['text']; st = t['styles'][0]
        lines = [esc(l) for l in t['text'].split('\n')]
        close = ('<button class="mng-ad-blocks__close" type="button" aria-label="Close ad">'
                 '<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="var(--color-gray-min, #141414)"/>'
                 '<path d="M5 5 15 15M15 5 5 15" stroke="#FFFFFF" stroke-width="2"/></svg></button>') if x['close'] else ''
        secs.append(f'''  <section class="mng-variant" data-variant="{esc(x['label'])}">
    <h2 class="mng-variant__title">{esc(x['label'])} <small>{x['w']:.0f}×{x['h']:.0f} · slot {esc(x['slot'])}</small></h2>
    <!-- Ad slot. In production this <div> is the GPT container; the green box is a design placeholder only. -->
    <div class="mng-ad-blocks" data-component="Ad Blocks" data-device="{esc(x['device'])}" data-name="{esc(x['name'])}" style="width:{x['w']:.0f}px;height:{x['h']:.0f}px">
      <svg class="mng-ad-blocks__x" viewBox="0 0 {x['w']:.0f} {x['h']:.0f}" preserveAspectRatio="none" aria-hidden="true"><path d="M0 0 {x['w']:.0f} {x['h']:.0f}M{x['w']:.0f} 0 0 {x['h']:.0f}"/></svg>
      <p class="mng-ad-blocks__label" style="font-size:{st['size']}px">{'<br>'.join(lines)}</p>
      {close}
    </div>
  </section>''')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Ad Blocks — skeleton</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../tokens.css">
<style>
[hidden]{{display:none!important}}
body{{font-family:'Noto Sans',sans-serif;margin:24px;background:#fff;color:#141414}}
.mng-variant{{margin:0 0 32px}}
.mng-variant__title{{font-size:14px;font-weight:700;margin:0 0 8px}} .mng-variant__title small{{font-weight:400;color:#5D5B5A}}
/* Ad Blocks: fixed IAB size, 2px inside border, centered label, X diagonals. */
.mng-ad-blocks{{position:relative;box-sizing:border-box;flex-shrink:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;
  overflow:hidden;background:var(--ad-placeholder-fill,#85FF9B);border:2px solid var(--color-gray-min,#141414)}}
.mng-ad-blocks__x{{position:absolute;inset:0;width:100%;height:100%}} .mng-ad-blocks__x path{{stroke:var(--color-gray-min,#141414);stroke-width:2;fill:none;vector-effect:non-scaling-stroke}}
.mng-ad-blocks__label{{position:relative;margin:0;text-align:center;font-family:'Noto Serif',serif;font-weight:700;line-height:normal;letter-spacing:.1em;
  color:var(--color-gray-min,#141414);-webkit-text-stroke:3px var(--color-gray-600,#F1EFEB);paint-order:stroke fill}}
.mng-ad-blocks__close{{position:absolute;top:4px;right:4px;width:20px;height:20px;padding:0;border:0;background:none;cursor:pointer;line-height:0}}
</style></head>
<body>
<h1 style="font-size:20px">Ad Blocks <small style="font-weight:400">({len(variants)} variants · WordPress Elements {esc(SET['id'])})</small></h1>
{chr(10).join(secs)}
</body></html>
'''

# ----------------------------------------------------------------- write
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, ITEM_DIR, 'previews'))
ids = {x['v']['id']: x['preview'] for x in variants}
for nid, b in PREV.items():
    fn = f'{SLUG}--overview.png' if nid == 'SET' else ids[nid]
    open(os.path.join(OUT, ITEM_DIR, 'previews', fn), 'wb').write(base64.b64decode(b))

def bpcell(b): return ', '.join(b) if b else '—'
def usage_cell(u):
    parts = [f'{k} ×{n}' for k, n in u['templates'].items()] + [f'in {k} ×{n}' for k, n in u['nestedIn'].items()] + [f'{k} ×{n}' for k, n in u['other'].items()]
    return '<br>'.join(parts) if parts else '**unused**'

# --- .md
props = SET['properties']
md = [f'''---
name: Ad Blocks
kind: component
order: 1
figma_file: {FILE_KEY} ({FILE_NAME})
figma_node: "{SET['id']}"
component_key: {SET['key']}
variants: {len(variants)}
breakpoints: [{', '.join(b for b in BP_KEYS if any(b in x['usage']['breakpoints'] for x in variants))}]
built_from: []
built_into: [{', '.join(sorted({k.split(' / ')[0] for x in variants for k in x['usage']['nestedIn']}))}]
spec_json: {SLUG}.json
skeleton: {SLUG}.html
exported: {DATE}
---

# Ad Blocks

> Ad slot placeholders, one variant per production ad unit and size. Each is a fixed-size green box with a 2px border, X diagonals and a centered "<unit> <size> / ADVERTISEMENT" label. In production the slot is a Google Publisher Tag container sized to the creative; the box only reserves the space in designs.

![All variants](previews/{SLUG}--overview.png)

## Figma references

- File: [{FILE_NAME}](https://www.figma.com/design/{FILE_KEY}/) (`{FILE_KEY}`), page **{PAGE}**
- Component set: [`{SET['id']}`]({url(SET['id'])}), key `{SET['key']}`
- Base drawing (not a component): "Advertizment Template" frame [`{SPECS['template']['id']}`]({url(SPECS['template']['id'])}), 720×320, "built to resize based on enclosing container".
- RevContent (`506:3865`, same page) is **not** in this export.

## Properties

| Property | Type | Default | Options |
|---|---|---|---|''']
for k, p in props.items():
    md.append(f"| {k} | {p['type']} | {p['default']} | {len(p['options'])} values (see table below) |" if k == 'Name' else f"| {k} | {p['type']} | {p['default']} | {', '.join(p['options'])} |")
md.append('\n## Ad units\n\nOne row per variant, grouped by unit. Breakpoints come from real template instances (homepage templates and the Masthead / TOP ZONE / Upcoming Events variants the ad sits in). Production slot names come from the template layer names and the Ads page labels.\n')
md.append('| Unit | Size | Device | Production slot | Breakpoints | Where it is used | Figma node | Key | Preview |')
md.append('|---|---|---|---|---|---|---|---|---|')
for x in variants:
    md.append(f"| {x['unit']}{' (with close ×)' if x['close'] else ''} | {x['w']:.0f}×{x['h']:.0f} | {x['device']} | {x['slot']} | {bpcell(x['usage']['breakpoints'])} | {usage_cell(x['usage'])} | [`{x['v']['id']}`]({url(x['v']['id'])}) | `{x['v']['key'][:12]}…` | [png](previews/{x['preview']}) |")

md.append('\n## Breakpoints\n\n| Key | Viewport | Homepage template | Ad units placed (homepage templates and nested components) |\n|---|---|---|---|')
for k, vp, tp, _ in BREAKPOINTS:
    us = [f"{x['name']}" for x in variants if k in x['usage']['breakpoints']]
    md.append(f"| {k} | {vp} | {tp} | {', '.join(us) or '—'} |")

md.append('\n## Homepage slot map\n\nFrom the homepage template layer names (each ad frame names its production slot and position).\n\n| Breakpoint | Unit | Layer (slot and position) |\n|---|---|---|')
rows = []
for x in variants:
    for bp, lab in x['usage']['homepageSlots']: rows.append((BP_KEYS.index(bp), bp, x['name'], lab))
for _, bp, n, lab in sorted(rows): md.append(f'| {bp} | {n} | {lab} |')
md.append('\nAlso placed by components (not template layers): the Masthead carries Top Leaderboard at every width (970x250 at 1024 and up, 728x90 at 768, 320x50 at 360, 320x100 at 340) and Sponsorship 1 (320x50 in the XL-Desktop Masthead, 300x50 in the Obituaries mastheads and ObitMastHead); TOP ZONE Block carries the Cube 1 RRail ATF (300x1050 at 1024 / 1100 / 1280, 300x250 at Mobile / Tablet); Upcoming Events Block carries Sidebar Rectangle 300x250 (CitySpark).')

md.append('''
## Responsive rules

- An ad slot never scales. Each width gets its own fixed-size unit; pick the variant listed for that breakpoint.
- Full-width slots (Top / Bottom Leaderboard, Sponsorship 2) step down 970×250 → 728×90 → 320×50 (or 320×100) as the viewport narrows; the 970×90 and 300×50 sizes are in the Ad Team's map for the same slots but aren't placed in any template yet.
- At 1024 / 1100 / 1280 the right-rail cubes are 300×600 (Cube 2 / 3) or 300×1050 (Cube 1, in TOP ZONE Block) inside a 384px ad column (`landing-three-one`). At 340 / 360 / 768 the same slots become 300×250.
- Mobile Adhesion is a sticky bottom overlay (320×50 at ≤639, 728×90 at 768) with a 20px close button 4px from the top-right corner. It's not in the page flow.
- Center the unit horizontally in its slot; the slot keeps the unit's height so the page doesn't jump when the creative loads.

## Anatomy

```
Ad Blocks / <variant>        COMPONENT  W×H, vertical auto-layout, gap 8, centered, clips content
├── Union                    BOOLEAN_OPERATION (UNION) of two full-size diagonal vectors → the X
│   ├── Vector 1             top-left → bottom-right, 2px stroke
│   └── Vector 2             top-right → bottom-left, 2px stroke
├── <Unit Size> ADVERTISEMENT TEXT  "<Unit Size>\\n\\nADVERTISEMENT" (short units: one line break)
└── (Mobile Adhesion 320x50 / 728x90 only)
    ├── Close Button BG      ELLIPSE 20×20 at top-right (x = W−24, y = 4)
    ├── X Line 1             LINE 14.1, rotated −45°, 2px white
    └── X Line 2             LINE 14.1, rotated 45°, 2px white
```

## Size & layout

| Property | Value |
|---|---|
| Size | fixed, exactly the IAB size in the variant name |
| Layout | vertical auto-layout, gap 8, padding 0, centered on both axes |
| Border | 2px inside, `color/gray/min` (#141414) |
| Corner radius | 0 |
| Clip content | yes |

## Typography

| Text | Font | Size | Weight | Line height | Letter spacing | Color | Type token |
|---|---|---|---|---|---|---|---|
| Label (all but 160×600) | Noto Serif | 16 | Bold | auto | 10% | `color/gray/min` #141414, 3px outside stroke `color/gray/600` #F1EFEB as a halo | `font/family/noto-serif`, `font/size/16`, `font/style/bold` |
| Label (Cube 1 RRail ATF 160x600) | Noto Serif | 14 | Bold | auto | 10% | same | `font/family/noto-serif`, `font/style/bold` (14 not bound) |

## Color & effects

| Use | Value | Token |
|---|---|---|
| Box fill | #85FF9B | — (placeholder green, unbound) |
| Border, X diagonals, label | #141414 | `color/gray/min` |
| Label halo | #F1EFEB | `color/gray/600` |
| Close button circle | #141414 | — (unbound) |
| Close button × | #FFFFFF | — (unbound) |

No effects.

## Production references

- Slot names: `sponsorship_1`, `sponsorship_2` / `_3` / `_4`, `top_leaderboard`, `bottom_leaderboard`, `mobile_adhesion`, `cube1_rrail_atf`, `cube2_rrail_mid`, `cube3_rrail_lower`, `cube_article`, `outstream_video`.
- Layout classes in the template layer names: `landing-three-one` (content + 384px ad column at ≥800px).
- Sizes per width were read live from OC Register's GPT setup at 360, 768, 1024 and 1280 (2026-10-02). Article-page units (outstream_video 480×360 / 300×250, cube_article 300×250) were seen on OC Register articles.

## Known issues
''')
for i in issues: md.append(f'- {i}')
md.append('''
## Rendering steps

1. Find the slot for the page and breakpoint in the tables above and take that variant's width and height.
2. Render a block-level container exactly that size (`ad-blocks.html` has one `<section>` per variant). In production, this is the GPT ad container; leave it empty and let the ad script fill it.
3. In mock-ups, draw the placeholder: green fill, 2px `color/gray/min` border, X diagonals and the centered label.
4. Mobile Adhesion: position it fixed to the bottom of the viewport, centered, with the close button.
''')
item_md = '\n'.join(md)
open(os.path.join(OUT, ITEM_DIR, f'{SLUG}.md'), 'w').write(item_md)

# --- .json
spec = dict(schema='mng-design-system/component-spec@1', kind='component', name='Ad Blocks', slug=SLUG, order=1,
            description='Ad slot placeholders, one variant per production ad unit and size.',
            exported=DATE,
            figma=dict(fileKey=FILE_KEY, fileName=FILE_NAME, page=PAGE, mainId=SET['id'], mainKey=SET['key'], url=url(SET['id']),
                       baseTemplateFrame=dict(id=SPECS['template']['id'], name=SPECS['template']['name'], url=url(SPECS['template']['id'])),
                       variants=[dict(label=x['label'], id=x['v']['id'], key=x['v']['key'], url=url(x['v']['id'])) for x in variants]),
            excluded=['RevContent (506:3865): not built to production (Karl, 2026-10-08)'],
            properties=props, breakpoints=[dict(key=k, viewport=vp, template=tp, bucket=b) for k, vp, tp, b in BREAKPOINTS],
            usage=dict(builtInto=sorted({k.split(' / ')[0] for x in variants for k in x['usage']['nestedIn']}),
                       perVariant=[dict(label=x['label'], **x['usage']) for x in variants]),
            dependencies=dict(builtFrom=[]),
            adSlots=[dict(unit=x['unit'], name=x['name'], width=x['w'], height=x['h'], device=x['device'], productionSlot=x['slot'],
                          closeButton=x['close'], breakpoints=x['usage']['breakpoints'], instances=x['usage']['count']) for x in variants],
            variants=[dict(label=x['label'], variantProperties=x['v']['variantProperties'], id=x['v']['id'], key=x['v']['key'],
                           width=x['w'], height=x['h'], layout=x['v'].get('layout'), fills=x['v'].get('fills'), strokes=x['v'].get('strokes'),
                           strokeWeight=x['v'].get('strokeWeight'), description=x['v'].get('componentDescription'),
                           preview=f'previews/{x["preview"]}', breakpoints=x['usage']['breakpoints'], layerTree=x['v']) for x in variants],
            typography=[dict(text='label', font='Noto Serif', weight='Bold', size=16, lineHeight='auto', letterSpacing='10%',
                             color='color/gray/min', halo='3px outside stroke, color/gray/600',
                             tokens=['font/family/noto-serif', 'font/size/16', 'font/style/bold'], exceptions={'Cube 1 RRail ATF 160x600': 'size 14, unbound'})],
            colors=[dict(use='fill', hex='#85FF9B', token=None), dict(use='border, diagonals, label', hex='#141414', token='color/gray/min'),
                    dict(use='label halo', hex='#F1EFEB', token='color/gray/600'), dict(use='close circle', hex='#141414', token=None),
                    dict(use='close ×', hex='#FFFFFF', token=None)],
            knownIssues=issues, skeleton=f'{SLUG}.html')
json.dump(spec, open(os.path.join(OUT, ITEM_DIR, f'{SLUG}.json'), 'w'), indent=1, ensure_ascii=False)
open(os.path.join(OUT, ITEM_DIR, f'{SLUG}.html'), 'w').write(skeleton_html())

# --- root: tokens, index, README
json.dump(dict(colors={k: dict(hex=v, css=cssname(k)) for k, v in VARS.items()},
               placeholders={'#85FF9B': 'ad placeholder fill (unbound)'},
               typography=TYPE_VARS, breakpoints=[dict(key=k, viewport=vp) for k, vp, _, _ in BREAKPOINTS]),
          open(os.path.join(OUT, 'tokens.json'), 'w'), indent=1, ensure_ascii=False)
open(os.path.join(OUT, 'tokens.css'), 'w').write(':root {\n' + ''.join(f'  {k}: {v};\n' for k, v in TOKENS_CSS.items()) + '}\n')
json.dump(dict(schema='mng-design-system/export-index@1', exported=DATE, source=f'{FILE_NAME} ▸ {PAGE} ▸ Ad Blocks ({SET["id"]})',
               items=[dict(order=1, name='Ad Blocks', kind='component', variants=len(variants),
                           breakpoints=[b for b in BP_KEYS if any(b in x['usage']['breakpoints'] for x in variants)],
                           builtFrom=[], builtInto=spec['usage']['builtInto'], md=f'{ITEM_DIR}/{SLUG}.md', json=f'{ITEM_DIR}/{SLUG}.json',
                           html=f'{ITEM_DIR}/{SLUG}.html', figmaNode=SET['id'], issues=len(issues))],
               excluded=spec['excluded']), open(os.path.join(OUT, 'index.json'), 'w'), indent=1, ensure_ascii=False)

used = sum(1 for x in variants if x['usage']['count'])
readme = f'''# MNG ad slots — component spec export

Exported {DATE} from Figma: the **Ad Blocks** component set in WordPress Elements ▸ {PAGE} (`{SET['id']}`), {len(variants)} variants ({used} placed in templates or components, {len(variants) - used} not used yet), with {len(PREV) - 1} variant previews plus an overview. **RevContent is excluded** (not built to production; Karl, 2026-10-08).

Rebuild: run the calls in `scripts/ads-export/extract.js` in Figma, then `python3 scripts/ads-export/build-ads-export.py <raw> figma-exports/mng-ads-export`.

## How an agent should use this folder

1. Open [`{ITEM_DIR}/{SLUG}.md`]({ITEM_DIR}/{SLUG}.md): the **Ad units** table lists every unit with its size, production slot name, breakpoints and where it's used; the **Homepage slot map** shows which unit fills which slot at each width.
2. For exact values use the `.json` twin (`adSlots[]` is the flat unit list; `variants[].layerTree` is the full Figma layer tree).
3. Start rendering from [`{SLUG}.html`]({ITEM_DIR}/{SLUG}.html) (one `<section>` per variant, colors from `tokens.css`).
4. In production the slot is an empty GPT container of that size; the green box is only a design placeholder.
5. Check **Known issues** before trusting a value.

## Breakpoints

| Key | Viewport | Homepage template |
|---|---|---|
''' + ''.join(f'| {k} | {vp} | {tp} |\n' for k, vp, tp, _ in BREAKPOINTS) + f'''
## Units at a glance

| Unit | Sizes |
|---|---|
''' + ''.join(f"| {f} | {', '.join(x['name'][len(f):].strip() or '300x250' for x in variants if x['unit'].startswith(f))} |\n" for f in FAMILY_ORDER) + f'''
## Folder layout

```
mng-ads-export/
├── README.md        this file
├── index.json       item list (paths, breakpoints, issue count)
├── tokens.json      color variables used (+ placeholder fill), type tokens, breakpoints
├── tokens.css       :root custom properties for the skeleton
└── {ITEM_DIR}/
    ├── {SLUG}.md       human-readable spec
    ├── {SLUG}.json     machine-readable spec with layer trees
    ├── {SLUG}.html     HTML/CSS skeleton, one section per variant
    └── previews/       one PNG per variant (1x) + {SLUG}--overview.png
```

## Not included

- RevContent component set (`506:3865`), the RevContent Image Template frame.
- The "Advertizment Template" frame (`{SPECS['template']['id']}`) is referenced but not exported; it's the drawing the Ad Blocks variants were built from, not a component.
- Page templates themselves (homepage templates are in `figma-exports/mng-design-system-export/` as usage evidence only).
'''
open(os.path.join(OUT, 'README.md'), 'w').write(readme)
print('built', len(variants), 'variants,', len(PREV), 'previews,', len(issues), 'issues')
