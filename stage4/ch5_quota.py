DAILY_BUDGET = 100
used = 0
COST_PER_CALL = 40


def call(prompt):
    global used
    if used + COST_PER_CALL > DAILY_BUDGET:
        return {"status": 429, "message": "今日额度已用完", "used": used}
    used += COST_PER_CALL
    return {"status": 200, "reply": "ok", "used": used}


for i in range(1, 4):
    print(f"第 {i} 次：", call("问题" + str(i)))
