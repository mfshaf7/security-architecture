# Saved-project preview source review

## Summary

Review the Prototype saved-source connection and managed local browser
address for the existing Epic #1384 plan. Platform owns the running
instance and verified address. The Broker owns the authorized saved-source
command and Console reads the reported outcome.

## Scope Delta

Platform setup read [#395](https://github.com/mfshaf7/platform-engineering/pull/395)
landed at `8c875a020ea14faf1d5ee6994985eab8196b98c7`. Broker
[#441](https://github.com/mfshaf7/operator-orchestration-service/pull/441)
has head `f50d3ff94f34cb07da80241ba07a1851cb42e3bd`.
Platform browser preview [#396](https://github.com/mfshaf7/platform-engineering/pull/396)
has head `90ccce2033ff841dae087b475246a975566be2f5`.

## Review Areas

**Identity and custody.** The new setup read requires the existing
authenticated provider and matches exact scope, source subject and project.
The Broker validates current actor and source session, accepts only the
existing immutable saved command and retains original identity through
reconciliation. The browser has no host-path, credential, repository scope
or platform destination input.

**Runtime.** Browser service uses a loopback listener inside the existing
Platform provider, conditional on its reviewed private port setting. Each
request checks owner admission, current pod identity and the fixed approved
port. A historical operation has no active address. The route filters
credentials and foreign hosts, retains host-only cookies and disables
embedding. Existing workload and paired API isolation remain prerequisites.

**Evidence.** The paired real Git and K3s rehearsal refused unsaved input;
the current Console adapter projected the exact owner address in the
original Run result. Windows Chrome read two successive qualified versions,
rejected other hosts and confirmed route withdrawal on Stop. A subsequent
owner read restored a deliberately closed preview listener without running
the application a second time. Prototype browser coverage includes reopening
the exact address received from Platform through the normal editor button.

## Decision

`approved` under the standing delegated review for the exact Platform and
Broker source heads above. Both required GitHub checks and the connected
candidate rehearsal passed. Acceptance covers guarded source landing.
Each feature still needs its approved Console review packet. The recorded
independent #1413 isolation acceptance and #1418 activation requirements
remain part of the Epic.
