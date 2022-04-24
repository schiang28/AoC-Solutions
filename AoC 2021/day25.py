from copy import deepcopy

with open("day25input.txt") as f:
    file = [list(i) for i in f.read().splitlines()]

cuc = deepcopy(file)
count = 1

while True:
    move = False

    for r in range(len(file)):
        for c in range(len(file[0])):
            if file[r][c] == ">" and file[r][(c + 1) % len(file[0])] == ".":
                cuc[r][(c + 1) % len(file[0])], cuc[r][c] = ">", "."
                move = True
    file = deepcopy(cuc)
    for r in range(len(file)):
        for c in range(len(file[0])):
            if file[r][c] == "v" and file[(r + 1) % len(file)][c] == ".":
                cuc[(r + 1) % len(file)][c], cuc[r][c] = "v", "."
                move = True
    file = deepcopy(cuc)

    if not move:
        break
    count += 1

print(count)