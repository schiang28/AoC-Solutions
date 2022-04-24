import networkx as nx
from collections import deque

with open("day12input.txt") as f:
    cave = nx.Graph([i.split("-") for i in f.read().splitlines()])
start = ("start", set(["start"]), False)
ans, Q, checktwice = 0, deque([start]), True

while Q:
    current, small, twice = Q.popleft()
    if current == "end":
        ans += 1
        continue
    for c in cave[current]:
        if c not in small:
            nsmall = set(small)
            if c.islower():
                nsmall.add(c)
            Q.append((c, nsmall, twice))
        if c in small and not twice and c not in ["start", "end"] and checktwice:
            Q.append((c, small, True))
print(ans)
