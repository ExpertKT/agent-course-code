import argparse
import json
import logging
from pathlib import Path

ROOT = Path(__file__).parent
CONFIG = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))

logging.basicConfig(filename=ROOT / "agent.log", level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s", encoding="utf-8")


def get_weather(args):
    return {"city": args["city"], "rain": True}


TOOLS = {"get_weather": get_weather}


def run(goal):
    state = {"rain": None, "advice": None}
    for step in range(1, CONFIG["max_steps"] + 1):
        if state["rain"] is None:
            action, args = "get_weather", {"city": CONFIG["city"]}
        elif state["advice"] is None:
            state["advice"] = "带伞" if state["rain"] else "不用带伞"
            print(f"[{step}] 结论：{state['advice']}")
            break
        result = TOOLS[action](args)
        state["rain"] = result["rain"]
        logging.info("step=%d action=%s result=%s", step, action, result)
        print(f"[{step}] {action} → {result}")
    return state["advice"]


parser = argparse.ArgumentParser()
parser.add_argument("--goal", default="明天要不要带伞")
args = parser.parse_args()
print("目标：", args.goal)
print("答案：", run(args.goal))
