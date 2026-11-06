import json
import sqlite3


def get_weather(args):
    return {"city": args["city"], "rain": True}


def plan_trip(args):
    return "带伞" if args["rain"] else "不用带伞"


TOOLS = {"get_weather": get_weather, "plan_trip": plan_trip}


def run(goal, max_steps=5):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE steps (step INTEGER, action TEXT, result TEXT)")
    state = {"city": "常州", "rain": None, "advice": None}
    history = []

    for step in range(1, max_steps + 1):
        if state["rain"] is None:
            action, args = "get_weather", {"city": state["city"]}
        elif state["advice"] is None:
            action, args = "plan_trip", {"rain": state["rain"]}
        else:
            break

        result = TOOLS[action](args)
        if action == "get_weather":
            state["rain"] = result["rain"]
        else:
            state["advice"] = result

        print(f"[{step}] 调工具 {action}({json.dumps(args, ensure_ascii=False)}) → {json.dumps(result, ensure_ascii=False)}")
        db.execute("INSERT INTO steps VALUES (?, ?, ?)", (step, action, json.dumps(result, ensure_ascii=False)))
        history.append((step, action, result))

    db.commit()
    answer = f"明天{state['city']}有雨，出门{state['advice']}" if state["rain"] else f"明天{state['city']}不下雨"
    print(f"[{len(history) + 1}] 结束：{answer}")
    print("日志：", db.execute("SELECT step, action FROM steps").fetchall())
    return answer


print(run("明天出门要不要带伞？"))
