# Withdraw the unqualified Windows health launcher

## Summary

- Date: 2026-11-11.
- Classification: operator-authorized maintenance rollback outside ART.
- Landing Unit Decision: `child_isolated_landing_unit`,
  `withdraw-windows-health-acceptance-20261111`; Security review and generated
  index follow the independently reviewed Host Bridge source withdrawal.
- Decision: approved for source withdrawal and containment only.

Supersedes the [windowless launcher review](2026-11-11-windowless-windows-health.md).
The withdrawn launcher was not successfully commissioned on the installation.

## Scope Delta

[Bridge PR19](https://github.com/mfshaf7/openclaw-host-bridge/pull/19) merges
reviewed Gary head `f87a277f934b515676dca61c76b1db8b84910878` as
`f66a14d1ebf66a412b165c33ff1351c69ccb1d82`. It restores the original CMD,
removes the introduced JScript and withdraws its installation instructions.
The original installed monitor and its local recovery extensions are preserved.
No new runtime, privileged operation, Startup entry or execution path is added.

## Review Areas

Runtime: Kaspersky terminated the operator-private installation process with
`PDM:Trojan.Win32.Generic`. The reported hash matches that installation harness.
Stopping a process, changing Startup and attempting hidden execution are plausible
behavioural triggers; the precise rule and false-positive status are unverified.
A second reported Startup-folder detection lacks an exact filename and cannot
be attributed to either the old CMD or the introduced shortcut.

Containment restored the original launcher bytes and removed the unused new
helper. Both known health Startup entries remain disabled. No exclusion,
protection change, restoration of a quarantined object or alternative launcher
is authorized. The operator selected Windows Console Host as the default;
Windows Terminal remains directly usable for interactive work. This preference
is not evidence that endpoint protection permits automatic health startup.

## Validation And Operating Evidence

The bridge rollback passes all 26 owner tests, committed governance checks
against fetched `origin/main`, and the required hosted check for the reviewed
head. The prior isolated native test did not prove live antivirus compatibility.

The installed monitor's SHA-256 matches its preserved pre-change bytes. An exact
process check found one original monitor already running; no duplicate was
started. Fresh valid Windows health snapshots continued after source withdrawal,
and the Console returned HTTP 200. These observations prove current activity,
not automatic recovery after another logon or reboot. Removing a Startup entry
does not establish that its existing process has stopped.

## Decision

Approved: withdraw the rejected launcher, retain the original monitor and
preserve the endpoint-protection hold in owner guidance. The earlier conditional
launcher approval is superseded and grants no deployment permission.
Automatic health-monitor startup remains unverified; retain the owner record's
hold until the blocked object and security disposition can be established.
Do not recreate a deleted entry under a different name or retry the blocked
deployment. There is no claim of malware absence or a confirmed false positive.

Main agent retains Security closure and final source landing judgment under
standing operator delegation. This review is not independent external
attestation. No ART mutation, Platform activation or Console source pin change
is required for this utility rollback.
