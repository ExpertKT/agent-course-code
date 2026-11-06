import os
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

CASES = [
    ("stage2/ch0_pipeline.py", ['"total_min": 430', '"avg_min": 43.0', '"avg_acc": 0.71']),
    ("stage2/ch1_similarity.py", ["算法练习 1.0", "刷算法题 0.894", "背单词 0.1"]),
    ("stage2/ch2_fit.py", ["loss 0.1501", "预测正确率 0.74", "预测正确率 0.97"]),
    ("stage2/ch3_classify.py", ["训练集 7 条，准确率 71%", "测试集 3 条，准确率 100%", "分界线约在 32.1 分钟"]),
    ("stage2/ch4_llm.py", ["建议每天 40 分钟：先做题，再看讲解。"]),
    ("stage2/ch5_structured.py", ["取用字段：科目 = 算法"]),
    ("stage2/ch6_agent.py", ["[2] 调工具 plan_trip", "日志： [(1, 'get_weather'), (2, 'plan_trip')]"]),
    ("stage2/ch6_tool_call.py", ["[1] 模型要求调用 get_weather", "[2] 模型最终回答：明天常州有雨，带伞。"]),
    ("stage2/ch7_evaluate.py", ["通过 9/10，通过率 90%"]),
    ("stage3/ch0_config.py", ["INFO 启动，城市=常州"]),
    ("stage3/ch1_tools.py", ["第 2 次失败", "'attempts': 3"]),
    ("stage3/ch2_messages.py", ["回复： 建议每天 40 分钟。", "'prompt_tokens': 18"]),
    ("stage3/ch3_memory.py", ["(3, 'user', '那算法练多久？')"]),
    ("stage3/ch4_retrieval.py", ["0.707", "0.500"]),
    ("stage3/ch5_loop.py", ["检测到动作 get_weather 重复两次"]),
    ("stage3/ch6_eval.py", ["通过 7/8，通过率 88%"]),
    ("stage3/ch7_cli.py", ["答案： 带伞"]),
    ("stage4/ch0_service.py", ["每天 40 分钟，先做题。", "收到：帮我看看这段代码"]),
    ("stage4/ch1_sessions.py", ["s1 2", "s2 1"]),
    ("stage4/ch2_limit.py", ["峰值并发 = 2"]),
    ("stage4/ch3_metrics.py", ['"avg_ms": 40.0']),
    ("stage4/ch4_security.py", ["拦截：检测到提示注入标记", "工具不在白名单：delete_all"]),
    ("stage4/ch5_quota.py", ["429"]),
    ("stage4/ch6_multi.py", ["汇总： 共 430 分钟"]),
    ("stage4/ch7_deploy.py", ["{'status': 'ok'}", "{'status': 'stopping'}"]),
]


@pytest.mark.parametrize("rel_path,expected", CASES)
def test_chapter_output(rel_path, expected):
    script = ROOT / rel_path
    env = {**os.environ, "PYTHONUTF8": "1"}
    result = subprocess.run(
        [sys.executable, script.name],
        cwd=script.parent,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
        env=env,
    )
    output = result.stdout + result.stderr
    assert result.returncode == 0, output
    for text in expected:
        assert text in output, f"{rel_path} 缺少输出：{text}\n实际输出：\n{output}"
