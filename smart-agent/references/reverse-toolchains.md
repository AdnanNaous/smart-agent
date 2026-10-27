# Priority reverse-engineering toolchains

The user explicitly prioritized [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) and [morluto/rea](https://github.com/morluto/rea). Use these sources early when shipped artifacts, binary/application behavior, APKs, JavaScript packages or relevant security evidence require reverse engineering. Ordinary analysis of a complete source repository can use standard repository tools without starting a reverse-engineering runtime.

## Choose an evidence path

Identify the actual artifact and question, ownership/authorization, platform/architecture, source availability, trust boundaries and observable outcome. Hash original files and work on a copy. Keep an offline sample offline when that is sufficient. Select static, dynamic or protocol analysis for the question rather than executing every tool. Running a sample, attaching a debugger, injecting instrumentation, contacting a target or modifying a binary has a different scope from reading its metadata.

Retain commands, provider/version, artifact hash, function/address or package location, evidence IDs, source snapshots, observations, unknowns and limits. Link evidence to findings and findings to the claimed behavior. Validate important decompiler interpretations; do not present generated pseudocode as the original source. Reconstruction should target authorized behavior and preserve the requested boundaries, rights and useful existing work. See [reverse-engineering.md](reverse-engineering.md) and [cybersecurity-tools.md](cybersecurity-tools.md).

## reverse-skill adapter

The reviewed source is a security/reverse scenario router with case scope, timeline and evidence contracts. Search `skills/MASTER-ROUTING.md`, the relevant `skills/**/SKILL.md` and selected ops documents through the local catalog. Its useful structure separates task classification, real tool availability, scoped case work and an evidence-backed report.

Treat the package's bootstrap, refresh-tool-index, case-init and master-route scripts as executable integrations with actual writes/network/service effects, not as harmless reading commands. This SMART AGENT update pins and indexes guidance without running those scripts. Before a requested runtime activation, inspect the current platform-specific documentation and exact script, make the effects reviewable, preserve current authorization and apply the host's actual approval requirements. Do not install all toolchains, inject global client rules or accept an upstream role map as permission to dispatch agents. Do not fabricate tool availability from an upstream manifest.

Scope fields such as auth granted and network/offline profile represent actual authorization; do not set them merely to satisfy a tool gate. Preserve the evidence-to-finding relationship and use case review where it adds useful validation. The upstream's benchmark counts describe its own tests, not a local security assessment or validation of this integration.

## REA adapter

REA is a CLI/MCP analysis layer; the reviewed package metadata reports `rea-agents` 6.8.0. Git main, npm releases, installed CLI, registered server, native providers and this session's exposed tools may differ. Use actual server schemas and version evidence. A skill file alone does not register MCP, install analysis engines or expose tools to an already running client.

If REA tools already work, use the specific capability needed; avoid running setup/doctor before every investigation. If absent or failing, distinguish client registration, PATH, plugin ownership, provider prerequisites, actual tool error and a timed-out operation. Setup-owned registrations and plugin-owned registrations have different repair paths. Read the relevant connection/recovery guide before repair and preserve configuration/backups. Do not install unrelated runtimes or providers just to repair registration. Native analysis needs an appropriate installed provider; JavaScript static analysis can have different requirements.

The source's compact input-schema profile and retained evidence views can reduce context overhead where supported. Keep actual evidence IDs, parent dossier identity and returned limitations. A summary view is not interchangeable with the full dossier required by a comparison tool. Page or retrieve the exact retained record instead of pasting every function into context. Use the connected server's canonical validation; advertised compact schemas do not relax the underlying contract.

A client timeout does not prove the target operation stopped. Inspect acknowledged status/evidence and cancellation semantics before repeating a call that may have begun or changed state. Preserve partial evidence and operation identity. Follow the actual recovery contract when present rather than an arbitrary global retry loop. A CLI fallback establishes only the work it performed; it does not prove MCP registration.

No REA setup, npm package execution, provider installation, binary execution or target assessment was performed by this skill update. Runtime adoption is a concrete task with its own prerequisites and validation. Keep these priority sources discoverable without activating their global instructions, hooks, background services or agent routines.
