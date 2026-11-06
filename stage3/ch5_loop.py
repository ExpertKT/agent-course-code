def get_weather(args):
    return {"ok": False, "error": "service timeout"}


def decide(state, history):
    if state["rain"] is None:
        return "get_weather", {"city": "常州"}
    return "finish", {}


state = {"rain": None}
history = []
for step in range(1, 6):
    action, args = decide(state, history)
    if action == "finish":
        print(f"[{step}] 结束")
        break
    if history.count(action) >= 2:
        print(f"[{step}] 检测到动作 {action} 重复两次，停止")
        break
    result = get_weather(args)
    history.append(action)
    print(f"[{step}] {action} → {result}")
