from math import sqrt
def tri(n): return n*(n+1)//2


def fact(n):
    if n == 1:
        return []
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return [i]+fact(n//i)
    return [n]


def ndivs(n):
    res = 1
    thelist = fact(n)
    theset = set(thelist)
    for i in theset:
        res *= thelist.count(i)+1
    return res


numberofdivisors = 0
ind = 1
while numberofdivisors < 500:
    ind += 1
    numberofdivisors = ndivs(tri(ind))
print(ind)
print(tri(ind))
