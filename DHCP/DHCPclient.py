import json
import os
import time

from scapy.all import *
from scapy.layers.dhcp import BOOTP, DHCP
from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff

s_mac = RandMAC()
src_ip = "0.0.0.0"
dst_ip = "255.255.255.254"
serverP = 67
clientP = 68
IFACE = 'enp0s3'
IFACE2 = 'wlp0s20f3'
FILTER = 'udp and (port 68 or port 67) and host 255.255.255.254'


def type_packet(temp_packet):
    temp1 = str((temp_packet)).split(",")
    print(temp1)
    return


def discover_get():
    discover = Ether(dst='ff:ff:ff:ff:ff:ff', src=s_mac) / IP(src=src_ip, dst=dst_ip) / UDP(
        dport=serverP, sport=clientP) / BOOTP(op=1) / DHCP(options=[('message-type', 'discover'), 'end'])
    return discover


def request_get(ip_temp=src_ip):
    request = Ether(dst="ff:ff:ff:ff:ff:ff", src=s_mac) / \
              IP(src=ip_temp, dst=dst_ip) / \
              UDP(sport=clientP, dport=serverP) / \
              BOOTP(op=1) / \
              DHCP(options=[("message-type", "request"), ("end")])
    return request


def send_discover():
    discover = discover_get()
    sendp(discover)
    print("[+] client Send discovery.")
    return


def get_offer():
    while True:
        packet_offer = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_offer)) <= 0: continue
        if packet_offer[0].haslayer(UDP): break

    print("[+] client Receive offer")
    return packet_offer[0][DHCP].options


def send_request(t_ip):
    if t_ip != 0:
        data = request_get(t_ip)
    else:
        data = request_get()
    sendp(data)
    print("[+] client send request")
    return


def get_ack():
    while True:
        packet_ack = sniff(filter=FILTER, iface=IFACE2, count=0, store=1, timeout=1)
        if len(list(packet_ack)) <= 0: continue
        if packet_ack[0].haslayer(UDP): break
    if packet_ack[0][DHCP].options[0][1] == 5:
        t = "ack"
    else:
        t = "nak"
    print("[+] client Receive " + t)
    return packet_ack


def get_DNS():
    filename = 'DHCP/dhcpclient.json'
    with open(filename, 'r') as f:
        data = json.load(f)
    find = True
    my_ip = data['ip']
    temp_lease = data['lease_time']
    while find:
        if (not my_ip.__eq__("0.0.0.0")) and temp_lease > time.time():
            send_request(my_ip)
            ack_packet = get_ack()
        else:
            send_discover()
            the_offer = get_offer()
            send_request(0)
            ack_packet = get_ack()
        lease_time = ack_packet[0][DHCP].options[1][1] + time.time()
        temp_list = (str(ack_packet[0][DHCP].options)).split(",")
        if ack_packet[0][DHCP].options[0][1] == 5:
            find = False
            ip_client = temp_list[5]
            dns_temp = temp_list[6]
            data['ip'] = ip_client
            data['lease_time'] = lease_time
            data['dns'] = dns_temp
        my_ip = "0.0.0.0"
    os.remove(filename)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    return ip_client, dns_temp
