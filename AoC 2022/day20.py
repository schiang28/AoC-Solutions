from collections import deque

with open("day20input.txt") as f:
    file = deque(int(i) * 811589153 for i in f.read().splitlines())
M = (moves := list(range(size := len(file)))).copy() * 10

for i in M:
    item = moves.index(i)
    moves.pop(item)
    moves.insert((item + file[i]) % len(moves), i)

z = moves.index(file.index(0))
print(file[moves[(z + 1000) % size]] + file[moves[(z + 2000) % size]] + file[moves[(z + 3000) % size]])
