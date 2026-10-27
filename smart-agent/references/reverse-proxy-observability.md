# Reverse proxy performance monitoring and troubleshooting

Use for diagnosing NGINX, HAProxy or another actual reverse proxy, gateway or load balancer. Start with the deployed topology, installed version and observed symptom; do not replace the proxy or tune every setting by habit. The request path may include browser/client, DNS, CDN/WAF, TLS termination, proxy, upstream queue, app and database.

## Establish the measurement boundary

Record the time window, affected route and traffic cohort, healthy comparison, deployment/config revision and user-visible consequence. Measure request rate, p50/p95/p99 latency, error/timeout rate, retries, active connections, queue depth, upstream health and resource saturation. Define success for the actual service; a low average can hide a poor tail. Compare percentiles computed from the same raw population; averaging p95 values across instances is not a valid fleet p95.

Carry a bounded correlation/request ID across proxy and application logs. Use consistent timestamps/timezones and inspect clock skew. Do not log authorization headers, cookies, credentials or private request bodies by default. Protect access to logs and metrics and account for retention and ingestion lag.

## Instrument the actual proxy

For NGINX consult the official [log module](https://nginx.org/en/docs/http/ngx_http_log_module.html), [upstream module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html), and [stub status](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html). Inspect current access/error logs and effective configuration before enabling extra collection. Useful request fields include `$request_time`, `$upstream_connect_time`, `$upstream_header_time`, `$upstream_response_time`, `$upstream_status`, `$status`, bytes, route and a request ID. Availability and interpretation depend on configuration and version.

NGINX upstream timing fields can contain several values for retries or several upstream groups. Preserve that structure. Do not cast the entire string into one number or add overlapping timing measurements as independent phases. A missing upstream value, cache hit or error has a different meaning from zero latency. `stub_status` gives basic connection/request counters, not a complete latency histogram.

For HAProxy consult official [alerts and monitoring](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/alerts-and-monitoring/) and the configuration manual matching the installed release. Correlate frontend/backend/server statistics, queue/connect/response/total timings, termination state, retries and health checks. Timer names, units and behavior vary by log format/version. Identify the actual schema rather than copying a parser from another deployment.

Use existing metrics/logging systems when suitable. Splunk can correlate proxy, application and security events when actually configured; it is not assumed installed. Keep Prometheus/other metric labels bounded (route templates rather than user IDs or raw URLs), separate readiness from a shallow liveness check, and restrict management/status endpoints to intended access.

## Troubleshoot by evidence

| Observation | Investigate next | Verification |
| --- | --- | --- |
| Slow connection establishment | DNS resolution, routing, connection limits, upstream listener/backlog, TLS and handshake behavior | Compare proxy-to-upstream timings and bounded connection tests from the same vantage. |
| Long time to upstream headers | Upstream queue, application execution, dependency/database waits, worker saturation | Correlate a slow request with application traces/logs and upstream resource state. |
| Long transfer after headers | Large payloads, client backpressure, buffering, streaming, network loss and throughput | Inspect bytes, duration, packet evidence if authorized, and streaming behavior. |
| 502/503/504 or connection resets | Error log reason, upstream health, connection refusal/reset, TLS mismatch, timeout alignment and capacity | Reproduce a scoped request and compare proxy/app evidence; status code alone does not identify the root cause. |
| Rising retries or queues | Upstream failures, retry amplification, pool sizing, limits and uneven load | Compare first-attempt results and end-to-end latency; ensure non-idempotent requests are not replayed blindly. |
| Cache anomalies | Cache key, vary/auth rules, invalidation, hit/miss and stale behavior | Check correctness and tenant/user isolation alongside performance; test expected freshness. |
| Sudden regression after deploy | Config or dependency changes, routing, resolver, compression, TLS and resource limits | Compare known-good configuration and traffic cohorts, then verify an authorized rollback or focused change. |

Measure before changing buffers, keep-alive, workers, timeouts, compression, HTTP versions or kernel settings. Do not mask a slow upstream by increasing every timeout. Preserve server-sent events, WebSockets, uploads and long-running legitimate traffic when relevant. Consider retry load and cancellation propagation. Distinguish origin processing time from client transfer time and CDN effects.

## Change and verify

Back up the configuration and run the proxy's supported syntax/configuration check before reload. Plan a reversible scoped change, use an appropriate reload/deployment mechanism, observe health and representative traffic, and compare the same latency/error/resource measures. A syntax check proves parsing, not operational success. Avoid load generation on production without the relevant authorization and resource limits; use representative controlled workloads when possible.

Deliver the symptom, supported root cause or remaining hypotheses, exact change, before/after evidence, effect on correctness and tail latency, limitations and rollback. If data are incomplete, say what can be concluded and what observation would distinguish the remaining causes. This module defines a workflow; it does not install continuous monitoring or promise an unmeasured speedup.
