import json
import time
import enum
import socket

class contains(enum.Enum):
    UP_TO_DATE = 1
    EXPAIRE = 0
    NOT_FOUND = -1


class record:
    def __init__(self, domain, address, ttl):
        self.domain = domain
        self.address = address
        self.ttl = ttl

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def __str__(self):
        return "{domain: " + self.domain + ", address: " + self.address + ", ttl: " + str(self.ttl) + " }"


class record_list:
    def __init__(self):
        self.records = list()
        self.to_late = 1500000

    @staticmethod
    def is_valid_ipv4_address(address):
        try:
            socket.inet_pton(socket.AF_INET, address)
        except AttributeError:  # no inet_pton here, sorry
            try:
                socket.inet_aton(address)
            except socket.error:
                return False
            return address.count('.') == 3
        except socket.error:  # not a valid address
            return False
        return True

    def append(self, record):
        if not self.is_valid_ipv4_address(record.address): return
        ans = self.is_contains(record.domain)
        if ans[0] == contains.EXPAIRE or ans[0] == contains.UP_TO_DATE: self.records.remove(ans[1])
        self.records.append(record)

    def is_contains(self, domain):
        for r in self.records:
            if r.domain == domain:
                if r.ttl + self.to_late >= time.time() * 1000:
                    return contains.UP_TO_DATE, r
                return contains.EXPAIRE, r
        return contains.NOT_FOUND, None

    def write_json(self):
        json_string = json.dumps([ob.__dict__ for ob in self.records])
        with open("records.json", "w") as file:
            file.write(json_string)

    def read_json(self):
        ans = list()
        with open('records.json') as json_file:
            json_data = json.load(json_file)

        for item in json_data:
            #  print(record(item['domain'], item['address'], item['ttl']))
            ans.append(record(item['domain'], item['address'], item['ttl']))
        self.records = ans

    def __str__(self):
        a = ""
        for s in self.records:
            a += str(s)
        return a

