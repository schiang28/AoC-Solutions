from itertools import groupby

with open("day1input.txt") as f:
    file = f.read().splitlines()
snacks = sorted([sum(list(map(int, g))) for k, g in groupby(file, key=bool) if k])

print(snacks[-1])
print(sum(snacks[-3:]))
