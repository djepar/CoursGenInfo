# Creating/inspecting key pair, encrypting/decrypting and sign/verify using OpenSSL
## Generating keys
### Generating a private key
`openssl genrsa -out private_key.pem 2048`

### Generating a public key
`openssl rsa -in private_key.pem -outform PEM -pubout -out public_key.pem`

## Encrypting and decrypting
Creating the message:
`echo 'This is a secret message, for authorized parties only' > secret.txt`

Encrypting the message:
`openssl rsautl -encrypt -pubin -inkey public_key.pem -in secret.txt -out secret.enc`

Decrypting the message
`openssl rsautl -decrypt -inkey private_key.pem -in secret.enc`

## Creating a has digest
Creating a hash digest :
`openssl dgst -sha256 -sign private_key.pem -out secret.txt.sha256 secret.txt`

Public key + hash digest for repudiation
`openssl dgst -sha256 -verify public_key.pem -signature secret.txt.sha256 secret.txt`