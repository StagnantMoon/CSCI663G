# Alex Basden
# Uses Curve 25519 as is one of fastest curves in ECC, and is not covered by known patents
# -x2 + y2 = 1 – (121665/121666) x2y2 (mod 2255 – 19)
# y = (u-1)/(u+1) u = 9
import base64
from typing import Tuple
import random
import hashlib
import hmac
from Crypto.Cipher import AES

p = pow(2, 255) - 19
# Arguments for curve

a = -1
d = -121665 * pow(121666, -1, p)

# Base for Curve 25519
G = (15112221349535400772501151409588531511454012693041857206046113283949847762202,
     46316835694926478169428394003475163141307993866256225615783033603165251855960)


# Methods

def isoncurve(P: Tuple[int, int], p: int):
    x, y = P
    assert ((a * x * x) + (y * y)) % p == (1 + d * x * x * y * y) % p


def addpoints(P: Tuple[int, int], Q: Tuple[int, int], ):
    x1, y1 = P
    x2, y2 = Q

    x3 = (((x1 * y2 + y1 * x2) % p) * pow(1 + d * x1 * x2 * y1 * y2, -1, p)) % p
    y3 = (((y1 * y2 - a * x1 * x2) % p) * pow(1 - d * x1 * x2 * y1 * y2, -1, p)) % p

    isoncurve((x3, y3), p)
    return x3, y3


# Scalar Multiplication

def applydoubleaddmethod(G: Tuple[int, int], k: int):
    targetPoint = G
    # 0b111111101
    kBinary = bin(k)[2:]

    for i in range(1, len(kBinary)):
        currentBit = kBinary[i: i + 1]
        targetPoint = addpoints(targetPoint, targetPoint)

        if currentBit == "1":
            targetPoint = addpoints(targetPoint, G)

        isoncurve(targetPoint, p)

        return targetPoint


def derivekeys(T):
    tx, ty = T
    # get x coordinate of point T as binary
    tx_binary = bin(tx)[2:]
    # get its first 192-bit value
    tx_binary_cropped = tx_binary[0:192]
    # restore 192-bit x coordinate
    tx_restored = str(int(tx_binary_cropped, 2))
    # use sha-256 to hash
    hashed_tx = bin(int(hashlib.sha256(str.encode(tx_restored)).hexdigest(), 16))[2:]

    assert len(hashed_tx) == 256

    # split the hash into 128-bit and 128-bit as k1 and k2

    k1 = int(hashed_tx[0:128], 2).to_bytes(16, byteorder='big')
    k2 = int(hashed_tx[128:], 2).to_bytes(16, byteorder='big')

    return k1, k2


def findmac(message, key):
    return hmac.new(
        key,
        message,
        hashlib.sha256
    ).hexdigest()


# User 1 Private key
user1ka = random.getrandbits(256)
# User 1 Public Key
user1kq = applydoubleaddmethod(G=G, k=user1ka)

# User 2 Random Key Fun
user2rb = random.getrandbits(256)

# Sent to User 1
U = applydoubleaddmethod(G=G, k=user2rb)

# Kept secret for encryption
T = applydoubleaddmethod(G=user1kq, k=user2rb)
k1, k2 = derivekeys(T)


messageInput = input("Please enter a message to encrypt:")

# User 2 uses k1 to encrypt a message and to obtain c
user2obj = AES.new(k1)  #####THIS THE ERROR, IT IS a POSITIONAL THING IN MODE, and I can't solve it.
c = base64.b64encode(user2obj.encrypt(messageInput))

r = findmac(c, k2)
#User 1 recieves U and finds userKa x U
tPrime = applydoubleaddmethod(G=U, k=user1ka)

# User 1 obtains the keys
k1Prime, k2Prime = derivekeys(tPrime)

assert r == findmac(c, k2Prime)

user1obj = AES.new(k1Prime)
plaintext = user1obj.decrypt(base64.b64decode(c))

print("The message User B sent to User A is: ", plaintext)
