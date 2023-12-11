with open("day11input.txt") as f:
    file = [list(i) for i in f.read().splitlines()]
exrow, excol, galaxies, total = [], [], [], 0

for i in range(len(file)):
    if all(j == '.' for j in file[i]): exrow.append(i)
    if all(j == "." for j in [file[c][i] for c in range(len(file))]): excol.append(i)
    for j in range(len(file[i])):
        if file[i][j] == "#": galaxies.append((i, j))

for g1 in range(len(galaxies)):
    for g2 in range(g1+1, len(galaxies)):
        g1x, g1y, g2x, g2y = galaxies[g1][0], galaxies[g1][1], galaxies[g2][0], galaxies[g2][1]
        path = abs(g1x - g2x) + abs(g1y - g2y)
        path += sum([999999 if min(g1x, g2x)<=i<=(max(g1x, g2x)) else 0 for i in exrow])
        path += sum([999999 if min(g1y, g2y)<=i<=(max(g1y, g2y)) else 0 for i in excol])
        total += path
    
print(total)