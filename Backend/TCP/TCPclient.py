import socket

BUFFER_SIZE = 65565

DEFAULT_CLIENT_HOST = "127.0.0.1"  # The default host
DEFAULT_CLIENT_PORT = 20215  # The default port

class TCPclient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = None

    def sendData(self, request):
        self.client_socket.sendall(request)
        print(f"{self.server_address} Sending request of length {len(request)} bytes")
        response = self.client_socket.recv(BUFFER_SIZE)
        print(f"{self.server_address} Got response of length {len(response)} bytes")
        return response

    def connect(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.client_socket.bind(('',DEFAULT_CLIENT_PORT))
        self.client_socket.connect(self.server_address)
        print(f"{self.server_address} Connection established")

    def close(self):
        self.client_socket.close()
        print(f"{self.server_address} Connection closed")
