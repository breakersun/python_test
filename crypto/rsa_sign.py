import binascii
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

keypair = RSA.generate(1024)
pubkey = keypair.publickey()

msg = b'message for signing'
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(keypair)
sign = signer.sign(hash)
print('Signature:', binascii.hexlify(sign))

msg = b'message for signing'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubkey)
try:
    verifier.verify(hash, sign)
    print('Signature is valid')
except:
    print('Signa')

msg = b'tampered message for signing'
hash = SHA256.new(msg)
verifier = PKCS115_SigScheme(pubkey)
try:
    verifier.verify(hash, sign)
    print('Signature is valid')
except:
    print('Signature is invalid')