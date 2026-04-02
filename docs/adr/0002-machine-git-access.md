# ADR-0002: Machine Git Access For Argo CD Should Move To GitHub App

## Status

Proposed

## Context

PAT-based Git access is serviceable but weak from a least-privilege, audit, and rotation standpoint.

## Decision

Move Argo CD machine Git access to a GitHub App model. PATs are transitional only.

## Consequences

- better auditability and scope control
- reduced dependence on long-lived user tokens
- requires installation, secret handling, and migration planning
