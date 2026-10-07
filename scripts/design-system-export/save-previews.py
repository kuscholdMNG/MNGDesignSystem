#!/usr/bin/env python3
"""Decode a saved preview-export result into <previews>/<section-slug>/<variant>.png.
Usage: python3 save-previews.py <saved-result.txt> <raw_dir> <previews_dir>"""
import json, base64, os, re, sys, glob
res, RAW, PREV = sys.argv[1:4]
def slug(s):
    s = s.lower().replace('&', 'and').replace('+', '')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')
idmap = {}
for f in glob.glob(os.path.join(RAW, 'specs_*.json')):
    for s in json.load(open(f))['result']['sections']:
        sl = slug(s['section']); seen = {}
        for m in s['mains']:
            vs = m['variants'] if m['type'] == 'COMPONENT_SET' else [m['tree']]
            for v in vs:
                if m['type'] == 'COMPONENT_SET': base = sl + '--' + '-'.join(slug(str(x)) for x in v['variantProperties'].values())
                else: base = sl if len(s['mains']) == 1 else sl + '--' + slug(m['name'])
                n = seen.get(base, 0) + 1; seen[base] = n
                idmap[v['id']] = (sl, base + ('' if n == 1 else f'-{n}') + '.png')
d = json.load(open(res))['result']
for nid, b in d['out'].items():
    sl, fn = idmap[nid]; os.makedirs(os.path.join(PREV, sl), exist_ok=True)
    open(os.path.join(PREV, sl, fn), 'wb').write(base64.b64decode(b))
print(len(d['out']), 'saved; errors:', d['err'])
