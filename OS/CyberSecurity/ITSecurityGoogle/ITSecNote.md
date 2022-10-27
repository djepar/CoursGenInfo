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
  - SYN flood | Half-open attackss
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
