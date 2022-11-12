IT Security: Defense against the digital dark arts

# Malicious Software
## The CIA Triad 
- Confidentiality
  - hide information
- Integrity
  - "Keeping our data accurate and untampered with"
- Availability
  - "The information we have is readily accessible to those people that should have it."

## Essential Security Terms
- Risk : "the possibility of suffering a loss in the event of an attack on the system"
- Vulnerability : "a flaw in a system that could be exploited to compromise the system"
  - 0-day vulnerability (zero day) : "A vulnerability that is not known to the software developer or vendor, but is known to an attacker."
- Exploit : "Software that is used to take advantage of a security bug or vulnerability"
- Threat : "The possibility of danger that could exploit a vulnerability"
- Hacker : "someone who attempts to break into or exploit a system"
- Attack : "an actual attempt at causing harm to a system"

## Malicious Software
Malware : "A type of malicious software that can be used to obtain your sensitive information, or delete or modify files"
- Adware : "Software that displays advertisements and collects data"
- Trojan : "Malware that disguises itself as one thing but does something else"
- Spyware: "a type of malware that's meant to spy on you"
- keylogger : "a common type of spyware that's used to record every keystroke you make"
- Rootkit : "a collection of software or tools that an Admin would use"
- Logic bomb : "A type of malware that's intentionally installed"

# Network Attacks
- DNS Cache Poisoning Attack : "works by tricking a DNS server into accepting a fake DNS record that will point you to a compromised DNS server. It then feeds you fake DNS addresses when you try to access legitimate website"
- Hacker-in-the-middle attack
  - Rogue AP : "An access point that is installed on the network without the network administrator's knowledge"
  - Evil Twins
- Denial-of-service(DoS) attack: "An attack that tries to prevent access to a service for legitimate users by overwhelming the network or server"
  - Ping of death (large ping)
  - Ping flood (a lot of ping)
  - SYN flood | Half-open attacks
  - Distributed denial-of-service attack(DDoS) : A DoS attack using multiple systems

# Other Attacks
## Client-side Attacks
- Injection attacks
  - To prevent injection attacks : "validating input and sanitizing data"
- Cross-site scription (XSS) attacks : "A type of injection attack where the attacker can insert malicious code and target the user of the service"

## Password Attacks
Password attacks : "utilize software like password-crackers that try and guess your password"
- Brute-force attack

## Deceptive Attacks
Social engineering : "an attack method that relies heavily on interactions with humans instead of computers"
- Phising attack
- Spear phishing
- Spoofing : "a source masquerading around as something else"
- tailgating : "Gaining access into a restricted area or building by following a real employee in"

# Cryptography
Encryption : "The act of taking a message, called **plaintext**, and applying an operation to it, called a **cipher**, so that you receive a garbled, unreadable message as the output, called ciphertext"

Decryption : ciphertext --> plaintext

Encryption algorith : "The underlying logic of process that's used to convert the plaintext into ciphertext"

Cryptosystem : "A collection of algorithms for key generation and encryption and decryption operations that comprise a cryptographic service should remain secure - even if everything about the system is known except the key"
Also knowns as Shannon's maxim : "the enemy knows the system"  which mean "The system should remain secure even if your adversary knows exactly what kind of encryption systems you're employing, as long as your keys remain secure"
Frequency analysis : "The practice of studying the frequency with which letters appear in a ciphertext"
Steganography : "The practice of hiding information form ovservers, but not encoding it"
## Symmetric Encryption
Same key to encrypting and decrypting.
- Substitution cipher : "An encryption mechanism that replaces parts of your plaintext with ciphertext"
- Stream cipher : "takes a stream of input and encrypts the stream one character or one digit at a time, outputting one encrypted character or digit at a time"
- Block ciphers : "Thecipher takes data in, places it into a bucket or block of data that's a fixed size, then encodes that entire block as one unit"

## Symmetric Encryption Algorithms
Data encryption Standard (DES) was adopted as the Federal Information Processing standard (FIPS).
Then : Advanced Encryption Standard was replaced. "Because of the large key size, brute-force attacks on AES are only theoretical right now, because the computing power required (or time required using modern technology) exceeds anything feasible today"
"An important thing to keep in mind when considering various encryption algorithms is **speed** and **ease of implementation**."

# Public Key or Asymmetric Encryption
Grant us 
- Confidentiality
  - Through encryption-decryption
- Authenticity
  - By digital signature 
- Non-repudiation
  - Cannot "dispute the origin of the message"

Message Authentication Codes (MAC) : "A bit of information that allows authentication of a received message, ensuring that the message came from the alleged sender and not a third party"
HMAC : "Keyed-hash message authentication code"
CMACs : "Cipher-based Message Authentication Codes"
CBC-MAC : "Cipher block chaining message authentication codes"

## Asymmetric Encryption Algorithms
Digital Signature Algorithm (DSA)
- RSA
- DH

Elliptic curve cryptographiy (ECC) : 
"A public-key encryption system that uses the algebraic structure of elliptic curves over finite fields to generate secure keys"
"Both Diffie-Hellmen and DSA have elliptic curve variants, referred to as ECDH and ECDSA, respectively"

"US NEST recommends using EC encryption, and the NSA allows its use to protect top secret data with 384 bit EC keys. But the NSA has expressed concern about EC encryption being potentially vulnerable to quantum computing attacks, as quantum computing technology continues to evolve and mature."

# Hashing
Hashing or has function : "A type of function or operation that takes in an arbitrary data input and maps it to an output of fixed size, called a hash or digest"
"Hashing can also be used to identify duplicate data sets in databases or archives to speed up searching of tables or to remove duplicate data to save space."
"Cryptographic hashing is distinctly different from encryption because cryptographic hash functions should be one directional."
"The ideal cryptographic hash function should be deterministic, meaning that the same input value should always return the same hash value."

## Hashing Algorithms
"SHA1 is part of the Secure Hash Algorithm suite of functions, designed by the NSA, published in 1995."

"A successful brute force attack, against even the most secure system imaginable, is a function of attacker time and resources"

Rainbow tables : table of list of password hash
Password salt : "Additional randomized data that's added into the hashing function to generate a hash that's unique to the password and salt combination"

# Cryptography Application
## Public Key Infrastructure (PKI)
A digital certificate contains
"""
- Info on public key
- Registered owner
- digital signature
"""
"The entity that's responsible for storing, issuing and signing certificates is referred to as CA or __Certificate Authority__"
Registration Authority : "responsible for verifying the identities of any entities requesting certificates to be signed and stored with the CA"
"A central repository is needed to securely store and index keys, and a certificate management system of some sort makes managing access to stored certificates and issuance of certificates easier."
Most common certificates : "SSL or TLS server certificate" 

SSL or TLS client certificate : "As the name implies, these are certificates that are __bound to clients__ and are used to __authenticate__ the client to the server, allowing access control to an SSL/TLS service."

Code signing certificate: "This allow users of these signed applications to verify the signatures and ensure that the application was not tampered with."

Based on chain-of-trust with the root certificate at the top.
"A certificate that has no authority as a CA is referred to an __end-entity__ or __leaf certificate__"

"The X.509 standard is what defines the format of digital certificates"
"""
The filed defined in X.509 certificate are:
- Version : What version of the X.509 standard the certificate adheres to
- Serial number : A unique identifier for the certificate assigned by the CA which allows the CA to manage and identify individual certificates
- Certificate Signature Algorithm : This field indicates what public key algorithm is used for the public key and what hashing algorithm is used to sign the certificate
- Issuer Name : This field contains information about the authority that signed the certificate
- Validity : This contains two subfields - "Not before" and "Not After" -which define the dates when the certificate is valid for"
- Subject : This field contains identifying information about the entity the certificate was issued to
- Subject Public Key Info : These two subfields define the algorithm of the public key, along with the public key itself.
- Certificate Signature Algorithm : Same as the Subject Public Key Info field : these two fields must match
- Certificate Signature Value : The digital sign.02
- ature data itself
"""
An alternative to the chain of trust is the web of trust

## Cryptography in Action
HTTPS: "The secure version of HTTP, the HyperText Transport Protocol" could also be call http over TLS or SSL.
TLS and SSL grant us :
"""
1. A __secure__ communication line, which means data being transmitted is protected from potential eavesdroppers
2. The ability to __authenticate__ both parties communicating, though typically only the server is authenticated by the client.
3. The __integrity__ of communications, meaning there are checks to ensure that messages aren't lost or altered in transit.
"""
Look for the diagram for the TLS handshake
"The session key is the shared symmetric encryption key used in TLS sessions to encrypt data being sent back and forth."
Secure Shell : "A secure network protocol that uses encrpytion to allow access to a network service over unsecured networks."
Pretty-Good-Privacy (PGP) : "An encryption application that allows authentication of data, along with privacy from third parties, relying upon asymmetric encryption to achieve this."

## Securing Network Traffic
Virtual Private Network (VPN): "A mechanism that allows you to remotely connect a host or network to an internal, private network, passing the data over a public channel, like the internet."
IPSec: 
- Transport mode : "When transport mode is used, only the payload of the IP packet is encrypted, leaving the IP headers untouched"
- Tunnel mode : "In tunnel mode, the netire IP packet, heder payload and all, is encrypted and encapsulated inside a new IP packet with new headers".
Layer 2 tunneling Protocol (L2TP) in conjunction with IPSec: "L2TP doesn't provide encryption itself. It's a simple tunneling protocol that allows encapsulation of different protocols or traffic over a network that may not support the type of traffic being sent. L2TP can also jus tsegregate and manage the traffic"

"The __tunnel__ is provided by L2TP which permits the passaing of unmodified packets from one network to another. The __secure channel__, on other hand, is provided by IPsec, which provides confidentiality, integrity and authentication of data being passed."

## Cryptographic Hardware
Trusted Platform Module or TPM : "TPM offers - secure generation of keys,
- random number generation,
- remote attestation, 
- data binding and sealing.
  
A TPM has a unique secret RSA key burned into the hardware at the time of manufacture, which allows a TPM to perform things like hardware authentication"

TEE : Trusted Execution Environment :"provides a full-blown isolated execution environment that runs alongside the main OS."

Full disk encryption (TPE) : "practice of encrypting the entire drive in the system"
- PGP (commercial)
- Bitlocker (Microsoft)
- Filevault 2 (Apple)
- dm-crypt (Linux)

# AAA Security : Authentication, Identification and  Accounting
- Identification : "The idea of describing an entity uniquely"
- Authentication (authn) : "proving who you claim to be"
- Authorization (authz) : "pertains to the resources and identity has acces to"

"Incorporating good password policies into an organization is key to ensuring that employees are securing their accounts with strong passwords"

## Multifactor authentication
A system where users are authenticated by presenting multiple pieces of information or objects.
Three types : 
- Something you know : password /pin
- Something you have : ATM / Bank card
- Somthing you are: Biometric ID

## Certificates
"Certificates are public keys that are signed by a certificate authority or CA as a sign of trust"

"In order to issue client certificates, an organization must setup and maintain CA infrastructure to issue and sign certificates"

"Certificate revocation list (CRL) : A signed list published by the CA which defines certificates that have been explicitly revoked"

## LDAP
Lightweight Directory Access Protocol (LDAP) : "An open, industry-standard protocol for accessing and maintaining directory services"

## RADIUS
Remote Authentication Dial-In User Service(RADIUS) : "A protocol that provides AAA services for users on a network"

"The Network Access Server doesn't handle authentication decisions directly. Instead, it related authentication messages between the client and the RADIUS server"

"Client don't actually interact directly with the RADIUS server; the authentication is relayed via the Network Access Server."

## Kerberos
Kerberos : "A netwrok authentication protocol that uses 'tickets' to allow entities to prove their identity over potentially insecure channels to provide mutual authentication"

How it's operate : 
1. Users enters username/password in the client machine
2. "Their kerberos client software will then take the password and generate a symmetric encryption key from it" 
3. "The client sends a plain text message to the Kerberos, AS or Authentication Server WHICH INCLUDES THE USER ID of the authenticating users.
4. AS look for the user in the authentication database.
5. If the user is in the database, the AS "use the secret key to encrypt and send a message containing the client TGS session key". (Ticket Granting Service)
6. "The AS also sends a second message with a Ticket Granting Ticket (TGT) which is encrypted using the TGS secret key."
7. The user can now use the TGT to "request access to services from within the Kerberos realm. This is done by sending a message to the Ticket Granting Service with the encrypted Ticket Grantinkg Ticket."
8. The TGS decrypts the TGT using TGS secret key and check the client ID to look if it's match. If so, it sends 2 messages to the client : 
   1. "The first one, contains the client to server ticket which is comprised of the client ID, client address, validity period, and the client-server session key encrypted using the service's key.
   2. The second message, contains the client-server session key itself, and is encrypted using the client TGS key."
9. "The client has enough information to authenticate itself to the service server or SS".


## TACACS+
Terminal Access Controller Access-Control System Plus
"It's a Cisco developed AAA protocol that was released as an open standard in 1993"
"TACACS+ is mainly used as an authentication system for network infrastructure devices, which tend to be high value targets for attackers."

## Single Sign-On
Single Sign-on (SSO) : "An authentication concept that allows users to authenticate once to be granted access to a lot of different services and applications"
Kerberos is an example of SSO system. 

An other example of an SSO system is OpenID.

# Authorization
Authorization : "Pertains to describing what the user account has access to, or doesn't have access to"
"One very popular open standard for authorization and access delegation is OAuth"

## Mobile Security Methods
### Common mobile security threats and challenges
- Phishing : "Phishing attacks can use SMS messaging, email accounts, messages via numerous social media applications, or malicious links in browsers to target your movile devices"
- Malicious applications (malware) : "Malware can take the form of apps designed to collect and transmit personal and corporate information to third parties"
- Insecure Wi-fi and "meddler in the middle" attacks : "An attacker places themself in the middle of two hosts that think they're communicating directly. The attacker may monitor the information from these hosts and potentially modify it in transit. Open or "free" Wi-fi hotspots are especially susceptible to meddler in the middle and similar attacks."
- Poor update habits for devices and apps : "An example is failure to install security patches regularly deployed through software and firmware updates. Unpatched devices and applications often contain exploits and vulnerabilities that attackers may use to collect sensitive data"

### Security measures used to protect mobile devices
- Screen Locks
- Remote wipes : "Remotes wipes are methods to remove data from a device remotely.
  - Locator applications
  - OS updates
  - Device encrpytion
  - Remote backup applications
  - Failed login attempt restrictions
  - Antivirus/Antimalware
  - Firewall

## Access Control
OAuth : "An open standard that allows users to grant third-party websites and applications access to their information without sharing account credentials"
Connecting to a third-party through Google or Facebook account
"OAuth permissions can be used in phishing-style attacks to gain access to accounts, __without requiring credentials__ to be compromised"

"OAuth is specifically an authorization system and OpenID is an authentication system"

## Access Control List
Access Control List (ACL) : "A way of defining permissions or authorizations for objects"
"These individual access permissions per object are called Access Control Entries and they make up the ACL"

# Accounting
Accounting : "Keeping records of what resources and services your users accessed, or what they did when they were using your systems"

"__TACASCS+__ is a device access AAA system that manages who has access to your network devices and what they do on them"

# Secure Network Architecture
## Network Hardening Best Practices
Network hardening : "The process of securing a network by reducing its potential vulnerabilities through configuration changes and taking specific steps"

"Disabling unnecessary extra services or restricting access to them"

- Implicit deny (whitelisting (instead of blacklisting))  : "A network security concept where anything not explicitly permitted or allowed should be denied"  
  - Can be done with ACL configuration and firewall.
- Monitoring networking 
  - Analyzing logs : "The practice of collecting logs from different network and sometimes client devices on your network, then performing an automated analysis on them"
  - "__Logs analysis systems__ are confirgured using user-degined rules to match interesting or atypical log entries"
  - "__Normalizing log data__ is an important step, since logs from different devices and systems may not be formatted in a common way"
- Correlation analysis : "the process of taking log data from different systems and matching events across the systems" also important in post-fail analysis
  - Good tools for that : __Splunk__
- Flood guards : "Provide protection against DoS"
  - Like fail2ban
- Network segmentation : Separation of network virtualy

## Network Hardware Hardening
DHCP Discovering
DHCP (Dynamic Host Configuration Protocol) : "Protocol where devices on a network are assigned critical configuration information for communicating on the network"
- DHCP Snooping
  - "A switch that has DHCP snooping will monitor DHCP traffic being sent across it. It will also track IP assignments and map them to hosts connected to switch ports."
  - Protect against : Rogue DHCP Server-Attack : "If an attacker can manage to deploy a rogue DHCP server on your network, they could hand out DHCP leases with whatever information they want. This includes setting a gateway address or DNS server, that's actually a machine within their control."
- Dynamic ARP inspection : 
  - ARP can lead to Men-in-the-middle attack "because of the unauthenticated nature of ARP" (Gratuitous ARP response)
  - "IP source guard (IPSG) can be enabled on enterprise switches along with DHCP snooping"
- 802.1X --> "IEEE standard for encapsulating Extensible Authentication Protocol (EAP)"
  - EAP-TLS : "An authentication type supported by EAP that uses TLS to provide mutual authentication of both the client and the authenticating server"

## IEEE 802.1X
"There are three nodes in the authentication process : supplicant, authenticator, and authentication server."
"The authentication server uses either a shared key system or open access system to control who is able to connect to the network"
"Based on the criteria of the authentication server the supplicator will grant the authentication request and begin the connection process or it will be sent an Access REject message and terminate the connection"

## Network Software Hardening
- Firewalls
  - Host-based firewall
  - Network-based firewall
- Proxies
  - HAPROX : "is a free, very fast and reliable reverse-proxy offering high availability, load balancing, and proxyingfor TCP and HTTP-based applications. It is particularly suited for very high traffic web sites and powers a significant portion of thw world's most visited one"
  - Appache : "In addition to being a 'basic' web server, and providing static and dynamic content to end-users, Apache httpd (as well as most other web servers) can also act as a reverse proxy server, also-known-as a 'gateway' server"
- VPN: "are commonly used to provide __Secure remote access__, and __link two networks securely__"

# Wireless Security
## WEP Encryption and Why You Shouldn't Use it
Wire Equivalent Privacy (WEP): Bad for privacy. 
- No one should use WEP
-  Support originally two modes : Open system authentification and shared key authentication

## LEt's Get rid of WEP!WPA/WPA2
Wi-fi Protected Access (WPA) : "Designed as a short-term replacement that would be compatible with older WEP-enabled hardware with a simple firmware update"
Temporal Key Integrity Protocol (TKIP) add three features:
1. "more secure key derivation method was used to more securely incorporate the IV into the per packet encryption
2. a sequence counter was implemented to prevent replay attacks by rejecting out of order packets
3. A 64-bit MIC or Message Integrity Check was introduced to prevent forging, tampering, or corruption of packets." 
"Under WPA, the __pre-shared key__ is the Wifi password you share with people when they come over and want to use your wireless network"
WPA2 implement CCMP -> Counter Mode CBC-MAC Protocol

Four-way Handshake: "It's designed to allow an AP to confirm that the client has the correct pairwise master key, or pre-shared key in a WPA-PSK setup without disclosing the PMK"

## Wireless Hardening
Best option : 802.1X with EAP-TLS
- Really complex 
- "Need a Radius server and an additional authentication back-end"
"If 802.1X is to complicated for a company, the next best alternative would be WPA2 with AES/CCMP mode"
- But we need to set up "A long and complex passphrase that wouldn't be found in a dictionary"
- Disable WPS

# Network Monitoring
## Sniffing the Network
Packet sniffing (packet capture) : "The process of intercepting network packets in their entirety for analysis"
Promiscuous Mode : "A type of computer networking operational mode in which all network data packets can be accesed and viewed by all network adapters operating in this mode"
- On OSX :
  - `tcpdump -li en0`
- On Windows
Port mirroring : "Allows the switch to take all packets form a specified port, port range, or entire VLAN and mirror the packets to a specified switch port"
Monitor mode : "Allows us to scan across channels to see all wireless traffic being sent by APs and clients"

## Wireshark and tcpdump
Tcpdump : "A super popular, lightweight, command-line based utility that you can use to capture and analyse packets"
`sudo tcpdump -i eno1 ip and host example.com`



Wireshark 

## Intrusion Detection /Prevention Systems
Intrusion Detection and Prevention System(IDS/IPS) "operate by monitoring network traffic and analyzing it"
"They look for matching behavior or characteristics that would indicate malicious traffic"
Network base : "__Network Intrusion Detection System (NIDS)__ the detection system would be deployed somewhere on a network where it can __monitor traffic__ for a network segment or subnet"

Network Intrusion Prevention System (NIPS) : can "take action against a suspected malicious traffic"

NIPS or NIDS software : Snort, Suricata, Zeek Network Security Monitor

## Unified Threat Management (UTM)
"UTM solutions stretch beyond the traditional firewall to include an array of network security tools with a single management interface. UTM simplifies the configuration and enforcement of security controls and policies, saving time and resources. Security event logs and reporting are also centralized and simplified to provide a holistic view of network security events"

## Home Network Security
Common security vulnerabilities
- Meddler in the middle attacks
- Data Theft
- Ransomware

## Keeping home networks secure
- Change the default name and password 
- Limit access to the home network
- Create a guest network
- Turn on WiFi network encryption
- Turn on the router's firewall
- Update to the newest WiFi standard

# System Hardening
## Intro to Defense in Depth
Defense in depth : "The concept of having multiple, overlapping systems of defense to protect IT systems"

## Disabling Unnecessary Components
Attack vector : "The method or mechanism by which an attacker or malware gains access to a network or system"
Attack surface : "The sum of all the different attack vectors in a given system"
"The less complex somthing is, the less likely there will be undetected flaws"
"Another way to keep things simple is to reduce your software deploywments"
Ex : "Telnet access for a managed switch has no business being enabled in a real-world environment"


## Host-based firwalls
Host-based firewalls : "Protect individual hosts from being compromised when they're used in untrusted, potentially malicious environments"
A host-based firewall "plays a big part in reducing what's accessible to an outside attacker"
If the users of the system have administrator rights, then they have the ability to change firewall rules and configurations"

## Logging and Auditing
Security information and event managements systems (SIEMS) : "A SIEM can be thought of as a centralized log server. It has some extra analysis features too"
Normalization : "The process of of taking log data in different formats and converting it into a standardized format that's consistent with a defined log structure"
"Once logs are centralized and standardized, you can write automated alerting based on __rules__"

## Windows Defender Guide 
User Account Control (UAC) : "allows IT administrators to create standard user accounts with limited access rights and privileges for end users. This configuration can prevent users from installing unauthorized programs, changing system settings, tampering with firewalls, and more"

## Antimalware Protection
"Lots of unprotected systems would be compromised __in a matter of minutes__ if directly connected to the internet without any safeguards or protections in place"
"Antivirus software will monitor and analyze things, like new files being created or being modified on the system, in order to watch for any behavior that matches a known malware signature", but "it protects against the most common attacks out there on the internet."
"Antivirus software is just one piece of our anti-malware defense"

## Disk Encryption
Full-disk encryption (FDE): "Works by automatically converting data on a hard drive into a form that cannot be understood by anuone who doesn't have the key to 'undo' the conversation"

Secure boot : Bit Locker(Microsoft), FileVault 2 (Mac) Dm crypt (Linux)

"When you implement a full disk encryption solution at scale, it's super important to think about how to handle cases where password are forgotten."
Hey Escrow : "Allows the encryption key to be securely stored for later retrieval by an authorized party"

"__Home directory__ or __file-based encryption__ only guarantees confidentiality and integrity of files protected by encryption."

## Bastion Host 
"Bastion hosts are special-purpose machines that permit restricted access to more sensitive networks or systems. By having one specific purpose, these systems can have strict authentication enforced, more firewall rules locked down, and closer monitoring and logging"


# Application Hardening
## Software Patch Management
"As an IT Support Specialist, it's critical that you make sure that you install software updates and security patches in a timely way, in order to __defend your company's systems and networks__"

## Browser Hardening
### Identifying trusted versus untrusted sources
- "Use antivirus and anti-malware software and browser extensions"
- "Check for SSL certificates"
- "Ensure the URL displayed in the address bar shows the correct domain name"
- "Search for negative review of the website from trusted sources"
- "Don't automatically trust website links provided by people or organization you trust."
- "Use hashing algorithms for downloaded file"

## Browser settings
- Block pop-up
- Clear browsing data and cache
- Use private-browsing mode
- Sign-in/browser data synchronization
  Use ad blockers

## Application Policies
"A common recommendation, or even a requirement, is to only support or require the __latest version__ of a piece of software"
"It's generally a good idea to __disallow risky classes__ of software by policy. Things like file sharing software and piracy-related software tend to be closely associated with malware infections"
"Understanding __what your users need__ to do their jobs will help shape your approach to software policies and guidelines"
"Helping your users accomplish tasks by recommending or supporting specific software makes for a more __secure environment__"
"Extensions that require full access to web sites visited can be risky, since the extension developer has the power to modify pages visited"

# Risk in the Workplace
## Security Goals
"If your company handles credit card payments, then you have to follow the __PCI DSS__, or __Payment Card Industry Data Security Standard__"
PCI DSS Objectives
"""
1. Build and maintain a secure network and systems
2. Protect cardholder data.
3. Maintain a vulnerability management program
4. Implement strong access control measures
5. Regularly monitor and test networks
6. Maintain an information security policy
"""

## Measuring and Assessing Risk
"Security is all about determining __risks__ or exposure; understanding the likelihood of __attacks__; and designing __defenses__ around these risks to __minimize__ the impact of an attack."
"Security risk assessment starts with __threat modeling__"
"High-value data usually includes account information, like usernames and passwords. Typically, __any kind of user data is considered high value__, especially if payment processing is involved"
Vulnerability Scanner : "A computer program designed to assess computers, computer systems, networks or applications for weaknesses"
Ex : Nessus, OpenVAS, Qualys
Penetration testing : "The practice of attempting to break into a system or network to verify the systems in place"

## Privacy Policy
Privacy policies : "oversee the access and use of sensitive data"
"It's a good practice to apply the principle of __least privilege__ here, by not allowing access to this type of data by default"
"__Data-handling policies__ should cover the details of how different data is classified"

## Data Destruction
Data destruction : "is removing or destroying data stored on electronic devices so that an operating system or application cannot read it. Data destruction is required when a company no longer needs a device, when there are unused or multiple copies of data, or you are required to destroy specific data"

### Recycling
"Standard recycling methods include the following: 
- Erasing/wiping
- Low-level formatting
- Standard formatting"

# Users
## User Habits
"You can build the world's best security systems, but they won't protect you if the users are going to be practicing __unsafe security__"
Risky business "You should __never upload confidential information__ onto a third-party service that hasn't been evaluated by your company"
"It's important to __make sure employees use new and unique passwords__, and don't reuse them from other services"
"A much greater risk in the workplace that users should be educated on is __cerdential theft__ from phishing emails"
"If someone entered their password into a phishing site, or even suspects they did, it's important to __change their password__ as soon as possible"

## Third-Party Security
"If they have subpar security, you're undermining your security defenses by potentially opening a new avenue of attack"

## Security Training
"Helping others keep security in mind will help decrease the security burdens you'll have as an IT Support Specialist"

# Incident Handling
## Incident Reporting and Analysis
- Detect it
- Analyse it --> "determine the effects and the scope of damage"
"If an account was compromised, change the password immediately. If the owner is unable to __change the password__ right away, then __lock the account__"
"__Severity__ includes factors like what and how many systems were compromised, and how the breach affects business functions"
"The __impact__ of an incident is also an important issue to consider"
Data exfiltration : "The unauthorized transfer of data from a computer"
Revocerability : "How complicated and time-consuming the recovery effort will be"

## Incident Response
Incident Response : "When you've had a data breach, you may need forensic analysis to analyze the attack. This analysis usually involves extensive evidence gathering"

Regulated data : "It's important to consider the type of data involved in an incident. Many types of data are subject to government regulations that require you to take extra care when handling it"

Digital Rights Management (DRM) : "help ensure data regulations compliante. DRM technology comes in the form of either software or hardware solutions"
- Restrict users
- Set expiration dates
- Limit access

End User Licensing Agreements (EULAs) : "are similar to DRM in specifying certain rights and restrictions that apply to the software. [...] you can't complete an installation (or acess, share, or download data) until you agree to the terms written in the EULa statement"

Chain of custody : "refers to a process that tracks evidence movement through its collection, safeguarding, and analysis lifecycle."

## Bring Your Own Device (BYOD)
BYOB threats
- Loss or theft
- Data loss
- Data leakage
- Data portability
- Data portability
- Security vulnerabilities
- Meddler in the middle attacks
- Malware
- Jailbreaking

Solutions 
- BYOD policy
- Mobile Device management (MDM) software
- "Use an Enterprise Mobile Management (EMM) system"
- "Require the use of multi-factor authentication (MFA)"
- Acceptable use policy(AUP)
- Non-disclosure agreements (NDA)
- Restrict data access
- Educate staff about data security
- Back up device data
- Data leakage prevention (DLP)