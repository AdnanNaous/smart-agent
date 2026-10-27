# Motion design and visual review

## Match motion to construction

| Subject | Useful model | Failure to watch for |
| --- | --- | --- |
| Trees | Root anchoring, slow branch sway, secondary motion, subtle leaf flutter | Entire tree rotates; rubbery trunk stretching |
| Grass | Fixed bases, tip-weighted bend, spatial wind and local phase variation | Synchronized waves, detached roots, CPU-updated blade populations |
| Cloth | Pinned edges, traveling deformation, gravity/tension cues | Rigid-card wobble or unconstrained translation |
| Water | Consistent wave scale/direction, restrained surface and normal motion | Unrelated noise frequencies, implausible reflections |
| Rigid products | Intentional camera/object transforms and easing | Deformed surfaces, purposeless perpetual spinning |
| Particles | Defined source, lifetime, bounded population, flow and depth | Random glitter obscuring text |
| Layered illustrations | Depth-aware parallax and isolated moving parts | Exposed edges, cardboard warping, excessive cursor following |

These are options, not required effects. A quiet still is preferable when motion adds nothing.

## Vegetation details

Anchor bases with local-height or authored weights. Use branch/leaf attributes, vertex colors, or rigs where available; height alone cannot distinguish a stiff trunk from flexible leaves. Inspect imported assets before choosing deformation. If topology or weights are unsuitable, adapt the asset, select another, or use a simpler convincing treatment.

Combine slow directional wind, world-space variation, occasional gusts, and small instance/leaf phase differences. Preserve shared gust direction without perfect synchronization. Scale amplitude to plant size and camera distance. Deform large populations on the GPU and update only small uniform sets per frame. Keep normals and shadows coherent with the scene lighting.

## Review the rendered page

- Does the visual support headings and calls to action at wide and narrow widths?
- Do lighting, perspective, colors, textures, and motion belong to this site?
- Is cropping intentional on touch devices and tall or short viewports?
- Can users read, click, scroll, and navigate with a keyboard while the effect runs?
- Over a full loop or gust cycle, do roots slip, branches stretch, objects clip, particles pop, or seams appear?
- Do initial/slow loading, missing assets, unsupported WebGL, and reduced motion yield a useful stable page?
- Do resizing, route changes, backgrounding, and repeated mounting cause errors or duplicate loops?

Use screenshots for framing and responsive comparisons. Observe live motion or record a short clip when supported to inspect timing and continuity. Check runtime errors and network failures alongside visuals. Fix the cause of a problem and revisit that state; do not add effects to disguise incoherent composition.

When tools cannot inspect motion or a device, document the gap precisely. Responsive browser emulation supports layout checks but does not prove real-phone performance.
