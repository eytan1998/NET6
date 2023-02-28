import argparse
import atexit
import json
import socket
import struct
import threading

from UDP.UDPclient import checksum_calculator
from synagogue import SynagogueList, Synagogue, Nosah, City
from gabai import Gabai

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


def client_handler(server_socket, data, client_address) -> None:
    udp_header = data[:16]
    data1 = data[16:]
    udp_header = struct.unpack("!IIII", udp_header)
    correct_checksum = udp_header[3]
    # print(correct_checksum)
    # print(checksum_calculator(data1))
    data = data1
    if not data:
        return
    try:
        try:
            request = api.mHeader.unpack(data)
        except Exception as e:
            raise e

        print(f"{client_address} Got request of length {len(data)} bytes")
        print(f"{client_address} got " + str(request))

        process_request_and_send(server_socket, client_address, request)

    except:
        pass


def process_request_and_send(server_socket, client_address, request: api.mHeader):
    if request.kind == api.Kind.REQUEST_BY_QUERY.value:
        temp = synagogue_list.get_by_name_and_nosah(request.data.decode(), request.nosah)
        if temp is None:
            send_response(server_socket, client_address, None)

        if temp is not None:
            send_response(server_socket, client_address,
                          api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0, bytes(temp)))

    elif request.kind == api.Kind.REQUEST_BY_IDS.value:
        list_of_ids = list(request.data)
        if list_of_ids is None: send_response(server_socket, client_address, None)
        for id_in_list in list_of_ids:
            temp = synagogue_list.get_by_id(id_in_list)
            if temp is None:
                send_response(server_socket, client_address, None)
            else:
                send_response(server_socket, client_address,api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0,str(temp).encode()))

    elif request.kind == api.Kind.SET_SYNAGOGUE.value:
        ans = synagogue_list.set_by_id(Synagogue.fromJSON(request.data.decode()))
        print(synagogue_list.get_by_id(1))
        if ans == 0:
            send_response(server_socket, client_address,
            api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0, "sucsseful".encode()))

        elif ans == -1:
            send_response(server_socket, client_address,
            api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0, "fail".encode()))


def send_response(server_socket, client_address, response):
    if response is None:
        send_response(server_socket, client_address,
        api.mHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0, "not found".encode()))
    else:
        print(f"{client_address} Sending " + str(response))
        response = response.pack()
        print(f"{client_address} Sending response of length {len(response)} bytes")
        server_socket.sendto(response, client_address)


if __name__ == '__main__':
    synagogue_list.read_json()
    atexit.register(exit_handler)
    # g = Gabai("eitan", 92929, "1234", "0512312312", [1, 2])
    # g1 = Gabai("oz", 732433229, "51241", "099999", [9])
    # synagogue_list.append(Synagogue("שמש ומגן", 1, Nosah.ASHCANZE, City.JERULEAM, "12345676543456787654", g))
    # synagogue_list.append(Synagogue("שמש שלום", 2, Nosah.SPARAD, City.JERULEAM, "'קראטוןםפםןוטארקראטון'", g))
    # synagogue_list.append(Synagogue("יונת שלום", 9, Nosah.SHAMI, City.ALL, "iuytrewrtyuioiuytrtyu", g1))
    # synagogue_list.write_json()

    arg_parser = argparse.ArgumentParser(
        description='Server.')

    arg_parser.add_argument('-p', '--port', type=int,
                            default=api.DEFAULT_SERVER_PORT, help='The port to listen on.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default=api.DEFAULT_SERVER_HOST, help='The host to listen on.')

    args = arg_parser.parse_args()
    host = args.host
    port = args.port

    server(host, port)
