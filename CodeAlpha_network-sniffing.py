# Packet Sniffer Program(Passsive Sniffing)
# Using Scapy library to capture live network packets
 
from scapy.all import sniff, IP, TCP, UDP, ICMP 
from datetime import datetime
 
packet_count = 0
MAX_PACKETS = 40
 
# this function runs every time a packet is captured
def process_packet(packet):
    global packet_count
    packet_count += 1
 
    print(f"\n{'=' * 60}")
    print(f"Packet #{packet_count}  |  Time: {datetime.now().strftime('%H:%M:%S')}")
    print(f"{'=' * 60}")
 
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
 
        print(f"Source IP       : {src_ip}")
        print(f"Destination IP  : {dst_ip}")
 
        # checking which protocol the packet is using
        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            print("Protocol        : TCP")
            print(f"Source Port     : {sport}")
            print(f"Destination Port: {dport}")
 
        elif packet.haslayer(UDP):
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            print("Protocol        : UDP")
            print(f"Source Port     : {sport}")
            print(f"Destination Port: {dport}")
 
        elif packet.haslayer(ICMP):
            print("Protocol        : ICMP")
 
        else:
            print(f"Protocol        : OTHER ({ip_layer.proto})")
 
    else:
        # arp packets dont have IP layer
        print("Non-IP packet (probably ARP)")
        print(packet.summary())
 
    print(f"Packet Size     : {len(packet)} bytes")
 
 
# this tells scapy when to stop sniffing
def stop_filter(packet):
    return packet_count >= MAX_PACKETS
 
 
print("Starting Packet Sniffer...")
print(f"Capturing {MAX_PACKETS} packets")
print("Press CTRL+C to stop\n")
 
sniff(prn=process_packet, stop_filter=stop_filter, store=False)
 
print(f"\nDone. Total packets captured: {packet_count}")
 
