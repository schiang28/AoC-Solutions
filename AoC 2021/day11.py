with open("day11input.txt") as f:
    file = [[int(i) for i in j] for j in f.read().splitlines()]

flashes, step = 0, 0
deltas = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def flash(file):
    for r in range(len(file)):
        for c in range(len(file[r])):
            if file[r][c] == 10 and (r, c) not in flashed:
                flashed.append((r, c))
                for d in deltas:
                    dr, dc = r + d[0], c + d[1]
                    if (
                        0 <= dr < len(file)
                        and 0 <= dc < len(file[0])
                        and file[dr][dc] != 10
                    ):
                        file[dr][dc] += 1
                        if file[dr][dc] == 10:
                            flash(file)


while True:
    file = [[i + 1 for i in j] for j in file]
    step, flashed = step + 1, []
    flash(file)
    file = [[0 if i == 10 else i for i in j] for j in file]
    flashes += sum(x.count(0) for x in file)
    if not any(any(x) for x in file):
        break
    if step == 100:
        print(flashes)

print(step)
