
import os

from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

if __name__ == '__main__':
    # readable password to hash
    password = input("Please input a password: ")
    data = input("Please input your message: ")

    # encrypt
    hasher = MD5.new(password.encode('utf-8'))
    key = hasher.digest()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = cipher.iv

    # decrypt
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    dt_bytes = unpad(decryptor.decrypt(ct_bytes), AES.block_size)
    print(dt_bytes)

