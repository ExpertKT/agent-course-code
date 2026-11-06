import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = json.loads(self.rfile.read(length))
        question = body["messages"][-1]["content"]
        reply = "建议每天 40 分钟。" if "时长" in question else "收到：" + question[:12]
        data = json.dumps({
            "choices": [{"message": {"role": "assistant", "content": reply}}],
            "usage": {"prompt_tokens": 18, "completion_tokens": 9},
        }, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 18091), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def chat(messages):
    request = urllib.request.Request(
        "http://127.0.0.1:18091/chat",
        data=json.dumps({"model": "mock", "messages": messages}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": "Bearer local"},
    )
    with urllib.request.urlopen(request, timeout=3) as response:
        payload = json.loads(response.read())
    return payload["choices"][0]["message"]["content"], payload["usage"]


reply, usage = chat([
    {"role": "system", "content": "你是学习教练，回答简短。"},
    {"role": "user", "content": "我每天学习时长多少合适？"},
])
print("回复：", reply)
print("用量：", usage)
server.shutdown()
