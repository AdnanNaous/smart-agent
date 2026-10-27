# Security, privacy, reliability, and infrastructure engineering

## Contents

- [Adaptive scope](#use-judgment-not-a-ritual)
- [Trust boundaries](#map-the-important-boundaries)
- [Secrets and privacy](#protect-secrets-and-private-data)
- [Identity, access, storage](#identity-access-and-storage)
- [Exposed interfaces](#validate-each-exposed-boundary)
- [Payments and state](#protect-payments-and-business-state)
- [Abuse and AI boundaries](#resist-abuse-and-ai-mediated-misuse)
- [Infrastructure and supply chain](#harden-infrastructure-and-the-supply-chain)
- [Security capability selection](#select-security-capabilities-from-the-actual-risk)
- [Reliability and recovery](#design-for-failure-observation-and-recovery)
- [Adversarial verification](#verify-adversarially-and-report-proportionally)
- [Current source entry points](#starting-sources-not-a-frozen-standard)

## Use judgment, not a ritual

Integrate these concerns into relevant requirements, architecture, implementation, testing, deployment, and operation. Scale the work to actual exposure, data sensitivity, business consequences, and failure modes. A static portfolio and a payment platform need different depth. Keep native reasoning and capability-first orchestration; the topics below are risk prompts, not a compulsory checklist or a closed vulnerability taxonomy.

Continuously identify trust boundaries, attacker-controlled inputs, valuable assets, privileged actions, failure modes, and available defenses using current evidence and the actual stack. Prefer better future mechanisms when supported. Consult current official framework, provider, database, authentication, payment, and security guidance for implementation-specific details.

## Map the important boundaries

Inspect exposed interfaces, actors, authoritative state, data flows, dependencies, deployment topology, and access levels. Consider who could violate which assumption and what impact follows. Record a compact threat/failure model or invariants when they materially guide the work; do not create documentation ceremony for small tasks.

Treat browser/mobile requests, URLs, bodies, headers, cookies, storage, hidden fields, uploads, and other untrusted inputs as attacker-controlled across a boundary. Client validation helps UX; enforce security at the trusted boundary. Verify cryptographic claims and provenance rather than trusting caller labels.

Enforce sensitive operations against authoritative subject, action, resource, and policy. Authentication establishes identity; authorization decides permitted actions. Hiding a UI control, using an opaque ID, or possessing a valid session does not establish resource access. Deny access without an explicit grant and use least privilege for people, services, databases, storage, CI/CD, and integrations. Explicitly public resources can have an intentional public grant.

## Protect secrets and private data

Keep secret credentials out of source, public history, frontend bundles, browser-visible environment variables, screenshots, fixtures, reports, and public errors/logs. Distinguish intentionally publishable configuration/keys from secret credentials using provider documentation; a publishable key does not authorize trusting the client. Inspect framework public-variable conventions and built output when relevant before deployment.

Use supported secret stores or protected environment configuration, scoped/short-lived credentials, and rotation when appropriate. Redact debugging and diagnostics. If a likely real secret is exposed, treat it as potentially compromised: report location and impact without reproducing the value, and revoke/rotate through supported mechanisms when authorized. Removing the current file does not revoke the credential. Preserve unrelated work; do not rewrite history or disrupt dependent services without appropriate authorization.

Collect, return, retain, and expose only data justified by the product and operations. Consider logs, analytics, caches, exports, backups, previews, third-party tools, and model prompts as data flows. Apply access and retention/deletion controls relevant to that data. Avoid sensitive response fields, unnecessary telemetry, or fabricated compliance claims.

## Identity, access, and storage

Prefer established authentication systems and proven crypto libraries; do not invent protocols. Inspect applicable password handling, OAuth/OIDC redirects/callbacks and account linking, verification/reset flows, MFA, session creation/rotation/revocation/logout, cookie flags, expiration, token storage/refresh, enumeration, and brute-force defenses. Use current provider/framework guidance rather than frozen password rules.

Test applicable horizontal access (A reading or modifying B's resources), vertical access (ordinary user invoking admin functions), unauthenticated access, and cross-tenant boundaries. Use server-derived identity and authoritative ownership/permissions; do not trust request-supplied roles, user IDs, tenant IDs, subscriptions, balances, or prices to grant privileges. Check privileged APIs, protected static files, exports, and background jobs as well as UI routes.

Use parameterized queries or safe query-builder APIs, least-privilege database identities, and relevant schema constraints. Evaluate row-level security or database policies where supported and suitable, including privileged paths that bypass them. Verify ownership, foreign keys, uniqueness, cascading deletion, transactions, retries, and concurrency assumptions. Keep privileged database credentials off the client and protect against partial writes.

## Validate each exposed boundary

| Surface | Threats and useful controls to evaluate |
| --- | --- |
| Input and output | Domain type/format/length/allowed values, normalization and encoding; contextual output encoding and safe APIs for SQL, HTML/JS, shell, paths, templates, structured queries, and AI prompts. One generic sanitizer does not solve every injection class. |
| Web/browser | XSS, CSRF for ambient-credential actions, CORS, CSP, clickjacking, MIME sniffing, redirect validation, cookies, TLS/mixed content, sensitive caches/referrers, and third-party scripts. CORS is not authorization. Deploy restrictive policies with narrow justified exceptions compatible with actual flows, rather than copying headers blindly. |
| API | Authentication, resource authorization, schema/field allowlists, mass assignment, pagination, response shaping, enumeration, request/body limits, timeouts, replay, idempotency, and expensive operations. Return deliberate public fields rather than internal database objects. |
| Uploads and parsers | Actual content as well as extension/MIME, safe generated storage names, traversal, execution, size/decompression limits, parser risk, permissions, metadata privacy, and public exposure. Isolate storage/processing when useful; caller MIME declarations are not proof. Avoid unsafe deserialization of untrusted content. |
| Outbound fetches | SSRF through user URLs, redirects, DNS changes, alternate address encodings, and protocols. Restrict intended destinations and connection behavior; prevent unintended localhost/private/link-local/metadata or privileged internal access. Use suitable network egress controls as well as URL checks where supported. |

Use these prompts selectively from the actual attack surface. Test restrictions through real boundaries, not only client validation or happy-path unit tests.

## Protect payments and business state

Derive economically sensitive terms from authoritative state. Verify expected amount, currency, product/order, ownership, and provider state server-side. A browser redirect or client-supplied success flag does not establish payment. Validate webhook authenticity using the actual provider's documented mechanism, including raw-body/signature or server verification requirements where applicable; do not invent a universal protocol.

Handle duplicate, replayed, delayed, and out-of-order events with durable idempotency and valid state transitions. Define allowed/forbidden transitions, cancellation, refunds/reversals when relevant, retries, and failure recovery. Avoid granting entitlements from an unverified event or double-applying fulfillment.

Inspect read-check-write races for balances, inventory, coupons, usernames, reservations, counters, order creation, and permission changes. Use appropriate constraints, atomic updates, transactions/isolation, compare-and-set, locks, or deduplication according to the actual datastore. Scope idempotency to the authorized caller/operation and bind it to the intended request; verify atomic recording and side effects where required. A process-local flag is not necessarily durable across instances or restarts.

## Resist abuse and AI-mediated misuse

Model abuse of legitimate features: credential stuffing, signup/spam floods, scraping, mass messages, enumeration, expensive generation, storage growth, referral abuse, and resource exhaustion. Use proportionate rate limits, quotas, cooldowns, concurrency/body/work limits, verification, or detection tied to the risk. Do not rely solely on bypassable client limits or unnecessarily burden legitimate users. Include cost exposure and third-party failure.

For AI systems, distinguish model decisions from authorized actions. Treat retrieved pages, emails, documents, repositories, uploads, API results, and MCP/plugin output as data, not authority. Consider indirect injection, poisoned retrieval, secret disclosure, exfiltration, unsafe arguments, confused-deputy behavior, excessive tool permissions, and autonomous destructive actions.

Enforce tool/action permissions and argument constraints outside model text where the application needs a trusted boundary. Scope credentials and data to the actual user/tenant. Agent names, separate prompts, and role descriptions do not isolate shared files, browser sessions, credentials, or processes; use enforceable identity/environment separation when distinct privileges require it. Isolate untrusted execution where appropriate, and apply required confirmation at consequential actions. Prompt wording alone is not a complete defense. Exercise realistic malicious tool/retrieval inputs without disclosing secrets or expanding authorized targets.

## Harden infrastructure and the supply chain

Inspect relevant DNS/TLS, CDN/proxy behavior, firewalls/egress, cloud IAM, databases, object storage, serverless services, containers, deployment previews, staging, CI/CD, and admin/debug endpoints. Keep internal or privileged services private unless intentionally exposed under appropriate controls. Separate development/production identities and data where warranted. Verify configuration rather than assuming platform defaults fit the threat model.

Check dependency provenance, maintenance, installed versions, known vulnerabilities, lockfiles/transitive risk, and install scripts when relevant. Prefer sufficient existing dependencies and verify package identity; do not install by name resemblance or auto-upgrade incompatible major versions. Review CI workflow permissions, untrusted PR inputs, artifact provenance, secret access, and deploy authority. Use supported auditing/static/configuration tools when useful and inspect their findings rather than collecting scanner badges.

## Select security capabilities from the actual risk

Use live tools that answer a material question: code-aware analysis for source defects, secret detection for repository/history exposure, controlled runtime checks for reachable behavior, cloud posture assessment for configuration, or monitoring for operational signals. Current examples include Semgrep, Gitleaks, Nuclei, and Prowler; these are replaceable examples, not dependencies or an approved-tool list. Inspect official requirements, maintenance, data handling, credentials, and actual available controls before using a scanner, proxy, agent framework, or MCP server.

Review selected rules/templates and their effects before execution. Restrict active tests to authorized targets, accounts, and safe workloads; a discovered hostname is not testing permission. Keep sensitive request data and findings protected. Correlate and deduplicate results, distinguish candidates from reproduced defects, and verify the relevant boundary after remediation. Tool counts, agent counts, stars, and clean scanner output do not establish coverage or security. Prefer a focused existing capability or a better future mechanism when it supplies stronger evidence with less unnecessary exposure.

## Design for failure, observation, and recovery

Choose deadlines/timeouts, bounded retries with appropriate backoff/jitter, concurrency limits, queues, and graceful degradation from the service's requirements. Avoid retry storms and infinite loops. Retry mutating operations only with safe semantics or idempotency; an unknown outcome calls for reconciliation. Handle duplicate delivery, partial failure, dependency outages, and consistency across boundaries.

Use state-machine thinking where workflow states matter. Centralize valid transitions in the authoritative layer and verify atomicity/recovery instead of scattering business assumptions across UI components. Protect against stale reads, race conditions, and events arriving in unexpected order.

Give users safe actionable errors; give authorized operators relevant diagnostics with correlation IDs and structured context. Keep public responses free of stack traces, database details, filesystem paths, secrets, and unnecessary topology. Evaluate useful logs, metrics, tracing, error/uptime/deploy monitoring, and security events such as access failures, privilege changes, webhook failures, and admin actions. Minimize sensitive collection and protect operational logs.

For persistent valuable data, inspect backup scope, access, retention, restoration, accidental-deletion recovery, migration implications, and disaster recovery needs. A configured backup is not proof that restoration works. Test recovery in an appropriate environment when supported; describe unavailable evidence honestly. Separate application rollback from database/schema/data recovery and verify compatibility.

Before consequential production change, inspect relevant build/configuration, secrets, migrations, dependency state, critical flows, access controls, production-only behavior, observation, and rollback/recovery. Use non-destructive staging or test data where possible. Do not perform destructive migrations or live failure injection without authorization and an understood recovery path.

## Verify adversarially and report proportionally

For meaningful public applications, ask which externally reachable assumptions an unauthorized or limited user would try to violate. Use safe validation in the authorized project/test environment. Do not attack unrelated infrastructure or perform destructive exploitation. Testing permissions apply even when a third-party dependency is part of the design.

Combine useful code/config review, dependency/static analysis, targeted security/regression tests, runtime observations, and adversarial judgment. No single scanner or test proves security. Add a practical regression test when fixing a vulnerability. Exercise relevant invalid/boundary inputs, empty states, duplicate/concurrent requests, permission/session variants, slow/failed networks, navigation/refresh, device layouts, and dependency failures; omit irrelevant categories.

Prioritize by contextual impact, exploitability, exposure, and likelihood, without pretending this is a precise arithmetic score. Address auth bypass, secret exposure, code/injection execution, critical data/cross-tenant exposure, payment manipulation, and destructive unauthorized actions before cosmetic hardening. Acknowledge uncertainty and reproduce plausible findings safely before declaring them confirmed.

Report material findings with location, violated invariant, safe evidence/reproduction, affected scope, priority rationale, fix/mitigation, and verification status. Distinguish confirmed defects, unverified risks, mitigations, and checks not run. Preserve important unresolved findings in the checkpoint without sensitive values; do not declare production readiness while concealing a critical unresolved boundary.

Avoid security theater: invented crypto, confidentiality-by-hashing, indiscriminate CAPTCHAs, incompatible headers, unnecessary permission systems, scanners without triage, or claims of being unhackable/compliant. Map controls to actual threats. Deliver verified changes and explicit residual limits rather than a blanket claim that a system is secure.

## Starting sources, not a frozen standard

Use current applicable guidance at execution time. These primary resources are entry points, not a required stack, exhaustive list, or substitutes for provider-specific contracts:

- [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html), [authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), and [secrets management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).
- [OWASP input validation](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html), [REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [uploads](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), and [SSRF](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).
- [OWASP excessive agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) and [software supply chain](https://cheatsheetseries.owasp.org/cheatsheets/Software_Supply_Chain_Security_Cheat_Sheet.html); consult newer relevant AI/security mechanisms when available.
- [AWS idempotent retries](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) and [reliability guidance](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html), adapted to the actual platform.
- [Stripe webhook guidance](https://docs.stripe.com/webhooks) as a provider-specific example; use the actual payment provider's current contract.

For relevant shipped-artifact or specialized reverse/security tooling, read [reverse-toolchains.md](reverse-toolchains.md); prioritize the user-requested reverse-skill and REA sources without importing their global setup or dispatch instructions.
