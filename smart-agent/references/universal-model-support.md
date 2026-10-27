# Provider-agnostic support for present and future models

Use this reference when the task spans providers, local models, an unfamiliar model family, a new modality, or a future model. SMART AGENT's instructions can adapt to any model/runtime capable of following the relevant instructions. Its catalog accepts arbitrary provider/model identifiers and capability names. This is a compatibility strategy, not a claim to possess every model, know unreleased specifications, or execute every provider API.

## Distinguish four kinds of support

- **Instruction portability:** adapt the skill's goals, scope and evidence standards to the host model's real context, instruction hierarchy and tools. A platform without skill loading can receive the relevant instructions through its supported interface.
- **Discovery/catalog support:** record models exposed by an actual runtime or provider catalog. A public model repository, local weight file, provider listing and usable hosted endpoint are distinct observations.
- **Execution support:** the host must expose a suitable invocation tool, account access, credentials, quota and compatible API/runtime. This skill does not add those by naming a model or importing metadata.
- **Validated task fit:** verify the capability needed for the actual task. A declared feature, a connected endpoint and a successful representative task provide different evidence. No one benchmark establishes universal superiority.

Keep the current model normally. Honor explicit user choices, including the user's Terra 6.1 preference for computer-use plugin tasks when it is actually selectable and suitable. Supporting another model does not authorize dispatch, another chat, paid inference, weight downloads, service installation or a global default change.

## Discover from the actual surface

Prefer the host's live tool/control schema. For a provider integration already in scope, use current official catalog documentation and existing authorized access. Do not probe all vendors, scan local accounts or request new keys merely to answer a simple task. Model lists can be paginated, regional, account-specific, gated or stale. Resolve relevant pages and metadata deliberately; a single page is not a worldwide inventory.

Primary catalog examples reviewed on 2026-10-27:

| Surface | Discovery reference | What the local helper accepts |
| --- | --- | --- |
| OpenAI and compatible catalog exports | [List models](https://developers.openai.com/api/reference/resources/models/methods/list) | `data` arrays with exact `id` values; compatible listing shape does not prove compatible inference behavior |
| Anthropic | [List models](https://platform.claude.com/docs/en/api/models/list) | `data`, `display_name`, declared capability `supported` objects and pagination markers |
| Google Gemini | [Models API](https://ai.google.dev/api/models) | `models`, exact resource `name`, reported token limits, generation methods and thinking metadata |
| Ollama/local runtime | [List models](https://docs.ollama.com/api/tags) | `models` with `name`/`model`; weight presence is not proof of loaded capacity or tool support |
| Hugging Face | [Hub API](https://huggingface.co/docs/hub/en/api) | exported arrays with `id`; repository presence does not establish an inference endpoint, license permission or affordable hardware |
| Codex cache | Host-owned model catalog | `models` with `slug` and declared reasoning levels; exact execution controls still take precedence |
| Any other or future source | Its current official schema or a neutral export | list, `data` or `models` rows; arbitrary nested collections/IDs through explicit field mappings |

These are parsing/decision adapters, not authenticated inference clients. No provider accounts, keys, paid requests or model downloads were used to implement this layer.

## Offline catalog management

`scripts/models.py` uses the Python standard library and performs no network requests. Export the catalog using a separately available authorized tool, remove credentials if present, and import the file locally. The helper copies selected model metadata rather than arbitrary account fields. Import snapshots sequentially to the same registry.

```text
python scripts/models.py import --provider my-provider --input catalog.json --observed-on 2026-10-27
python scripts/models.py list --provider my-provider --limit 10
python scripts/models.py check --provider my-provider --model exact-model-id --require computer_use --require image_input
```

For a new wrapper schema:

```text
python scripts/models.py import --provider future-provider --input catalog.json --observed-on 2026-10-27 --items-field results.entries --id-field release.identifier
```

Use the actual observation date. `--registry <path>` goes before the command to isolate a project or test. The default is `${CODEX_HOME}/skill-state/smart-agent/model-registry.json`, outside the skill bundle. Provider and model IDs form a pair, so two services can expose identical model names without overwriting each other. No global registry of all worldwide models is maintained.

An ordinary import upserts observed rows and preserves unobserved rows with their original dates. Only `--complete`, after confirming the provider snapshot is complete, replaces that provider's stored set; other providers remain intact. Known continuation markers block a contradictory complete claim. Unknown/new pagination conventions still require reviewing the actual schema. Completeness is explicitly operator-declared, not automatically established by the helper.

The shipped `assets/model-catalog-example.json` is synthetic. It documents a neutral shape, not the existence or performance of the example model. New IDs, capability keys and reasoning labels do not require edits to a fixed family list. New response wrappers can use field mappings or a small reviewed adapter if the provider's shape changes materially.

## Capabilities are evidence, not guesses

Record task-relevant input/output modalities, tool/function calling, structured outputs, reasoning controls, streaming, computer use, context/output limits and lifecycle information only when supplied by reliable current evidence. Capability keys are open-ended: additional future capabilities can be recorded without changing the parser. Preserve the provider's exact names and semantics. Unsupported parameters must be omitted or adapted explicitly; do not map all providers' effort values onto a single intelligence scale.

Capabilities with explicit boolean true/false are treated as declared support/non-support. Missing or null values stay unknown. Nested provider `supported` objects can be flattened to qualified capability names. Generation methods and token limits remain separately reported metadata and do not imply computer use or permission to call arbitrary tools. Names such as vision, thinking, pro or latest are not a capability test.

`check` reports metadata support, an unsupported requirement, a need for verification, a missing catalog entry, or reported retirement. Old or future-dated observations require verification; default maximum age is seven days and can be set for the task. `execution_verified` remains false because this helper never calls a model. The age threshold is a configurable local heuristic, not proof that fresher data are sufficient. A negative/missing result is limited to the imported snapshots.

## Execute and evolve only where supported

Inspect the actual inference contract: message format and roles, tokenizer/context packing, multimodal encoding, tool schemas/results, structured output, reasoning controls, streaming, cancellation, error/retry semantics, data location and billing. An OpenAI-compatible models endpoint alone proves none of these other behaviors. For local/open-weight models, also consider chat templates, license, quantization, RAM/VRAM, runtime support and loading cost before a requested deployment. A text-only or embedding model need not be treated as a chat coordinator.

When the required controls are absent, continue useful work with the current capable model or provide the concrete integration needed. Do not simulate a model switch, silently substitute a different model, fabricate execution or introduce a new service to imitate unavailable controls. A small authorized representative test should verify the task-critical contract before claiming execution support. Recheck current documentation when API/version or failure evidence changes; preserve existing configuration and a reversible adapter update.

Future readiness means open-ended identity/capability schemas, current discovery, explicit unknowns and adaptable execution boundaries. It cannot guarantee access, compatibility, correctness, price or speed for every present or unreleased model. Keep dates and evidence, retire obsolete adapters and preserve user intent as the runtime evolves.
