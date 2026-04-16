# Secrets And Recovery Domain

## Purpose

This document defines the security architecture view for secret custody,
controller secret delivery, and recovery-material governance.

## Scope

This domain covers:

- Vault as secret authority
- External Secrets delivery into runtime namespaces
- controller credentials and repository secrets
- recovery material for Vault and other break-glass paths
- secret rotation, storage, and post-use review expectations

## Boundaries And Interfaces

- secret authority should remain centralized in Vault where supported
- delivery controllers should consume least-privileged, reviewable trust paths
- recovery material should be governed separately from routine credentials
- product runtimes should consume secrets, not become the secret authority

## Key Risks

- static shared credentials with unclear owners
- recovery material depending on operator memory or local disk copies
- controller secret paths that exist but are not reviewable or reproducible
- secret delivery that breaks under recovery because bootstrap steps are not
  formalized

## Control Objectives

- every privileged secret should have an owner, storage location, and rotation
  model
- recovery material should have explicit custody and drill expectations
- controller secrets should be declarative and attributable
- bootstrap and re-bootstrap paths should be documented and testable

## Review Triggers

- new secret path or credential class
- changes to Vault auth, secret engines, or recovery handling
- changes to External Secrets store configuration
- any change that introduces local copies of high-sensitivity material

## Related Standards And Evidence

- [`../../standards/secrets-and-recovery.md`](../../standards/secrets-and-recovery.md)
- [`../components/vault/README.md`](../components/vault/README.md)
- [`../components/external-secrets/README.md`](../components/external-secrets/README.md)
- [`../../assessments/platform/2026-04-detailed.md`](../../assessments/platform/2026-04-detailed.md)
