# OpenClaw Required Controls

## Identity

- privileged operator actions should remain attributable
- stage and prod admin exposure should be explicit, not accidental

## Secrets

- runtime secrets should flow from governed platform secret paths
- product code should not become the long-term secret authority

## Delivery

- released behavior should reconcile through approved platform contracts
- stage and prod should remain attestable by source SHA and digest
- any separate Telegram overlay artifact must remain explicitly scoped,
  reversible, digest-pinned, tied to an exact qualified base image, and
  stage-approved before prod promotion

## Runtime

- typed tools only for host-facing operations
- explicit permission tiers for read, organize, export, and admin
- bridge policy and audit must remain outside the model surface

## AI

- prompt and tool paths must treat user input as adversarial by default
- privileged actions require deterministic checks or human oversight
- AI-shaped actions must remain attributable in logs or audit surfaces
