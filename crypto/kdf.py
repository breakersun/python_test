from backports.pbkdf2 import pbkdf2_hmac
import binascii

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
password = 'p@$Sw0rD~1'.encode('utf-8')
key = pbkdf2_hmac('sha256', password, salt, 50000, 32)

print('Derived key:', binascii.hexlify(key))