# Contributing to DiCompute

Thanks for taking the time. This file is the organization-wide default — a
repository that ships its own `CONTRIBUTING.md` overrides it, so check there first.

## Before you open a pull request

- **Open an issue first** for anything beyond a typo or an obvious one-line fix.
  It is cheaper to agree on the approach than to redo the work.
- **One concern per PR.** A bug fix and a refactor in the same diff is two PRs.
- **Never report a vulnerability in a public issue or PR.** See [SECURITY.md](SECURITY.md).

## Pull request expectations

- Explain **what changed and why** — the why is the part reviewers can't reconstruct.
- **Include a test** that fails before your change and passes after it. A fix without
  a regression test tends to come back.
- **Keep the existing style.** Match the surrounding code's naming, comment density,
  and idiom rather than importing conventions from elsewhere.
- **Green checks.** Every repository gate must pass. A red CI run is not ready for review.
- **A human merges.** Contributors do not merge their own pull requests.

## Commit messages

Write a short imperative subject line that says what the commit does:

```
Reject unenumerated upstreams instead of falling back to plaintext
```

Reference the issue it closes in the body, not the subject.

## Money path and security-sensitive code

Changes touching metering, billing, the ledger, settlement, key handling, or trust
boundaries get a stricter review and need an explicit test for the invariant they
preserve. If your change makes accounting or authorization *simpler*, say so
plainly in the description — that claim is exactly what a reviewer needs to check.

## Reporting bugs

Use the issue templates. The two things that most often decide whether a bug gets
fixed quickly are **exact reproduction steps** and **what you expected instead**.

## Conduct

Participation is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).
