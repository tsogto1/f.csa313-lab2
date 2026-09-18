from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        time.sleep(0.1)
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b'k6 lab2 local server ok\n')
    def log_message(self, format, *args):
        return

if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', 8001), Handler)
    print('Serving on http://127.0.0.1:8001')
    server.serve_forever()
