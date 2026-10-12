# OOS Delivery ART Human Ruleset-Bypass Delta Review

- date: 2026-10-12
- scope: bounded use of the existing human repository-policy bypass by the Delivery ART `work merge` path
- owner repo: `operator-orchestration-service`
- security owner: `security-architecture`
- status: approved

## Summary

The correction is approved. It allows the existing Delivery ART merge executor
to invoke GitHub's administrator merge mode only after the active identity is
the admitted human reviewer and the existing exact pull-request, exact-head,
approval, check, and durable Review Packet gates have passed. It does not grant
Agent Gary review, merge, or repository-administration authority.

## Scope Delta

The current managed path performs a normal squash merge after proving the
approved immutable head. The active single-human-reviewer repository ruleset
then blocks the same accountable human whose configured bypass is intended to
resolve that boundary. The proposed owner-repo change adds `--admin` to that
final GitHub merge invocation while retaining `--match-head-commit` and every
pre-existing eligibility check.

No new identity, credential, secret, public endpoint, GitOps controller, or
general-purpose administrative command is introduced. The bypass remains
reachable only through the bounded source adapter after deterministic workflow
authorization.

## Review Areas

### Delivery

- design intent: the accountable human reviewer remains the only approval and
  merge authority; Agent Gary remains source author and PR publisher only.
- implemented control: the adapter re-reads the open PR, verifies its base and
  exact head, requires an approval from the admitted reviewer on that head,
  asserts active human merge authority, preserves `--match-head-commit`, and
  requires exact merged readback.
- operating evidence: owner-repo tests and CI must pass before landing; the
  repaired runtime must then merge work item 1253 and return the exact merged
  head before closeout.

### Runtime

- design intent: repository-policy bypass is a final transport option, not a
  substitute for workflow authorization or evidence custody.
- implemented control: no caller can select arbitrary merge arguments or a
  different PR; the executor derives the target from the durable work session
  and fails closed on identity, review, base, URL, or head drift.
- operating evidence: activation remains limited to the existing local
  `dev-integration` profile until the repaired source is merged and refreshed.

## Residual Risk

The human GitHub identity retains repository-level bypass capability outside
OOS. This change does not widen that existing provider permission. Inside OOS,
misuse remains bounded by the exact identity, approval, immutable-head, and
durable-evidence checks. A live retry of work item 1253 is required to prove
the configured ruleset and provider behavior.

## Decision

`approved`

Security closure and final landing judgment remain with the accountable human
reviewer. Approval is conditioned on the owner-repo regression test retaining
both `--admin` and `--match-head-commit`, clean CI at the exact PR head, and
successful exact merged-head readback through `work merge`.
