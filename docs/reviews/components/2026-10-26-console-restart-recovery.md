# Console restart recovery security delta

## Summary

Approve the existing local dev-integration lifecycle correction under the same
Platform owner, architecture and composed gate. Reviewed Gary candidate
`e1ebd4792ea2c8bc809d86f8b5a5c1c8357fd5b5`, exact tree
`75096a11ace5a3f0b3f190794c595bf5986b404c`. The paired decision binds merged Platform revision
`2a04edacd6674e0094403b156f22c7d3a6f6179d`, whose tree matches exactly. Console
application source, artifact, provider executable, callers, purposes and all
other execution-owner pins remain unchanged.

## Scope Delta

The shared composition runner carries its owning lifecycle action through its
existing child environment. Failed-start compensating down preserves the
existing operator-login recovery registration, allowing degraded-state/result
publication and the existing bounded systemd retry. A normal composition down
still removes registration; standalone execution clears stale parent metadata.
Profile reset remains unchanged. Parent action is controller-owned operational
context, not a browser input, permission, acceptance or arbitrary command.
The existing composition ownership checks and OS-user boundary remain enforced.

The complete-runtime owner waits at most120seconds for Docker daemon and
Kubernetes API readiness. Each read-only subprocess is bounded and resolves
its executable through the existing controlled service PATH. Kubernetes must
return the exact ready body; a foreign successful body is not accepted. Failure
reports prerequisite labels without exposing raw command output, credentials
or environment. The internal activation path performs this wait before private
policy, credential, artifact and workload effects. Normal external activation
may register/delegate to the existing supervisor first, intentionally preserving
its retry behavior. No new service, root path, credential source, network grant,
account access or privileged execution mechanism is added.

## Review Areas

Runtime/delivery: compensation remains teardown of the same admitted participant
resources and retains original reverse order and private credential cleanup.
Preserving the controller is not activation acceptance or permission to skip
cleanup. An intentional shutdown still prevents unintended auto-resume. The
existing policy remains three starts in ten minutes with sixty seconds between
attempts. Unavailable dependencies and persistent native crashes remain visible
failures. This is a start-rate limit, not a lifetime attempt cap; slow faults
can retry across windows. It does not guarantee PC availability.

Identity/secrets: exact source/Security acceptance still precedes activation,
and caller/session/provider authority is unchanged. The new metadata contains
only the owning action. It grants no model, browser or source identity authority
and is cleared from standalone dispatch. Readiness probes neither issue new
credentials nor weaken endpoint/source verification. No diagnostics dump raw
environments or credential material.

Source proof: full local Platform validation passed, including the complete
runtime, composition, lifecycle and infrastructure checks, followed by committed
base-aware whitespace and owner governance checks. Regression reproduced two
old failures (manual/automatic compensation) while explicit shutdown passed.
Corrected source passes those boundaries, stale context removal, dependency
readiness/recovery, exhaustion, timeout/foreign-body rejection and denial before
effects. Provider CI40345693621 and repo-posture40345693674 passed at the exact
Gary head; delegated human review approved PR343 before merge2a04eda with
identical tree.

Native process proof uses real systemd plus the real composition/runner with a
disposable synthetic profile and no Kubernetes/business effects. Old source
made one attempt, removed registration and killed its own controller before
failed-result publication. Corrected source published failure and recovered on
attempt2 with registration intact; external intentional down still removed it.
Both disposable units were retired. This is real process/lifecycle evidence,
not full Console business qualification or an actual PC reboot observation.

## Decision

**approved** for the exact landed source/tree selected by the paired decision.
Merge the Platform source/owner record first, then regenerate the Security
owner-record index and land this acceptance. Only then advance the live watched
checkout and use normal complete-runtime activation. Require fresh consumed
identity/bindings, owner/current/history/model projections, source-bound frontend
and memory limits, renewal and recovery readback. A source check, healthy
homepage or isolated failure fixture cannot replace full operating evidence.

The Windows login task and Docker startup entry are existing infrastructure;
no Windows/BIOS/Desktop settings are changed by this delta. Physical process
fault causes remain unverified and outside this source judgment. Final runtime,
actual restart and cleanup evidence belongs in the existing memory learning
closeout PR314, avoiding another post-review source-pin loop. Main-agent judgment
retains Security closure and final landing authority.
