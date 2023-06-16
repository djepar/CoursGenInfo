# Introduction to Python for Cybersecurity

## Introduction to MITRE ATT&CK and Shield
"MITRE ATT&CK is a tool developed by the MITRE Corporation to improve cybersecurity understanding."

"It maps different attacker techniques and procedures to the cyberattack life cycle and an adversary's goals"

"MITRE Shield was developed by MITRE to promote active defense"

"It identifies different goals that an active defender may have and outlines methods for achieving those goals"

### Terminology of MITRE ATT&CK and Shield

- Tactic : "The tactical goal at a particular stage of a cyberattack or a goal in active defense."
- Technique: "A mechanism by which an attacker can achieve the goal outline in a particular Tactic
  - Sub-technique : "A method for carrying out a particular Technique"
- Procedure : "A specific implementation of a particular Technique or Sub-Technique"


### MITRE ATT&CK Tactics
1. PRE-ATT&CK : Reconnaissance and Resource Development
2. Initial Access
3. Execution
4. Persistence
5. Privilege Escalation
6. Defense Evasion
7. Credential Access
8. Discovery
9. Lateral Movement
10. Collection
11. Command and Control
12. Exfiltration
13. Impact

### MITRE Shield Tactics
1. Channel
2. Collect
3. Contain
4. Detect
5. Disrupt
6. Facilitate
7. Legitimize
8. Test

# Python for PRE-ATT&CK
## MITRE PRE-ATT&CK
- MITRE PRE-ATT&CK matrix used to be its own standalone matrix.
  - Contained a collection of Tactics and Techniques
  - Mapped to the Recon and Weaponize stages of the cyber kill chain
- Now PRE-ATT&CK is the first two stages of the MITRE PRE-ATT&CK for the Entreprise framework 
  - Reconnaissance
  - Resource Development

### PRE-ATT&CK : Reconnaissance
- The first stage of PRE-ATT&CK focuses on gathering target information from a variety of different sources:
  - Active Scanning
  - Gather Victim Host Information
  - Gather Victim Identity Information
  - Gather Victim Network Information
  - Gather Victim Org Information
  - Phishing for Information
  - Search Closed Sources
  - Search Open Technical Databases
  - Search Open Websites/Domains
  - Search Victim-Owned/Websites

### PRE-ATT&CK: Resource Development
- The second stage of PRE-ATT&CK involves the attacker developing or acquiring the tools needed to perform their attack:
- Acquire Infrastructure
- Compromise Accounts
- Compromise Infrastructure
- Develop Capabilities
- Establish Account
- Obtain Capabilities

### Python for PRE-ATT&CK
- The Resource Development Tactic of PRE-ATT&CK largely occurs on the attacker's infrastructure 
  - No interaction with target systems for defenders to detect
  - Depends heavily on the attacker's goals and resources

## Network Scanning

- Knowledge of a target network is vital for an attacker.
  - Identification of potential target systems
  - Discovery of vulnerable applications
- Network scanning is one method of learning a target network architecture
  - Port scanning
  - Banner collectioon
  - Vulnerability scanning

## Introduction to Scapy

```
from scapy.all import *



# Create an HTTP packet
http_packet = Ether() / IP(dst="www.google.com") / TCP() / "GET / HTTP/1.1\r\nHost: www.example.com\r\n\r\n"

# Create a list of packets containing the HTTP packet
packet_list = [http_packet]

# Write the packets to the capture file
wrpcap("http.cap", packet_list)

# To see the information 
packet 

p = packet[0] 
p.show()

# Creating packet 
p2 = IP()/TCP()
p2.show()

# changing a port
p2[TCP].dport = 35

p3 = IP(dst=8.8.8.8)/TCP(dport=53)
