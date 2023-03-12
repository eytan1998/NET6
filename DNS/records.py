import enum
import json
import socket
from re import A
from sre_constants import IN
from time import time

from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1, srp1, send
from scapy.volatile import RandShort

DNS_SERVER_IP = "127.0.0.1"  # Your local IP

'''
QR (query/response): It is a 1-bit subfield. If its value is 0, the message is of request type and if its value is 1, the message is of response type.
opcode: It is a 4-bit subfield that defines the type of query carried by a message. This field value is repeated in the response. Following is the list of opcode values with a brief description:
    If the value of the opcode subfield is 0 then it is a standard query. 
    The value 1 corresponds to an inverse of query that implies finding the domain name from the IP Address. 
    The value 2 refers to the server status request. The value 3 specifies the status reserved and therefore not used.
AA: It is an Authoritative Answer. It is a 1-bit subfield that specifies the server is authoritative if the value is 1 otherwise it is non-authoritative for a 0 value.
TC: It is Truncation. This is a 1-bit subfield that specifies if the length of the message exceeds the allowed length of 512 bytes, the message is truncated when using RUDP services.
RD: It is Recursion Desired. It is a 1-bit subfield that specifies if the value is set to 1 in the query message then the server needs to answer the query recursively. Its value is copied to the response message.
RA: It is Recursion Available. It is a 1-bit subfield that specifies the availability of recursive response if the value is set to 1 in the response message.
Zero: It is a 3-bit reserved subfield set to 0.
rCode: It stands for Response Code. It is a 4-bit subfield used to denote whether the query was answered successfully or not. If not answered successfully then the status of error is provided in the response.  Following is the list of values with their error status –
    The value 0 of rcode indicates no error. 
    A value of 1 indicates that there is a problem with the format specification.
    Value 2 indicates server failure.
    Value 3 refers to the Name Error that implies the name given by the query does not exist in the domain. 
    Value of 4 indicates that the request type is not supported by the server.
    The value 5 refers to the nonexecution of queries by the server due to policy reasons.
Number of Questions- It is a 16-bit field to specify the count of questions in the Question Section of the message. It is present in both query and response messages.
A number of answer RRs- It is a 16-bit field that specifies the count of answer records in the Answer section of the message. This section has a value of 0 in query messages. The server answers the query received from the client. It is available only in response messages.
A number of authority RRs- It is a 16-bit field that gives the count of the resource records in the Authoritative section of the message. This section has a value of 0 in query messages. It is available only in response messages. It gives information that comprises domain names about one or more authoritative servers.
A number of additional RRs– It is a 16-bit field that holds additional records to keep additional information to help the resolver. This section has a value of 0 in query messages. It is available only in response messages
'''


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
    FROM_AUTH = 2
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
        self.to_late = time_to_save_in_minuts * 60 # to secounds

    def get_answer(self, packet):
        domain = packet.getlayer(DNS).qd.qname.decode()

        temp = self.is_contains(domain)
        # if got up-to-date record
        # return
        if temp[0] == contains.UP_TO_DATE:
            # know time() + to_late >= tll
            print('[!] Retrieved from table.\nTime until expire is: ' +
                  str((self.to_late - (time() - temp[1].ttl)) / 60) + " minutes for " + (domain) + " domain")
            return self.cnstractDNSRR(packet, domain, temp)
        # not up to date in record ask google
        else:
            #ask google
            response = sr1(
                IP(dst="8.8.8.8") / UDP(sport=RandShort(), dport=53) / DNS(rd=1, qd=DNSQR(qname=domain, qtype="A")))
            # if didnt get answer
            if response is None or response.getlayer(DNS).an is None:
                # return expire record
                if temp[0] == contains.EXPAIRE:
                    print('[-] Sending expire record of ' + domain)
                    return self.cnstractDNSRR(packet, domain, temp)
                # return that got no answer
                else:
                    print('[-] Cant get ip of ' + domain + " domain")
                    response.getlayer(IP).src = DNS_SERVER_IP
                    response.getlayer(IP).dst = packet[IP].src
                    response.getlayer(UDP).sport = 53
                    response.getlayer(UDP).dport = packet[UDP].sport
                    return response
            # got answer from google
            else:
                rdata = response.getlayer(DNS).an.rdata
                print("[+] Got answer " + str(rdata) + " and save it")
                self.append(record(domain, rdata, time()))
                newans = response.getlayer(DNS).an
                newans.rdata = rdata
                resp_pkt = IP(dst=packet[IP].src, src=DNS_SERVER_IP) / UDP(dport=packet[UDP].sport) / DNS(an=newans)
                resp_pkt[DNS] = response[DNS]
                return resp_pkt

    def append(self, record):
        if not is_valid_ipv4_address(str(record.address)): return
        ans = self.is_contains(record.domain)
        if ans[0] == contains.EXPAIRE or ans[0] == contains.UP_TO_DATE: self.records.remove(ans[1])
        self.records.append(record)

    def is_contains(self, domain):
        for r in self.records:
            if r.domain == domain:
                if (r.ttl + self.to_late) >= time():
                    return contains.UP_TO_DATE, r
                return contains.EXPAIRE, r
        return contains.NOT_FOUND, None

    def write_json(self):
        json_string = json.dumps([ob.__dict__ for ob in self.records], indent=4)
        with open("DNS/records.json", "w") as file:
            file.write(json_string)

    def read_json(self):
        ans = list()
        with open("DNS/records.json") as json_file:
            json_data = json.load(json_file)

        for item in json_data:
            ans.append(record(item['domain'], item['address'], item['ttl']))
        self.records = ans

    #for constract DNS packet
    def cnstractDNSRR(self, packet, domain, iscontains):
        if iscontains[0] == contains.UP_TO_DATE:
            return IP(src=DNS_SERVER_IP, dst=packet[IP].src) / UDP(dport=7654, sport=53) / DNS(qr=1, opcode=0, aa=0,
                                                                                               z=0, ad=0, cd=0, rcode=6,
                                                                                               ancount=1, nscount=0,
                                                                                               arcount=0,
                                                                                               qd=DNSQR(qname=domain,
                                                                                                        qtype=A,
                                                                                                        qclass=IN),
                                                                                               an=DNSRR(rrname=domain,
                                                                                                        type=A,
                                                                                                        rclass=IN,
                                                                                                        ttl=int((
                                                                                                                        self.to_late - (
                                                                                                                        time() -
                                                                                                                        iscontains[
                                                                                                                            1].ttl))),
                                                                                                        rdlen=None,
                                                                                                        rdata=
                                                                                                        (iscontains[
                                                                                                            1].address)),
                                                                                               ns=None, ar=None)
        elif iscontains[0] == contains.EXPAIRE:
            return IP(src=DNS_SERVER_IP, dst=packet[IP].src) / UDP(dport=7654, sport=53) / DNS(qr=1, opcode=0, aa=0,
                                                                                               z=0, ad=0, cd=0, rcode=0,
                                                                                               ancount=1, nscount=0,
                                                                                               arcount=0,
                                                                                               qd=DNSQR(qname=domain,
                                                                                                        qtype=A,
                                                                                                        qclass=IN),
                                                                                               an=DNSRR(rrname=domain,
                                                                                                        type=A,
                                                                                                        rclass=IN,
                                                                                                        ttl=0,
                                                                                                        rdlen=None,
                                                                                                        rdata=
                                                                                                        iscontains[
                                                                                                            1].address),
                                                                                               ns=None, ar=None)


    def __str__(self):
        a = ""
        for s in self.records:
            a += str(s)
        return a
