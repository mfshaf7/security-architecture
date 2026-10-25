# Lifecycle context Unicode wire compatibility

## Summary

Approve the existing lifecycle-boundary correction at
`operator-orchestration-service@8827eaa66d97ba0b247b4238aa577794d7501b65`.
Gary PR379 merged reviewed candidate
`38245855aeee337ea934cbfb86c18fe77b8cbc8a` after accountable exact-head review
and successful CI40164087886. The [paired composed decision](2026-10-24-configurable-ai-routing.yaml)
and [source review](2026-10-24-configurable-ai-routing.md) remain the activation
authority. CGG source and its existing protocol remain unchanged.

## Scope Delta

Actual1328 Console preparation, exact source authorization and the scoped
Prototype session succeeded. Optional generation then failed before model
dispatch. Read-only replay of its exact retained context request through the
commissioned client proved CGG HTTP400, `context_projection_invalid` and
`sources_digest does not match the canonical source list`.

Both OOS authoring producers used the ART UTF-8 hash for CGG source lists, and
their shared response validator expected the same bytes for the projection
envelope. The established CGG lifecycle format is compact sorted ASCII-escaped
JSON. This correction confines that format to the existing wire boundary:
Prototype and Delivery source-list digests, retained Prototype wire validation
and shared CGG response-envelope integrity. Source text, UTF-8 content digests,
ART/Landing/internal custody and historical source records stay unchanged.
There is no dual-codec fallback or CGG protocol change.

The client also retains the actual FastAPI error's nested owner code and
retryability through its existing bounded error projection. Private upstream
details are not exposed. No new endpoint, service, schema, activation flag,
architecture version, source grant or model entitlement is introduced.

## Review Areas

Identity and secrets retain their existing scopes and custody. Runtime and AI
context admission still bind the exact caller, operator, source, session,
execution, budget, redaction/custody receipts and denied authority. Unicode
compatibility neither selects a model nor authorizes inference, raw context,
source acceptance/application, baseline approval or runtime activation. Delivery
and Prototype retain separate subjects under the same established projection
boundary. Changed content, wrong envelopes, replay conflicts and unauthorized
callers remain denied.

Three new regressions fail before repair; all36 focused context, realization
and operator-draft cases pass afterward. Independent Python serializer checks
include accented, CJK, astral, DEL, BOM and CRLF data and verify preserved source
bytes. Full OOS tests pass1637 cases with two existing optional skips. The13
remaining owner checks, fetched-base committed gates and API/worker image smoke
pass. The worker remains fail closed by default.

Nine additional isolated cases execute the actual OOS producers, client and
consumer against the actual CGG FastAPI/Python pipeline and private local stores.
They prove both authoring routes, immutable owner replay, old ART-frame denial,
changed-content replay conflict, caller denial, wrong envelope denial and typed
owner-error propagation. Work/session/source and caller credentials are
synthetic; this is actual protocol proof, not live model or runtime
qualification. The earlier failed generation remains retained without a draft,
model dispatch, source application or commit.

## Decision

- decision: `approved`
- scope: exact merged OOS repair and its indexed security-tagged owner record in
  the existing local dev-integration composition. All other exact source/tree/
  architecture bindings and the finite decision/gate remain unchanged.
- operating requirement: normal exact-source activation/status, then an
  explicitly linked generation retry in the same original source request and
  session. Finish actual Prototype editor/import/amendment/reload/cancel proof
  in1328 and actual LittleList source delivery in1329 before initiative closure.

Do not rewrite a retained failed request or use raw context to complete proof.
The existing approved exact source scope and owner history remain authoritative.
The delegated accountable reviewer retains Security closure and final landing
judgment; no sub-agent was used. No broader private-client or stage/prod
qualification is granted.
