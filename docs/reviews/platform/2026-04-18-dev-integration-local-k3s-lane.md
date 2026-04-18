# Dev-Integration Local-k3s Lane Review

- date: 2026-04-18
- scope: workspace-standardized `dev-integration` lane for fast local cross-repo
  iteration on local `k3s`
- owner repos:
  - `workspace-governance`
  - `platform-engineering`
- related repo:
  - `operator-orchestration-service`
- security owner: `security-architecture`
- status: approved-local-lane

## Summary

This review approves `dev-integration` as the workspace-standard fast local
iteration lane for cross-repo workflows that are still too fluid for governed
stage rehearsal.

Approved scope:

- local `k3s` namespaces only
- local-only generated credentials
- profile-driven runtime shape with branch or worktree source inputs
- local session manifests and promotion reports
- local disposable dependencies such as scratch OpenProject instances

Not approved:

- direct writes to governed stage or prod backends
- reuse of governed shared secrets
- Argo- or digest-backed rollout claims from the local lane
- direct promotion of a local runtime into stage

## Review Areas

### Identity

- the lane creates local machine identities only inside the disposable runtime
- operator identity and machine identity remain distinct through the session
  manifest plus local runtime credentials
- local identities are acceptable only if they do not overlap with stage or
  prod principals

### Secrets

- `dev-integration` may generate local-only secrets under local state roots
- governed Vault paths and governed shared credentials must remain out of scope
- profile-owned credentials must be ephemeral and resettable

### Delivery

- this lane is intentionally ungoverned for delivery and must stay separate
  from the governed stage path
- the winning shape must still move through commits, PRs, platform contracts,
  and stage rehearsal before it is treated as governed
- local session manifests are operating notes, not rollout evidence

### Runtime

- local `k3s` is the correct shared runtime target because it stays close to
  the real platform shape without using governed stage as the design lab
- per-profile or per-operator namespaces are required
- easy teardown is part of the control model, not just a convenience feature

### AI

- this lane does not itself approve any governed AI path
- if a profile later uses a local model or simulator, that path must remain
  labeled local or integrated until the governed AI access plane exists and is
  reviewed separately

## Required Controls

1. a workspace-standard lane policy in `workspace-governance`
2. a shared local-k3s runner in `platform-engineering`
3. explicit profile ownership in the owner repo
4. session manifest recording branch/worktree inputs and dirty state
5. clear stage handoff rules that rebuild through the governed path instead of
   promoting the local runtime directly
6. local-only secret generation and no governed backend writes

## Decision

Approved as the current fast local iteration lane for cross-repo workflow
development.

Future expansion to shared remote scratch clusters, governed secret reuse, or
live AI-assisted paths requires a fresh review.
