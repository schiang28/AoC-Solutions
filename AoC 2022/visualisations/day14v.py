import os
from termcolor import colored

with open("day14input.txt") as f:
    file = [i.split(" -> ") for i in f.read().splitlines()]
file = [[tuple(map(int, i.split(","))) for i in j] for j in file]
blocked, sx, sy, grain = set(), 500, 0, 0
minx,miny,maxx,maxy = 1000,1000,0,0

for i in file:
    for j in file:
        minx = min(minx, min([k[0] for k in j]))
        miny = min(miny, min([k[1] for k in j]))
        maxx = max(maxx, max([k[0] for k in j]))
        maxy = max(maxy, max([k[1] for k in j]))


for p in file:
    for c in range(len(p) - 1):
        if p[c][0] == p[c + 1][0]: # vertical path
            for k in range(min(p[c][1], p[c + 1][1]), max(p[c][1], p[c + 1][1]) + 1):
                blocked.add((p[c][0], k))
        else: # horizontal path
            for k in range(min(p[c][0], p[c + 1][0]), max(p[c][0], p[c + 1][0]) + 1):
                blocked.add((k, p[c][1]))

cave = []
x = 300
for i in range(maxy+3):
    temp = []
    for j in range(x, 700):
        if i==maxy+2:
            temp.append(colored("#", "blue"))
        elif (j, i ) in blocked:
            temp.append(colored("#", "red"))
        else:
            temp.append(" ")
    cave.append(temp)

clear = "cls"
if os.name =="posix":
    clear = "clear"
os.system(clear)

while True:
    end = False
    while True:
        if (sx, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx, sy + 1
            if cave[sy][sx-x] == " ":
                cave[sy][sx-x] = colored("o", "yellow")
                os.system(clear)
                for i in cave:
                    print("".join(i))
        elif (sx - 1, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx - 1, sy + 1
            if cave[sy][sx-x] == " ":
                cave[sy][sx-x] = colored("o", "yellow")
                os.system(clear)
                for i in cave:
                    print("".join(i))
        elif (sx + 1, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx + 1, sy + 1
            if cave[sy][sx-x] == " ":
                cave[sy][sx-x] = colored("o", "yellow")
                os.system(clear)
                for i in cave:
                    print("".join(i))
        else:
            blocked.add((sx,sy))
            if sx == 500 and sy == 0:
                end = True
            sx, sy, grain = 500, 0, grain + 1
            break
    if end:
        break

print(grain)