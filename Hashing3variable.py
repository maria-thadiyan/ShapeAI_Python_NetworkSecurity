import hashlib
Hashing = input("Enter the word :")
enc = hashlib.sha3_256(Hashing.encode())

enc = hashlib.sha1(Hashing.encode())

enc = hashlib.blake2b(Hashing.encode())

print(enc.hexdigest())