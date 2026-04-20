# Operator Orchestration Service Accepted-Idea Delivery Consume Review

- date: 2026-04-20
- scope: internal consume route from accepted proposal backlog items into the
  separate OpenProject delivery ART project
- owner repo: `operator-orchestration-service`
- related repos:
  - `platform-engineering`
  - `workspace-governance`
- security owner: `security-architecture`
- status: approved-bounded-expansion

## Summary

This expansion is approved as a bounded internal workflow change.

The important control boundary is preserved:

- the broker still owns the workflow seam
- Telegram still does not gain a delivery-management command surface
- OpenProject remains the canonical system of record for both the source
  proposal and the delivery record
- the delivery handoff stays attributable and repairable through durable
  backlinks instead of chat memory

Approved scope:

- `POST /v1/ideas/{idea_id}/consume`
- delivery lookup by `origin_idea_ref`
- source backlink repair through `delivery_ref`
- creation of one top-level delivery initiative in `workspace-delivery-art`

Still not approved:

- public ingress
- Telegram delivery execution commands
- automatic bidirectional synchronization
- multi-ART routing
- governed AI activation

## Review Areas

### Identity

- caller authentication stays on the existing internal broker boundary
- operator identity remains explicit in the consume request and audit stream
- the route does not introduce a new machine identity or broaden caller
  allowlists by itself

### Secrets

- no new secret class is introduced by the consume route
- the same broker-owned OpenProject token is acceptable only while access stays
  limited to the proposal and delivery projects
- Telegram still must not hold backend credentials

### Delivery

- the route widens backend write scope from one OpenProject project to two, so
  project membership and field contracts must stay reviewed and platform-owned
- durable backlinks in both directions are required so partial failures are
  observable and repairable
- the route remains a bounded internal delivery handoff, not a general project
  automation API

### Runtime

- idempotent reuse of an existing delivery record is required to avoid
  duplicate execution artifacts after partial failure
- the broker must not become a generic OpenProject proxy or project browser
- the route is acceptable because it still operates on one broker-owned source
  record and one broker-owned delivery target

### AI

- no governed AI invocation path is introduced by this expansion
- future AI-assisted planning or delivery management would require a separate
  review

## Required Controls

1. source proposals expose durable `delivery_ref` backlinks
2. delivery records expose durable `origin_idea_ref` backlinks
3. the broker rejects consume requests unless the source proposal is already
   `accepted`
4. the delivery handoff remains internal-only and is not surfaced as a
   Telegram command
5. platform-owned OpenProject provisioning keeps the backlog and delivery field
   contracts in sync with the broker runtime

## Decision

Approved as a bounded internal delivery-handshake expansion for
`operator-orchestration-service`.

The security posture remains acceptable because the change improves delivery
traceability without widening the broker into a general delivery controller or
public operator surface.
