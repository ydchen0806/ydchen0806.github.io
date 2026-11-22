/**
 * Private visitor log for a static GitHub Pages site.
 * Public: POST /collect; private (ADMIN_TOKEN): GET /api/stats and /api/visits.
 * The /dashboard HTML contains no visitor data until authentication succeeds.
 */
const MAX_BODY_BYTES = 2048;
const DEFAULT_RAW_DAYS = 3;
const DEFAULT_RETENTION_DAYS = 30;
const BOT_PATTERN = /(?:bot\b|spider|crawler|headless|lighthouse|curl\/|wget\/|python-requests|facebookexternalhit|slurp|preview)/i;

const jsonHeaders = {
  'Content-Type': 'application/json; charset=utf-8',
  'Cache-Control': 'no-store, private',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'no-referrer',
};

function replyJson(body, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: jsonHeaders });
}
function integerInRange(value, fallback, max) {
  const n = Number(value);
  return Number.isInteger(n) && n >= 1 && n <= max ? n : fallback;
}
function safeEqual(a, b) {
  const x = new TextEncoder().encode(a);
  const y = new TextEncoder().encode(b);
  let result = x.length ^ y.length;
  for (let i = 0; i < Math.max(x.length, y.length); i++) result |= (x[i] || 0) ^ (y[i] || 0);
  return result === 0;
}
function isAuthorized(request, env) {
  const expected = env.ADMIN_TOKEN;
  if (!expected || expected.length < 32) return false;
  const auth = request.headers.get('Authorization') || '';
  return auth.startsWith('Bearer ') && safeEqual(auth.slice(7), expected);
}
function maskIP(ip) {
  if (/^(?:\d{1,3}\.){3}\d{1,3}$/.test(ip)) {
    const parts = ip.split('.');
    if (parts.every((part) => Number(part) <= 255)) return `${parts.slice(0, 3).join('.')}.*`;
  }
  if (ip.includes(':') && /^[a-fA-F0-9:.]+$/.test(ip)) {
    return `${ip.split(':').slice(0, 3).join(':')}::/48`;
  }
  return 'Unavailable';
}
function cleanText(value, max = 80) {
  return typeof value === 'string' ? value.replace(/[\x00-\x1F\x7F]/g, '').trim().slice(0, max) : '';
}
function sanitizePath(raw) {
  if (typeof raw !== 'string' || !raw.startsWith('/') || raw.startsWith('//')) return '/';
  return cleanText(raw.split(/[?#]/, 1)[0], 200) || '/';
}
function referrerHost(raw, siteOrigin) {
  if (!raw || typeof raw !== 'string') return 'Direct';
  try {
    const ref = new URL(raw);
    if (ref.protocol !== 'https:' && ref.protocol !== 'http:') return 'Direct';
    if (ref.origin === siteOrigin) return 'Internal';
    return cleanText(ref.hostname.toLowerCase(), 100) || 'Direct';
  } catch { return 'Direct'; }
}
function getBrowser(ua) {
  if (/Edg\//.test(ua)) return 'Edge';
  if (/Firefox\//.test(ua)) return 'Firefox';
  if (/Chrome\//.test(ua) || /CriOS\//.test(ua)) return 'Chrome';
  if (/Safari\//.test(ua)) return 'Safari';
  return 'Other';
}
function getOS(ua) {
  if (/Android/i.test(ua)) return 'Android';
  if (/iPhone|iPad|iPod/i.test(ua)) return 'iOS';
  if (/Windows/i.test(ua)) return 'Windows';
  if (/Mac OS X/i.test(ua)) return 'macOS';
  if (/Linux/i.test(ua)) return 'Linux';
  return 'Other';
}
function getDevice(ua) {
  return /iPad|Tablet/i.test(ua) ? 'Tablet' : /Mobile|Android|iPhone|iPod/i.test(ua) ? 'Mobile' : 'Desktop';
}
function sqlDate() {
  return new Date().toISOString().replace('T', ' ').slice(0, 19);
}
function originAllowed(request, env) {
  const allowed = (env.SITE_ORIGIN || '').replace(/\/$/, '');
  return Boolean(allowed) && request.headers.get('Origin') === allowed;
}
async function collect(request, env) {
  // A same-origin browser signal, not a security boundary: scripts and curl can forge Origin.
  if (!originAllowed(request, env)) return replyJson({ error: 'Forbidden origin' }, 403);
  if (!/^text\/plain(?:;|$)/i.test(request.headers.get('Content-Type') || '')) {
    return replyJson({ error: 'Only text/plain is accepted' }, 415);
  }
  if (Number(request.headers.get('Content-Length') || 0) > MAX_BODY_BYTES) {
    return replyJson({ error: 'Payload too large' }, 413);
  }
  const ua = request.headers.get('User-Agent') || '';
  if (BOT_PATTERN.test(ua)) return new Response(null, { status: 204 });
  let body;
  try {
    const raw = await request.text();
    if (raw.length > MAX_BODY_BYTES) return replyJson({ error: 'Payload too large' }, 413);
    body = JSON.parse(raw);
  } catch { return replyJson({ error: 'Invalid JSON' }, 400); }
  if (!body || typeof body !== 'object' || Array.isArray(body)) return replyJson({ error: 'Invalid event' }, 400);
  const cf = request.cf || {};
  const ip = cleanText(request.headers.get('CF-Connecting-IP') || '', 80);
  const rawDays = integerInRange(env.RAW_IP_DAYS, DEFAULT_RAW_DAYS, 30);
  const ipRaw = rawDays > 0 && ip !== '' && maskIP(ip) !== 'Unavailable' ? ip : null;
  const page = sanitizePath(body.page);
  const source = referrerHost(body.referrer, (env.SITE_ORIGIN || '').replace(/\/$/, ''));
  await env.DB.prepare(`
    INSERT INTO visits (visited_at, ip_masked, ip_raw, country, region, city, page, source, browser, os, device)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    sqlDate(), maskIP(ip), ipRaw,
    cleanText(cf.country || '', 60) || 'Unknown',
    cleanText(cf.region || '', 80), cleanText(cf.city || '', 80),
    page, source, getBrowser(ua), getOS(ua), getDevice(ua),
  ).run();
  return new Response(null, { status: 204, headers: { 'Cache-Control': 'no-store' } });
}
async function visits(request, env) {
  const url = new URL(request.url);
  const limit = integerInRange(url.searchParams.get('limit'), 50, 100);
  const days = integerInRange(env.DATA_RETENTION_DAYS, DEFAULT_RETENTION_DAYS, 365);
  const rawDays = integerInRange(env.RAW_IP_DAYS, DEFAULT_RAW_DAYS, 30);
  const showRaw = url.searchParams.get('raw') === '1';
  const ipExpression = showRaw
    ? `CASE WHEN visited_at >= datetime('now', ?) THEN ip_raw ELSE NULL END AS ip_raw`
    : 'NULL AS ip_raw';
  const stmt = env.DB.prepare(`
    SELECT id, visited_at, ip_masked, ${ipExpression}, country, region, city, page, source, browser, os, device
    FROM visits WHERE visited_at >= datetime('now', ?)
    ORDER BY visited_at DESC, id DESC LIMIT ?
  `);
  const args = showRaw ? [`-${rawDays} days`, `-${days} days`, limit] : [`-${days} days`, limit];
  const result = await stmt.bind(...args).all();
  return replyJson({ visits: result.results || [], raw_ip_days: rawDays, retention_days: days });
}
async function stats(env) {
  const [c24, c7, c30, daily, countries, sources, pages] = await Promise.all([
    env.DB.prepare("SELECT COUNT(*) AS value FROM visits WHERE visited_at >= datetime('now', '-1 day')").first(),
    env.DB.prepare("SELECT COUNT(*) AS value FROM visits WHERE visited_at >= datetime('now', '-7 days')").first(),
    env.DB.prepare("SELECT COUNT(*) AS value FROM visits WHERE visited_at >= datetime('now', '-30 days')").first(),
    env.DB.prepare("SELECT date(visited_at) AS day, COUNT(*) AS visits FROM visits WHERE visited_at >= datetime('now', '-14 days') GROUP BY date(visited_at) ORDER BY day").all(),
    env.DB.prepare("SELECT country AS label, COUNT(*) AS count FROM visits WHERE visited_at >= datetime('now', '-30 days') GROUP BY country ORDER BY count DESC LIMIT 8").all(),
    env.DB.prepare("SELECT source AS label, COUNT(*) AS count FROM visits WHERE visited_at >= datetime('now', '-30 days') GROUP BY source ORDER BY count DESC LIMIT 8").all(),
    env.DB.prepare("SELECT page AS label, COUNT(*) AS count FROM visits WHERE visited_at >= datetime('now', '-30 days') GROUP BY page ORDER BY count DESC LIMIT 8").all(),
  ]);
  return replyJson({
    last24h: c24?.value || 0, last7d: c7?.value || 0, last30d: c30?.value || 0,
    daily: daily.results || [], countries: countries.results || [],
    sources: sources.results || [], pages: pages.results || [],
    updated_at: new Date().toISOString(),
  });
}
function dashboard() {
  const nonce = crypto.randomUUID().replace(/-/g, '');
  const html = `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive"><title>Visitor Insights | Private Dashboard</title>
<style nonce="${nonce}">
:root{color-scheme:light;font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#233247;background:#f6f8fb}*{box-sizing:border-box}body{margin:0}main{max-width:1100px;margin:0 auto;padding:38px 24px 70px}header{display:flex;justify-content:space-between;align-items:start;flex-wrap:wrap;gap:12px;margin-bottom:26px}h1{font-size:1.9rem;letter-spacing:-.055em;margin:5px 0 8px}h2{font-size:1rem;margin:0 0 18px}.muted{color:#66768a;font-size:.86rem}.eyebrow{text-transform:uppercase;color:#4b6591;letter-spacing:.14em;font-size:.72rem;font-weight:700}.auth{background:#fff;border:1px solid #e1e6ee;border-radius:13px;padding:22px;max-width:560px;box-shadow:0 5px 18px rgba(31,55,88,.035)}input{font:inherit;border-radius:8px;border:1px solid #d1dbe6;padding:11px 13px;min-width:180px;flex:1}input:focus{outline:2px solid #9bb8ea}button{font:inherit;border:0;border-radius:8px;background:#243d61;color:#fff;padding:11px 18px;cursor:pointer}button:hover{background:#395c8a}.login{display:flex;gap:9px;flex-wrap:wrap;margin:14px 0}.status{min-height:1.4em;color:#8e3d33;font-size:.86rem}.kpis{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:20px 0}.kpi,.panel{background:#fff;border:1px solid #e1e6ee;border-radius:12px;padding:19px 21px;box-shadow:0 4px 15px rgba(31,55,88,.027)}.kpi b{display:block;font-size:2rem;letter-spacing:-.06em;margin-top:9px}.details{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:14px 0 24px}.item{display:flex;justify-content:space-between;gap:15px;padding:9px 0;border-bottom:1px solid #eef1f5;font-size:.86rem}.item:last-child{border:0}.item span:first-child{word-break:break-word}.meter{width:100%;height:65px;display:flex;align-items:end;gap:5px;border-bottom:1px solid #dde5ee;margin:12px 0 8px}.bar{background:linear-gradient(#799ecc,#456b9f);flex:1;min-width:5px;border-radius:4px 4px 0 0}.table-wrap{overflow-x:auto}table{width:100%;border-collapse:collapse;text-align:left;font-size:.83rem;white-space:nowrap}th{color:#6a778a;font-weight:600;background:#f7f9fc}th,td{padding:12px;border-bottom:1px solid #edf0f4}td:nth-child(4){max-width:230px;overflow:hidden;text-overflow:ellipsis}td:nth-child(5){max-width:170px;overflow:hidden;text-overflow:ellipsis}.table-head{display:flex;gap:15px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:12px}.check{font-size:.82rem;color:#4c5d72;display:flex;gap:8px;align-items:center}.check input{min-width:auto}#app[hidden],#auth[hidden]{display:none}footer{margin-top:28px;color:#7d8998;font-size:.75rem}@media(max-width:720px){main{padding:24px 12px}.kpis,.details{grid-template-columns:1fr}.kpi b{font-size:1.65rem}h1{font-size:1.6rem}}
</style></head><body><main>
<header><div><div class="eyebrow">Yinda Chen / Personal Website</div><h1>Visitor Insights</h1><div class="muted">A private, lightweight view of recent website activity.</div></div><div class="muted" id="updated">Private access only</div></header>
<section class="auth" id="auth"><h2>Enter your dashboard key</h2><div class="muted">Your key is only kept in this browser tab's memory. It is never written to the webpage repository.</div><form id="login" class="login"><input id="key" type="password" autocomplete="off" placeholder="ADMIN_TOKEN" required><button type="submit">Unlock dashboard</button></form><div class="status" id="error" role="status"></div></section>
<div id="app" hidden><div class="kpis"><div class="kpi"><div class="muted">Last 24 hours</div><b id="k24">—</b></div><div class="kpi"><div class="muted">Last 7 days</div><b id="k7">—</b></div><div class="kpi"><div class="muted">Last 30 days</div><b id="k30">—</b></div></div>
<div class="panel"><h2>Activity • Last 14 days</h2><div class="meter" id="chart" aria-label="Daily visitor activity"></div><div class="muted" id="chartCaption"></div></div>
<div class="details"><div class="panel"><h2>Countries</h2><div id="countries"></div></div><div class="panel"><h2>Referrers</h2><div id="sources"></div></div><div class="panel"><h2>Popular pages</h2><div id="pages"></div></div></div>
<div class="panel"><div class="table-head"><h2>Latest visits</h2><label class="check"><input type="checkbox" id="raw"> Show recent raw IPs (private)</label></div><div class="table-wrap"><table><thead><tr><th>Time (UTC)</th><th>IP</th><th>Location</th><th>Page</th><th>Source</th><th>Device</th></tr></thead><tbody id="visits"></tbody></table></div><p class="muted" id="dataPolicy"></p></div></div>
<footer>IP-based location is approximate, and visits are not verified human identities. Do not share your dashboard key.</footer>
<script nonce="${nonce}">
(()=>{'use strict';let token='';const $=id=>document.getElementById(id);const txt=(el,value)=>{el.textContent=String(value??'')};
const get=async path=>{const response=await fetch(path,{headers:{Authorization:'Bearer '+token},cache:'no-store'});if(!response.ok)throw new Error(response.status===401?'Invalid dashboard key.':'Request failed: '+response.status);return response.json()};
const drawItems=(id,items)=>{const host=$(id);host.replaceChildren();for(const item of items){const row=document.createElement('div');row.className='item';const label=document.createElement('span');txt(label,item.label);const count=document.createElement('strong');txt(count,item.count);row.append(label,count);host.append(row)}if(!items.length)txt(host,'No visits yet')};
const drawChart=items=>{const host=$('chart');host.replaceChildren();const today=new Date();const m=new Map(items.map(x=>[x.day,Number(x.visits)]));const days=[];for(let i=13;i>=0;i--){const d=new Date(today.getTime());d.setUTCDate(today.getUTCDate()-i);days.push([d.toISOString().slice(0,10),m.get(d.toISOString().slice(0,10))||0])}const max=Math.max(1,...days.map(x=>x[1]));for(const [day,n] of days){const el=document.createElement('div');el.className='bar';el.style.height=Math.max(2,n/max*100)+'%';el.title=day+': '+n+' visits';host.append(el)}txt($('chartCaption'),days[0][0]+' — '+days[13][0]+' (UTC)')};
const refresh=async()=>{const [summary,recent]=await Promise.all([get('/api/stats'),get('/api/visits?limit=100'+($('raw').checked?'&raw=1':''))]);txt($('k24'),summary.last24h);txt($('k7'),summary.last7d);txt($('k30'),summary.last30d);drawChart(summary.daily);drawItems('countries',summary.countries);drawItems('sources',summary.sources);drawItems('pages',summary.pages);const host=$('visits');host.replaceChildren();for(const row of recent.visits){const tr=document.createElement('tr');const city=[row.country,row.region,row.city].filter(Boolean).join(' · ');for(const field of [row.visited_at,row.ip_raw||row.ip_masked,city,row.page,row.source,[row.device,row.browser,row.os].join(' / ')]){const td=document.createElement('td');txt(td,field);tr.append(td)}host.append(tr)}if(!recent.visits.length){const tr=document.createElement('tr');const td=document.createElement('td');td.colSpan=6;txt(td,'No visits collected yet.');tr.append(td);host.append(tr)}txt($('updated'),'Updated '+new Date(summary.updated_at).toLocaleString());txt($('dataPolicy'),'Raw IP access limited to '+recent.raw_ip_days+' days; logs retained for '+recent.retention_days+' days (UTC).')};
$('login').addEventListener('submit',async e=>{e.preventDefault();token=$('key').value;txt($('error'),'Loading…');try{await refresh();$('key').value='';$('auth').hidden=true;$('app').hidden=false;txt($('error'),'')}catch(err){txt($('error'),err.message);token=''}});
$('raw').addEventListener('change',()=>refresh().catch(e=>txt($('updated'),e.message)));
setInterval(()=>{if(token)refresh().catch(e=>txt($('updated'),e.message))},60000);
})();
</script></main></body></html>`;
  return new Response(html, {
    headers: {
      'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store, private',
      'Referrer-Policy': 'no-referrer', 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff',
      'Content-Security-Policy': `default-src 'none'; script-src 'nonce-${nonce}'; style-src 'nonce-${nonce}'; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'`,
    },
  });
}
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.pathname === '/health' && request.method === 'GET') return replyJson({ ok: true });
    if (url.pathname === '/collect' && request.method === 'POST') return collect(request, env);
    if (url.pathname === '/dashboard' && request.method === 'GET') return dashboard();
    if (url.pathname.startsWith('/api/')) {
      if (request.method !== 'GET') return replyJson({ error: 'Method not allowed' }, 405);
      if (!env.ADMIN_TOKEN || env.ADMIN_TOKEN.length < 32) return replyJson({ error: 'Dashboard not configured' }, 503);
      if (!isAuthorized(request, env)) return replyJson({ error: 'Unauthorized' }, 401);
      if (url.pathname === '/api/stats') return stats(env);
      if (url.pathname === '/api/visits') return visits(request, env);
    }
    return replyJson({ error: 'Not found' }, 404);
  },
  async scheduled(_event, env, ctx) {
    const rawDays = integerInRange(env.RAW_IP_DAYS, DEFAULT_RAW_DAYS, 30);
    const dataDays = integerInRange(env.DATA_RETENTION_DAYS, DEFAULT_RETENTION_DAYS, 365);
    ctx.waitUntil((async () => {
      await env.DB.prepare("UPDATE visits SET ip_raw = NULL WHERE ip_raw IS NOT NULL AND visited_at < datetime('now', ?)").bind(`-${rawDays} days`).run();
      await env.DB.prepare("DELETE FROM visits WHERE visited_at < datetime('now', ?)").bind(`-${dataDays} days`).run();
    })());
  },
};
