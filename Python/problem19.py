days = ("Monday", "Tuesday", "wednesday", "thursday",
        "friday", "saturday", "sunday")


# date is a list with the format day,month,year
def inc_date(date):
    newdate = date.copy()
    newdate[0] -= 1
    newdate[1] -= 1
    newdate[0] += 1
    if newdate[1]+1 in {9, 4, 6, 11}:
        newdate[1] += newdate[0]//30
        newdate[0] = newdate[0] % 30
    elif newdate[1]+1 != 2:
        newdate[1] += newdate[0]//31
        newdate[0] = newdate[0] % 31
    else:
        if newdate[2] % 4 != 0:
            newdate[1] += newdate[0]//28
            newdate[0] = newdate[0] % 28
        elif newdate[2] % 100 == 0 and newdate[2] % 400 != 0:
            newdate[1] += newdate[0]//28
            newdate[0] = newdate[0] % 28
        else:
            newdate[1] += newdate[0]//29
            newdate[0] = newdate[0] % 29
    newdate[2] += newdate[1]//12
    newdate[1] = newdate[1] % 12
    newdate[0] += 1
    newdate[1] += 1
    return newdate


somme = 0
ind = 0
date = [1, 1, 1900]
while date[2] != 2001:
    if days[ind] == "sunday" and date[2] > 1900 and date[0] == 1:
        somme += 1
    ind += 1
    ind %= 7
    date = inc_date(date)
print(somme)
