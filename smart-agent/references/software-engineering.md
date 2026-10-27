# Software and AI-agent engineering

## Establish the outcome and context

Inspect the actual repository, applicable instructions, architecture, relevant files, dependencies, logs, current changes, and environment before editing. Recover concrete user behavior and acceptance criteria. Distinguish required behavior from optional improvements. Preserve the existing product's identity and user changes unless the task justifies changing them.

Plan only as much as uncertainty and dependencies warrant. Define risky interfaces and invariants where useful: data ownership, state transitions, access, errors, retries, or integration contracts. Choose architecture from requirements and evidence; avoid frameworks, services, dependencies, or abstractions added solely to fit an agent workflow.

For unfamiliar/current technology, combine installed-code inspection with relevant official documentation. Research should inform implementation without becoming a compulsory phase for familiar tasks. Use the strongest useful available coding/execution environment and keep its actual capabilities distinct from its name.

For production-facing software, sensitive data, auth/access, payments, public APIs, databases, infrastructure, deployment, or meaningful abuse/failure surfaces, load [security-reliability-infrastructure.md](security-reliability-infrastructure.md). Integrate its relevant invariants during design and implementation, not only in a final scanner pass. Scale depth to the system and preserve native judgment about how to perform the work.

## Implement and debug

Build cohesive increments and keep the application runnable when practical. Complete the requested user flow, including errors and recovery that materially affect it. Reproduce a defect or obtain decisive evidence; change the smallest coherent area that resolves the actual cause.

Fix causes rather than hiding symptoms with disabled checks, swallowed exceptions, unrelated rewrites, or weakened assertions. Inspect the combined diff and integration boundaries after concurrent work. Measure relevant bottlenecks before complex performance optimization; verify data compatibility and recovery needs before an authorized migration.

For integrations, inspect provider contracts, server-side trust boundaries, failure/replay behavior, and secret handling where applicable. For payment/access flows, client success alone does not establish a confirmed payment or download right. Test the affected enforcement and idempotency behavior in an appropriate test environment.

## Build AI agents as working systems

Inspect the actual SDK and model/tool interfaces rather than assuming a prompt supplies orchestration. Define task outcomes, tools, state persistence, error recovery, observable termination, and human handoff where useful. Match execution authority to the user's scope.

Separate model output from trusted execution. Validate tool arguments/results to the application's needs; exercise malformed data and prompt-injection boundaries when relevant. Implement concurrency, timeouts, bounded retries, and measurable spend controls from the application's requirements. These deployed-system controls are distinct from a universal limit on the assistant's intelligence.

For repeated agent work, diagnose whether a failure concerns task definition, state, permissions, orchestration, integration, or implementation. Repair the responsible layer and exercise comparable cases without supplying the prior answer. Keep assignment-specific history out of reusable instructions.

Evaluate task-level success and realistic failure cases. Measure cost or latency when optimization is required and trustworthy metrics exist. Adopt retrieval, memory, multiple agents, or complex planning when the actual use case benefits, rather than as mandatory architecture.

## Verify relevant behavior

| Deliverable | Useful evidence |
| --- | --- |
| Logic or regression fix | Focused tests for the input/output or state invariant at issue. |
| Feature spanning components | Integration checks at affected boundaries and relevant project lint/type/test/build checks. |
| User interface | Rendered inspection, interactions, responsive layouts, loading/errors, keyboard/touch behavior, and runtime/network observations. |
| External integration | Provider contract checks and sandbox evidence; identify production behavior not exercised. |
| Data change | Representative compatibility checks and authorized migration/recovery verification. |
| AI agent | Task outcomes, tool errors, interruption/replay behavior, and applicable authority boundaries. |

Choose checks by consequences, regression likelihood, and unresolved uncertainty. Run required project checks and added executable scripts. Avoid meaningless tests or a full suite for every trivial edit. Once relevant checks pass, broaden testing only when new changes, failures, or uncertainty justify it. Treat builds, unit tests, runtime QA, and live deployment as different evidence.

For significant features, use relevant failure-model prompts: invalid/boundary input, empty state, slow/failed dependencies, duplicate actions, refresh/navigation, concurrent requests/tabs, device layouts, session and permission variants. Model meaningful business-state transitions and test forbidden transitions or partial failure rather than scattering state assumptions through UI code. Add practical regression tests for fixed security/reliability defects.

For independent review, provide requirements and raw artifacts rather than your preferred diagnosis. Resolve disagreement with observable defects and discriminating checks. Verify integrated behavior after concurrent edits when needed.

## Deliver working results

For build/fix requests, actually implement, run, inspect failures, correct them, and verify as far as access permits. Do not substitute instructions for feasible execution. Respect repository branch, commit, and release conventions; stage only task-owned changes and preserve history.

Prepare concrete artifacts and configuration before any genuinely required final approval. Perform already-authorized repository updates or deployment when supported. Verify external outcomes before reporting success or retrying interrupted operations. Report changes, purpose, meaningful verification, and material limitations; preserve an exact next action when blocked.
