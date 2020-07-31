from Crypto.PublicKey import RSA

keypair = RSA.generate(1024)
print(f'pub key : (n = {hex(keypair.n)}, e = {hex(keypair.e)})')
print(f'private key : (n = {hex(keypair.n)}, d = {hex(keypair.d)})')

msg = b'message for signing'
from hashlib import sha512
hash = int.from_bytes(sha512(msg).digest(), byteorder='big')
sign = pow(hash, keypair.d, keypair.n)
hash_from_sign = pow(sign, keypair.e, keypair.n)
print(sign)
print('Sign valid ', hash == hash_from_sign)
