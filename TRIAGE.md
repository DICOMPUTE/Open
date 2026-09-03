# DICOMPUTE/Open issue triage

This repository is a public issue tracker with no application code. The open issues below are product-level requests and observations that map to implementation work in other repositories, live service configuration, or product decisions. This file records their disposition and the next concrete step for each, as of 2026-09-03.

| Open issue | Title | Disposition | Implementation home | Related internal issues / notes |
|---|---|---|---|---|
| #57 | SSL Labs reporting: TLS 1.0/1.1 still enabled | `needs-cloudflare-config` | Cloudflare dashboard for `dicompute.ai` zone (SSL/TLS → Edge Certificates → Minimum TLS Version) | No code change possible here; follow the issue's 7-step workflow and re-run SSL Labs. |
| #63 | Email sign-in fails outright | `needs-web-repo` | `DICOMPUTE/web` or equivalent (`apps/web/src/routes/login.tsx`) | Not present in `DICOMPUTE/AI`. Needs the web repo and live magic-link/OTP dispatch service logs. |
| #66 | Listen / text-to-speech not working | `needs-deployment-config` | DiCompute chat deployment (`hey.dicompute.ai`) and/or console TTS gating | Likely missing `TTS_PROVIDER`/`TTS_API_KEY`; UI should also hide LISTEN when the backend reports speech unconfigured. Needs service credentials. |
| #84 | Confidential Compute (TEE Workers) | `roadmap / needs-decision` | `DICOMPUTE/AI` | Overlaps `DICOMPUTE/AI#4603` (confidential lanes), `DICOMPUTE/AI#4602` (E2E/direct-path transparency), and `DICOMPUTE/AI#4596` (open security review). Large cross-cutting feature; requires attestation architecture decision. |
| #85 | Data Residency / Region-Pinned Routing | `roadmap / needs-decision` | `DICOMPUTE/AI` (router + agent join + API) | No direct internal duplicate found. Requires `provider.region` design, worker self-declaration, and API parameter. |
| #98 | Agent Development Workspace | `roadmap` | `DICOMPUTE/AI` (console) | No direct internal duplicate. Large feature: integrations, agent registry, trajectory visualization. |
| #103 | Task-Based Training & AutoTrainer | `roadmap` | `DICOMPUTE/AI` (training + models) | No direct internal duplicate. Multi-day feature with dataset/ eval/ recipe/ deployment lifecycle. |
| #106 | Response Execution Details in Chat | `actionable-in-ai` | `DICOMPUTE/AI` (console chat) | Closely related to `DICOMPUTE/AI#4567` (per-request cost in chat). Smaller than the roadmap items above. |
| #107 | Resolve Settlement/Provider-Earnings Messaging | `docs-messaging` | `DICOMPUTE/AI` (provider pages + docs) | Overlaps `DICOMPUTE/AI#4416`, `DICOMPUTE/AI#4417`, `DICOMPUTE/AI#4378`, `DICOMPUTE/AI#4549`. Needs a single LIVE/PILOT/NOT YET LIVE taxonomy decided by product/legal. |
| #108 | Make “Live vs Planned” Status Consistent | `docs-messaging` | `DICOMPUTE/AI` (homepage + docs + console) | Overlaps #107 and `DICOMPUTE/AI#4416`. Requires the same product taxonomy before writers can align copy. |
| #110 | Resolve Conflicting Privacy/Product Messaging | `docs-messaging` | `DICOMPUTE/AI` (homepage + privacy page + demo) | Overlaps `DICOMPUTE/AI#4361` (privacy/terms version history) and `DICOMPUTE/AI#4603`. Needs legal/product sign-off on the exact protection-level vocabulary. |
| #111 | Encrypt Database Files at Rest | `roadmap / needs-decision` | `DICOMPUTE/AI` (ledger/keys/ops) | Complements `DICOMPUTE/AI#4616` (off-box backup) and `DICOMPUTE/AI#4591` (TLS status). Requires key-management decision: managed KMS vs operator-controlled keys. |
| #112 | Off-Site Backup and Disaster Recovery | `actionable-in-ai` | `DICOMPUTE/AI` (ops) | Directly tracked by `DICOMPUTE/AI#4616` (off-box backup of ledger/keys/signup-grants). Human ops step is provisioning the backup destination; in-repo alarm/monitoring work is already in progress. |

## What was done here

- All 13 open issues were reviewed.
- 0 are fixable by committing code to this repository, because this repository contains only issue templates and project metadata.
- The table above routes each issue to the correct implementation surface and names related internal issues where they exist.
- Two items (#106 and #112) are the most tractable in `DICOMPUTE/AI`; the rest are blocked on product decisions, external service access, or another repository.

## Suggested next actions

1. **Close #112** once `DICOMPUTE/AI#4616` lands and the backup destination is provisioned on the live host.
2. **Pick up #106** in `DICOMPUTE/AI` as a console chat improvement alongside `DICOMPUTE/AI#4567`.
3. **Schedule product review** for #107, #108, and #110 to agree on the LIVE/PILOT/ROADMAP taxonomy and privacy vocabulary; then update docs and pages in a single pass.
4. **Route #57** to whoever has Cloudflare dashboard access for the `dicompute.ai` zone.
5. **Locate/clone the `apps/web` repository** for #63 before any engineering work begins.
