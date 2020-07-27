import hmac, hashlib, binascii

def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()

def hmac_sha384(key, msg):
    return hmac.new(key, msg, hashlib.sha384).digest()

# mac = hmac.new(b'key', b'some msg', hashlib.sha256).digest()
# key = b'12345'
# msg = b'sample message'
# print(binascii.hexlify(hmac_sha256(key, msg)))

key = b'cryptography'
msg = b'hello'
print(binascii.hexlify(hmac_sha384(key, msg)))
key = b'again'
msg = b'hello'
print(binascii.hexlify(hmac_sha384(key, msg)))