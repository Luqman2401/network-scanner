import scapy.all as scapy
# Scan a network for open ports
def scan_network(ip_address, port_range):
    for port in range(port_range[0], port_range[1]):
        packet = scapy.IP(dst=ip_address, ttl=64) / scapy.TCP(dport=port)
        response = scapy.sr1(packet, timeout=1, verbose=0)
        if response:
            print(f"Port {port} is open on {ip_address}")
scan_network("192.168.1.1", (1, 100))
