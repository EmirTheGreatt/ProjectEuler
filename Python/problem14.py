col = {1: 0, 2: 0, 4: 0}
maxx = 1


def coll(n):
    if n in col:
        return col[n]
    if n % 2 == 0:
        res = 1+coll(n//2)
        col[n] = res
        return res
    res = 1+coll(n*3+1)
    col[n] = res
    return res


for i in range(1, 1000000):
    if coll(i) > col[maxx]:
        maxx = i
print(maxx)
