import argparse
import atexit

from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.sendrecv import sniff, send

from records import record_list

IFACE = "lo"  # Or your default interface
DNS_SERVER_IP = "127.0.0.1"  # Your local IP



def exit_handler():
    records_list.write_json()
    print("\n[!] Server shutting down, saving data to json...")


def querysniff(pkt):
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0 and pkt.getlayer(DNS).qd is not None:
            print(str(ip_src) + " -> " + str(ip_dst) + " : (" + str(pkt.getlayer(DNS).qd.qname) + " )")
            new_pkt = records_list.get_answer(pkt)
            send(new_pkt, verbose=0)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        description='DNS Server.')

    arg_parser.add_argument('-i', '--iface', type=str,
                            default=IFACE, help='The interface to sniff on.')
    arg_parser.add_argument('-H', '--host', type=str,
                            default=DNS_SERVER_IP, help='The host to listen on.')
    args = arg_parser.parse_args()
    IFACE = args.iface
    DNS_SERVER_IP = args.host

    records_list = record_list(5)
    records_list.read_json()
    atexit.register(exit_handler)
    print("[+] DNS server is running...")
    print("[+] sniff on \"" + IFACE + "\", Ip: " + DNS_SERVER_IP+".")
    BPF_FILTER = f"udp dst port 53 and ip dst {DNS_SERVER_IP}"
    sniff(filter=BPF_FILTER, prn=querysniff, iface=IFACE)
