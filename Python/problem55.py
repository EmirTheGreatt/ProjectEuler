# a program that finds lychrel numbers under 10000
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(n):
            return False
    return True


lychrel_numbers = []
for i in range(10000):
    if lychrel(i):
        lychrel_numbers.append(i)
print(len(lychrel_numbers))
