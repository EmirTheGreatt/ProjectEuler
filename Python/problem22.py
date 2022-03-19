from string import ascii_uppercase
from re import sub

namesfile = open("../p22_names.txt", "r")
names = namesfile.read()
names = names.split(",")
names = [sub("[\"]", "", i) for i in names]
names.sort()


def score(name): return sum([ascii_uppercase.index(i)+1 for i in name])*(names.index(name)+1)


print(len(names))
print(sum([score(i) for i in names]))
