f1 = 1
f2 = 1
summ = 0
while f2 < 4000000:
    f1, f2 = f2, f1+f2
    if f2 % 2 == 0:
        summ += f2
print(f"toplam: {summ}")
