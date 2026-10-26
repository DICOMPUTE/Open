#!/usr/bin/env python3
"""Shape check for DICOMPUTE/Open's issue forms and TRIAGE.md contract (Open#1789).

Run: python3 .github/scripts/check-tracker.py [--labels labels.txt]
Exit 0 = clean, 1 = findings (each printed as one line).

Checks:
  forms     every .github/ISSUE_TEMPLATE/*.yml form parses, has name/description/body,
            each body item has a known type, non-markdown items have a unique id and a label.
  config    config.yml keeps blank issues off and keeps the security contact link.
  markdown  engineering.md keeps the eight section headings, in order.
  labels    (with --labels) every label a form applies exists in the repo.
  triage    TRIAGE.md names the six dispositions, and does not carry an issue list or
            an open-issue count (the Open#568 defect).
"""
import glob
import os
import re
import sys

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TPL = os.path.join(ROOT, ".github", "ISSUE_TEMPLATE")
FORM_TYPES = {"markdown", "textarea", "input", "dropdown", "checkboxes"}
SECTIONS = ["What", "Why", "Prompt", "Workflow", "Loop", "Graph", "Layout", "Flow"]
DISPOSITIONS = [
    "tracked-internally",
    "needs-operator",
    "needs-decision",
    "not-reproducible",
    "works-as-designed",
    "not-actionable-as-filed",
]


def check_forms(findings, form_labels):
    for path in sorted(glob.glob(os.path.join(TPL, "*.yml"))):
        name = os.path.basename(path)
        if name == "config.yml":
            continue
        try:
            doc = yaml.safe_load(open(path, encoding="utf-8"))
        except yaml.YAMLError as e:
            findings.append(f"forms: {name}: does not parse: {e}")
            continue
        if not isinstance(doc, dict):
            findings.append(f"forms: {name}: not a mapping")
            continue
        for key in ("name", "description", "body"):
            if not doc.get(key):
                findings.append(f"forms: {name}: missing `{key}`")
        for lab in doc.get("labels") or []:
            form_labels.append((name, lab))
        ids = set()
        for i, item in enumerate(doc.get("body") or []):
            t = (item or {}).get("type")
            if t not in FORM_TYPES:
                findings.append(f"forms: {name}: body[{i}] has unknown type {t!r}")
                continue
            if t == "markdown":
                continue
            iid = item.get("id")
            if not iid:
                findings.append(f"forms: {name}: body[{i}] ({t}) has no id")
            elif iid in ids:
                findings.append(f"forms: {name}: duplicate id {iid!r}")
            ids.add(iid)
            if not (item.get("attributes") or {}).get("label"):
                findings.append(f"forms: {name}: body[{i}] ({t}) has no label")


def check_config(findings):
    path = os.path.join(TPL, "config.yml")
    if not os.path.exists(path):
        findings.append("config: .github/ISSUE_TEMPLATE/config.yml is missing")
        return
    doc = yaml.safe_load(open(path, encoding="utf-8")) or {}
    if doc.get("blank_issues_enabled") is not False:
        findings.append("config: blank_issues_enabled must stay false")
    urls = [str((c or {}).get("url", "")) for c in doc.get("contact_links") or []]
    if not any("SECURITY.md" in u for u in urls):
        findings.append("config: the security contact link (SECURITY.md) is missing")


def check_markdown(findings):
    path = os.path.join(TPL, "engineering.md")
    if not os.path.exists(path):
        return
    text = re.sub(r"<!--.*?-->", "", open(path, encoding="utf-8").read(), flags=re.S)
    heads = re.findall(r"^## (\w+)\s*$", text, flags=re.M)
    got = [h for h in heads if h in SECTIONS]
    if got != SECTIONS:
        findings.append(f"markdown: engineering.md sections are {got}, expected {SECTIONS}")


def check_triage(findings):
    path = os.path.join(ROOT, "TRIAGE.md")
    if not os.path.exists(path):
        findings.append("triage: TRIAGE.md is missing")
        return
    text = open(path, encoding="utf-8").read()
    for d in DISPOSITIONS:
        if f"`{d}`" not in text:
            findings.append(f"triage: disposition `{d}` is not in TRIAGE.md")
    if re.search(r"^\s*\|\s*#\d+\s*\|", text, flags=re.M):
        findings.append("triage: TRIAGE.md lists issues in a table (Open#568: link the live list instead)")
    for m in re.finditer(r"\b\d+\s+(?:open\s+)?issues?\s+(?:are\s+)?open\b", text, flags=re.I):
        line = text[: m.start()].count("\n") + 1
        ctx = text.splitlines()[line - 1]
        if "Until" not in ctx and "By then" not in ctx and "were open" not in ctx:
            findings.append(f"triage: TRIAGE.md:{line} states an open-issue count (Open#568)")


def main(argv):
    findings, form_labels = [], []
    check_forms(findings, form_labels)
    check_config(findings)
    check_markdown(findings)
    check_triage(findings)
    if "--labels" in argv:
        have = {l.strip() for l in open(argv[argv.index("--labels") + 1], encoding="utf-8") if l.strip()}
        for name, lab in form_labels:
            if lab not in have:
                findings.append(f"labels: {name} applies {lab!r}, which does not exist in the repo")
    for f in findings:
        print(f)
    print(f"check-tracker: {len(findings)} finding(s)")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
