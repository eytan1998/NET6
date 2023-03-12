import socket

from Backend.Help.app_packet import AppHeader

BUFFER_SIZE = 65565




class TCPclient:
    def __init__(self, server_address, from_address: tuple[str, int]):
        self.server_address = server_address
        self.client_socket = None

    def sendData(self, request: AppHeader):
        request = request.pack()
        self.client_socket.sendall(request)
        print(f"{self.server_address} Sending request of length {len(request)} bytes")
        response = self.client_socket.recv(BUFFER_SIZE)
        print(f"{self.server_address} Got response of length {len(response)} bytes")
        response = AppHeader.unpack(response)
        return response

    def connect(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.client_socket.bind(('',DEFAULT_CLIENT_PORT))
            self.client_socket.connect(self.server_address)
            print(f"{self.server_address} Connection established")
            return 0
        except:
            self.client_socket.close()
            return None

    def close(self):
        self.client_socket.close()
        print(f"{self.server_address} Connection closed")
