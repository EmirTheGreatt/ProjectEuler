from math import sqrt
from numpy import array, prod


def solve(s):
    if s == 1:
        return 1
    for i in range(2, int(sqrt(s)) + 1):
        if s % i == 0:
            return max(i, solve(s // i))
    return s


def factorize(n):
    returned = []
    while n != 1:
        divisor = solve(n)
        returned.append(divisor)
        n //= divisor
    return returned


thePlist = []
for i in range(1, 20):
    factorization = factorize(i)
    for k in factorization:
        fcount = (factorization).count(k)
        Pcount = thePlist.count(k)
        if fcount-Pcount > 0:
            print("yey ", k)
            thePlist += [k]*(fcount-Pcount)
print(thePlist)
print(prod(array(thePlist)))
