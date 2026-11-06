import json

metrics = {"requests": 0, "errors": 0, "total_ms": 0}

def handle(prompt, fail=False):
    metrics["requests"] += 1
    cost_ms = 40
    if fail:
        metrics["errors"] += 1
    metrics["total_ms"] += cost_ms
    return {"ok": not fail}

handle("问题一")
handle("问题二")
handle("问题三", fail=True)

avg = metrics["total_ms"] / metrics["requests"]
print(json.dumps({**metrics, "avg_ms": round(avg, 1)}, ensure_ascii=False))
