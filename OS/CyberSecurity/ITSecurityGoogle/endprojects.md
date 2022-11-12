



An external website permitting users to browse and purchase widgets

Authentication system
- Incorporating good password policies
   1. More than 6 chars
   2. symbol + maj + min + 
   3. No dictionary words
- Multifactor authentication


External website security
- Risk and Solution
  - Injection Attacks : clear type for every input in the website
  - Protection against DNS Cache Poisoning Attack
  - Protection against Denial-of-Service
    - Ping of death --> Limit the size of ping 
    - Ping flood --> Limit the quantity of Ping (with same adress an)
    - SYN flood --> log audit to look for anormality
- Measures
  - Use of HTTPS, which is a secure way of accessing the web
  - Installing a Firewall
  - OAuth can be usefull, let user use third-party app to connect


Internal website security
- Kerberos or LDAP
- Strict ACL, least privelege as possible

Remote access solution
- VPN and RADIUS (Remote Authentication Dial-In User Service)
- Using Proxies

Firewall and basic rules recommendations
- Firewall both host-based and network-based
- See Security and privac policy recommendation
- log auditing (with normalization for easy detection of anomaly)
- Implicit deny (whitelisting), through ACL
- "Disabling unnecessary extra services or restricting access to them"

Wireless security
- WPA2 which use AES which is the best for the moment with a good password. 
  - Disabling WPS
- Using DHCP so we can be protected against DHCP Snooping
- Using Dynamic ARP inspection
- 

VLAN configuration recommendations

Laptop security configuration
- Full disk encryption to secure against thieft and such. Can use PGP, Bitlocker, Filevualt or DM-Crypt
Application policy recommendations

Security and privacy policy recommendations
- Teaching the danger of social engineering
  - through games and general culture : be sure to always close the lock screen otherwise coworker can do harmless pranks. 
  - Through exercises 
  - Open culture, so if someone thing it's got phished, we can use measure (without fear of blame)
- Updating frequently

Intrusion detection or prevention for systems containing customer data
- Using an Intrusion Detection System (IDS) and a Intrusion Prevention System"
- 

