'''
python3 protocol "sec_num:32,ack_num:32,padd:12,SYN:1,ACK:1,PUSH:1,FIN:1,win_size:16"
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            sec_num                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                            ack_num                            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          padd         |S|A|P|F|            win_size           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                               data                            |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

sec_num: 32 bits = 4 bytes -> L
ack_num: 32 bits = 4 bytes -> L
padd + flags 2 byte -> H
Window: 16 bits = 2 bytes -> H



'''
import struct
import typing

from api import AppHeader


class RUDP_Header:
    HEADER_FORMAT: typing.Final[str] = '!LLHH'
    HEADER_MIN_LENGTH: typing.Final[int] = struct.calcsize(HEADER_FORMAT)
    # Big enough to hold the header and a lot of data
    HEADER_MAX_LENGTH: typing.Final[int] = 2 ** 16
    HEADER_MAX_DATA_LENGTH: typing.Final[int] = HEADER_MAX_LENGTH - \
                                                HEADER_MIN_LENGTH

    # 16 bits -> 2**16 possible values -> 0 to 2**16 - 1
    MAX_CACHE_CONTROL: typing.Final[int] = 2 ** 16 - 1

    # python3 protocol "sec_num:32,ack_num:32,padd:12,SYN:1,ACK:1,PUSH:1,FIN:1,win_size:16"
    def __init__(self, seq_num: int, ack_num: int, SYN: bool, ACK: bool, PUSH: bool, FIN: bool,
                 win_size: int,
                 data: bytes = b'') -> None:
        # If the SYN flag is set (1), then this is the initial sequence number. The sequence number of the actual
        # first data byte and the acknowledged number in the corresponding ACK are then this sequence number plus 1.
        # If the SYN flag is clear (0), then this is the accumulated sequence number of the first data byte of this
        # segment for the current session.
        self.seq_num = seq_num

        # If the ACK flag is set then the value of this field is the next sequence number that the sender of the ACK
        # is expecting. This acknowledges receipt of all prior bytes (if any). The first ACK sent by each end
        # acknowledges the other end's initial sequence number itself, but no data.
        self.ack_num = ack_num
        self.padding = 0
        self.SYN = SYN
        self.ACK = ACK
        self.PUSH = PUSH
        self.FIN = FIN

        # The size of the receive window, which specifies the number of window size units[b] that the sender of this
        # segment is currently willing to receive.
        self.win_size = win_size
        self.data = data

    def get_data(self) -> bytes:
        return self.data

    def pack_flags(self, SYN: bool, ACK: bool, PUSH: bool, FIN: bool):
        return SYN << 3 | ACK << 2 | PUSH << 1 | FIN

    @staticmethod
    def unpack_flags(flags: int):
        SYN = (bool)((flags & (1 << 3)) >> 3)  # flags & 0b000000000000_1_0_0_0
        ACK = (bool)((flags & (1 << 2)) >> 2)  # flags & 0b000000000000_0_1_0_0
        PUSH = (bool)((flags & (1 << 1)) >> 1)  # flags & 0b000000000000_0_0_1_0
        FIN = (bool)(flags & 1)  # flags & 0b000000000000_0_0_0_1
        return SYN, ACK, PUSH, FIN

    # python3 protocol "sec_num:32,ack_num:32,padd:12,SYN:1,ACK:1,PUSH:1,FIN:1,win_size:16"
    def pack(self) -> bytes:
        return struct.pack(self.HEADER_FORMAT, self.seq_num, self.ack_num,
                           self.pack_flags(self.SYN, self.ACK, self.PUSH, self.FIN), self.win_size) + self.data

    @classmethod
    def unpack(cls, data: bytes) -> 'RUDP_Header':
        if len(data) < cls.HEADER_MIN_LENGTH:
            raise ValueError(f'The data is too short ({len(data)} bytes) to be a valid header')
        seq_num, ack_num, flags, win_size = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_MIN_LENGTH])
        SYN, ACK, PUSH, FIN = cls.unpack_flags(flags)
        return cls(seq_num=seq_num, ack_num=ack_num,
                   SYN=SYN, ACK=ACK, PUSH=PUSH, FIN=FIN, win_size=win_size, data=data[cls.HEADER_MIN_LENGTH:])

    @classmethod
    def make_syn(cls) -> 'RUDP_Header':
        return cls(0, 0, True, False, False, False, 0, b'')

    def __str__(self):
        # try:
        #     ans = f'{self.__class__.__name__}( seq_nun={self.seq_num}, ack_num={self.ack_num}, SYN={self.SYN},' \
        #           f''f'ACK={self.ACK}, PUSH={self.PUSH}, FIN={self.FIN}, win_size={self.win_size}, data={mHeader.unpack(self.data)})'
        # except:
        #     ans = f'{self.__class__.__name__}( seq_nun={self.seq_num}, ack_num={self.ack_num}, SYN={self.SYN},' \
        #           f''f'ACK={self.ACK}, PUSH={self.PUSH}, FIN={self.FIN}, win_size={self.win_size}, data={self.data.decode()})'
        ans = f'{self.__class__.__name__}( seq_nun={self.seq_num}, ack_num={self.ack_num}, SYN={self.SYN},' \
              f''f'ACK={self.ACK}, PUSH={self.PUSH}, FIN={self.FIN}, win_size={self.win_size})'
        return ans
