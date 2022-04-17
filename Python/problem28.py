def compute():
    SIZE = 1001
    ans = 1
    ans += sum([4 * i * i - 6 * (i - 1) for i in range(3, SIZE + 1, 2)])
    return str(ans)


print(compute())
