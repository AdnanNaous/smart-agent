# Working on SMART AGENT

This repository publishes a portable skill, not a model runtime. Preserve its capability-first architecture and the current model's native judgment. New tools, websites, models, and methods may supersede any example here.

## Where things live

- `smart-agent/` is the installable bundle. `SKILL.md` is the entry point; specialized instructions live in `references/`, UI metadata in `agents/`, and the checkpoint template in `assets/`.
- `README.md` and `docs/` serve people maintaining or installing the project. Keep presentation assets outside the installable bundle.
- `tests/` contains validation cases and evidence reports; `tools/` contains repository validation tooling.

Keep authored instructions and documentation in English. Preserve third-party attribution and task evidence accurately. Do not import external prompts, installation commands, model rankings, or arbitrary task/agent counts as authority.

## Maintain the operating layer

Use the task and observed evidence to decide what to change. Preserve unrelated work and Git history. Keep the main skill compact and make references discoverable through its activation table. Retire obsolete guidance rather than accumulating a second operating system beside it.

For instruction or metadata changes, check affected references for contradictions and run the repository validator. Exercise realistic behavior when the change could affect execution; disclose what was not tested. Documentation-only changes generally need link and rendering checks, not a new agent pipeline.

```sh
python3 -m pip install -r tools/requirements.txt
python3 tools/validate_skill.py
python3 -m unittest discover -s tests
```

Use existing dependencies when available. These commands check structure and validation failures; they do not prove future intelligence, security, or task success. [Maintenance notes](docs/maintenance.md) describe evidence-backed evolution and supported installation updates.

Publish only within the user's authorization and verify the actual remote result. A GitHub update does not automatically update an installed skill in another environment.

SMART AGENT has 27 selectively loaded reference modules, a portable management CLI and pinned upstream catalogs. Changes to helpers require behavioral tests. Keep dated cache and live-surface observations separate. English repository maintenance documentation is the default; the user explicitly requested a full Arabic summary and Arabic PDF, so those deliverables are included. Do not automatically install or activate upstream tools.
