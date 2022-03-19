# wha do you think I am a grammar teacher
numsineng = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
             6: "six", 7: "seven", 8: "eight",
             9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
             14: "fourteen", 15: "fifteen",
             16: "sixteen", 17: "seventeen", 18: "eigtheen", 19: "nineteen",
             20: "twenty",
             30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy",
             80: "eigthy",
             90: "ninety", 100: "hundred", 1000: "thousand"}


def stringize(n):
    if n == 1000:
        return "one thousand"
    if n <= 20:
        return numsineng[n]
    if n < 100:
        return (numsineng[n-(n % 10)]+" "+numsineng[n % 10]).strip()
    if n % 100 == 0:
        return stringize(n//100)+" "+"hundred"
    return stringize(n-n % 100)+" and "*int(bool(stringize(n % 100)))+stringize(n % 100)


def summ(s):
    res = 0
    for i in str(s):
        if i != " ":
            res += 1
    return res


somme = 0
for i in range(1, 1001):
    somme += summ(stringize(i))
print(somme)
print(stringize(1000))
