import os, binascii, pbkdf2, secrets, pyaes

# Derive a 256-bit AES encryption key from the password
password = 's3cr3t*c0d3'
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption Key : ', binascii.hexlify(key))

# Encrypt the plaintext with the given key
#  ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
# iv = secrets.randbits(256)
iv = os.urandom(16)
plaintext = 'plain text111111'
# aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
aes = pyaes.AESModeOfOperationCBC(key, iv)
ciphertext = aes.encrypt(plaintext)
print('Ciphertext : ', binascii.hexlify(ciphertext))

# Decrypt the ciphertext with the given key
#  plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
# aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
aes = pyaes.AESModeOfOperationCBC(key, iv)
decryptedtext = aes.decrypt(ciphertext)
print('Decrypted : ', decryptedtext)