import re

with open("day15input.txt") as f:
    file = [re.findall(r"x=(-?\d+), y=(-?\d+)", i) for i in f.read().splitlines()]
S, NB = {tuple(map(int, i[0])): tuple(map(int, i[1])) for i in file}, set()
level, maxxy = 2000000, 4000000

for s,b in S.items():
    d = abs(s[0] - b[0]) + abs(s[1] - b[1])
    length, inc = 0, True
    if s[1]-d <= level <= s[1]+d+1:
        for i in range(s[1] - d, s[1] + d + 1):
            if i == level:
                for j in range(s[0] - length, s[0] + length + 1):
                    coord = (j, i)
                    if coord not in S.keys() and coord not in S.values():
                        NB.add(coord)
            if length >= d:
                inc = False
            if inc:
                length += 1
            else:
                length -= 1

print(len(NB))