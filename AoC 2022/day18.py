import networkx as nx

with open("day18input.txt") as f:
    file = [tuple(map(int, i.split(","))) for i in f.read().splitlines()]
area, G = 0, nx.grid_graph(dim=[range(-1, max([i[0] for i in file])+2)] * 3)
outside = G.copy()
outside.remove_nodes_from(file)
steam = nx.node_connected_component(outside, (0, 0, 0))

for i in range(len(file)):
    sides, curr = 6, file[i]
    for j in range(len(file)):
        if i != j:
            c1, c2 = file[i], file[j]
            if ((abs(c1[0]-c2[0]) == 1 and c1[1] == c2[1] and c1[2] == c2[2])
            or (abs(c1[1]-c2[1]) == 1 and c1[0] == c2[0] and c1[2] == c2[2])
            or (abs(c1[2]-c2[2]) == 1 and c1[0] == c2[0] and c1[1] == c2[1])):
                sides -= 1
    area += sides

print(area)
print(len(list(nx.edge_boundary(G, steam))))