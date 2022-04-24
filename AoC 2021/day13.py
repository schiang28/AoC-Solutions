from itertools import groupby
import re
import numpy as np

with open("day13input.txt") as f:
    file = f.read().splitlines()
file = [list(g) for k, g in groupby(file, key=bool) if k]
instructions, folding = [list(map(int, i.split(","))) for i in file[0]], file[1]

maxx, maxy, p1 = 0, 0, True
for i in instructions:
    maxx, maxy = max(maxx, i[0]), max(maxy, i[1])
paper = [["." for _ in range(maxx + 1)] for _ in range(maxy + 1)]

for i in instructions:
    paper[i[1]][i[0]] = "#"

for f in folding:
    t = re.findall("fold along (\w+)=(\d+)", f)
    axis, num = t[0][0], t[0][1]
    if axis == "y":
        flip = np.flipud(np.array(paper[int(num) + 1 :][:]))
        paper = paper[: int(num)][:]
        for y in range(len(flip)):
            for x in range(len(flip[y])):
                if flip[y][x] == "#":
                    paper[y + (len(paper) - len(flip))][x] = "#"
    else:
        flip = [i[::-1] for i in [i[: int(num)] for i in paper]]
        paper = [i[int(num) + 1 :] for i in paper]
        for y in range(len(flip)):
            for x in range(len(flip[y])):
                if flip[y][x] == "#":
                    paper[y][x] = "#"
    if p1:
        print(sum([len([j for j in i if j == "#"]) for i in paper]))
        p1 = False

for i in paper:
    print("".join([j if j == "#" else " " for j in i])[::-1])
