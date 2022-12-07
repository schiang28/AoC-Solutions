import re
from collections import defaultdict

with open("day7input.txt") as f:
    file = f.read().splitlines()

parents, sizes = [], defaultdict(int)

for parts in file:
    parts = re.split(" ", parts)
    if len(parts) == 3:
        if parts[-1] != "..":
            parents.append(parts[-1])
        else:
            parents.pop()
    elif parts[0].isnumeric():
        temp = parents.copy()
        while len(temp) > 0:
            sizes["/".join(temp)] += int(parts[0])
            temp.pop()

print(sum([v for v in sizes.values() if v < 100000]))
left = 30000000 - (70000000 - max([v for v in sizes.values()]))
print(min([v for v in sizes.values() if v >= left]))
