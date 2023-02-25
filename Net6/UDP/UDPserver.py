import argparse
import socket
import threading

import api


def server(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind((host, port))

        threads = []
        print(f"Listening on {host}:{port}")

        while True:
            try:
                massage, address = server_socket.recvfrom(api.BUFFER_SIZE)
                # Create a new thread to handle the client request
                thread = threading.Thread(target=client_handler, args=(server_socket,
                                                                       massage, address))
                thread.start()
                threads.append(thread)
            except KeyboardInterrupt:
                print("Shutting down...")
                break

        for thread in threads:  # Wait for all threads to finish
            thread.join()


def process_request(request: api.mHeader):
    return api.mHeader(None, api.Kind.RESPONSE.value, api.Nosah.NULL.value, api.Status_code.STATUS_OK.value, request.checksum, 123, "שלום מירומר".encode())


def client_handler(server_socket, data, client_address) -> None:
    if not data:
        return
    try:
        try:
            request = api.mHeader.unpack(data)
        except Exception as e:
            raise api.CalculatorClientError(
                f'Error while unpacking request: {e}') from e

        print(f"{client_address} Got request of length {len(data)} bytes")
        print(f"{client_address} got " + str(request))

        response = process_request(request)
        print(f"{client_address} Sending " + str(response))
        response = response.pack()
        print(f"{client_address} Sending response of length {len(response)} bytes")
        server_socket.sendto(response, client_address)
    except:
        pass


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='Server.')

    arg_parser.add_argument('-p', '--port', type=int,
                            default=9999, help='The port to listen on.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default="127.0.0.1", help='The host to listen on.')

    args = arg_parser.parse_args()

    host = args.host
    port = args.port

    server(host, port)
