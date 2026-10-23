# Little List Owner-Managed Local Application Security Baseline

## Scope And Decision

Decision: `approved` for owner-managed, non-deployed source ownership of
`console-todo-1275` and nonsensitive browser-local application qualification.
This is product admission evidence for the existing Console journey, not a
new runtime approval or a claim that Delivery or Publication is complete.

The exact reviewed application source is
`console-todo-1275@7efd4c3e87e2d41e10b252daf473db416e03090f`, source PR5,
with finalized Review Packet
`wgcf://artifacts/delivery-art/sha256/73c9c02aaaefc71b72f4e00a4d7fb903514f46ef6ef23048f7a44f9f40ca64eb`.
Native source graduation retained the original Prototype/Delivery identities
and completed with receipt
`receipt://prototype-closure/96c216ceb6bfac70afecf08aefd48645ef66612b46cfbe88f03c1bf6b9ef374e`.

Workspace Intake must classify the real product Proposed before this coverage
entry lands, then update that same canonical record to Admitted before active
Inventory promotion. The earlier unmerged admitted attempt failed the existing
coverage prerequisite and was cancelled; it grants no admission. This review
does not rewrite its history or relax that prerequisite.

## Ownership And Boundaries

- `console-todo-1275` owns the application, source custody, local data behavior
  and owner-local validation. It has no shared orchestration, identity,
  credential, privileged host or release authority.
- `platform-engineering` remains the declared platform owner. This baseline
  does not create a product service, runtime profile, public listener or
  platform deployment. The review inventory's product owner field records that
  platform role; it does not transfer application source ownership.
- `security-architecture` owns this limited product review.
- Workspace Governance owns classification and active Inventory; OOS/WGCF own
  the existing workflow and readiness boundaries. Console submits reviewed
  intent and reads their actual receipts.

The application has no account, backend, cloud synchronization, AI invocation,
runtime third-party dependency or secret-delivery path. Public repository
visibility was accepted for this exercise. It is not proof of private-client
repository operation, public/client service access, sensitive-data handling,
authentication, shared hosting, stage/prod or release readiness.

## Inspected Controls

`app/index.html` loads only the local stylesheet and ES module. Its CSP sets
`default-src 'self'`, `connect-src 'none'`, `object-src 'none'`, `base-uri 'none'`
and `form-action 'none'`. There is no remote script, network adapter, external
form destination or application telemetry.

`app/app.mjs` renders task content with DOM `textContent` and fixed element
construction, rather than interpreting it as HTML. It uses the product's
browser-local storage key. Visible state advances only after storage writes
succeed. Failed writes preserve prior tasks and the unsaved input; unreadable
or corrupt saved data is preserved and editing visibly pauses. Storage events
reread the native same-origin list for other tabs.

`app/tasks.mjs` validates the storage version, bounded array and text sizes,
unique bounded identifiers and boolean completion. It limits lists to500
tasks, text to240 characters and serialized reads to512000 characters. Add,
toggle and delete operate on exact validated identities. These are application
integrity controls, not encryption, authentication, concurrency transactions
or protection from another script/user with the same browser origin. Task
content for this exercise must remain nonsensitive.

The browser verifier serves only four fixed application paths through a
disposable loopback listener, denies other paths/methods, uses isolated serial
Chromium contexts and closes browser/server resources. Its explicit corrupt
storage and write-denial injections are synthetic negative tests. They are
not fixtures or seeded tasks in the application. The verifier rejects external
requests and page errors. It does not create lifecycle or publication evidence.

## Evidence And Limits

The landed owner profile contains nine actual task-unit cases, exact base/head
source validation and seven serial browser cases: empty/whitespace/keyboard
behavior, inert HTML-looking task text, completion and exact deletion across
reload, cross-tab state, narrow layout and long text, honest storage-write
denial, and corrupt-data preservation with editing paused. Code and the
existing source packet are reviewed here; the final accepted-base native
browser witness remains required by the main exercise. No unperformed Console
operation or future receipt is counted as completed evidence.

Admission may proceed only within this owner-managed source boundary after
the normal explicit Intake decision, exact source review, merged readback and
separate active Inventory promotion. Internal Portfolio listing still requires
truthful completed-Delivery/operational owner evidence and its own reviewed
manifest and receipt. A source record, local browser server or successful test
does not independently grant those states.

## Expansion Gates And Review

Sensitive data, accounts, backend synchronization, external integrations,
private-client delivery, public/client hosting, new runtime/deployment,
privileged effects or release promotion require a separate review of the
actual changed boundary. No new implementation or permission is introduced
by this baseline. Review again on a boundary change, or by 2027-04-23.

Landing Unit Decision: feature_single_landing_unit,
maintenance-1275-little-list-product-review. This is the existing1309
non-source Security acceptance artifact; no ART repair item or application
implementation Landing Unit is added.

## Source Evidence

- [Application document](https://github.com/mfshaf7-workspace/console-todo-1275/blob/7efd4c3e87e2d41e10b252daf473db416e03090f/app/index.html)
- [DOM and storage behavior](https://github.com/mfshaf7-workspace/console-todo-1275/blob/7efd4c3e87e2d41e10b252daf473db416e03090f/app/app.mjs)
- [Task and storage validation](https://github.com/mfshaf7-workspace/console-todo-1275/blob/7efd4c3e87e2d41e10b252daf473db416e03090f/app/tasks.mjs)
- [Browser verifier](https://github.com/mfshaf7-workspace/console-todo-1275/blob/7efd4c3e87e2d41e10b252daf473db416e03090f/tests/browser/little-list.mjs)
- [Accepted owner evidence profile](https://github.com/mfshaf7-workspace/console-todo-1275/blob/7efd4c3e87e2d41e10b252daf473db416e03090f/contracts/delivery-art-work-session/evidence-profile.json)
