import api
from gabai import Gabai
from synagogue import Synagogue, Nosah, City


# the_synagogue_list = SynagogueList()
# the_gabi_list = GabaiList()
#
#
# def exit_handler():
#     the_synagogue_list.write_json()
#     the_gabi_list.write_json()
#     print("end, saved to json")
#

# def server(host: str, port: int) -> None:
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
#         server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         server_socket.bind((host, port))
#
#         threads = []
#         print(f"Listening on {host}:{port}")
#
#         while True:
#             try:
#                 massage, address = server_socket.recvfrom(api.BUFFER_SIZE)
#                 # Create a new thread to handle the client request
#                 thread = threading.Thread(target=client_handler, args=(server_socket,
#                                                                        massage, address))
#                 thread.start()
#                 threads.append(thread)
#             except KeyboardInterrupt:
#                 print("Shutting down...")
#                 break
#
#         for thread in threads:  # Wait for all threads to finish
#             thread.join()
#

#
# def client_handler(server_socket, data, client_address) -> None:
#     udp_header = data[:16]
#     data1 = data[16:]
#     udp_header = struct.unpack("!IIII", udp_header)
#     correct_checksum = udp_header[3]
#     # print(correct_checksum)
#     # print(checksum_calculator(data1))
#     data = data1
#     if not data:
#         return
#     try:
#         try:
#             request = api.AppHeader.unpack(data)
#         except Exception as e:
#             raise e
#
#         print(f"{client_address} Got request of length {len(data)} bytes")
#         print(f"{client_address} got " + str(request))
#
#         process_request_and_send(server_socket, client_address, request)
#
#     except:
#         pass


def process_request(request: api.AppHeader):
    import server
    the_synagogue_list = server.getSynagogues()
    the_gabi_list = server.getGabais()

    if request.kind == api.Kind.REQUEST_BY_QUERY.value:
        temp = the_synagogue_list.get_by_name_and_nosah_and_city(request.data.decode(), request.nosah, request.city)
        if temp is None:
            return api.AppHeader(api.Status_code.NOT_FOUND.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, b'')

        if temp is not None:
            return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                                 bytes(temp))

    elif request.kind == api.Kind.REQUEST_SYNG_BY_ID.value:
        the_data_got = request.data.decode()
        try:
            the_data_got = int(the_data_got)
            temp = the_synagogue_list.get_by_id(the_data_got)
        except:
            temp = None
        if temp is None:
            return api.AppHeader(api.Status_code.NOT_FOUND.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, b'')
        else:
            return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                                 temp.toJSON().encode())

    elif request.kind == api.Kind.SET_SYNAGOGUE.value:
        syng = Synagogue.fromJSON(request.data.decode())
        ans = the_synagogue_list.edit(syng, the_gabi_list.get_by_id(syng.gabai.gabai_id))
        the_synagogue_list.write_json()
        the_gabi_list.write_json()

        return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, str(ans).encode())

    elif request.kind == api.Kind.SET_GABAI.value:
        gabai = Gabai.fromJSON(request.data.decode())
        ans = the_gabi_list.edit(gabai, the_synagogue_list)
        the_gabi_list.write_json()

        return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, str(ans).encode())

    elif request.kind == api.Kind.REQUEST_ALL_GABAI.value:
        ids = []
        for gabai_to_send in the_gabi_list.gabai_list:
            ids.append(gabai_to_send.gabai_id)
        return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                             City.NULL.value, bytes(ids))

    elif request.kind == api.Kind.REQUEST_GABAI_BY_ID.value:
        the_data_got = request.data.decode()
        try:
            the_data_got = int(the_data_got)
            temp = the_gabi_list.get_by_id(the_data_got)
        except:
            temp = None
        if temp is None:
            return api.AppHeader(api.Status_code.NOT_FOUND.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, b'')
        else:
            return api.AppHeader(api.Status_code.OK.value, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value,
                                 temp.toJSON().encode())

    elif request.kind == api.Kind.REQUEST_LOGIN.value:
        the_data_got = request.data.decode().split(',')
        try:
            int(the_data_got[0])
        except:
            the_data_got[0] = 0
        the_gabai = the_gabi_list.get_by_id(int(the_data_got[0]))
        if the_gabai is None:
            return api.AppHeader(api.Status_code.WRONG_ID.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                 City.NULL.value, b'')
        else:
            if the_gabai.password == the_data_got[1]:
                return api.AppHeader(api.Status_code.CORRECT_LOGIN.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                     City.NULL.value, str(the_gabai).encode())
            else:
                return api.AppHeader(api.Status_code.WRONG_PASSWORD.value, api.Kind.RESPONSE.value, Nosah.NULL.value,
                                     City.NULL.value, b'')

#
# def send_response(server_socket, client_address, response):
#     if response is None:
#         send_response(server_socket, client_address,
#                       api.AppHeader(None, api.Kind.RESPONSE.value, Nosah.NULL.value, City.NULL.value, 1234, 0,
#                                   "not found".encode()))
#     else:
#         # print(f"{client_address} Sending " + str(response))
#         response = response.pack()
#         print(f"{client_address} Sending response of length {len(response)} bytes")
#         server_socket.sendto(response, client_address)


# if __name__ == '__main__':
#     the_synagogue_list.read_json()
#     the_gabi_list.read_json()
#     atexit.register(exit_handler)
#     arg_parser = argparse.ArgumentParser(
#         description='Server.')
#
#     arg_parser.add_argument('-p', '--port', type=int,
#                             default=api.DEFAULT_SERVER_PORT, help='The port to listen on.')
#     arg_parser.add_argument('-H', '--host', type=str,
#                             default=api.DEFAULT_SERVER_HOST, help='The host to listen on.')
#
#     args = arg_parser.parse_args()
#     host = args.host
#     port = args.port
#
#     server(host, port)
