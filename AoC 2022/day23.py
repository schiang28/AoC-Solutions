with open("day23input.txt") as f:
    file = f.read().splitlines()
elves, delta, proposed, f, num = [], [(1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1)], {}, (face := "NSWE")[0], 1
direction = {"N":[(0,-1), (1,-1), (-1,-1)], "S":[(0,1), (1,1), (-1,1)],"W":[(-1,0), (-1,1), (-1,-1)], "E":[(1,0), (1,1), (1,-1)]}

for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] == "#":
            elves.append((j,i))

while True:
    print(num)
    proposed = {}
    for elf in elves:
        empty = True
        for d in delta:
            if (elf[0] + d[0], elf[1] + d[1]) in elves:
                empty = False
        if empty:
            continue
        if all((elf[0] + check[0], elf[1] + check[1]) not in elves for check in direction[f]):
            proposed[(elf[0], elf[1])] = (elf[0] + direction[f][0][0], elf[1] + direction[f][0][1])
            continue
        tf = face[(face.index(f) + 1) % 4]
        if all((elf[0] + check[0], elf[1]+check[1]) not in elves for check in direction[tf]):
            proposed[(elf[0], elf[1])] = (elf[0] + direction[tf][0][0], elf[1] + direction[tf][0][1])
            continue
        tf = face[(face.index(f) + 2) % 4]
        if all((elf[0] + check[0], elf[1] + check[1]) not in elves for check in direction[tf]):
            proposed[(elf[0], elf[1])] = (elf[0] + direction[tf][0][0], elf[1] + direction[tf][0][1])
            continue
        tf = face[(face.index(f) + 3) % 4]
        if all((elf[0] + check[0], elf[1] + check[1]) not in elves for check in direction[tf]):
            proposed[(elf[0], elf[1])] = (elf[0] + direction[tf][0][0], elf[1] + direction[tf][0][1])
            continue
    moved = False
    for k, v in proposed.items():
        if list(proposed.values()).count(v) == 1:
            moved = True
            elves.remove(k)
            elves.append(v)
    if not moved:
        print(num)
        break
    num += 1
    f = face[(face.index(f) + 1) % 4]

maxx = max([i[0] for i in elves])
maxy = max([i[1] for i in elves])
minx = min([i[0] for i in elves])
miny = min([i[1] for i in elves])

area = (maxx - minx + 1) * (maxy - miny + 1)
print(area - len(elves))
