from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from z_main import Main


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        epsilon = main.get_epsilon()
        self._set_response()
        self.wfile.write(json.dumps({'epsilon': epsilon}).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        data = json.loads(post_data)
        main.recieved_data(data)

        self._set_response()
        self.wfile.write("POST request for {}".format(
            self.path).encode('utf-8'))


def run(server_class=HTTPServer, handler_class=S, port=1616):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"[+] Started http-server on port {port}")
    print(f"[i] Listening for new games...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(f"[i]] Destroying http-server...")


main = Main()
run()
