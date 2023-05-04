# Using Pydes.py
# Alex Basden
# Simple Message using DES with Pydes.Py

from pydes import des

key = "secret_K"
text = input("Please enter your message you wish to decrypt/encrypt: ")
d = des()

encrypted = d.encrypt(key, text, padding=True)
decrypted = d.decrypt(key, encrypted, padding=True)
print("Encrypted Message: %r" % encrypted)
print("Your original Message was: ", decrypted)
