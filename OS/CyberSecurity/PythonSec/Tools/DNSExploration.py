#!/usr/bin/env python3

import dns
import dns.resolver
import socket

def ReverseDNS(ip):
    """
    Performs reverse DNS lookup for the given IP address.
    Returns a list of domain names associated with the IP address.
    """
    try :
         result = socket.gethostbyaddr(ip)
    except:
        return []
    return [result[0]] + result[1]

def DNSRequest(domain):
    """
    Performs a DNS request for the given domain.
    Prints the domain name and associated IP addresses.
    Performs reverse DNS lookup for each IP address and prints the associated domain names.
    """
    try:
        result = dns.resolver.resolve(domain,'A')
        if result:
            print(domain)
            for answer in result:
                print(answer)
                print("Domain Names : %s"  % ReverseDNS(answer.to_text()))
    except (dns.resolver.NXDOMAIN, dns.exception.Timeout):
        return

def SubdomainSearch(domain, dictionary, nums):
    for word in dictionary:
        subdomain = word+"."+ domain
        DNSRequest(subdomain)
        if nums: 
            for i in range(0,10):
                s = word+str(i)+"."+domain
                DNSRequest(s)


domain = "google"
d = "subdomains.txt"
dictionary = []
with open(d, "r") as f:
    dictionary = f.read().splitlines()
SubdomainSearch(domain, dictionary, True)