def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)


f = factorial
print(f(40)/f(20)**2)
