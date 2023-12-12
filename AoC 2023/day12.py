from functools import cache

with open("day12input.txt") as f:
    file, total = [[i.split()[0], list(map(int, i.split()[1].split(",")))] for i in f.read().splitlines()], 0

def nextr(n1, n2):
    if n2 >= len(rec): return 0
    elif len(row) < rec[n2] + n1 or '.' in row[n1:n1+rec[n2]]: return 0
    if len(row) == rec[n2] + n1: return solve(len(row), n2+1)
    elif row[n1+rec[n2]] in '.?': return solve(n1+rec[n2]+1, n2+1)
    else: return 0

@cache
def solve(n1, n2):
    if n1 >= len(row) and n2 >= len(rec): return 1
    elif n1 >= len(row) and n2 < len(rec): return 0
    if row[n1] == "#": return nextr(n1, n2)
    elif row[n1] == ".": return solve(n1+1, n2)
    return nextr(n1, n2) + solve(n1+1, n2)

for r1, r2 in file:
    row, rec = ((r1+"?")*5)[:-1], r2*5
    total += solve(0,0)
    solve.cache_clear()

print(total)