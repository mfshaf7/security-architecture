# Identity And Access Domain

## Purpose

This document defines the security architecture view for human identity, machine
identity, and break-glass separation across the platform.

## Scope

This domain covers:

- GitHub and protected-branch workflows
- Argo CD operator and machine access
- Vault operator and machine access
- Kubernetes service-account trust
- host-level administrative access

## Boundaries And Interfaces

- humans must remain distinct from machine identities
- routine operator access must remain distinct from break-glass access
- controller and automation identities must be reviewable and least-privileged
- product authorization must not bypass platform identity controls

## Key Risks

- shared administrator credentials reused across several control planes
- weak attribution because several actions collapse to the same credential
- machine identity paths hidden inside local config or unmanaged secrets
- break-glass access normalized into daily operations

## Control Objectives

- human privileged access should use federated identity where supported
- machine access should use dedicated, scoped identities
- break-glass credentials should be separate, rare, and reviewable
- role mapping should be group-based and explicit
- identity changes should have an approval path and evidence trail

## Review Triggers

- new operator role or admin group
- new controller, automation, or GitHub App
- any change to Argo CD, Vault, or Kubernetes auth model
- any change that widens host administrative access

## Related Standards And Evidence

- [`../../standards/identity-and-access.md`](../../standards/identity-and-access.md)
- [`../platform/trust-boundaries.md`](../platform/trust-boundaries.md)
- [`../../assessments/platform/2026-04-detailed.md`](../../assessments/platform/2026-04-detailed.md)
