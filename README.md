# Open

## Filing an issue

Every issue here uses one format — eight sections, in this order, then a
trailer. The template (`.github/ISSUE_TEMPLATE/issue.md`) pre-fills the
headings with guidance; blank issues are disabled, so **New issue** opens it.

| Section | Holds |
|---|---|
| **What** | The gap or defect, with `file:line` on our side and a URL for anything it mirrors. Partial implementations stated honestly. |
| **Why** | The user-visible consequence. If none can be named, the issue is not filed. |
| **Prompt** | A self-contained implementation prompt, including the traps specific to the area (integer µUSD wherever money appears; the fleet-canary caveat wherever fleet metrics appear). |
| **Workflow** | Ordered implementation steps. |
| **Loop** | The verification loop, the definition of done, and what to re-check afterwards. |
| **Graph** | Mermaid of the affected modules or data path. |
| **Layout** | A wireframe, or the one line "No UI surface." with the heading kept. |
| **Flow** | Mermaid of the user journey or state transitions, including failure branches. |

The body ends with `Severity: <critical|high|medium|low> · Effort: <S|M|L>`.
Severity is technical blast radius, independent of schedule; Effort is
implementation cost. Priority is derived from those two plus how live the
surface is — it is never written into an issue by hand.
