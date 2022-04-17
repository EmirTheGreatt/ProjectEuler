# Purpose: Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
def get_cycle(d):
    remainders = {}
    remainder = 1
    while remainder not in remainders:
        remainders[remainder] = True
        remainder *= 10
        remainder %= d
    return len(remainders)


def main():
    max_cycle = 0
    max_d = 0
    for d in range(1, 1000):
        cycle = get_cycle(d)
        if cycle > max_cycle:
            max_cycle = cycle
            max_d = d
    print(max_d)


main()
