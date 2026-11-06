GOAL = "写一份本周学习计划"

def plan(goal):
    if "计划" in goal:
        return ["统计上周时长", "找出最弱的科目", "安排下周重点"]
    return ["直接回答"]


def worker(task):
    return {"统计上周时长": "共 430 分钟", "找出最弱的科目": "算法，正确率 0.710",
            "安排下周重点": "每天 40 分钟算法"}.get(task, "完成")


steps = plan(GOAL)
print("计划：", steps)
results = []
for task in steps:
    result = worker(task)
    results.append(result)
    print(f"  {task} → {result}")
print("汇总：", "；".join(results))
