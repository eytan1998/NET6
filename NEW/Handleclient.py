import api
from RUDP.RUDPclient import RUDPclient


from synagogue import Nosah
from synagogue import City



def send_login(connection: RUDPclient, mId, password):
    request = api.AppHeader(0, api.Kind.REQUEST_LOGIN.value, Nosah.NULL, City.NULL,
                            (mId + ',' + password).encode())

    response = connection.sendData(request.pack())
    if response is None: return None
    return api.AppHeader.unpack(response)


def send_request_all_gabai(connection: RUDPclient):
    request = api.AppHeader(0, api.Kind.REQUEST_ALL_GABAI.value, Nosah.NULL.value, City.NULL.value, b'').pack()
    response = connection.sendData(request)

    response = api.AppHeader.unpack(response)
    if response.status_code == api.Status_code.NOT_FOUND.value: return None
    return send_request_gabai_by_id(connection, list(response.data))


def send_edit_syng(connection, syng):
    request = api.AppHeader(0, api.Kind.SET_SYNAGOGUE.value, Nosah.NULL, City.NULL, str(syng).encode()).pack()
    response = connection.sendData(request)
    response = api.AppHeader.unpack(response)
    return response.data.decode()


def send_edit_gabai(connection, gabai):
    request = api.AppHeader(0, api.Kind.SET_GABAI.value, Nosah.NULL, City.NULL, str(gabai).encode()).pack()
    response = connection.sendData(request)
    response = api.AppHeader.unpack(response)
    return response.data.decode()


def send_by_query(connection: RUDPclient, name, nosah, city):
    request = api.AppHeader(0, api.Kind.REQUEST_BY_QUERY.value, nosah, city, name.encode()).pack()
    response = connection.sendData(request)

    response = api.AppHeader.unpack(response)
    if response.status_code == api.Status_code.NOT_FOUND.value: return None
    return send_request_syng_by_id(connection, list(response.data))


def send_request_syng_by_id(connection: RUDPclient, ids):
    recvSyng = []
    for id_to_send in ids:
        request = api.AppHeader(0, api.Kind.REQUEST_SYNG_BY_ID.value, Nosah.NULL, City.NULL,
                                str(id_to_send).encode()).pack()
        ans = api.AppHeader.unpack(connection.sendData(request))
        if ans.status_code == api.Status_code.OK.value:
            recvSyng.append(ans)
    if len(recvSyng) <= 0: return None
    return recvSyng


def send_request_gabai_by_id(connection, ids):
    recvGabai = []
    for id_to_send in ids:
        request = api.AppHeader(0, api.Kind.REQUEST_GABAI_BY_ID.value, Nosah.NULL, City.NULL,
                                str(id_to_send).encode()).pack()
        ans = api.AppHeader.unpack(connection.sendData(request))
        if ans.status_code == api.Status_code.OK.value:
            recvGabai.append(ans)
    if len(recvGabai) <= 0: return None
    return recvGabai

#
# def client(server_address: tuple[str, int], ids: list) -> None:
#     server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
#     port = server_address[1]
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
#         client_socket.bind(('', port + 1))
#         client_socket.connect(server_address)
#         print(f"{server_prefix} Connection established")
#
#         try:
#             request = api.AppHeader(None, api.Kind.REQUEST_BY_IDS.value, Nosah.NULL, 0, 1, 1, bytes(ids))
#             checksum = checksum_calculator(request.pack())
#
#             udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
#             request = request.pack()
#             packet_with_header = udp_header + request
#
#             print(f"{server_prefix} Sending request of length {len(request)} bytes")
#             client_socket.sendto(packet_with_header, server_address)
#
#             response = client_socket.recv(api.BUFFER_SIZE)
#             print(f"{server_prefix} Got response of length {len(response)} bytes")
#             response = api.AppHeader.unpack(response)
#             print(response)
#         except Exception as e:
#             print(f"{server_prefix} Unexpected error: {str(e)}")
#     print(f"{server_prefix} Connection closed")

# if __name__ == "__main__":
#     arg_parser = argparse.ArgumentParser(description="A Calculator Client.")
#
#     arg_parser.add_argument("-p", "--port", type=int,
#                             default=api.DEFAULT_SERVER_PORT, help="The port to connect to.")
#     arg_parser.add_argument("-H", "--host", type=str,
#                             default=api.DEFAULT_SERVER_HOST, help="The host to connect to.")
#
#     args = arg_parser.parse_args()
#
#     host = args.host
#     port = args.port
#
#     client((host, port),[2])
