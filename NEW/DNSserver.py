import atexit

from scapy.layers.dns import DNS
from scapy.layers.inet import IP
from scapy.sendrecv import sniff, send

from records import record_list

IFACE = "lo"  # Or your default interface
DNS_SERVER_IP = "127.0.0.1"  # Your local IP
BPF_FILTER = f"udp dst port 53 and ip dst {DNS_SERVER_IP}"


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
    records_list = record_list(5)
    records_list.read_json()
    atexit.register(exit_handler)
    sniff(filter=BPF_FILTER, prn=querysniff, iface=IFACE)
