import re

with open("day15input.txt") as f:
    file = [re.findall(r"x=(-?\d+), y=(-?\d+)", i) for i in f.read().splitlines()]
S, NB = {tuple(map(int, i[0])): tuple(map(int, i[1])) for i in file}, set()
distance = {s: abs(s[0] - b[0]) + abs(s[1] - b[1]) for s, b in S.items()}
level, maxxy, c1, c2, bx, by = 2000000, 4000000, set(), set(), 0, 0

for s, b in S.items():
    d = distance[s]
    if s[1] - d <= level <= s[1] + d + 1:
        for i in range(s[1] - d, s[1] + d + 1):
            if i == level:
                length = d - (abs(i - s[1]))
                for j in range(s[0] - length, s[0] + length + 1):
                    coord = (j, i)
                    if coord not in S.keys() and coord not in S.values():
                        NB.add(coord)

[c1.update([s[1] - s[0] + d + 1, s[1] - s[0] - d - 1]) for s, d in distance.items()]
[c2.update([s[0] + s[1] + d + 1, s[0] + s[1] - d - 1]) for s, d in distance.items()]

for i in c1:
    for j in c2:
        ix, iy = (j - i) // 2, (i + j) // 2
        if 0 < ix < maxxy and 0 < iy < maxxy:
            if all(abs(ix-k[0]) + abs(iy-k[1]) > distance[k] for k in S.keys()):
                bx, by = ix, iy

print(len(NB))
print(bx * maxxy + by)