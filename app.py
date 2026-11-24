from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = json.dumps({"status": "ok"}).encode("utf-8")
            content_type = "application/json"
            status = 200
        elif self.path == "/":
            body = b"Hello from mypipeline!\n"
            content_type = "text/plain; charset=utf-8"
            status = 200
        else:
            body = b"Not found\n"
            content_type = "text/plain; charset=utf-8"
            status = 404

        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8000"))
    server = HTTPServer(("0.0.0.0", port), AppHandler)
    print("Serving on http://localhost:{0}".format(port), flush=True)
    server.serve_forever()
