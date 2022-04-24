import networkx as nx

with open("day15input.txt") as f:
    file = [list(map(int, i)) for i in f.read().splitlines()]
deltas, size = ((0, 1), (1, 0), (-1, 0), (0, -1)), len(file)


def shortest_path(file, size):
    cave = nx.DiGraph()
    for i in range(len(file)):
        for j in range(len(file[i])):
            for d in deltas:
                dy, dx = i + d[0], j + d[1]
                if 0 <= dy < size and 0 <= dx < size:
                    cave.add_edge((i, j), (dy, dx), weight=file[dy][dx])
    print(nx.dijkstra_path_length(cave, (0, 0), (size - 1, size - 1), weight="weight"))


shortest_path(file, size)

for _ in range(4):
    for i in file:
        i.extend([j + 1 if j < 9 else 1 for j in i[-size:]])
for _ in range(4):
    for i in file[-size:]:
        file.append([j + 1 if j < 9 else 1 for j in i])

shortest_path(file, len(file))