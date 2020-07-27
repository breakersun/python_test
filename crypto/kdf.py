from backports.pbkdf2 import pbkdf2_hmac
import binascii, time

salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
password = 'p@$Sw0rD~1'.encode('utf-8')
start_time = time.time()
key = pbkdf2_hmac('sha256', password, salt, 50000, 32)
end_time = time.time()

print('Derived key:', binascii.hexlify(key))
print('Excution time: %s Seconds', end_time - start_time)