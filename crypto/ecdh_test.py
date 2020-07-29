import pyDHE

alice = pyDHE.new(group = 14)
alicePubkey = alice.getPublicKey()
print('Alice pub key:', alicePubkey)

bob = pyDHE.new(group = 14)
bobPubkey = bob.getPublicKey()
print('Bob pub key:', bobPubkey)

print('Exchange over Internet...done')

aliceSharedkey = alice.update(bobPubkey)
print('Alice shared key:', hex(aliceSharedkey))

bobSharedKey = bob.update(alicePubkey)
print('Bob shared key:', hex(bobSharedKey))