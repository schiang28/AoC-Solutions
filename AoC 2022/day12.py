import networkx as nx

with open("day12input.txt") as f:
    file = [list(i) for i in f.read().splitlines()]
lvls, deltas = "SabcdefghijklmnopqrstuvwxyzE", [(0,1), (1,0), (-1,0), (0,-1)]
starts, S, E, G, minpath = [], (), (), nx.DiGraph(), 500

for r in range(len(file)):
    for c in range(len(file[r])):
        if file[r][c] == "a":
            starts.append((r, c))
        if file[r][c] == "E":
            E = (r, c)
        if file[r][c] == "S":
            S = (r, c)
        for d in deltas:
            dr, dc, current = r + d[0], c + d[1], file[r][c]
            if 0 <= dr < len(file) and 0 <= dc < len(file[r]):
                if (
                    (current == "S" and (file[dr][dc] == "a" or file[dr][dc] == "b")) or
                    (current == "E" or current == "y") or
                    (lvls.index(file[dr][dc]) <= lvls.index(current) + 1)
                ):
                    G.add_edge((r, c), (dr, dc))

for start in starts:
    try:
        minpath = min(minpath, len(nx.shortest_path(G, source=start, target=E))-1)
    except:
        pass

print(len(nx.shortest_path(G, source=S, target=E))-1)
print(minpath)