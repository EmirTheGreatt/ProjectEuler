num = 2**1000
summ = 0
while num != 0:
    dig = num % 10
    summ += dig
    num -= dig
    num //= 10
print(summ)
