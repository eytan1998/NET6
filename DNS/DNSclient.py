import socket

if __name__ == '__main__':
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0)
    message = input()
    addr = ("127.0.0.1", 6547)
    client_socket.sendto(message.encode(), addr)
    try:
        data, server = client_socket.recvfrom(1024)
        print(data.decode())
    except socket.timeout:
        print('REQUEST TIMED OUT')