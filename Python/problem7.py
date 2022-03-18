import numpy as np
primes = np.empty(10001, dtype=int)
ind = 2
p = 0
while p <= 10000:
    if 0 in ind % primes[:p]:
        ind += 1
        continue
    primes[p] = ind
    p += 1
    ind += 1
print(primes[-1])
