import struct
import typing

DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_SERVER_PORT = 9999
BUFFER_SIZE = 65555

'''
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Total Length         | Res.|b1|b2|b3| Status Code    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                              Data                             +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
Total Length: 16 bits = 2 bytes -> H
Reserved + Flags + Status Code: 3 bits + 3 bits + 10 bits = 2 byte -> H
'''


class mHeader:
    HEADER_FORMAT: typing.Final[str] = '!HH'
    HEADER_MIN_LENGTH: typing.Final[int] = struct.calcsize(HEADER_FORMAT)
    # Big enough to hold the header and a lot of data
    HEADER_MAX_LENGTH: typing.Final[int] = 2 ** 16
    HEADER_MAX_DATA_LENGTH: typing.Final[int] = HEADER_MAX_LENGTH - \
                                                HEADER_MIN_LENGTH

    # 16 bits -> 2**16 possible values -> 0 to 2**16 - 1
    MAX_CACHE_CONTROL: typing.Final[int] = 2 ** 16 - 1

    STATUS_OK: typing.Final[int] = 200
    STATUS_CLIENT_ERROR: typing.Final[int] = 400
    STATUS_SERVER_ERROR: typing.Final[int] = 500
    STATUS_UNKNOWN: typing.Final[int] = 999

    def __init__(self, total_length: typing.Optional[int], reserved: int, bool1: bool, bool2: bool, bool3: bool,
                 status_code: int,
                 data: bytes = b'') -> None:
        self.total_length = total_length
        if self.total_length is None:
            self.total_length = self.HEADER_MIN_LENGTH + len(data)
        self.reserved = reserved
        self.bool1 = bool1
        self.bool2 = bool2
        self.bool3 = bool3
        self.status_code = status_code
        self.data = data

    def pack_flags(self, reserved, bool1, bool2, bool3, status_code):
        return (reserved << 13) | (bool1 << 12) | (bool2 << 11) | (bool3 << 10) | status_code

    @staticmethod
    def unpack_flags(flags: int):
        status_code = flags & ((1 << 10) - 1)  # flags & 0b000_0_0_0_1111111111
        bool1 = flags & (1 << 10)  # flags & 0b000_0_0_1_0000000000
        bool2 = flags & (1 << 11)  # flags & 0b000_0_1_0_0000000000
        bool3 = flags & (1 << 12)  # flags & 0b000_1_0_0_0000000000
        # flags & 0b111_0_0_0_0000000000
        reserved = (flags >> 13) & ((1 << 3) - 1)
        return reserved, bool(bool1), bool(bool2), bool(bool3), status_code

    def pack(self) -> bytes:
        return struct.pack(self.HEADER_FORMAT, self.total_length,
                           self.pack_flags(self.reserved, self.bool1, self.bool2, self.bool3,
                                           self.status_code)) + self.data

    @classmethod
    def unpack(cls, data: bytes) -> 'mHeader':
        if len(data) < cls.HEADER_MIN_LENGTH:
            raise ValueError(f'The data is too short ({len(data)} bytes) to be a valid header')
        total_length, flags = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_MIN_LENGTH])
        reserved, bool1, bool2, bool3, status_code = cls.unpack_flags(flags)
        return cls(total_length=total_length, reserved=reserved,
                   bool1=bool1, bool2=bool2, bool3=bool3, status_code=status_code, data=data[cls.HEADER_MIN_LENGTH:])

    def __str__(self):
        return f'{self.__class__.__name__}( total_length={self.total_length}, reserved={self.reserved}, bool1={self.bool1}, bool2={self.bool2}, bool3={self.bool3}, status_code={self.status_code}, data={self.data})'


'''
 python3 protocol "length:16, isRequest:1, isList:1, nosah:4, Status Code :10, Checksum:16, Window:16, data:256"
 
 * Total Length (16 bits = 2 bytes):
    The total length of the packet, in bytes (including the header and the data)
    This minimum value is 8 bytes (header only)

* Flags (3 bits):
    - isRequest (1 bit):
        Whether  (1 = request, 0 = response)
    - isList (1 bit):
        Whether the data containts 1 = just list of id's of synagogue(both for request and respone for query)
        0 = query contains string to do contains to titles  
    - nosah (4 bit):
        Whether only for request, 0 if response
        SPARAD = 1
        ASHCANZE =2
        SPARADI = 3
        BALADY = 4
        SHAMI = 5 //room to add
        All = 15
        
* Status Code (10 bits):
    The status code of the response (only valid if the packet is a response)
    2xx = success, 4xx = client error, 5xx = server error, 0 = not a response
    
* Checksum (16 bits):
    to check if packet is not currapted
    
* Window (16 bits):
    to help with flow control
    
* Data (at most 65440 bits = 8180 bytes):
    The data of the packet
    It's at most 65440 bits because the total length is 16 bits, and the minimum value is 8 bytes (header only)
    2^16 - 12*8 = 65440
    contains:
        request: 
                query -> string to do contains for titles
                 list -> int[] to find specially synagogue id's
        respunse:
                list -> int[] answer to query to know to who to wait
                synagogue -> the object    
                 
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             length            |i|i|nosah |     Status Code    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|            Checksum           |             Window            |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                                                               +
|                                                               |
+                              data                             +
|                                                               |
+                                                               +
|                                                               |
+                                                               +
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


'''
