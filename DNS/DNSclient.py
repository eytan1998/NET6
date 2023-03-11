from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sr1


def sendDNS(dns_server, domain):
    ans = sr1(IP(dst=dns_server) / UDP(sport=7654, dport=53) / DNS(rd=1, qd=DNSQR(qname=domain, qtype="A")), timeout=2)
    if ans is not None and ans.haslayer(DNS):
        if ans.getlayer(DNSRR):
            try:
                # print(ans.getlayer(DNS).an.rdata.decode())
                return ans.getlayer(DNS).an.rdata.decode()
            except:
                # print(ans.getlayer(DNS).an.rdata)
                return ans.getlayer(DNS).an.rdata
    else:
        # print("[-] no answer")
        return None
