from itertools import groupby

with open("day5input.txt") as f:
    file = [list(g) for k, g in groupby(f.read().splitlines(), key=bool) if k]
mapvals = [[list(map(int, file[i][j].split())) for j in range(1, len(file[i]))] for i in range(1, len(file))]
seeds = list(map(int, file[0][0].split()[1:]))

def minloc(seeds):
    for i in range(len(mapvals)):
        newseeds = []
        for rsrc, rran in seeds:
            inter = False
            for dest, src, ran in mapvals[i]:
                rend, end, insrc, diff = rsrc+rran, src+ran, max(rsrc, src), dest-src
                if rsrc < end and src < rend:
                    inter, inran = True, min(rend, end) - insrc # intersection range
                    nend = insrc + inran
                    newseeds.append((insrc+diff, inran))
                    if insrc > rsrc: seeds.append((rsrc, insrc-rsrc)) # before intersection range
                    if nend < rend: seeds.append((nend, rend-nend)) # after intersection range
                    break
            if not inter: newseeds.append((rsrc, rran))
        seeds = newseeds

    return min([i[0] for i in seeds])

print(minloc([(seeds[i], 1) for i in range(0, len(seeds), 2)]))
print(minloc([(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]))