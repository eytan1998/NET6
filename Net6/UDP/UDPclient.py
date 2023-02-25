import argparse
import socket

from UDP import api


def client(server_address: tuple[str, int]) -> None:
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.connect(server_address)
        print(f"{server_prefix} Connection established")

        try:
            request = api.mHeader(
                None, api.Kind.REQUEST_BY_QUERY.value, api.Nosah.SPARAD.value, 0, 1234, 5678, "שלום מי".encode())

            request = request.pack()
            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(request, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            response = api.mHeader.unpack(response)
            print(response)


        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="A Calculator Client.")

    arg_parser.add_argument("-p", "--port", type=int,
                            default=api.DEFAULT_SERVER_PORT, help="The port to connect to.")
    arg_parser.add_argument("-H", "--host", type=str,
                            default=api.DEFAULT_SERVER_HOST, help="The host to connect to.")

    args = arg_parser.parse_args()

    host = args.host
    port = args.port

    client((host, port))
