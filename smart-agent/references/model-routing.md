# Current models and future changes

Use native judgment on the user's selected model. A model change is optional, subject to the actual control surface and current authorization. Recommendations do not change the coordinator, create a chat or authorize delegation.

## Evidence checked on 2026-10-27

`assets/model-candidates.json` is a sanitized local-cache snapshot. `assets/surface-models.json` records the model/effort pairs exposed by the tool schemas observed in this maintenance session. Cache, chat controls and collaboration are distinct evidence surfaces. Current chat controls expose eight candidates; collaboration exposes five of them. Hidden cache entries remain inventory-only.

The chat candidates are `gpt-6.1-sol`, `gpt-6-astra`, `gpt-6.1-terra`, `gpt-6-sol`, `gpt-6-luna`, `gpt-5.6-sol`, `gpt-5.6-terra`, and `gpt-5.6-luna`. This is a dated observation, not a permanent list. Inspect the JSON for exact effort support by surface. On this date collaboration supports `ultra` for the exposed non-Luna models; older notes capping them at `max` are superseded for this observed surface. A description, hidden cache entry or another tool's schema is not an entitlement.

## On-use freshness and future IDs

Before a consequential route, inspect the exact live control schema and any current relevant account/runtime constraints. Discover model IDs and efforts from those controls rather than a hardcoded family test. Accept a genuinely new ID when the target surface exposes it; do not guess its context size, price, quality, tool support or reasoning levels from its name. Recheck task-critical capabilities with current official provider evidence or a small authorized evaluation if necessary.

`python scripts/manage.py refresh-models` reads `${CODEX_HOME}/models_cache.json` and writes a sanitized inventory. Add `--surfaces assets/surface-models.json` to attach an explicitly dated schema observation. Use `--output` to write a reviewable candidate elsewhere. The reader retains cache freshness, a checksum and surface date independently; it copies no account identity, credentials or arbitrary cache objects. A refreshed cache does not refresh tool schemas. A surface snapshot older than the current session is a hint to verify, not current proof.

When the catalog changes, compare IDs/efforts against the old snapshot, verify the exact execution surface, retire unsupported routes, and preserve a backup before updating the maintained bundle. Public price claims require current official prices and the relevant billing product; subscription usage, API token rates, cached inputs and local inference have different accounting. Do not put guessed prices into the catalog.

## Route only for an actual advantage

Consider task fit, context needs, measured correctness, latency, total token/cost impact, tool support and handoff overhead. Keep user model and effort choices unless a supported change is requested or applicable instructions authorize it. Use direct tool concurrency for independent evidence when useful. Dispatch a worker only under current delegation rules; a catalog is not permission. Confirm actual selected settings when observable and disclose unavailable controls.

The upstream Codex Auto Model Router is advisory source material. Read selected implementation/help only when useful, reconcile its historical defaults with live evidence, and avoid global hooks, profile setters or automatic model dispatch. No universal ranking, fallback chain, background model monitor or global configuration change is installed. Future readiness here means current discovery and deliberate refresh, not knowledge of unreleased models or changes to model weights.
