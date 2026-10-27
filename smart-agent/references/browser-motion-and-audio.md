# Browser motion and procedural audio

Use for an interactive browser promo, audiovisual explainer, or code-only motion piece with synthesized sound. Read [motion-video-production.md](motion-video-production.md) for the production context and exported delivery. Treat this as one available technique; do not impose its aesthetic, scene count, tempo, library, or music structure on other briefs.

## Content, identity, and responsive composition

Inspect the actual site or product for factual claims. Text retrieval can establish copy but cannot establish the visual identity; inspect rendered pages or authorized brand material when appearance matters. Build a compact palette/type/layout vocabulary appropriate to the brief. Establish readable composition before adding effects when that helps isolate layout problems.

Use a defined composition container and proportional units when they fit. Container-query units require the intended query container; verify computed behavior rather than assuming they scale to any parent. Keep semantic text available to assistive technologies and avoid exposing every animated letter as separate content. Segment text in a language-appropriate way and preserve graphemes, shaping, ligatures, and reading order. A mask, whole-word animation, or composited text may work better than independent letter transforms.

Use accessible playback controls with keyboard/touch operation and visible focus. Provide a considered reduced-motion or static state when appropriate, and check contrast and flashing rather than reproducing an intense reference effect by default.

## Use a coherent time model

Keep scene durations, cuts, musical sections, and event cues in shared timeline data. Align to a beat grid when musically appropriate; fixed tempo, chord progression, geometry counts, and transition lengths are creative choices. Reserve intentional sound tails or fades instead of requiring every visible cut to coincide with an abrupt audio stop.

For live synthesized sound, schedule audio on the audio context's timeline and derive visual progress from the same logical playback position. For silence, use an appropriate monotonic clock; for offline rendering, evaluate the requested frame/time. Account for start offsets, context suspension, pause, seeking, replay, and hidden-tab behavior. Timers can initiate work but are not a precision playback clock. Reconcile state to current time after a delayed callback rather than replaying every missed timer.

Evaluate decay, interpolation, pulses, and camera motion from elapsed time or a tested time step rather than a fixed multiplier per displayed frame. Otherwise the effect changes with refresh rate. Explicitly define the visual state at scene boundaries and during covering transitions.

Restarting CSS animations through class changes and a layout read can work for a small live sequence, but does not make seeking or frame capture deterministic and can incur synchronous layout work. Use the existing renderer's controls, explicit animation time, or a supported animation API when better suited to replay/export. Inspect delayed entrances and flash states; fill modes, transforms, clipping, and layer composition can affect what appears before a cue. Avoid prescribing one browser-specific workaround without testing the actual implementation.

## Procedural sound and playback controls

Synthesis can use oscillators, noise, envelopes, filters, or other available audio mechanisms without a media model or prerecorded soundtrack. Reuse an established composition/synthesis library when it is suitable and already available; do not add one merely because a reference used it. Schedule bounded work, leave headroom, and use gain envelopes to avoid unintended clicks and abrupt stops. Seed generated noise when repeatable output matters.

Start or resume audio from an allowed user interaction and handle the resulting context state or rejection. Provide intentional silent playback and appropriate mute/replay or pause controls. On replay, cancel old visual jobs and stop/disconnect old scheduled sources before scheduling a new run; avoid overlapping sound or leaking nodes. Test repeated starts and muted/silent transitions. Browser support and autoplay behavior require current documentation and actual observation.

Use compatible, inspected dependency versions and deliberate failure states. A CDN script is still a runtime dependency even if no image, video, or audio asset files are used. Pinning alone does not establish maintenance, compatibility, or offline operation. Check missing-script, initialization failure, unavailable WebGL, and context-loss behavior when relevant; a try/catch around initialization does not cover every asynchronous or later failure. Keep essential text and controls useful without the effect.

## Verify visual, audio, and delivery behavior

Inspect representative scenes, transitions, narrow/wide layouts, overflow, console errors, replay, controls, and relevant disabled-capability paths. Choose sample counts and viewport sizes from the actual risks rather than a universal screenshot quota. Test real-device behavior when available and distinguish it from emulation.

When supported, render the same audio graph with an offline audio context or equivalent mechanism. Check actual sample count/rate, finite output, channel behavior, peaks/headroom, unintentional silence, event timing, tails, and total duration. Peaks or energy changes can reveal technical defects but cannot prove musical quality, intelligibility, or audibility; listening is a separate check. Verify audible output only when it was actually heard through a supported capability.

Distinguish an interactive HTML experience from a rendered MP4. If video export is requested, explicitly capture or render the visual timeline and include the audio through a supported export/muxing path, then inspect the final file. Offline audio rendering by itself neither produces video nor proves a synchronized master. Report the actual deliverable and completed checks, and preserve precise limits when playback, capture, export, or listening is unavailable.

## Current implementation references

Consult these when the selected browser mechanisms need confirmation, or prefer newer authoritative guidance:

- [Audio context time](https://developer.mozilla.org/en-US/docs/Web/API/BaseAudioContext/currentTime)
- [Web Audio best practices](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices)
- [Offline audio rendering](https://developer.mozilla.org/en-US/docs/Web/API/OfflineAudioContext)
- [Animation-frame timing](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame)
