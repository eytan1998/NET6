import json
from enum import IntEnum

import jsonpickle as jsonpickle

from Backend.Help.gabai import Gabai


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
    Afula = 1
    Akko = 2
    Arad = 3
    Ariel = 4
    Ashdod = 5
    Ashkelon = 6
    Baqa = 7
    Bat_Yam = 9
    Beer_Sheva = 11
    Beit_Shean = 13
    Beit_Shemesh = 15
    Betar = 16
    Illit = 17
    Bnei = 18
    Berak = 19
    Dimona = 20
    Eilat = 21
    Givatayim = 22
    Hadera = 23
    Haifa = 24
    Harish = 25
    Herzliya = 26
    Hod_HaSharon = 28
    Holon = 29
    Jerusalem = 30
    Karmiel = 31
    Kfar_Sava = 33
    Kiryat_Ata = 35
    Kiryat_Bialik = 37
    Kiryat_Gat = 39
    Kiryat_Malachi = 41
    Kiryat_Motzkin = 43
    Kiryat_Ono = 45
    Kiryat_Shemone = 47
    Kiryat_Yam = 49
    Lod = 50
    Maale = 51
    Adumim = 52
    Maalot_Tarshiha = 54
    Migdal = 55
    HaEmek = 56
    Modiin = 57
    Nahariya = 58
    Nazareth = 59
    Nes_Ziona = 61
    Nesher = 62
    Netanya = 63
    Netivot = 64
    Nof_Hagalil = 66
    Ofakim = 67
    Or_Akiva = 69
    Or_Yehuda = 71
    Petah = 72
    Tikva = 73
    Qalansawe = 74
    Raanana = 75
    Rahat = 76
    Ramat_Hasharon = 78
    Ramat_Gan = 79
    Ramla = 80
    Rehovot = 81
    Rishon_Lezion = 83
    Rosh_Haayin = 85
    Sakhnin = 86
    Sderot = 87
    Shefaram = 88
    Taibeh = 89
    Tamra = 90
    Tel_Aviv = 91
    Tiberias = 92
    Tira = 93
    Tirat_Carmel = 95
    Tsfat = 96
    Umm_al_Fahm = 97
    Yavne = 98
    Yehud_Monosson = 99
    Yokneam = 100

    @staticmethod
    def getAll():
        a = []
        for s in City:
            a.append(s.name)
        return a


class Synagogue:
    def __init__(self, name: str = "", id_synagogue: int = 0, nosah: Nosah = Nosah.NULL, city: City = City.NULL,
                 prayers: str = "",
                 gabai: Gabai = None) -> None:
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
    def fromJSON(syng_as_json):
        json_data = json.loads(syng_as_json)
        try:
            ans = Synagogue(json_data['name'], json_data['id_synagogue'], Nosah(json_data['nosah']),
                            City(json_data['city']),
                            json_data['prayers'],
                            Gabai(json_data['gabai']['name'], json_data['gabai']['gabai_id'],
                                  json_data['gabai']['password'],
                                  json_data['gabai']['phone'], json_data['gabai']['synagogue_list']))
        except:
            ans = Synagogue(json_data['name'], json_data['id_synagogue'], json_data['nosah'],
                            json_data['city'],
                            json_data['prayers'],
                            json_data['gabai'])
        return ans

    def __str__(self):
        return self.toJSON()


class SynagogueList:
    def __init__(self):
        self.synagogues = list()
        self.nextid = 10

    def append(self, synagogue) -> Synagogue | None:
        if self.synagogues.__contains__(synagogue): return None
        self.synagogues.append(synagogue)
        return synagogue

    def get_by_name(self, name) -> Synagogue | None:
        for s in self.synagogues:
            if s.name == name: return s
        return None

    def get_by_name_and_nosah_and_city(self, name, nosah: int, city: int) -> list | None:
        l = []
        empty = True
        for s in self.synagogues:
            if name in s.name:
                if s.nosah.value == nosah or nosah == 0:
                    if s.city.value == city or city == 0:
                        l.append(s.id_synagogue)
                        empty = False
        if empty:
            return None
        return l

    def get_by_id(self, id_synagogue) -> Synagogue | None:
        for s in self.synagogues:
            if s.id_synagogue == id_synagogue: return s
        return None

    def edit(self, o, gabai):
        try:
            self.synagogues.remove(self.get_by_id(o.id_synagogue))
        except:
            pass
        # dor del
        if o.name == "":
            gabai.synagogue_list.remove(o.id_synagogue)
            return 0
        # for add
        ans = o.id_synagogue
        if o.id_synagogue == 0:
            o.id_synagogue = self.nextid
            ans = self.nextid
            gabai.synagogue_list.append(self.nextid)
            self.nextid += 1
        # edit|add
        self.synagogues.append(o)
        return ans

    def set_by_id(self, other: Synagogue):
        for s in self.synagogues:
            if s.id_synagogue == other.id_synagogue:
                self.synagogues.remove(s)
                self.synagogues.append(other)
                return 0
        return -1

    def remove_from_gabai(self, id_gabai: int):
        for syng in self.synagogues:
            if syng.gabai.gabai_id == id_gabai:
                self.synagogues.remove(syng)

    def edit_from_gabai(self, gabai: Gabai):
        for syng in self.synagogues:
            if syng.gabai.gabai_id == gabai.gabai_id:
                syng.gabai = gabai

    def write_json(self) -> None:
        jsonpickle.set_encoder_options('json', sort_keys=False, indent=4)
        frozen = jsonpickle.encode(self.synagogues)
        with open("Backend/Data/data_syng.json", "w") as text_file:
            print(frozen, file=text_file)
        with open("Backend/Data/index_syng.txt", "w") as text_file:
            print(str(self.nextid), file=text_file)

    def read_json(self) -> None:

        file = open("Backend/Data/data_syng.json", "r")
        self.synagogues = jsonpickle.decode(file.read())
        file = open("Backend/Data/index_syng.txt", "r")
        self.nextid = int(file.readline())

    def __str__(self):
        a = ""
        for s in self.synagogues:
            a += str(s)
        return a
