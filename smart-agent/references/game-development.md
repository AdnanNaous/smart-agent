# Game development workflow and engine guides

Use for a playable game, level, mechanic, engine integration or substantial game continuation. A focused fix needs only its relevant parts. Consult [game-assets-and-blender.md](game-assets-and-blender.md) and [game-testing-and-release.md](game-testing-and-release.md) when their concerns apply.

## Start from the real project

For continuation, reconcile the checkpoint with the live checkout, engine/project version, actual scenes and assets, build configuration, and existing evidence. Preserve working content, saves and art direction. Establish the player-facing outcome: core verb, camera, genre, target devices, control schemes, session length, visual direction and delivery format. Infer routine choices from the project. Ask only about decisions that materially change the product and cannot be inferred.

For a new game, define a small playable promise before producing a large design document. Examples: a jump-and-dash room with readable hazards; a combat encounter with telegraphed attacks; a puzzle with a learnable rule and a clear solved state. Use [GAME_BRIEF.md](../assets/GAME_BRIEF.md) only when persistent coordination benefits from it. Choose scope that can be built and validated; do not replace the user's real-game request with a concept deck or decorative landing page.

## Engine and source selection

Keep an existing engine and language. For a new project, compare deployment, team familiarity, 2D/3D needs, editor availability, asset pipeline, hardware and licensing. Verify installed versions and export support before committing to a platform. These are guides, not engine rankings:

| Track | Match source material through `toolkit.py search` | Decisions to verify |
| --- | --- | --- |
| Godot | `godot-nodes-scenes`, GDScript/C#, movement, signals, physics, UI, shaders, export, headless testing | Engine/.NET compatibility, input actions, resources, scene ownership, import and export templates. |
| Unity | C# scripting, Input System, physics, animation, ScriptableObjects, build pipeline; installed Unity plugin skills when relevant | Project Unity version, render pipeline, package compatibility, scene/prefab state, player build settings. |
| Unreal | Blueprints, C++ gameplay, Enhanced Input, behavior trees, Niagara and packaging | Engine/toolchain version, assets/references, input mapping, cook/package target and performance. |
| Browser | Phaser/PixiJS or Three.js scene, materials and glTF guides | 2D versus 3D needs, renderer support, pointer lock/audio activation, touch, resize, loading, local server and deploy target. |
| Other engines | Ebitengine, Bevy, pygame, LÖVE, Defold, Roblox | Existing stack and supported runtime, API versions, lifecycle, packaging and platform-specific behavior. |

Read one engine skill plus the relevant genre or discipline as needed. Check each source's version assumptions against the project and official docs. A C# compilation or headless scene check does not prove editor import, rendering, input or packaged behavior.

## Build a representative playable slice

Use a compact loop: player intent → response → consequence → readable feedback → retry or progress. Build the mechanic and its camera, collision, state transitions and feedback together. Use placeholders when they accelerate proving a mechanic, and mark them clearly. Replace them as the agreed visual target becomes stable.

For platforming, consider acceleration, braking, jump arc, coyote time, input buffering, wall/ledge behavior and recovery. For combat, consider wind-up, active/recovery windows, hit confirmation, invulnerability, enemy telegraphs and damage rules. For puzzles, ensure rules and reset behavior are learnable. For strategy or simulation, verify time controls, resource accounting and readable state. Load the matching genre guide rather than imposing every mechanic everywhere.

Keep simulation state separate from presentation where it improves reliability. Use bounded state machines, engine-native scene/entity lifecycles, data-driven tuning and deterministic seeds where useful. Handle pause, death, respawn, victory, checkpoint reload, restart and quit as real flows. Avoid introducing online services, analytics, monetization or multiplayer unless the requested game needs them.

## Levels, worlds and feel

Make stages distinct through topology, traversal/combat rhythm, a taught mechanic, encounter behavior, goals, environmental interaction and art direction. A palette change alone is weak evidence of a different world. Introduce an idea in a readable space, develop it, combine it, then provide a satisfying test. Keep landmarks, foreground/background separation, silhouette, camera framing and telegraphs clear at gameplay scale.

Tune input and camera with actual play. Use world-space feedback, animation, particles, sound and motion deliberately; keep shake, flashes and effects adjustable when relevant. Preserve a requested silent or reduced-motion experience. Give each required input mode a usable path through gameplay and menus. Share action semantics across keyboard/mouse, controller and touch, while adapting prompts, aiming, dead zones and layout to the device.

## Codex Game Studio integration

The source library supplies design, architecture, prototype, vertical-slice, art-bible, asset-spec, game-feel-tuning, playtest, QA, performance, release and handoff material. Search source `codex-game-studio`, then read the selected workflow and linked `cgs-*` skill. Use templates only when they help the current project. Do not require its entire agent roster or document set.

For an existing game, adopt useful workflows manually without replacing `AGENTS.md`, `.codex` configuration or project structure. The source template's fixed model frontmatter and old fallbacks do not establish current model availability; use [model-routing.md](model-routing.md). No studio initialization is needed to use these guides.

For a user-requested studio workspace, copy the pinned template into a new dedicated directory, preserve the source library, inspect the CLI and project instructions, install its locked dependencies, and inspect supported options. Its `init` command can prune maintainer-only source and tests; do not run it on the preserved source checkout or an existing game as a casual setup step. Use preview/dry-run facilities for role execution where offered. Roles are optional coordination, not evidence that work happened.

## Progress and handoff

Finish useful increments in the running game before expanding content. Keep active scene/entrypoint, controls, tuning changes, source assets and build instructions discoverable. Record the tested build/commit and actual runtime evidence. For larger work, use the existing continuity checkpoint plus a short playable milestone and unresolved risks. A production board or agent report does not substitute for launching and playing the delivered build.
