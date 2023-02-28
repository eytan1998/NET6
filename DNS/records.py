import enum
import json
import socket
import time


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


def get_Host_name_IP(domain):
    try:
        host_ip = socket.gethostbyname(domain)
        return host_ip
    except:
        return None


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
    def __init__(self, time_to_save_in_minuts):
        self.records = list()
        self.to_late = time_to_save_in_minuts * 60 * 1000

    def get_answer(self, message):
        message = message.decode()
        print("[+] Got domain :"+message+" ")
        temp = self.is_contains(message)
        # if got up to date record
        if temp[0] == contains.UP_TO_DATE:
            print('[!] Retrieved from table.\nTime until expire is: ' + str(
                (self.to_late - (time.time() - temp[1].ttl)) / 1000 / 60) + " minutes for " + message + " domain")
            return temp[1].address

        # else get answer
        ans = get_Host_name_IP(message)
        # if cant get answer
        if ans is None:
            # if had expaire record send it
            if temp[1] == contains.EXPAIRE:
                print('[-] Sending expire record of ' + message)
                return temp[1].address

            # if not record and cant get answer return the cant get answer
            else:
                print('[-] Cant get ip of ' + message + " domain")

                return 'Cant get ip of ' + message + " domain"
        # got an answer return and save it
        else:
            print("[+] Got answer "+ans+" and save it")
            self.append(record(message, ans, time.time()))
            return ans

    def append(self, record):
        if not is_valid_ipv4_address(record.address): return
        ans = self.is_contains(record.domain)
        if ans[0] == contains.EXPAIRE or ans[0] == contains.UP_TO_DATE: self.records.remove(ans[1])
        self.records.append(record)

    def is_contains(self, domain):
        for r in self.records:
            if r.domain == domain:
                if r.ttl + self.to_late >= time.time():
                    return contains.UP_TO_DATE, r
                return contains.EXPAIRE, r
        return contains.NOT_FOUND, None

    def write_json(self):
        json_string = json.dumps([ob.__dict__ for ob in self.records], indent=4)
        with open("/home/eitan/PycharmProjects/Net6/DNS/records.json", "w") as file:
            file.write(json_string)

    def read_json(self):
        ans = list()
        with open('/home/eitan/PycharmProjects/Net6/DNS/records.json') as json_file:
            json_data = json.load(json_file)

        for item in json_data:
            ans.append(record(item['domain'], item['address'], item['ttl']))
        self.records = ans

    def __str__(self):
        a = ""
        for s in self.records:
            a += str(s)
        return a
