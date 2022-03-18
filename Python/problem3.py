from math import sqrt


def solve(s):
    if s == 1:
        return 1
    for i in range(2, int(sqrt(s)) + 1):
        if s % i == 0:
            return max(i, solve(s // i))
    return s


print(solve(600851475143))
