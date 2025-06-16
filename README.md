# PRODIGY_CS_04
# 🧠 My Network Packet Sniffer

A simple Python-based network packet sniffer built using the Scapy library. This script captures live IP traffic on the network, showing key packet information such as source/destination IP addresses, protocol used, and a snippet of payload data.

## 🚀 Features

- Captures IP packets in real-time
- Displays source and destination IP addresses
- Shows protocol type (TCP/UDP/Other)
- Extracts and prints the first 50 bytes of payload if available
- Operates at Layer 3 (No Npcap needed on Windows)

## 🛠️ How It Works

1. The script uses Scapy's `sniff()` function to capture packets.
2. It processes each packet with `process_packet()`.
3. If an IP layer is found:
   - It prints the source and destination IP addresses.
   - It identifies the protocol used.
   - If raw data (payload) is available, it prints the first 50 bytes.

## 🧪 Requirements

- Python 3.x
- [Scapy](https://scapy.readthedocs.io/en/latest/)

You can install Scapy via pip:

<pre>bash
pip install scapy</pre>

## 🖥️ How to Run
<pre>bash
python My_network_packet_sniffer.py</pre>

Ensure that you run the script with appropriate privileges (e.g., Administrator on Windows or sudo on Linux/macOS) to allow packet sniffing.

## 🔒 Disclaimer
This tool is intended for educational and ethical use only. Unauthorized packet sniffing on networks without permission is illegal and unethical.

## 👨‍💻 Author
### Manik Chand Singh
Cybersecurity enthusiast | Python beginner | Ethical hacker-in-training
