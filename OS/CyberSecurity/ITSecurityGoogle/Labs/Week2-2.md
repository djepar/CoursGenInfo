# Hands-on with Hashing
"Md5sum is a hashing program that calculates and verifies 128-bit MD5 hashes."

Shasum : "is an encryption program that calculates and verifies SHA hashes. It's also commonly used to verify the integrity of files"

## MD5
Creating a file
`echo 'This is some text in a file, just so we have some data' > file.txt`
Generating the MD5 sum:
`md5sum file.txt > file.txt.md5`

## Verifying an invalid file
Copying the file
`cp file.txt badfile.txt`

Generating a new md5sum
`md5sum badfile.txt > badfile.txt.md5`

Changing the file (badfile.txtwith nano or wtf)

Looking it the file match
`md5sum -c badfile.txt.md5` 
Should failed

## SHA1 
Creating a SHA1 sum
`shasum file.txt > file.txt.sha1`

To verify the hash 
`shasum -c file.txt.sha1`

## SHA256
The `-a` specifies the algorithm to use, by defaults it's SHA1.
`shasum -a 256 file.txt > file.txt.sha256`