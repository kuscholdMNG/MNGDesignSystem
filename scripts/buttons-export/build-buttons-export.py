#!/usr/bin/env python3
"""Build figma-exports/mng-buttons-export/ from raw Figma dumps.

Usage:  python3 build-buttons-export.py <raw_dir> <out_dir>

<raw_dir> must hold three files saved from figma_execute results (see extract.js
in this folder for the exact Figma plugin code):
  specs.json     {"fileKey", "page", "items": [{set, doc, texts}, ...]} for the 8 sets, in META order
  previews.json  {"result": {"out": {variantNodeId: base64 PNG @2x}}}
  docs.json      {"result": {"out": {docFrameId: base64 PNG @0.5x}}}
<out_dir> is deleted and rebuilt (point it at a scratch copy, then replace the repo folder).
Curated text (descriptions, responsive rules, curated known issues) lives in META below;
update it when Karl changes a decision. Last used 2026-10-02.
"""
import json, base64, re, os, shutil, html, sys
from collections import OrderedDict, Counter, defaultdict

RAW = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(RAW), 'mng-buttons-export')
DATE = os.environ.get('EXPORT_DATE', '2026-10-02')
FILE_KEY = 'jFHYqhZbJjvWQmDI4myCsd'
FILE_NAME = 'MNG Design System'
PAGE = 'Buttons | 2026.09.30'
PAGE_ID = '1079:34282'
ICONS_SET = '4693:5'

def url(nid): return f'https://www.figma.com/design/{FILE_KEY}/?node-id={nid.replace(":", "-")}'

specs = json.load(open(os.path.join(RAW, 'specs.json')))
previews = json.load(open(os.path.join(RAW, 'previews.json')))['result']['out']
docpngs = json.load(open(os.path.join(RAW, 'docs.json')))['result']['out']

CTA_BP = '''| Breakpoint value | Viewport (MNG templates) | Behavior |
|---|---|---|
| Desktop | ≥640px (768, 1024, 1100, 1280 templates) | The `Button` hugs its label and icons |
| Mobile | ≤639px (340 XS-Fold, 360 SM-Mobile templates) | The `Button` fills the container width, inside the 8px side margin |

*The viewport mapping is the export convention, not a Figma property; Figma only says Desktop / Mobile.*'''

CTA_RULES = [
    '**Desktop** (`Breakpoint=Desktop`): the `Button` frame hugs its label and icons (HUG horizontally) inside the variant root, which keeps an 8px left/right margin. Buttons in a row or a stack keep a 16px gap.',
    '**Mobile** (`Breakpoint=Mobile`): the `Button` frame fills the container width (FILL) inside the same 8px margin. Stacked buttons use an 8px gap.',
    '**Height:** 40px in every state (8px top/bottom padding with a 40px min-height). It grows only when the label wraps to a second line.',
    'The breakpoint split is Desktop vs Mobile only; there are no per-template variants (340/768/1024/1100/1280). Use Mobile below 640px and Desktop from 640px up unless a layout says otherwise.',
]
FOCUS_RULE = ('**Focus ring:** InFocus adds one `Focus Ring` frame, absolutely positioned 1px outside the element, with a 2px OUTSIDE stroke bound to `color/gray/black`. '
              'It draws outside the component and never changes its size or moves anything inside or around it (a 40px button reads as 46px with the ring). '
              'In CSS: `outline: 2px solid var(--color-gray-black); outline-offset: 1px;` or an absolutely positioned pseudo-element; never a border or padding change.')

META = [
    dict(idx=0, order=1, name='Button Primary', slug='button-primary',
         desc='Primary CTA button: the one preferred action on a page. Brand-primary fill, white Noto Sans Bold 16px Title Case label, optional 16px icon left or right.',
         rules=CTA_RULES + [FOCUS_RULE], bp=CTA_BP, issues=[]),
    dict(idx=1, order=2, name='Button Secondary', slug='button-secondary',
         desc='Secondary button: white fill, 1px brand-primary border and brand-primary label. Use when actions are equal, or next to a single Primary.',
         rules=CTA_RULES + [FOCUS_RULE], bp=CTA_BP, issues=[]),
    dict(idx=2, order=3, name='Button Tertiary', slug='button-tertiary',
         desc='Tertiary button: light-gray fill (color/gray/600), 1px gray border (color/gray/400), near-black label. Lowest-emphasis boxed button.',
         rules=CTA_RULES + [FOCUS_RULE], bp=CTA_BP, issues=[]),
    dict(idx=3, order=4, name='Action Button', slug='action-button',
         desc='Small icon + label utility action (documented example: "Copy Link"). No box at rest; a 1px black border appears on Hover/Pressed. Figma set name: `Button Action`.',
         rules=['Single size at every breakpoint (95×32, HUG). No Breakpoint property. It stays compact (32px), not 40px (Karl, 2026-10-02).',
                'Width hugs icon + label; swapping the label changes the width.', FOCUS_RULE],
         bp=None,
         issues=['**Name swap (2026-10-02).** This documented set is `Button Action` (`7075:6357`). The older library set on the same page (`5417:3876`, formerly `Button Action`, kept for Reader Dashboard files) is now `Action Button`. The documentation frame keeps the page title "Action Button".',
                 '**Single-purpose reference.** This set only documents "Copy Link". The older `Action Button` library set bundles Resend Invitation, Link Copied, Share (Android/Apple/Unknown), Preview Most Recent, Save/Saved, Gift Article, Remove, Cancel and Delete as hidden layers, none exposed as variants. To render another action, swap the icon instance and the label text.',
                 '**Hidden trailing icon.** Every variant carries a hidden `Icon Right` (content_copy) after the label. It is never shown; ignore it when rendering.',
                 '**Margin not specified** (open spec gap, per the Figma Specifications column).']),
    dict(idx=4, order=5, name='Button Linkstyle', slug='button-linkstyle',
         desc='Text-link styled button (used for disclosures and inline CTAs such as "Forgot password?"). Underlined brand-primary text at rest; a 1px brand-primary box appears on Hover/Pressed.',
         rules=['Single size at every breakpoint. No Breakpoint property. It stays compact (38px with one line), not 40px (Karl, 2026-10-02).',
                '`Style=1 Row` keeps the label on one line (157×38 with sample text). `Style=Stacked` fixes the text width at 75px so the label wraps to two lines (91×60), for narrow right-aligned slots.', FOCUS_RULE],
         bp=None,
         issues=['**Margin not specified** (open spec gap, per the Figma Specifications column).']),
    dict(idx=5, order=6, name='Pop-Up Modal Close', slug='pop-up-modal-close',
         desc='Circular 32px close (X) button for pop-up modals (ModalsCenter, Modals/*). Light-gray circle at rest, white on Hover/Pressed; InFocus keeps the Default look and adds the ring.',
         rules=['Single size at every breakpoint (32×32 in every state). No Breakpoint property.',
                'Sits in the modal header, top-right; see ModalsCenter in the main file.', FOCUS_RULE.replace('a 40px button reads as 46px', 'the 32px circle reads as 38px')],
         bp=None,
         issues=['**Margin not specified** (open spec gap, per the Figma Specifications column).']),
    dict(idx=6, order=7, name='In-Line Close', slug='in-line-close',
         desc='Close (X) button for in-line panels and alerts (InLineMessage, ModalsOffset). Bare 12px icon in a 40px hit area at rest; the 28px `Box` gets a white fill and 1px near-black border on Hover/Pressed.',
         rules=['Single size at every breakpoint (40×40 hit area). No Breakpoint property.',
                'Every state has the same layers (`Button` › `Box` › `Icon`); the `Box` has no fill or border in Default and InFocus.',
                'Usually placed top-right of an InLineMessage panel, with the hit area aligned to the panel padding.',
                FOCUS_RULE.replace('(a 40px button reads as 46px with the ring)', '(the ring surrounds the 40px hit area with 4px corners, matching the Hover/Pressed box)')],
         bp=None,
         issues=['**Margin not specified** (open spec gap, per the Figma Specifications column).']),
    dict(idx=7, order=8, name='Non-Button Hyperlink', slug='non-button-hyperlink',
         desc='Plain in-text hyperlink (not a button). Brand-primary text with a 1px bottom border: dashed at rest, solid on Hover/Pressed, 2px teal box on InFocus. Figma set name: `Hyperlink`.',
         rules=['Hugs its text at every breakpoint. No Breakpoint property.',
                'Implement the underline as `border-bottom`, not `text-decoration` (that is how Figma builds it).',
                '**Intentional, matches production (Karl, 2026-10-02):** 16.5px text, a teal (color/theme/primary) 2px focus box with 4px corners instead of the black ring, and the dashed underline kept inside the InFocus box (`Underline` › `Label`). Because the focus box is part of the layout, InFocus is 2px taller (25 vs 23px). Do not "fix" these.'],
         bp=None,
         issues=[]),
]

# ---------------------------------------------------------------- helpers
def tok(v):
    if not v: return None
    return v.split('/', 1)[1] if v.startswith(('Colors/', 'Spacing & Radius/')) else v

def css_var(t): return '--' + t.replace('/', '-')

def paint_str(ps):
    if not ps or ps == 'mixed': return None
    out = []
    for p in ps:
        if p['type'] == 'SOLID': out.append(tok(p.get('variable')) or p['hex'] + ' (unbound)')
        else: out.append(p['type'])
    return ', '.join(out)

def short_vprops(vp, keys):
    return ' / '.join(vp[k] for k in keys)

def vslug(vp, keys):
    return '-'.join(re.sub(r'[^a-z0-9]+', '-', vp[k].lower()).strip('-') for k in keys)

def walk(n, fn, depth=0, parent=None):
    fn(n, depth, parent)
    for c in n.get('children', []) or []:
        walk(c, fn, depth + 1, n)

def layout_str(n):
    l = n.get('layout')
    if not l: return 'no auto-layout'
    p = l['pad']
    return f"{l['dir'].lower()}, gap {fmt(l['gap'])}, pad {'/'.join(fmt(x) for x in p)}"

def fmt(x):
    if isinstance(x, float) and x.is_integer(): return str(int(x))
    return str(round(x, 2)) if isinstance(x, float) else str(x)

def sizing_str(n):
    s = n.get('sizing')
    return f"{s['h']}×{s['v']}" if s else '—'

def radius_str(n):
    r = n.get('radius')
    if r is None: return '—'
    rv = (n.get('vars') or {}).get('topLeftRadius')
    if isinstance(r, list): return '/'.join(fmt(x) for x in r)
    return fmt(r) + (f' ({tok(rv)})' if rv else '')

def node_line(n):
    bits = [f"{fmt(n['w'])}×{fmt(n['h'])}"]
    if n.get('layout'): bits.append(layout_str(n))
    if n.get('sizing'): bits.append(sizing_str(n))
    if n.get('minH'): bits.append(f"min-h {fmt(n['minH'])}")
    if n.get('absolute'): bits.append(f"absolute at {fmt(n.get('x',0))},{fmt(n.get('y',0))}")
    if n.get('radius') is not None: bits.append('r' + radius_str(n))
    f = paint_str(n.get('fills'))
    if f: bits.append('fill ' + f)
    s = paint_str(n.get('strokes'))
    if s:
        sw = n.get('strokeWeight')
        sw = '/'.join(fmt(x) for x in sw) if isinstance(sw, list) else fmt(sw)
        bits.append(f"stroke {s}, {sw} {n.get('strokeAlign','').lower()}" + (' dashed' if n.get('dash') else ''))
    if n['type'] == 'TEXT':
        st = n['styles'][0]
        bits.append(f"\"{n['text'][:40]}\" {st['font']} {st['weight']} {fmt(st['size'])}px, align {n['align'].lower()}")
    if n['type'] == 'INSTANCE':
        bits.append(f"→ {n.get('component')} ({', '.join(f'{k}={v}' for k,v in (n.get('variant') or {}).items())})")
    if n.get('hidden'): bits.append('**hidden**')
    return f"- **{n['name']}** `{n['type']}` — " + ', '.join(bits)

def anatomy(n, maxd=5):
    lines = []
    def f(x, d, p):
        if d <= maxd: lines.append('  ' * d + node_line(x))
    walk(n, f)
    return '\n'.join(lines)

ICON_GLYPH = {'close': '✕', 'new-tab': '↗', 'content_copy': '⧉', 'floppy-disk': '💾', 'user-plus': '+'}

def css_paint(p):
    t = tok(p.get('variable'))
    return f"var({css_var(t)}, {p['hex']})" if t else p['hex']

def node_css(n, parent):
    css = []
    l = n.get('layout')
    if l:
        css.append('display:flex')
        css.append('flex-direction:' + ('row' if l['dir'] == 'HORIZONTAL' else 'column'))
        css.append(f"gap:{fmt(l['gap'])}px")
        css.append('padding:' + ' '.join(fmt(x) + 'px' for x in l['pad']))
        m = {'MIN': 'flex-start', 'CENTER': 'center', 'MAX': 'flex-end', 'SPACE_BETWEEN': 'space-between', 'BASELINE': 'baseline'}
        css.append('justify-content:' + m.get(l['main'], 'flex-start'))
        css.append('align-items:' + m.get(l['cross'], 'flex-start'))
    pl = parent.get('layout') if parent else None
    s = n.get('sizing') or {}
    if n.get('absolute'):
        css.append('position:absolute')
        c = n.get('constraints') or {}
        if c.get('horizontal') == 'STRETCH' and parent:
            css.append(f"left:{fmt(n['x'])}px;right:{fmt(parent['w'] - n['x'] - n['w'])}px")
        else:
            css.append(f"left:{fmt(n.get('x',0))}px;width:{fmt(n['w'])}px")
        if c.get('vertical') == 'STRETCH' and parent:
            css.append(f"top:{fmt(n['y'])}px;bottom:{fmt(parent['h'] - n['y'] - n['h'])}px")
        else:
            css.append(f"top:{fmt(n.get('y',0))}px;height:{fmt(n['h'])}px")
    else:
        horiz_main = pl and pl['dir'] == 'HORIZONTAL'
        for axis, dim in (('h', 'width'), ('v', 'height')):
            mode = s.get(axis)
            main = (axis == 'h') == bool(horiz_main)
            if mode == 'FIXED' or (n['type'] == 'INSTANCE' and mode == 'HUG') or (not pl and mode == 'FIXED'):
                css.append(f"{dim}:{fmt(n['w'] if axis=='h' else n['h'])}px")
                if pl and main: css.append('flex-shrink:0')
            elif mode == 'FILL' and pl:
                css.append('flex:1 1 0' if main else 'align-self:stretch')
    if n.get('minH'): css.append(f"min-height:{fmt(n['minH'])}px")
    if n.get('minW'): css.append(f"min-width:{fmt(n['minW'])}px")
    r = n.get('radius')
    if r is not None:
        rv = (n.get('vars') or {}).get('topLeftRadius')
        rr = f"var({css_var(tok(rv))}, {fmt(r)}px)" if rv and not isinstance(r, list) else (' '.join(fmt(x)+'px' for x in r) if isinstance(r, list) else f'{fmt(r)}px')
        css.append('border-radius:' + rr)
    fills = n.get('fills')
    if fills and fills != 'mixed' and n['type'] != 'TEXT':
        css.append('background:' + css_paint(fills[0]))
    st = n.get('strokes')
    if st and st != 'mixed':
        col = css_paint(st[0]); w = n.get('strokeWeight'); al = n.get('strokeAlign')
        style = 'dashed' if n.get('dash') else 'solid'
        if isinstance(w, list):
            for side, ww in zip(('top', 'right', 'bottom', 'left'), w):
                if ww: css.append(f'border-{side}:{fmt(ww)}px {style} {col}')
        elif al == 'OUTSIDE':
            css.append(f'box-shadow:0 0 0 {fmt(w)}px {col}')
        elif al == 'INSIDE' and style == 'solid':
            css.append(f'box-shadow:inset 0 0 0 {fmt(w)}px {col}')
        else:
            css.append(f'border:{fmt(w)}px {style} {col}')
    if n.get('clip'): css.append('overflow:hidden')
    if any(c.get('absolute') for c in n.get('children', []) or []): css.append('position:relative')
    if n['type'] == 'TEXT':
        stl = n['styles'][0]
        wt = 700 if 'Bold' in stl['weight'] else 400
        lh = 'normal' if stl['lineHeight'] == 'auto' else stl['lineHeight']
        css.append(f"font:{wt} {fmt(stl['size'])}px/{lh} '{stl['font']}',sans-serif")
        if stl.get('color'): css.append('color:' + css_paint(stl['color'][0]))
        css.append('text-align:' + n['align'].lower())
        if n.get('autoResize') == 'WIDTH_AND_HEIGHT': css.append('white-space:nowrap')
        if stl.get('case') == 'UPPER': css.append('text-transform:uppercase')
    return ';'.join(css)

def cls(slug, name): return f"mng-{slug}__" + (re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-') or 'layer')

def node_html(n, slug, parent=None, ind=4):
    pad = ' ' * ind
    hid = ' hidden' if n.get('hidden') else ''
    c = cls(slug, n['name'])
    st = node_css(n, parent)
    if n['type'] == 'TEXT':
        return f'{pad}<span class="{c}" data-layer="{html.escape(n["name"])}" style="{st}"{hid}>{html.escape(n["text"])}</span>'
    if n['type'] == 'INSTANCE':
        var = ', '.join(f'{k}={v}' for k, v in (n.get('variant') or {}).items())
        g = ICON_GLYPH.get((n.get('variant') or {}).get('Name', ''), '◻')
        return (f'{pad}<!-- instance of {n.get("component")} ({var}) — Figma node {n.get("mainId")}; not part of this export -->\n'
                f'{pad}<span class="mng-instance {c}" data-component="{html.escape(n.get("component") or "")}" data-variant="{html.escape(var)}" data-label="{html.escape(n["name"])}" aria-hidden="true" style="{st}"{hid}>{g}</span>')
    kids = '\n'.join(node_html(k, slug, n, ind + 2) for k in n.get('children', []) or [])
    aria = ' aria-hidden="true"' if n['name'] == 'Focus Ring' else ''
    return f'{pad}<div class="{c}" data-layer="{html.escape(n["name"])}" style="{st}"{hid}{aria}>\n{kids}\n{pad}</div>' if kids else f'{pad}<div class="{c}" data-layer="{html.escape(n["name"])}" style="{st}"{hid}{aria}></div>'

# ---------------------------------------------------------------- build
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(os.path.join(OUT, 'components'))
index_items = []
token_use = defaultdict(set)
all_hex = Counter()
type_combos = Counter()

PROP_ORDER = {'Breakpoint': 0, 'Icon': 1, 'Style': 1, 'State': 2}
STATE_ORDER = ['Default', 'Hover', 'Pressed', 'InFocus']

for meta in META:
    item = specs['items'][meta['idx']]
    s = item['set']; doc = item['doc']; texts = item['texts']
    slug = meta['slug']; nn = f"{meta['order']:02d}-{slug}"
    d = os.path.join(OUT, 'components', nn); os.makedirs(os.path.join(d, 'previews'))
    keys = sorted(s['properties'].keys(), key=lambda k: PROP_ORDER.get(k, 5))
    def vkey(v):
        vp = v['variantProperties']
        FIX = {'State': STATE_ORDER, 'Breakpoint': ['Desktop', 'Mobile'], 'Icon': ['None', 'Left', 'Right'], 'Style': ['1 Row', 'Stacked']}
        return tuple((FIX[k].index(vp[k]) if k in FIX else s['properties'][k]['options'].index(vp[k])) for k in keys)
    variants = sorted(s['variants'], key=vkey)
    # previews
    for v in variants:
        v['_label'] = short_vprops(v['variantProperties'], keys)
        fn = f"{slug}--{vslug(v['variantProperties'], keys)}.png"
        open(os.path.join(d, 'previews', fn), 'wb').write(base64.b64decode(previews[v['id']]))
        v['_preview'] = 'previews/' + fn
    docfn = f'{slug}--documentation.png'
    open(os.path.join(d, 'previews', docfn), 'wb').write(base64.b64decode(docpngs[doc['id']]))

    # usage
    total = sum(v['usage']['total'] for v in variants)
    built_into = Counter(); pages = Counter(); nested = 0
    for v in variants:
        for k, c in v['usage']['inComponents'].items(): built_into[k.split('/')[0]] += c
        for k, c in v['usage']['other'].items(): pages[k.split(' ▸ ')[0]] += c
        nested += v['usage']['nested']
    # deps
    deps = Counter(); icons = Counter(); colors = OrderedDict(); typo = OrderedDict(); unbound = []; fonts = set()
    def collect(n, depth, parent, vlabel):
        if n['type'] == 'INSTANCE':
            deps[n.get('component')] += 1
            if n.get('component') == 'Icons': icons[(n.get('variant') or {}).get('Name')] += 1
        for kind in ('fills', 'strokes'):
            ps = n.get(kind)
            if ps and ps != 'mixed':
                for p in ps:
                    if p['type'] != 'SOLID': continue
                    all_hex[p['hex']] += 1
                    t = tok(p.get('variable'))
                    if t:
                        token_use[t].add(meta['name'])
                        colors.setdefault(t, {'hex': p['hex'], 'usedAs': set()})['usedAs'].add(f"{kind[:-1]} on {n['name']}")
                    elif n['type'] != 'TEXT':
                        unbound.append(f"`{vlabel}` → {n['name']} {kind[:-1]} {p['hex']}")
        for k, v2 in (n.get('vars') or {}).items():
            if isinstance(v2, str): token_use[tok(v2)].add(meta['name'])
        if n['type'] == 'TEXT':
            for st in n['styles']:
                fonts.add(st['font'])
                col = st.get('color') or []
                ct = tok(col[0].get('variable')) if col else None
                if ct: token_use[ct].add(meta['name']); colors.setdefault(ct, {'hex': col[0]['hex'], 'usedAs': set()})['usedAs'].add(f"text on {n['name']}")
                elif col: unbound.append(f"`{vlabel}` → {n['name']} text {col[0]['hex']}")
                k = (st['font'], st['weight'], st['size'], st['lineHeight'], st.get('case') or '—', ct or (col[0]['hex'] if col else '—'), n['align'])
                typo.setdefault(k, set()).add(n['name'])
                type_combos[f"{st['font']} {st['weight']} {fmt(st['size'])}px"] += 1
    for v in variants:
        walk(v, lambda n, dd, p, vl=v['_label']: collect(n, dd, p, vl))

    # known issues (automatic + curated)
    issues = list(meta['issues'])
    zero = [v['_label'] for v in variants if v['usage']['total'] == 0]
    doconly = [v['_label'] for v in variants if v['usage']['total'] > 0 and v['usage']['total'] == v['usage']['doc']]
    if unbound: issues.insert(0, '**Hard-coded colors not bound to a variable:** ' + '; '.join(unbound) + '.')
    if meta['bp']:
        hs = Counter(); off = []
        for v in variants:
            b = next(c for c in v['children'] if c['name'] == 'Button')
            hs[b['h']] += 1
            if b['h'] != 40: off.append(f"`{v['_label']}` {fmt(b['h'])}px")
        if off: issues.insert(0, '**`Button` height is not 40px** in: ' + ', '.join(off) + '.')
    if [f for f in fonts if f != 'Noto Sans' and f != 'Noto Serif']:
        issues.append('**Fonts outside the production pair:** ' + ', '.join(sorted(fonts - {'Noto Sans', 'Noto Serif'})) + '.')
    if nested: issues.append(f'**{nested} instances are nested inside other instances** (counted in the total, not per parent, in "Where it is used").')
    if zero: issues.append(f"**{len(zero)} of {len(variants)} variants have 0 instances** anywhere in the file: " + ', '.join(f'`{z}`' for z in zero) + '.')
    if doconly: issues.append(f"**{len(doconly)} variants are placed only in their own documentation frame** (not yet used in any real layout): " + ', '.join(f'`{z}`' for z in doconly) + '.')

    default = next((v for v in variants if v['variantProperties'].get('State') == 'Default'), variants[0])
    infocus = next((v for v in variants if v['variantProperties'].get('State') == 'InFocus'
                    and all(v['variantProperties'][k] == default['variantProperties'][k] for k in keys if k != 'State')), None)
    bps = s['properties'].get('Breakpoint', {}).get('options') if 'Breakpoint' in s['properties'] else None
    spec_text = '\n'.join(texts)

    # ---- markdown
    fm = OrderedDict([('name', meta['name']), ('kind', 'component'), ('order', meta['order']), ('figma_file', FILE_KEY),
                      ('figma_set_name', s['name']), ('figma_node', f'"{s["id"]}"'), ('component_key', s['key']),
                      ('variants', len(variants)), ('breakpoints', '[' + (', '.join(bps) if bps else 'all (single size)') + ']'),
                      ('built_from', '[' + ', '.join(sorted(deps)) + ']'), ('built_into', '[' + ', '.join(sorted(built_into)) + ']'),
                      ('spec_json', f'{slug}.json'), ('skeleton', f'{slug}.html'), ('exported', DATE)])
    md = ['---'] + [f'{k}: {v}' for k, v in fm.items()] + ['---', '', f"# {meta['name']}", '', f"> {meta['desc']}", '',
          '**Specification text from the Figma documentation frame** (verbatim, one text layer per line):', '', '```text', spec_text, '```', '',
          '## Figma references', '',
          f'- File: **{FILE_NAME}** (`{FILE_KEY}`), page **{PAGE}**',
          f"- Component set: [`{s['name']}` · {s['id']}]({url(s['id'])}) · key `{s['key']}`",
          f"- Documentation frame: [{doc['id']}]({url(doc['id'])}) · overview PNG: [previews/{docfn}](previews/{docfn})", '',
          '| Variant | Node | Key | Size | Preview |', '|---|---|---|---|---|']
    for v in variants:
        md.append(f"| `{v['_label']}` | [{v['id']}]({url(v['id'])}) | `{v['key'][:12]}…` | {fmt(v['w'])}×{fmt(v['h'])} | [png]({v['_preview']}) |")
    md += ['', '## Properties', '', '| Property | Type | Default | Options |', '|---|---|---|---|']
    for k in keys:
        p = s['properties'][k]; md.append(f"| {k} | {p['type']} | {p['default']} | {', '.join(p['options'])} |")
    md += ['', '## Where it is used', '', 'Scope: local instances in the MNG Design System file only. Instances in other files that use the published library (WordPress Elements, Reader Dashboard v2.0) are not counted.', '',
           f'Total instances: **{total}**.', '']
    if built_into: md += ['Nested inside (component sets / components): ' + ', '.join(f'{k} ×{c}' for k, c in built_into.most_common()) + '.', '']
    if pages: md += ['Placed directly on pages: ' + ', '.join(f'{k} ×{c}' for k, c in pages.most_common()) + '.', '']
    md += ['| Variant | Total | Doc frame | In components | Other placements |', '|---|---|---|---|---|']
    for v in variants:
        u = v['usage']
        ic = ', '.join(f'{k} ×{c}' for k, c in u['inComponents'].items()) or '—'
        ot = ', '.join(f"{k.replace('|', chr(92)+'|')} ×{c}" for k, c in u['other'].items()) or '—'
        md.append(f"| `{v['_label']}` | {u['total']} | {u['doc']} | {ic} | {ot} |")
    md += ['', '## Breakpoints', '', meta['bp'] or 'No Breakpoint property: one size at every viewport.', '',
           '## Responsive rules', ''] + [f'- {r}' for r in meta['rules']] + ['', '## Dependencies', '', '**Built from:**', '']
    if deps:
        for k, c in deps.most_common():
            md.append(f"- {k} ([{ICONS_SET}]({url(ICONS_SET)})) ×{c} — not in this export" if k == 'Icons' else f'- {k} ×{c}')
        if icons: md += ['', 'Icon variants used: ' + ', '.join(f'`{k}` ×{c}' for k, c in icons.most_common()) + '.']
    else: md.append('- nothing (no nested components).')
    md += ['', '**Built into:** ' + (', '.join(sorted(built_into)) if built_into else 'nothing yet (standalone).'), '',
           '## Anatomy', '', 'Every variant in the set has the same layer tree; InFocus only adds the `Focus Ring` frame. Hidden layers are marked.', '',
           f"Default variant `{default['_label']}`:", '', anatomy(default), '']
    if infocus:
        md += [f"InFocus variant `{infocus['_label']}`:", '', anatomy(infocus), '']
    md += ['Full layer trees for every variant are in the JSON twin (`variants[].layerTree`).', '',
           '## Size & layout', '', '| Variant | W×H | Sizing | Layout | Radius | Fill | Stroke |', '|---|---|---|---|---|---|---|']
    for v in variants:
        b = next((c for c in v.get('children', []) if c['name'] == 'Button'), v)
        tgt = b if meta['bp'] or meta['slug'] == 'action-button' else v
        md.append(f"| `{v['_label']}` | {fmt(tgt['w'])}×{fmt(tgt['h'])} | {sizing_str(tgt)} | {layout_str(tgt)}{', min-h '+fmt(tgt['minH']) if tgt.get('minH') else ''} | {radius_str(tgt)} | {paint_str(tgt.get('fills')) or '—'} | {paint_str(tgt.get('strokes')) or '—'} |")
    note = '*Values are for the `Button` frame (the visible button); the variant root adds the 8px side margin.*' if meta['bp'] else ('*Values are for the `Button` frame.*' if meta['slug'] == 'action-button' else '*Values are for the variant root.*')
    md += ['', note, '', '## Typography', '']
    if typo:
        md += ['| Font | Weight | Size | Line height | Case | Color | Align | Layers |', '|---|---|---|---|---|---|---|---|']
        for k, layers in typo.items():
            md.append(f"| {k[0]} | {k[1]} | {fmt(k[2])}px | {k[3]} | {k[4]} | {k[5]} | {k[6].lower()} | {', '.join(sorted(layers))} |")
    else: md.append('No text layers (icon-only).')
    md += ['', '## Color & effects', '', '| Token | Hex | Used as |', '|---|---|---|']
    for t, c in colors.items(): md.append(f"| {t} | {c['hex']} | {'; '.join(sorted(c['usedAs']))} |")
    md += ['', 'Hex values are the MNG Design System default mode. At runtime use the token (`var(--color-theme-primary)` etc.); theme colors change per site. No effects (shadows/blurs) are used.', '',
           '## Image ratios', '', 'N/A: no image fills or placeholders.', '', '## Ad slots', '', 'N/A.', '',
           '## Production references', '', 'None recorded in Figma (no domains, selectors or layout tokens in descriptions or layer names). Production gaps, if any, belong in `production-vs-design-differences.md`.', '',
           '## Known issues', '']
    md += [f'{i+1}. {x}' for i, x in enumerate(issues)] if issues else ['None open.']
    md += ['', '## Rendering steps', '',
           '1. Pick the variant from the Properties table (State comes from interaction: Default → Hover on pointer-over → Pressed on mouse/touch down → InFocus on keyboard focus).',
           f'2. Copy that variant\'s structure from `{slug}.html` (or build it from `variants[].layerTree` in the JSON).',
           '3. Use the tokens from `../../tokens.css`, never the hex, so the site theme applies.',
           '4. Replace icon placeholders with the named `Icons` variant (see Dependencies).' if deps else '4. No nested components to resolve.',
           '5. Draw the focus ring outside the element so it never changes layout (see Responsive rules).',
           '6. Check against the preview PNG in `previews/`.', '']
    open(os.path.join(d, f'{slug}.md'), 'w').write('\n'.join(md))

    # ---- json
    def vjson(v):
        b = v
        return OrderedDict([('label', v['_label']), ('variantProperties', v['variantProperties']), ('id', v['id']), ('key', v['key']), ('url', url(v['id'])),
                            ('width', v['w']), ('height', v['h']), ('layout', v.get('layout')), ('sizing', v.get('sizing')), ('fills', v.get('fills')),
                            ('strokes', v.get('strokes')), ('radius', v.get('radius')), ('preview', v['_preview']),
                            ('breakpoints', [v['variantProperties']['Breakpoint']] if 'Breakpoint' in v['variantProperties'] else ['all']),
                            ('usage', v['usage']), ('layerTree', {k: x for k, x in v.items() if not k.startswith('_') and k not in ('usage', 'key', 'variantProperties', 'description')})])
    j = OrderedDict([('schema', 'mng-design-system/component-spec@1'), ('exported', DATE), ('kind', 'component'), ('name', meta['name']), ('slug', slug), ('order', meta['order']),
                     ('figmaSetName', s['name']), ('description', meta['desc']), ('componentDescription', s['description']), ('specText', ' | '.join(texts)),
                     ('figma', OrderedDict([('fileKey', FILE_KEY), ('fileName', FILE_NAME), ('page', PAGE), ('mainId', s['id']), ('mainKey', s['key']), ('url', url(s['id'])),
                                            ('documentationFrame', doc['id']), ('documentationUrl', url(doc['id'])),
                                            ('variants', [{'label': v['_label'], 'id': v['id'], 'key': v['key'], 'url': url(v['id'])} for v in variants])])),
                     ('properties', {k: s['properties'][k] for k in keys}), ('breakpoints', bps or ['all']),
                     ('usage', OrderedDict([('totalInstances', total), ('builtInto', dict(built_into)), ('pages', dict(pages)), ('nestedInInstances', nested),
                                            ('scope', 'Local instances in the MNG Design System file only.')])),
                     ('dependencies', [{'component': k, 'nodeId': ICONS_SET if k == 'Icons' else None, 'inThisExport': False, 'count': c} for k, c in deps.items()]),
                     ('iconsUsed', dict(icons)), ('variants', [vjson(v) for v in variants]),
                     ('typography', [{'font': k[0], 'weight': k[1], 'size': k[2], 'lineHeight': k[3], 'case': k[4], 'color': k[5], 'align': k[6], 'layers': sorted(l)} for k, l in typo.items()]),
                     ('colors', [{'token': t, 'hex': c['hex'], 'usedAs': sorted(c['usedAs'])} for t, c in colors.items()]),
                     ('focusRing', {'layer': 'Focus Ring', 'stroke': '2px OUTSIDE', 'offset': '1px', 'color': 'color/theme/primary' if slug == 'non-button-hyperlink' else 'color/gray/black',
                                    'affectsLayout': slug == 'non-button-hyperlink'}),
                     ('imageRatios', []), ('adSlots', []), ('responsiveRules', meta['rules']), ('productionRefs', []), ('knownIssues', issues),
                     ('skeleton', f'{slug}.html'), ('paths', {'md': f'components/{nn}/{slug}.md', 'json': f'components/{nn}/{slug}.json', 'html': f'components/{nn}/{slug}.html', 'dir': f'components/{nn}/'})])
    if slug == 'non-button-hyperlink':
        j['focusRing'] = {'layer': 'variant root border', 'stroke': '2px CENTER, 4px corners', 'color': 'color/theme/primary', 'affectsLayout': True, 'note': 'Intentional, matches production.'}
    json.dump(j, open(os.path.join(d, f'{slug}.json'), 'w'), indent=1, ensure_ascii=False)

    # ---- html
    secs = []
    for v in variants:
        secs.append(f'''<section class="mng-variant" data-variant="{html.escape(v['_label'])}">
  <h2 class="mng-variant__label">{html.escape(v['_label'])} <small>{fmt(v['w'])}×{fmt(v['h'])} · <a href="{url(v['id'])}">Figma {v['id']}</a></small></h2>
  <div class="mng-variant__stage">
{node_html(v, slug)}
  </div>
</section>''')
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{meta['name']} — skeleton</title>
<!-- Generated {DATE} from Figma MNG Design System ({FILE_KEY}), set {s['id']} ("{s['name']}"). Structure + tokens only; see {slug}.md for rules. -->
<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif:wght@400;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../tokens.css">
<style>
  [hidden]{{display:none!important}}
  *{{box-sizing:border-box}}
  body{{font-family:'Noto Sans',sans-serif;margin:24px;background:#fff;color:#141414}}
  h1{{font-size:20px;margin:0 0 16px}}
  .mng-variant{{margin:0 0 20px}}
  .mng-variant__label{{font:600 12px/1.4 'Noto Sans',sans-serif;color:#666;margin:0 0 6px}}
  .mng-variant__label small{{font-weight:400}}
  .mng-variant__stage{{padding:8px;display:inline-block;background:repeating-conic-gradient(#fafafa 0 25%,#fff 0 50%) 0 0/16px 16px}}
  .mng-instance{{display:inline-flex;align-items:center;justify-content:center;font-size:12px;line-height:1;color:currentColor}}
</style></head>
<body>
<h1>{meta['name']} <small style="font-weight:400;color:#666">· {len(variants)} variants · Figma set “{s['name']}”</small></h1>
{chr(10).join(secs)}
</body></html>
'''
    open(os.path.join(d, f'{slug}.html'), 'w').write(page)

    index_items.append(OrderedDict([('order', meta['order']), ('kind', 'component'), ('name', meta['name']), ('figmaSetName', s['name']), ('slug', slug),
                                    ('variants', len(variants)), ('breakpoints', bps or ['all']), ('builtFrom', sorted(deps)), ('builtInto', sorted(built_into)),
                                    ('totalInstances', total), ('figmaNode', s['id']), ('figmaUrl', url(s['id'])), ('documentationFrame', doc['id']), ('issues', len(issues)),
                                    ('paths', {'md': f'components/{nn}/{slug}.md', 'json': f'components/{nn}/{slug}.json', 'html': f'components/{nn}/{slug}.html', 'dir': f'components/{nn}/'})]))
    meta['_built_into'] = built_into; meta['_total'] = total; meta['_setname'] = s['name']; meta['_nvar'] = len(variants); meta['_bps'] = bps; meta['_deps'] = deps; meta['_nn'] = nn

# ---------------------------------------------------------------- root files
VALUES = {'radius/sm': 4, 'radius/utility': 5, 'radius/lg': 8, 'spacing/050': 4, 'spacing/100': 8, 'spacing/150': 12, 'spacing/200': 16, 'spacing/250': 20, 'spacing/300': 24}
color_hex = {}
for it in specs['items']:
    def g(n, dd, p):
        for kind in ('fills', 'strokes'):
            for pp in (n.get(kind) or []) if n.get(kind) != 'mixed' else []:
                if pp.get('variable'): color_hex[tok(pp['variable'])] = pp['hex']
        if n['type'] == 'TEXT':
            for st in n['styles']:
                for pp in st.get('color') or []:
                    if pp.get('variable'): color_hex[tok(pp['variable'])] = pp['hex']
    for v in it['set']['variants']: walk(v, g)
tokens = OrderedDict([('schema', 'mng-design-system/tokens@1'), ('exported', DATE),
                      ('source', {'fileKey': FILE_KEY, 'fileName': FILE_NAME, 'mode': 'default mode (values shown are the MNG Design System defaults; theme tokens change per site)'}),
                      ('colors', OrderedDict((t, {'hex': color_hex[t], 'css': css_var(t), 'usedBy': sorted(token_use[t])}) for t in sorted(color_hex))),
                      ('dimensions', OrderedDict((t, {'px': VALUES[t], 'css': css_var(t), 'usedBy': sorted(token_use[t])}) for t in sorted(token_use) if t in VALUES)),
                      ('typeCombinations', dict(type_combos)),
                      ('breakpoints', {'Desktop': '≥640px', 'Mobile': '≤639px', 'note': 'Only the CTA families have a Breakpoint property.'})])
json.dump(tokens, open(os.path.join(OUT, 'tokens.json'), 'w'), indent=1, ensure_ascii=False)
css = [f'/* MNG buttons export {DATE}: tokens used by these components (default mode values). */', ':root {']
for t in sorted(color_hex): css.append(f'  {css_var(t)}: {color_hex[t]};  /* {t} */')
for t in sorted(tokens['dimensions']): css.append(f'  {css_var(t)}: {VALUES[t]}px;  /* {t} */')
css.append('}')
open(os.path.join(OUT, 'tokens.css'), 'w').write('\n'.join(css) + '\n')

index = OrderedDict([('schema', 'mng-design-system/index@1'), ('exported', DATE),
                     ('figma', {'fileKey': FILE_KEY, 'fileName': FILE_NAME, 'page': PAGE, 'pageUrl': url(PAGE_ID)}),
                     ('items', index_items), ('templates', []), ('tokens', {'json': 'tokens.json', 'css': 'tokens.css'})])
json.dump(index, open(os.path.join(OUT, 'index.json'), 'w'), indent=1, ensure_ascii=False)

nvar = sum(m['_nvar'] for m in META)
rows = '\n'.join(f"| {m['order']:02d} | [{m['name']}](components/{m['_nn']}/{m['slug']}.md) | {m['_setname']} | `{specs['items'][m['idx']]['set']['id']}` | {m['_nvar']} | {', '.join(m['_bps']) if m['_bps'] else 'single size'} | {m['_total']} | {', '.join(sorted(m['_deps'])) or '—'} | {', '.join(sorted(m['_built_into'])) or '—'} |" for m in META)
ctok = '\n'.join(f"`{t}` {color_hex[t]}" for t in sorted(color_hex))
readme = f'''# Buttons and links: MNG Design System export

**Exported {DATE}** from the **Buttons | 2026.09.30** page. It reflects Karl's 2026-10-02 review: 40px CTAs, focus rings drawn outside the element, the set renames and the layer-name cleanup. It replaces the 2026-10-01 export.

This is a portable, AI-readable spec export from the **MNG Design System** Figma file (`{FILE_KEY}`), page [Buttons | 2026.09.30]({url(PAGE_ID)}). It holds 8 component sets with {nvar} variants in total. Design (Figma) is the source of truth. Values here are design values, not production values.

## How an agent should use this folder

1. Read `index.json` first. It lists the 8 components in order, with paths to every file.
2. For context (description, the verbatim Figma spec text, where it's used, known issues), read the component's `.md`.
3. For exact data (hex and token per layer, sizes, per-variant layer trees, usage counts), read the `.json` twin (`schema: mng-design-system/component-spec@1`).
4. To see the structure rendered, open the `.html` skeleton. It has one `<section>` per variant and uses `tokens.css`. Compare it with the PNGs in `previews/`: one per variant at 2×, plus `<slug>--documentation.png`, the whole Figma documentation frame at 0.5×.
5. Always use the **tokens** (`var(--color-theme-primary)`, `var(--radius-sm)` and so on), never the hex. Theme colors change per site.

## Components (build order)

| # | Component | Figma set name | Node | Variants | Breakpoints | Instances in file | Built from | Built into |
|---|---|---|---|---|---|---|---|---|
{rows}

The component name is the documentation-frame title; the Figma set name is what you search for in the Assets panel. Note the 2026-10-02 swap: the documented utility button is the set **`Button Action`**, and the older library set on the same page (`5417:3876`, used by Reader Dashboard files) is **`Action Button`**. That older set is not in this export.

All 8 are leaf components: none is built from another one in this export. The only dependency is the shared **Icons** set (`{ICONS_SET}`), which isn't in this export. Instance counts cover this file only; library instances in WordPress Elements and Reader Dashboard v2.0 aren't counted.

```mermaid
flowchart LR
  Icons(["Icons {ICONS_SET} (not exported)"])
  P[Button Primary] & S[Button Secondary] & T[Button Tertiary] & AB[Action Button] & MC[Pop-Up Modal Close] & IC[In-Line Close] --> Icons
  LS[Button Linkstyle]
  HL[Non-Button Hyperlink]
  P --> ILM[[InLineMessage]] & MOD[[ModalsCenter / Modals]]
  T --> ILM
  LS --> MOD & ILM & FF[[Form Field]]
  MC --> MOD
  IC --> ILM & MO[[ModalsOffset]]
  HL --> ILM
```

## Layer structure

Every variant in a set has the same layer tree, so text and icon overrides carry across variant swaps. InFocus adds only a `Focus Ring` frame.

| Family | Layers |
|---|---|
| Primary, Secondary, Tertiary | variant root (8px side margin) › `Button` › `Content` › `Icon Left` / `Label` / `Icon Right` |
| Action Button (`Button Action`) | `Button` › `Content` › `Icon Left` / `Label` / `Icon Right` (hidden) |
| Button Linkstyle | `Label` |
| Pop-Up Modal Close | `Icon` |
| In-Line Close | `Button` › `Box` › `Icon` |
| Non-Button Hyperlink | `Label` (InFocus: `Underline` › `Label`) |

## States (shared by all families)

- **Default:** resting appearance.
- **Hover:** pointer over the button. The fill or border changes to the family's hover token.
- **Pressed:** mouse down or tap. It's currently the same as Hover everywhere, because no pressed token exists yet.
- **InFocus:** keyboard focus. The Default look plus a 2px `color/gray/black` focus ring, 1px outside the element. The ring never changes the component's size or moves anything (a 40px button reads as 46px with the ring). The exception is Non-Button Hyperlink: its teal 2px focus box is part of the layout, which matches production and is intentional.

## Breakpoints

Only the three CTA families (Primary, Secondary, Tertiary) have a `Breakpoint` property:

| Value | Viewport (export convention) | Behavior |
|---|---|---|
| Desktop | ≥640px (768, 1024, 1100 and 1280 templates) | The button hugs its label and icon. Gap in a row or stack is 16px. |
| Mobile | ≤639px (340 XS-Fold and 360 SM-Mobile templates) | The button fills the container with an 8px side margin. Stacked gap is 8px. |

The other five families are a single size at every viewport.

## Sizes

- **CTAs:** 40px tall in every state: 8px top/bottom padding (`spacing/100`), 16px left/right (`spacing/200`), 40px min-height so a wrapped label can grow. 16px icons. 4px corners (`radius/sm`).
- **Action Button:** 95×32 (compact by design), 16px icon. **Linkstyle:** 38px for one line (compact by design). **Modal Close:** 32×32 circle, 12px icon. **In-Line Close:** 40×40 hit area, 28px box, 12px icon.

## Tokens summary

Colors (default mode, see `tokens.json` and `tokens.css`): {ctok.replace(chr(10), ', ')}. Every color in the 8 sets is bound to a variable. Radius and spacing are bound to `radius/sm` (4px), `spacing/100` (8px) and `spacing/200` (16px).

Type: Noto Sans only. CTA buttons use Bold 16px Title Case. Action Button uses Bold 12px. Linkstyle uses Regular 16px. Hyperlink uses Regular 16.5px (matches production).

## Known issues

Each component's `.md` lists its own under **Known issues**. The open ones across the page:

- **Margin not specified** for Action Button, Linkstyle, Modal Close and In-Line Close (open spec gap in Figma).
- **Low adoption:** most Hover, Pressed, InFocus, Mobile and icon variants appear only in their documentation frame, or nowhere. The stacked Linkstyle variants and the Action Button aren't used anywhere yet.

## Folder layout

```
mng-buttons-export/
  README.md  index.json  tokens.json  tokens.css
  components/
''' + '\n'.join(f"    {m['_nn']}/{' ' * (24 - len(m['_nn']))}{m['slug']}.md  .json  .html  previews/ ({m['_nvar']} variants + documentation)" for m in META) + '''
```

Not included: the Icons set, the older `Action Button` / `Button ActionMenu` / `Button Pay` / social and save button sets on the same page, and page templates.
'''
open(os.path.join(OUT, 'README.md'), 'w').write(readme)
print('built', OUT, nvar, 'variants')
