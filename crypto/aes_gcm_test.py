import os, binascii
from Crypto.Cipher import AES

def encrypt(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt(encryptedMsg, secretKey):
    (ciphertext, nonce, autTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, autTag)
    return plaintext

secretKey = os.urandom(32) # 256-bit random encrytion key
print('Encryption key : ', binascii.hexlify(secretKey))

msg = b'plain text message'
encryptedMsg = encrypt(msg, secretKey)
print('encryptedMsg', {'ciphertext' : binascii.hexlify(encryptedMsg[0]),
                       'aesIV' : binascii.hexlify(encryptedMsg[1]),
                       'authTag' : binascii.hexlify(encryptedMsg[2])})

decryptMsg = decrypt(encryptedMsg, secretKey)
print('decryptedMsg : ', decryptMsg)