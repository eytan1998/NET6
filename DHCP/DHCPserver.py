from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff

s_mac = RandMAC()
src_ip = "10.0.0.0"
dst_ip = "255.255.255.250"
dns = "127.0.0.0"
serverP = 67
clientP = 68
IFACE = 'enp0s3'
IFACE2 = 'wlp0s20f3'
FILTER = "udp and dst port 67"


def type_packet(temp_packet):
    temp1 = temp_packet.getlayer(DHCP).fields['options'][0][1]
    if temp1 == 2:
        return "request"
    if temp1 == 2:
        return 'offer'
    return 'ack'


def nak_get():
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2) / \
              DHCP(options=[("type", "nak"), ",", "nak", ",", "null", ",", "null", ",", "end"])
    return package


def ack_get(ip_ack):
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2) / \
              DHCP(options=[("message-type", "ack"), ",", "ack", ",", ip_ack, ",", dns, ",", "end"])
    return package


def offer_get(ip_offer):
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2, siaddr=ip_offer) / \
              DHCP(options=[('message-type', 'offer'), 'end'])
    return package


def get_discover():
    while True:
        packet_discover = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_discover)) <= 0: continue
        if packet_discover[0].haslayer(UDP): break

    print("[+] server Receive discover")
    print((str(packet_discover[0][DHCP].options)))
    return


def send_offer(packet):
    offer_ip = "10.0.0.16"
    offer_packet = offer_get(offer_ip)
    sendp(offer_packet)
    print("[+] server Send offer")
    return


def get_request():
    while True:
        packet_request = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_request)) <= 0: continue
        if packet_request[0].haslayer(UDP): break

    print("[+] server Receive request")
    print((str(packet_request[0][DHCP].options)))
    return packet_request[0][DHCP].options


def send_ack(ip_requsted):
    ack_packet = ack_get(ip_requsted)
    sendp(ack_packet)
    print("[+] server send ack")
    return


if __name__ == '__main__':
    get_discover()
    print("[+]new ip")
    send_offer(packet)
    ip_requsted = get_request()
    send_ack(ip_requsted)
