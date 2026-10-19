# DICOMPUTE/Open

The public issue tracker for DiCompute — bug reports, UX gaps and feature
requests for the inference API, console, provider fleet and settlement rail.
No application code lives here; every issue maps to work in another
repository, to live service configuration, or to a product/compliance
decision (see `TRIAGE.md` for how an issue is dispositioned).

## Filing an issue

Use the one enforced format in
[`.github/ISSUE_TEMPLATE/issue.md`](.github/ISSUE_TEMPLATE/issue.md) — it is
the template GitHub offers on **New issue**, and the board's tooling reads
its shape (the eight headings, in order — What / Why / Prompt / Workflow /
Loop / Graph / Layout / Flow — plus the `Severity: Low|Medium|High|Critical ·
Effort: S|M|L` trailer). A checker
(`.github/workflows/issue-template-check.yml`) flags issues that miss it.

## Reading the board

- [All open issues](https://github.com/DICOMPUTE/Open/issues) — the live
  state, by definition.
- [`TRIAGE.md`](TRIAGE.md) — the disposition rules every issue resolves into,
  and what closes one.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) — the organization-wide default.
