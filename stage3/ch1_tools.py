import time

CALLS = {"n": 0}

def flaky_weather(args):
    """前两次抛超时，第三次成功。"""
    CALLS["n"] += 1
    if CALLS["n"] < 3:
        raise TimeoutError("weather service timeout")
    return {"city": args["city"], "rain": True}


TOOLS = {"get_weather": flaky_weather}


def call_tool(name, args, retry_limit=2):
    for attempt in range(1, retry_limit + 2):      # 首次 + 2 次重试 = 3 次机会
        try:
            result = TOOLS[name](args)
            return {"ok": True, "result": result, "attempts": attempt}
        except Exception as error:
            print(f"  第 {attempt} 次失败：{type(error).__name__}: {error}")
            if attempt > retry_limit:
                return {"ok": False, "error": str(error), "attempts": attempt}
            time.sleep(0.05)


print(call_tool("get_weather", {"city": "常州"}))
