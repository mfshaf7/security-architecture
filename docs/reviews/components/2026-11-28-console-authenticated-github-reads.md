# Authenticated GitHub reads for Console workflows

## Summary

Five anonymous GitHub REST reads in the existing Console composition are
moved to its authenticated read paths. The maintenance change covers
Registry visibility, Repository Setup, Prototype transfer, Gary admission
and Publication freshness.

## Scope Delta

Registry uses the connected Repository Custody metadata reader. Setup and
Prototype transfer use the protected Platform source interface. Gary source
admission and Publication use a finite Source App read lease for one exact
repository. Platform continues to own issuance and revocation. Broker and
Console carry bounded results under their existing operator workflow.

## Review Areas

**Identity and custody.** Platform binds the Source App lease to the admitted
provider repository ID and read-only contents and metadata permissions.
Protected setup and transfer check accepted operator, caller and owner
authority before inspecting source. The Prototype import uses the reviewed
merge and manifest, validates the exact provider repository, and rechecks
the current main revision before returning proof. Release of a read lease
must be confirmed for successful setup and transfer.

**Delivery and runtime.** Gary admission confirms current Workspace
Governance main before issuing a write credential. Publication observes the
existing registered product and keeps unverified freshness distinct from a
proven current source. Registry distinguishes unproven visibility from
private visibility. GitHub throttling and missing access produce distinct
results. Existing Git-backed setup results remain readable. The new
credentialed result requires evidence of the exact accepted read scope and
revocation.

**Verification.** The connected isolated rehearsal ran the Console adapter,
the Broker HTTP endpoint and the protected Platform service against an
isolated GitHub responder. It passed Repository Setup success, throttling,
missing access and exact Prototype source verification. All seven test
grants were revoked. Separate live read-only checks confirmed the existing
metadata connection and scoped Source App read and revocation. The
Platform, Broker and Console checks are recorded with the authored source
review. The candidate composition must still complete operating readback
after activation.

## Decision

`approved` for these exact reviewed owner trees under the standing delegated review. Use Platform's existing coordinated activation. Verify operating readiness and the affected Console and provider reads on the accepted composition.

| Owner | Reviewed PR | Merged revision | Reviewed tree |
| --- | --- | --- | --- |
| platform-engineering | [#394](https://github.com/mfshaf7/platform-engineering/pull/394) | `4e5fc2dd368022bbd1440f8558edef8ffacde139` | `ead72654203b8e23fa28b8056d3ccbc10ed55ee9` |
| governance-operations-console | [#199](https://github.com/mfshaf7/governance-operations-console/pull/199) | `851b6825fac2930dbece9cbda6ee60a59d122e2f` | `f01ce0058006cc9dc0785453669088b33fafafbe` |
| operator-orchestration-service | [#438](https://github.com/mfshaf7/operator-orchestration-service/pull/438) | `39fa5198d084608d5f7b00d5694fd26f4d2c66f7` | `e5a245812e9076c4a3813aff258a3886a039e312` |
