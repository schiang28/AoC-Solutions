with open("day10input.txt") as f:
    file = f.read().splitlines()
X, cycle, a1, cpt, sprite = 1, 0, 0, "", [0, 1, 2]


def draw(l, sprite):
    if l & 40 in sprite:
        cpt += "#"
    else:
        cpt += "."


for instruction in file:
    if instruction == "noop":
        cycle += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            a1 += cycle * X
        if len(cpt) % 40 in sprite:
            cpt += "#"
        else:
            cpt += "."
    else:
        p1, p2 = instruction.split(" ")[0], int(instruction.split(" ")[1])
        cycle += 1

        if len(cpt) % 40 in sprite:
            cpt += "#"
        else:
            cpt += "."
        if cycle in [20, 60, 100, 140, 180, 220]:
            a1 += cycle * X
        cycle += 1

        if len(cpt) % 40 in sprite:
            cpt += "#"
        else:
            cpt += "."
        if cycle in [20, 60, 100, 140, 180, 220]:
            a1 += cycle * X
        X += p2
    sprite = [X, X - 1, X + 1]

print(a1)
print(*[cpt[i : i + 40] for i in range(0, len(cpt), 40)], sep="\n")
