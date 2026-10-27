# SMART AGENT module management

Use this guide to navigate, configure or maintain this consolidated skill. One coordinator owns the outcome; modules are conditional references, not independent agents or mandatory phases.

## Inventory and selection

`assets/modules.json` is the module registry: stable ID, purpose, keywords, reference, related modules, default enablement, and validation expectation. `assets/toolkit-sources.json` pins upstream libraries; `assets/toolkit-index.json` contains searchable metadata and content hashes. `assets/integration-sites.json` records websites that cannot be pinned as Git repositories. Source libraries remain outside the active skill folder.

Run Python 3.10+ from the skill root, or pass absolute script paths:

```text
python scripts/manage.py list
python scripts/manage.py recommend "Arabic RTL accessible dashboard"
python scripts/manage.py show web-3d
python scripts/manage.py disable visual-retrieval
python scripts/manage.py enable visual-retrieval
python scripts/manage.py doctor
python scripts/toolkit.py search "systematic debugging" --source superpowers --limit 5
python scripts/toolkit.py read "superpowers:skills/systematic-debugging/SKILL.md"
python scripts/toolkit.py check
```

`recommend` matches registry words and returns a bounded shortlist. Interpret it with native judgment; an empty result is not a capability limit. `enable` and `disable` affect this skill's module suggestions only. They never install/uninstall tools or weaken authorization, security or verification requirements. State lives in `${CODEX_HOME}/skill-state/smart-agent/modules.json`, outside the portable bundle. `SMART_AGENT_STATE` overrides that file for isolated testing. `CODEX_HOME` defaults to `~/.codex`.

Before selecting optional guidance, inspect the module state when relevant; do not run management commands for every simple task. Load one relevant guide, then another only if a concrete dependency or uncertainty calls for it. Explicit user requests take precedence over advisory module state; explain an override if material. `show` returns metadata even for disabled modules. No command starts agents or changes the selected model.

## Module lifecycle

Add a module only for a distinct recurring decision. Write a concise adapter, add its registry entry and entrypoint link, record its source and license, exercise its actual helper behavior, and validate links. Merge overlapping guidance rather than multiplying skill folders. Retire a module through disablement or a reviewed removal after checking callers; preserve useful work in a backup.

Use `doctor` for local reference integrity and source presence; use `toolkit.py check` for source pins, indexed file hashes and preserved notices. Missing optional libraries should be reported without preventing unrelated work. Source code presence does not establish installed dependencies, authenticated services or a functioning application.

## Safe maintenance

Inspect the installed bundle and current repository separately. Back up before migration, keep one active personal coordinator, preserve Git history, and verify installed-versus-published contents. For upstream updates, inspect changes in a separate checkout, review licensing and behavioral changes, update the pin deliberately, then rebuild the offline index. `toolkit.py refresh` never fetches or executes upstream code and must not be used to silently bless unexpected modifications.

Portable manifests use `${CODEX_HOME}` roots. Older library and runtime directories may retain the historical `agent-engineering-os` name to preserve working dependencies. This is storage compatibility, not a second active skill. Use `scripts/fetch_sources.py --source <id>` to acquire an exact recorded revision in an empty destination. It performs network Git operations only when explicitly invoked, rejects an existing target, and does not run installers or hooks from source content. Rebuild the offline index after retrieval. A sparse local source snapshot is sufficient for guidance; it is not a tested product installation.

## Model freshness

Use [model-routing.md](model-routing.md) before a consequential model decision. Refresh the local cache snapshot with `manage.py refresh-models --surfaces assets/surface-models.json`. The cache and surface observation retain separate dates. Updating one never claims to refresh the other. Replace the surface file only from current tool schemas or current explicit capability evidence. An unavailable route is a limitation to disclose; never simulate a model switch.

## Evidence and rollback

Keep technical maintenance results and measurements project-local. Retain the prior bundle or commit until validation completes. Roll back a faulty module, source pin or helper independently. Updating this skill is not permission to alter global agent configuration, capture histories, schedule background jobs, train models, publish projects or write personal memory. Follow the current task and runtime permissions for those operations.

For provider-independent catalogs, use [universal-model-support.md](universal-model-support.md) and `scripts/models.py`. Provider registries remain local outside the bundle; the shipped neutral example is synthetic. Model checks preserve unknown capabilities, stale observations and execution limits.
