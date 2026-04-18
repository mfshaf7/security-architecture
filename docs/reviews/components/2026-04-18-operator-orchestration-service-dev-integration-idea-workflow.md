# Operator Orchestration Service Dev-Integration Idea Workflow Review

- date: 2026-04-18
- scope: first concrete `dev-integration` profile for the broker-owned idea
  workflow on local `k3s`
- owner repo: `operator-orchestration-service`
- related repos:
  - `platform-engineering`
  - `openclaw-telegram-enhanced`
  - `workspace-governance`
- security owner: `security-architecture`
- status: approved-local-profile

## Summary

This review approves the first concrete `dev-integration` profile,
`idea-workflow`, as a local-only runtime for fast rehearsal of the broker-owned
idea workflow.

Approved scope:

- local broker deployment from local source state
- local disposable OpenProject plus Postgres plus Memcached
- local-only automation identity and API token inside the disposable
  OpenProject runtime
- reuse of the real Telegram `/idea` handler through a local simulator
- local smoke flow for help, capture, list, list all, and show

Not approved:

- any direct stage or prod backend writes
- any use of governed OpenProject or governed Vault credentials
- claiming local smoke as governed evidence

## Review Areas

### Identity

- the profile creates a local automation identity only inside the disposable
  OpenProject runtime
- local caller auth between simulator and broker is acceptable because it is
  local-only and resettable
- local identities must not be reused for stage or prod

### Secrets

- broker env material and caller secrets are generated under the local state
  root and are not shared with governed runtimes
- the profile must fail closed if the local backlog seeding contract is missing
  required field ids instead of guessing stage or prod values

### Delivery

- the profile intentionally runs from local source state, including local
  branches, worktrees, and dirty trees
- the promotion path remains separate: real source commits, PRs, immutable
  artifacts, and governed stage rehearsal

### Runtime

- reusing the real broker runtime and the real Telegram `/idea` handler through
  a simulator is the correct contract-aligned local shape
- the local profile must remain bounded to its declared services and smoke
  checks instead of turning into a second platform control plane

### AI

- this profile does not enable governed AI triage
- any later AI-assisted local path must remain explicitly labeled local or
  integrated until the governed AI access path exists

## Required Controls

1. the profile uses the shared `dev-integration` runner instead of inventing a
   repo-local lane
2. the local OpenProject seed runners come from `platform-engineering`
3. the broker profile records source state and promotion requirements in local
   session artifacts
4. the simulator remains a local adapter and does not imply Telegram-owned
   workflow truth

## Decision

Approved as the first local-only `dev-integration` profile for
`operator-orchestration-service`.

Fresh review is required if the profile starts reusing governed credentials,
touching remote shared scratch infrastructure, or enabling AI-assisted triage.
