import networkx as nx

with open("day9input.txt") as f:
    file = f.read().splitlines()

deltas = ((0, -1), (0, 1), (-1, 0), (1, 0))
total = 0

for i in range(len(file)):
    for j in range(len(file[i])):
        low = True
        for d in deltas:
            x, y = i + d[0], j + d[1]
            if 0 <= y < len(file[0]) and 0 <= x < len(file):
                if file[x][y] <= file[i][j]:
                    low = False
        if low:
            total += int(file[i][j]) + 1

print(total)

room, G = file, nx.Graph()
for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] != "9":
            G.add_edge((j, i), (j, i))
            for d in deltas:
                x = j + d[0]
                y = i + d[1]
                if 0 <= y < len(room) and 0 <= x < len(room[0]) and room[y][x] != "9":
                    G.add_edge((j, i), (x, y))


basins = sorted([len(i) for i in list(nx.connected_components(G))])
print(basins[-1] * basins[-2] * basins[-3])
