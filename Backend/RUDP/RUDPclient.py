import random
import socket

from Backend.RUDP.CC import CC
from Backend.RUDP.rudp_packet import RUDP_Header
from Backend.Help.app_packet import AppHeader

MAX_BUFFER = 65535
SEGMENT_MAX_SIZE = 65535
TIME_OUT = 0.5
TIME_GIVEUP_CONNECT = 10 / TIME_OUT  # 10 sec to give up sending syn
TIME_GIVEUP_CLOSE = 3  # 3 times to give up sending fin


class RUDPclient:
    def __init__(self, to_address: tuple[str, int], from_address: tuple[str, int]):
        self.dest_win_size = 0
        self.my_win_size = MAX_BUFFER
        self.cwnd = CC()

        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.m_socket.bind(from_address)  # for address
        self.m_socket.settimeout(TIME_OUT)

        self.buffer = b''
        self.server_address = to_address
        self.seq_num = 0
        # for more accurate
        self.seq_num = random.randint(100, 1000000)
        self.ack_num = 0

    def connect(self):
        print("-----------------------------connection state----------------------------")

        response = None
        # send syn
        request = RUDP_Header(self.seq_num, 0, None, 0, True, False, True, False, self.my_win_size, b'')
        request.checksum = RUDP_Header.checksum_func(request.pack())
        print("client syn:" + str(request))
        request = request.pack()
        # update after send
        self.seq_num += 1
        tries = 0
        while True:
            self.m_socket.sendto(request, self.server_address)
            # get ack
            message = self.receiveFrom(None)
            tries += 1
            if tries >= TIME_GIVEUP_CONNECT: break
            if message is None:
                continue
            response = message
            if not response.ACK or not response.SYN: continue
            self.ack_num = response.ack_num
            break
        if tries >= TIME_GIVEUP_CONNECT: return None  # if cant connect
        print("server syn|ack : " + str(response))
        # update after recv
        self.ack_num = response.seq_num + 1

        # send ack
        request = RUDP_Header(self.seq_num, self.ack_num, None, 0, False, True, True, False, self.my_win_size,
                              b'')
        request.checksum = RUDP_Header.checksum_func(request.pack())
        print("client ack:" + str(request))
        request = request.pack()
        self.m_socket.sendto(request, self.server_address)
        # update after send
        self.seq_num += 1
        print("-----------------------------request state----------------------------")

        return 0

    def close(self):
        print("-----------------------------close state----------------------------")

        response = None

        # send fin
        request = RUDP_Header(self.seq_num, self.ack_num, None, 0, False, True, True, True, self.my_win_size, b'')
        request.checksum = RUDP_Header.checksum_func(request.pack())
        print("client fin:" + str(request))
        request = request.pack()
        tries = 0
        while True:
            self.m_socket.sendto(request, self.server_address)
            # get ack
            message = self.receiveFrom(None)
            tries += 1
            if tries >= TIME_GIVEUP_CLOSE: break
            if message is None:
                continue
            response = message
            if not response.ACK or not response.FIN: continue
            break
        if tries >= TIME_GIVEUP_CLOSE: return None  # if cant disconnect
        print("server fin|ack : " + str(response))

        # send ack
        request = RUDP_Header(self.seq_num + 1, response.seq_num + 1, None, 0, False, True, True, False,
                              self.my_win_size, b'')
        request.checksum = RUDP_Header.checksum_func(request.pack())
        print("client ack:" + str(request))
        request = request.pack()
        self.m_socket.sendto(request, self.server_address)
        self.m_socket.close()

    def receiveFrom(self, msg_in_timeout):
        msg = None
        try:
            msg = self.m_socket.recvfrom(self.my_win_size)
            msg = msg[0]
            if msg is None:
                return None
            msg = RUDP_Header.unpack(msg)
            if not msg.verify_checksum():
                print("bad checksum")
                return None

        except socket.timeout:
            if msg_in_timeout is not None:
                print(msg_in_timeout)
        return msg

    # get AppHeader.pack()
    def sendData(self, request: AppHeader):
        # 1 send segments
        data = request.pack()
        start = 0
        end = min(self.dest_win_size, self.cwnd.getCWND(), SEGMENT_MAX_SIZE, len(data))
        while True:
            the_end = (end == len(data))
            # send
            replay = RUDP_Header(self.seq_num, self.ack_num, None, 0, False, True, the_end, False, self.my_win_size
                                 , data[start:end])
            # send so update seq
            self.seq_num += len(replay.data)

            replay.checksum = RUDP_Header.checksum_func(replay.pack())
            print("client: " + str(len(data[start:end])) + " : " + str(replay))
            replay = replay.pack()
            # stop and wait for ack
            while True:
                self.m_socket.sendto(replay, self.server_address)
                # 2 get ack for segment
                received = self.receiveFrom(None)
                # 2.1 process
                if received is None:
                    self.cwnd.lowCWND()
                    continue
                if not received.ACK: continue
                if received.ack_num < self.seq_num:
                    print("Got wrong ack: "+str(received.ack_num)+ ", but seq is: "+str(self.seq_num))
                    continue
                break
            print("server ack: " + str(len(received.data)) + " : " + str(received))
            # got packet so update ack
            self.ack_num = received.seq_num + len(received.data)
            self.cwnd.raiseCWND()
            self.dest_win_size = received.win_size

            # finish segment see if the end
            if the_end:
                break
            start = end
            end = min(end + self.dest_win_size, end + self.cwnd.getCWND(), end + SEGMENT_MAX_SIZE, len(data))
        # 3 sent all now receive
        # get App header
        return self.receiveData()

    def make_ack(self, request: RUDP_Header):
        ack = RUDP_Header(self.seq_num, request.seq_num + len(request.data), None, 0, False, True, False, False,
                          self.my_win_size, b'')
        return ack

    def receiveData(self) -> AppHeader:
        # receive data
        while True:
            # 1 receive
            received = self.receiveFrom(None)
            # 2 process
            if received is None:
                self.cwnd.lowCWND()
                continue
            if received.ack_num < self.seq_num:
                print("Got wrong ack: " + str(received.ack_num) + ", but seq is: " + str(self.seq_num))
                continue
            # All good
            print("server : " + str(len(received.data)) + " : " + str(received))
            self.cwnd.raiseCWND()
            self.dest_win_size = received.win_size

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
            print("client ack: " + str(len(send.data)) + " : " + str(send))
            send = send.pack()
            self.m_socket.sendto(send, self.server_address)
            # 4 combine all segments
            if received.PUSH and len(received.data) > 0:
                # TODO
                if self.buffer == b'':
                    self.buffer = received.data
                print("ensemble segment total length : " + str(len(self.buffer)))
                the_packet = AppHeader.unpack(self.buffer)
                self.buffer = b''
                # print("result: " + str(the_packet))

                return the_packet
