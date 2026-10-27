# Token efficiency without losing evidence

Optimize useful verified work per total cost, including input, output, reasoning, retrieval, image processing, latency, rework and any worker duplication. Do not promise a percentage without comparable measurements. A concise final response alone does not establish token savings.

## Low-overhead working habits

- Read the entrypoint and only the reference that changes the next decision. Search catalog metadata before opening an upstream skill. Avoid concatenating libraries, manuals, entire repositories or long histories into context.
- Search narrowly with `rg`, filenames and bounded excerpts. Request the important fields from tools. Summarize long logs with failure context and retain the original file path; do not discard the exact error, trace, command, source location or verification result.
- Batch independent reads in a tool call when useful. Keep dependent decisions, mutations and approval boundaries sequential. Avoid repeated polling or rerunning successful checks without new changes or uncertainty.
- Record a small resumable checkpoint: user intent, authorization, actual branch/revision, changed files, evidence, unresolved work and next action. Refresh it when material state changes rather than after every tool.
- Reuse stable context and cacheable prefixes when the actual API supports them. Check current provider caching documentation and measured usage; fewer characters do not necessarily imply a lower bill.
- Keep the user's selected model and effort. Choose a supported alternative only when authorized and a measured capability/cost advantage exceeds handoff overhead. Do not run several agents for a bounded task just to appear thorough.
- Stop research when the evidence supports the requested decision; deepen only for uncertainty that could change the outcome. Preserve required quality, security and verification checks.

## Headroom adapter

Pinned source: [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom). Consult the local README or selected docs through the toolkit index for version-specific capabilities. It offers library, proxy and MCP approaches to reducing context. Treat upstream benchmark percentages as the authors' results, not savings achieved here.

Start with deterministic selection and bounded outputs. If actual output volume warrants compression, evaluate an isolated sample using the smallest useful integration. Preserve originals and retrieval pointers. Check that compression retains negatives, ordering, timestamps, IDs, units, source citations, exceptions, policy constraints and the error needed to reproduce a failure. Retrieve original content when a decision depends on omitted details. Do not compress away user intent or authorization.

Installing wrappers, changing provider endpoints, downloading models, modifying agent config or enabling history learning is a separate integration choice. Source inclusion does not activate these actions. Inspect current platform support, dependencies, storage behavior, recovery and uninstall path before an authorized installation. Do not add a proxy to the user's live Codex application based on documentation alone.

## Measurements

Save actual usage telemetry for equivalent tasks and acceptance checks, with model, effort, source version, sample count and relevant cache/billing categories. Compare baseline and optimized quality before accepting savings. Report regressions and negative savings as well as improvements. Character counts, index size and guessed ratios are not token telemetry.

`scripts/manage.py token-report <measurements.json>` evaluates measured input-token comparisons. Example schema (numbers must come from actual telemetry):

```json
{"runs": [{"id": "observed-run", "baseline_input_tokens": 1000,
  "actual_input_tokens": 800, "same_task": true, "quality_passed": true}]}
```

The example is synthetic and establishes no real savings. Without measurements the result is not calculable. The helper reports arithmetic only; `same_task` and `quality_passed` are supplied evidence assertions, not independently verified by the script. It does not calculate full cost, output/reasoning use or latency.

The pinned Headroom recovery guide records an earlier Codex wrapper regression involving temporary `CODEX_HOME` directories and missing normal chat history. Inspect version-specific recovery and preservation behavior before any wrapper experiment; do not adopt wrapping as a default token optimization. The guide is indexed for discovery.
