from itertools import groupby
import regex as re
from collections import defaultdict
import functools
from copy import deepcopy

with open('day19input.txt') as f:
    file = f.read()
    instructions, parts = [list(g) for k, g in groupby(file.splitlines(), key=bool) if k]
    rules, _ = file.strip().split('\n\n')
instructions, total, p2, r = {i.split("{")[0]: i.split("{")[1][:-1].split(",") for i in instructions},0,0,defaultdict(list)
for rule in rules.splitlines():
    name, rest = rule[:-1].split('{')
    workflows = rest.split(',')
    for w in workflows:
        if ':' in w: r[name].append(tuple(w.split(':')))
        else: r[name].append((None, w))
xmas_map = {x: y for y, x in enumerate('xmas')}

for part in parts:
    state = 'in'
    x, m, a, s = list(map(int, re.findall(r'\d+', part)))

    while True:
        if state == 'A':
            total += x + m + a + s
            break
        if state == 'R': break

        conds, valid = instructions[state], False
        for i in range(len(conds) - 1):
            if eval(conds[i].split(":")[0]):
                state, valid = conds[i].split(":")[1], True
                break

        if valid: continue
        state = conds[-1]

print(total)


