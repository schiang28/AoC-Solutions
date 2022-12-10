with open("day10input.txt") as f:
    file = f.read().splitlines()
X, cycle, a1, cpt, sprite = 1, 0, 0, "", [0, 1, 2]

def draw_cpt(l):
    if l % 40 in sprite:
        return "#"
    else:
        return "."

def check_cycle(c, X):
    if c in [20, 60, 100, 140, 180, 220]:
        return c * X
    return 0


for instruction in file:
    if instruction == "noop":
        cycle += 1
        a1, cpt = a1 + check_cycle(cycle, X), cpt + draw_cpt(len(cpt))
    else:
        for _ in range(2):
            cycle += 1
            a1, cpt = a1 + check_cycle(cycle, X), cpt + draw_cpt(len(cpt))
        X += int(instruction.split(" ")[1])
    sprite = [X, X - 1, X + 1]

print(a1)
print(*[cpt[i : i + 40] for i in range(0, len(cpt), 40)], sep="\n")
