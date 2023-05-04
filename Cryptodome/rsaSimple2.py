# Part 2 of RsaSimple.py
from Crypto.Cipher import AES

fileIn = open("encrypted.bin", "rb")
nonce, tag, ciphertext = [fileIn.read(x) for x in (16, 16, -1)]
fileIn.close()

# Assumes Key is available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)