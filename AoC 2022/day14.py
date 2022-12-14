with open("day14input.txt") as f:
    file = [i.split(" -> ") for i in f.read().splitlines()]
file = [[tuple(map(int, i.split(","))) for i in j] for j in file]
maxy, blocked, sx, sy, grain = max([max([j[1] for j in i]) for i in file]), set(), 500, 0, 0

for p in file:
    for c in range(len(p) - 1):
        if p[c][0] == p[c + 1][0]: # vertical path
            for k in range(min(p[c][1], p[c + 1][1]), max(p[c][1], p[c + 1][1]) + 1):
                blocked.add((p[c][0], k))
        else: # horizontal path
            for k in range(min(p[c][0], p[c + 1][0]), max(p[c][0], p[c + 1][0]) + 1):
                blocked.add((k, p[c][1]))

while True:
    end = False
    while True:
        if (sx, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx, sy + 1
        elif (sx - 1, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx - 1, sy + 1
        elif (sx + 1, sy + 1) not in blocked and sy + 1 < maxy + 2:
            sx, sy = sx + 1, sy + 1
        else:
            blocked.add((sx,sy))
            if sx == 500 and sy == 0:
                end = True
            sx, sy, grain = 500, 0, grain + 1
            break
    if end:
        break

print(grain)