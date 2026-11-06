state = {"ready": True, "stopping": False}


def health():
    return {"status": "ok" if state["ready"] and not state["stopping"] else "stopping"}


def request_stop():
    state["stopping"] = True          # 先不再接新请求
    print("收到停止信号，等待在途请求结束")
    state["ready"] = False
    print("在途请求已清空，进程可以退出")


print(health())
request_stop()
print(health())
