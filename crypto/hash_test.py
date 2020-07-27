import hashlib, binascii

if __name__ == "__main__":
    text = 'hello'
    data = text.encode('utf-8')
    sha256hash = hashlib.sha256(data).digest()
    sha224hash = hashlib.sha224(data).digest()
    sha3_224hash = hashlib.sha3_224(data).digest()
    sha3_256hash = hashlib.sha3_256(data).digest()
    print('SHA224:      ', binascii.hexlify(sha224hash))
    print('SHA256:      ', binascii.hexlify(sha256hash))
    print('SHA3-224:    ', binascii.hexlify(sha3_224hash))
    print('SHA3-256:    ', binascii.hexlify(sha3_256hash))
