def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def calc(a, b):
    return lambda x: x**2+a*x+b


def longest_seq(f):
    ind = 0
    while is_prime(f(ind)):
        ind += 1
    return ind


maxx = 0
inds = 0, 0
for i in range(-999, 1000):
    for j in range(-1000, 1001):
        longest = longest_seq(calc(i, j))
        if longest >= maxx:
            inds = i, j
            maxx = longest
print(inds[0]*inds[1])
print(inds)
