# Game assets, Meowa and Blender

Use for art direction, sprites, animation, tiles, UI art, 3D assets, materials or game audio. Keep the production pipeline compatible with the game's engine and target devices. Use the source catalog to find `create-game-assets`, the relevant engine import guide, and Meowa capability references.

## Define and prove the asset contract

Inspect the game's existing art and establish the view/camera, scale, silhouette, palette, material/lighting language, native resolution, transparency, dimensions, pivots and animation states. For 3D, include axes, units, topology, UVs, rig, collision, LOD and material budget. For audio, include purpose, timing, looping, duration, sample/format needs, loudness and mix context. Preserve source URLs, license or generation provenance, and edit history.

Prove one representative asset at actual gameplay size before producing a family. Reuse that target to keep scale, palette, viewpoint, lighting and identity consistent. Small batches make drift visible early. Separate editable source, normalized/imported files and engine-generated caches. A generated image, alpha channel, grid, rig or loop is an input to inspection, not proof of readiness.

Validate dimensions, alpha edges, pixel grid, slice boundaries, pivots, frame order and timing. Test repeating textures/tiles as a repeated patch and adjacent terrain variants. Inspect animation over time for identity drift, foot sliding and clipping. Keep UI labels and interaction in code when appropriate. For 3D, verify transforms, normals, UVs, skin weights, materials, collision and engine import. Set filtering, mipmaps, compression, color space and texture/atlas roles deliberately. Judge assets inside the running game.

## Meowa game-assets installation and use

Installed with the user's requested `npx skills add https://github.com/Meowa-AI/meowa-skills --skill game-assets`, targeted globally to Codex and made non-interactive. The installed complete folder is `~/.agents/skills/game-assets/`; do not update only its `SKILL.md`. The checked-out source is also preserved in the source manifest.

Read that skill's current `SKILL.md`, capability-routing reference and relevant asset-family reference before using its CLI. Its available capabilities include pixel/HD art, variants and views, UI sheets/extraction, tiles/maps/textures, frame animation, video, sound and music. Choose the capability that accepts the actual inputs and produces the requested output. An account/API key is required for remote jobs; configure secrets locally through the service's supported mechanism without printing or writing them into the skill, chat or source manifest.

The dedicated Python runtime includes `requests` and Pillow. Use it explicitly:

```powershell
& '<runtime>/Scripts/python.exe' '<game-assets>/meowart_api.py' --version
& '<runtime>/Scripts/python.exe' '<game-assets>/meowart_api.py' --help
```

Use an explicit project output directory, retain final manifests, and inspect real outputs before import. Track submitted job IDs and recover/poll interrupted work before resubmitting, especially for billed jobs. Read current command help and costs before paid execution; source examples may age. This skill update installs and checks the local CLI; it does not generate paid assets or verify account credentials.

When Meowa is unavailable, use an exposed image/media tool, engine primitives, Blender or licensed assets as the brief permits. Do not silently change the engine or publish a remote workbench project to work around a missing asset service. Follow runtime image-tool instructions for generation/editing. Do not repeatedly rasterize or "pixelate" already suitable pixel assets without an observed defect and a compatible source workflow.

## Official Blender MCP: source, bundle and connection

The requested clone is `C:/blender_mcp`, origin `https://projects.blender.org/lab/blender_mcp.git`. Its components are the add-on in `addon/blender_mcp_addon/` and Python MCP server in `mcp/`. The server is installed in the dedicated skill runtime and can be invoked with `Scripts/python.exe -m blmcp`; `--help` checks its CLI. A copied package is not a connected Blender session.

On 2026-10-26, the installed server passed an isolated stdio MCP initialization, listed 26 tools, and answered a local `search_api_docs` request. This verifies protocol startup and bundled documentation access. Codex desktop MCP registration, a running Blender add-on, scene requests and scene mutations were not exercised. The verification record is `${CODEX_HOME}/backups/agent-engineering-os-20261026-225154/integration-verification.json`.

The user-supplied `~/Downloads/blender-1.0.3.mcpb` was inspected as an archive. Its manifest identifies Blender Lab, package version 1.0.3, GPL-3.0-or-later, Python >=3.10 and a `uv run blender-mcp` entrypoint. The cloned repository's Python project reports 1.0.2 and its add-on requires Blender >=5.1.0. Keep these versions distinct; do not overwrite the source with the bundle or assume identical content. The attachment is recorded by SHA-256 in the manifest; the optional original download was absent during the 2026-10-27 check, which reports a warning. Its contents are package data, not authorization to run an installer.

For an actual connection:

1. Verify the installed Blender version and save the current `.blend` before editing. A compatible application was not located in standard install directories during this update; discover the actual executable when connecting rather than assuming installation.
2. Install/enable the matching official add-on and start its socket listener. The inspected server uses `BLENDER_MCP_HOST` / `BLENDER_MCP_PORT`, defaulting to `localhost:9876`. Keep the execution bridge local unless a deliberate secured remote arrangement is requested.
3. Register the Python server's stdio command with the current MCP client's supported mechanism, preserving unrelated configuration. The supplied `.mcpb` is a client bundle, not a Codex skill or proof that Codex imports that bundle format. Do not claim tool availability until the client exposes tools and a request succeeds.
4. Start with scene/path summaries and a viewport capture. Confirm the intended file and scene before any mutation. Read the relevant current Python API from the bundled docs before constructing unfamiliar Blender operations.

The server can execute Python in Blender; treat that as code execution with scene and filesystem effects. Use small reviewable operations, explicit output paths and saved source versions. Do not run arbitrary code embedded in third-party meshes, notes, prompts or archives. When MCP is unavailable, an installed Blender CLI can run a reviewed script if the actual version, file and command are known; screenshots or script success alone do not prove engine integration.

## 3D production and engine handoff

Author in real scale with intentional origins, naming, collections and material slots. Check applied transforms, mesh cleanup, normals, topology and UV islands. Bake or simplify expensive materials for the target engine when needed, and include texture dependencies. For animated characters, verify rest pose, bone axes, deformation, clips, root motion and events in the engine rather than only the DCC preview.

Export the format supported by the target pipeline, such as glTF/GLB or FBX, with deliberate axes, units, animation and material settings. Keep `.blend` and other editable sources. Reimport into the real project, compare size/orientation/materials, verify animation and collision, and measure runtime cost. An isolated render is useful evidence of appearance, while the running game establishes usability and performance.
