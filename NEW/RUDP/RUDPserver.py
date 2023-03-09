import socket

import Handelserver
from RUDP.rudp_packet import RUDP_Header
from api import AppHeader

MAX_WIN_SIZE = 65536
START_WIN_SIZE = 5000
SEGMENT_MAX_SIZE = 1000
TIMES_TO_EXIT = 3


class RUDPserver:
    def __init__(self, server_socket: socket):
        self.dest_win_size = MAX_WIN_SIZE
        self.my_win_size = START_WIN_SIZE

        self.server_socket = server_socket
        self.client_address = None
        self.buffer = b''
        self.seq_num = 0
        # for more accurate
        # self.seq_num = random.randint(100, 1000000)

    def accept(self):
        request = None
        while True:
            # get syn
            ans = self.recevFrom(True)
            if ans is None: continue
            request = RUDP_Header.unpack(ans[0])
            if not request.SYN: continue
            break
        # send syn acl
        self.client_address = ans[1]
        response = RUDP_Header(self.seq_num, request.seq_num + 1, True, True, True, False, self.my_win_size, b'')
        response = response.pack()
        while True:
            self.server_socket.sendto(response, self.client_address)
            # get ack
            ans = self.recevFrom()
            if ans is None:
                continue
            request = RUDP_Header.unpack(ans[0])
            if not request.ACK:
                continue
            # if request.ack_num < self.seq_num: continue
            break
        print("Connect to " + str(self.client_address))

    def recevFrom(self, accept: bool = True):
        msg = None
        try:
            msg = self.server_socket.recvfrom(self.my_win_size)
        except socket.timeout:
            if not accept:
                print('time out')
        return msg

    def client_handler(self) -> None:
        request = None
        ans = None
        while True:
            # get
            if ans is None:
                ans = self.recevFrom()
                if ans is None: continue
                request = RUDP_Header.unpack(ans[0])
                if self.seq_num > request.ack_num:
                    print("got wrong ack")
                    continue
                self.seq_num = request.ack_num
            if request.FIN: break
            # else
            response = self.make_ack(request)
            response = response.pack()
            while True:
                self.server_socket.sendto(response, self.client_address)
                # get replay
                ans = self.recevFrom()
                if ans is None: continue
                request = RUDP_Header.unpack(ans[0])
                # if not request.ACK: continue
                if self.seq_num >= request.ack_num:
                    print("got wrong ack")
                    ans = None
                break

        # send syn ack
        response = RUDP_Header(self.seq_num, request.seq_num + 1, False, True, True, True, self.my_win_size, b'')
        response = response.pack()

        # if client close and don't listen
        temp = 0
        while True:
            if temp >= TIMES_TO_EXIT: break
            self.server_socket.sendto(response, self.client_address)
            # get ack
            ans = self.recevFrom()
            temp += 1
            if ans is None: continue
            request = RUDP_Header.unpack(ans[0])
            if not request.ACK: continue
            break
        print("done with " + str(self.client_address))

    def make_ack(self, request: RUDP_Header):

        self.seq_num = request.ack_num
        self.buffer += request.data
        data = b''
        # print(len(self.buffer))
        # print(request)
        if request.PUSH and len(request.data) > 0:
            the_packet = AppHeader.unpack(self.buffer)
            self.buffer = b''
            data = Handelserver.process_request(the_packet)
            data = data.pack()

        replay = RUDP_Header(self.seq_num, request.seq_num + len(request.data), False, True, True, False,
                             self.my_win_size, data)
        return replay



# def chunkIt(seq):
#     avg = len(seq) / float(SEGMENT_MAX_SIZE)
#     out = []
#     last = 0.0
#
#     while last < len(seq):
#         out.append(seq[int(last):int(last + avg)])
#         last += avg
#
#     return out
