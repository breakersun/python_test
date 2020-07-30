from nacl.public import PrivateKey
import binascii

privKey = PrivateKey.generate()
pubKey = privKey.public_key

print(binascii.hexlify(bytes(privKey)))
print(binascii.hexlify(bytes(pubKey)))