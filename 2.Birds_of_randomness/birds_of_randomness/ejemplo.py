import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Recibe los datos del cliente
        self.data = self.request.recv(1024).strip()
        print(f"Se recibieron los siguientes datos: {self.data}")

        # Envía una respuesta al cliente
        response = "¡Mensaje recibido correctamente!\n"
        self.request.sendall(response.encode())

if __name__ == "__main__":
    HOST, PORT = "localhost", 1234
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
