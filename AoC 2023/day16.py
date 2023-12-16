import sys
recur_limit = sys.setrecursionlimit(100000)

with open('day16input.txt') as f:
    file = f.read().splitlines()
maxenergised = 0

def travel(row, col, face):
    if not (0<=row<len(file) and 0<=col<len(file[0])): return 
    if (row, col, face) in visited: return

    visited.append((row, col, face))
    current = file[row][col]

    if current == '.':
        if face == 'R': travel(row, col+1, face)
        elif face == 'D': travel(row+1, col, face)
        elif face == 'L': travel(row, col-1, face)
        else: travel(row-1, col, face)
    elif current == '|':
        if face in 'RL':
            travel(row+1, col, 'D')
            travel(row-1, col, 'U')
        elif face == 'D': travel(row+1, col, face)
        else: travel(row-1, col, face)
    elif current == '-':
        if face in 'DU':
            travel(row, col-1, 'L')
            travel(row, col+1, 'R')
        elif face == 'R': travel(row, col+1, face)
        else: travel(row, col-1, face)
    elif current == '/':
        if face == 'R': travel(row-1, col, 'U')
        elif face == 'D': travel(row, col-1, 'L')
        elif face == 'L': travel(row+1, col, 'D')
        else: travel(row, col+1, 'R')
    elif current == '\\':
        if face == 'R': travel(row+1, col, 'D')
        elif face == 'D': travel(row, col+1, 'R')
        elif face == 'L': travel(row-1, col, 'U')
        else: travel(row, col-1, 'L')

# top
for col in range(len(file[0])):
    visited = []
    travel(0, col, 'D')
    maxenergised = max(maxenergised, len(set([(i[0], i[1]) for i in visited])))

# left
for row in range(len(file)):
    visited = []
    travel(row, 0, 'R')
    maxenergised = max(maxenergised, len(set([(i[0], i[1]) for i in visited])))

# bottom
for col in range(len(file)):
    visited = []
    travel(len(file)-1, col, 'U')
    maxenergised = max(maxenergised, len(set([(i[0], i[1]) for i in visited])))

# right
for row in range(len(file)):
    visited = []
    travel(row, len(file[0])-1, 'L')
    maxenergised = max(maxenergised, len(set([(i[0], i[1]) for i in visited])))

print(maxenergised)