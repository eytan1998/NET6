import socket

from records import record_list

if __name__ == '__main__':

    records_list = record_list(5)
    records_list.read_json()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 6547))

    while True:
        try:
            message, address = server_socket.recvfrom(1024)
            ans = records_list.get_answer(message)
            server_socket.sendto(ans.encode(), address)
        except KeyboardInterrupt:
            records_list.write_json()
            server_socket.close()
            print("\n[!] Server shutting down, saving data to json...")
            break
