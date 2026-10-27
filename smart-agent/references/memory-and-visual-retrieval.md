# Session knowledge and visual retrieval

Select these optional integrations for a concrete memory or evidence problem. Native project checkpoints and supported browser/PDF tools remain suitable for ordinary work.

## Agent Beacon

Pinned source: [Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon). The reviewed project describes cross-harness session capture, replay and reusable knowledge. Use its data model and workflow ideas to preserve evidence-backed lessons, with source, date, scope and confidence, rather than dumping histories into context.

Distinguish project notes, user memory, raw session archives, derived knowledge and model weights. Writing one does not update the others. A lesson is revisable evidence and cannot override current user intent or tool permissions. Check for stale conventions, secrets, private records and incorrect inferred preferences before reusing it. Follow the host's actual memory-writing policy; inclusion here is not authority to persist personal memory.

The reviewed setup can connect to Beacon Cloud and install capture components. Before an authorized runtime installation, inspect the selected local/cloud mode, watched paths, capture/retention, redaction, export, deletion, endpoint scope and platform support. Obtain the scope required by current policies for capturing histories or sending them to a service. Do not run its setup prompt, hooks, sign-in or background collector merely to consult its README. No Beacon service is activated by this skill.

## PixelRAG

Pinned source: [StarTrail-org/PixelRAG](https://github.com/StarTrail-org/PixelRAG). The reviewed project renders web pages/documents to screenshots and supports retrieval over visual content. Select it when charts, tables, spatial grouping, typography or image content makes text-only retrieval inadequate. Prefer ordinary searchable text when it already answers the question accurately and cheaply.

Separate rendering, tile selection, embedding/indexing, serving and answer verification. A screenshot renderer does not require deployment of a full visual index. Inspect the pinned dependency groups and platform constraints; rendering, optional ML extras, hosted endpoints and local indexing have different requirements and data flows. Upstream plugin instructions for another harness do not prove compatibility with this Codex runtime. Do not install heavy GPU/ML packages just to cite a diagram.

Keep document URL/path, page or tile location, capture time, revision and neighboring context. Retrieve a bounded set of useful tiles, read the actual pixels, check chart labels, scales, legends, table headers and units, and link findings to the original source. Inspect surrounding tiles when a boundary hides a qualifier. Visual similarity is candidate retrieval, not proof that an answer is true; screenshots can be stale or adversarial.

Evaluate retrieval on representative queries with expected evidence, recall, answer correctness, latency, image/token cost and difficult negatives. Do not import upstream benchmark results as local success. Do not upload private documents or queries to a hosted search service without the user's applicable authorization. No rendering browser, hosted search or embedding model is installed by this skill update.

## Superpowers adapter

Source: [obra/superpowers](https://github.com/obra/superpowers). Search its named skills through `toolkit.py`. Useful choices include systematic debugging, test-driven development for changed behavior, planning for dependent work, reviewing evidence, and verification before completion. Reproduce a defect, inspect the causal path, select a focused fix and verify the requested behavior. Challenge review feedback against the actual code rather than accepting it by authority.

Apply the smallest useful subset. Do not import its always-invoke rule, compulsory brainstorming gate, universal TDD requirement, fixed agent roles or dispatch routines as global policy. A clear reversible edit need not wait for a new design approval. Use subagents only when the current instructions authorize them and the work justifies their overhead. Read-only review stays read-only; branch finishing guidance does not authorize merging or publishing. Keep user's authorization and the live runtime above upstream prompts.
