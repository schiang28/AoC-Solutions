import heapq

with open('day17input.txt') as f:
    graph = {i + j*1j: int(b) for i, c in enumerate(f.read().splitlines()) for j, b in enumerate(list(c))}

def travel(minstep, maxstep, count):
    Q, seen = [(0,0,0,1), (0,0,0,1j)], []

    while Q:
        heatloss, _, pos, face = heapq.heappop(Q)
        if (pos == list(graph.keys())[-1]): return heatloss
        if (pos, face) in seen: continue
        seen.append((pos, face))

        for d in 1j/face, -1j/face:
            for i in range(minstep, maxstep+1):
                if pos+d*i in graph:
                    v, count = sum(graph[pos+d*j] for j in range(1,i+1)), count+1
                    heapq.heappush(Q, (heatloss+v, count, pos+d*i, d))

print(travel(4, 10, 0))