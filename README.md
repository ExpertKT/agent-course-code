# agent-course-code

四本教材（阶段二至四）的配套代码与自动判分。每一章的脚本都能单独运行，测试用子进程跑脚本并核对输出。

## 运行

```powershell
cd "$HOME\Desktop\agent-course-code"
$env:PYTHONUTF8='1'
python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
```

预期：`24 passed`。

## 目录

```
stage2/            机器学习与 LLM（8 章）
  ch0_pipeline.py      读 CSV → 统计 → 写 JSON
  ch1_similarity.py    向量与余弦相似度
  ch2_fit.py           手写梯度下降拟合直线
  ch3_classify.py      逻辑回归与训练/测试划分
  ch4_llm.py           本机模拟模型 + HTTP 调用
  ch5_structured.py    结构化输出与重试
  ch6_agent.py         最小 Agent 循环 + 日志
  ch7_evaluate.py      10 条评测集与通过率
stage3/            Agent 工程化（8 章）
  ch0_config.py        配置与日志
  ch1_tools.py         工具重试
  ch2_messages.py      messages 协议与用量
  ch3_memory.py        SQLite 会话记忆
  ch4_retrieval.py     关键词向量检索
  ch5_loop.py          步数上限与重复检测
  ch6_eval.py          评测
  ch7_cli.py           命令行入口
stage4/            Agent 服务化（8 章）
  ch0_service.py       HTTP 服务
  ch1_sessions.py      会话隔离
  ch2_limit.py         并发限流
  ch3_metrics.py       指标
  ch4_security.py      注入拦截与工具白名单
  ch5_quota.py         配额
  ch6_multi.py         多 Agent 分工
  ch7_deploy.py        健康检查与优雅退出
tests/
  test_chapters.py     24 条输出断言
answers/               练习参考答案与边界用例
```

## 测试怎么判分

测试不检查代码写法，只跑脚本、核对输出里的关键数字或句子。例如：

```python
("stage2/ch0_pipeline.py", ['"total_min": 430', '"avg_min": 43.0'])
```

这样改实现也不影响判分，改坏结果就会红。

## 与教材对应

每个 `chN_*.py` 对应教材第 N 章。教材里的“实际输出”就是这些脚本跑出来的。

## 版本

Python 3.12+，numpy 2.5.4，pytest 8.3.4。
