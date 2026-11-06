import json
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers["Content-Length"])
        body = json.loads(self.rfile.read(length))
        prompt = body["prompt"]
        if "时长" in prompt:
            reply = "建议每天 40 分钟：先做题，再看讲解。"
        else:
            reply = "收到你的问题：" + prompt[:20]
        data = json.dumps({"reply": reply}, ensure_ascii=False).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass


server = HTTPServer(("127.0.0.1", 18090), Handler)
threading.Thread(target=server.serve_forever, daemon=True).start()


def ask(prompt):
    request = urllib.request.Request(
        "http://127.0.0.1:18090/chat",
        data=json.dumps({"prompt": prompt}, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=3) as response:
        return json.loads(response.read())["reply"]


print(ask("我每天学习时长多少合适？"))
server.shutdown()
