// Figma plugin code for the Buttons export (run with figma_execute in the
// MNG Design System file, jFHYqhZbJjvWQmDI4myCsd). Each call's result is too
// big to return inline, so the tool saves it to disk; copy each saved file to
// <raw_dir>/ under the name given below, then run build-buttons-export.py.
// Last used 2026-10-02.

// [set node, documentation frame] in build order (must match META in build-buttons-export.py)
const SETS = [
  ['5328:15928', '7012:33138'], // Button Primary
  ['5333:16013', '7015:36207'], // Button Secondary
  ['5333:16089', '7018:36565'], // Button Tertiary
  ['7075:6357',  '7075:6715'],  // Button Action (doc: "Action Button")
  ['5428:3953',  '7075:7436'],  // Button Linkstyle
  ['5335:16196', '7078:7807'],  // Button Modal Close (doc: "Pop-Up Modal Close")
  ['5335:16200', '7078:7975'],  // Button In-Line Close (doc: "In-Line Close")
  ['6282:5568',  '7078:8121'],  // Hyperlink (doc: "Non-Button Hyperlink")
];

// ---------------------------------------------------------------- 1. specs.json
// Run once per RANGE ([0,1] then [1,8] keeps each result under the timeout),
// then merge the "results" arrays into {"fileKey","page","items":[...]}.
// timeout: 30000
const RANGE = [0, 8];
const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, '0')).join('').toUpperCase();
const varCache = {};
async function vname(id) { if (!(id in varCache)) { const v = await figma.variables.getVariableByIdAsync(id); let col = ''; if (v) { const c = await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId); col = c ? c.name : ''; } varCache[id] = v ? (col + '/' + v.name) : id; } return varCache[id]; }
async function paints(ps) { if (!ps || ps === figma.mixed) return ps === figma.mixed ? 'mixed' : undefined; const out = []; for (const p of ps) { if (p.visible === false) continue; const o = { type: p.type }; if (p.type === 'SOLID') { o.hex = hex(p.color); if (p.opacity !== 1) o.opacity = +p.opacity.toFixed(2); if (p.boundVariables && p.boundVariables.color) o.variable = await vname(p.boundVariables.color.id); } out.push(o); } return out.length ? out : undefined; }
async function bv(n) { if (!n.boundVariables) return undefined; const o = {}; for (const [k, v] of Object.entries(n.boundVariables)) { if (k === 'fills' || k === 'strokes') continue; if (Array.isArray(v)) { o[k] = []; for (const x of v) o[k].push(await vname(x.id)); } else if (v && v.id) o[k] = await vname(v.id); } return Object.keys(o).length ? o : undefined; }
async function ser(n, depth) {
  const o = { name: n.name, type: n.type, id: n.id, w: +n.width.toFixed(1), h: +n.height.toFixed(1) };
  if (n.parent && n.parent.type !== 'PAGE' && n.parent.type !== 'COMPONENT_SET') { o.x = +n.x.toFixed(1); o.y = +n.y.toFixed(1); }
  if (n.visible === false) o.hidden = true;
  if ('layoutSizingHorizontal' in n) { try { o.sizing = { h: n.layoutSizingHorizontal, v: n.layoutSizingVertical }; } catch (e) {} }
  if (n.layoutPositioning === 'ABSOLUTE') { o.absolute = true; o.constraints = n.constraints; }
  if (n.minWidth) o.minW = n.minWidth; if (n.minHeight) o.minH = n.minHeight; if (n.maxWidth) o.maxW = n.maxWidth;
  if ('layoutMode' in n && n.layoutMode && n.layoutMode !== 'NONE') o.layout = { dir: n.layoutMode, gap: n.itemSpacing, pad: [n.paddingTop, n.paddingRight, n.paddingBottom, n.paddingLeft], main: n.primaryAxisAlignItems, cross: n.counterAxisAlignItems };
  if ('clipsContent' in n && n.clipsContent) o.clip = true;
  if ('cornerRadius' in n) { if (n.cornerRadius === figma.mixed) o.radius = [n.topLeftRadius, n.topRightRadius, n.bottomRightRadius, n.bottomLeftRadius]; else if (n.cornerRadius) o.radius = n.cornerRadius; }
  if ('opacity' in n && n.opacity < 1) o.opacity = +n.opacity.toFixed(2);
  if ('fills' in n && n.type !== 'TEXT') { const f = await paints(n.fills); if (f) o.fills = f; }
  if ('strokes' in n && n.strokes && n.strokes.length) { const s = await paints(n.strokes); if (s) { o.strokes = s; o.strokeWeight = n.strokeWeight === figma.mixed ? [n.strokeTopWeight, n.strokeRightWeight, n.strokeBottomWeight, n.strokeLeftWeight] : n.strokeWeight; o.strokeAlign = n.strokeAlign; if (n.dashPattern && n.dashPattern.length) o.dash = n.dashPattern; } }
  if ('effects' in n && n.effects.length) o.effects = n.effects.filter(e => e.visible !== false).map(e => ({ type: e.type, radius: e.radius }));
  const b = await bv(n); if (b) o.vars = b;
  if (n.type === 'TEXT') {
    o.text = n.characters; o.autoResize = n.textAutoResize; o.align = n.textAlignHorizontal;
    const segs = n.getStyledTextSegments(['fontName', 'fontSize', 'lineHeight', 'letterSpacing', 'textCase', 'textDecoration', 'fills']);
    o.styles = []; for (const s of segs.slice(0, 4)) o.styles.push({ font: s.fontName.family, weight: s.fontName.style, size: s.fontSize, lineHeight: s.lineHeight.unit === 'AUTO' ? 'auto' : (s.lineHeight.unit === 'PIXELS' ? s.lineHeight.value + 'px' : s.lineHeight.value + '%'), case: s.textCase !== 'ORIGINAL' ? s.textCase : undefined, decoration: s.textDecoration !== 'NONE' ? s.textDecoration : undefined, color: (await paints(s.fills)) });
  }
  if (n.type === 'INSTANCE') { const m = await n.getMainComponentAsync(); if (m) { const isV = m.parent && m.parent.type === 'COMPONENT_SET'; o.component = isV ? m.parent.name : m.name; o.componentSetId = isV ? m.parent.id : m.id; if (isV) o.variant = m.variantProperties; o.mainId = m.id; } return o; }
  if ('children' in n && depth < 12) { o.children = []; for (const c of n.children) o.children.push(await ser(c, depth + 1)); }
  return o;
}
const results = [];
for (let IDX = RANGE[0]; IDX < RANGE[1]; IDX++) {
  const [sid, did] = SETS[IDX]; const s = await figma.getNodeByIdAsync(sid); const doc = await figma.getNodeByIdAsync(did);
  const set = { id: s.id, key: s.key, name: s.name, description: s.description || null, properties: Object.fromEntries(Object.entries(s.componentPropertyDefinitions).map(([k, v]) => [k, { type: v.type, default: v.defaultValue, options: v.variantOptions }])), variants: [] };
  for (const v of s.children) {
    const t = await ser(v, 0); t.key = v.key; t.variantProperties = v.variantProperties; t.description = v.description || null;
    const ins = await v.getInstancesAsync(); const u = { total: 0, doc: 0, nested: 0, inComponents: {}, other: {} };
    for (const i of ins) {
      u.total++; if (i.parent && i.parent.type === 'INSTANCE') { u.nested++; continue; }
      let p = i, page = null, top = null, inComp = null, inDoc = false;
      while (p && p.type !== 'DOCUMENT') { if (p.id === did) inDoc = true; if (p.type === 'PAGE') page = p.name; if (p.parent && p.parent.type === 'PAGE') top = p.name; if (!inComp && p !== i && p.type === 'COMPONENT') inComp = (p.parent && p.parent.type === 'COMPONENT_SET') ? p.parent.name : p.name; p = p.parent; }
      if (inDoc) u.doc++; else if (inComp) u.inComponents[inComp] = (u.inComponents[inComp] || 0) + 1; else { const k = page + ' ▸ ' + top; u.other[k] = (u.other[k] || 0) + 1; }
    }
    t.usage = u; set.variants.push(t);
  }
  const texts = doc.findAll(n => n.type === 'TEXT' && n.visible).filter(n => { let p = n.parent; while (p && p !== doc) { if (p.type === 'INSTANCE' || p.type === 'COMPONENT_SET') return false; p = p.parent; } return true; }).map(n => n.characters);
  results.push({ SPEC_MARK: IDX, set, doc: { id: doc.id, name: doc.name, w: doc.width, h: doc.height }, texts });
}
return { MULTI: true, results, fileKey: figma.fileKey, page: { name: 'Buttons | 2026.09.30', id: '1079:34282' } };

// ---------------------------------------------------------------- 2. previews.json (separate call)
// const out = {}; for (const [sid] of SETS) { const s = await figma.getNodeByIdAsync(sid);
//   for (const v of s.children) out[v.id] = figma.base64Encode(await v.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: 2 } })); }
// return { PREVIEWS: true, out };

// ---------------------------------------------------------------- 3. docs.json (separate call)
// const out = {}; for (const [, did] of SETS) { const n = await figma.getNodeByIdAsync(did);
//   out[did] = figma.base64Encode(await n.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: 0.5 } })); }
// return { DOCS: true, out };
