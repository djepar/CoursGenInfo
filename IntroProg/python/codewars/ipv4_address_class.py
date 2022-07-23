'''
networking 101/2: Identify the IPv4 address Class

def ipv4_address_class(ipv4_addr):
    bonjour = ipv4_addr.split(".")
    print(bonjour[0])
    return bonjour

'''
import re
def ipv4_address_class(ipv4_addr):
    pattern = r"\d{1,3}\.\d{1,3}.\d{1,3}.\d{1,3}"
    return re.match(pattern, ipv4_addr)

assert(ipv4_address_class('192.0.0.0'), True)
assert(ipv4_address_class('a.1.2.2'), False)

