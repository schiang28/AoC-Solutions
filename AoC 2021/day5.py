import re

# extracts coordinates of each instruction
with open("day5input.txt") as f:
    file = f.read().splitlines()
coord = [re.findall("(\d+),(\d+) -> (\d+),(\d+)", instruct) for instruct in file]

# find the maximum x and y coordinate in the instructions
maxx, maxy = 0, 0
for i in coord:
    for j in i:
        maxx, maxy = max(maxx, int(j[0]), int(j[2])), max(maxy, int(j[1]), int(j[3]))
matrix = [[0] * (maxx + 1) for _ in range(maxy + 1)]


# part 2 for finding diagonall pipes
def diagonal(matrix, x1, y1, x2, y2):
    if x1 > x2:
        x1, y1, x2, y2 = x2, y2, x1, y1

    slope = (y2 - y1) // (x2 - x1)
    for i, j in zip(range(x1, x2), range(y1, y2, slope)):
        matrix[j][i] += 1
    matrix[y2][x2] += 1


# increments the coordinate by 1 if a line crosses
for instruct in coord:
    x1, y1, x2, y2 = (
        int(instruct[0][0]),
        int(instruct[0][1]),
        int(instruct[0][2]),
        int(instruct[0][3]),
    )
    if x1 == x2 and y1 != y2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            matrix[i][x1] += 1
    elif y1 == y2 and x1 != x2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            matrix[y1][i] += 1
    else:
        diagonal(matrix, x1, y1, x2, y2)

ans = [[1 for i in x if i >= 2] for x in matrix]
print(sum(len(x) for x in ans))
