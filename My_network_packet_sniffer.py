from scapy.all import sniff, IP, TCP, UDP, Raw, conf

def process_packet(packet):
    if IP in packet:
        print(f"\n[+] {packet[IP].src} -> {packet[IP].dst} | Protocol: {packet[IP].proto}")
        if Raw in packet:
            print(f"    Payload: {packet[Raw].load[:50]}...")

print("Sniffing on Layer 3 (no Npcap required)...")
conf.use_pcap = False  # Force Layer 3 sniffing
sniff(prn=process_packet, filter="ip", store=False)
