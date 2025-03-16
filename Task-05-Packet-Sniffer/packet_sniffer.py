#!/usr/bin/env python3
from scapy.all import *
import argparse
from datetime import datetime

# Ethical safeguards
def check_privileges():
    try:
        if os.getuid() != 0:
            print("ERROR: Requires root/admin privileges")
            exit(1)
    except AttributeError:
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print("ERROR: Requires administrator privileges")
            exit(1)

def packet_handler(packet):
    # Initialize variables
    payload = ""
    protocol = ""
    src_ip = ""
    dst_ip = ""
    
    # IP Layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # TCP
        if packet.haslayer(TCP):
            protocol = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
            
        # UDP
        elif packet.haslayer(UDP):
            protocol = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
            
        # ICMP
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            
        # Payload handling (truncated for ethics)
        if packet.haslayer(Raw):
            payload = hexdump(packet[Raw].load, dump=True)
            payload = payload[:64]  # Show first 64 bytes only

    # Build output
    output = f"""
[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]
Protocol: {protocol}
Source: {src_ip}:{sport if 'sport' in locals() else ''}
Dest: {dst_ip}:{dport if 'dport' in locals() else ''}
Payload Preview:
{payload if payload else 'No payload detected'}
{'-'*40}"""
    
    print(output)

def main():
    check_privileges()
    
    print("""
    ETHICAL PACKET SNIFFER
    ----------------------
    Features:
    - Captures IP/TCP/UDP/ICMP traffic
    - Shows truncated payload (first 64 bytes)
    - Requires admin privileges
    - No packet storage
    - Real-time display only
    
    Legal Notice: You must have explicit permission
    to monitor this network!
    """)
    
    try:
        sniff(prn=packet_handler, store=0)
    except KeyboardInterrupt:
        print("\nSniffing stopped by user")

if __name__ == "__main__":
    main()
