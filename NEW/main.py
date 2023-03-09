import socket
import struct


def checksum_func(data):
    checksum = 0
    data_len = len(data)
    if (data_len % 2):
        data_len += 1
        data += struct.pack('!B', 0)

    for i in range(0, data_len, 2):
        w = (data[i] << 8) + (data[i + 1])
        checksum += w

    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = ~checksum & 0xFFFF
    return checksum


def verify_checksum(data, checksum):
    data_len = len(data)
    if (data_len % 2) == 1:
        data_len += 1
        data += struct.pack('!B', 0)

    for i in range(0, data_len, 2):
        w = (data[i] << 8) + (data[i + 1])
        checksum += w
        checksum = (checksum >> 16) + (checksum & 0xFFFF)

    return checksum

def ip2int(ip_addr):
    if ip_addr == 'localhost':
        ip_addr = '127.0.0.1'
    return [int(x) for x in ip_addr.split('.')]


if __name__ == '__main__':
    port = 8989
    server_address = ("127.0.0.1", port)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        client_socket.bind(('', port + 1))
        client_socket.connect(server_address)

        data = b'hi new data'
        data_len = len(data)
        udp_length = 8 + data_len

        checksum = 0
        src_ip, dest_ip = ip2int(server_address[0]), ip2int(server_address[0])
        src_ip = struct.pack('!4B', *src_ip)
        dest_ip = struct.pack('!4B', *dest_ip)
        src_port = port + 1
        dest_port = port

        pseudo_header = struct.pack('!BBH', 0, socket.IPPROTO_UDP, udp_length)
        pseudo_header = src_ip + dest_ip + pseudo_header
        udp_header = struct.pack('!4H', src_port, dest_port, udp_length, checksum)
        checksum = checksum_func(pseudo_header + udp_header + data)
        udp_header = struct.pack('!4H', src_port, dest_port, udp_length, checksum)
        with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP) as s:
            s.sendto(udp_header + data, server_address)

