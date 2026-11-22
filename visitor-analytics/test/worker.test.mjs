import test from 'node:test';
import assert from 'node:assert/strict';
import worker from '../src/worker.js';

function fakeDB() {
  const calls = [];
  const db = {
    calls,
    prepare(sql) {
      let values = [];
      const stmt = {
        bind(...args) { values = args; return stmt; },
        async run() { calls.push({ sql, values }); return { success: true }; },
        async first() { return { value: 2 }; },
        async all() { return { results: [] }; },
      };
      return stmt;
    },
  };
  return db;
}
const token = 'a'.repeat(64);
function env() { return { DB: fakeDB(), SITE_ORIGIN: 'https://ydchen0806.github.io', ADMIN_TOKEN: token, RAW_IP_DAYS: '3', DATA_RETENTION_DAYS: '30' }; }
function event(origin = 'https://ydchen0806.github.io', body = { page: '/research?email=user@example.com', referrer: 'https://scholar.google.com/citations?x=secret' }) {
  const req = new Request('https://worker.example/collect', { method: 'POST', headers: { Origin: origin, 'Content-Type': 'text/plain', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/605.1.15 Version/18.0 Safari/605.1.15', 'CF-Connecting-IP': '203.0.113.24' }, body: JSON.stringify(body) });
  Object.defineProperty(req, 'cf', { value: { country: 'US', city: 'Boston', region: 'MA' } });
  return req;
}
test('health endpoint', async () => {
  const res = await worker.fetch(new Request('https://worker.example/health'), env());
  assert.equal(res.status, 200);
  assert.deepEqual(await res.json(), { ok: true });
});
test('rejects collect events from another origin', async () => {
  const e = env();
  const res = await worker.fetch(event('https://attacker.example'), e);
  assert.equal(res.status, 403);
  assert.equal(e.DB.calls.length, 0);
});
test('stores sanitized path, referrer host and masked IP', async () => {
  const e = env();
  const res = await worker.fetch(event(), e);
  assert.equal(res.status, 204);
  assert.equal(e.DB.calls.length, 1);
  const args = e.DB.calls[0].values;
  assert.equal(args[1], '203.0.113.*');
  assert.equal(args[2], '203.0.113.24');
  assert.equal(args[3], 'US');
  assert.equal(args[6], '/research');
  assert.equal(args[7], 'scholar.google.com');
  assert.equal(args[8], 'Safari');
});
test('private API rejects absent or invalid tokens', async () => {
  for (const auth of [undefined, 'Bearer wrong']) {
    const headers = auth ? { Authorization: auth } : {};
    const res = await worker.fetch(new Request('https://worker.example/api/stats', { headers }), env());
    assert.equal(res.status, 401);
  }
});
test('private API returns dashboard information after login', async () => {
  const e = env();
  const headers = { Authorization: 'Bearer ' + token };
  const a = await worker.fetch(new Request('https://worker.example/api/stats', { headers }), e);
  assert.equal(a.status, 200);
  assert.equal((await a.json()).last24h, 2);
  const b = await worker.fetch(new Request('https://worker.example/api/visits?raw=1', { headers }), e);
  assert.equal(b.status, 200);
  assert.equal((await b.json()).raw_ip_days, 3);
});
test('dashboard HTML contains no private data and has CSP', async () => {
  const r = await worker.fetch(new Request('https://worker.example/dashboard'), env());
  assert.equal(r.status, 200);
  assert.match(r.headers.get('Content-Security-Policy'), /nonce-/);
  const html = await r.text();
  assert.match(html, /Visitor Insights/);
  assert.match(html, /type="password"/);
  assert.doesNotMatch(html, /203\.0\.113\.24/);
});
test('daily scheduled cleanup removes expired raw IP and event records', async () => {
  const e = env(); const tasks = [];
  await worker.scheduled({}, e, { waitUntil: promise => tasks.push(promise) });
  await Promise.all(tasks);
  assert.equal(e.DB.calls.length, 2);
  assert.deepEqual(e.DB.calls.map(c => c.values[0]), ['-3 days', '-30 days']);
});
