from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from coincurve import PrivateKey

# in terminal: eciespy -h
# this shows help
# eciespy -g
# generates eth key

eth_k = generate_eth_key()
sk_hex = eth_k.to_hex()  # hex string
pk_hex = eth_k.public_key.to_hex()  # hex string
data = b'this is a test'
decrypt(sk_hex, encrypt(pk_hex, data))
b'this is a test'
secp_k = generate_key()
sk_bytes = secp_k.secret  # bytes
pk_bytes = secp_k.public_key.format(True)  # bytes
decrypt(sk_bytes, encrypt(pk_bytes, data))
b'this is a test'

# Coincurve
k1 = PrivateKey.from_int(3)
k2 = PrivateKey.from_int(2)
k1.public_key.format(False).hex()
k2.public_key.format(False).hex()
k1.ecdh(k2.public_key.format()).hex()
k2.ecdh(k1.public_key.format().hex())
