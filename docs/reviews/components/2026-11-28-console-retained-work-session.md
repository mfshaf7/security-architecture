# Reopen retained Console Work Sessions

## Summary

A completed item on the live Work Board can reopen its same Work Session
after active source custody has been cleaned up. The underlying final
review is already available through the exact item route.

## Scope Delta

Console presentation is the sole source difference from the previous
decision. The selected card checks the existing Work Session route and
reuses the current session dialog and Broker authorization.

## Review Areas

**Identity and evidence.** The browser receives a saved session action
only after a live current read returns the exact work-item and Delivery
identities and a closed session with its retained cleanup receipt.
A failed check can be retried on the same item. The lookup adds no
mutation, credentials, access grant or workspace-wide index.

**Operating evidence.** On the live prior source, the completed card for
#1386 had no session action while the exact authorized route returned its
closed result. Preview used the current owner responses over a GET-only
connection. It opened the real completed card and showed its original
finalized Broker PR #433 link. The isolated regression and the two
existing grouped completion browser cases passed. Full Console validation
passed, including 1,211 semantics tests, type checks, the production
build and the dependency audit.

The selected item read uses the same retained source evidence and does
not change rollback or the stored outcome.

## Decision

`approved` under standing operator delegation. Confirm the action at the normal live Work Board entry point after activation.

The exact reviewed and merged source for [Console #201](https://github.com/mfshaf7/governance-operations-console/pull/201) is `756bb4778a3ba405617209dba0c1b52fa3ba4a8c` with tree `db472d12bdf8d3a341ac30df233ddae3ec2bf7f9`.
