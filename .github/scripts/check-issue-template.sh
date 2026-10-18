#!/usr/bin/env bash
# #1789: the template-shape checker for this tracker's one issue format
# (.github/ISSUE_TEMPLATE/issue.md): the eight headings, in order, plus the
# "Severity · Effort" trailer. A violation gets ONE comment and the
# `template-incomplete` label; a fixed issue loses the label again. Exit 0
# always -- the signal is the label/comment, never a red board on a repo
# whose whole purpose is holding issues.
set -euo pipefail

NUMBER="${1:?usage: check-issue-template.sh <issue-number>}"
REPO="${GITHUB_REPOSITORY:?}"

body="$(gh issue view "$NUMBER" --repo "$REPO" --json body --jq .body)"

required=(What Why Prompt Workflow Loop Graph Layout Flow)
pos=0
missing=()
for h in "${required[@]}"; do
  # match "## What" (allowing trailing whitespace/CR), from the last match on
  found="$(printf '%s' "$body" | tail -c +$((pos + 1)) | grep -n -m1 -E "^## ${h}[[:space:]]*$" || true)"
  if [ -z "$found" ]; then
    missing+=("$h")
  else
    line="${found%%:*}"
    # advance the search cursor past this heading: byte offset within the
    # remaining slice, approximated by line count (headings are short lines)
    pos=$((pos + line))
  fi
done

trailer="$(printf '%s' "$body" | grep -c -E 'Severity:[^[:alnum:]]*(Low|Medium|High|Critical)[^[:alnum:]]*·[^[:alnum:]]*Effort:' || true)"

has_label="$(gh issue view "$NUMBER" --repo "$REPO" --json labels --jq '[.labels[].name] | contains(["template-incomplete"])')"

if [ "${#missing[@]}" -eq 0 ] && [ "$trailer" -ge 1 ]; then
  if [ "$has_label" = "true" ]; then
    gh issue edit "$NUMBER" --repo "$REPO" --remove-label template-incomplete >/dev/null
    gh issue comment "$NUMBER" --repo "$REPO" --body "Template shape now complete (all eight sections in order, Severity · Effort trailer present) -- removing \`template-incomplete\`. Thanks for fixing it." >/dev/null
  fi
  echo "issue #$NUMBER: template shape ok"
  exit 0
fi

problem=""
[ "${#missing[@]}" -gt 0 ] && problem="missing or out-of-order section(s): \`${missing[*]}\`"
[ "$trailer" -eq 0 ] && problem="${problem:+$problem; }missing the \`Severity: ... · Effort: ...\` trailer"

if [ "$has_label" != "true" ]; then
  gh issue edit "$NUMBER" --repo "$REPO" --add-label template-incomplete >/dev/null 2>&1 || true
  gh issue comment "$NUMBER" --repo "$REPO" --body "This issue does not follow the tracker's one format (.github/ISSUE_TEMPLATE/issue.md): ${problem}.

The board and burndown tooling read that shape, so it is enforced here by bot. Keep all eight headings, in order -- What / Why / Prompt / Workflow / Loop / Graph / Layout / Flow -- and end with the \`Severity: Low|Medium|High|Critical · Effort: S|M|L\` trailer. Editing the body re-runs this check and clears the label automatically." >/dev/null
fi
echo "issue #$NUMBER: $problem"
