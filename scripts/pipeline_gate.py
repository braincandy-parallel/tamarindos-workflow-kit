"""Read-only structural project gates. These checks do not prove semantic acceptance."""
import argparse
from pathlib import Path
import re
import sys

def metadata(path):
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---(?:\s*\n|$)", text, re.S)
    if not match:
        raise ValueError("Missing frontmatter: " + str(path))
    fields = {}
    for line in match[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text

def linked(value, path):
    target = value.removeprefix("[[").removesuffix("]]").split("|")[0]
    # A full vault-relative path or a unique note title is valid.
    return target.removesuffix(".md").split("/")[-1] == path.stem

def task_states(text):
    rows = []
    column = None
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            column = None
            continue
        cells = [v.strip() for v in line.strip().strip("|").split("|")]
        if "Status" in cells or "Estado" in cells:
            column = cells.index("Status") if "Status" in cells else cells.index("Estado")
            continue
        if column is None or all(re.fullmatch(r"[:\- ]*", cell) for cell in cells):
            continue
        if len(cells) <= column:
            raise ValueError("Malformed task row")
        state = cells[column].lower()
        if state not in {"todo", "in-progress", "blocked", "done"}:
            raise ValueError("Unknown task status: " + state)
        rows.append((cells[0], state))
    if not rows:
        raise ValueError("No task table with Status/Estado column")
    if len({r[0] for r in rows}) != len(rows):
        raise ValueError("Duplicate task IDs")
    return rows

def check(spec, review, plan, stage="implement"):
    for path, prefix in ((spec, "SPC - "), (plan, "PL - ")):
        if not path.name.startswith(prefix):
            raise ValueError("Unexpected file prefix: " + path.name)
    sm, _ = metadata(spec)
    rm, _ = metadata(review)
    pm, text = metadata(plan)
    if sm.get("status", "").lower() not in {"ready", "approved", "active"}:
        raise ValueError("Spec is not ready; finish the interview")
    if rm.get("outcome", "").lower() != "ready":
        raise ValueError("Review has unresolved findings or no ready outcome")
    if not linked(rm.get("source", ""), spec):
        raise ValueError("Review does not reference this spec")
    if not linked(pm.get("source", ""), spec) or not linked(pm.get("review", ""), review):
        raise ValueError("Plan must link this spec and review")
    if pm.get("status", "").lower() not in {"ready", "in progress", "in-progress", "active", "complete", "completed"}:
        raise ValueError("Plan is not ready")
    rows = task_states(text)
    done = sum(state == "done" for _, state in rows)
    if int(pm.get("completed", "-1")) != done or int(pm.get("total", "-1")) != len(rows):
        raise ValueError("Plan counters disagree with task table")
    if stage == "complete" or pm.get("status", "").lower() in {"complete", "completed"}:
        if done != len(rows):
            raise ValueError("Project still has unfinished tasks")
        if pm.get("acceptance", "").lower() != "verified":
            raise ValueError("Project acceptance is not verified")
        evidence = pm.get("acceptance_evidence", "")
        if not evidence:
            raise ValueError("Missing acceptance evidence file")
        # Relative file path, kept within project; links are not treated as file paths.
        target = (plan.parent / evidence).resolve()
        project = plan.parent.parent.parent.resolve()
        if not target.is_relative_to(project) or not target.is_file():
            raise ValueError("Acceptance evidence must exist within this project")
    return {"tasks": len(rows), "done": done, "stage": stage,
            "result": "structural-pass", "semantic_acceptance": "must be reviewed by the agent"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("spec", "review", "plan"):
        parser.add_argument("--" + name, required=True, type=Path)
    parser.add_argument("--stage", choices=("implement", "complete"), default="implement")
    args = parser.parse_args()
    try:
        print(check(args.spec, args.review, args.plan, args.stage))
    except (ValueError, OSError) as exc:
        print("Pipeline gate failed: " + str(exc), file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
