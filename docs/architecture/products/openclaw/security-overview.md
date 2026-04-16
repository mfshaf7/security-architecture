# OpenClaw Security Overview

## Purpose

This document summarizes the security posture of OpenClaw as a product.

## Product Boundary

OpenClaw spans several owner repos and control layers:

- Telegram behavior in `openclaw-telegram-enhanced`
- runtime packaging in `openclaw-runtime-distribution`
- host enforcement in `openclaw-host-bridge`
- rollout governance in `platform-engineering`

Security review should treat those as a coordinated product boundary, not as
independent unrelated repos.

## Why OpenClaw Uses An Isolated Model

OpenClaw is intentionally isolated because combining the following in one place
would create an unsafe trust concentration:

- user-facing chat interaction
- model-assisted behavior
- host-facing execution capability
- operator tooling and shell access
- secrets and recovery-sensitive state

The product therefore keeps:

- Telegram behavior separate from host enforcement
- typed host-control tools separate from raw shell access
- host policy and audit outside the runtime
- rollout approval outside the product repos

## Major Trust Characteristics

- user-facing and model-adjacent interaction surface
- typed host-control boundary that can eventually reach privileged host actions
- separate stage and prod environments governed through GitOps
- sensitive delivery paths for files, screenshots, and callbacks

## Review Focus

- runtime must not become the host trust anchor
- privileged behavior must stay behind deterministic policy gates
- stage and prod drift must remain visible
- Telegram and AI-driven behavior must remain subject to explicit control

## Related Views

- [`data-flow-and-boundaries.md`](data-flow-and-boundaries.md)
- [`threat-model.md`](threat-model.md)
- [`required-controls.md`](required-controls.md)
- [`../../domains/host-control.md`](../../domains/host-control.md)
- [`../../domains/ai-and-agentic.md`](../../domains/ai-and-agentic.md)
