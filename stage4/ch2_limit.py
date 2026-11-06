import threading
import time

limit = threading.Semaphore(2)      # 最多两个同时干活
state = {"running": 0, "peak": 0}
lock = threading.Lock()


def job(n):
    with limit:
        with lock:
            state["running"] += 1
            state["peak"] = max(state["peak"], state["running"])
        time.sleep(0.2)
        with lock:
            state["running"] -= 1


threads = [threading.Thread(target=job, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("完成 5 个任务，峰值并发 =", state["peak"])
