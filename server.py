import argparse
import socket
import threading

from Backend.Help import Handelserver
from Backend.Help.app_packet import AppHeader
from Backend.RUDP.RUDPserver import RUDPserver
from Backend.Help.gabai import GabaiList
from Backend.Help.synagogue import SynagogueList

BUFFER_SIZE = 65536
DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_SERVER_PORT = 30381
TIME_OUT = 2

the_synagogue_list = SynagogueList()
the_gabi_list = GabaiList()
the_synagogue_list.read_json()
the_gabi_list.read_json()


def getSynagogues():
    global the_synagogue_list
    return the_synagogue_list


def getGabais():
    global the_gabi_list
    return the_gabi_list


def TCPclient_handler(client_socket: socket.socket, client_address: tuple[str, int]) -> None:
    while True:
        data = client_socket.recv(BUFFER_SIZE)
        print(f"{client_address} Got request of length {len(data)} bytes")
        if not data:
            break
        try:
            request = AppHeader.unpack(data)
            response = Handelserver.process_request(request)
            response = response.pack()
            client_socket.sendall(response)
            print(f"{client_address} Sending response of length {len(response)} bytes")
        except Exception as e:
            print(f"Unexpected server error: {e}")


def TCPserver(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(10)
        threads = []
        print(f"Listening on {host}:{port}")

        while True:
            try:
                client_socket, address = server_socket.accept()

                # Create a new thread to handle the client request
                thread = threading.Thread(target=TCPclient_handler, args=(
                    client_socket, address))
                thread.start()
                threads.append(thread)
            except KeyboardInterrupt:
                print("Shutting down...")
                break

        for thread in threads:
            thread.join()


def UDPserver(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.settimeout(TIME_OUT)
        server_socket.bind((host, port))
        print(f"Listening on {host}:{port}")

        while True:
            try:
                connection = RUDPserver(server_socket)
                connection.accept()
                connection.receiveData()
            except KeyboardInterrupt:
                print("Shutting down...")
                break


if __name__ == '__main__':
    the_synagogue_list.read_json()
    the_gabi_list.read_json()
    arg_parser = argparse.ArgumentParser(
        description='Server.')

    arg_parser.add_argument('-p', '--port', type=int,
                            default=DEFAULT_SERVER_PORT, help='The port to listen on.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default=DEFAULT_SERVER_HOST, help='The host to listen on.')
    arg_parser.add_argument('--tcp', action=argparse.BooleanOptionalAction, help='Do the connection tcp instead of '
                                                                                 'rudp.')

    args = arg_parser.parse_args()
    host = args.host
    port = args.port
    if args.tcp is None:
        UDPserver(host, port)
    else:
        TCPserver(host, port)
