# Authorize the existing post-merge verification action

## Summary

Review the exact Broker [PR #436](https://github.com/mfshaf7/operator-orchestration-service/pull/436).
The Gary-authored head is `5d0a5d970a2cfe1476aa9092317ab6fe750908db`. Its reviewed tree is `57a25c454523e8ae3a8977d4331a78d6c6cfaae2`.

## Scope Delta

An authenticated operator can continue operating evidence and Review Packet
finalization for the exact merged session after its source write approval
expires. The Broker reads the canonical next action and retained reviewed
checkout. Every allowed transition checks either the exact merged Review
Packet or the validated finalization draft that follows it.

## Review Areas

- **Identity and access.** The command retains caller/operator identity,
  optimistic revision checks under the session lock, and the existing
  executor context. Replays keep their original command receipt.
- **Delivery and runtime.** The bounded continuation permits operating
  acquisition and finalization transitions. Actual source preparation,
  other source effects, and publication use the existing source approval
  and private executor lease. Scope and packet validation stay in the owner.
- **Evidence.** The connected Console preview used disposable ART and PR
  records, the candidate Broker action, and the four actual named Platform
  owner readbacks. One canonical command obtained a result, replay returned
  its receipt, and no source preparation or lease was requested. The real
  lifecycle tests cover finalization and refusal of pre-merge transitions.
  Local checks passed 2,093 tests with two skips.

## Decision

`approved` for the exact source delta above. The composed source decision
and the ordinary Platform rollout govern live use. The original #1386
operating profile binding remains a separate evidence recovery decision.
