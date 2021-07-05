import hashlib
Hashing = input("Enter the word :")
enc= hashlib.md5(Hashing.encode())
print(enc.hexdigest())