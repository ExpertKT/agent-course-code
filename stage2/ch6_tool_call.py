import json

def model(messages):
    if len(messages) == 1:
        return {"tool_call": {"name": "get_weather", "arguments": {"city": "常州"}}}
    return {"content": "明天常州有雨，带伞。"}


def get_weather(args):
    return {"city": args["city"], "rain": True}


TOOLS = {"get_weather": get_weather}

messages = [{"role": "user", "content": "明天要不要带伞？"}]
for step in range(1, 4):
    reply = model(messages)
    if "tool_call" in reply:
        call = reply["tool_call"]
        print(f"[{step}] 模型要求调用 {call['name']}({json.dumps(call['arguments'], ensure_ascii=False)})")
        result = TOOLS[call["name"]](call["arguments"])
        messages.append({"role": "assistant", "content": json.dumps(reply, ensure_ascii=False)})
        messages.append({"role": "tool", "name": call["name"], "content": json.dumps(result, ensure_ascii=False)})
    else:
        print(f"[{step}] 模型最终回答：{reply['content']}")
        break
