import random, time
import secrets
import hashlib
import binascii

random.seed(time.time())
r1 = random.randrange(1e49, 1e50-1)
random.seed(time.time())
r2 = random.randrange(1e49, 1e50-1)

# print(r1)
# print(r2)
# print(secrets.randbelow(int(1e50)))

entropy = ''
for i in range(5):
    s = input("Enter Something[" + str(i + 1) + 'of 5]:')
    entropy = entropy + s + '|' + str(time.time()) + '|'

print("Entropy:", entropy)
startSeed = str(binascii.hexlify(hashlib.sha256(entropy.encode('ascii')).digest()))[2:-1]
print('Start seed = SHA-256(entopy) = ', startSeed)

# startSeed = str(time.time()) + '|'
# print(startSeed)
min = 10
max = 20
for i in range(5):
    nextSeed = startSeed + str(i)
    hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
    bigRand = int.from_bytes(hash, 'big')
    rand = min + bigRand % (max - min + 1)
    print(nextSeed, bigRand, '-->', rand)