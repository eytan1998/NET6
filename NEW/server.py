import argparse
import atexit
import socket
import threading

from RUDP.RUDPserver import RUDPserver
from gabai import GabaiList
from synagogue import SynagogueList

TIME_OUT = 0.2
the_synagogue_list = SynagogueList()
the_gabi_list = GabaiList()
the_synagogue_list.read_json()
the_gabi_list.read_json()



def getSynagogues():
    global the_synagogue_list
    return the_synagogue_list


def setSynagogues(list):
    global the_synagogue_list
    the_synagogue_list = list

def getGabais():
    global the_gabi_list
    return the_gabi_list


def UDPserver(host: str, port: int) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.settimeout(TIME_OUT)
        threads = []
        print(f"Listening on {host}:{port}")

        while True:
            try:
                connection = RUDPserver(server_socket)
                connection.accept()

                # Create a new thread to handle the client request
                thread = threading.Thread(target=connection.client_handler)
                thread.start()
                threads.append(thread)
            except KeyboardInterrupt:
                print("Shutting down...")
                # print(the_synagogue_list)
                # the_synagogue_list.append(Synagogue("asd", 123,0,0,"sadas"))
                # the_synagogue_list.write_json()
                break

        for thread in threads:  # Wait for all threads to finish
            thread.join()


if __name__ == '__main__':
    the_synagogue_list.read_json()
    the_gabi_list.read_json()
    arg_parser = argparse.ArgumentParser(
        description='Server.')

    arg_parser.add_argument('-p', '--port', type=int,
                            default=9879, help='The port to listen on.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default="127.0.0.1", help='The host to listen on.')

    args = arg_parser.parse_args()
    host = args.host
    port = args.port

    UDPserver(host, port)
    # atexit.register(exit_handler)
    #
    # addr = ("127.0.0.1", 9879)
    #
    # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    #     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #     server_socket.bind(addr)
    #     server_socket.settimeout(TIME_OUT)
    #     threads = []
    #     print(f"Listening on :" + str(addr))
    #
    #     while True:
    #         try:
    #             connection = RUDPserver(server_socket)
    #             connection.accept()
    #
    #             # Create a new thread to handle the client request
    #             thread = threading.Thread(target=connection.client_handler)
    #             thread.start()
    #             threads.append(thread)
    #         except KeyboardInterrupt:
    #             print("Shutting down...")
    #             getSynagogues().write_json()
    #             the_gabi_list.write_json()
    #             print("saved to json")
    #             break
    #     try:
    #         for thread in threads:  # Wait for all threads to finish
    #             thread.join()
    #     except:
    #         getSynagogues().write_json()
    #         the_gabi_list.write_json()
    #         print("saved to json")
