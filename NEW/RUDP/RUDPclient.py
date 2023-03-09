import socket

from RUDP.rudp_packet import RUDP_Header

MAX_WIN_SIZE = 65536
START_WIN_SIZE = 5000
SEGMENT_MAX_SIZE = 1000
TIME_OUT = 0.1


class RUDPclient:
    def __init__(self, to_address: tuple[str, int]):
        self.dest_win_size = MAX_WIN_SIZE
        self.my_win_size = START_WIN_SIZE

        self.m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.m_socket.settimeout(TIME_OUT)

        self.server_address = to_address
        self.seq_num = 0
        # for more accurate
        # self.seq_num = random.randint(100, 1000000)
        self.ack_num = 0

    def connect(self):
        response = None
        # send syn
        request = RUDP_Header(self.seq_num, 0, True, False, True, False, self.my_win_size, b'')
        print("client syn:" + str(request))
        request = request.pack()
        while True:
            self.m_socket.sendto(request, self.server_address)
            # get ack
            message = self.recevFrom()
            if message is None: continue
            response = RUDP_Header.unpack(message[0])
            if not response.ACK or not response.SYN: continue
            self.ack_num = response.ack_num
            break
        print("server syn|ack : " + str(response))

        # send ack
        self.seq_num += 1
        request = RUDP_Header(self.seq_num, response.seq_num + 1, False, True, True, False, self.my_win_size, b'')
        print("client ack:" + str(request))
        request = request.pack()
        self.m_socket.sendto(request, self.server_address)

    def close(self):
        response = None
        # send fin
        request = RUDP_Header(self.seq_num, self.ack_num, False, True, True, True, self.my_win_size, b'')
        print("client fin:" + str(request))

        request = request.pack()
        while True:
            self.m_socket.sendto(request, self.server_address)
            # get ack
            message = self.recevFrom()
            if message is None: continue
            response = RUDP_Header.unpack(message[0])
            if not response.ACK or not response.FIN: continue
            break

        print("server fin|ack : " + str(response))

        # send ack
        request = RUDP_Header(self.seq_num + 1, response.seq_num + 1, False, True, True, False, self.my_win_size, b'')
        print("client ack:" + str(request))
        request = request.pack()
        self.m_socket.sendto(request, self.server_address)
        self.m_socket.close()

    def recevFrom(self):
        msg = None
        try:
            msg = self.m_socket.recvfrom(self.my_win_size)
        except socket.timeout:
            print('time out')
        return msg

    def sendData(self, data):
        start = 0
        response = None
        # print(len(data))
        end = min(SEGMENT_MAX_SIZE, len(data))
        while True:
            the_end = (end == len(data))
            # print(data[start:end])
            # send
            request = RUDP_Header(self.seq_num, self.ack_num, False, True, the_end, False, self.my_win_size,
                                  data[start:end])
            print("client: " + str(len(data[start:end]))+" - "+str(request))
            request = request.pack()
            while True:
                self.m_socket.sendto(request, self.server_address)
                # get response
                message = self.recevFrom()
                if message is None: continue
                response = RUDP_Header.unpack(message[0])
                if not response.ACK: continue
                if response.ack_num != self.seq_num + len(data[start:end]): continue
                break
            self.seq_num = self.seq_num + len(data[start:end])
            self.ack_num += len(response.data)

            print("server: " + str(len(response.data)) + " " + str(response))
            if the_end:
                break
            start = end
            end = min(len(data), end + SEGMENT_MAX_SIZE)
        return response.data

    # @staticmethod
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

    def recevData(self):
        receive = None
        while True:
            # get
            ans = self.recevFrom()
            if ans is None: continue
            receive = RUDP_Header.unpack(ans[0])
            # else
            send = self.make_ack(receive)
            send = send.pack()
            while True:
                self.m_socket.sendto(send, self.server_address)
                # get ack
                ans = self.recevFrom()
                if ans is None: continue
                send = RUDP_Header.unpack(ans[0])
                if not send.ACK: continue
                break
        return receive

    def make_ack(self, receive):
        self.seq_num = receive.ack_num
        response = RUDP_Header(self.seq_num, receive.seq_num + len(receive.data), False, True, False, False,
                               self.my_win_size, b'')
        return response
