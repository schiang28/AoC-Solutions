from collections import defaultdict

with open("day14input.txt") as f:
    file = f.read().splitlines()
template, rules = file[0], {i.split(" -> ")[0]: i.split(" -> ")[1] for i in file[2:]}

counts = defaultdict(int)
for i in range(len(template) - 1):
    counts[template[i] + template[i + 1]] += 1

for _ in range(40):
    tempc = defaultdict(int)
    # if AB -> C, tempc will store pairs AC and CB, and value is no. of times AB appears
    for k in counts:
        tempc[k[0] + rules[k]] += counts[k]
        tempc[rules[k] + k[1]] += counts[k]
    counts = tempc

ans = defaultdict(int, {template[-1]: 1})
for k in counts:
    ans[k[0]] += counts[k]
print(max(ans.values()) - min(ans.values()))