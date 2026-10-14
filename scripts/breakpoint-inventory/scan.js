// MNG Web Design System: live breakpoint scan (Claude in Chrome, javascript_tool). Used 2026-10-14 for
// tokens/breakpoint-inventory.json. Reads every @media rule with a width condition in the page's stylesheets
// (cross-origin sheets are fetched and parsed; blocked ones are listed) and merges pages of one site in
// localStorage, so it can run on several pages of the same site:
//   1. Store this file's expression in localStorage('__mngscan') on the site, then on each page:
//        window.__F = false; await eval(localStorage.getItem('__mngscan'))   // homepage, article
//        window.__F = true;  await eval(localStorage.getItem('__mngscan'))   // last page (obituaries)
//   2. The last page replaces the page body with the JSON result; read it with get_page_text
//      (javascript_tool output is cut at about 1,000 characters) and save it as scans/<domain>.json.
// KNOWN is the ocregister.com result: other sites report only values not in it ("b") and values missing
// from it ("absent"). Clear KNOWN to get a full list. Both localStorage keys are removed at the end.
// Keys: ">640" = (min-width: 640px), "<639" = (max-width: 639px); em/rem are converted at 16px.
(async () => {
  const FINAL = !!window.__F;
  const short = h => (h || 'inline').split('?')[0].replace(/^https?:\/\//, '');
  const conds = {};
  const add = (cond, sheet, rule) => {
    if (!/width/.test(cond)) return;
    const c = conds[cond] || (conds[cond] = { n: 0, sheets: [], sel: [] });
    c.n += 1; if (!c.sheets.includes(sheet)) c.sheets.push(sheet);
    const s = rule && rule.selectorText; if (s && c.sel.length < 1) c.sel.push(s.slice(0, 40));
  };
  const walk = (rules, sheet) => { for (const r of rules) {
    if (r.type === 4) { const cond = r.conditionText || r.media.mediaText; for (const i of r.cssRules) if (i.type === 1) add(cond, sheet, i); walk([...r.cssRules].filter(x => x.type !== 1), sheet); }
    else if (r.type === 3 && r.styleSheet) { try { walk(r.styleSheet.cssRules, short(r.href)); } catch (e) {} }
    else if (r.cssRules) walk(r.cssRules, sheet); } };
  const blocked = [];
  for (const ss of document.styleSheets) { const name = short(ss.href); let rules;
    try { rules = ss.cssRules; } catch (e) { try { const t = await fetch(ss.href).then(r => r.text()); const tmp = new CSSStyleSheet(); tmp.replaceSync(t.replace(/@import[^;]+;/g, '')); rules = tmp.cssRules; } catch (e2) { blocked.push(name.slice(0, 60)); continue; } }
    if (ss.media && /width/.test(ss.media.mediaText)) add(ss.media.mediaText, name, null);
    walk(rules, name); }
  const px = (v, u) => u === 'px' ? +v : +v * 16;
  const host = location.hostname.replace(/^www\./, '');
  const tag = s => /wp-content|_static|^inline/.test(s) || s.startsWith('www.' + host) || s.startsWith(host)
    ? s.replace(/^.*wp-content\/(themes|plugins|mu-plugins)\//, '').replace(/^.*\/_static\/.*/, '_static').replace(/\/(dist|static|build|assets)\/.*$/, '').replace(/^assets$/, 'theme')
    : '3P:' + s.split('/')[0];
  let store = {}; try { store = JSON.parse(localStorage.getItem('__mngbp') || '{}'); } catch (e) {}
  store.pages = (store.pages || []).concat(location.pathname.slice(0, 50));
  store.blocked = [...new Set((store.blocked || []).concat(blocked))];
  const out = store.b || {};
  const pageSeen = {};
  for (const [cond, c] of Object.entries(conds)) {
    const re = /\(\s*(min|max)-width\s*:\s*([\d.]+)(px|em|rem)\s*\)|\(\s*width\s*(>=|<=|>|<)\s*([\d.]+)(px|em|rem)\s*\)/g; let m;
    while ((m = re.exec(cond))) {
      let kind, val; if (m[1]) { kind = m[1]; val = px(m[2], m[3]); } else { kind = m[4].startsWith('>') ? 'min' : 'max'; val = px(m[5], m[6]); }
      val = Math.round(val * 100) / 100; const k = (kind === 'min' ? '>' : '<') + val;
      const o = out[k] || (out[k] = [0, [], '']);
      pageSeen[k] = (pageSeen[k] || 0) + c.n;
      c.sheets.forEach(s => { const t = tag(s); if (!o[1].includes(t)) o[1].push(t); });
      if (!o[2] && c.sel[0]) o[2] = c.sel[0];
    } }
  for (const [k, n] of Object.entries(pageSeen)) out[k][0] = Math.max(out[k][0], n);
  store.b = out;
  const art = [...document.querySelectorAll('a[href]')].map(a => a.href).find(h => h.includes(host) && /\/20\d\d\/\d\d\/\d\d\/[a-z0-9-]{25,}/.test(h) && !/redirect|voter-guide/.test(h));
  if (!FINAL) { localStorage.setItem('__mngbp', JSON.stringify(store)); return JSON.stringify({ page: location.pathname, keys: Object.keys(out).length, article: art, blocked }); }
  localStorage.removeItem('__mngbp'); localStorage.removeItem('__mngscan');
  const KNOWN = [">300", ">320", "<335", "<340", "<344", "<350", "<360", ">360", ">376", "<380", "<400", "<405", "<420", "<430", ">431", "<432", "<450", ">450", "<467", "<480", "<500", "<535", "<550", "<575.98", "<576", ">576", "<600", ">600", "<624", ">625", "<639", ">640", "<700", "<720", "<730", "<734", ">735", "<750", ">750", "<767", "<767.98", "<768", ">768", "<770", "<783", ">783", "<799", "<800", ">800", "<820", "<900", "<930", "<960", "<971", ">972", "<979", "<991", "<991.98", "<992", ">992", "<1000", ">1000", "<1024", ">1024", "<1025", "<1039", "<1040", ">1040", "<1064", "<1150", "<1199", "<1199.98", "<1200", ">1200", "<1279", "<1280", ">1280", ">1281", "<1299", ">1300", "<1399.98", ">1400"];
  const res = { site: host, w: innerWidth, pages: store.pages, blocked: store.blocked,
    absent: KNOWN.filter(k => !out[k]),
    b: Object.entries(out).filter(([k]) => !KNOWN.includes(k)).sort((a, b) => parseFloat(a[0].slice(1)) - parseFloat(b[0].slice(1)) || a[0].localeCompare(b[0])).map(([k, v]) => [k, ...v]) };
  document.body.innerHTML = '<main><article><pre id="bp"></pre></article></main>';
  document.getElementById('bp').textContent = JSON.stringify(res);
  return 'final ' + res.b.length;
})()
