import enum
import struct
import typing
import warnings

from synagogue import Nosah, City

DEFAULT_SERVER_HOST = "127.0.0.1"
DEFAULT_SERVER_PORT = 6666
BUFFER_SIZE = 65555

'''
 python3 protocol "length:16, kind:3, nosah:4, city :9, Window:16, padding:16 data:256"
 
 * Total Length (16 bits = 2 bytes):
    The total length of the packet, in bytes (including the header and the data)
    This minimum value is 8 bytes (header only)

* Flags (16 bits):
    - kind (3 bit):
        REQUEST_LOGIN = 0 data = id,pass
        REQUEST_BY_QUERY = 1
        REQUEST_BY_ID'S = 2
        REQUEST_ALL_GABAI = 3
        SET_SYNAGOGUE = 4
        SET_GABAI = 5 
        RESPONSE = 6
        
    - nosah (4 bit):
        NULL = 0
        SPARAD = 1
        ASHCANZE =2
        SPARADI = 3
        BALADY = 4
        SHAMI = 5 //room to add
        All = 15
        
    - city (9 bit):
        NULL =0  (not spec)
        JERUSLEM = 1
        ...
        
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
|             length            | kind|  nosah|       city      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|             Window            |             padding           |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                               data                            |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Length: 16 bits = 2 bytes -> H
kind + nosah + city: 3 bits + 4 bits + 9 bits = 2 byte -> H
Window: 16 bits = 2 bytes -> H
padding: 16 bits = 2 bytes -> H



C                  S
     -> login   id,pass  (saved gabai) : REQUEST_LOGIN
    <- gabai : RESPONSE (good?)
    
(admin):
        0. get all gabai REQUEST_ALL_GABAI,RESPONSE
       1. add _ gabai : SET_GABAI , RESPONSE (good?)
       2. del gabai (del synag) : SET_GABAI, RESPONSE (good?)
       
(gabai):
        0. get all synag: REQUEST_BY_ID'S : RESPONSE (multi synagogue) , ACK
        1. add synagogue: send synagogue :SET_SYNAGOGUE , RESPONSE (good?) ,ACK
        2. edit : send synagogue : SET_SYNAGOGUE , RESPONSE (good?), ACK
        3. del: send synagogue (empty but the id) : SET_SYNAGOGUE , RESPONSE (good?), ACK
        4. set is own gabai data : SET_GABAI, RESPONSE (good?),ACK
        
(guest):                                                                                    1               2                   3                   4
        1. send query (only name = data ,nosah = 4 bit(16),city = 8 bits(256))  :REQUEST_BY_QUERY :RESPONSE(list synag): REQUEST_BY_ID'S : RESPONSE (multi synagogue)
            |->    view specific synagogue (UI)
        

Gabai: (admin)
    name
    phone
    id
    pass
    id_list
    
Synagogue:
    Gabai?
    title
    nosah
    city
    id
    
'''


# TODO
# TODO cc
# TODO not response ,timeout
# TODO
# TODO
# TODO
# TODO fc

class Kind(enum.Enum):
    REQUEST_LOGIN = 0
    REQUEST_BY_QUERY = 1
    REQUEST_BY_IDS = 2
    REQUEST_ALL_GABAI = 3
    SET_SYNAGOGUE = 4
    SET_GABAI = 5
    RESPONSE = 6
    ACK_TO_RESPONSE = 7


class mHeader:
    HEADER_FORMAT: typing.Final[str] = '!HHHH'
    HEADER_MIN_LENGTH: typing.Final[int] = struct.calcsize(HEADER_FORMAT)
    # Big enough to hold the header and a lot of data
    HEADER_MAX_LENGTH: typing.Final[int] = 2 ** 16
    HEADER_MAX_DATA_LENGTH: typing.Final[int] = HEADER_MAX_LENGTH - \
                                                HEADER_MIN_LENGTH

    # 16 bits -> 2**16 possible values -> 0 to 2**16 - 1
    MAX_CACHE_CONTROL: typing.Final[int] = 2 ** 16 - 1

    # python3 protocol "length:16, kind:3, nosah:4, city :9, Window:16, padding:16 data:256"

    def __init__(self, length: typing.Optional[int], kind: int, nosah: int, city: int, window: int, padding: int,
                 data: bytes = b'') -> None:
        self.length = length
        if self.length is None:
            self.length = self.HEADER_MIN_LENGTH + len(data)
        if not (self.HEADER_MIN_LENGTH <= self.length <= self.HEADER_MAX_LENGTH):
            raise ValueError(
                f'Invalid total length: {self.length} (must be between {self.HEADER_MIN_LENGTH} and {self.HEADER_MAX_LENGTH} bytes inclusive)')
        elif self.length != self.HEADER_MIN_LENGTH + len(data):
            warnings.warn(f'The total length ({self.length}) does not match the length of the data ({len(data)})')
        self.kind = kind
        self.city = city
        self.nosah = nosah
        if self.kind != 1 and self.nosah != 0:
            warnings.warn(f'The nosah ({Nosah(self.nosah)}) is not 0 for a not query')
            self.nosah = 0
        self.checksum = 0
        self.window = window
        self.padding = padding

        self.data = data
        if len(self.data) > self.HEADER_MAX_DATA_LENGTH:
            raise ValueError(
                f'Invalid data length: {len(self.data)} (must be at most {self.HEADER_MAX_DATA_LENGTH} bytes)')

    def pack_flags(self, kind, nosah, city):
        return (kind << 13) | (nosah << 9) | city

    # , kind: 3, nosah: 4, city: 9
    @staticmethod
    def unpack_flags(flags: int):
        city = flags & ((1 << 9) - 1)  # flags & 0b000_0000_111111111
        nosah = (flags & (15 << 9)) >> 9  # flags & 0b000_1111_000000000
        kind = (flags & (7 << 13)) >> 13  # flags & 0b111_0000_000000000
        return kind, nosah, city

    def pack(self) -> bytes:
        return struct.pack(self.HEADER_FORMAT, self.length,
                           self.pack_flags(self.kind, self.nosah, self.city), self.window,
                           self.padding) + self.data

    @classmethod
    def unpack(cls, data: bytes) -> 'mHeader':
        if len(data) < cls.HEADER_MIN_LENGTH:
            raise ValueError(f'The data is too short ({len(data)} bytes) to be a valid header')
        length, flags, window, padding = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_MIN_LENGTH])
        kind, nosah, city = cls.unpack_flags(flags)
        return cls(length=length, kind=kind,
                   nosah=nosah, city=city, window=window, padding=padding, data=data[cls.HEADER_MIN_LENGTH:])

    def __str__(self):
        return f'{self.__class__.__name__}( total_length={self.length}, kind={Kind(self.kind)}, nosah={Nosah(self.nosah)}, City={City(self.city)}, window={self.window}, padding={self.padding}, data={self.data.decode()})'
