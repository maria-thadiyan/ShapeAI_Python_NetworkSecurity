import hashlib
Hashing = input("Enter the word :")
enc= hashlib.md5(Hashing.encode())
enc.update(b"abcd")
hex_d = enc.hexdigest()
for i in range(1,5):
    hex_d += (hex_d)
for j in range(1,5):
    hex_d5 = hashlib.md5(hex_d.encode())

print("Hashed Form : ",hex_d5.hexdigest())