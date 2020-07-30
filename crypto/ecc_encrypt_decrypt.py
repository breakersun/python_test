import secrets
from tinyec import registry

curve = registry.get_curve('brainpoolP256r1')

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_encryption_keys(pubKey):
    cipherPrivKey = secrets.randbelow(curve.field.n)
    cipherPubKey = cipherPrivKey * curve.g
    sharedECCKey = pubKey * cipherPrivKey
    return(sharedECCKey, cipherPubKey)

def ecc_calc_decryption_key(privKey, cipherPubKey):
    return (privKey * cipherPubKey)

privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g

print("private key:", hex(privKey))
print("public key:", compress_point(pubKey))

(encryptKey, ciphertextPubKey) = ecc_calc_encryption_keys(pubKey)
print("ciphertext pubKey:", compress_point(ciphertextPubKey))
print("encryption key:", compress_point(encryptKey))

decryptKey = ecc_calc_decryption_key(privKey, ciphertextPubKey)
print("decryption key:", compress_point(decryptKey))

