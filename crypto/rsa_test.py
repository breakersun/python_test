from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

import binascii

key = RSA.importKey(open('public.pem').read())

encryptor = PKCS1_OAEP.new(key)
inputMsg = input('Input Msg : ')
encryptedMsg = encryptor.encrypt(inputMsg.encode('ascii'))
print("Encrypted : ", binascii.hexlify(encryptedMsg))