import re

with open("day16input.txt") as f:
    file = [re.findall(r"([A-Z]{2}|\d+)", i) for i in f.read().splitlines()]
flow, paths = {i[0]:int(i[1]) for i in file}, {i[0]: i[2:] for i in file}
O, seen, PL = {k: False for k in flow.keys()}, {}, []

def pressure(time, pos, fl):
    if seen.get((time, pos), -1) >= sum(fl):
        return
    if time == 30:
        PL.append(sum(fl))
        return
    seen[time, pos] = sum(fl)

    for i in range(2):
        if i == 0:
            if O[pos] or flow[pos] == 0:
                continue
            O[pos] = True
            j = sum(flow[k] for k, v in O.items() if v == True)
            pressure(time + 1, pos, fl + [j])
            O[pos] = False
        else:
            j = sum(flow[k] for k, v in O.items() if v == True)
            for v in paths[pos]:
                pressure(time + 1, v if v != None else pos, fl + [j])

pressure(1, "AA", [0])
print(max(PL)) # Part 1