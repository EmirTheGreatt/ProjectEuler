def f(n):
    if n == 0:
        return 1
    return n*f(n-1)


print(sum([int(i) for i in str(f(100))]))
