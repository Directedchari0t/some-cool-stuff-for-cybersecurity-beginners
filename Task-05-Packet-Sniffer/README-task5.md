# Task 5 - Network Packet Sniffer

## 🌐 Description
**ETHICAL USE ONLY**  
Basic network traffic analyzer using Scapy

## ⚠️ Requirements
- Run with admin privileges
- Network owner permission
- Educational use only

## 🚀 Usage
```bash
sudo python packet_sniffer.py
```
Displays real-time:
- Source/Destination IPs
- Protocol (TCP/UDP/ICMP)
- Truncated payload (64 bytes)

## 📦 Dependencies
- Scapy (`pip install scapy`)

## Example Output
```
[2023-08-21 14:35:22]
Protocol: TCP
Source: 192.168.1.15:54321  
Dest: 104.18.25.123:443
Payload Preview:
0000  17 03 03 01 5A  [...]
```

## ⛔ Limitations
- No packet storage
- No deep packet inspection
- Limited protocol support
