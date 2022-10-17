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
Then : Advanced Encryption Standard was replaced. "Because of the large key size, brute-force attacks on AES are only theoreticla right now, because the computing power required (or time required using modern technology) exceeds anything feasible today"
"An important thing to keep in mind when considering various encryption algorithms is **speed** and **ease of implementation**."