# Durable owner result and mounted validator recovery

## Summary

- date: 2026-10-28
- decision: `approved`
- initiative: `openproject://work_packages/1332`
- operating verification: `openproject://work_packages/1346`

Review the bounded maintenance of the existing validation-readiness path. The
actual original run survived lost acknowledgement, exact retry and workflow
worker restart. WGCF then returned a genuine failed validation receipt with an
independent ready repository decision. OOS incorrectly rejected that supported
combination. The failed validator was a Git metadata ownership check in the
read-only mounted governance source, not evidence of corrupted source.

## Scope Delta

Workspace Governance's existing repository structure validator trusts only its
exact resolved repository root for one Git origin read, disables hooks, removes
ambient Git overrides and ignores global/system configuration. It does not
change ownership, trust all directories, persist configuration, fetch source,
invoke a credential helper or relax the expected repository origin.

OOS validates readiness reason counts independently of validation outcome.
A failed validation may coexist with ready repository readiness, while aggregate
readiness remains denied. Ready results still require successful validation,
ready repository readiness and zero reasons. Exact activity/request identity,
source binding, receipt outcome/digest and allowed result fields remain enforced.
No protocol fields, definition version, queue, permission, endpoint, activation
bundle, worker image or architecture are added or changed.

The paired existing finite source decision and source list must select the
actual reviewed owner merges before runtime commissioning. Update the generated
owner change-record index with the OOS repair record. Platform source/tree,
original C786 generation and exact WGCF worker image remain unchanged.

## Review Areas

- runtime: exact-root read-only metadata access under the existing container identity
- delivery: preserve genuine independent owner receipts and aggregate refusal
- identity: no ambient Git override, wildcard trust or caller permission expansion

## Decision

- decision: `approved`
- findings: None
- residual risk: source conformance cannot establish operating success; native original-run recovery and supported retry are required after normal commissioning

The retained real Temporal exchange was accepted as blocked by the corrected
pure decoder. Focused tests verify scoped Git trust, suppressed ambient Git
configuration, genuine origin preservation, independent mixed results,
malformed reason counts and false-ready denial. Exact-head complete owner CI,
human review, hosted checks and merged-source acceptance remain mandatory
before runtime use. Do not replace failed historical evidence or declare this
review to be a completed operating proof.

The existing accepted logical architecture and all human decision gates remain
unchanged. Roll back both owner fixes and their finite source selection together
if commissioning fails; retain the original run, request, failure and receipts.

## Exact source selection

- `workspace-governance@f78b40839862b42c1106eb7f76ba16548eb8df99`
- `operator-orchestration-service@2ba65433b2ef3f78c36143559821c1189c27e463`

Hosted checks passed at the exact Gary heads and both squash trees match.
Native operating proof remains a later commissioning obligation.
