# DICOMPUTE/Open issue triage

This repository is a public issue tracker with no application code. Nothing here
is fixable by committing code to this repository — every open issue maps to
implementation work in another repository, to live service configuration, or to a
product/compliance decision. This file records the disposition and next concrete
step for each.

**Reviewed against the real tree and the decision record on 2026-09-04.** Where
an issue is settled by a standing decision, the decision is named; where the
implementing change has already merged, the PR is cited.

## Open issues

| Issue | Title | Disposition | Next concrete step |
|---|---|---|---|
| #57 | SSL Labs: TLS 1.0/1.1 still enabled | `needs-cloudflare-config` | No code change is possible. Cloudflare dashboard for the `dicompute.ai` zone → SSL/TLS → Edge Certificates → Minimum TLS Version, then re-run SSL Labs. Needs whoever holds dashboard access. |
| #84 | Confidential Compute (TEE Workers) | `roadmap / needs-decision` — tracked internally | Direct internal counterpart exists: **`DICOMPUTE/AI#5049`**. Blocked on an attestation-architecture decision, not on someone starting work. |
| #98 | Agent Development Workspace | `roadmap` — tracked internally | Direct internal counterpart exists: **`DICOMPUTE/AI#5047`**. Large multi-part feature (integrations, agent registry, trajectory visualization). |
| #103 | Task-Based Training & AutoTrainer | `roadmap` — tracked internally | Direct internal counterpart exists: **`DICOMPUTE/AI#5046`**. Multi-day feature with dataset / eval / recipe / deployment lifecycle. |
| #111 | Encrypt Database Files at Rest | `partially shipped / remainder needs an operator` | Settled by **decision 0124**. See below — this one has moved. |
| #121 | Website "Cleaner" Section — Refresh & Bug | `not actionable as filed` | The issue is a generic prompt template for refreshing "a section" and never names which section of this product is wrong, so there is nothing to verify or fix. Needs a named section plus the actual defect, or it should be closed. |
| #123 | ISO 27001:2022 Certification Pursuit | `needs-decision (business process)` | Not a code change, as the issue itself states: gap assessment, ISMS documentation, and an accredited certification body. Needs a budget//timeline owner. Overlaps the evidence gathering in the open security-review issue. |
| #128 | X/Twitter @dicompute link is broken | `needs-external-fact` | See below — the repository side is already correct. |

## #111 — what actually shipped, and what did not

Decision **0124** ("Database encryption at rest: the live volume, not the store
code, is the actual gap, and it needs an operator with root, not a PR") splits
this issue in two, and the two halves have very different status:

- **Field-level encryption of specific secrets: shipping.** The narrow slice
  0124 identifies as in-scope has landed — organization SSO client secrets are
  now AES-256-GCM encrypted at rest with a 12-byte per-call nonce, a verified
  tag, and the owning `orgId` bound in as AAD so a ciphertext copied from
  another org's row fails to open rather than decrypting.
  (`DICOMPUTE/AI#8743`, merged 2026-09-04.) Two earlier precedents already did
  the same for other secrets: admin 2FA material and scheduled-prompt
  credentials.
- **The actual reported gap — whole database files — has not moved.** Roughly
  31 independent `bun:sqlite` stores still sit as plaintext files on the live
  volume. 0124 is explicit that the only real fix is putting those directories
  on an encrypted volume, that this means re-partitioning hosts holding the live
  ledger and signup data, and that the risky irreversible step has to be run by
  someone with hands on the boxes. It is filed **Proposed, not decided**,
  blocked on two questions that are operational rather than technical: who has
  root on the deploy hosts, and what key-custody model the unattended-reboot
  contract is willing to trade away.

Worth stating plainly because it is easy to misread as progress: the encrypted
**backup archive** that already exists is not at-rest encryption, and the deploy
documentation says so in those words.

**Recommendation:** keep #111 open as the operator-facing tracker for the volume
work, and do not treat #8743 as closing it.

## #128 — the repository side is correct; the destination is the open question

Verified against the tree rather than assumed. The link is not hardcoded and is
not inconsistent:

- `apps/console/lib/site.ts` resolves `SOCIAL_X_HANDLE` (or
  `NEXT_PUBLIC_SOCIAL_X_HANDLE`) with a `dicompute` fallback, and derives
  `SOCIAL_X_URL` from it.
- The two consumers — the `/help` page and the sidebar help menu — both read
  that seam, and a regression test asserts they do rather than re-hardcoding a
  literal.
- Every occurrence of an X URL in the tree resolves to `https://x.com/dicompute`.
  None of the 14 static landing variants carries an X link at all.

So the reported symptom can only be true if the destination account itself does
not exist or has been renamed — an external fact this repository cannot check. If
the handle is wrong, the fix is one environment variable (`SOCIAL_X_HANDLE`) and
no code change; **someone who owns the account needs to supply the correct
handle.** If the account is fine, the issue should be closed as not reproducible.

One unrelated inconsistency found while checking: `apps/console/public/llms.txt`
hardcodes the handle outside the seam, so a white-labeled deployment would still
publish the original operator's handle in that one file. Minor, and separate
from this issue.

## Closed since the previous revision of this file

Eight issues the earlier draft of this table listed as open have since been
resolved: **#63** (email sign-in), **#66** (Listen/TTS), **#85** (data residency
/ region-pinned routing — implemented with a hard region filter that fails
closed, so a worker declaring no region is excluded rather than admitted),
**#106** (response execution details in chat), **#107**, **#108**, **#110** (the
three messaging-consistency issues), and **#112** (off-site backup).

## Summary

- 8 issues open; **0** are fixable by code in this repository.
- 3 are already tracked by direct internal counterparts (#84, #98, #103) — the
  earlier draft of this file wrongly recorded these as having no internal
  duplicate.
- 2 need a person with external access: Cloudflare (#57) and the X account
  (#128).
- 1 is a business/compliance process (#123).
- 1 is blocked on operational decisions recorded in 0124 (#111).
- 1 is not actionable as written (#121).
