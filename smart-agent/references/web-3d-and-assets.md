# Three.js and external 3D assets

Use for browser 3D, interactive scenes, WebGL/WebGPU experiences and relevant asset ingestion. Preserve the actual engine for an existing game. A native-engine project does not need Three.js merely because it has 3D assets.

## Three.js

Use [threejs.org](https://threejs.org/) for the official manual, API reference and examples, and [mrdoob/three.js](https://github.com/mrdoob/three.js) for pinned source and migration evidence. The reviewed source reports version 0.186.0 on 2026-10-27; match the consuming project's installed version instead of silently upgrading it. The toolkit indexes selected guides rather than every API entry.

Define a playable or interactive slice before adding visual complexity. Separate scene state, rendering, input and lifecycle. Use the renderer supported by the actual browser and brief; select WebGPU only with tested support and a suitable fallback. Keep core and addon imports compatible, use the actual package export map, and check migrations when moving versions. Do not assume a WebGL recipe works unchanged in WebGPU or TSL.

For assets, prefer a format supported by the target engine and loaders, often glTF/GLB for web delivery. Preserve scale, orientation, rig, animation clips, material/color-space assumptions and licensing. Apply compression only with matching decoders and measured quality. Dispose of scene resources, event listeners and animation loops when replacing scenes. Resize with the container, bound pixel ratio according to performance, and test visibility/focus transitions, context loss where relevant, loading errors, keyboard/touch and actual device constraints.

Verify the rendered result and interactions in a real browser. Check frame times, memory and asset/network cost against a task-specific budget. Compilation, a screenshot or importing Three.js alone is insufficient evidence of a working 3D experience. Reuse the game release guide for controls, saves and packaging when this is a game.

## Atlas Components

Pinned source: [TurkiHassan/atlas-components](https://github.com/TurkiHassan/atlas-components). The reviewed project integrates React/TypeScript components and an Arabic RTL catalog. It re-exports upstream implementations; it is not a new implementation of every component. Use selected catalog examples, component criteria and comparison/verification reports to choose components that fit the project.

Inspect the current package and peer dependencies before installation. At the reviewed revision `@atlas/ui` is a private workspace package built into a local archive, not a presumed public npm package. Follow the repository's pack workflow for an authorized integration. Retain required styles, providers, specialized exports and client boundaries. Test Arabic and English, RTL/LTR direction, mixed-script text, focus, keyboard, touch, dialogs, forms and narrow screens. Do not replace an existing design system merely to use Atlas.

No repository-level license grant was found at the reviewed snapshot. Its third-party notices do not grant rights to all original Atlas content. Keep this as linked guidance; resolve rights before redistributing its own code/assets. Preserve each upstream package's notices. Check font rights separately; a locally referenced font is not permission to bundle it.

## Open3DLab

User-requested external source: [Open3DLab](https://open3dlab.com/). The automated read on 2026-10-27 returned an Anubis browser challenge. No asset listing, asset download, license, account action or site-wide content assessment was verified. Use a supported browser interaction if actual asset selection requires it; do not bypass a challenge or infer blanket permission from the domain.

Treat each candidate as a separate acquisition decision. Record the asset page, creator, download/version date, exact license and required attribution; examine commercial use, derivative work and redistribution terms for the intended project. Check whether content is appropriate for the user's brief and audience before previewing or downloading it. Do not generalize one asset's license to the whole site or choose sensitive material merely because it is available.

Inspect format, textures, polygon counts, skeleton/rig, animation, dependencies and archive contents before importing. Work in a staging folder and avoid running scripts, add-ons or executable content bundled with an asset. Preserve originals and notices; convert and optimize a copy. Test the actual imported asset's materials, scale, animation and performance in the consuming engine. Record any unverified rights or compatibility as a release constraint.
