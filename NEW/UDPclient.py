import socket
import struct
import zlib

import api

try:
    from synagogue import Nosah
    from synagogue import City
except:
    from .synagogue import Nosah
    from .synagogue import City


def checksum_calculator(data):
    checksum = zlib.crc32(data)
    return checksum


def send_request_all_gabai(server_address):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)
        try:
            request = api.mHeader(None, api.Kind.REQUEST_ALL_GABAI.value, Nosah.NULL, City.NULL, 1234, 0, ''.encode())
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            number_to_get = client_socket.recv(api.BUFFER_SIZE)
            number_to_get = api.mHeader.unpack(number_to_get).data.decode()

            recvGabai = []
            for i in range(int(number_to_get)):
                response = client_socket.recv(api.BUFFER_SIZE)
                print(f"{server_prefix} Got response of length {len(response)} bytes")
                recvGabai.append(api.mHeader.unpack(response).data.decode())
            return recvGabai
        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


def send_edit_syng(server_address: tuple[str, int], syng):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)

        try:
            request = api.mHeader(None, api.Kind.SET_SYNAGOGUE.value, Nosah.NULL, City.NULL, 1234, 0,
                                  str(syng).encode())
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            response = api.mHeader.unpack(response)
            return response.data.decode()

        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


def send_edit_gabai(server_address: tuple[str, int], gabai):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)

        try:
            request = api.mHeader(None, api.Kind.SET_GABAI.value, Nosah.NULL, City.NULL, 1234, 0,
                                  str(gabai).encode())
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            response = api.mHeader.unpack(response)
            return response.data.decode()

        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


def send_by_query(server_address: tuple[str, int], name, nosah, city):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)

        try:
            request = api.mHeader(None, api.Kind.REQUEST_BY_QUERY.value, nosah, city, 1234, 0, name.encode())
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            response = api.mHeader.unpack(response)
            if response.data.decode() == "not found": return None
            return send_request_by_ids(server_address, list(response.data))

        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


def send_login(server_address: tuple[str, int], id, password):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)
        try:
            request = api.mHeader(None, api.Kind.REQUEST_LOGIN.value, Nosah.NULL, City.NULL, 1234, 0,
                                  (id + ',' + password).encode())
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            return api.mHeader.unpack(response).data.decode()

        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
        print(f"{server_prefix} Connection closed")


def send_request_by_ids(server_address: tuple[str, int], ids):
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 2))
        client_socket.connect(server_address)
        try:
            print(ids)
            request = api.mHeader(None, api.Kind.REQUEST_BY_IDS.value, Nosah.NULL, City.NULL, 1234, 0, bytes(ids))
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            recvSyng = []
            for i in range(len(ids)):
                response = client_socket.recv(api.BUFFER_SIZE)
                print(f"{server_prefix} Got response of length {len(response)} bytes")
                recvSyng.append(api.mHeader.unpack(response).data.decode())
            return recvSyng
        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")


def client(server_address: tuple[str, int], ids: list) -> None:
    server_prefix = f"{{{server_address[0]}:{server_address[1]}}}"
    port = server_address[1]
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)
        print(f"{server_prefix} Connection established")

        try:
            request = api.mHeader(None, api.Kind.REQUEST_BY_IDS.value, Nosah.NULL, 0, 1, 1, bytes(ids))
            checksum = checksum_calculator(request.pack())

            udp_header = struct.pack("!IIII", port + 1, port, request.length, checksum)
            request = request.pack()
            packet_with_header = udp_header + request

            print(f"{server_prefix} Sending request of length {len(request)} bytes")
            client_socket.sendto(packet_with_header, server_address)

            response = client_socket.recv(api.BUFFER_SIZE)
            print(f"{server_prefix} Got response of length {len(response)} bytes")
            response = api.mHeader.unpack(response)
            print(response)
        except Exception as e:
            print(f"{server_prefix} Unexpected error: {str(e)}")
    print(f"{server_prefix} Connection closed")

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
