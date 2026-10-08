#!/usr/bin/env python3
"""Build figma-exports/mng-design-system-export/ from raw Figma extraction files.

Usage: python3 build-design-system-export.py <raw_dir> <previews_dir> <out_dir> [export-date]

raw_dir holds the files written by the calls in extract.js:
  specs_*.json      component specs (one file per extraction batch)
  usage_*.json      instance usage scans (one per Figma file)
  colormodes.json   color variable values per theme mode
previews_dir holds <section-slug>/<variant>.png exported by extract.js.
"""
import json, re, os, sys, glob, shutil, collections, html

RAW, PREV, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
DATE = sys.argv[4] if len(sys.argv) > 4 else '2026-10-07'

# ----------------------------------------------------------------- config
GROUPS = {
    'homepage': {'title': 'Homepage components', 'fileKey': 'b1iZxkFwtAYq9rElmnCAzd', 'page': 'Homepage',
                 'source': 'WordPress Elements ▸ Homepage ▸ Components (3334:42288)'},
    'menus-and-parts': {'title': 'Menus and Parts', 'fileKey': 'b1iZxkFwtAYq9rElmnCAzd', 'page': 'Menus and Parts',
                        'source': 'WordPress Elements ▸ Menus and Parts ▸ Push Nav Section Menu, Frame 12634 (Mastheads), Frame 12776 (User & Account Menus), Frame 12804 (Breaking News), Frame 12774 (Footer)'},
    'form-fields': {'title': 'Form Fields', 'fileKey': 'jFHYqhZbJjvWQmDI4myCsd', 'page': 'Form Fields | 2026.09.24',
                    'source': 'MNG Design System ▸ Form Fields | 2026.09.24 (all components)'},
}
FILES = {'b1iZxkFwtAYq9rElmnCAzd': 'WordPress Elements', 'jFHYqhZbJjvWQmDI4myCsd': 'MNG Design System'}
# Non-homepage items: (figma name, export name, kind) in build order.
MANIFEST = {
    'menus-and-parts': [('Weather Bug', None, 'component'), ('SectionMenuHeader', None, 'component'), ('AlertLevel', None, 'component'),
                        ('UserImage', None, 'component'), ('SearchBar', None, 'component'), ('Breaking News Banner', None, 'component'),
                        ('Footer', None, 'component'), ('SectionMenuItem', None, 'assembly'), ('UserPic', None, 'assembly'),
                        ('SectionMenu', None, 'assembly'), ('UserStatus', None, 'assembly'), ('Masthead', None, 'assembly')],
    'form-fields': [('Form Field', None, 'component', '6963:6863'), ('Code Box', None, 'component'),
                    ('Form Field Assembly / Checkbox + Terms', None, 'assembly'), ('Search Field / Obituaries — Core', None, 'component'),
                    ('Form Field', 'Form Field (Dashboard Mockup Set)', 'component', '2832:766'),
                    ('Form Field Assembly / Name pair', None, 'assembly'), ('Form Field Assembly / Zip + Street #', None, 'assembly'),
                    ('Form Field Assembly / Zip + Phone', None, 'assembly'), ('Form Field Assembly / Address block', None, 'assembly'),
                    ('Form Field Assembly / CC details', None, 'assembly'), ('Form Field Assembly / Password', None, 'assembly'),
                    ('Form Field Assembly / Verification Code', None, 'assembly'), ('Search Field / Obituaries', None, 'assembly')],
}
BREAKPOINTS = [  # key, viewport, template, bucket
    ('340', '≤639px (XS-Fold, built 340)', '340 HomePage', 'XS-Fold'),
    ('360', '≤639px (SM-Mobile, built 360)', 'Mobile HomePage', 'SM-Mobile'),
    ('768', '640–799px (MD-TabletV)', '768 HomePage', 'MD-TabletV'),
    ('1024', '800–1039px (LG-TabletH, built 1009)', '1024 HomePage', 'LG-TabletH'),
    ('1100', '≥1040px (XL-Desktop, built 1085)', '1100 HomePage', 'XL-Desktop'),
    ('1280', '≥1040px (XL-Desktop, built 1280)', 'Desktop HomePage', 'XL-Desktop'),
]
BP_KEYS = [b[0] for b in BREAKPOINTS]
TPL2BP = {b[2]: b[0] for b in BREAKPOINTS}
VIEWPORT = {b[0]: b[1] for b in BREAKPOINTS}
PLACEHOLDER = {'#E1A1FF': 'image placeholder fill', '#D9D9D9': 'image placeholder fill', '#FFC76B': 'video placeholder accent',
               '#8BE38B': 'ad placeholder fill', '#9CFF9C': 'ad placeholder fill'}
# Hand-written notes, re-checked against the previews for this export.
CURATED = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'curated.json')))

# ----------------------------------------------------------------- helpers
def slug(s):
    s = s.lower().replace('&', 'and').replace('+', '')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
def num(v):
    if v is None: return ''
    return str(int(v)) if float(v).is_integer() else str(round(v, 2))
def size(n): return f"{num(n['w'])}×{num(n['h'])}"
def url(fk, nid): return f"https://www.figma.com/design/{fk}/?node-id={nid.replace(':', '-')}"
def vlabel(v):
    vp = v.get('variantProperties')
    return ', '.join(f'{k}={x}' for k, x in vp.items()) if vp else v['name']
def layout_str(l):
    if not l: return ''
    s = f"{l['dir'].lower()} gap {num(l['gap'])} pad {'/'.join(num(p) for p in l['pad'])} main {l['main']} cross {l['cross']}"
    if l.get('wrap'): s += f" wrap row-gap {num(l.get('rowGap'))}"
    return s
def walk(n, fn, depth=0, parent=None):
    fn(n, depth, parent)
    for c in n.get('children', []): walk(c, fn, depth + 1, n)
def esc(s): return str(s).replace('|', '\\|').replace('\n', ' ')
def rel(a, b): return os.path.relpath(b, os.path.dirname(a)).replace(os.sep, '/')

# ----------------------------------------------------------------- load
sections = []
for f in sorted(glob.glob(os.path.join(RAW, 'specs_*.json'))):
    d = json.load(open(f))['result']
    for s in d['sections']:
        s['fileKey'] = d['fileKey']; s['fileName'] = d['fileName']; sections.append(s)
usage = {}
for f in glob.glob(os.path.join(RAW, 'usage_*.json')):
    usage.update(json.load(open(f))['result']['out'])
colormodes = json.load(open(os.path.join(RAW, 'colormodes.json')))

# order items
items = []
hp = sorted([s for s in sections if s['group'] == 'homepage'], key=lambda s: s['order'])
for s in hp:
    s['name'] = s['section']; s['kind'] = 'assembly' if s['typeLabel'].lower().startswith('assembly') else 'component'
    items.append(s)
for g in ('menus-and-parts', 'form-fields'):
    pool = [s for s in sections if s['group'] == g]
    for entry in MANIFEST[g]:
        fname, ename, kind = entry[:3]; nid = entry[3] if len(entry) > 3 else None
        s = next(x for x in pool if x['section'] == fname and (nid is None or x['mains'][0]['id'] == nid))
        s['name'] = ename or fname; s['kind'] = kind; items.append(s)
for i, s in enumerate(items):
    s['order'] = i + 1; s['slug'] = slug(s['name'])
    s['dir'] = f"{s['group']}/{'assemblies' if s['kind'] == 'assembly' else 'components'}/{s['order']:02d}-{s['slug']}"
    vs = []
    for m in s['mains']:
        if m['type'] == 'COMPONENT_SET':
            for v in m['variants']: v['_main'] = m; vs.append(v)
        else:
            t = m['tree']; t['key'] = m['key']; t['variantProperties'] = None; t['componentDescription'] = m['componentDescription']; t['_main'] = m; vs.append(t)
    s['variants'] = vs
    if s['group'] != 'homepage':
        n = len(vs)
        s['typeLabel'] = f"{s['kind'].title()} · " + (f"{n} variants" if s['mains'][0]['type'] == 'COMPONENT_SET' else 'Standalone')
        s['description'] = s.get('description') or s['mains'][0].get('componentDescription')
    # previews (same naming as extract.js / saveprev.py)
    seen = {}
    for v in vs:
        if v.get('variantProperties'):
            base = s_slug = slug(s['section']) + '--' + '-'.join(slug(str(x)) for x in v['variantProperties'].values())
        else:
            base = slug(s['section']) if len(s['mains']) == 1 else slug(s['section']) + '--' + slug(v['name'])
        k = seen.get(base, 0) + 1; seen[base] = k
        fn = base + ('' if k == 1 else f'-{k}') + '.png'
        src = os.path.join(PREV, slug(s['section']), fn)
        outfn = s['slug'] + fn[len(slug(s['section'])):]  # export name, e.g. the Dashboard Mockup set
        if not v.get('variantProperties') and slug(v['name']) == slug(s['section']):  # same-named standalone mains
            outfn = s['slug'] + ('' if k == 1 else f'-{k}') + '.png'
        v['_preview'] = outfn if os.path.exists(src) else None; v['_previewSrc'] = src
        v['_label'] = vlabel(v)

byName = {s['name']: s for s in items}
compName2item = {}
for s in items:
    for m in s['mains']: compName2item.setdefault(m['name'], s)
# key "Set / Variant" or "Component" -> (item, variant)
inc_key = collections.defaultdict(list)
for s in items:
    for v in s['variants']:
        m = v['_main']
        inc_key[(m['name'] + ' / ' + v['name']) if m['type'] == 'COMPONENT_SET' else m['name']].append((s, v))

# ----------------------------------------------------------------- usage + breakpoints
def u(v): return usage.get(v['id'], {'templates': {}, 'inComponents': {}, 'other': {}})
memo = {}
def eff_templates(s, v, stack=()):
    """{template: set(via assembly names)}; direct uses get via=None"""
    if v['id'] in memo: return memo[v['id']]
    out = collections.defaultdict(set)
    for t in u(v)['templates']: out[t].add(None)
    for k in u(v)['inComponents']:
        for ps, pv in inc_key.get(k, []):
            if pv['id'] in stack: continue
            for t in eff_templates(ps, pv, stack + (v['id'],)): out[t].add(ps['name'])
    memo[v['id']] = out
    return out

def declared(s, v):
    vp = v.get('variantProperties') or {}
    vals = [str(x) for x in vp.values()]
    allvals = ' '.join(str(x) for vv in s['variants'] for x in (vv.get('variantProperties') or {}).values()).lower()
    has_fold = 'fold' in allvals; has_tab = bool(re.search(r'tablet|\b768\b', allvals)); has_1024 = bool(re.search(r'tableth|\b1024\b', allvals))
    out = set()
    for x in vals:
        lx = x.lower()
        if s['group'] == 'form-fields' and lx in ('mobile',) and 'Size' in vp: out |= {'340', '360'}; continue
        if s['group'] == 'form-fields' and lx == 'desktop' and 'Size' in vp: out |= {'768', '1024', '1100', '1280'}; continue
        if 'fold' in lx: out.add('340')
        elif re.search(r'sm-mobile|^mobile', lx):
            out.add('360')
            if not has_fold: out.add('340')
            if not has_tab: out.add('768')
        elif re.search(r'md-tabletv|^tabletv$|^tablet$', lx): out.add('768')
        elif re.search(r'lg-tableth|^tableth$|^1024$', lx): out.add('1024')
        elif lx == '1100': out.add('1100')
        elif lx == '1280': out.add('1280')
        elif re.search(r'xl-desktop|^desktop$', lx):
            out |= {'1100', '1280'}
            if not has_1024: out.add('1024')
    return out

for s in items:
    allbp = set()
    for v in s['variants']:
        et = eff_templates(s, v)
        used = {TPL2BP[t] for t in et if t in TPL2BP}
        v['_used'] = used; v['_declared'] = declared(s, v)
        v['_bps'] = used or v['_declared']
        allbp |= v['_bps']
    s['breakpoints'] = [b for b in BP_KEYS if b in allbp]

# ----------------------------------------------------------------- dependencies
def instances(n, acc):
    def f(x, d, p):
        if x['type'] == 'INSTANCE': acc.append(x)
    walk(n, f)
    return acc
for s in items:
    cnt = collections.Counter(); keys = {}
    for v in s['variants']:
        c = collections.Counter(i.get('component') for i in instances(v, []) if i is not v)
        for k, n in c.items(): cnt[k] = max(cnt[k], n)
    own = {m['name'] for m in s['mains']}
    s['builtFrom'] = [{'name': k, 'count': n, 'item': compName2item.get(k)} for k, n in cnt.items() if k and k not in own]
for s in items:
    s['builtInto'] = [p for p in items if any(b['item'] is s for b in p['builtFrom'])]

# ----------------------------------------------------------------- per-item analysis
FONT_OK = {'Noto Sans', 'Noto Serif'}
def analyse(s):
    typo = collections.OrderedDict(); colors = collections.OrderedDict(); ratios = []; ads = []; refs = set(); issues = []
    fonts_bad = collections.OrderedDict(); hard = collections.Counter(); detached = []
    for v in s['variants']:
        bad = collections.Counter()
        def f(n, d, p):
            if n['type'] == 'TEXT':
                for st in n.get('styles', []):
                    col = (st.get('color') or [{}])[0] if isinstance(st.get('color'), list) else {}
                    tv = n.get('vars') or {}
                    ttok = None
                    for k in ('fontSize', 'lineHeight', 'fontFamily'):
                        if tv.get(k):
                            x = tv[k] if isinstance(tv[k], str) else tv[k][0]
                            name = re.sub(r'^[^/]+/', '', x)  # drop the collection
                            # primitives (font/size/16) keep their full name; composite roles drop the property (Editorial/Titles/X/Size -> Editorial/Titles/X)
                            ttok = name if name.startswith('font/') else name.rsplit('/', 1)[0]; break
                    key = (n['name'], st['font'], st['weight'], st['size'], st['lineHeight'], st.get('letterSpacing'), st.get('case'), col.get('hex'))
                    if key not in typo:
                        typo[key] = {'layer': n['name'], 'font': st['font'], 'weight': st['weight'], 'size': st['size'], 'lineHeight': st['lineHeight'],
                                     'letterSpacing': st.get('letterSpacing'), 'case': st.get('case'), 'decoration': st.get('decoration'),
                                     'color': col.get('hex'), 'token': col.get('variable'), 'typeToken': ttok, 'textStyle': st.get('textStyle'),
                                     'truncate': (f"{n.get('maxLines')} lines" if n.get('truncate') else None),
                                     'sample': (st.get('chars') or n.get('text') or '')[:50], 'variants': []}
                    typo[key]['variants'].append(v['_label'])
                    if st['font'] not in FONT_OK or 'Display' in st['weight']:
                        bad[f"{st['font']} {st['weight']}"] += 1
                    if col.get('type') == 'SOLID' and not col.get('variable'): hard[col['hex']] += 1
            for role in ('fills', 'strokes'):
                ps = n.get(role)
                if not isinstance(ps, list) or n['type'] == 'TEXT': continue
                for pnt in ps:
                    if pnt.get('type') != 'SOLID': continue
                    key = (n['name'], role, pnt['hex'], pnt.get('variable'))
                    if key not in colors:
                        colors[key] = {'layer': n['name'], 'role': role[:-1], 'type': 'SOLID', 'hex': pnt['hex'], 'token': pnt.get('variable'),
                                       'opacity': pnt.get('opacity'), 'note': PLACEHOLDER.get(pnt['hex'], '') if not pnt.get('variable') else '',
                                       'strokeWeight': n.get('strokeWeight') if role == 'strokes' else None}
                    if not pnt.get('variable') and n['type'] != 'INSTANCE': hard[pnt['hex']] += 1
            nm = n['name'].lower()
            is_ph = n['type'] == 'INSTANCE' and re.search(r'image placeholder|video tile', (n.get('component') or '').lower())
            is_img = (n['type'] in ('FRAME', 'RECTANGLE') and re.search(r'graphic|image|photo|thumb', nm) and any(pp.get('type') == 'IMAGE' or pp.get('hex') in PLACEHOLDER for pp in (n.get('fills') or []) if isinstance(pp, dict)))
            if (is_ph or is_img) and n['w'] >= 20 and n['h'] >= 20:
                ratios.append({'layer': n['name'], 'w': n['w'], 'h': n['h'], 'ratio': ratio(n['w'], n['h']), 'source': n.get('component') or 'frame', 'variant': v['_label']})
            if n['type'] == 'INSTANCE' and n.get('component') == 'Ad Blocks':
                ads.append({'layer': n['name'], 'unit': (n.get('variant') or {}).get('Name'), 'device': (n.get('variant') or {}).get('Device'), 'size': size(n), 'variant': v['_label']})
            elif re.search(r'\b(ad|advert|sidebar rectangle|cube|leaderboard|sponsorship)\b', nm) and n['w'] >= 100 and n['h'] >= 50 and n['type'] != 'TEXT':
                ads.append({'layer': n['name'], 'unit': None, 'device': None, 'size': size(n), 'variant': v['_label']})
            for t in (n['name'],):
                for r in re.findall(r'\b[\w-]+\.com\b|landing-[\w-]+|sponsorship_\d|bottom_leaderboard|floating_anchor|mobile_adhesion|cube_article|outstream_video', t): refs.add(r)
            if 'detached' in nm: detached.append(n['name'])
            if n['type'] not in ('TEXT', 'INSTANCE') and p is not None and not n.get('absolute') and not n.get('hidden') and p.get('clip') is not True:
                if n.get('x') is not None and p['type'] not in ('INSTANCE',) and (n['x'] < -1 or n['y'] < -1 or n['x'] + n['w'] > p['w'] + 1 or n['y'] + n['h'] > p['h'] + 1) and d <= 2 and n['type'] != 'LINE':
                    pass
        walk(v, f)
        # overflow: direct children of the variant outside its bounds
        for c in v.get('children', []):
            if c.get('hidden') or c.get('x') is None: continue
            if c['x'] < -1 or c['y'] < -1 or c['x'] + c['w'] > v['w'] + 1 or c['y'] + c['h'] > v['h'] + 1:
                if not v.get('clip'):
                    issues.append(f"`{v['_label']}`: content overflows frame — '{c['name']}' ({size(c)} at {num(c['x'])},{num(c['y'])}) exceeds frame {size(v)}.")
        if bad: fonts_bad[v['_label']] = bad
    for t in [s.get('description') or '', *(v.get('componentDescription') or '' for v in s['variants'])]:
        for r in re.findall(r'\b[a-z0-9-]+\.com(?:/[\w/-]+)?|landing-[\w-]+|sponsorship_\d|bottom_leaderboard|floating_anchor|mobile_adhesion|\.[a-z][\w-]+(?=\s|,|\))', t): refs.add(r)
    # automatic issues
    fk = s['fileKey']
    unused = [v['_label'] for v in s['variants'] if not any(u(v)[k] for k in ('templates', 'inComponents', 'other'))]
    if unused and len(unused) == len(s['variants']) and len(unused) > 1:
        issues.insert(0, f"No variant has instances in {FILES[fk]} (unused here, or used only from another file): " + ', '.join(f'`{x}`' for x in unused) + '.')
    elif unused and len(s['variants']) > 1:
        issues.insert(0, f"{len(unused)} of {len(s['variants'])} variants have no instances anywhere in {FILES[fk]} (unused, or used only from another file): " + ', '.join(f'`{x}`' for x in unused) + '.')
    for v in s['variants']:
        if v['w'] < 1 or v['h'] < 1: issues.append(f"Variant `{v['_label']}` is 0×0 (intentionally empty state?) — no preview exported.")
        if v['_used'] and v['_declared'] and not v['_used'] <= v['_declared']:
            issues.append(f"`{v['_label']}` is declared for {', '.join(b for b in BP_KEYS if b in v['_declared'])} but is placed in template(s) at {', '.join(b for b in BP_KEYS if b in v['_used'] - v['_declared'])} — check the variant choice.")
    for lab, bad in fonts_bad.items():
        issues.append(f"`{lab}`: fonts outside the production set (Noto Sans / Noto Serif, no Display styles): " + ', '.join(f'{k} ×{n}' for k, n in bad.items()) + '.')
    if hard:
        issues.append(f"{sum(hard.values())} solid paints are hard-coded (not bound to a color variable): " + ', '.join(f'{k} ×{n}' for k, n in hard.most_common(8)) + '.')
    for nm in dict.fromkeys(detached): issues.append(f"Layer '{nm}' is marked detached.")
    m0 = s['mains'][0]
    if m0.get('propertyError'):
        issues.append(f"Figma reports the component set is in an error state: \"{m0['propertyError']}\".")
    names = collections.Counter(v['name'] for v in s['variants'] if v.get('variantProperties'))
    dup = [k for k, n in names.items() if n > 1]
    if dup: issues.append('Duplicate variant names in the set: ' + ', '.join(f'{k} ×{names[k]}' for k in dup) + '.')
    cur = CURATED.get(s['name'], {})
    issues += cur.get('issues', [])
    s.update(typography=list(typo.values()), colors=list(colors.values()), imageRatios=ratios, adSlots=ads,
             productionRefs=sorted(refs), knownIssues=issues)
    rules = cur.get('rules', [])[:]
    for v in s['variants']:
        rules.append(f"{v['_label']}: {size(v)}" + (f", {layout_str(v.get('layout'))}" if v.get('layout') else '') +
                     (f" — renders at {', '.join(b for b in BP_KEYS if b in v['_bps'])}" if v['_bps'] else ' — no breakpoint (not placed in a template)'))
    s['responsiveRules'] = rules

RATIOS = [(16, 9), (4, 3), (3, 2), (1, 1), (9, 16), (3, 4), (2, 3), (21, 9), (5, 4), (2, 1)]
def ratio(w, h):
    if not h: return '—'
    r = w / h
    for a, b in RATIOS:
        if abs(r - a / b) / (a / b) < 0.03: return f'{a}:{b}'
    return f'{r:.2f}:1'

for s in items: analyse(s)

# ----------------------------------------------------------------- markdown
def anatomy(n, maxd):
    lines = []
    def lay(x):
        l = x.get('layout'); return f" [{l['dir'].lower()} gap {num(l['gap'])}]" if l else ''
    def sz(x):
        z = x.get('sizing'); return f" ({z['h'].lower()}/{z['v'].lower()})" if z else ''
    def rec(x, d):
        if d > maxd: return
        kids = x.get('children', [])
        desc = f"{'  ' * d}- {x['name']} — {x['type'].lower().replace('_', ' ')} {size(x)}{lay(x)}{sz(x)}"
        if x['type'] == 'INSTANCE':
            desc += f" → {x.get('component')}" + (f" [{', '.join(f'{k}={v}' for k, v in (x.get('variant') or {}).items())}]" if x.get('variant') else '')
        if x['type'] == 'TEXT': desc += f' "{(x.get("text") or "")[:40]}"'
        if x.get('hidden'): desc += ' (hidden)'
        lines.append(desc)
        i = 0
        while i < len(kids):
            k = kids[i]; j = i
            sig = lambda y: (y['type'], y.get('component'), json.dumps(y.get('variant')), y['name'], y['w'], y['h'], y.get('hidden'))
            while j + 1 < len(kids) and kids[j + 1]['type'] == 'INSTANCE' and sig(kids[j + 1]) == sig(k): j += 1
            if j > i:
                rec(k, d + 1); lines[-1] += f' ×{j - i + 1}'
            else: rec(k, d + 1)
            i = j + 1
    rec(n, 0)
    return '\n'.join(lines)

def where_used(s, v):
    uu = u(v); et = eff_templates(s, v)
    parts = [f"breakpoints: {', '.join(b for b in BP_KEYS if b in v['_bps']) or '—'}"]
    if uu['templates']: parts.append('templates (direct): ' + ', '.join(f'{k} ×{n}' for k, n in uu['templates'].items()))
    via = {t: sorted(x for x in vs if x) for t, vs in et.items() if any(vs)}
    if via: parts.append('templates (via assembly): ' + ', '.join(f"{t} (via {', '.join(x)})" for t, x in via.items()))
    if uu['inComponents']: parts.append('nested inside: ' + ', '.join(f'{k} ×{n}' for k, n in uu['inComponents'].items()))
    if uu['other']: parts.append('other pages: ' + ', '.join(f'{k} ×{n}' for k, n in uu['other'].items()))
    if not (uu['templates'] or uu['inComponents'] or uu['other']): parts.append('no instances in this file')
    return f"- **{v['_label']}** — " + '; '.join(parts)

def md_item(s):
    fk = s['fileKey']; g = GROUPS[s['group']]; m0 = s['mains'][0]
    path = f"{s['dir']}/{s['slug']}.md"
    fm = ['---', f'name: {json.dumps(s["name"], ensure_ascii=False)}', f"kind: {s['kind']}", f"group: {s['group']}", f"order: {s['order']}",
          f'figma_file: "{FILES[fk]} ({fk})"', f'figma_node: "{m0["id"]}"', f"component_key: {m0['key']}", f"variants: {len(s['variants'])}",
          f"breakpoints: [{', '.join(s['breakpoints'])}]",
          f"built_from: {json.dumps([b['name'] for b in s['builtFrom']], ensure_ascii=False)}",
          f"built_into: {json.dumps([p['name'] for p in s['builtInto']], ensure_ascii=False)}",
          f"spec_json: {s['slug']}.json", f"skeleton: {s['slug']}.html", f"exported: {DATE}", '---', '']
    L = fm + [f"# {s['name']}", '', f"**{s['typeLabel']}** · {g['title']} · source: {FILES[fk]} ▸ {g['page']}", '']
    if s.get('description'): L += ['> ' + s['description'].replace('\n', '\n> '), '']
    notes = [n for n in (s.get('designerNotes') or []) if n.strip()]
    if notes: L += ['**Designer notes on the canvas:**', ''] + [f"- {n.strip()}".replace('\n', ' ') for n in notes] + ['']
    L += ['## Figma references', '', f"- File: {FILES[fk]} (`{fk}`) · Page: {g['page']}" + (f" · Frame path: {s['path']}" if s.get('path') else '')]
    for m in s['mains']: L.append(f"- Main: [{m['name']}]({url(fk, m['id'])}) · node `{m['id']}` · key `{m['key']}`")
    L += ['', '| Variant | Node | Key | Size | Preview |', '|---|---|---|---|---|']
    for v in s['variants']:
        pv = f"![{esc(v['_label'])}](previews/{v['_preview']})" if v['_preview'] else '_none (0×0)_'
        L.append(f"| {esc(v['_label'])} | [{v['id']}]({url(fk, v['id'])}) | {v['key']} | {size(v)} | {pv} |")
    L += ['', '## Properties', '']
    props = {}
    for m in s['mains']: props.update(m.get('properties') or {})
    if props:
        L += ['| Property | Type | Default | Options |', '|---|---|---|---|']
        for k, p in props.items():
            L.append(f"| {k.split('#')[0]} | {p['type']} | {esc(p.get('default'))} | {esc(', '.join(p.get('options') or []))} |")
    else: L.append('_None._')
    L += ['', '## Where it is used', ''] + [where_used(s, v) for v in s['variants']]
    L += ['', '## Breakpoints', '', '| Key | Viewport | Variant(s) |', '|---|---|---|']
    for b in BP_KEYS:
        vs = [v['_label'] for v in s['variants'] if b in v['_bps']]
        if vs: L.append(f"| {b} | {VIEWPORT[b]} | {esc(', '.join(vs))} |")
    if not s['breakpoints']: L.append('| — | not placed in any homepage template | — |')
    L += ['', '## Responsive rules', ''] + [f'- {r}' for r in s['responsiveRules']]
    L += ['', '## Dependencies', '', '**Built from:**', '']
    if s['builtFrom']:
        for b in s['builtFrom']:
            if b['item']: L.append(f"- [{b['name']}]({rel(path, b['item']['dir'] + '/' + b['item']['slug'] + '.md')}) ×{b['count']}")
            else: L.append(f"- {b['name']} ×{b['count']} _(not in this export)_")
    else: L.append('_Nothing — leaf component._')
    L += ['', '**Built into:**', '']
    L += [f"- [{p['name']}]({rel(path, p['dir'] + '/' + p['slug'] + '.md')})" for p in s['builtInto']] or ['_Not used inside another exported item._']
    L += ['', '## Anatomy', '']
    depth = 5 if s['kind'] == 'component' else 3
    for v in s['variants'][:12]:
        L += [f"**{v['_label']}**", '', '```', anatomy(v, depth), '```', '']
    if len(s['variants']) > 12: L += [f"_{len(s['variants']) - 12} more variants — see `variants[].layerTree` in {s['slug']}.json._", '']
    L += ['## Size & layout', '', '| Variant | Size | Width | Height | Auto-layout | Radius | Clip |', '|---|---|---|---|---|---|---|']
    for v in s['variants']:
        z = v.get('sizing') or {}
        L.append(f"| {esc(v['_label'])} | {size(v)} | {z.get('h', '')} | {z.get('v', '')} | {layout_str(v.get('layout'))} | {esc(v.get('radius') or '')} | {'yes' if v.get('clip') else ''} |")
    L += ['', '## Typography', '']
    if s['typography']:
        L += ['| Layer | Font | Weight | Size | Line height | Letter sp. | Case | Color | Color token | Type token | Truncate | Sample | Variants |', '|---|---|---|---|---|---|---|---|---|---|---|---|---|']
        for t in s['typography'][:60]:
            L.append(f"| {esc(t['layer'][:60])} | {t['font']} | {t['weight']} | {num(t['size'])} | {t['lineHeight']} | {t['letterSpacing'] or ''} | {t['case'] or ''} | {t['color'] or ''} | {t['token'] or ''} | {t['typeToken'] or ''} | {t['truncate'] or ''} | {esc(t['sample'])} | {esc(', '.join(dict.fromkeys(t['variants'])) if len(s['variants']) > 1 and len(set(t['variants'])) < len(s['variants']) else 'all')} |")
        if len(s['typography']) > 60: L.append(f"\n_{len(s['typography']) - 60} more rows in {s['slug']}.json → typography._")
    else: L.append('_No text._')
    L += ['', '## Color & effects', '']
    if s['colors']:
        L += ['| Layer | Role | Type | Hex | Token | Opacity | Note |', '|---|---|---|---|---|---|---|']
        for c in s['colors'][:60]:
            L.append(f"| {esc(c['layer'][:60])} | {c['role']} | {c['type']} | {c['hex']} | {c['token'] or ''} | {c['opacity'] or ''} | {c['note']} |")
        if len(s['colors']) > 60: L.append(f"\n_{len(s['colors']) - 60} more rows in {s['slug']}.json → colors._")
    else: L.append('_None._')
    L += ['', '## Image ratios', '']
    if s['imageRatios']:
        L += ['| Variant | Layer | Size | Ratio | Source |', '|---|---|---|---|---|'] + [f"| {esc(r['variant'])} | {esc(r['layer'])} | {num(r['w'])}×{num(r['h'])} | {r['ratio']} | {r['source']} |" for r in s['imageRatios'][:40]]
    else: L.append('_None._')
    L += ['', '## Ad slots', '']
    if s['adSlots']:
        L += ['| Variant | Layer | Unit | Size |', '|---|---|---|---|'] + [f"| {esc(a['variant'])} | {esc(a['layer'])} | {a['unit'] or ''} | {a['size']} |" for a in s['adSlots']]
    else: L.append('_None._')
    L += ['', '## Production references', '']
    L += [f'- `{r}`' for r in s['productionRefs']] or ['_None found in descriptions or layer names._']
    L += ['', '## Known issues', '']
    L += [f'- {i}' for i in s['knownIssues']] or ['_None detected._']
    L += ['', '## Rendering steps', '',
          f"1. Pick the variant for the target breakpoint from the Breakpoints table (property values in `{s['slug']}.json` → `variants[].variantProperties`).",
          f"2. Start from `{s['slug']}.html` — each `<section>` is one variant; auto-layout is already mapped to flexbox and colors use `tokens.css` variables.",
          "3. Replace every dashed `data-component` box with the referenced component's own skeleton (links under Dependencies); leave `data-component` on the wrapper.",
          "4. Fill image slots at the ratio listed in Image ratios; fill text using the Typography table (truncate where a line clamp is listed).",
          "5. Check against the preview PNG, then against the production references.", '']
    return '\n'.join(L)

def strip_private(n):
    if isinstance(n, dict): return {k: strip_private(v) for k, v in n.items() if not k.startswith('_')}
    if isinstance(n, list): return [strip_private(x) for x in n]
    return n

def json_item(s):
    fk = s['fileKey']; m0 = s['mains'][0]; g = GROUPS[s['group']]; path = f"{s['dir']}/{s['slug']}.md"
    props = {}
    for m in s['mains']: props.update(m.get('properties') or {})
    return {
        'schema': 'mng/component-spec@1', 'kind': s['kind'], 'group': s['group'], 'name': s['name'], 'slug': s['slug'], 'order': s['order'],
        'typeLabel': s['typeLabel'], 'description': s.get('description'), 'designerNotes': s.get('designerNotes') or [],
        'figma': {'fileKey': fk, 'fileName': FILES[fk], 'page': g['page'], 'path': s.get('path'), 'mainId': m0['id'], 'mainKey': m0['key'],
                  'url': url(fk, m0['id']), 'variants': [{'label': v['_label'], 'id': v['id'], 'key': v['key'], 'url': url(fk, v['id'])} for v in s['variants']]},
        'properties': props, 'breakpoints': s['breakpoints'],
        'usage': {'templates': sorted({t for v in s['variants'] for t in eff_templates(s, v)}), 'builtInto': [p['name'] for p in s['builtInto']],
                  'perVariant': [{'label': v['_label'], 'id': v['id'], 'templatesDirect': u(v)['templates'],
                                  'templatesVia': {t: sorted(x for x in vs if x) for t, vs in eff_templates(s, v).items() if any(vs)},
                                  'inComponents': u(v)['inComponents'], 'other': u(v)['other'],
                                  'breakpoints': [b for b in BP_KEYS if b in v['_bps']]} for v in s['variants']]},
        'dependencies': {'builtFrom': [{'name': b['name'], 'count': b['count'], 'inExport': bool(b['item']), 'section': b['item']['name'] if b['item'] else None,
                                        'path': rel(path, b['item']['dir'] + '/' + b['item']['slug'] + '.md') if b['item'] else None} for b in s['builtFrom']],
                         'builtInto': [{'name': p['name'], 'path': rel(path, p['dir'] + '/' + p['slug'] + '.md')} for p in s['builtInto']]},
        'variants': [{'label': v['_label'], 'variantProperties': v.get('variantProperties'), 'id': v['id'], 'key': v['key'], 'url': url(fk, v['id']),
                      'width': v['w'], 'height': v['h'], 'layout': v.get('layout'), 'sizing': v.get('sizing'), 'fills': v.get('fills'),
                      'strokes': v.get('strokes'), 'radius': v.get('radius'), 'preview': f"previews/{v['_preview']}" if v['_preview'] else None,
                      'breakpoints': [b for b in BP_KEYS if b in v['_bps']], 'layerTree': strip_private({k: x for k, x in v.items() if k not in ('_main',)})} for v in s['variants']],
        'typography': s['typography'], 'colors': s['colors'], 'imageRatios': s['imageRatios'], 'adSlots': s['adSlots'],
        'responsiveRules': s['responsiveRules'], 'productionRefs': s['productionRefs'], 'knownIssues': s['knownIssues'],
        'skeleton': f"{s['slug']}.html", 'exported': DATE}

# ----------------------------------------------------------------- tokens
CSSNAME = lambda v: '--mng-' + re.sub(r'^Colors/color/', '', v).replace('/', '-')
used_vars = collections.Counter(); all_hex = collections.Counter(); type_combos = collections.Counter()
for s in items:
    for c in s['colors']:
        all_hex[c['hex']] += 1
        if c['token']: used_vars[c['token']] += 1
    for t in s['typography']:
        if t['color']: all_hex[t['color']] += 1
        if t['token']: used_vars[t['token']] += 1
        type_combos[(t['font'], t['weight'], t['size'], t['lineHeight'], t['letterSpacing'] or '')] += 1
DEF = colormodes['def']
colorVariables = {}
for v in sorted(used_vars):
    short = re.sub(r'^Colors/color/', '', v); modes = colormodes['out'].get(short) or {}
    base = modes.get(DEF)
    others = sorted({h for m, h in modes.items() if h and h != base})
    colorVariables[v] = {'css': CSSNAME(v), 'hex': base, 'otherModeValues': others,
                         'byTheme': {m: h for m, h in modes.items()} if others else None}

def css_color(hexv, var):
    if var and var in colorVariables: return f"var({colorVariables[var]['css']}, {hexv})"
    return hexv

# ----------------------------------------------------------------- html skeleton
def cls(s, n): return f"mng-{'a' if s['kind'] == 'assembly' else 'c'}-{s['slug']}__" + (re.sub(r'^(\d)', r'c-\1', slug(n['name'])[:40]) or 'layer')
JUST = {'MIN': 'flex-start', 'CENTER': 'center', 'MAX': 'flex-end', 'SPACE_BETWEEN': 'space-between', 'BASELINE': 'baseline'}
def node_css(n, parent):
    c = []
    z = n.get('sizing'); pl = parent.get('layout') if parent else None
    if parent is None:
        c.append(f"width:{num(n['w'])}px;min-height:{num(n['h'])}px;position:relative")
    elif pl and not n.get('absolute'):
        horiz = pl['dir'] == 'HORIZONTAL'
        for axis, val in (('h', n['w']), ('v', n['h'])):
            mode = (z or {}).get(axis, 'FIXED'); main = (axis == 'h') == horiz; prop = 'width' if axis == 'h' else 'height'
            if mode == 'FILL': c.append('flex:1 1 0;min-width:0' if main else 'align-self:stretch')
            elif mode == 'FIXED' or n['type'] == 'INSTANCE' or not n.get('layout') and n['type'] not in ('TEXT',):
                c.append(f"{prop}:{num(val)}px;flex-shrink:0")
    else:
        c.append(f"position:absolute;left:{num(n.get('x', 0))}px;top:{num(n.get('y', 0))}px;width:{num(n['w'])}px;height:{num(n['h'])}px")
    l = n.get('layout')
    if l and n['type'] != 'TEXT':
        c.append(f"display:flex;flex-direction:{'row' if l['dir'] == 'HORIZONTAL' else 'column'};gap:{num(l['gap'])}px;padding:{' '.join(num(p) + 'px' for p in l['pad'])};justify-content:{JUST.get(l['main'], 'flex-start')};align-items:{JUST.get(l['cross'], 'flex-start')}" + (';flex-wrap:wrap' if l.get('wrap') else ''))
        if parent is not None: c.append('position:relative')
    fills = n.get('fills') if n['type'] != 'TEXT' else None
    if isinstance(fills, list):
        for f in fills:
            if f.get('type') == 'SOLID': c.append(f"background:{css_color(f['hex'], f.get('variable'))}"); break
    st = n.get('strokes')
    if isinstance(st, list) and st and st[0].get('type') == 'SOLID':
        col = css_color(st[0]['hex'], st[0].get('variable')); w = n.get('strokeWeight') or 1
        if n['type'] == 'LINE': c.append(f"border-top:{num(w if not isinstance(w, list) else w[0])}px solid {col}")
        elif isinstance(w, list): c.append(';'.join(f"border-{side}:{num(x)}px solid {col}" for side, x in zip(('top', 'right', 'bottom', 'left'), w) if x))
        else: c.append(f"border:{num(w)}px {'dashed' if n.get('dash') else 'solid'} {col};box-sizing:border-box")
    r = n.get('radius')
    if r: c.append('border-radius:' + (' '.join(num(x) + 'px' for x in r) if isinstance(r, list) else num(r) + 'px'))
    if n.get('clip'): c.append('overflow:hidden')
    if n.get('opacity'): c.append(f"opacity:{n['opacity']}")
    for e in n.get('effects') or []:
        if e['type'] == 'DROP_SHADOW': c.append(f"box-shadow:{num(e.get('x') or 0)}px {num(e.get('y') or 0)}px {num(e.get('blur') or 0)}px {num(e.get('spread') or 0)}px rgba(0,0,0,{e.get('a') or .25})"); break
    if n['type'] == 'TEXT' and n.get('styles'):
        t = n['styles'][0]; serif = 'Serif' in t['font']
        wmap = {'Thin': 100, 'ExtraLight': 200, 'Light': 300, 'Regular': 400, 'Medium': 500, 'SemiBold': 600, 'Bold': 700, 'ExtraBold': 800, 'Black': 900}
        w = next((v for k, v in sorted(wmap.items(), key=lambda kv: -len(kv[0])) if k in t['weight']), 400)
        lh = 'normal' if t['lineHeight'] == 'auto' else t['lineHeight']
        col = (t.get('color') or [{}])[0] if isinstance(t.get('color'), list) else {}
        c.append(f"font-family:'{t['font']}', {'serif' if serif else 'sans-serif'};font-size:{num(t['size'])}px;font-weight:{w};line-height:{lh}" +
                 (f";letter-spacing:{t['letterSpacing']}" if t.get('letterSpacing') else '') + (f";font-style:italic" if 'Italic' in t['weight'] else '') +
                 (f";text-transform:{'uppercase' if t['case'] == 'UPPER' else 'lowercase' if t['case'] == 'LOWER' else 'capitalize'}" if t.get('case') else '') +
                 (f";color:{css_color(col['hex'], col.get('variable'))}" if col.get('hex') else '') + f";text-align:{(n.get('align') or 'LEFT').lower()};margin:0")
        if n.get('truncate'): c.append(f"display:-webkit-box;-webkit-line-clamp:{n.get('maxLines') or 1};-webkit-box-orient:vertical;overflow:hidden")
    return ';'.join(x for x in c if x)

def html_item(s):
    rules = {}; body = []
    def rec(n, parent, ind, root_s):
        k = cls(s, n); base = k; i = 2
        while k in rules and rules[k] != node_css(n, parent): k = f"{base}-{i}"; i += 1
        css = node_css(n, parent); hid = ' hidden' if n.get('hidden') else ''
        sp = '  ' * ind
        if n['type'] == 'INSTANCE':
            target = compName2item.get(n.get('component'))
            ref = f"{target['dir']}/{target['slug']}.html" if target else 'not in this export'
            var = ', '.join(f'{a}={b}' for a, b in (n.get('variant') or {}).items())
            if target and re.search(r'image placeholder|video tile', (n.get('component') or '').lower()):
                rules[k] = css + f";aspect-ratio:{num(n['w'])}/{num(n['h'])};background:#D9D9D9;margin:0"
                body.append(f'{sp}<figure class="{k}" data-component="{html.escape(n["component"])}" data-variant="{html.escape(var)}"{hid}><!-- image slot {ratio(n["w"], n["h"])} ({size(n)}) — see {ref} --></figure>')
            else:
                rules[k] = css + ";box-sizing:border-box;border:1px dashed #8A8A8A;background:repeating-linear-gradient(45deg,#fafafa,#fafafa 6px,#f0f0f0 6px,#f0f0f0 12px);font:11px/1.3 monospace;color:#555;padding:4px;overflow:hidden"
                body.append(f'{sp}<!-- instance of "{html.escape(n.get("component") or "?")}" → {ref} -->')
                body.append(f'{sp}<div class="{k}" data-component="{html.escape(n.get("component") or "?")}" data-variant="{html.escape(var)}" data-label="{html.escape(n["name"])}"{hid}>{html.escape(n.get("component") or "?")}{" · " + html.escape(var) if var else ""}</div>')
            return
        rules[k] = css
        if n['type'] == 'TEXT':
            t = (n.get('styles') or [{}])[0]
            tag = 'h3' if 'Serif' in t.get('font', '') and 'Bold' in t.get('weight', '') and (t.get('size') or 0) >= 15 else ('h2' if re.search(r'title|eyebrow|header', n['name'], re.I) else ('p' if len(n.get('text') or '') > 40 else 'span'))
            body.append(f'{sp}<{tag} class="{k}"{hid}>{html.escape(n.get("text") or "")}</{tag}>')
            return
        body.append(f'{sp}<div class="{k}" data-layer="{html.escape(n["name"])}"{hid}>')
        for c in n.get('children', []): rec(c, n, ind + 1, root_s)
        body.append(f'{sp}</div>')
    for v in s['variants']:
        body.append(f'<section class="skel-variant" data-variant="{html.escape(v["_label"])}">')
        body.append(f'  <h1>{html.escape(s["name"])} · {html.escape(v["_label"])} · {size(v)}</h1>')
        body.append('  <div class="skel-stage">')
        rec(v, None, 2, s)
        body.append('  </div>'); body.append('</section>')
    depth = s['dir'].count('/') + 1
    head = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(s["name"])} — skeleton</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Noto+Serif:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{'../' * depth}tokens.css">
<style>
*{{box-sizing:border-box}} body{{margin:0;padding:24px;background:#f4f4f4;font-family:'Noto Sans',sans-serif;color:#141414}}
[hidden]{{display:none!important}}
.skel-variant{{margin:0 0 40px}} .skel-variant>h1{{font:600 13px/1.4 monospace;color:#555;margin:0 0 8px}}
.skel-stage{{background:#fff;display:inline-block;outline:1px solid #ddd}}
'''
    css = '\n'.join(f'.{k}{{{v}}}' for k, v in rules.items())
    return head + css + '\n</style></head>\n<body>\n<!-- Structural skeleton generated from Figma auto-layout. Instances are dashed placeholders; open the referenced file to render them. -->\n' + '\n'.join(body) + '\n</body></html>\n'

# ----------------------------------------------------------------- write
if os.path.exists(OUT):
    for g in GROUPS: shutil.rmtree(os.path.join(OUT, g), ignore_errors=True)
os.makedirs(OUT, exist_ok=True)
for s in items:
    d = os.path.join(OUT, s['dir']); os.makedirs(os.path.join(d, 'previews'), exist_ok=True)
    open(os.path.join(d, s['slug'] + '.md'), 'w').write(md_item(s))
    json.dump(json_item(s), open(os.path.join(d, s['slug'] + '.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(d, s['slug'] + '.html'), 'w').write(html_item(s))
    for v in s['variants']:
        if v['_preview']: shutil.copy(v['_previewSrc'], os.path.join(d, 'previews', v['_preview']))

tokens = {'schema': 'mng/tokens@1', 'exported': DATE, 'defaultTheme': DEF, 'colorVariables': colorVariables,
          'hexInUse': dict(all_hex.most_common()), 'placeholders': PLACEHOLDER,
          'typeCombinations': [{'font': k[0], 'weight': k[1], 'size': k[2], 'lineHeight': k[3], 'letterSpacing': k[4] or None, 'count': n} for k, n in type_combos.most_common()],
          'breakpoints': [{'key': b[0], 'viewport': b[1], 'template': b[2], 'bucket': b[3]} for b in BREAKPOINTS]}
json.dump(tokens, open(os.path.join(OUT, 'tokens.json'), 'w'), indent=1, ensure_ascii=False)
css = [':root {']
for v, t in colorVariables.items():
    css.append(f"  {t['css']}: {t['hex']};" + (f"  /* varies by theme — see tokens.json byTheme */" if t['otherModeValues'] else ''))
css += ['  --mng-font-sans: "Noto Sans", system-ui, sans-serif;', '  --mng-font-serif: "Noto Serif", Georgia, serif;', '}', '']
open(os.path.join(OUT, 'tokens.css'), 'w').write('\n'.join(css))

index = {'schema': 'mng/index@1', 'exported': DATE, 'sources': GROUPS, 'files': FILES,
         'items': [{'order': s['order'], 'name': s['name'], 'group': s['group'], 'kind': s['kind'], 'typeLabel': s['typeLabel'], 'variants': len(s['variants']),
                    'breakpoints': s['breakpoints'], 'builtFrom': [b['name'] for b in s['builtFrom']], 'builtInto': [p['name'] for p in s['builtInto']],
                    'md': f"{s['dir']}/{s['slug']}.md", 'json': f"{s['dir']}/{s['slug']}.json", 'html': f"{s['dir']}/{s['slug']}.html",
                    'figmaFile': s['fileKey'], 'figmaNode': s['mains'][0]['id'], 'issues': len(s['knownIssues'])} for s in items],
         'templates': []}
json.dump(index, open(os.path.join(OUT, 'index.json'), 'w'), indent=1, ensure_ascii=False)

# README
nv = sum(len(s['variants']) for s in items)
R = ['# MNG Design System — component spec export', '',
     f"Exported {DATE} from Figma. {len(items)} items ({sum(s['kind'] == 'component' for s in items)} components, {sum(s['kind'] == 'assembly' for s in items)} assemblies, {nv} variants). "
     'Page templates are not included; the homepage templates are used only as "where it is used" and breakpoint evidence.', '',
     'Rebuild: run the calls in `scripts/design-system-export/extract.js` in Figma, then `python3 scripts/design-system-export/build-design-system-export.py <raw> <previews> figma-exports/mng-design-system-export`.', '',
     '## Sources', ''] + [f"- **{g['title']}** — {g['source']}" for g in GROUPS.values()] + [
     '', '## How an agent should use this folder', '',
     '1. Read `index.json` to find the item (by name, group or breakpoint). Items are numbered in build order: leaf components before the assemblies that contain them.',
     "2. Open the item's `.md` for the human-readable spec, or its `.json` twin for exact values (`variants[].layerTree` holds the full Figma layer tree with sizes, auto-layout, fills, text styles, bound variables and instance references).",
     '3. Start rendering from the `.html` skeleton, which already maps auto-layout to flexbox and colors to `tokens.css`. Replace each dashed `data-component` placeholder with the skeleton of the referenced component.',
     '4. Pick variants per breakpoint using the breakpoint table below.',
     '5. Check `Known issues` before trusting a value; compare with the preview PNGs.',
     '6. Typography: the Type token column names the bound typography token group (for example `Editorial/Body/Excerpt`). Use those tokens rather than the raw values; Figma binds the `…/Style` token (font style) instead of `…/Weight`, and code uses the weight.',
     '', '## Breakpoints', '', '| Key | Viewport | Template | Bucket |', '|---|---|---|---|'] + [f'| {b[0]} | {b[1]} | {b[2]} | {b[3]} |' for b in BREAKPOINTS] + [
     '', 'Variant values map onto these keys as follows: `XS-Fold`/`FOLD` → 340, `SM-Mobile`/`Mobile` → 360 (and 340 when no Fold variant exists), `MD-TabletV`/`Tablet` → 768, `LG-TabletH`/`1024` → 1024, `XL-Desktop`/`Desktop` → 1100 and 1280. Form-field `Size=Mobile` → ≤639px and `Size=Desktop` → ≥640px. When a variant is placed in a homepage template, the template decides its breakpoints.', '']
for g, meta in GROUPS.items():
    gi = [s for s in items if s['group'] == g]
    R += [f"## {meta['title']} ({len(gi)})", '', '| # | Item | Kind | Variants | Breakpoints | Built from (in export) | Issues |', '|---|---|---|---|---|---|---|']
    for s in gi:
        R.append(f"| {s['order']} | [{s['name']}]({s['dir']}/{s['slug']}.md) | {s['kind']} | {len(s['variants'])} | {', '.join(s['breakpoints'])} | {', '.join(b['name'] for b in s['builtFrom'] if b['item'])} | {len(s['knownIssues'])} |")
    R.append('')
R += ['## Dependency graph', '', '```mermaid', 'flowchart LR']
nid = {s['name']: f'n{i}' for i, s in enumerate(items)}
for g, meta in GROUPS.items():
    R.append(f'  subgraph {g.replace("-", "_")}["{meta["title"]}"]')
    for s in items:
        if s['group'] == g:
            lab = s['name'].replace('"', "'")
            R.append(f'    {nid[s["name"]]}{"[[" if s["kind"] == "assembly" else "["}"{lab}"{"]]" if s["kind"] == "assembly" else "]"}')
    R.append('  end')
for s in items:
    for b in s['builtFrom']:
        if b['item']: R.append(f"  {nid[b['item']['name']]} --> {nid[s['name']]}")
R += ['```', '', 'Assemblies are drawn as `[[ ]]`. Arrows point from the building block to the item that contains it.', '',
      '## Tokens', '', f"`tokens.css` defines {len(colorVariables)} color variables bound in Figma (default theme: {DEF}); `tokens.json` also lists every theme's value for the theme-varying colors, every hex value in use, placeholder colors, all font/size/line-height combinations and the breakpoints.", '',
      '| Variable | CSS | Hex | Varies by theme |', '|---|---|---|---|'] + [f"| {v} | {t['css']} | {t['hex']} | {'yes (' + str(len(t['otherModeValues']) + 1) + ' values)' if t['otherModeValues'] else ''} |" for v, t in colorVariables.items()] + [
      '', '## Folder layout', '', '```', 'README.md  index.json  tokens.json  tokens.css', '<group>/components/NN-slug/   slug.md  slug.json  slug.html  previews/*.png',
      '<group>/assemblies/NN-slug/   …same…', '```', '', 'Groups: `homepage/`, `menus-and-parts/`, `form-fields/`.', '',
      '## Not included', '',
      '- Components on Menus and Parts outside the requested frames (AccountMenu in Frame 12695, Footer_w_signup in Frame 12775, the draft Logo, Event Card). They appear only as external references where other items use them.',
      '- Components from other pages (Icons, Ad Blocks, Button Primary/Linkstyle, CheckBox, NavMenu, etc.). These are listed as "not in this export" dependencies.',
      '- Page templates (components only). Template names such as "Desktop HomePage" still appear in each spec under Where it is used.',
      '- Content rules and accessibility notes.', '']
open(os.path.join(OUT, 'README.md'), 'w').write('\n'.join(R))
print(f'{len(items)} items, {nv} variants, {sum(1 for s in items for v in s["variants"] if v["_preview"])} previews → {OUT}')
