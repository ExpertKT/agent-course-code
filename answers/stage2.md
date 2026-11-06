# 阶段二练习答案与边界用例

## 第 0 章 · best_day

```python
best = max(rows, key=lambda r: r["accuracy"])
summary["best_day"] = {"date": best["date"], "accuracy": best["accuracy"]}
```

边界：正确率并列时，`max` 取先出现的那个；要固定取最早日期，先按日期排序再取。

## 第 1 章 · 加一句“看算法讲解”

```python
vectors["看算法讲解"] = [3, 0, 1]
scores = sorted(
    ((cosine(vectors["算法练习"], v), k) for k, v in vectors.items()),
    reverse=True,
)
```

边界：全零向量（句子一个关键词都没有）会让分母为 0，函数要返回 0.0，不能抛除零错误。

## 第 2 章 · 学习率实验

- `lr = 1.0`：loss 在几步内震荡甚至变成 `nan`，因为每步迈过头。
- `lr = 0.01`：200 步后 loss 仍在缓慢下降，需要更多步才收敛。

边界：学习率不是越大越好，也不是越小越好；判断标准是 loss 是否单调下降并稳定。

## 第 3 章 · 及格线改成 0.8

```python
passed = (accuracy &gt;= 0.8).astype(float)
```

分界线会右移（要求更长的学习时间才算及格），测试集里原本及格的样本可能变成不及格。边界：改动标签等于改问题定义，训练集与测试集必须同时改，不能只改一边。

## 第 4 章 · 加一条“算法”规则

```python
if "算法" in prompt:
    reply = "先做题，再讲解。"
elif "时长" in prompt:
    reply = "建议每天 40 分钟：先做题，再看讲解。"
```

边界：两条规则同时命中时，先判断的那条生效，顺序就是优先级。

## 第 5 章 · 四字段提取

```python
def extract_task(prompt, retry_limit=2):
    for _ in range(retry_limit + 1):
        text = fake_model(prompt, strict=True)
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            prompt += "\n只输出 JSON，不要解释。"
            continue
        if {"subject", "minutes", "date", "mood"} &lt;= data.keys():
            return data
        prompt += "\n必须包含 subject、minutes、date、mood 四个字段。"
    raise ValueError("模型连续返回不合规的结构")
```

边界：字段存在但类型不对（`minutes` 是字符串）也要判失败，用 `isinstance(data["minutes"], int)` 检查。

## 第 6 章 · send_message 工具

```python
def send_message(args):
    print("发送：", args["text"])
    return {"ok": True}

TOOLS["send_message"] = send_message
```

在循环里加条件：只有 `state["advice"]` 不为空时才允许选这个动作。边界：工具执行失败要计入日志，不能只打印。

## 第 7 章 · 扩到 20 条

边界：答案有多种说法时，关键词评分会误判。至少给每条准备 2 个可接受关键词，或改成“包含任一即通过”。别为了让分数好看而放宽标准。
