// Figma plugin code for the MNG ad-slot export (figma-exports/mng-ads-export).
// File: WordPress Elements (b1iZxkFwtAYq9rElmnCAzd), page "Ads and Sponsored", component set Ad Blocks (517:4304).
// Scope: Ad Blocks only. RevContent (506:3865) is excluded on purpose (not built to production).
//
// Run each block below with figma_execute (Desktop Bridge plugin, fileKey b1iZxkFwtAYq9rElmnCAzd, timeout 30000).
// Each result is too big to come back inline, so the tool saves it to tool-results/*.txt (the `pad` key forces that).
// Copy the saved files into <raw>/ as specs.json, usage.json and previews.json, then run
//   python3 scripts/ads-export/build-ads-export.py <raw> figma-exports/mng-ads-export [date]
// Last used 2026-10-09.

// ============================================================ 1. SPECS → raw/specs.json
const hex=c=>'#'+[c.r,c.g,c.b].map(v=>Math.round(v*255).toString(16).padStart(2,'0')).join('').toUpperCase();
const varCache={},styleCache={};
async function vname(id){if(!(id in varCache)){let v=null;try{v=await figma.variables.getVariableByIdAsync(id)}catch(e){}let col='';if(v){const c=await figma.variables.getVariableCollectionByIdAsync(v.variableCollectionId);col=c?c.name:'';}varCache[id]=v?(col+'/'+v.name):id;}return varCache[id];}
async function sname(id){if(!id||typeof id!=='string')return null;if(!(id in styleCache)){let s=null;try{s=await figma.getStyleByIdAsync(id)}catch(e){}styleCache[id]=s?s.name:null;}return styleCache[id];}
async function paints(ps){if(!ps||ps===figma.mixed)return ps===figma.mixed?'mixed':undefined;const out=[];for(const p of ps){if(p.visible===false)continue;const o={type:p.type};if(p.type==='SOLID'){o.hex=hex(p.color);if(p.opacity!==1)o.opacity=+p.opacity.toFixed(2);if(p.boundVariables&&p.boundVariables.color)o.variable=await vname(p.boundVariables.color.id);}out.push(o);}return out.length?out:undefined;}
async function bv(n){if(!n.boundVariables)return undefined;const o={};for(const [k,v] of Object.entries(n.boundVariables)){if(k==='fills'||k==='strokes'||k==='textRangeFills')continue;if(Array.isArray(v)){const a=[];for(const x of v)a.push(await vname(x.id));o[k]=[...new Set(a)];if(o[k].length===1)o[k]=o[k][0];}else if(v&&v.id)o[k]=await vname(v.id);}return Object.keys(o).length?o:undefined;}
async function ser(n,depth){
  const o={name:n.name,type:n.type,id:n.id,w:+n.width.toFixed(1),h:+n.height.toFixed(1)};
  if(n.parent&&n.parent.type!=='PAGE'){o.x=+n.x.toFixed(1);o.y=+n.y.toFixed(1);}
  if(n.visible===false)o.hidden=true;
  if('constraints' in n&&n.parent&&n.parent.type!=='COMPONENT_SET')o.constraints=n.constraints;
  if('layoutMode' in n&&n.layoutMode&&n.layoutMode!=='NONE'){o.layout={dir:n.layoutMode,gap:n.itemSpacing,pad:[n.paddingTop,n.paddingRight,n.paddingBottom,n.paddingLeft],main:n.primaryAxisAlignItems,cross:n.counterAxisAlignItems};}
  if('clipsContent' in n&&n.clipsContent)o.clip=true;
  if('cornerRadius' in n){if(n.cornerRadius===figma.mixed)o.radius=[n.topLeftRadius,n.topRightRadius,n.bottomRightRadius,n.bottomLeftRadius];else if(n.cornerRadius)o.radius=n.cornerRadius;}
  if('opacity' in n&&n.opacity<1)o.opacity=+n.opacity.toFixed(2);
  if('fills' in n&&n.type!=='TEXT'){const f=await paints(n.fills);if(f)o.fills=f;}
  if('strokes' in n&&n.strokes&&n.strokes.length){const s=await paints(n.strokes);if(s){o.strokes=s;o.strokeWeight=n.strokeWeight===figma.mixed?'mixed':n.strokeWeight;o.strokeAlign=n.strokeAlign;if(n.dashPattern&&n.dashPattern.length)o.dash=n.dashPattern;}}
  if('effects' in n&&n.effects.length){o.effects=n.effects.filter(e=>e.visible!==false).map(e=>({type:e.type,hex:e.color?hex(e.color):undefined,a:e.color?+e.color.a.toFixed(2):undefined,x:e.offset?e.offset.x:undefined,y:e.offset?e.offset.y:undefined,blur:e.radius,spread:e.spread}));}
  if(n.type==='BOOLEAN_OPERATION')o.op=n.booleanOperation;
  const b=await bv(n);if(b)o.vars=b;
  if(n.type==='TEXT'){o.text=n.characters;o.autoResize=n.textAutoResize;o.align=n.textAlignHorizontal;o.alignV=n.textAlignVertical;
    const segs=n.getStyledTextSegments(['fontName','fontSize','lineHeight','letterSpacing','textCase','fills','textStyleId']);
    o.styles=[];for(const s of segs.slice(0,4)){o.styles.push({font:s.fontName.family,weight:s.fontName.style,size:s.fontSize,lineHeight:s.lineHeight.unit==='AUTO'?'auto':(s.lineHeight.unit==='PIXELS'?+s.lineHeight.value.toFixed(2)+'px':+s.lineHeight.value.toFixed(2)+'%'),letterSpacing:s.letterSpacing.value?(s.letterSpacing.unit==='PIXELS'?+s.letterSpacing.value.toFixed(3)+'px':+s.letterSpacing.value.toFixed(2)+'%'):undefined,case:s.textCase!=='ORIGINAL'?s.textCase:undefined,color:(await paints(s.fills)),textStyle:await sname(s.textStyleId)});}}
  if(n.type==='LINE'||n.type==='ELLIPSE'||n.type==='VECTOR'){o.rotation=+n.rotation.toFixed(1);}
  if('children' in n&&depth<6){o.children=[];for(const c of n.children)o.children.push(await ser(c,depth+1));}
  return o;
}
const set=await figma.getNodeByIdAsync('517:4304');
const page=(()=>{let p=set;while(p.type!=='PAGE')p=p.parent;return p.name})();
const variants=[];for(const v of set.children){const t=await ser(v,0);t.key=v.key;t.variantProperties=v.variantProperties;t.componentDescription=v.description||null;variants.push(t);}
const tpl=await figma.getNodeByIdAsync('496:7892'); // "Advertizment Template" base frame (reference only)
return {SPECS_MARKER:true,fileKey:figma.fileKey,fileName:figma.root.name,page,set:{id:set.id,key:set.key,name:set.name,description:set.description||null,w:set.width,h:set.height,properties:Object.fromEntries(Object.entries(set.componentPropertyDefinitions).map(([k,v])=>[k,{type:v.type,default:v.defaultValue,options:v.variantOptions}])),variants},template:await ser(tpl,0),pad:'x'.repeat(90000)};

// ============================================================ 2. USAGE → raw/usage.json
// Every instance of each variant that isn't nested inside another instance, with its full frame path.
// Instances on no page (inside deleted nodes Figma still keeps) are skipped.
await figma.loadAllPagesAsync();
const set=await figma.getNodeByIdAsync('517:4304');
const out={};
for(const v of set.children){const insts=await v.getInstancesAsync();const list=[];
 for(const i of insts){let p=i.parent,nested=false,page=null,inComp=null;const path=[];
  while(p&&p.type!=='DOCUMENT'){if(p.type==='INSTANCE')nested=true;if(p.type==='PAGE')page=p.name;else path.unshift({n:p.name,t:p.type,id:p.id});if(!inComp&&p.type==='COMPONENT')inComp=(p.parent&&p.parent.type==='COMPONENT_SET')?p.parent.name+' / '+p.name:p.name;p=p.parent;}
  if(nested||!page)continue;
  list.push({id:i.id,name:i.name,w:Math.round(i.width),h:Math.round(i.height),x:Math.round(i.x),y:Math.round(i.y),page,inComp,path});}
 out[v.name]=list;}
return {USAGE_MARKER:true,out,pad:'x'.repeat(90000)};

// ============================================================ 3. PREVIEWS → raw/previews.json
const set=await figma.getNodeByIdAsync('517:4304');const out={},err={};
for(const n of set.children){try{const b=await n.exportAsync({format:'PNG',constraint:{type:'SCALE',value:1}});out[n.id]=figma.base64Encode(b);}catch(e){err[n.id]=String(e);}}
try{const b=await set.exportAsync({format:'PNG',constraint:{type:'SCALE',value:0.5}});out['SET']=figma.base64Encode(b);}catch(e){err.SET=String(e)}
return {PREVIEWS:true,err,out};
