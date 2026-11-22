# Private Visitor Insights for ydchen0806.github.io

A lightweight Cloudflare Worker + D1 visitor log for the existing GitHub Pages homepage. **The Flag Counter map and Google Analytics stay unchanged.** These files are inert until the Worker is deployed and its endpoint is added to the Jekyll configuration.

## What it provides

- An owner-only dashboard at the deployed Worker URL ending in /dashboard with 24-hour, 7-day, 30-day counts, activity trend, popular pages, countries, and referral domains.
- Up to 100 recent visits with UTC time, country/region/city, page path, device, browser and OS.
- Masked IPs by default; private short-term display of exact IPs for 3 days (then removed). Other visit records expire after 30 days.
- No cookies, full user-agent logging, URL query storage or browser fingerprinting. The tracker respects GPC/DNT and supports a browser-based opt-out.

## Deploy once

Prerequisites: a Cloudflare account and Node.js. Run the following in the visitor-analytics directory.

1. Install dependencies: npm install
2. Authenticate: npx wrangler login
3. Create D1 database once: npx wrangler d1 create yinda-visitor-logs
4. Copy the returned database_id into wrangler.jsonc, replacing REPLACE_WITH_YOUR_DATABASE_ID.
5. Initialize the remote database: npx wrangler d1 migrations apply yinda-visitor-logs --remote
6. Deploy: npx wrangler deploy. Note the printed HTTPS address, usually https://yinda-visitor-analytics.YOUR-SUBDOMAIN.workers.dev
7. Generate a private 64-character random admin key on your own computer: openssl rand -hex 32. Store it in a password manager. Set it with: npx wrangler secret put ADMIN_TOKEN (paste only at the local terminal prompt).
8. Visit the Worker URL ending in /health, then visit /dashboard and unlock with your key.
9. In the homepage repository's _config.yml, change visitor_analytics_endpoint from an empty string to the Worker HTTPS root URL. Commit that change. The tracker will load automatically after GitHub Pages rebuilds.
10. Open the homepage once (without GPC/DNT or opt-out) and check that the visit appears in /dashboard. Existing map and GA continue independently.

Run automated tests with npm test.

**Warning:** Do not place the admin key in GitHub, HTML, JavaScript or public CI output. Do not enable Cloudflare Access for the *entire* Worker: that would block the public /collect endpoint. For extra access control, apply path-specific Cloudflare Access rules to /dashboard and /api/*, leaving /collect public. The /api/* paths independently require the secret key.

## Retention and privacy

The daily 03:00 UTC cron task deletes exact IPs older than RAW_IP_DAYS (default 3) and visits older than DATA_RETENTION_DAYS (default 30). For safety, the private API also hides expired exact IPs even if the scheduled cleanup has not yet run. The tracker sends only the path without query parameters and the referrer origin, not the full referrer URL. The Worker stores only the referral hostname.

Opt out in a browser at https://ydchen0806.github.io/?visitor_optout=1 and re-enable at ?visitor_optout=0. These switches affect only the optional custom tracker, not the independent Flag Counter or Google Analytics services. The site's public /privacy/ page describes collection.

The Origin header helps reduce accidental cross-site events but is not security authentication. Anyone can forge it outside a browser, so traffic figures are approximate. Locations inferred from IP addresses are also approximate, not identities. Existing historical Flag Counter logs cannot be reconstructed. Inspect runtime errors with npx wrangler tail, but do not log raw visitor IP addresses during debugging.
