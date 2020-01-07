
import os

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

if __name__ == '__main__':

    # encrypt
    data = b'secret message?'
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv

    # decrypt
    decryptor = AES.new(key, AES.MODE_CBC, iv)
    dt_bytes = unpad(decryptor.decrypt(ct_bytes), AES.block_size)
    print(dt_bytes)

