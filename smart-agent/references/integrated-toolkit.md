# Integrated toolkit

Use this reference to find a specific workflow, skill, or implementation guide from the sources the user requested. These are selectively integrated source libraries, not mandatory workflows. The installed Meowa skill is also independently discoverable. Keep one coordinator and read only material that changes the next decision.

## Local discovery

`../assets/toolkit-sources.json` records source URLs, checked-out commits, licenses, local roots, and catalog patterns. `../assets/toolkit-index.json` indexes the primary skills, studio workflows, and selected Blender guides. Complete upstream repositories, supporting scripts, assets, and license files remain in `${CODEX_HOME}/skill-sources/agent-engineering-os/`; Blender is at `C:/blender_mcp` as requested. Nothing in these source directories is automatically executed by this skill.

Run `scripts/toolkit.py` relative to the skill folder using a working Python 3.10+ interpreter. This installation has a dedicated interpreter at `${CODEX_HOME}/skill-runtimes/agent-engineering-os/Scripts/python.exe`. In PowerShell invoke a quoted executable with `&`.

```powershell
& '<python>' '<skill>/scripts/toolkit.py' search 'godot input'
& '<python>' '<skill>/scripts/toolkit.py' search 'vertical-slice' --source codex-game-studio
& '<python>' '<skill>/scripts/toolkit.py' search 'accessibility' --source ui-skills
& '<python>' '<skill>/scripts/toolkit.py' read '<exact id from search>'
& '<python>' '<skill>/scripts/toolkit.py' check
& '<python>' '<skill>/scripts/toolkit.py' models
```

`search` uses all supplied words, `--limit` bounds output, and IDs include the source and relative file path. Read sibling references/assets using the returned source path. `read` checks the indexed content hash; `check` checks source revisions and all indexed files. A missing library is a specific integration limitation, not a reason to stop unrelated work. `refresh` rebuilds the local index without network access after an intentional, reviewed source update; it never pulls, installs, or executes upstream code.

## Select the source

| Source | Useful material | Adaptation in this skill |
| --- | --- | --- |
| [Codex Auto Model Router](https://github.com/orange-the-weak/codex-auto-model-router) | Optional route advice, direct tool concurrency, routing profiles and execution evidence | Use [model-routing.md](model-routing.md). Respect current delegation policy, selected models, and live model IDs; its old effort caps and rankings are not universal. No global hook installed. |
| [UI Skills](https://github.com/ibelick/ui-skills) | `improve-ui`, `baseline-ui`, accessibility, metadata, motion performance, component/canvas exploration | Preserve the actual stack and visual brief. Stack preferences, one-accent rules, gradient bans, and animation bans in individual prompts are defaults to assess, not global requirements. |
| [gstack](https://github.com/garrytan/gstack) | Product framing, architecture review, design critique, evidence-backed review, browser QA and release planning | Use its questions and review lenses selectively. This is an instruction/reference integration; its Bun binaries, browser runtime, hooks, telemetry, cookie import and cross-model CLIs are not installed or activated. |
| [Awesome Gamedev Agent Skills](https://github.com/gamedev-skills/awesome-gamedev-agent-skills) | Engine, genre and discipline skills; art production, fast prototypes, jams and publishing guides | Load the matching engine/version and task. Do not install or load every engine. Its version pins must be compared with the real project. |
| [Meowa skills](https://github.com/Meowa-AI/meowa-skills) | Installed `game-assets` runner, art, animation, audio and asset preparation guides | Complete skill installed at `~/.agents/skills/game-assets/`. Read it when using its CLI. Remote generation requires account access; installation is not a successful generation. |
| [Blender MCP](https://projects.blender.org/lab/blender_mcp) | Blender Python/manual search, scene summaries, viewport capture, execution and export support | Repository at `C:/blender_mcp`; Python server installed in the dedicated runtime. A compatible Blender application, enabled add-on and connected MCP client remain separate prerequisites. |
| [Codex Game Studio](https://github.com/merlinhu1/codex-game-studio) | `.agents/skills`, `.codex/workflows`, engine references and production templates | Use selected workflows in an existing project without overwriting its instructions. Treat agents and fixed model frontmatter as optional source templates; no studio was initialized and no roles were dispatched. |

## UI and review integration

For UI implementation or polish, inspect the existing interface and pick a concrete direction. Use UI Skills for the relevant concern, such as focus management, readable hierarchy, truthful loading/error states, clipping, safe areas, or animation cost. Keep the project's primitives and tokens; introduce a UI library only when its benefit justifies the dependency. Test rendered behavior, keyboard and touch as applicable. Browser DOM rules do not substitute for engine-native game HUD input and accessibility.

For substantial engineering decisions, gstack offers useful product, engineering, design, review, and QA lenses. A review should identify a reproducible trigger, affected path and user consequence. A QA pass should exercise actual interactions and failure states. Keep read-only review requests read-only; automated fix or ship language inside an upstream prompt does not change the user's request. Scale review depth to the change and use the tools actually exposed in this runtime.

Full gstack setup is a separate option when its executable tools are wanted. Inspect its current `docs/install.md` and `docs/hosts.md` first: Codex host support is experimental and outside reviews can require another authenticated CLI. Do not claim hooks or browser automation work merely because Markdown is available.

## Maintenance and provenance

Review source changes before updating pins or regenerating the index. Preserve local changes and upstream license files; avoid running broad installers to refresh documentation. Keep source-specific constraints in adapters instead of concatenating incompatible prompts into `SKILL.md`. Do not distribute upstream code or assets without preserving the relevant notices. The Blender attachment and repository have different version metadata; see [game-assets-and-blender.md](game-assets-and-blender.md).

## SMART AGENT additions

The 2026-10-27 update adds pinned Three.js, Agent Beacon, Atlas Components, Superpowers, Headroom and PixelRAG sources. Read [web-3d-and-assets.md](web-3d-and-assets.md) for Three.js, Atlas and Open3DLab; [token-efficiency.md](token-efficiency.md) for Headroom; and [memory-and-visual-retrieval.md](memory-and-visual-retrieval.md) for Beacon, PixelRAG and Superpowers. Open3DLab and the Three.js website are recorded in `assets/integration-sites.json`; websites have no Git pin or blanket asset license.

Portable roots in the manifest resolve `${CODEX_HOME}` at runtime. Existing source and runtime paths may retain the former skill name. Source references and adapters are available locally; optional source runtimes are not thereby installed or tested. Use the module registry to discover guidance instead of loading every library.

Priority reverse-engineering sources: [reverse-toolchains.md](reverse-toolchains.md) adapts pinned reverse-skill and REA guides, case scope and retained-evidence workflows without bootstrapping tools or dispatching agents.
