# GitOps And Machine Trust Domain

## Purpose

This document defines the security architecture view for source-to-runtime trust
and machine-controlled delivery.

## Scope

This domain covers:

- protected source repositories
- Argo CD repository access
- GitHub Actions and automation trust
- promotion and environment approval paths
- Kubernetes controller authorization involved in reconciliation

## Boundaries And Interfaces

- source repositories define candidates, not live authority
- `platform-engineering` records approved runtime intent
- Argo CD reconciles approved Git state into cluster state
- controller credentials must be explicit, reviewable, and recoverable

## Key Risks

- repository trust drifting out of managed visibility
- mutable image or source references breaking attestation
- controller credentials hidden outside governed paths
- bypassing GitOps during incident response and never backporting the fix

## Control Objectives

- machine identities should be isolated and scoped to their function
- source-to-runtime trust should be reviewable from repository to controller
- rollbacks should occur through governed state, not live mutation
- promotions should preserve attestation evidence and approval context

## Review Triggers

- new GitHub App, deploy key, or machine credential
- changes to Argo CD repository auth or environment promotion flow
- new controller that can mutate cluster state
- changes to artifact recording or digest pinning logic

## Related Standards And Evidence

- [`../components/argo-cd/README.md`](../components/argo-cd/README.md)
- [`../platform/overview.md`](../platform/overview.md)
- [`../../assessments/platform/2026-04-detailed.md`](../../assessments/platform/2026-04-detailed.md)
