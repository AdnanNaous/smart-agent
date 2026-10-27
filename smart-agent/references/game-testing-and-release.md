# Game testing, performance and release

Choose checks from the changed behavior, target platforms and consequence of failure. Use [GAME_QA.md](../assets/GAME_QA.md) as an optional compact record; do not turn a small tuning edit into a release audit. Use the source catalog for engine tests/export, input systems, saves, performance, playtest, soak-test and release guides.

## Player-facing verification

Launch the actual project or packaged game and exercise the affected loop. Cover the relevant transitions: boot/menu, start/load, gameplay, pause/resume, failure, respawn, checkpoint, victory/ending/replay, restart and quit. Record what was actually played, with engine version, entry scene/build and useful logs or captures. Headless checks, compilation, screenshot review and template validation each prove only their own boundary.

| Area | Meaningful checks when relevant |
| --- | --- |
| Input | Keyboard/mouse, controller and touch action mappings; menus and gameplay; remapping/dead zones; device disconnect; held inputs across state changes; browser pointer lock and focus loss. |
| Movement/physics | Jump/landing, slopes/edges, variable frame time, high speed, moving platforms, collision layers, triggers, spawn overlap and out-of-bounds recovery. |
| Damage/state | Death and invulnerability, respawn damage windows, simultaneous events, pause/time-scale changes, animation cancellation and ending/replay state. |
| Saves | Round-trip load, atomic writes, concurrent/interrupted saves where possible, corrupted/missing/old versions, fresh profile, checkpoint consistency and idempotent rewards. Preserve user saves during testing. |
| UI/accessibility | Legibility at gameplay scale, navigation focus, contrast, text scaling, subtitles where needed, localization/RTL when requested, safe areas, reduced motion/flashes and adjustable effects. |
| Content | Required stages reachable and distinct, progression/unlocks, collision and spawn fairness, correct scene transitions, intentional audio and missing-asset detection. |
| Lifecycle | Alt-tab, focus loss, resize, minimize/resume, scene cleanup, repeated runs and recovery after interruption. |

For regressions, reproduce the fault and test a minimal boundary that would fail before the fix. Prefer deterministic mechanics tests for repeatable rules, scene/integration tests for cross-system behavior, and playthroughs for feel and rendering. Test real save/storage and package paths when they are affected. Do not trust aggregate CI counts or agent reports as a substitute for the missing player path.

## Performance and device evidence

Set a target from the actual hardware/display and game brief. Measure frame time as well as average FPS, especially during loading, combat, effects and scene changes. Inspect CPU/GPU work, memory, draw calls, texture/mesh budgets, allocations and loading stalls using available profilers. Optimize the measured bottleneck; avoid speculative engine rewrites or blanket visual reductions.

For web/mobile, exercise representative viewport sizes, orientation changes, touch hit targets, loading and memory pressure, and renderer/audio restrictions. Desktop emulation is useful but does not prove a physical phone's thermals, touch feel, GPU behavior or store packaging. For native games, separate editor performance from exported-player performance. Record unavailable devices as untested rather than extrapolating a pass.

## Packaging and release

Build the requested target using the real export preset/toolchain. Launch the produced artifact from its output directory, verify entrypoint and bundled dependencies, and test saves/configuration under the packaged application. For portability claims, test without editor-only assumptions, workspace-relative paths or undeclared external files. Inspect assets, notices, platform metadata and required permissions. Keep packages and manifests aligned; verify checksums against the exact distributed bytes when producing integrity metadata.

Use source workflows such as Game Studio's `ship-check`, `release-checklist` or Awesome Gamedev's itch/Steam guides only for requested release work. These guides do not authorize store uploads, account actions, purchases, public previews or publication by themselves. Prepare the concrete package and metadata first, then follow the user's existing publication authorization and actual platform controls.

Report implementation, automated checks, runtime play, packaged launch and physical-device coverage separately. Include the delivered artifact, controls/launch path and any material blocker. "Release ready" requires evidence for the relevant release paths, not merely a successful build.
