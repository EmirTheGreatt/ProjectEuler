from math import sqrt
from functools import reduce


def fact(n):
    if n == 1:
        return []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return [i]+fact(n//i)
    return [n]


def d(n):
    l2 = fact(n)
    l1 = list(set(l2))
    t = [0]*len(l1)
    thedict = {i: l2.count(i) for i in l1}
    somme = 0
    while t[0] <= thedict[l1[0]]:
        somme += reduce((lambda x, y: x*y),
                        [l1[i]**t[i] for i in range(len(l1))])
        t[-1] += 1
        for i in range(-1, -len(t), -1):
            t[i-1] += t[i]//(thedict[l1[i]]+1)
            t[i] %= (thedict[l1[i]]+1)
    return somme-n


listo = set()
somme = 0
for i in range(2, 10001):
    if i not in listo:
        if d(i) != 1:
            if (i != d(i)) and (i == d(d(i))):
                listo.add(i)
                listo.add(d(i))
print(sum(listo))
print(listo)
