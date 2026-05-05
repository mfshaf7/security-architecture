# Context Governance Gateway Service Mode Security Requirements

## Purpose

Define the security requirements that must be satisfied before
`context-governance-gateway` can operate as a shared service instead of a
local-only CLI/source tool.

These requirements are admission gates. They do not approve a runtime by
themselves.

## Admission State

- current approved state: local CLI/source evidence only
- proposed next state: service-mode implementation after security and platform
  gates are complete
- blocked until gates: API listener, workers, shared metadata store, shared
  artifact store, dashboard upload, broker adapters, WGCF adapters, scanner
  execution, model invocation, stage, and production

## Required Contracts

### Identity And Authorization

Service mode must define:

- service identities for API, worker, maintenance, and migration roles
- caller identities for CLI, CI, OOS, WGCF, operator console, and future
  adapters
- operation-level authorization for capture, pack, project, inspect, retention
  deletion, debug override, profile administration, and policy changes
- human operator attribution for approval, override, deletion, and exception
  paths
- audit correlation fields linking request id, caller, operator, artifact
  digest, packet id, receipt id, and ledger event id

Minimum denied patterns:

- anonymous projection
- shared production caller secret as the long-term identity model
- borrowing OOS, WGCF, platform, or security authority identities
- allowing CGG evidence to mutate ART, platform release state, workspace
  contracts, security findings, or governed model profiles

### Artifact Custody

Shared custody must define:

- raw artifact store
- redacted artifact store
- manifest, packet, receipt, and ledger metadata store
- encryption at rest
- access control by artifact class
- digest algorithm and collision-resistant artifact identity
- backup and restore posture
- deletion and legal-hold behavior
- operator visibility without raw body exposure by default

Raw and redacted artifacts must be logically separated. Receipts and model-safe
packets must reference raw artifacts by digest and location metadata instead of
embedding raw bodies.

### Retention And Deletion

Retention policy must define:

- default retention period by artifact class
- maximum retention period for raw artifacts
- deletion trigger and approval role
- deletion receipt fields
- legal hold or incident hold behavior
- evidence retained after deletion, including digest, manifest metadata,
  deletion decision, operator, reason, time, and ledger reference

Deletion must not silently erase the audit trail. If raw artifact deletion is
approved, the ledger must still preserve enough metadata to prove what was
deleted, why, by whom, and under which policy.

### Debug Override

Debug override is exceptional access, not a normal projection mode.

Every debug override must include:

- operator identity
- caller identity
- artifact digest
- reason
- approved scope
- expiry
- reviewer or approval reference when required by policy
- denied or suppressed fields that remain unavailable
- ledger event id

Minimum denied patterns:

- indefinite override
- override without operator attribution
- override that sends raw artifacts to a model by default
- override that changes retention or deletion policy without a separate
  authorized operation

### Tamper-Evident Ledger

The ledger must record security-relevant events for:

- capture
- redaction
- projection
- packet creation
- receipt creation
- retention decision
- deletion decision
- debug override
- policy/profile decision
- denied projection
- adapter handoff

Each event must include stable ids, actor metadata, artifact digest or packet
id, event time, outcome, and previous event hash or equivalent tamper-evident
linkage once shared service mode is active.

### Packet Projection

Model-safe and operator-safe packets must be:

- purpose-bound
- profile-bound
- budgeted
- redacted
- reference-based for raw artifact evidence
- explicit about denied and suppressed material
- traceable to artifact digest, manifest, receipt, and ledger event

Raw projection must fail closed when secret-like material or uncertainty is
detected unless a future approved profile explicitly allows a bounded
exception.

### Downstream Consumers

Downstream consumers must treat CGG output as context evidence, not approval
authority.

Adapters to OOS, WGCF, CI, operator console, LiteLLM, OpenClaw, Ollama, or any
other tool must preserve:

- caller attribution
- profile id
- packet id
- receipt id
- denial and suppression metadata
- audit correlation id
- human approval boundary where required

No downstream adapter may request raw artifacts by default.

## Service Mode Review Gate

Runtime implementation may start only after:

- this requirements artifact is current
- the dated service-mode security delta review is current
- the platform gate defines deployment, persistence, backup, restore, release,
  and rollback controls
- the ART plan records the dependency or waiver explicitly

Runtime activation may happen only after:

- implementation evidence maps to every required contract above
- platform runtime profile and release gates are satisfied
- security review is refreshed against implemented behavior
- operator docs explain the normal and exceptional paths
- validation proves default raw projection denial and ledger evidence behavior
