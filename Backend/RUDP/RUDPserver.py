import socket

from Backend.Help import Handelserver
from Backend.RUDP.rudp_packet import RUDP_Header
from Backend.Help.app_packet import AppHeader

MAX_BUFFER = 65535
SEGMENT_MAX_SIZE = 65535
TIMES_TO_EXIT = 3
START_CWND_SIZE = 10


class RUDPserver:
    def __init__(self, server_socket: socket):
        self.dest_win_size = 0
        self.my_win_size = MAX_BUFFER
        self.cwnd = START_CWND_SIZE
        self.server_socket = server_socket
        self.client_address = None
        self.buffer = b''
        self.ack_num = 0
        self.seq_num = 0

        # for more accurate
        # self.seq_num = random.randint(100, 1000000)

    def accept(self):
        request = None
        while True:
            # get syn
            ans = self.receiveFrom(None)
            if ans is None: continue
            request = ans
            if not request.SYN: continue
            break
        # send syn acl

        response = RUDP_Header(self.seq_num, request.seq_num + 1, None, 0, True, True, True, False, self.my_win_size,
                               b'')
        response.checksum = RUDP_Header.checksum_func(response.pack())
        response = response.pack()

        self.seq_num = self.seq_num + 1
        while True:
            self.server_socket.sendto(response, self.client_address)
            # get ack
            ans = self.receiveFrom(None)
            if ans is None:
                continue
            request = ans
            if not request.ACK:
                continue
            if request.ack_num < self.seq_num: continue
            break
        self.ack_num = request.ack_num
        print("Connect to " + str(self.client_address))

    def receiveFrom(self, msg_to_print) -> RUDP_Header | None:
        msg = None
        try:
            msg = self.server_socket.recvfrom(self.my_win_size)
            if self.client_address is None:
                self.client_address = msg[1]
            msg = msg[0]
            if msg is None:
                return None
            msg = RUDP_Header.unpack(msg)
            if not msg.verify_checksum():
                print("bad checksum")
                return None

        except socket.timeout:
            # got time out so cwnd half
            self.cwnd = int(self.cwnd / 2)
            if msg_to_print is not None:
                print(msg_to_print)
        if msg is not None:
            # got so update win
            self.dest_win_size = msg.win_size
        # got so increase cwnd
        self.cwnd = self.cwnd * 2
        return msg

    def receiveData(self) -> None:
        # receive data
        while True:
            # 1 receive
            received = self.receiveFrom(None)
            # 2 process
            if received is None:
                continue
            if received.FIN:
                break
            if received.ack_num < self.seq_num:
                # print("got wrong ack")
                continue
            # All good
            # only if new
            if self.ack_num != received.seq_num + len(received.data):
                self.buffer += received.data
                self.my_win_size -= len(received.data)

            # got packet so update ack
            self.ack_num = received.seq_num + len(received.data)

            # 3 send ack
            send = self.make_ack(received)
            # send so update seq
            self.seq_num += len(send.data)

            send.checksum = RUDP_Header.checksum_func(send.pack())
            send = send.pack()
            self.server_socket.sendto(send, self.client_address)

            # 4 send Data (optional)
            if received.PUSH and len(received.data) > 0:
                self.sendData(self.make_response(received))
        # if got FIN
        self.close(received)

    def make_ack(self, request: RUDP_Header):
        ack = RUDP_Header(self.seq_num, request.seq_num + len(request.data), None, 0, False, True, False, False,
                          self.my_win_size, b'')
        return ack

    def make_response(self, received: RUDP_Header):
        # TODO
        if self.buffer == b'':
            self.buffer = received.data

        the_packet = AppHeader.unpack(self.buffer)
        self.buffer = b''
        self.my_win_size = MAX_BUFFER
        data = Handelserver.process_request(the_packet)
        data = data.pack()

        replay = RUDP_Header(self.seq_num, received.seq_num + len(received.data), None, 0, False, True, True, False,
                             self.my_win_size, data)
        return replay

    def sendData(self, replay):
        # send in chunks
        if len(replay.data) > 0:
            data = replay.data
            start = 0
            end = min(self.dest_win_size, self.cwnd, SEGMENT_MAX_SIZE, len(data))
            while True:
                the_end = (end == len(data))
                # send
                replay = RUDP_Header(self.seq_num, self.ack_num, None, 0, False, True, the_end, False, self.my_win_size,
                                     data[start:end])
                # send so update seq
                self.seq_num += len(replay.data)

                replay.checksum = RUDP_Header.checksum_func(replay.pack())
                replay = replay.pack()
                # stop and wait for ack
                while True:
                    self.server_socket.sendto(replay, self.client_address)
                    # 1 get response ack
                    received = self.receiveFrom(None)
                    # 2 process
                    if received is None: continue
                    if not received.ACK: continue
                    if received.ack_num < self.seq_num:
                        # print("got wrong ack")
                        continue
                    break

                # got packet so update ack
                self.ack_num = received.seq_num + len(received.data)
                # finish segment see if the end
                if the_end:
                    break
                start = end
                end = min(end + self.dest_win_size, end + self.cwnd, end + SEGMENT_MAX_SIZE, len(data))

    def close(self, received):
        # send fin ack
        response = RUDP_Header(self.seq_num, received.seq_num + 1, None, 0, False, True, True, True, self.my_win_size,
                               b'')
        response.checksum = RUDP_Header.checksum_func(response.pack())
        response = response.pack()

        # if client close and don't listen
        temp = 0
        while True:
            if temp >= TIMES_TO_EXIT: break
            self.server_socket.sendto(response, self.client_address)
            # get ack
            ans = self.receiveFrom(None)
            temp += 1
            if ans is None: continue
            request = ans
            if not request.ACK: continue
            break
        print("done with " + str(self.client_address))
