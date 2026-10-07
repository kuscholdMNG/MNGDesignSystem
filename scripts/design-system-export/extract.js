// Figma plugin code for the MNG design-system spec export (figma-exports/mng-design-system-export).
// Run each block with figma_execute (Desktop Bridge plugin). Big results are saved by the tool to
// tool-results/*.txt — copy each one into <raw>/ under the file name given, then run
//   python3 build-design-system-export.py <raw> <previews> figma-exports/mng-design-system-export [date]
// Last used 2026-10-07.
//
// Files: WordPress Elements = b1iZxkFwtAYq9rElmnCAzd, MNG Design System = jFHYqhZbJjvWQmDI4myCsd.
// After a library publish, relaunch the Desktop Bridge plugin before running these.

// ============================================================ 0. SETUP (run once per file, both files)
// Setup: defines globalThis.__ser / __entry used by the batch calls. Run once per file (fileKey).
const hex=c=>'#'+[c.r,c.g,c.b].map(v=>Math.round(v*255).toString(16).padStart(2,'0')).join('').toUpperCase();
const varCache={},styleCache={};
async function vname(id){if(!(id in varCache)){let v=null;try{v=await figma.variables.getVariableByIdAsync(id)}catch(e){}let col='';if(v){const c=await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId);col=c?c.name:'';}varCache[id]=v?(col+'/'+v.name):id;}return varCache[id];}
async function sname(id){if(!id||typeof id!=='string')return null;if(!(id in styleCache)){let s=null;try{s=await figma.getStyleByIdAsync(id)}catch(e){}styleCache[id]=s?s.name:null;}return styleCache[id];}
async function paints(ps){if(!ps||ps===figma.mixed)return ps===figma.mixed?'mixed':undefined;const out=[];for(const p of ps){if(p.visible===false)continue;const o={type:p.type};if(p.type==='SOLID'){o.hex=hex(p.color);if(p.opacity!==1)o.opacity=+p.opacity.toFixed(2);if(p.boundVariables&&p.boundVariables.color)o.variable=await vname(p.boundVariables.color.id);}else if(p.type==='IMAGE'){o.scaleMode=p.scaleMode;}else if(p.type.startsWith('GRADIENT')){o.stops=p.gradientStops.map(s=>({hex:hex(s.color),a:+s.color.a.toFixed(2),pos:+s.position.toFixed(2)}));}out.push(o);}return out.length?out:undefined;}
async function bv(n){if(!n.boundVariables)return undefined;const o={};for(const [k,v] of Object.entries(n.boundVariables)){if(k==='fills'||k==='strokes'||k==='textRangeFills')continue;if(Array.isArray(v)){const a=[];for(const x of v)a.push(await vname(x.id));o[k]=[...new Set(a)];if(o[k].length===1)o[k]=o[k][0];}else if(v&&v.id)o[k]=await vname(v.id);}return Object.keys(o).length?o:undefined;}
async function ser(n,depth){
  const o={name:n.name,type:n.type,id:n.id,w:+n.width.toFixed(1),h:+n.height.toFixed(1)};
  if(n.parent&&n.parent.type!=='PAGE'){o.x=+n.x.toFixed(1);o.y=+n.y.toFixed(1);}
  if(n.visible===false)o.hidden=true;
  if('layoutSizingHorizontal' in n&&n.parent&&'layoutMode' in n.parent&&n.parent.layoutMode&&n.parent.layoutMode!=='NONE'){o.sizing={h:n.layoutSizingHorizontal,v:n.layoutSizingVertical};if(n.layoutPositioning==='ABSOLUTE')o.absolute=true;}
  else if('layoutSizingHorizontal' in n&&n.layoutMode&&n.layoutMode!=='NONE'){o.sizing={h:n.layoutSizingHorizontal,v:n.layoutSizingVertical};}
  if(n.minWidth)o.minW=n.minWidth;if(n.maxWidth)o.maxW=n.maxWidth;
  if('layoutMode' in n&&n.layoutMode&&n.layoutMode!=='NONE'){o.layout={dir:n.layoutMode,gap:n.itemSpacing,pad:[n.paddingTop,n.paddingRight,n.paddingBottom,n.paddingLeft],main:n.primaryAxisAlignItems,cross:n.counterAxisAlignItems};if(n.layoutWrap==='WRAP'){o.layout.wrap=true;o.layout.rowGap=n.counterAxisSpacing;}}
  if('clipsContent' in n&&n.clipsContent)o.clip=true;
  if('cornerRadius' in n){if(n.cornerRadius===figma.mixed)o.radius=[n.topLeftRadius,n.topRightRadius,n.bottomRightRadius,n.bottomLeftRadius];else if(n.cornerRadius)o.radius=n.cornerRadius;}
  if('opacity' in n&&n.opacity<1)o.opacity=+n.opacity.toFixed(2);
  if('fills' in n&&n.type!=='TEXT'){const f=await paints(n.fills);if(f)o.fills=f;const fs=await sname(n.fillStyleId);if(fs)o.fillStyle=fs;}
  if('strokes' in n&&n.strokes&&n.strokes.length){const s=await paints(n.strokes);if(s){o.strokes=s;o.strokeWeight=n.strokeWeight===figma.mixed?[n.strokeTopWeight,n.strokeRightWeight,n.strokeBottomWeight,n.strokeLeftWeight]:n.strokeWeight;o.strokeAlign=n.strokeAlign;if(n.dashPattern&&n.dashPattern.length)o.dash=n.dashPattern;}}
  if('effects' in n&&n.effects.length){o.effects=n.effects.filter(e=>e.visible!==false).map(e=>({type:e.type,hex:e.color?hex(e.color):undefined,a:e.color?+e.color.a.toFixed(2):undefined,x:e.offset?e.offset.x:undefined,y:e.offset?e.offset.y:undefined,blur:e.radius,spread:e.spread}));}
  const b=await bv(n);if(b)o.vars=b;
  if(n.type==='TEXT'){o.text=n.characters.length>160?n.characters.slice(0,160)+'…':n.characters;o.autoResize=n.textAutoResize;o.align=n.textAlignHorizontal;if(n.textTruncation==='ENDING'){o.truncate=true;o.maxLines=n.maxLines;}
    const segs=n.getStyledTextSegments(['fontName','fontSize','lineHeight','letterSpacing','textCase','textDecoration','fills','textStyleId']);
    o.styles=[];for(const s of segs.slice(0,4)){o.styles.push({font:s.fontName.family,weight:s.fontName.style,size:s.fontSize,lineHeight:s.lineHeight.unit==='AUTO'?'auto':(s.lineHeight.unit==='PIXELS'?+s.lineHeight.value.toFixed(2)+'px':+s.lineHeight.value.toFixed(2)+'%'),letterSpacing:s.letterSpacing.value?(s.letterSpacing.unit==='PIXELS'?+s.letterSpacing.value.toFixed(3)+'px':+s.letterSpacing.value.toFixed(2)+'%'):undefined,case:s.textCase!=='ORIGINAL'?s.textCase:undefined,decoration:s.textDecoration!=='NONE'?s.textDecoration:undefined,color:(await paints(s.fills)),textStyle:await sname(s.textStyleId),chars:segs.length>1?s.characters.slice(0,40):undefined});}
  }
  if(n.type==='INSTANCE'){const m=await n.getMainComponentAsync();if(m){const isV=m.parent&&m.parent.type==='COMPONENT_SET';o.component=isV?m.parent.name:m.name;if(isV)o.variant=m.variantProperties;o.componentKey=m.key;o.mainId=m.id;}else o.component='(missing main)';
    try{const cp=n.componentProperties;const props={};for(const [k,v] of Object.entries(cp)){if(v.type!=='VARIANT')props[k.split('#')[0]]=v.value;}if(Object.keys(props).length)o.props=props;}catch(e){}
    return o;}
  if('children' in n&&depth<14){o.children=[];for(const c of n.children)o.children.push(await ser(c,depth+1));}
  return o;
}
async function mainEntry(m){const me={id:m.id,key:m.key,type:m.type,name:m.name,componentDescription:m.description||null};
  let defs=null,err=null;try{defs=m.componentPropertyDefinitions}catch(e){err=String(e)}
  if(err)me.propertyError=err;
  if(m.type==='COMPONENT_SET'){me.properties=defs?Object.fromEntries(Object.entries(defs).map(([k,v])=>[k,{type:v.type,default:v.defaultValue,options:v.variantOptions}])):null;me.variants=[];for(const v of m.children){if(v.type!=='COMPONENT')continue;const t=await ser(v,0);t.key=v.key;t.variantProperties=v.variantProperties;t.componentDescription=v.description||null;me.variants.push(t);}}
  else{me.properties=defs?Object.fromEntries(Object.entries(defs).map(([k,v])=>[k,{type:v.type,default:v.defaultValue}])):null;me.tree=await ser(m,0);}
  return me;}
// designer notes: visible text layers that sit next to the item (siblings in its parent frame, outside components)
function notes(m){const p=m.parent;if(!p||p.type==='PAGE')return [];return p.children.filter(c=>c!==m&&c.type==='TEXT'&&c.visible).map(c=>c.characters).slice(0,8);}
globalThis.__ser=ser;globalThis.__mainEntry=mainEntry;globalThis.__notes=notes;
return 'ok';

// ============================================================ 1. SPECS
// 1a. Homepage, WordPress Elements. Run with RANGE=[0,12] → specs_hp_a.json, then [12,24] → specs_hp_b.json
/*
const RANGE=[0,12];const root=await figma.getNodeByIdAsync('3334:42288');const all=root.findAll(n=>n.type==='FRAME'&&n.name.endsWith(' Container')&&n.children.some(c=>c.name==='Variant Grid'));const out=[];
for(const s of all.slice(RANGE[0],RANGE[1])){const head=s.children.find(c=>c.name==='Header');const desc=s.children.find(c=>c.name==='Description');const grid=s.children.find(c=>c.name==='Variant Grid');
 const e={group:'homepage',section:s.name.replace(/ Container$/,''),typeLabel:head.children[0].characters,description:desc?desc.characters:null,order:all.indexOf(s),mains:[]};
 for(const m of grid.children.filter(c=>c.type==='COMPONENT'||c.type==='COMPONENT_SET'))e.mains.push(await __mainEntry(m));out.push(e)}
return {SPECS_MARKER:'hp_a',fileKey:figma.fileKey,fileName:figma.root.name,sections:out};
*/
// 1b. Menus and Parts, WordPress Elements → specs_mp_a.json (Masthead 456:2572 alone → specs_mp_b.json)
/*
const IDS=['654:10020','456:5745','456:5683','456:5708','456:5910','506:5632','354:1282','456:5781','456:5674','456:5837','456:5728'];const out=[];
for(const id of IDS){const m=await figma.getNodeByIdAsync(id);let p=m.parent,path=[];while(p&&p.type!=='PAGE'){path.unshift(p.name);p=p.parent}
 out.push({group:'menus-and-parts',section:m.name,description:m.description||null,path:path.join(' ▸ '),designerNotes:__notes(m),mains:[await __mainEntry(m)]})}
return {SPECS_MARKER:'mp_a',fileKey:figma.fileKey,fileName:figma.root.name,sections:out};
*/
// 1c. Form Fields, MNG Design System, same pattern with group:'form-fields' →
//     specs_ff_a.json: ['6963:6863','6964:7032','7003:29236','6995:27285','7003:28636','7003:28651','7003:28666','7003:28741','7003:28816','7003:28940','7003:29223','6996:27351']
//     specs_ff_b.json: ['2832:766'] (Form Field Dashboard Mockup Set, 102 variants)

// ============================================================ 2. USAGE (one call per file → usage_wp.json / usage_mf.json)
/*
await figma.loadAllPagesAsync();const TPL='3369:44781'; // homepage templates frame (WordPress Elements only)
const mains=[]; // all homepage mains (from 3334:42288 sections) + the menus IDs above; in the main file the form-field IDs
function ctx(i){let p=i,page=null,top=null,tmpl=null,inComp=null;while(p&&p.type!=='DOCUMENT'){if(p.type==='PAGE')page=p.name;if(p.parent&&p.parent.type==='PAGE')top=p.name;if(p.parent&&p.parent.id===TPL)tmpl=p.name;if(!inComp&&p!==i&&p.type==='COMPONENT')inComp=(p.parent&&p.parent.type==='COMPONENT_SET')?p.parent.name+' / '+p.name:p.name;p=p.parent;}return {page,top,tmpl,inComp};}
const out={};for(const m of mains){const comps=m.type==='COMPONENT_SET'?m.children.filter(c=>c.type==='COMPONENT'):[m];
 for(const c of comps){const insts=await c.getInstancesAsync();const tm={},inc={},other={};
  for(const i of insts){let nested=false;{let p=i.parent;while(p&&p.type!=='PAGE'){if(p.type==='INSTANCE'){nested=true;break}p=p.parent}}if(nested)continue;const x=ctx(i);if(!x.page)continue; /* skip deleted nodes getInstancesAsync still returns */if(x.inComp)inc[x.inComp]=(inc[x.inComp]||0)+1;else if(x.tmpl)tm[x.tmpl]=(tm[x.tmpl]||0)+1;else{const k=x.page+' ▸ '+x.top;other[k]=(other[k]||0)+1;}}
  out[c.id]={set:m.name,variant:c.name,templates:tm,inComponents:inc,other}}}
return {USAGE_MARKER:'wp',out};
*/

// ============================================================ 3. COLOR MODES (main file → colormodes.json)
// For each color/<name> variable in the "Colors" collection: {modes, def, out:{name:{mode:hex}}}.

// ============================================================ 4. PREVIEWS (batches of ~10 mains; Masthead in 3 slices of 25)
/*
const MAINS=[...];const out={},err={};
for(const id of MAINS){const m=await figma.getNodeByIdAsync(id);const vs=m.type==='COMPONENT_SET'?m.children.filter(c=>c.type==='COMPONENT'):[m];for(const v of vs){if(v.width<1||v.height<1){err[v.id]='zero';continue}try{out[v.id]=figma.base64Encode(await v.exportAsync({format:'PNG',constraint:{type:'SCALE',value:1}}))}catch(e){err[v.id]=String(e)}}}
return {PREVIEWS:'p1',err,out};
*/
// Decode each saved result with save-previews.py <saved-result.txt> <raw> <previews>.
