import json
import logging
from pathlib import Path

ROOT = Path(__file__).parent

CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler(ROOT / "agent.log", encoding="utf-8")],
)
log = logging.getLogger("agent")

log.info("启动，城市=%s，最多 %d 步", CONFIG["city"], CONFIG["max_steps"])
print("配置：", CONFIG)
print("日志写到：", ROOT / "agent.log")
print((ROOT / "agent.log").read_text(encoding="utf-8").strip().splitlines()[-1])
