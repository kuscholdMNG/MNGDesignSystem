// MNG Web Design System: shared component exporter, Figma side (EXPORT-STANDARD.md section 7).
// Run with figma_execute (Desktop Bridge plugin) in the file that owns the components (fileKey from
// registry.json). Paste the registry entries to export into SETS as [setNodeId, docFrameNodeId or null].
// Big results are saved to disk by the tool; copy each saved file into the raw folder given to export.py:
//   1. specs   (MODE = 'specs')    -> raw/specs-<n>.json   (split SETS into batches if a call times out)
//   2. previews (MODE = 'previews') -> raw/previews-<n>.json (variant PNGs @2x, documentation frames @0.5x)
// If a result is small enough to come back inline (not saved to disk), add  pad: 'x'.repeat(150000)  to the
// returned object so the tool saves it; export.py ignores the pad field.
// timeout: 30000. First used 2026-10-14 (Buttons pilot: 8 sets in 2 batches of 4, specs then previews).
const MODE = 'specs';
const SETS = [
  // ['5328:15928', '7012:33138'],
];

const hex = c => '#' + [c.r, c.g, c.b].map(v => Math.round(v * 255).toString(16).padStart(2, '0')).join('').toLowerCase();
const varCache = {};
async function vname(id) {
  if (!(id in varCache)) {
    const v = await figma.variables.getVariableByIdAsync(id); let col = '';
    if (v) { const c = await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId); col = c ? c.name : ''; }
    varCache[id] = v ? (col + '/' + v.name) : id;
  }
  return varCache[id];
}
async function paints(ps) {
  if (!ps || ps === figma.mixed) return ps === figma.mixed ? 'mixed' : undefined;
  const out = [];
  for (const p of ps) {
    if (p.visible === false) continue;
    const o = { type: p.type };
    if (p.type === 'SOLID') { o.hex = hex(p.color); if (p.opacity !== 1) o.opacity = +p.opacity.toFixed(3); if (p.boundVariables && p.boundVariables.color) o.variable = await vname(p.boundVariables.color.id); }
    out.push(o);
  }
  return out.length ? out : undefined;
}
async function bv(n) {
  if (!n.boundVariables) return undefined; const o = {};
  for (const [k, v] of Object.entries(n.boundVariables)) {
    if (k === 'fills' || k === 'strokes') continue;
    if (Array.isArray(v)) { if (v[0] && v[0].id) o[k] = await vname(v[0].id); }
    else if (v && v.id) o[k] = await vname(v.id);
  }
  return Object.keys(o).length ? o : undefined;
}
async function ser(n, depth) {
  const o = { name: n.name, type: n.type, id: n.id, w: +n.width.toFixed(2), h: +n.height.toFixed(2) };
  if (n.parent && n.parent.type !== 'PAGE' && n.parent.type !== 'COMPONENT_SET') { o.x = +n.x.toFixed(2); o.y = +n.y.toFixed(2); }
  if (n.visible === false) o.hidden = true;
  if ('layoutSizingHorizontal' in n) { try { o.sizing = { h: n.layoutSizingHorizontal, v: n.layoutSizingVertical }; } catch (e) {} }
  if (n.layoutPositioning === 'ABSOLUTE') { o.absolute = true; o.constraints = n.constraints; }
  if (n.minWidth) o.minW = n.minWidth; if (n.minHeight) o.minH = n.minHeight; if (n.maxWidth) o.maxW = n.maxWidth;
  if ('layoutMode' in n && n.layoutMode && n.layoutMode !== 'NONE') o.layout = { dir: n.layoutMode, gap: n.itemSpacing, pad: [n.paddingTop, n.paddingRight, n.paddingBottom, n.paddingLeft], main: n.primaryAxisAlignItems, cross: n.counterAxisAlignItems, wrap: n.layoutWrap };
  if ('clipsContent' in n && n.clipsContent) o.clip = true;
  if ('cornerRadius' in n) { if (n.cornerRadius === figma.mixed) o.radius = [n.topLeftRadius, n.topRightRadius, n.bottomRightRadius, n.bottomLeftRadius]; else if (n.cornerRadius) o.radius = n.cornerRadius; }
  if ('opacity' in n && n.opacity < 1) o.opacity = +n.opacity.toFixed(3);
  if ('fills' in n && n.type !== 'TEXT') { const f = await paints(n.fills); if (f) o.fills = f; }
  if ('strokes' in n && n.strokes && n.strokes.length) { const s = await paints(n.strokes); if (s) { o.strokes = s; o.strokeWeight = n.strokeWeight === figma.mixed ? [n.strokeTopWeight, n.strokeRightWeight, n.strokeBottomWeight, n.strokeLeftWeight] : n.strokeWeight; o.strokeAlign = n.strokeAlign; if (n.dashPattern && n.dashPattern.length) o.dash = n.dashPattern; } }
  if ('effects' in n && n.effects.length) o.effects = n.effects.filter(e => e.visible !== false).map(e => ({ type: e.type, radius: e.radius, color: e.color ? hex(e.color) : undefined, offset: e.offset }));
  const b = await bv(n); if (b) o.vars = b;
  if (n.type === 'TEXT') {
    o.text = n.characters; o.autoResize = n.textAutoResize; o.align = n.textAlignHorizontal;
    const segs = n.getStyledTextSegments(['fontName', 'fontSize', 'lineHeight', 'letterSpacing', 'textCase', 'textDecoration', 'fills', 'boundVariables']);
    o.styles = [];
    for (const s of segs.slice(0, 4)) {
      const sv = {};
      for (const [k, v] of Object.entries(s.boundVariables || {})) { const x = Array.isArray(v) ? v[0] : v; if (x && x.id) sv[k] = await vname(x.id); }
      o.styles.push({ font: s.fontName.family, style: s.fontName.style, size: s.fontSize,
        lineHeight: s.lineHeight.unit === 'AUTO' ? 'auto' : (s.lineHeight.unit === 'PIXELS' ? s.lineHeight.value + 'px' : s.lineHeight.value + '%'),
        letterSpacing: s.letterSpacing.unit === 'PIXELS' ? s.letterSpacing.value + 'px' : s.letterSpacing.value + '%',
        case: s.textCase !== 'ORIGINAL' ? s.textCase : undefined, decoration: s.textDecoration !== 'NONE' ? s.textDecoration : undefined,
        color: await paints(s.fills), vars: Object.keys(sv).length ? sv : undefined });
    }
  }
  if (n.type === 'INSTANCE') {
    const m = await n.getMainComponentAsync();
    if (m) { const isV = m.parent && m.parent.type === 'COMPONENT_SET'; o.component = isV ? m.parent.name : m.name; o.componentSetId = isV ? m.parent.id : m.id; if (isV) o.variant = m.variantProperties; o.mainId = m.id; }
    const vec = n.findOne(x => 'fills' in x && x.type !== 'FRAME' && x.fills && x.fills !== figma.mixed && x.fills.length);
    if (vec) o.iconFill = await paints(vec.fills);
    return o;
  }
  if ('children' in n && depth < 12) { o.children = []; for (const c of n.children) o.children.push(await ser(c, depth + 1)); }
  return o;
}

if (MODE === 'specs') {
  const results = [];
  for (const [sid, did] of SETS) {
    const s = await figma.getNodeByIdAsync(sid); const doc = did ? await figma.getNodeByIdAsync(did) : null;
    const set = { id: s.id, key: s.key, name: s.name, description: s.description || null, type: s.type,
      properties: s.type === 'COMPONENT_SET' ? Object.fromEntries(Object.entries(s.componentPropertyDefinitions).map(([k, v]) => [k, { type: v.type, default: v.defaultValue, options: v.variantOptions }])) : {},
      variants: [] };
    const comps = s.type === 'COMPONENT_SET' ? s.children : [s];
    for (const v of comps) {
      const t = await ser(v, 0); t.key = v.key; t.variantProperties = v.variantProperties || {}; t.description = v.description || null;
      const ins = await v.getInstancesAsync(); const u = { total: 0, doc: 0, nested: 0, inComponents: {}, other: {} };
      for (const i of ins) {
        u.total++; if (i.parent && i.parent.type === 'INSTANCE') { u.nested++; continue; }
        let p = i, page = null, top = null, inComp = null, inDoc = false;
        while (p && p.type !== 'DOCUMENT') { if (did && p.id === did) inDoc = true; if (p.type === 'PAGE') page = p.name; if (p.parent && p.parent.type === 'PAGE') top = p.name; if (!inComp && p !== i && p.type === 'COMPONENT') inComp = (p.parent && p.parent.type === 'COMPONENT_SET') ? p.parent.name : p.name; p = p.parent; }
        if (inDoc) u.doc++; else if (inComp) u.inComponents[inComp] = (u.inComponents[inComp] || 0) + 1; else { const k = page + ' > ' + top; u.other[k] = (u.other[k] || 0) + 1; }
      }
      t.usage = u; set.variants.push(t);
    }
    let page = s; while (page && page.type !== 'PAGE') page = page.parent;
    const texts = doc ? doc.findAll(n => n.type === 'TEXT' && n.visible).filter(n => { let p = n.parent; while (p && p !== doc) { if (p.type === 'INSTANCE' || p.type === 'COMPONENT_SET') return false; p = p.parent; } return true; }).map(n => n.characters) : [];
    results.push({ set, page: { id: page.id, name: page.name }, doc: doc ? { id: doc.id, name: doc.name, w: doc.width, h: doc.height } : null, texts });
  }
  return { MODE, fileKey: figma.fileKey, fileName: figma.root.name, results };
}
if (MODE === 'previews') {
  const out = {};
  for (const [sid, did] of SETS) {
    const s = await figma.getNodeByIdAsync(sid);
    for (const v of (s.type === 'COMPONENT_SET' ? s.children : [s])) out[v.id] = figma.base64Encode(await v.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: 2 } }));
    if (did) { const d = await figma.getNodeByIdAsync(did); out[did] = figma.base64Encode(await d.exportAsync({ format: 'PNG', constraint: { type: 'SCALE', value: 0.5 } })); }
  }
  return { MODE, out };
}
