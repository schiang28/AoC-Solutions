with open("day9input.txt") as f:
    file = [(i.split(" ")[0], int(i.split(" ")[1])) for i in f.read().splitlines()]

ohx, ohy, coords, v1, v2 = 0, 0, {i: (0, 0) for i in range(1, 10)}, [], []
direction = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
deltas = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
move = {
    (2, 0): (1, 0), (2, -1): (1, -1), (2, -2): (1, -1), (1, -2): (1, -1),
    (0, -2): (0, -1), (-1, -2): (-1, -1), (-2, -2): (-1, -1), (-2, -1): (-1, -1),
    (-2, 0): (-1, 0), (-2, 1): (-1, 1), (-2, 2): (-1, 1), (-1, 2): (-1, 1),
    (0, 2): (0, 1), (1, 2): (1, 1), (2, 2): (1, 1), (2, 1): (1, 1),
}


def inrange(tx, ty, hx, hy):
    for d in deltas:
        if tx + d[0] == hx and ty + d[1] == hy:
            return True
    return False


for i in file:
    for step in range(i[1]):
        ohx, ohy = ohx + direction[i[0]][0], ohy + direction[i[0]][1]
        hx, hy = ohx, ohy

        for p, knots in coords.items():
            tx, ty = knots[0], knots[1]
            if not inrange(tx, ty, hx, hy):
                dx, dy = hx - tx, hy - ty
                tx, ty = tx + move[(dx, dy)][0], ty + move[(dx, dy)][1]
            coords[p], hx, hy = (tx, ty), tx, ty

            if p == 1 and (tx, ty) not in v1:
                v1.append((tx, ty))
        if (tx, ty) not in v2:
            v2.append((tx, ty))

print(len(v1))
print(len(v2))
