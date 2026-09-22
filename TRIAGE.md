# DICOMPUTE/Open issue triage

This repository is a public issue tracker with no application code. Nothing here
is fixable by committing to this repository: every open issue maps to
implementation work in another repository, to live service configuration, or to
a product/compliance decision.

## Why this file no longer lists issues

It used to. Until 2026-09-22 this file carried a table headed "Open issues" with
eight rows and a summary line reading "8 issues open". By then **all eight were
closed**, and **47 issues were open, none of them mentioned**. The table had been
accurate when it was written on 2026-09-04 and was wrong about every row
eighteen days later, silently, because nothing made it wrong out loud.

That is the failure DICOMPUTE/Open#568 reported, and a hand-rewritten table
would only reset the clock on it. A snapshot of a live list, stored somewhere
that does not change when the list does, goes stale as fast as the list moves —
and this list moves daily. The issue list itself is the live view and always
right:

- **[All open issues](https://github.com/DICOMPUTE/Open/issues)** — the actual
  state, by definition.
- Per-issue disposition lives in a comment **on that issue**, where it is
  attached to the thing it describes and disappears from view exactly when the
  issue is closed.

So this file keeps only what is genuinely durable: the rules for how an issue
here gets dispositioned, and the small number of standing facts that are true
across issues rather than about one of them.

## Disposition rules

Every issue filed here resolves into exactly one of these. The label is the
disposition; the next step belongs in a comment on the issue.

| Disposition | Meaning | Who unblocks it |
|---|---|---|
| `tracked-internally` | Real work, with a counterpart issue in the implementation repo. | Whoever picks up the internal issue. Cite its number in a comment. |
| `needs-operator` | No code change is possible or sufficient; needs someone with access to the live hosts, DNS, or a third-party dashboard. | A person with that access. |
| `needs-decision` | Blocked on a product, business, or compliance call rather than on implementation. | The owner of that call. |
| `not-reproducible` | Measured against the live surface and the reported symptom does not occur. | Close it, with the measurement in the comment. |
| `works-as-designed` | The behaviour is real and intended; the report is a misreading, or asks for a policy change. | Close it, naming the decision or the code comment that records the intent. |
| `not-actionable-as-filed` | The report does not name a surface, a symptom, or a reproduction, so there is nothing to verify. | The reporter. |

Two rules that have repeatedly mattered here:

- **Close with evidence, not with a verdict.** A close comment should carry the
  command that was run and its output, or the file and line that settles it.
  Several issues in this tracker were filed because an earlier close said "fixed"
  with nothing a reader could check.
- **A wrong diagnosis in a correct report is worth saying out loud.** More than
  one issue here has reported a real symptom with a cause that turned out to be
  something else; implementing the prescribed fix would have changed nothing and
  hidden the real one. Verify the mechanism, not just the symptom.

## Standing facts

These are true across issues, not about any single one, which is why they
survive here rather than in a comment.

- **This repository accepts no code.** A fix lands in the implementation
  repository; the issue here is closed by reference to it.
- **Decision records are authoritative.** Where a standing decision settles an
  issue, name the decision rather than re-arguing it. Several recurring topics
  (at-rest encryption, fleet-path activation, cross-origin key custody) are
  already settled that way.
- **An encrypted backup archive is not encryption at rest.** This has been
  misread as progress on the at-rest question more than once; the deploy
  documentation says so in those words.
- **External facts cannot be verified from the tree.** Whether a DNS record, a
  social account, or a dashboard setting is correct is not answerable by reading
  code, and an issue that turns on one is `needs-operator` no matter how it was
  filed.

## Keeping this file honest

Everything above is a rule or a standing fact: it is wrong only when the
practice changes, not when an issue is opened or closed. If a future revision
adds a list of issues, states a count of them, or names a specific issue's
status, it has reintroduced Open#568 — the same defect, in the same file, for
the same reason.
