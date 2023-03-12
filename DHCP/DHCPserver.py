import argparse

from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff
import json
import os

s_mac = RandMAC()
src_ip = "0.0.0.0"
dst_ip = "255.255.255.254"
dns = "127.0.0.1"
serverP = 67
clientP = 68
IFACE = 'enp0s3'
IFACE2 = 'wlp0s20f3'
FILTER = "udp and (port 68 or port 67) and host 255.255.255.254"


def get_ip():
    # if dynamic ip
    filename = 'DHCP/dhcpserver.json'
    with open(filename, 'r') as f:
        data = json.load(f)
        data['ip4'] = (data['ip4'] + 1) % 255
        give_ip = str(data['ip1']) + "." + str(data['ip2']) + "." + str(data['ip3']) + "." + str(data['ip4'])
    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    return give_ip


def nak_get():
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2) / \
              DHCP(options=[("type", "nak"), "end"])
    return package


def ack_get(ip_ack):
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2) / \
              DHCP(options=[("message-type", "ack"), ('lease_time', 259200), ",", ip_ack, ",", dns, ",", "end"])
    return package


def offer_get(ip_offer):
    package = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=src_ip, dst=dst_ip) / \
              UDP(sport=serverP, dport=clientP) / \
              BOOTP(op=2, siaddr=ip_offer) / \
              DHCP(options=[('message-type', 'offer'), ip_offer, ('end')])
    return package


def get_discover():
    while True:
        packet_discover = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_discover)) <= 0: continue
        if packet_discover[0].haslayer(UDP): break
    print("[+] server Receive discover")
    return packet_discover


def send_offer(packet, offer_ip):
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
    return packet_request


def send_ack(requsted, ip_):
    if requsted[0][DHCP].options[0][1] == 3:
        ack_packet = ack_get(ip_)
        t = "ack"
    else:
        ack_packet = nak_get()
        t = "nak"
    sendp(ack_packet)
    print("[+] server send  " + t)
    return ack_packet[0][DHCP].options[0][1] == 5


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='DHCP Server.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default=dns, help='The dns server.')
    args = arg_parser.parse_args()
    dns = args.host
    print("[+] DHCP server is running")
    while True:
        packet = get_discover()
        if packet[0][DHCP].options[0][1] == 3:
            print("[+] Renewal ip")
            find = send_ack(packet, packet[0][IP].src)
        else:
            print("[+] new ip")
            temp_ip = get_ip()
            send_offer(packet, temp_ip)
            packet_requsted = get_request()
            find = send_ack(packet_requsted, temp_ip)
