// MNG Web Design System: read the Figma variables for the token build.
// Run in the main file (MNG Web Design System, jFHYqhZbJjvWQmDI4myCsd) with the Desktop Bridge plugin
// (figma_execute). Save the returned object's collections as scripts/build-tokens/figma-variables.json
// (see that file's header), then run make-tokens.py and build.py.
// Colors are returned as 6-digit hex (alpha as "#rrggbb@0.6" when below 1); aliases as "{figma/variable/name}".
// Dashboard Typography is skipped until Reader Dashboard tokens are added to core.
const cols = await figma.variables.getLocalVariableCollectionsAsync();
const hex = c => '#' + [c.r, c.g, c.b].map(x => Math.round(x * 255).toString(16).padStart(2, '0')).join('') +
  (c.a !== undefined && c.a < 1 ? '@' + Math.round(c.a * 1000) / 1000 : '');
const out = {};
for (const c of cols) {
  if (c.name === 'Dashboard Typography') continue;
  const modeName = Object.fromEntries(c.modes.map(m => [m.modeId, m.name]));
  const arr = [];
  for (const id of c.variableIds) {
    const v = await figma.variables.getVariableByIdAsync(id);
    const values = {};
    for (const [mid, val] of Object.entries(v.valuesByMode)) {
      let x = val;
      if (val && val.type === 'VARIABLE_ALIAS') {
        const a = await figma.variables.getVariableByIdAsync(val.id);
        x = '{' + (a ? a.name : val.id) + '}';
      } else if (v.resolvedType === 'COLOR') x = hex(val);
      values[modeName[mid]] = x;
    }
    arr.push({ name: v.name, type: v.resolvedType, values, description: v.description || '', scopes: v.scopes });
  }
  out[c.name] = arr;
}
return { file: figma.fileKey, collections: out };
