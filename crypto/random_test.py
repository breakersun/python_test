import random, time
import secrets
import hashlib

random.seed(time.time())
r1 = random.randrange(1e49, 1e50-1)
random.seed(time.time())
r2 = random.randrange(1e49, 1e50-1)

# print(r1)
# print(r2)
# print(secrets.randbelow(int(1e50)))

startSeed = str(time.time()) + '|'
print(startSeed)
min = 10
max = 20
for i in range(5):
    nextSeed = startSeed + str(i)
    hash = hashlib.sha256(nextSeed.encode('ascii')).digest()
    bigRand = int.from_bytes(hash, 'big')
    rand = min + bigRand % (max - min + 1)
    print(nextSeed, bigRand, '-->', rand)