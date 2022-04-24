import re
from collections import Counter

with open("day22input.txt") as f:
    file = f.read().splitlines()


def part1(x1, x2, y1, y2, z1, z2):
    if (
        ((x1 < -50 or x1 > 50) and (x2 < -50 or x2 > 50))
        or ((y1 < -50 or y1 > 50) and (y2 < -50 or y2 > 50))
        or ((z1 < -50 or z1 > 50) and (z2 < -50 or z2 > 50))
    ):
        return True
    return False


def part2(p1=False):
    cuboids = Counter()
    for i in file:
        instruct = 1 if i.split()[0] == "on" else -1
        x1, x2, y1, y2, z1, z2 = map(int, re.findall("-*\d+", i))
        if p1:
            if part1(x1, x2, y1, y2, z1, z2):
                continue
        cuboid = Counter()

        for k, v in cuboids.items():
            nx1, nx2, ny1, ny2, nz1, nz2 = k
            minx, maxx = max(nx1, x1), min(nx2, x2)
            miny, maxy = max(ny1, y1), min(ny2, y2)
            minz, maxz = max(nz1, z1), min(nz2, z2)

            if minx <= maxx and miny <= maxy and minz <= maxz:
                cuboid[(minx, maxx, miny, maxy, minz, maxz)] -= v
        if instruct == 1:
            cuboid[(x1, x2, y1, y2, z1, z2)] += 1

        cuboids.update(cuboid)

    ans = sum(
        (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * v
        for (x1, x2, y1, y2, z1, z2), v in cuboids.items()
    )
    print(ans)


part2(p1=True)
part2()