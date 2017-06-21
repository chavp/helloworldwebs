from http.server import BaseHTTPRequestHandler, HTTPServer

# HTTPRequestHandler class
class ListenHTTPServerRequestHandler(BaseHTTPRequestHandler):

  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

print('starting server...')
server_address = ('127.0.0.1', 5000)
httpd = HTTPServer(server_address, ListenHTTPServerRequestHandler)
print('running server...')
httpd.serve_forever()