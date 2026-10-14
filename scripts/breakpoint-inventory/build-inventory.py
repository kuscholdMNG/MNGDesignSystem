#!/usr/bin/env python3
"""MNG Web Design System: build tokens/breakpoint-inventory.json (EXPORT-STANDARD.md section 6).

Inputs
  scripts/breakpoint-inventory/scans/<domain>.json   live CSS scans of the 6 review sites (scan.js), 2026-10-14.
                                                      ocregister.com is the full list; the other files list only
                                                      the differences from it ("b" = extra, "absent" = missing).
  CLASSIFY below                                      who owns each value and what it should snap to (hand-checked).
  REPO_SOURCES below                                  breakpoints found in the website repo copy (2026-05-08), from
                                                      status open item 11 and production-vs-design entries 30 and 31.
Output
  tokens/breakpoint-inventory.json

Tiers (EXPORT-STANDARD.md section 6): official (MNG Device or WordPress grid), component (an intended one-off,
goes in that component's tokens), drift (logged in production-vs-design-differences.md with what to snap to),
plus third-party and wordpress-admin (not ours, listed for completeness, no action).

Run from the repo top: python3 scripts/breakpoint-inventory/build-inventory.py      Stdlib only.
"""
import glob, json, os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SCANS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scans')
BASE = 'ocregister.com'

DEVICE = {'fold': 340, 'mobile': 360, 'tablet': 768, 'tablet-landscape': 1024, 'desktop': 1280}
GRID = {'xs': 320, 's': 640, 'm': 800, 'l': 1040, 'xl': 1280}

def bp(set_name, key, kind):
    """Human form of a boundary, e.g. 'WordPress grid s: min-width 640 / max-width 639'."""
    v = (DEVICE if set_name == 'device' else GRID)[key]
    label = ('MNG Device ' if set_name == 'device' else 'WordPress grid ') + key
    return {'set': set_name, 'token': ('breakpoint.%s' % key) if set_name == 'device' else ('breakpoint.wordpress-grid.%s' % key),
            'query': '(min-width: %dpx)' % v if kind == 'min' else '(max-width: %dpx)' % (v - 1), 'label': label}

THEME = 'WordPress theme (boldcoastal / measuredvibrant / modernearthy CSS)'
DIGI = 'mng-digisubs (MNG subscriptions: account menu, regwall, sign-in)'
DIGI_APP = 'plugins.mngdigisubs.com (MNG digisubs app, Bootstrap 5 default grid)'
TRUST = 'dfm-trust-indicators plugin (MNG)'
ADS = 'WordPress theme ad rules (dfp-ad, mobile adhesion)'
MG2 = 'Mg2 Connext paywall (third party, engage.<site>)'
OSANO = 'Osano cookie consent (third party, inline)'
KARGO = 'Kargo ads (third party, inline)'
HTL = 'HTL ad bidder (third party, htlbid.com)'
WPADMIN = 'WordPress admin bar (logged-in editors only)'

# key: (owners, tier, snap_to or None, note)
G, D = 'wordpress-grid', 'device'
CLASSIFY = {
    '>0': ([HTL], 'third-party', None, ''),
    '>300': ([ADS], 'drift', bp('grid', 'xs', 'min'), 'Top leaderboard ad sizing (.dfp-ad.dfp-top_leaderboard).'),
    '>320': ([THEME], 'official', bp('grid', 'xs', 'min'), ''),
    '<320': ([KARGO], 'third-party', None, ''),
    '<335': ([THEME], 'drift', bp('device', 'fold', 'max'), 'Nav search icon on very small phones. Below the WordPress grid; the nearest official boundary is MNG Device fold (340).'),
    '<340': ([DIGI, DIGI_APP], 'drift', bp('device', 'fold', 'max'), 'Off by one: (max-width: 340px) overlaps fold; should be 339.'),
    '<344': ([DIGI], 'drift', bp('device', 'fold', 'max'), 'Digisubs modal on very small phones.'),
    '<350': ([THEME], 'drift', bp('device', 'fold', 'max'), 'Nav hamburger icon on very small phones.'),
    '<360': ([DIGI_APP], 'drift', bp('device', 'mobile', 'max'), 'Off by one: (max-width: 360px) overlaps mobile; should be 359.'),
    '>360': ([DIGI], 'official', bp('device', 'mobile', 'min'), 'Regwall button.'),
    '>376': ([OSANO], 'third-party', None, ''),
    '<380': ([DIGI], 'drift', bp('device', 'mobile', 'max'), 'Spoof banner.'),
    '<400': ([DIGI_APP], 'drift', bp('device', 'mobile', 'max'), 'Sign-in modal.'),
    '<405': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar scores widget (#content.sports-radar-content).'),
    '<420': ([MG2], 'third-party', None, ''),
    '<430': ([DIGI], 'drift', bp('device', 'mobile', 'max'), 'Digisubs push prompt.'),
    '>431': ([DIGI], 'drift', bp('device', 'mobile', 'min'), 'Article share box.'),
    '<432': ([MG2], 'third-party', None, ''),
    '<450': ([DIGI, THEME], 'drift', bp('grid', 's', 'max'), 'Employee debugger and digisubs rules.'),
    '>450': ([DIGI], 'drift', bp('device', 'mobile', 'min'), 'Employee debugger.'),
    '<467': ([MG2], 'third-party', None, ''),
    '<480': ([ADS], 'drift', bp('grid', 's', 'max'), 'Mobile adhesion ad (#mobile-adhesion).'),
    '<500': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar widget.'),
    '<535': ([THEME], 'drift', bp('grid', 's', 'max'), 'Sports Radar widget.'),
    '<550': ([DIGI], 'drift', bp('device', 'mobile', 'max'), 'Regwall (:root:not(:has(#server-regwall))).'),
    '<575.98': ([DIGI_APP], 'drift', bp('device', 'tablet', 'max'), 'Bootstrap sm-down.'),
    '<576': ([DIGI, MG2], 'drift', bp('device', 'tablet', 'max'), 'Digisubs content (.sspw-content); Mg2 also uses it.'),
    '>576': ([DIGI_APP], 'drift', bp('device', 'tablet', 'min'), 'Bootstrap sm container.'),
    '<600': ([DIGI, THEME, MG2], 'drift', bp('grid', 's', 'max'), 'Article sharing and theme rules.'),
    '>600': ([WPADMIN], 'wordpress-admin', None, 'body.admin-bar.'),
    '<624': ([THEME], 'drift', bp('grid', 's', 'max'), 'Obituaries 1-column layout (entry 31).'),
    '>625': ([THEME], 'drift', bp('grid', 's', 'min'), 'Obituaries 2-column start (entry 31).'),
    '<639': ([THEME], 'official', bp('grid', 's', 'max'), ''),
    '>640': ([THEME], 'official', bp('grid', 's', 'min'), ''),
    '<700': ([THEME], 'drift', bp('grid', 's', 'max'), 'Promotion widget.'),
    '<720': ([MG2], 'third-party', None, ''),
    '<730': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Special investigative header.'),
    '<734': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Photo gallery widget (.gallery-container, entry 31).'),
    '>735': ([THEME], 'drift', bp('grid', 'm', 'min'), 'Photo gallery widget (entry 31).'),
    '<750': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Header banners (.header-banners).'),
    '>750': ([ADS], 'drift', bp('grid', 'm', 'min'), 'Top leaderboard ad.'),
    '<767': ([MG2], 'third-party', None, ''),
    '<767.98': ([DIGI_APP], 'official', bp('device', 'tablet', 'max'), 'Bootstrap md-down: the same boundary as MNG Device tablet (below 768).'),
    '<768': ([MG2], 'third-party', None, ''),
    '>768': ([DIGI, DIGI_APP, MG2, OSANO], 'official', bp('device', 'tablet', 'min'), 'Digisubs rules match MNG Device tablet; Mg2 and Osano also use 768.'),
    '<770': ([DIGI], 'drift', bp('device', 'tablet', 'max'), 'Account dropdown menu.'),
    '<783': ([WPADMIN], 'wordpress-admin', None, ''),
    '>783': ([WPADMIN], 'wordpress-admin', None, ''),
    '<799': ([THEME], 'official', bp('grid', 'm', 'max'), ''),
    '<800': ([THEME, MG2], 'drift', bp('grid', 'm', 'max'), 'Off by one: (max-width: 800px) overlaps m; should be 799 (#featured-flex-landing-three).'),
    '>800': ([THEME], 'official', bp('grid', 'm', 'min'), ''),
    '<820': ([DIGI], 'drift', bp('device', 'tablet', 'max'), 'Account dropdown menu.'),
    '<900': ([THEME], 'drift', bp('grid', 'm', 'max'), 'Promotion widget.'),
    '<930': ([THEME], 'drift', bp('grid', 'l', 'max'), 'Footer cookie notice button.'),
    '<960': ([THEME], 'drift', bp('grid', 'l', 'max'), 'Sports Radar widget.'),
    '<971': ([MG2], 'third-party', None, ''),
    '>972': ([MG2], 'third-party', None, ''),
    '<979': ([MG2], 'third-party', None, ''),
    '<991': ([MG2], 'third-party', None, ''),
    '<991.98': ([DIGI_APP], 'drift', bp('device', 'tablet-landscape', 'max'), 'Bootstrap lg-down.'),
    '<992': ([MG2], 'third-party', None, ''),
    '>992': ([DIGI_APP, MG2], 'drift', bp('device', 'tablet-landscape', 'min'), 'Bootstrap lg container; Mg2 also uses 992.'),
    '<1000': ([ADS], 'drift', bp('grid', 'l', 'max'), 'Mobile adhesion ad (entry 31 notes the 1000px ad rule).'),
    '>1000': ([ADS], 'drift', bp('grid', 'l', 'min'), 'Top and bottom leaderboard ad placement.'),
    '<1024': ([DIGI, THEME, MG2], 'drift', bp('device', 'tablet-landscape', 'max'), 'Off by one for the Device set (should be 1023); the theme rule (#dfm-digisubs-menu) should use grid l (1039).'),
    '>1024': ([DIGI], 'official', bp('device', 'tablet-landscape', 'min'), 'Digisubs card line.'),
    '<1025': ([ADS], 'drift', bp('grid', 'l', 'max'), 'Mobile adhesion ad.'),
    '<1039': ([THEME, DIGI, TRUST], 'official', bp('grid', 'l', 'max'), 'The masthead switches to desktop here.'),
    '<1040': ([TRUST, THEME], 'drift', bp('grid', 'l', 'max'), 'Off by one: (max-width: 1040px) overlaps l; should be 1039 (trust-indicator footer links).'),
    '>1040': ([THEME], 'official', bp('grid', 'l', 'min'), ''),
    '<1064': ([MG2], 'third-party', None, ''),
    '<1150': ([THEME], 'drift', bp('grid', 'l', 'max'), 'Special investigative header.'),
    '<1199': ([MG2], 'third-party', None, ''),
    '<1199.98': ([DIGI_APP], 'drift', bp('device', 'desktop', 'max'), 'Bootstrap xl-down.'),
    '<1200': ([OSANO, MG2], 'third-party', None, ''),
    '>1200': ([DIGI_APP, MG2], 'drift', bp('device', 'desktop', 'min'), 'Bootstrap xl container; Mg2 also uses 1200.'),
    '<1279': ([THEME], 'official', bp('grid', 'xl', 'max'), ''),
    '<1280': ([THEME], 'drift', bp('grid', 'xl', 'max'), 'Off by one: (max-width: 1280px) overlaps xl; should be 1279 (.custom-dfm-section.dark-layout).'),
    '>1280': ([THEME, DIGI], 'official', bp('grid', 'xl', 'min'), 'Also MNG Device desktop (1280).'),
    '>1281': ([MG2], 'third-party', None, ''),
    '<1299': ([THEME], 'drift', bp('grid', 'xl', 'max'), 'Obituaries listing (entry 31).'),
    '>1300': ([THEME], 'drift', bp('grid', 'xl', 'min'), 'Obituaries "stop scaling" (entry 31).'),
    '<1399.98': ([DIGI_APP], 'drift', bp('device', 'desktop', 'max'), 'Bootstrap xxl-down: no official breakpoint above 1280.'),
    '>1400': ([DIGI_APP], 'drift', bp('device', 'desktop', 'min'), 'Bootstrap xxl container: no official breakpoint above 1280.'),
    '<599': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
    '<782': ([WPADMIN], 'wordpress-admin', None, 'Admin bar (only when an editor is logged in).'),
    '>782': ([WPADMIN], 'wordpress-admin', None, ''),
    '>900': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
    '>960': ([WPADMIN], 'wordpress-admin', None, 'Admin bar notes.'),
}

REPO_SOURCES = [
    {'source': 'assets/client/scss/common-base/layout/_grid-variables.scss (WordPress themes)',
     'values': [320, 640, 800, 1040, 1280], 'tier': 'official', 'set': 'wordpress-grid',
     'note': 'The WordPress grid ($columns-map, ai-breakpoint() mixin, written in em). The masthead switches at l (1040).'},
    {'source': 'plugins/mng-digital-subscriber-widgets/reader-dashboard-src (Reader Dashboard, Tailwind v4)',
     'values': [640, 768, 1024, 1280, 1536], 'tier': 'drift', 'set': 'device',
     'note': 'Tailwind defaults sm/md/lg/xl/2xl; the layout switches at 1024 and 1280. 640 and 1536 are not Device values. Production-vs-design entry 30 (questions for DigiScrum).'},
    {'source': 'Reader Dashboard built CSS', 'values': [361, 413], 'tier': 'drift', 'set': 'device',
     'note': 'Source not traced yet; close to Device mobile (360). Entry 30.'},
    {'source': 'assets/client/scss/layouts/scng/components/features/_obits.scss (Obituaries)',
     'values': [624, 625, 734, 735, 1000, 1299, 1300], 'tier': 'drift', 'set': 'wordpress-grid',
     'note': 'Obituaries off-grid values; also seen live. Entry 31 (CMS team).'},
    {'source': 'Spotlight template (WordPress themes)', 'values': [624, 734, 735, 1299, 1300], 'tier': 'drift',
     'set': 'wordpress-grid', 'note': 'Same off-grid values as Obituaries (shared gallery and listing rules).'},
]

def load_scans():
    scans = {}
    for p in sorted(glob.glob(os.path.join(SCANS, '*.json'))):
        with open(p, encoding='utf-8') as f:
            d = json.load(f)
        scans[d['site']] = d
    return scans

def main():
    scans = load_scans()
    base = scans[BASE]
    base_keys = {e[0]: e for e in base['b']}
    values = {}
    for site, d in scans.items():
        if site == BASE:
            keys = set(base_keys)
            extra = {}
        else:
            keys = set(base_keys) - set(d.get('absent', []))
            extra = {e[0]: e for e in d['b']}
            keys |= set(extra)
        for k in keys:
            e = base_keys.get(k) or extra[k]
            v = values.setdefault(k, {'uses': e[1], 'sheets': list(e[2]), 'sample': e[3], 'sites': []})
            v['sites'].append(site)
            for s in e[2]:
                if s not in v['sheets']:
                    v['sheets'].append(s)
    missing = sorted(set(values) - set(CLASSIFY))
    if missing:
        raise SystemExit('classify these first: %s' % missing)
    rows = []
    for k, v in values.items():
        owners, tier, snap, note = CLASSIFY[k]
        kind = 'min' if k[0] == '>' else 'max'
        px = float(k[1:])
        px = int(px) if px == int(px) else px
        row = {'query': '(%s-width: %spx)' % (kind, px), 'kind': kind, 'px': px, 'tier': tier, 'owners': owners,
               'sites': sorted(v['sites']), 'rules': v['uses'], 'stylesheets': v['sheets'], 'sampleSelector': v['sample']}
        if snap:
            row['official' if tier == 'official' else 'snapTo'] = snap
        if note:
            row['note'] = note
        rows.append(row)
    rows.sort(key=lambda r: (r['px'], r['kind']))
    counts = {}
    for r in rows:
        counts[r['tier']] = counts.get(r['tier'], 0) + 1
    out = {
        '$description': 'Every width breakpoint found in production, classified as official, component, drift, third-party '
                        'or wordpress-admin (EXPORT-STANDARD.md section 6). Built by scripts/breakpoint-inventory/'
                        'build-inventory.py; never edit by hand. Drift is logged in production-vs-design-differences.md '
                        '(entries 30, 31, 33) with the official breakpoint to snap to.',
        'scanned': '2026-10-14',
        'method': 'Live CSS scan (scan.js) of every loaded stylesheet, @media width conditions only, on the homepage, an '
                  'article and the obituaries page of each review site, at a 1728px-wide window (media rules are read '
                  'from the CSS, so the window width does not matter). Cross-origin sheets were fetched; the HTL ad '
                  'bidder sheet was blocked on most sites. em/rem converted at 16px. JavaScript breakpoints '
                  '(matchMedia, window.innerWidth) are not included.',
        'officialSets': {
            'device': {'tokens': 'tokens/core/breakpoint.tokens.json', 'minWidths': DEVICE},
            'wordpress-grid': {'tokens': 'tokens/wordpress/breakpoint.tokens.json', 'minWidths': GRID},
        },
        'sites': {s: {'pages': d['pages'], 'blockedStylesheets': d.get('blocked', [])} for s, d in scans.items()},
        'summary': counts,
        'production': rows,
        'websiteRepo': {'copy': '~/Documents/digital-first-media-master-built COPY 20260508 (read-only, 2026-05-08)',
                        'found': REPO_SOURCES},
    }
    p = os.path.join(ROOT, 'tokens', 'breakpoint-inventory.json')
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print('breakpoint inventory: %d values %s' % (len(rows), counts))

if __name__ == '__main__':
    main()
