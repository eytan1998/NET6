import json

import jsonpickle


class Gabai:
    def __init__(self, name:str, gabai_id: int, password:str, phone:str, synagogue_list) -> None:
        self.name = name
        self.gabai_id = gabai_id
        self.password = password
        self.phone = phone
        self.synagogue_list = synagogue_list

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def fromJSON(gabai_as_json):
        json_data = json.loads(gabai_as_json)
        return Gabai(json_data['name'], json_data['gabai_id'], json_data['password'], json_data['phone'],
                     json_data['synagogue_list'])

    def __str__(self):
        return self.toJSON()


class GabaiList:
    def __init__(self):
        self.gabai_list = list()
        self.nextid = 10

    def append(self, o) -> Gabai | None:
        if self.gabai_list.__contains__(o): return None
        self.gabai_list.append(o)
        return o

    def get_by_id(self, id_to_check) -> Gabai | None:
        ans = None
        for x in self.gabai_list:
            if x.gabai_id == id_to_check:
                return x
        return ans

    def delete(self, o) -> None:
        self.gabai_list.remove(o)

    def edit(self, o: Gabai, list_of_sysngogue):
        try:
            self.gabai_list.remove(self.get_by_id(o.gabai_id))
        except:
            pass
        # for del
        if o.name == "":
            list_of_sysngogue.remove_from_gabai(o.gabai_id)
            return 0
        # for add
        ans = o.gabai_id
        if o.gabai_id == 0:
            o.gabai_id = self.nextid
            self.nextid += 1
        # for edit
        else:
            list_of_sysngogue.edit_from_gabai(o)
        # edit|add
        self.gabai_list.append(o)
        return ans

    def write_json(self) -> None:
        jsonpickle.set_encoder_options('json', sort_keys=False, indent=4)
        frozen = jsonpickle.encode(self.gabai_list)
        with open('Backend/Data/data_gabai.json', "w") as text_file:
            print(frozen, file=text_file)
        with open("Backend/Data/index_gabai.txt", "w") as text_file:
            print(str(self.nextid), file=text_file)

    def read_json(self) -> None:
        file = open('Backend/Data/data_gabai.json', "r")
        self.gabai_list = jsonpickle.decode(file.read())
        file = open("Backend/Data/index_gabai.txt", "r")
        self.nextid = int(file.readline())

    def __str__(self):
        a = ""
        for s in self.gabai_list:
            a += str(s)
        return a
