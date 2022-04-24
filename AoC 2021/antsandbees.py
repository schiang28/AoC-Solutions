from copy import deepcopy

with open("antsandbeesinput.txt") as f:
    file = [list(i) for i in f.read().splitlines()]

grid = deepcopy(file)
rows = len(file)
columns = len(file[0])

for _ in range(10 ** 10):
    for r in range(rows):
        for c in range(columns):
            if file[r][(c + 1) % columns] in "0.":
                if file[(r + 1) % rows][c] in "01":
                    grid[r][c] = "0"
                else:
                    grid[r][c] = "."
            else:
                if file[(r + 1) % rows][c] in "01":
                    grid[r][c] = "1"
                else:
                    grid[r][c] = "#"
    file = deepcopy(grid)

ants = sum([i.count("1") for i in file])
bees = sum([i.count("#") for i in file])
print(abs(ants - bees))
