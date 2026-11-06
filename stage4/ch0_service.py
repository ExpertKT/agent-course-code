import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer


def answer(prompt):
    return "每天 40 分钟，先做题。" if "时长" in prompt else "收到：" + prompt[:10]


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = json.loads(self.rfile.read(length))
        data = json.dumps({"reply": answer(body["prompt"])}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 18100), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def ask(prompt):
    req = urllib.request.Request(
        "http://127.0.0.1:18100/chat",
        data=json.dumps({"prompt": prompt}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=3) as resp:
        return json.loads(resp.read())["reply"]


print(ask("我每天学习时长多少合适？"))
print(ask("帮我看看这段代码"))
server.shutdown()
