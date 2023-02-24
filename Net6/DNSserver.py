import time
import socket
from records import record, record_list, contains
import atexit


def exit_handler():
    records_list.write_json()
    print("end, saved to json")


def get_Host_name_IP(domain):
    try:
        host_ip = socket.gethostbyname(domain)
        return host_ip
    except:
        return None


if __name__ == '__main__':

    records_list = record_list()
    records_list.read_json()
    atexit.register(exit_handler)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', 12000))

    while True:
        message, address = server_socket.recvfrom(1024)

        temp = records_list.is_contains(message.decode())
        if temp[0] == contains.UP_TO_DATE:
            server_socket.sendto(temp[1].address.encode(), address)
            print("from list, time lest is mils: " + str(150000-(time.time() * 1000 - temp[1].ttl)))
            continue
        ans = get_Host_name_IP(message.decode())
        if ans is None:
            if temp[1] == contains.EXPAIRE:
                server_socket.sendto(temp[1].address.encode(), address)

                print("expired")
            else:
                print("cant get ip")
        else:
            print("added to list")
            records_list.append(record(ans.decode(), ans, time.time() * 1000))
        server_socket.sendto(ans.encode(), address)
