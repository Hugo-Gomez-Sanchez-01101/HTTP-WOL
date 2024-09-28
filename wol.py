import ssl
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from wakeonlan import send_magic_packet

equipos = {
    1: {'mac': '74:56:3C:E5:46:9E', 'ip': '192.168.1.101'},
    # Agrega más equipos aquí
}

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path.startswith("/wol"):
            try:
                equipo_id = int(self.path.split('?equipo=')[-1])
            except ValueError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Equipo inválido o no proporcionado'}).encode())
                return

            if equipo_id in equipos:
                mac_address = equipos[equipo_id]['mac']
                send_magic_packet(mac_address)
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'success', 'message': f'Sent magic packet to {mac_address}'}).encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Equipo no encontrado'}).encode())
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor corriendo en el puerto {port}...')
    httpd.serve_forever()

#def run(server_class=HTTPServer, handler_class=MyRequestHandler, port=5000):
#    server_address = ('', port)
#    httpd = server_class(server_address, handler_class)
#
#    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
#    context.load_cert_chain(certfile='certs/cert.pem', keyfile='certs/key.pem')
#    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
#
#    print(f'Servidor HTTPS corriendo en el puerto {port}...')
#    httpd.serve_forever()

if __name__ == '__main__':
    run()
