# Asset preparation and delivery

Use the existing toolchain where possible. Check current official documentation when introducing unfamiliar or version-sensitive pipelines. Do not install every optimizer preemptively.

## Acquisition and provenance

Inspect actual asset pages and terms for commercial use, modification, redistribution, attribution, and restrictions relevant to web delivery. Distinguish code licenses from licenses of sample models and textures. Prefer explicit terms. Record the original page as well as the download URL; signed download links alone are not durable provenance.

Manifest entries should identify local delivery files, creator/title, source page, license name and URL, access date, modifications, and required credit. Render attribution where terms require it; a private manifest may be insufficient. Preserve relevant license files. Follow repository conventions for large originals.

## Images

- Size to rendered use with bounded high-density variants, responsive sources, and explicit dimensions. Do not deliver full-resolution desktop backgrounds to small viewports.
- Choose project-supported WebP/AVIF or other formats according to alpha, fidelity, browser targets, and tooling. Preserve suitable SVG artwork and sanitize untrusted active content.
- Compare edges, gradients, alpha fringes, texture detail, and colors after compression. Use meaningful alt text for content images and empty alt text for decoration.

## Video

- Crop and encode for the viewport, remove unused audio, and shorten loops where appropriate. Supply compatible sources and a lightweight poster with stable dimensions.
- For ambient playback use muted inline playback when supported; handle autoplay refusal, delayed loading, reduced motion, and constrained devices with a useful still.
- Inspect loop seams and text readability during bright or busy frames. Avoid downloading heavy video before it becomes useful.

## Models and textures

- Inspect bounds, pivot, scale, orientation, geometry density, material count, transparency, UVs, texture sizes, and animation/wind attributes. Set framing deliberately.
- Prefer self-contained GLB where practical. Verify external textures and clips. Remove unused data and simplify only as far as silhouette and camera distance allow.
- Consider Meshopt/Draco geometry compression and KTX2/Basis textures when compatible with installed loaders and deployment. Include and verify decoders/transcoders; compression without a working decoder causes loading failures.
- Budget decoded GPU memory as well as transfer size. Compressed downloads can expand into large textures and buffers. Reduce redundant materials/maps and instance repeated objects.
- Check color space, lighting, alpha, normals, and tone mapping in the application; optimization can change appearance.

## Rendering budget and fallback

Establish a baseline and measure relevant transfer sizes, draw calls, triangle counts, frame times, and memory indicators with available tools. A DPR cap around 1.5–2 can be a starting experiment, not a universal rule; tune from measurements.

For demanding scenes define a quality ladder reducing resolution, shadows, postprocessing, textures, geometry, and particle/grass density; use a designed still if needed. Avoid rapid quality oscillation. Use instancing and distance-dependent vegetation detail rather than per-blade JavaScript updates.

Verify bounds and culling after shader deformation. Match shadow deformation or use a cheaper coherent shadow treatment. Check that startup, route changes, and teardown leave no duplicate animation loops or resource leaks.
