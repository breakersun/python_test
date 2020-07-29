from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('ascii'))

privatePEM = keyPair.export_key()
print(privatePEM.decode('ascii'))

plaintext = b'a plain text message'
encryptor = PKCS1_OAEP.new(pubKey)
ciphermsg = encryptor.encrypt(plaintext)
print('Encrypted : ', binascii.hexlify(ciphermsg))

decrytor = PKCS1_OAEP.new(keyPair)
decryptedMsg = decrytor.decrypt(ciphermsg)
print('Decrypted : ', decryptedMsg)