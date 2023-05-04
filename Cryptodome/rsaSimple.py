# RSA Example with Cryptodome
# Alex Basden

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'Test of RSA'

key = get_random_bytes
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

fileOut = open("encrypted.bin", "wb")
[fileOut.write(x) for x in (cipher.nonce, tag, ciphertext)]
fileOut.close()
