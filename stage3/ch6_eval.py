CASES = [
    ("明天要带伞吗？", "带伞"),
    ("我每天学多久？", "40 分钟"),
    ("算法怎么练？", "先做题"),
    ("怎么复习？", "错题"),
    ("数据存在哪？", "SQLite"),
    ("为什么要日志？", "排查"),
    ("Agent 要限制什么？", "步数"),
    ("接口超时怎么办？", "重试"),
]

AGENT_ANSWERS = {
    "明天要带伞吗？": "有雨，带伞。",
    "我每天学多久？": "每天 40 分钟。",
    "算法怎么练？": "先做题再看讲解。",
    "怎么复习？": "每天回顾错题。",
    "数据存在哪？": "存进 SQLite。",
    "为什么要日志？": "出问题能排查。",
    "Agent 要限制什么？": "限制步数和重试次数。",
    "接口超时怎么办？": "等一会儿再问一次。",
}


def run_agent(goal):
    return AGENT_ANSWERS.get(goal, "不知道")


passed, failed = 0, []
for goal, must in CASES:
    reply = run_agent(goal)
    if must in reply:
        passed += 1
    else:
        failed.append((goal, must, reply))

print(f"通过 {passed}/{len(CASES)}，通过率 {passed / len(CASES):.0%}")
for goal, must, reply in failed:
    print(f"未通过：{goal} → 期望“{must}”，实际“{reply}”")
