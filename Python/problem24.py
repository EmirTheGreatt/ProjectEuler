# a function that returns the next permutation of a given list
def find_next(perm):
    # find the largest index k such that perm[k] < perm[k+1]
    k = len(perm) - 2
    while k >= 0 and perm[k] >= perm[k+1]:
        k -= 1
    if k == -1:
        return None
    # find the largest index l such that perm[k] < perm[l]
    l = len(perm) - 1
    while perm[k] >= perm[l]:
        l -= 1
    # swap the value of perm[k] with perm[l]
    perm[k], perm[l] = perm[l], perm[k]
    # reverse the sequence perm[k+1: ]
    perm[k+1:] = perm[len(perm)-1:k:-1]
    return perm


per = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1000000-1):
    per = find_next(per)
print(per)
