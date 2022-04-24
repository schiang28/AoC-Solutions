import re

with open("day17input.txt") as f:
    minx, maxx, miny, maxy = [int(i) for i in re.findall("-*\d+", f.read())]

maxheight, count = 0, 0
for i in range(maxx + 1):  # no -ve vx; would just get further away from target ∞
    for j in range(miny - 1, -miny + 1):
        vx, vy, x, y, peak = i, j, 0, 0, 0
        while True:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            vy -= 1
            peak = max(peak, y)
            if minx <= x <= maxx and miny <= y <= maxy:
                maxheight = max(maxheight, peak)
                count += 1
                break
            if x > maxx or y < miny:
                break

print(maxheight)
print(count)
