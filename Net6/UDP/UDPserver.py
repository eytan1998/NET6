import argparse
import atexit
import json
import socket
import threading
from synagogue import SynagogueList, Synagogue, Nosah
import api

synagogue_list = SynagogueList()


def exit_handler():
    synagogue_list.write_json()
    print(synagogue_list)
    print("end, saved to json")


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


def process_request_and_send(server_socket, client_address, request: api.mHeader):
    if request.kind == api.Kind.REQUEST_BY_QUERY.value:
        temp = synagogue_list.get_by_name_and_nosah(request.data.decode(), request.nosah)

        if temp is None:
            send_response(server_socket, client_address, None)

        if temp is not None:
            send_response(server_socket, client_address,
                          api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, api.Status_code.STATUS_OK.value,
                                      request.checksum, 123, bytes(temp)))

    elif request.kind == api.Kind.REQUEST_BY_IDS.value:
        list_of_ids = list(request.data)
        if list_of_ids is None: send_response(server_socket, client_address, None)
        for id_in_list in list_of_ids:
            temp = synagogue_list.get_by_id(id_in_list)
            if temp is None:
                send_response(server_socket, client_address, None)
            else:
                send_response(server_socket, client_address,
                              api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                          api.Status_code.STATUS_OK.value,
                                          0, 123, str(temp).encode()))

    elif request.kind == api.Kind.SET_BY_ID.value:
        ans = synagogue_list.set_by_id(Synagogue.fromJSON(request.data.decode()))
        print(synagogue_list.get_by_id(1))
        if ans == 0:
            send_response(server_socket, client_address,
                          api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                      api.Status_code.STATUS_OK.value,
                                      0, 123, "set sucssefuly".encode()))
        elif ans == -1:
            send_response(server_socket, client_address,
                          api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                      api.Status_code.STATUS_UNKNOWN.value,
                                      0, 123, "NOT sucssefuly".encode()))


def send_response(server_socket, client_address, response):
    if response is None:
        response = api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value,
                               api.Status_code.STATUS_UNKNOWN.value,
                               1, 123, 'object not found'.encode())
    print(f"{client_address} Sending " + str(response))
    response = response.pack()
    print(f"{client_address} Sending response of length {len(response)} bytes")
    server_socket.sendto(response, client_address)


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

        process_request_and_send(server_socket, client_address, request)

    except:
        pass


if __name__ == '__main__':
    synagogue_list.read_json()
    atexit.register(exit_handler)

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
