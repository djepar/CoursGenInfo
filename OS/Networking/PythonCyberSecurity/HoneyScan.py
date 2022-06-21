from scapy.all import *

ip = "10.10.11.164"
ports = [53,80]
honeys = [8080, 8443]

blocked = []

def analyzePackets(p):
    global blocked
    if p.haslayer(IP):
        response = Ether(src=p[Ether].dst,dst=p[Ether].src)/\
