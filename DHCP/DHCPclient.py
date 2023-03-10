from scapy.all import *
import time
import socket
import atexit
import socket
from scapy.sendrecv import sniff
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff, send, sr1

s_mac = RandMAC()
src_ip = "0.0.0.0"
dst_ip = "255.255.255.255"
serverP = 67
clientP = 68
IFACE = 'enp0s3'
IFACE2 = 'wlp0s20f3'
FILTER = 'udp and (port 68 or port 67)'
YIADDR = "10.0.0.17"
SIADDR = "10.0.0.16"
GIADDR = "0.0.0.0"
'''XID'''


def discover_get():
    discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=s_mac, type=0x0800) / IP(src='0.0.0.0', dst='255.255.255.255') / UDP(
        dport=67, sport=68) / BOOTP(op=1) / DHCP(options=[('message-type', 'discover'), 'end'])
    return discover


def request_get():
    request = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=clientP, dport=serverP) / \
              BOOTP(op=1, yiaddr=YIADDR, siaddr=SIADDR, giaddr=GIADDR) / \
              DHCP(options=[("message-type", "request"), ",", "request", ",", "oooooo", ",", "end"])
    return request


def send_discover():
    discover = discover_get()
    sendp(discover)
    print("[+] client Send discovery.")
    return

def get_offer():
    while True:
        packet_offer = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout = 1)
        if len(list(packet_offer)) <= 0: continue
        if packet_offer[0].haslayer(UDP):break

    print("[+] client Receive offer")
    print((str(packet_offer[0][DHCP].options)))
    return packet_offer[0][DHCP].options


def send_request(ip_offer):
    data = request_get()
    sendp(data)
    print("[+] client send request")
    return


def get_ack():
    while True:
        packet_ack = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_ack)) <= 0: continue
        if packet_ack[0].haslayer(UDP): break

    print("[+] client Receive " + str(list(packet_ack)))
    print((str(packet_ack[0][DHCP].options)))
    return packet_ack[0][DHCP].options


if __name__ == '__main__':
    send_discover()
    the_offer = get_offer()
    send_request(the_offer)
    ack_packet = get_ack()
