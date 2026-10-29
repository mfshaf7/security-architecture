# Console recovery timing and package cache security delta

## Summary

Review the existing local recovery path after failed automatic restart attempts.
The prior [Console capability recovery review](2026-10-28-console-capability-recovery.md)
continues to govern all unchanged identity, model, artifact and owner boundaries.
This delta is limited to OOS dependency preparation and the Platform complete
lifecycle budget and diagnostics. Exact merged owner revisions and Platform tree
remain selected by the existing [composed decision](2026-10-24-configurable-ai-routing.yaml).
No operating completion is claimed by source acceptance.

## Reviewed Source

- operator-orchestration-service: Gary candidate `150434d238128426cc269ae9271e4d38cc88b00a`, merged `17358f6deefa9e4b0b0dcee50366dc5b67ac86f4`, equal tree `108ab09453f265996c396608596828e400026a74`.
- platform-engineering: Gary candidate `46f38f044b54a98e54563be5d27fa80f60e00779`, merged `d81dca004a90103327af22d4005adce187d1886f`, equal tree `f03abc08e0dbe3be6975e76cf54f034ec7900a72`.

## Scope Delta

The existing three OOS init containers share one operator-profile `npm-cache`
directory under already admitted local state. It is created mode0700 by the
operator; symlink redirection is refused. Only those init containers mount it.
They still copy selected source into fresh runtime storage and run `npm ci`
against the lockfile, with npm package integrity checks. The cache stores public
package downloads, not a trusted installed tree, caller material or application
records. The prior packaged API image has a different lockfile and is not treated
as a current dependency bundle. No package mirror, registry, service or privileged
host helper is added.

Package installation drops root to uid/gid1000 before npm or lifecycle scripts.
The helper admits only an operator-owned cache directory at its fixed mount,
uses a fixed npm command and runtime directory, bounds installation at480seconds
and fetches at30seconds with one retry, and propagates nonzero or interrupted
execution as failure. Offline preference does not disable lock checking or audit
reporting. Corrupt cache data must be rejected or redownloaded and verified; it
cannot become readiness. The worker retains its deployment-generation guard and
allows600seconds for rollout instead of180seconds.

Only the existing complete-runtime product drop-in changes its finite startup
budget to45minutes; the generic profile service keeps its original15minutes.
Complete startup performs independent bounded integrity checks, sequential
participants, scoped identities, consumed bindings, frontend preparation, final
readback and compensation. Existing early failure behavior and explicit shutdown
semantics remain. This budget is a containment deadline, not a recovery guarantee
under missing prerequisites, unavailable package sources or hardware faults.

Platform records fixed startup phases without arguments or bindings. Only
composition-up combined output is written live to a unique mode0600 file under
operator-private `private/startup-logs/`, so interrupted child diagnostics survive.
The path is announced before execution. Vault/token and other helper outputs keep
existing in-memory custody; arguments and environments are never recorded by this
change. Raw private logs must remain outside source, ART, browser and model raw
projection. A surviving log is not a result receipt or readiness evidence.

## Review Areas

Runtime/delivery: reuse existing participant identities, namespaces, source
mounts and rollback. The additional writable path contains disposable downloads
inside the existing operator profile; it exposes no wider host root or source
write path. Same-operator cache tampering remains subject to lock integrity.
Unexpected cache ownership/redirection fails closed. Cold cache may require the
public npm registry; warm-cache and corrupt-cache behavior require explicit proof.
A failed worker remains a failed participant, never a fabricated ready condition.

Identity/secrets: no identity, credential scope, caller role, browser grant,
root-helper policy or durable generation changes. Private startup output is
sensitive operational context and may need redaction before projection. Readiness
continues to require exact source acceptance, consumed credentials and bindings,
owner projections, model configuration and accepted frontend. Current source and
native operating evidence stay distinct.

Source evidence: OOS full suite passed1703 checks with two existing optional skips,
plus focused cache-preservation, symlink refusal and cold-worker/failure checks.
Bundle/OpenAPI/governance/shell and committed base-aware checks passed. Platform
full `make validate` passed, including75 complete-runtime tests with four existing
skips. A real interrupted subprocess proves output exists mode0600 before parent
exit and survives process-group termination. Actual locked-dependency exercise passed in an isolated filesystem and network
namespace using the real helper and lockfile: empty cache131.845seconds; warm cache
with network disabled4.674seconds; corrupted copied cache denied without network
in11.939seconds; repair from the registry4.173seconds. This is dependency proof,
not live application acceptance. Exact hosted checks and delegated review must
pass before source merge.

## Decision

**approved** for the exact owner source/tree selected by the paired composed
decision after owner review and merge. Preserve other reviewed owners, the
original durable manifest, worker digest and activation generation. Advance only
accepted clean sources, then use the existing complete-runtime activation and
normal status. Require native cold/warm recovery, consumed binding freshness,
owner/model/current/history readbacks and the pending VMEM source-bound UI proof
before reporting this maintenance operationally complete. Isolated dependency or
process tests do not replace that operating witness.
