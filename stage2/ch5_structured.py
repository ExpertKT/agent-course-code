import json


def fake_model(prompt, strict=False):
    if strict:
        return '{"subject": "算法", "minutes": 45}'
    return "我猜是算法，45 分钟吧"


def extract(prompt):
    text = fake_model(prompt)
    try:
        return json.loads(text), text
    except json.JSONDecodeError:
        strict_prompt = prompt + "\n只输出 JSON，不要解释。"
        text2 = fake_model(strict_prompt, strict=True)
        return json.loads(text2), text2


result, raw = extract("帮我从这句话里提取：今天做了 45 分钟算法")
print("第一次返回：我猜是算法，45 分钟吧")
print("解析失败，加一句“只输出 JSON”再问")
print("第二次返回：", raw)
print("解析成功：", result)
print("取用字段：科目 =", result["subject"], "，时长 =", result["minutes"])
