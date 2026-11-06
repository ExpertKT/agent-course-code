CASES = [
    ("学习 45 分钟算法够吗？", "40 分钟"),
    ("我每天学多久？", "40 分钟"),
    ("算法怎么练？", "先做题"),
    ("正确率低怎么办？", "看讲解"),
    ("Python 要学多久？", "40 分钟"),
    ("怎么安排复习？", "每天"),
    ("刷题顺序？", "先易后难"),
    ("要不要背语法？", "用起来"),
    ("一天学两小时行吗？", "分两次"),
    ("考试前怎么突击？", "错题"),
]


def answer(prompt):
    canned = {
        "学习 45 分钟算法够吗？": "每天 40 分钟，先做题再看讲解。",
        "我每天学多久？": "建议每天 40 分钟，固定时段。",
        "算法怎么练？": "先做题，再看讲解，最后重写一遍。",
        "正确率低怎么办？": "回看讲解，把错题重做。",
        "Python 要学多久？": "每天 40 分钟，坚持四周。",
        "怎么安排复习？": "每天十分钟回顾昨天的错题。",
        "刷题顺序？": "先易后难，按题型分组。",
        "要不要背语法？": "用起来就记住了，别单独背。",
        "一天学两小时行吗？": "可以，但别超过 40 分钟不休息。",
        "考试前怎么突击？": "只看错题，不再刷新题。",
    }
    return canned.get(prompt, "这个问题我暂时答不上来。")


passed = 0
failed = []
prompt_chars = 0
for prompt, must_contain in CASES:
    prompt_chars += len(prompt)
    reply = answer(prompt)
    if must_contain in reply:
        passed += 1
    else:
        failed.append((prompt, must_contain, reply))

print(f"通过 {passed}/{len(CASES)}，通过率 {passed / len(CASES):.0%}")
for prompt, must, reply in failed:
    print(f"未通过：{prompt} → 期望包含“{must}”，实际“{reply}”")
tokens = prompt_chars / 2
print(f"输入共 {prompt_chars} 个字符，粗估 {tokens:.0f} tokens")
print(f"按每千 token 0.01 元估算，这一轮约 {tokens / 1000 * 0.01:.5f} 元")
