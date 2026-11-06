import csv
import json
from pathlib import Path

ROOT = Path(__file__).parent


def load_rows(path):
    rows = []
    with open(path, encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            rows.append({
                "date": row["日期"],
                "subject": row["科目"],
                "minutes": int(row["时长分钟"]),
                "accuracy": float(row["正确率"]),
            })
    return rows


def summarize(rows):
    total = sum(row["minutes"] for row in rows)
    average = total / len(rows)
    by_subject = {}
    for row in rows:
        by_subject.setdefault(row["subject"], []).append(row)
    subjects = {}
    for name, group in by_subject.items():
        subjects[name] = {
            "count": len(group),
            "avg_min": round(sum(r["minutes"] for r in group) / len(group), 1),
            "avg_acc": round(sum(r["accuracy"] for r in group) / len(group), 3),
        }
    return {"total_min": total, "avg_min": average, "subjects": subjects}


if __name__ == "__main__":
    rows = load_rows(ROOT / "data" / "study.csv")
    summary = summarize(rows)
    out = ROOT / "results"
    out.mkdir(exist_ok=True)
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False))
