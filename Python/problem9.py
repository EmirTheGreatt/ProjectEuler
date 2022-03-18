for i in range(1, 1001):
    for k in range(1, i+1):
        for j in range(1, k+1):
            if i+k+j == 1000 and k**2+j**2 == i**2:
                print(i*j*k)
