import enum
import struct
import typing
import warnings

from Backend.Help.synagogue import Nosah, City

'''
 python3 protocol "Status_code:16, kind:3, nosah:4, city :9, data:256"
 
 * Status_code (16 bits = 2 bytes):
    The total length of the packet, in bytes (including the header and the data)
    This minimum value is 8 bytes (header only)

* Flags (16 bits):
    - kind (3 bit):
    REQUEST_LOGIN = 0
    REQUEST_BY_QUERY = 1
    REQUEST_SYNG_BY_ID = 2
    REQUEST_ALL_GABAI = 3
    REQUEST_GABAI_BY_ID = 4
    SET_SYNAGOGUE = 5
    SET_GABAI = 6
    RESPONSE = 7
        
    - nosah (4 bit): witch nosah the synagogue pray
        
    - city (9 bit): the city the synagogue is
        NULL =0  (not spec)
        JERUSALEM = 1
        ...
        

* Data (at most 65440 bits = 8180 bytes):
    The data of the packet
    It's at most 65440 bits because the total length is 16 bits, and the minimum value is 8 bytes (header only)
    2^16 - 12*8 = 65440
    contains:
        REQUEST_LOGIN = 0  -> id,password
        REQUEST_BY_QUERY = 1 -> str to search
        REQUEST_SYNG_BY_ID = 2  -> id
        REQUEST_ALL_GABAI = 3 -> None
        REQUEST_GABAI_BY_ID = 4 -> id
        SET_SYNAGOGUE = 5 -> Synagogue
        SET_GABAI = 6  -> Gabai
        RESPONSE = 7 -->| Synagogue
                        | Gabai
                        | ids

 0                   1                   2                   3  
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|          Status_code          | kind|  nosah|       city      |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                               data                            |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Status_code: 16 bits = 2 bytes -> H
kind + nosah + city: 3 bits + 4 bits + 9 bits = 2 byte -> H




every level has all the below

(guest):  
        0. -> login   id,pass  (saved gabai) : REQUEST_LOGIN
        <- gabai : RESPONSE  
                                                                                        1               2                        3                   4
        1. send query (only name = data ,nosah = 4 bit(16),city = 8 bits(256))  :REQUEST_BY_QUERY :RESPONSE(list syng): loops (REQUEST_BY_ID : RESPONSE)
       
(gabai):
        0. get all syng: loops (REQUEST_BY_ID : RESPONSE)
        1. add synagogue: send synagogue :SET_SYNAGOGUE , RESPONSE 
        2. edit : send synagogue : SET_SYNAGOGUE , RESPONSE 
        3. del: send synagogue (empty name) : SET_SYNAGOGUE , RESPONSE
        4. set is own gabai data : SET_GABAI, RESPONSE (good?),ACK
     
(admin):
       0. get all gabai REQUEST_ALL_GABAI, RESPONSE , REQUEST_GABAI_BY_ID, RESPONSE
       1. add _ gabai : SET_GABAI , RESPONSE 
       2. del gabai (empty name) : SET_GABAI, RESPONSE 
       2. edit gabai  : SET_GABAI, RESPONSE 
   
'''


class Kind(enum.Enum):
    REQUEST_LOGIN = 0
    REQUEST_BY_QUERY = 1
    REQUEST_SYNG_BY_ID = 2
    REQUEST_ALL_GABAI = 3
    REQUEST_GABAI_BY_ID = 4
    SET_SYNAGOGUE = 5
    SET_GABAI = 6
    RESPONSE = 7


class Status_code(enum.Enum):
    OK = 0
    CORRECT_LOGIN = 1
    WRONG_ID = 2
    WRONG_PASSWORD = 3
    NOT_FOUND = 4
    ERROR = 5


class AppHeader:
    HEADER_FORMAT: typing.Final[str] = '!HH'
    HEADER_MIN_LENGTH: typing.Final[int] = struct.calcsize(HEADER_FORMAT)
    # Big enough to hold the header and a lot of data
    HEADER_MAX_LENGTH: typing.Final[int] = 2 ** 16
    HEADER_MAX_DATA_LENGTH: typing.Final[int] = HEADER_MAX_LENGTH - HEADER_MIN_LENGTH

    def __init__(self, status_code: int, kind: int, nosah: int, city: int,
                 data: bytes = b'') -> None:
        self.status_code = status_code
        self.kind = kind
        self.city = city
        self.nosah = nosah
        if self.kind != 1 and self.nosah != 0:
            warnings.warn(f'The nosah ({Nosah(self.nosah)}) is not 0 for a not query')
            self.nosah = 0
        self.checksum = 0

        self.data = data
        if len(self.data) > self.HEADER_MAX_DATA_LENGTH:
            raise ValueError(
                f'Invalid data length: {len(self.data)} (must be at most {self.HEADER_MAX_DATA_LENGTH} bytes)')

    def get_data(self) -> bytes:
        return self.data

    @staticmethod
    def pack_flags(kind, nosah, city):
        return (kind << 13) | (nosah << 9) | city

    # , kind: 3, nosah: 4, city: 9
    @staticmethod
    def unpack_flags(flags: int):
        city = flags & ((1 << 9) - 1)  # flags & 0b000_0000_111111111
        nosah = (flags & (15 << 9)) >> 9  # flags & 0b000_1111_000000000
        kind = (flags & (7 << 13)) >> 13  # flags & 0b111_0000_000000000
        return kind, nosah, city

    def pack(self) -> bytes:
        return struct.pack(self.HEADER_FORMAT, self.status_code,
                           self.pack_flags(self.kind, self.nosah, self.city)) + self.data

    @classmethod
    def unpack(cls, data: bytes) -> 'AppHeader':
        if len(data) < cls.HEADER_MIN_LENGTH:
            print(f'The data is too short ({len(data)} bytes) to be a valid header')
        status_code, flags = struct.unpack(cls.HEADER_FORMAT, data[:cls.HEADER_MIN_LENGTH])
        kind, nosah, city = cls.unpack_flags(flags)
        return cls(status_code=status_code, kind=kind,
                   nosah=nosah, city=city, data=data[cls.HEADER_MIN_LENGTH:])

    def __str__(self):
        return f'{self.__class__.__name__}( status_code={Status_code(self.status_code)}, kind={Kind(self.kind)}' \
               f', nosah={Nosah(self.nosah)}, City={City(self.city)}, data={self.data.decode()})'
