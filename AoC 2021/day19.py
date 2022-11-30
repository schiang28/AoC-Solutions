from itertools import groupby, combinations
from collections import Counter, deque

with open("day19input.txt") as f:
    file = f.read().splitlines()
file = [list(g) for k, g in groupby(file, key=bool) if k]

for i in file:
    del i[0]
for i in range(len(file)):
    for j in range(len(file[i])):
        x, y, z = file[i][j].split(",")
        file[i][j] = (int(x), int(y), int(z))

beacons = []
operations = ["+++"]
scanner = {0: (0, 0, 0)}
deltas = [
    ("-0", "-1", "-2"),
    ("-0", "-2", "-1"),
    ("-1", "-0", "-2"),
    ("-1", "-2", "-0"),
    ("-2", "-0", "-1"),
    ("-2", "-1", "-0"),
    ("-0", "-1", "2"),
    ("-0", "2", "-1"),
    ("-1", "-0", "2"),
    ("-1", "2", "-0"),
    ("2", "-0", "-1"),
    ("2", "-1", "-0"),
    ("-0", "1", "-2"),
    ("-0", "-2", "1"),
    ("1", "-0", "-2"),
    ("1", "-2", "-0"),
    ("-2", "-0", "1"),
    ("-2", "1", "-0"),
    ("-0", "1", "2"),
    ("-0", "2", "1"),
    ("1", "-0", "2"),
    ("1", "2", "-0"),
    ("2", "-0", "1"),
    ("2", "1", "-0"),
    ("0", "-1", "-2"),
    ("0", "-2", "-1"),
    ("-1", "0", "-2"),
    ("-1", "-2", "0"),
    ("-2", "0", "-1"),
    ("-2", "-1", "0"),
    ("0", "-1", "2"),
    ("0", "2", "-1"),
    ("-1", "0", "2"),
    ("-1", "2", "0"),
    ("2", "0", "-1"),
    ("2", "-1", "0"),
    ("0", "1", "-2"),
    ("0", "-2", "1"),
    ("1", "0", "-2"),
    ("1", "-2", "0"),
    ("-2", "0", "1"),
    ("-2", "1", "0"),
    ("0", "1", "2"),
    ("0", "2", "1"),
    ("1", "0", "2"),
    ("1", "2", "0"),
    ("2", "0", "1"),
    ("2", "1", "0"),
]


def overlapp(a, b):
    for d in deltas:
        differences = Counter()
        for j in range(len(file[a])):
            for i in range(len(file[b])):
                o = [
                    file[b][i][int(d[0][-1])],
                    file[b][i][int(d[1][-1])],
                    file[b][i][int(d[2][-1])],
                ]
                for neg in range(len(o)):
                    if len(d[neg]) == 2:
                        o[neg] = o[neg] * -1
                diff = tuple([file[a][j][c] - o[c] for c in range(3)])
                differences[diff] += 1

        for k, v in differences.items():
            if v >= 12:
                operation = ""
                for o in d:
                    if len(o) == 2:
                        operation += "-"
                    else:
                        operation += "+"

                x, y, z = scanner[a]
                coord = tuple(
                    [
                        eval(str(x) + operations[-1][0] + str(k[0])),
                        eval(str(y) + operations[-1][1] + str(k[1])),
                        eval(str(z) + operations[-1][2] + str(k[2])),
                    ]
                )
                operations.append(operation)
                scanner[b] = coord
                print(operation, k)
                for n in file[b]:
                    absd = tuple(
                        [
                            eval(str(k[0]) + operation[0] + str(n[0])),
                            eval(str(k[1]) + operation[1] + str(n[1])),
                            eval(str(k[2]) + operation[2] + str(n[2])),
                        ]
                    )
                    if absd in file[a]:
                        beacons.append(absd)


# for i in range(len(file)):
#     for j in range(i, len(file)):
#         overlapp(i, j)
# print(scanner)
# print(len(beacons))


def scanit(scan, rebased0):
    for rot, rot_scan in rotations(scan).items():
        rebased = {p1: {psub(p1, p2) for p2 in rot_scan} for p1 in rot_scan}
        for p1, p2 in [(p1, p2) for p1 in rebased0 for p2 in rebased]:
            if len(rebased0[p1] & rebased[p2]) > 11:
                return p1, p2, rot


def make_absolute(scanners):
    scanner_locs = {(0, 0, 0)}
    task_list = deque([*enumerate(scanners[1:], start=1)])
    while task_list:
        i, scan = task_list.popleft()
        rebased0 = {p1: {psub(p1, p2) for p2 in scanners[0]} for p1 in scanners[0]}
        result = scanit(scan, rebased0)
        if result == None:
            task_list.append((i, scanners[i]))
            continue
        p1, p2, rot = result
        scanner_locs.add(padd((0, 0, 0), psub(p1, p2)))
        for s in scan:
            x = rotate(s, *rot)
            x = padd(x, psub(p1, p2))
            if x not in rebased0[p1]:
                scanners[0].add(x)
    return len(scanners[0]), scanner_locs


def psub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1], p1[2] - p2[2]


def padd(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1], p1[2] + p2[2]


def rotate(s, a, b, c, i, j, k):
    return (a * s[i], b * s[j], c * s[k])


def rotations(scan):
    return {r: {rotate(s, *r) for s in scan} for r in orientations}


orientations = [
    (1, 1, 1, 0, 1, 2),
    (1, 1, 1, 1, 2, 0),
    (1, 1, 1, 2, 0, 1),
    (1, 1, -1, 2, 1, 0),
    (1, 1, -1, 1, 0, 2),
    (1, 1, -1, 0, 2, 1),
    (1, -1, -1, 0, 1, 2),
    (1, -1, -1, 1, 2, 0),
    (1, -1, -1, 2, 0, 1),
    (1, -1, 1, 2, 1, 0),
    (1, -1, 1, 1, 0, 2),
    (1, -1, 1, 0, 2, 1),
    (-1, 1, -1, 0, 1, 2),
    (-1, 1, -1, 1, 2, 0),
    (-1, 1, -1, 2, 0, 1),
    (-1, 1, 1, 2, 1, 0),
    (-1, 1, 1, 1, 0, 2),
    (-1, 1, 1, 0, 2, 1),
    (-1, -1, 1, 0, 1, 2),
    (-1, -1, 1, 1, 2, 0),
    (-1, -1, 1, 2, 0, 1),
    (-1, -1, -1, 2, 1, 0),
    (-1, -1, -1, 1, 0, 2),
    (-1, -1, -1, 0, 2, 1),
]

beacons, scanner_locs = make_absolute(
    [
        {eval(line) for line in scanner.splitlines() if "--" not in line}
        for scanner in open("day19input.txt").read().split("\n\n")
    ]
)
print(beacons)

ans = []
for a, b in combinations(scanner_locs, 2):
    total = 0
    for i in range(3):
        x = abs(a[i] - b[i])
        total += x
    ans.append(total)
print(max(ans))
