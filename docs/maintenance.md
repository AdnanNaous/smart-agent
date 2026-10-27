# Evolving the operating layer

SMART AGENT is working knowledge, open to improvement through real use. Its examples are replaceable. The durable parts are user intent, native judgment, authorization, evidence, state integrity, and useful continuity.

## Learn from a concrete outcome

Inspect what happened before editing instructions. A failure may belong to the application, tool integration, missing state, task definition, access boundary, or skill. Change the responsible layer. Prefer a small transferable lesson with its supporting conditions over a universal rule derived from one run.

When maintaining the skill is authorized, a supported agent can edit the reusable bundle, simplify obsolete guidance, validate affected behavior, and publish through its actual repository access. Preserve enough history to reverse a regression. The agent chooses the useful method; this document does not prescribe a model, research sequence, retry count, or team.

## Keep the right knowledge in the right place

| Location | Purpose |
| --- | --- |
| [SKILL.md](../smart-agent/SKILL.md) | Operating principles and conditional reference selection |
| [references/](../smart-agent/references/) | Reusable domain knowledge loaded when useful |
| Project-local state | Current objective, verified work, decisions, blockers, next action |
| [tests/](../tests/) | Reproduction cases and observed evaluation evidence with limits |
| [docs/](./) | Installation/maintenance context and repository presentation |

Do not put credentials, private records, entire conversations, or downloaded third-party media into public evaluation reports. Keep claims tied to observed versions and conditions. Replace outdated assertions when stronger evidence contradicts them.

## Validate and save where work actually runs

Use `python3 tools/validate_skill.py` and relevant tests from the repository root. Inspect changed links, metadata, examples, and the final diff. For a consequential instruction change, use a realistic task with raw inputs and verify the actual result rather than coaching an evaluator toward the intended answer.

The [validation workflow](../.github/workflows/validate.yml) checks repository structure on supported GitHub push/pull-request events. It has read-only repository permissions and does not modify the skill. Running checks automatically is different from authorizing an agent to edit instructions.

Update an installed copy through that runtime's supported skill-maintenance mechanism and verify it separately. Do not assume a GitHub commit propagates to ChatGPT, Codex, or future environments. Scheduling, persistent execution, credentials, and model controls exist only when the current runtime exposes them. Saved project knowledge and instruction revisions do not alter model weights.
