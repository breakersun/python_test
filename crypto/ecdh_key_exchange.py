from tinyec import registry
import secrets

def compress(pubKey):
    return hex(pubKey.x) + hex(pubKey.y % 2)[2:]

curve = registry.get_curve('brainpoolP256r1')

alicePrivKey = secrets.randbelow(curve.field.n)
alicePubKey = alicePrivKey * curve.g
print('Alice Pubkey : ', compress(alicePubKey))

bobPrivKey = secrets.randbelow(curve.field.n)
bobPubKey = bobPrivKey * curve.g
print('Bob Pubkey : ', compress(bobPubKey))

print('Now exchange pubkeys...')

aliceSharedKey = alicePrivKey * bobPubKey
print('Alice shared key ', compress(aliceSharedKey))
bobSharedKey = bobPrivKey * alicePubKey
print('Bob shared key ', compress(bobSharedKey))