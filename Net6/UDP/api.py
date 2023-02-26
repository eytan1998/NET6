import enum
import struct
import typing
import warnings
import  synagogue
DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_SERVER_PORT = 9999
BUFFER_SIZE = 65555

'''
 python3 protocol "length:16, kind:2, nosah:4, Status Code :10, Checksum:16, Window:16, data:256"
 
 * Total Length (16 bits = 2 bytes):
    The total length of the packet, in bytes (including the header and the data)
    This minimum value is 8 bytes (header only)

* Flags (3 bits):
    - kind (2 bit):
        REQUEST_BY_ID'S = 0 
        REQUEST_BY_QUERY = 1
        SET_BY_ID = 2
        RESPONSE = 3
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
                query -> string to do contains for titles (kind = 1)
                list -> int[] to find specially synagogue id's (kind = 0)
                edit synagogue (kind =2 ) 
        response: (differ by the caller)
                list -> int[] answer to query to know to who to wait (kind =3)
                synagogue -> the object (kind =3)
                 
 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             length            |kind |nosah |    Status Code   |
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
Length: 16 bits = 2 bytes -> H
kind + nosah + Status Code: 2 bits + 4 bits + 10 bits = 2 byte -> H
Checksum: 16 bits = 2 bytes -> H
Window: 16 bits = 2 bytes -> H
'''


class Kind(enum.Enum):
    REQUEST_BY_IDS = 0
    REQUEST_BY_QUERY = 1
    SET_BY_ID = 2
    RESPONSE = 3




class Status_code(enum.Enum):
    NULL = 0
    STATUS_OK = 200
    STATUS_CLIENT_ERROR = 400
    STATUS_SERVER_ERROR = 500
    STATUS_UNKNOWN = 999


class mHeader:
    HEADER_FORMAT: typing.Final[str] = '!HHHH'
    HEADER_MIN_LENGTH: typing.Final[int] = struct.calcsize(HEADER_FORMAT)
    # Big enough to hold the header and a lot of data
    HEADER_MAX_LENGTH: typing.Final[int] = 2 ** 16
    HEADER_MAX_DATA_LENGTH: typing.Final[int] = HEADER_MAX_LENGTH - \
                                                HEADER_MIN_LENGTH

    # 16 bits -> 2**16 possible values -> 0 to 2**16 - 1
    MAX_CACHE_CONTROL: typing.Final[int] = 2 ** 16 - 1

    #  "length:16, kind:2, nosah:4, Status Code :10, Checksum:16, Window:16, data:256"

    def __init__(self, length: typing.Optional[int], kind: int, nosah: int, status_code: int, checksum: int,
                 window: int,
                 data: bytes = b'') -> None:
        self.length = length
        if self.length is None:
            self.length = self.HEADER_MIN_LENGTH + len(data)
        if not (self.HEADER_MIN_LENGTH <= self.length <= self.HEADER_MAX_LENGTH):
            raise ValueError(
                f'Invalid total length: {self.length} (must be between {self.HEADER_MIN_LENGTH} and {self.HEADER_MAX_LENGTH} bytes inclusive)')
        elif self.length != self.HEADER_MIN_LENGTH + len(data):
            warnings.warn(f'The total length ({self.length}) does not match the length of the data ({len(data)})')
        self.status_code = status_code
        self.kind = kind

        if self.kind != 3 and self.status_code != 0:
            warnings.warn(f'The status code ({Status_code(self.status_code)}) is not 0 for a request')
        self.nosah = nosah
        if self.kind != 1 and self.nosah != 0:
            warnings.warn(f'The nosah ({synagogue.Nosah(self.nosah)}) is not 0 for a not query')
            self.nosah = 0
        self.checksum = checksum
        self.window = window

        self.data = data
        if len(self.data) > self.HEADER_MAX_DATA_LENGTH:
            raise ValueError(
                f'Invalid data length: {len(self.data)} (must be at most {self.HEADER_MAX_DATA_LENGTH} bytes)')

    def pack_flags(self, kind, nosah, status_code):
        return (kind << 14) | (nosah << 10) | status_code

    @staticmethod
    def unpack_flags(flags: int):
        status_code = flags & ((1 << 10) - 1)  # flags & 0b00_0000_1111111111
        nosah = (flags & (15 << 10)) >> 10  # flags & 0b00_1111_0000000000
        kind = (flags & (3 << 14)) >> 14  # flags & 0b11_0000_0000000000
        return kind, nosah, status_code

    def pack(self) -> bytes:
        return struct.pack(self.HEADER_FORMAT, self.length,
                           self.pack_flags(self.kind, self.nosah, self.status_code), self.checksum,
                           self.window) + self.data

    @classmethod
    def unpack(cls, data: bytes) -> 'mHeader':
        if len(data) < cls.HEADER_MIN_LENGTH:
            raise ValueError(f'The data is too short ({len(data)} bytes) to be a valid header')
        length, flags, checksum, window = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_MIN_LENGTH])
        kind, nosah, status_code = cls.unpack_flags(flags)
        return cls(length=length, kind=kind, status_code=status_code,
                   nosah=nosah, checksum=checksum, window=window, data=data[cls.HEADER_MIN_LENGTH:])

    def __str__(self):
        return f'{self.__class__.__name__}( total_length={self.length}, kind={Kind(self.kind)}, nosah={synagogue.Nosah(self.nosah)}, status_code={Status_code(self.status_code)}, checksum={self.checksum}, window={self.window}, data={self.data.decode()})'
