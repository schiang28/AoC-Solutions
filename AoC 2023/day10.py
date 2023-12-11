with open("day10input.txt") as f:
    file = f.read().splitlines()
deltas, lenr, lenc = [(-1, 0), (0, 1), (1, 0), (0, -1)], len(file), len(file[0])
end, step, prevrow, prevcol, paths, enclosed = False, 0, 0, 0, [], 0

for i in range(len(file)):
    for j in range(len(file[i])):
        if file[i][j] == "S": row, col = i, j

while True:
    paths.append((row, col))
    for dr, dc in deltas:
        if prevrow == dr and prevcol == dc: continue
        nrow, ncol, moved = row+dr, col+dc, False
        if 0<=nrow<lenr and 0<=ncol<lenc:
            newtile, curr = file[nrow][ncol], file[row][col]
            # check up
            if dr == -1 and dc == 0:
                if curr in '7-F': continue
                if newtile in '|7F': moved = True
            # check right
            if dr == 0 and dc == 1:
                if curr in '|J7': continue
                if newtile in '-J7': moved = True
            # check down
            if dr == 1 and dc == 0:
                if curr in '-LJ': continue
                if newtile in '|LJ': moved = True
            # check left
            if dr == 0 and dc == -1:
                if curr in '|LF': continue
                if newtile in '-LF': moved = True
            if newtile == "S":
                moved, end = True, True
            if moved:
                step += 1
                row, col, prevrow, prevcol = nrow, ncol, -dr, -dc
                break
    if end: break

for r in range(lenr):
    for c in range(lenc):
        if file[r][c] == "S": file[r] = file[r][:c] + "J" + file[r][c+1:]
        elif (r, c) not in paths:
            count = sum([1 for i in range(c) if file[r][i] in '|LJ' and (r, i) in paths])
            if count % 2 == 1: enclosed += 1

print(step // 2)
print(enclosed)