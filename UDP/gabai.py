import json


class Gabai:
    def __init__(self, name, gabai_id: int, password, phone, synagogue_list) -> None:
        self.name = name
        self.gabai_id = gabai_id
        self.password = password
        self.phone = phone
        self.synagogue_list = synagogue_list

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    @staticmethod
    def fromJSON(str):
        json_data = json.loads(str)
        return Gabai(json_data['name'], json_data['gabai_id'], json_data['password'], json_data['phone'],
                     json_data['synagogue_list'])

    def __str__(self):
        return "{name: " + self.name + \
            ", gabai_id: " + str(self.gabai_id) + \
            ", password: " + str(self.password) + \
            ", phone: " + (self.phone) + \
            ", synagogue_list: " + str(self.synagogue_list) + " }"


class GabaiList:
    def __init__(self):
        self.gabai_list = list()
