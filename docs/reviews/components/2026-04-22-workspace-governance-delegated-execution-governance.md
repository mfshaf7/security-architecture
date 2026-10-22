# Workspace Governance Delegated Execution Governance Review

## Periodic Baseline Reassessment — 2026-10-23

The April review below remains historical evidence. This periodic reassessment
renews its existing scope at current merged Workspace Governance
`61b9ea1d238cbc7facab155131997df373d66e64`; it does not backdate the October22
expiry or accept the unmerged pre-Inventory bootstrap extension.

Design intent: bounded implementation delegation with main-agent-only work
mutation, live mutation, Security closure, final proof/completion and planning.
Current `contracts/delegation-policy.yaml` and `docs/delegated-execution.md`
retain that split, disjoint write scopes, exact task packets, journal duties,
zero delegated live-control workers and a maximum of two bounded implementation
workers. The contract-foundation marker is not evidence of per-worker runtime
sandboxing. Separate agent-action authority is still required for AI actions.

Implemented control: current policy, registered skills and journal validator
retain the same owner boundaries; the live installed16-skill check and current
canonical delegation-journal validation pass. The complete current contract
and original review were read for this reassessment. Existing Security findings,
risk and remediation inventories contain no separate delegation-specific
finding to retire; the original narrative restrictions below remain in force.

Operating evidence: no sub-agents were delegated in this recovery. That fact
does not certify hypothetical delegated live actions. The October23 isolated
native registration rehearsal passes all292 Workspace Governance tests before
the independent review-coverage expiry gate. Its test result is engineering
evidence, not acceptance of the proposed source repair or a clean-state claim.

Decision: `approved-with-findings`, retaining the three original restrictions
below. Main-agent Security and landing judgment stay explicit; no new identity,
secret distribution, independent approval, live delegation or risk acceptance
is granted. Owner remains Workspace Governance, Security retains review closure.
The next baseline review is2027-04-23, preserving the existing six-month review
interval. Any trust-boundary change requires its own delta before that date.
The latest exact composed-operation review remains separately required for
Console/runtime changes and is unchanged by this baseline renewal.

## Summary

- date: 2026-04-22
- owner repo: `workspace-governance`
- affected review subjects:
  - `repos.workspace-governance`
- decision: `approved-with-findings`

This delta review covers the new workspace-wide delegated execution governance
model in `workspace-governance`, including:

- a machine-readable delegation policy contract
- the delegated-execution operator procedure and task-packet model
- write-scope ownership and delegation journal expectations
- skill and self-improvement controls that preserve main-agent authority for
  security closure, final proof, and final landing judgment

## Scope Delta

`workspace-governance` already acted as the workspace control plane for routing,
skills, validation, and self-improvement. The delegated execution model expands
that control plane into a new area: governed use of sub-agents for bounded
implementation work.

That changes the security posture in four meaningful ways:

1. agentic parallelism is no longer an ad hoc operator habit and now becomes a
   governed workspace capability
2. the task packet, write-scope, and audit model now influence how far
   delegated workers may act before the main agent must reassert authority
3. the security review surface must state explicitly that delegated workers may
   implement bounded slices, but may not close security decisions or land
   security-significant work on their own
4. the workspace control plane becomes responsible for keeping delegated
   execution bounded while stronger runtime enforcement is still deferred

The change does not introduce a new public ingress path, new human identity,
new secret class, or direct autonomous landing path. It does formalize a new
AI-shaped delivery control model and therefore requires a fresh decision.

## Review Areas

### Identity

- delegated workers must not be treated as independent trust principals for
  security-significant delivery
- operator identity and main-agent workflow authority remain the accountable
  boundary for review closure, final proof, and final landing judgment
- any future model that gives delegated workers independent authority would
  require a separate review because that would materially change the trust
  boundary

### Secrets

- this governance model does not approve any new secret distribution pattern
  into delegated task packets or delegated runtime helpers
- delegated execution remains acceptable only while secret custody stays with
  existing owner-repo and platform-controlled paths
- if a later delegated workflow needs direct secret handling, that would widen
  the review scope and require a fresh delta review rather than inheriting this
  approval

### Delivery

- moving delegated execution into an explicit policy-and-audit model is the
  correct delivery control direction because it replaces ad hoc parallelism with
  bounded execution rules
- delegated work should stay limited to ART-backed or otherwise explicitly
  tracked scope, with uncovered work routed back to the main agent for
  classification rather than silently expanding delegated scope
- final closure stays with the main agent, which is necessary to preserve one
  workflow authority across delivery, security, and audit surfaces

### Runtime

- the current delegated execution model is governance-first, not runtime
  capability enforcement
- that is acceptable for now only because delegated workers remain prohibited
  from live environment mutation, security closure, and final landing judgment
- stronger runtime controls such as capability envelopes and collision
  detection remain future hardening work and should not be implied as already
  implemented

### AI

- delegated execution increases the AI-shaped action surface because multiple
  workers may now contribute to one change stream
- the model remains acceptable only while task packets stay bounded, audit
  expectations stay explicit, and the main agent keeps responsibility for final
  security judgment
- delegated workers must not independently accept risk, reinterpret trust
  boundaries, or bypass the security review trigger model

## Decision

`approved-with-findings`

Approved because the delegated execution control model strengthens the current
workspace by replacing implicit parallelism with explicit policy, task packets,
and audit expectations while preserving a single authority for security
closure and landing judgment.

Required findings to carry forward:

- delegated execution should stay governance-bounded until runtime capability
  scoping exists; do not overclaim stronger enforcement than is actually
  present
- security-significant delegated work must keep the main agent as the explicit
  closer of security decisions and the final judge of whether the work may land
- future delegated workflows that widen into live control actions, secret
  handling, or independent delegated approval require a fresh delta review

## Related Artifacts

- `workspace-governance/docs/delegated-execution.md`
- `workspace-governance/contracts/delegation-policy.yaml`
- `workspace-governance/contracts/repo-rules/workspace-governance.yaml`
- `workspace-governance/skills-src/project-delivery-operator/SKILL.md`
- `workspace-governance/skills-src/self-improvement-review/SKILL.md`
- [`../security-delta-review-process.md`](../security-delta-review-process.md)
- [`../security-review-checklist.md`](../security-review-checklist.md)
