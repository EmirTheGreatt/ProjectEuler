import numpy as np
primes = np.ones(2000002, dtype=np.int64)
for i in range(2, len(primes)):
    if primes[i] != 0:
        primes[i] = i
        for k in range(i+i, len(primes), i):
            primes[k] = 0
primes = primes[primes > 1]
summ = 0
for i in primes:
    summ += i
print(summ)
