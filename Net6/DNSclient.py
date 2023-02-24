import socket

for pings in range(1):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(5.0)
    message = 'google.com'
    addr = ("127.0.0.1", 12000)
    client_socket.sendto(message.encode(), addr)
    try:
        data, server = client_socket.recvfrom(1024)
        print(data.decode())
    except socket.timeout:
        print('REQUEST TIMED OUT')