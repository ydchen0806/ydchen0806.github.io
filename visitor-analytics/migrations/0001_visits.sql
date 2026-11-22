-- Retention is enforced by the Worker's scheduled daily cleanup.
CREATE TABLE IF NOT EXISTS visits (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  visited_at TEXT NOT NULL,
  ip_masked TEXT NOT NULL,
  ip_raw TEXT,
  country TEXT NOT NULL,
  region TEXT NOT NULL,
  city TEXT NOT NULL,
  page TEXT NOT NULL,
  source TEXT NOT NULL,
  browser TEXT NOT NULL,
  os TEXT NOT NULL,
  device TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS visits_recent_idx ON visits(visited_at DESC);
CREATE INDEX IF NOT EXISTS visits_country_idx ON visits(country, visited_at);
