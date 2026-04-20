# Operator Orchestration Service Dev-Integration Accepted-Idea Delivery Review

- date: 2026-04-20
- scope: second concrete `dev-integration` profile for accepted-idea
  consumption into the local OpenProject delivery ART project on `k3s`
- owner repo: `operator-orchestration-service`
- related repos:
  - `platform-engineering`
  - `workspace-governance`
- security owner: `security-architecture`
- status: approved-local-profile

## Summary

This review approves `accepted-idea-delivery` as the second concrete
`dev-integration` profile for `operator-orchestration-service`.

Approved scope:

- local broker deployment from local source state
- local disposable OpenProject plus Postgres plus Memcached
- local proposal backlog seeding plus local delivery ART seeding
- local-only broker automation identity scoped to `workspace-proposals` and
  `workspace-delivery-art`
- local smoke flow for accepted lookup, delivery-project verification, consume,
  and backlink verification

Not approved:

- any direct stage or prod backend writes
- any use of governed OpenProject or governed Vault credentials
- any Telegram delivery-management command surface
- claiming local smoke as governed evidence

## Review Areas

### Identity

- the profile creates a local automation identity only inside the disposable
  OpenProject runtime
- that local identity is acceptable only while access stays limited to the
  proposal and delivery projects inside the same disposable runtime
- local caller auth between the smoke harness and broker remains acceptable
  because it is local-only and resettable

### Secrets

- broker env material and caller secrets remain generated under the local state
  root and are not shared with governed runtimes
- the profile must not pull broker API tokens or caller secrets from governed
  Vault paths
- the profile must fail closed if local backlog or delivery field ids are
  missing instead of guessing governed values

### Delivery

- the profile widens the local backend model from one OpenProject project to
  two, so durable backlinks in both directions are required
- the profile remains acceptable because the delivery handoff is still
  internal-only and does not create a new Telegram operator surface
- the promotion path stays separate: real source commits, PRs, immutable
  artifacts, and governed stage rehearsal

### Runtime

- reusing the real broker runtime against canonical platform-owned local seed
  runners is the correct contract-aligned local shape
- the profile must remain bounded to its declared services and smoke checks
  instead of turning into a general local project-management lab
- the shared runner must continue to control session manifests and profile
  launch behavior rather than letting the repo invent a separate lane

### AI

- this profile does not enable governed AI planning or delivery management
- any future AI-assisted delivery path must remain explicitly local or
  integrated until the governed AI access path exists and is reviewed

## Required Controls

1. the profile uses the shared `dev-integration` runner instead of inventing a
   repo-local lane
2. the local proposal and delivery seed runners come from `platform-engineering`
3. the broker local smoke flow verifies durable backlinks in both directions
4. the delivery handoff remains internal-only and is not surfaced as a
   Telegram command
5. the active profile admission truth stays recorded in
   `workspace-governance`

## Decision

Approved as the second local-only `dev-integration` profile for
`operator-orchestration-service`.

Fresh review is required if the profile starts reusing governed credentials,
touching remote shared scratch infrastructure, or exposing delivery execution
through a public operator surface.
