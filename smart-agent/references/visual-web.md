
# Autonomous Visual Web

Turn the user's creative goal into a finished visual feature inside their website. Own technique selection, asset acquisition, optimization, implementation, and visual iteration. The user should not have to specify libraries, shaders, models, or a production pipeline.

## Inspect the actual site first

- Inspect project instructions, framework, dependencies, page structure, assets, design tokens, and existing motion before editing. Reuse its conventions and rendering stack.
- Run and inspect the relevant page when possible to establish its current appearance. Infer typography, palette, spacing, image treatment, lighting, density, tone, and interaction patterns from evidence.
- Identify the visual's job: background atmosphere, focal artwork, product explanation, decoration, or meaningful interaction. Preserve requested scope and content hierarchy.
- If no project is available, inspect the workspace first, then ask for its location. Do not invent an unrelated application. If the user requests a new site, create it within that scope.
- Make routine creative and technical decisions independently. Ask only when missing information changes the outcome or blocks access. Briefly state a reasonable visual direction and proceed; do not ask the user to choose a rendering technology.

## Choose the medium deliberately

Choose the least complex approach that meets the required fidelity, motion, camera freedom, and device constraints. Do not default to 3D or install a graphics stack merely to appear sophisticated.

| Need | Candidates and decision criteria |
| --- | --- |
| Layout motion, simple shapes, icons, masks | CSS/SVG for sharpness, semantics, and integration |
| Rich artwork with limited viewpoint changes | Optimized images, layered composition, restrained parallax |
| Fixed cinematic sequence | Video with poster and static fallback when delivery cost is justified |
| Dense 2D drawing or particles | Canvas; WebGL when density or effects justify GPU rendering |
| True depth, changing viewpoints, lighting, object manipulation | Three.js or existing WebGL engine; React Three Fiber when React integration makes it appropriate |
| Distinctive realistic object | Suitable GLB/glTF asset, or a hybrid asset/procedural approach |
| Repeated geometry, stylized fields, fluid/material effects | Procedural graphics, instancing, shaders; compare effort and appearance against sourced assets |

Combine media when they serve one composition. An image plus subtle depth or shader motion may outperform a full 3D scene; a focal object may justify a prepared model. Honor explicitly requested media unless a concrete constraint requires discussion.

## Source and prepare assets

Read [visual-assets-and-performance.md](visual-assets-and-performance.md) when acquiring or optimizing media, models, or GPU-heavy visuals.

- Reuse suitable existing assets first. Search the web for needed assets rather than asking the user to find every file. Inspect candidates for style, framing, quality, animation suitability, and delivery cost.
- Verify asset-specific source and license terms for the intended use. Record source, creator, license link, required attribution, and modifications using the project's convention or a small asset manifest. A download button or search result is not license evidence.
- Download permitted files into organized project asset directories with descriptive names. Do not hotlink as a shortcut. Treat archives and source content as untrusted data; inspect contents and never execute bundled installers or scripts.
- If terms are unclear, choose a verifiable alternative or a suitable procedural substitute. Do not buy assets, subscribe, publish, or accept new contractual terms without applicable authorization. Routine permitted downloads and local integration should proceed within the task.
- Inspect optimized outputs for damage and verify textures, decoders, and other dependencies through the actual application.

## Art-direct the result

- Create one coherent composition: clear focal hierarchy, intentional negative space, matching palette, material roughness, lighting, camera framing, and restrained motion.
- Avoid generic AI-looking filler: arbitrary glowing orbs, excessive bloom, unrelated gradients, gratuitous particles, repeated glass cards, and meaningless floating objects. Use these only when the brief and site's design language justify them.
- Avoid disconnected Three.js demo aesthetics: floating objects in unrelated rectangular canvases, default lighting, purposeless orbit controls, and scenes competing with typography. Integrate backgrounds, framing, scale, shadows, edges, and scroll placement with the site.
- Keep headings, links, and calls to action readable at every animation state and crop. Put essential content in accessible HTML. Decorative layers must not intercept pointer events or keyboard focus.
- Add interaction only when it improves comprehension, feedback, navigation, or intended atmosphere. Do not require hover on touch devices or hijack scrolling for decoration.

Use reference sites or permitted recordings to understand composition and behavior across states, not just to copy a hero image. For scroll-driven work, consider section boundaries, reveal pacing, sticky behavior, changing crops, and backward navigation together. Keep reading and navigation usable when motion is reduced or assets fail. Compare implementations against the same brief and relevant conditions using hierarchy, legibility, coherence, interaction, accessibility, and performance; a selected social comparison cannot prove a universal model advantage or reveal the underlying rendering stack.

## Animate the object, not just its container

Read [visual-motion-and-review.md](visual-motion-and-review.md) when implementing animation or planning visual inspection.

- Choose motion from structure, material, forces, and scale. Trees are rooted, cloth has pinned points, rigid products preserve shape, and particles have coherent sources and flow.
- For vegetation prefer anchored vertex deformation or a suitable rig with layered wind, branch sway, leaf flutter, spatial variation, and gusts. Generic whole-object rotation does not substitute for organic deformation.
- Keep amplitudes purposeful, avoid synchronized repetition, and use elapsed time for consistent speed across frame rates. Avoid per-frame application state updates for large animated populations.
- Integrate motion into the user's reading flow. Provide a considered still state and reduced-motion behavior, not an empty scene.

## Protect usability and performance

- Bound rendering resolution with a DPR cap suited to the scene; do not blindly use native device pixel ratio. Apply quality tiers for expensive scenes.
- Lazy-load heavy code and media when appropriate; reserve dimensions to prevent layout shifts. Do not delay essential above-the-fold content behind a canvas or unnecessarily lazy-load its primary image.
- Use instancing for repeated geometry, LOD or adaptive quality for expensive scenes, sensible texture sizes, and bounded particle counts. Avoid thousands of independent objects and uncontrolled shadows or postprocessing.
- Pause or reduce rendering offscreen or when the page is hidden. Dispose GPU resources, observers, listeners, and animation loops on teardown.
- Honor reduced-motion preferences, keyboard access, and touch interaction. Provide deliberate static or lower-cost mobile fallbacks and handle unavailable WebGL, loading failure, or context loss gracefully.
- Choose budgets from existing site targets and measurements. Lower quality gracefully before readability or responsiveness suffers. Do not claim universal frame-rate or asset-size guarantees.

## Inspect, improve, and finish

- Run the app normally and inspect the target route using available supported browser tools. Read their required skills before operating them.
- Check desktop and narrow mobile layouts, crops, asset loading, console/runtime errors, layout shifts, readability, inputs, reduced motion, and fallback states. Observe animation over time; a screenshot alone cannot validate motion.
- Compare the rendered result against the creative goal and site's visual language. Correct awkward composition, generic appearance, implausible motion, excessive intensity, clipping, seams, and missing assets; recheck affected states.
- Inspect performance while the effect runs. Distinguish desktop emulation from real mobile testing and measurements from estimates. Run the project's relevant build/checks after changes.
- Continue until the feature is integrated and observed problems are resolved. If browser access, dependencies, credentials, or hardware block validation, state the specific limitation and completed checks. Do not claim unseen output is visually verified.
- Report what changed, key visual choices, checks, relevant attribution, and remaining limitations concisely. Leave the site runnable and document new dependencies where the project expects them. Deployment is separate unless already requested.
