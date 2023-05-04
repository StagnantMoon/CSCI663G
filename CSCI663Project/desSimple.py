# Test of Pycryptodome
# Kind of works, but needs more work on it.
# Would need to mess with the def(pad) to get other things to work.

from Crypto.Cipher import DES


def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)


key = b'hello123'
message = input("What is the word you wish to encrypt: ")
byteMessage = bytes(message, 'utf-8')


des = DES.new(key, DES.MODE_ECB)

paddedText = pad(byteMessage)
encryptedText = des.encrypt(paddedText)

print(encryptedText)
print(des.decrypt(encryptedText))