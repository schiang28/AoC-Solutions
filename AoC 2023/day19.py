from itertools import groupby, product
import regex as re
from collections import defaultdict
import functools
from copy import deepcopy

with open('day19input.txt') as f:
    file = f.read()
    instructions, parts = [list(g) for k, g in groupby(file.splitlines(), key=bool) if k]
    rules, candidates = file.strip().split('\n\n')
instructions, total, p2 = {i.split("{")[0]:i.split("{")[1][:-1].split(",") for i in instructions}, 0, 0

for part in parts:
    state = 'in'
    x,m,a,s = list(map(int, re.findall(r'\d+', part)))

    while True:
        if state == 'A':
            total += x+m+a+s
            break
        if state == 'R':
            break

        conds = instructions[state]
        valid = False
        for i in range(len(conds)-1):
            if eval(conds[i].split(":")[0]):
                state=  conds[i].split(":")[1]
                valid = True
                break
        if valid:
            continue

        state = conds[-1]

print(total)

r = defaultdict(list)
for rule in rules.splitlines():
    name, rest = rule[:-1].split('{')
    workflows = rest.split(',')
    for w in workflows:
        if ':' in w:
            r[name].append(tuple(w.split(':')))
        else:
            r[name].append((None, w))

xmas_map = {x:y for y,x in enumerate('xmas')}
def process2(min_ranges=[1 for _ in range(4)], max_ranges=[4000 for _ in range(4)], name='in', i = 0):
    global p2
    diffs = list(map(lambda x,y: y - x + 1,min_ranges, max_ranges))
    for d in diffs:
        if d < 0:
            return
    if name == 'A':
        p2 += functools.reduce(lambda x,y : x*y, diffs)
        return
    if name == 'R':
        return 
    rule, next = r[name][i]
    if rule is None:
        process2(min_ranges, max_ranges, next)
        return
    idx = xmas_map[rule[0]]
    number = int(rule[2:])
    if '>' in rule:
        min_ranges_og = deepcopy(min_ranges)
        max_ranges_og = deepcopy(max_ranges)
        
        min_ranges[idx] = max(min_ranges[idx], number+1)
        process2(min_ranges, max_ranges_og, next)
        
        max_ranges[idx] = min(max_ranges[idx], number)
        process2(min_ranges_og, max_ranges, name, i+1)
    if '<' in rule:
        min_ranges_og = deepcopy(min_ranges)
        max_ranges_og = deepcopy(max_ranges)
        
        max_ranges[idx] = min(max_ranges[idx], number-1)
        process2(min_ranges_og, max_ranges, next)
            
        min_ranges[idx] = max(min_ranges[idx], number)
        process2(min_ranges, max_ranges_og, name, i+1)

process2()
print(p2)
