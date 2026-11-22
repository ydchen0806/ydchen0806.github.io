/* Minimal, cookieless visitor analytics. Configured only after the Worker is deployed. */
(function () {
  'use strict';
  const script = document.currentScript;
  const endpoint = script && script.dataset.endpoint;
  if (!endpoint || !/^https:\/\//i.test(endpoint)) return;
  const params = new URLSearchParams(location.search);
  try {
    if (params.get('visitor_optout') === '1') localStorage.setItem('yc_visitor_optout', '1');
    if (params.get('visitor_optout') === '0') localStorage.removeItem('yc_visitor_optout');
    if (localStorage.getItem('yc_visitor_optout') === '1') return;
  } catch (_) { /* Private browsing can disable storage. */ }
  if (navigator.globalPrivacyControl === true || navigator.doNotTrack === '1' || window.doNotTrack === '1') return;
  if (navigator.webdriver) return;
  let referrer = '';
  try { if (document.referrer) referrer = new URL(document.referrer).origin; } catch (_) {}
  const data = JSON.stringify({ page: location.pathname, referrer: referrer });
  const target = endpoint.replace(/\/+$/, '') + '/collect';
  try {
    const blob = new Blob([data], { type: 'text/plain' });
    if (navigator.sendBeacon && navigator.sendBeacon(target, blob)) return;
  } catch (_) { /* Fallback below. */ }
  try {
    fetch(target, { method: 'POST', mode: 'no-cors', keepalive: true, headers: { 'Content-Type': 'text/plain' }, body: data }).catch(function () {});
  } catch (_) { /* Do not affect page rendering. */ }
})();
