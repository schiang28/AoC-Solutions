from math import lcm

with open("day8input.txt") as f:
    file = f.read().splitlines()
    steps, nodes = file[0], {i.split(" = ")[0]:i.split(" = ")[1][1:-1].split(", ") for i in file[2:]}
node = [i for i in nodes.keys() if i.endswith("A")]
ends, count, step, sol = [False] * len(node), 0, 0, 1

while True:
    count = count % len(steps)
    move, newnodes = steps[count], []
    for n in node:
        if move == 'L': newnodes.append(nodes[n][0])
        else: newnodes.append(nodes[n][1])
    step += 1
    count += 1
    for i in range(len(newnodes)):
        if newnodes[i].endswith("Z") and ends[i] == False: ends[i], sol = True, lcm(sol, step)
    if all([i for i in ends]): break
    node = newnodes

print(sol)