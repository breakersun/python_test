import os, binascii, hashlib, secrets
from Crypto.Cipher import AES
from tinyec import registry

def AES_GCM_encrypt(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def AES_GCM_decrypt(encryptedMsg, secretKey):
    (ciphertext, nonce, autTag) = encryptedMsg
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, autTag)
    return plaintext

def encrypt_AES_GCM(msg, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)

def decrypt_AES_GCM(ciphertext, nonce, authTag, secretKey):
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext

def ecc_point_to_256_bit_key(point):
    sha = hashlib.sha256(int.to_bytes(point.x, 32, 'big'))
    sha.update(int.to_bytes(point.y, 32, 'big'))
    return sha.digest()

secretKey = os.urandom(32) # 256-bit random encrytion key
print('Encryption key : ', binascii.hexlify(secretKey))

msg = b'plain text message'
encryptedMsg = AES_GCM_encrypt(msg, secretKey)
print('encryptedMsg', {'ciphertext' : binascii.hexlify(encryptedMsg[0]),
                       'aesIV' : binascii.hexlify(encryptedMsg[1]),
                       'authTag' : binascii.hexlify(encryptedMsg[2])})

decryptMsg = AES_GCM_decrypt(encryptedMsg, secretKey)
print('decryptedMsg : ', decryptMsg)

## ecc
curve = registry.get_curve('brainpoolP256r1')

def encrypt_ecc(msg, pubKey):
    ciphertextPrivKey = secrets.randbelow(curve.field.n)
    ciphertextPubKey = ciphertextPrivKey * curve.g
    sharedECCKey = pubKey * ciphertextPrivKey
    encryptKey = ecc_point_to_256_bit_key(sharedECCKey)
    ciphertext, nonce, authTag = encrypt_AES_GCM(msg, encryptKey)
    return (ciphertext, nonce, authTag, ciphertextPubKey)

def decrypt_ecc(encryptedMsg, privKey):
    (ciphertext, nonce, authTag, ciphertextPubKey) = encryptedMsg
    sharedECCKey = privKey * ciphertextPubKey
    encryptKey = ecc_point_to_256_bit_key(sharedECCKey)
    plaintext = decrypt_AES_GCM(ciphertext, nonce, authTag, encryptKey)
    return plaintext


msg = b'Text to be encrypted by ECC public key and ' \
      b'decrypted by its corresponding ECC private key'
print("original msg:", msg)
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

encryptedMsg = encrypt_ecc(msg, pubKey)
encryptedMsgObj = {
    'ciphertext': binascii.hexlify(encryptedMsg[0]),
    'nonce': binascii.hexlify(encryptedMsg[1]),
    'authTag': binascii.hexlify(encryptedMsg[2]),
    'ciphertextPubKey': hex(encryptedMsg[3].x) + hex(encryptedMsg[3].y % 2)[2:]
}
print("encrypted msg:", encryptedMsgObj)

decryptedMsg = decrypt_ecc(encryptedMsg, privKey)
print("decrypted msg:", decryptedMsg)