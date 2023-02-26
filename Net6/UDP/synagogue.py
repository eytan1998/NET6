from enum import IntEnum
import json


class Nosah(IntEnum):
    NULL = 0
    SPARAD = 1
    ASHCANZE = 2
    SPARADI = 3
    BALADY = 4
    SHAMI = 5
    ALL = 15


class Synagogue:
    def __init__(self, title, nosah: Nosah, id: int, prayers) -> None:
        self.title = title
        self.nosah = nosah
        self.id = id
        self.prayers = prayers

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def fromJSON(str):
        json_data = json.loads(str)
        return Synagogue(json_data['title'], json_data['nosah'], json_data['id'], json_data['prayers'])


    def __str__(self):
        return "{title: " + self.title + ", nosah: " + str(self.nosah) + ", id: " + str(self.id) + ", prayers: " + (
            self.prayers) + "}"


class SynagogueList:
    def __init__(self):
        self.synagogues = list()

    def append(self, synagogue) -> Synagogue | None:
        if self.synagogues.__contains__(synagogue): return None
        self.synagogues.append(synagogue)
        return synagogue

    def get_by_name(self, name) -> Synagogue | None:
        for s in self.synagogues:
            if s.title == name: return s
        return None

    def get_by_name_and_nosah(self, name, nosah: Nosah) -> list | None:
        l = []
        for s in self.synagogues:
            if s.title == name and s.nosah == nosah:
                l.append(s.id)
        if len(list) == 0: return None
        return l

    def get_by_id(self, id) -> Synagogue | None:
        for s in self.synagogues:
            if s.id == id: return s
        return None

    def set_by_id(self, other: Synagogue):
        for s in self.synagogues:
            if s.id == other.id:
                self.synagogues.remove(s)
                self.synagogues.append(other)
                return 0
        return -1

    def write_json(self) -> None:
        json_string = json.dumps([ob.__dict__ for ob in self.synagogues])
        with open("data.json", "w") as file:
            file.write(json_string)

    def read_json(self) -> None:
        ans = list()
        with open('data.json') as json_file:
            json_data = json.load(json_file)

        for item in json_data:
            ans.append(Synagogue(item['title'], item['nosah'], item['id'], item['prayers']))
        self.synagogues = ans

    def __str__(self):
        a = ""
        for s in self.synagogues:
            a += str(s)
        return a
