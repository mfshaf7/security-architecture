# Host-Control Domain

## Purpose

This document defines the security architecture view for host-facing operations
triggered from product runtimes.

## Scope

This domain covers:

- typed host-control tools exposed to product runtimes
- host-bridge policy enforcement and audit
- export and media staging
- recovery and supervision paths tied to privileged host actions
- stage versus prod boundary handling for host-connected runtimes

## Core Rule

Product runtimes may orchestrate host-facing actions, but they must not become
the host trust anchor.

That is why the current model uses:

- typed host-control tools instead of generic shell access
- a separate host bridge as the enforcement boundary
- explicit permission tiers
- audit and staging outside the model surface

## Permission Tiers

### Read

Examples:

- health checks
- file listing
- file search
- metadata inspection

### Organize

Examples:

- folder creation
- move and rename operations

### Export

Examples:

- stage file for delivery
- send file through the delivery channel
- capture and send screenshot

### Admin

Examples:

- allowed-root changes
- high-risk host controls

## Principal Risks

- user-facing or model-influenced input shaping privileged host actions
- bridge policy drift between environments
- audit or staging paths crossing environment boundaries
- privileged behavior exposed without deterministic checks or explicit approval

## Control Objectives

- keep host enforcement in the bridge, not in the runtime
- keep policy, audit, and staging outside the model surface
- separate low-risk read behavior from export and admin behavior
- make environment alignment reviewable when stage and prod coexist
- preserve attestation for the running bridge policy and runtime source

## Review Triggers

- new host-control tool or permission tier
- changes to bridge policy, allowed roots, or staging paths
- changes to export, screenshot, or file-delivery behavior
- concurrent stage and prod host-control changes

## Related Views

- [`../components/openclaw-host-bridge/README.md`](../components/openclaw-host-bridge/README.md)
- [`../products/openclaw/README.md`](../products/openclaw/README.md)
- [`../../standards/ai-security-and-governance.md`](../../standards/ai-security-and-governance.md)
