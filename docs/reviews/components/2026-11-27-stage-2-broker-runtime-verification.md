# Stage 2 Broker operating verification and Console action

## Summary

Review the exact Broker verifier in [PR #435](https://github.com/mfshaf7/operator-orchestration-service/pull/435)
and the merged Console action in [PR #197](https://github.com/mfshaf7/governance-operations-console/pull/197).

| Owner | Reviewed revision | Exact tree |
| --- | --- | --- |
| Broker | `6c833113fd26bae6f2b96a554bf11d6d30d4f894` | `ef85a2f75078ffbac33307bfcf463c401fd16f06` |
| Console | `c29ba97f2285db66723e25ab9bdc28e65b496bb9` | `01ab96602878cf70ad58387fe16c538610656ec6` |

## Scope Delta

The Broker now reads retained observations for its two approved operating
cases. The Console presents the existing Continue action as **Verify Runtime
Results** and keeps technical owner diagnostics available.

## Review Areas

- **Delivery.** The profile binds one read-only command to each approved
  case. The reader requires the exact Broker revision, paired reviewed
  Platform source, completed rehearsal, private receipt ownership, and record
  digest. Missing and mismatched receipts fail.
- **Runtime.** The rehearsal runs separately on an admitted disposable
  Dev Integration target. The recorded result follows namespace cleanup.
  The restart retained the original Run and produced one dispatch. The
  six invalid source and replay inputs dispatched zero operations and the
  original snapshot and owner state remained intact.
- **Operator authority.** The Console exposes the existing governed work
  action through the existing caller-bound Continue route. Preview covers the
  verification entry and retry. The deployed Console must read the recorded
  result before closeout.

The exact Broker rehearsal passed both owner case readers. Local validation
passed 2,092 Broker tests with two skips, and 1,206 Console semantic tests,
build, typecheck and dependency audit. Preserve the exact earlier Broker
and Platform evidence through the existing recovery and recording route.

## Decision

`approved` for the exact source delta listed above. Deployment requires the
existing composed source decision and Platform readiness readback. ART
closure requires acquisition of the approved operating results.
