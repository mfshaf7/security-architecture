# Technical Plan dependencies and owner error reporting

## Summary

Review the Console maintenance batch that exposes the existing Delivery
dependency operation and preserves actionable Technical Plan errors. Inherit the
[current composed source review](2026-11-19-delivery-principal-identity.md).
Gary authors implementation; the main agent retains Security closure and
exercises standing delegated human review and merge authority. This is not
independent assurance.

## Scope Delta

Work Structure reads the canonical dependency relations with its existing owner
projection. Named prerequisite choices affect only the local selected tree
draft. Explicit Review and Apply submit the existing `manage_dependency`
operation through the same same-origin Console server and OOS change-control
writer. No browser credential, new backend writer, identity scope, AI action or
automatic dependency submission is introduced.

Unchanged external links, lag and supporting notes are preserved. Self-links,
cycles visible in the loaded tree and missing local references block review;
these client checks do not replace native validation of the complete graph.
Creation precedes commands that require the new work-item identities, and old
edges are cleared before replacements. A rejected or uncertain command stops
the sequence. Applied steps remain visible, remaining commands retain their
review context, and readback can be retried without repeating acknowledged
effects. Exiting partial work distinguishes recorded changes from discarded
local input. Each next command binds the last accepted owner revision.

The shared Delivery adapter preserves native machine error identifiers carried
under `error`, with explicit `code` precedence and original HTTP status. Prose
does not become an error identifier. Technical Plan projects only string
validation findings from `errors` and `material_errors`; arbitrary owner
details remain outside the response. Local edits and new attempts clear stale
findings. A missing plan remains distinct from denied access or owner failure
and grants no execution exemption.

## Review Areas

- Delivery and identity: existing caller/operator bindings, explicit acceptance,
  optimistic revision enforcement, command identity, native relation rules and
  owner receipts remain authoritative. The advisor still edits only admitted
  narrative fields and cannot submit or approve dependency changes.
- Secrets and data: no new credential path, directory enumeration, source
  archive, automatic model context or public operational record is added.
  Error projection is restricted to the established string findings.
- Runtime: exact-source acceptance and normal Platform commissioning remain
  required. Source tests and synthetic browser responses do not certify a live
  ART mutation. Existing source/data/history and the pending plan are retained
  during rollout and recovery.

## Evidence

Native read-only evidence established the missing-plan error envelope and the
empty current dependency set. The current owner correctly rejects a proposed
plan whose order differs from recorded ART; this review does not weaken that
check or treat an unfinished plan as a backend defect.

Source tests cover native error shapes, permission/service separation,
preserved metadata/external links, clear-before-set order, new identity
resolution, self/cycle rejection and failed validation inspection. Browser
qualification uses explicitly synthetic transport for review, progress,
rejection/retry and result handling. Native qualification follows exact-source
commissioning and must use the actual Console and original owner receipts.

The final owner source passed 1,181 semantic tests, all architecture guards,
TypeScript, production build, repository/public-source validation and a zero
vulnerability production dependency audit. Focused change-adapter checks passed
14 cases and Technical Plan adapter checks passed eight. The isolated browser
walkthrough preserved external link metadata, rejected a cycle before any
write, reviewed the exact dependency delta, displayed partial progress after
an owner rejection, retried only the remaining change and reopened canonical
readback. Its layouts were inspected at 1700 and 1280 pixel desktop widths.
The validation-findings browser check also passed. These transport fixtures
are explicitly synthetic and are not operating evidence.

## Decision

`approved` for this bounded use of the existing authenticated writer and safe
error projection, subject to passing final owner validation and exact-source
binding before commissioning. No Stage/Prod, shared project runtime or Epic
implementation approval is granted. Retain the prior accepted composition as
rollback source and preserve canonical data and the reviewed plan.

## Exact source acceptance

[Console PR189](https://github.com/mfshaf7/governance-operations-console/pull/189)
merged as `56cb4e3ccb933c666be8d516070b3b6f755bdd66`. The exact Gary candidate
`7e9aca85822cb79bd168014196a178e5359bd74a` passed required provider CI and the
reviewed local checks. Candidate and merged trees are identical. The main agent
performed delegated human review and merge; the temporary source grant and
branch were retired with strict owner cleanup. The existing composed decision
binds this merged Console revision while preserving all other accepted pins.
