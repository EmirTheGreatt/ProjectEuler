# a function that finds all permutations of a list
def perm(l):
    if len(l) == 1:
        return [l]
    else:
        result = []
        for i in range(len(l)):
            x = l[i]
            xs = l[:i] + l[i+1:]
            for p in perm(xs):
                result.append([x] + p)
        return result


perms = perm([1, 2, 3, 6, 7, 8, 9, 0])
with open('p079_keylog.txt') as f:
    keylog = [[int(i) for i in k] for k in f.read().splitlines()]
    print(keylog)
    for i in perms:
        p = 1
        for j in keylog:
            if not (i.index(j[0]) < i.index(j[1]) and i.index(j[1]) < i.index(j[2])):
                p = 0
                break
        if p == 1:
            print(i)
