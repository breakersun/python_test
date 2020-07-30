
from tinyec import registry
import secrets

curve = registry.get_curve('secp192r1')
privKey = secrets.randbelow(curve.field.n)
pubKey = privKey * curve.g
print('privateKey : ', privKey)
print('pubKey : ', pubKey)