import pickle
from enum import IntEnum
import json

import jsonpickle as jsonpickle

try:
    from gabai import Gabai
except:
    from UDP.gabai import Gabai


class Nosah(IntEnum):
    NULL = 0
    SPARAD = 1
    ASHCANZE = 2
    SPARADI = 3
    BALADY = 4
    SHAMI = 5
    ALL = 15

    @staticmethod
    def getAll():
        a = []
        for s in Nosah:
            a.append(s.name)
        return a


class City(IntEnum):
    NULL = 0
    ALL = 1
    JERULEAM = 2

    @staticmethod
    def getAll():
        a = []
        for s in City:
            a.append(s.name)
        return a


class Synagogue:
    def __init__(self, name, id_synagogue: int, nosah: Nosah, city: City, prayers, gabai: Gabai) -> None:
        self.name = name
        self.id_synagogue = id_synagogue
        self.nosah = nosah
        self.city = city
        self.prayers = prayers
        self.gabai = gabai

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=False)

    @staticmethod
    def fromJSON(str):
        json_data = json.loads(str)
        return Synagogue(json_data['name'], json_data['id_synagogue'], json_data['nosah'], json_data['city'],
                         json_data['prayers'], json_data['gabai'])

    def __str__(self):
        return self.toJSON()


class SynagogueList:
    def __init__(self):
        self.synagogues = list()

    def append(self, synagogue) -> Synagogue | None:
        if self.synagogues.__contains__(synagogue): return None
        self.synagogues.append(synagogue)
        return synagogue

    def get_by_name(self, name) -> Synagogue | None:
        for s in self.synagogues:
            if s.name == name: return s
        return None

    def get_by_name_and_nosah(self, name, nosah: Nosah) -> list | None:
        l = []
        empty = True
        for s in self.synagogues:
            if name in s.name and s.nosah.value == nosah:
                l.append(s.id_synagogue)
                empty =False
        if empty:
            return None
        return l

    def get_by_id(self, id_synagogue) -> Synagogue | None:
        for s in self.synagogues:
            if s.id_synagogue == id_synagogue: return s
        return None

    def set_by_id(self, other: Synagogue):
        for s in self.synagogues:
            if s.id_synagogue == other.id_synagogue:
                self.synagogues.remove(s)
                self.synagogues.append(other)
                return 0
        return -1

    def write_json(self) -> None:
        jsonpickle.set_encoder_options('json', sort_keys=False, indent=4)
        frozen = jsonpickle.encode(self.synagogues)
        with open("data.json", "w") as text_file:
            print(frozen, file=text_file)

    def read_json(self) -> None:
        file = open("data.json", "r")
        self.synagogues = jsonpickle.decode(file.read())

    def __str__(self):
        a = ""
        for s in self.synagogues:
            a += str(s)
        return a
