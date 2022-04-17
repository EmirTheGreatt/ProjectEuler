import numpy as np
noms = np.arange(1, 28123+1)
noms1 = noms.copy()


# what this function essentially does is to find the sum of all the proper divisors of a number
def divisors(n):
    divs = 0
    for i in range(1, int(np.sqrt(n))+1):
        if n % i == 0:
            divs += i
            if i != 1 and i != n//i:
                divs += n//i
    return divs


for i in noms:
    if divisors(i) <= i:
        noms1[i-1] = 0
noms1 = noms1[noms1 > 0]
for i in noms1:
    for j in noms1:
        if i+j <= 28123:
            noms[i+j-1] = 0
print(sum(noms))
