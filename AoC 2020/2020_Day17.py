inpt = '''
...#..#.
#..#...#
.....###
##....##
......##
........
.#......
##...#..'''

num = inpt.split()
m = [(x, y, 0) for y, line in enumerate(num) for x, ch in enumerate(line) if ch == '#']

#PART 1

for _ in range(6):
    act = {}
    new_map = []
    for x, y, z in m:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if dx == dy == dz == 0:
                        continue
                    elif (x + dx, y + dy, z + dz) in act:
                        act[(x + dx, y + dy, z + dz)] += 1
                    else:
                        act[(x + dx, y + dy, z + dz)] = 1
    #print(act)
    for i in act:
        if i not in m and act[i] == 3:
            new_map.append(i)
        elif i in m and act[i] in [2, 3]:
            new_map.append(i)

    m = new_map
print('p1', len(m))

num = inpt.split()
m = [(x, y, 0, 0) for y, line in enumerate(num) for x, ch in enumerate(line) if ch == '#']

for _ in range(6):
    act = {}
    new_map = []
    for x, y, z, w in m:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if dx == dy == dz == dw == 0:
                            continue
                        elif (x + dx, y + dy, z + dz, w + dw) in act:
                            act[(x + dx, y + dy, z + dz, w + dw)] += 1
                        else:
                            act[(x + dx, y + dy, z + dz, w + dw)] = 1

    for i in act:
        if i not in m and act[i] == 3:
            new_map.append(i)
        elif i in m and act[i] in [2, 3]:
            new_map.append(i)

    m = new_map
print('p2', len(m))
