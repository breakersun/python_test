
from tinyec import registry
import secrets
from nummaster.basic import sqrtmod

def compress(point):
    return (point[0], point[1] % 2)

def uncompress_point(compressed_point, p, a, b):
    x, is_odd = compressed_point
    y = sqrtmod(pow(x, 3, p) + a * x + b, p)
    if bool(is_odd) == bool(y & 1):
        return (x, y)
    return (x, p - y)

curve = registry.get_curve('secp192r1')
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g
print('privateKey : ', privKey)
print('pubKey : ', pubKey)

p, a, b = 17, 0, 7
point = (10, 15)
print(f"original point = {point}")
compressed_p = compress(point)
print(f"compressed = {compressed_p}")
restored_p = uncompress_point(compressed_p, p, a, b)
print(f"uncompressed = {restored_p}")
