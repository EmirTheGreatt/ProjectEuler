maxi = 0
maxx = 0
for i in range(100, 1000):
    for k in range(100, 1000):
        numb = i*k
        if numb > maxx and str(numb) == str(numb)[::-1]:
            maxx = numb
            maxi = i, k
print(maxx, maxi)
