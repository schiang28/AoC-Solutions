from collections import Counter, defaultdict

with open("day6input.txt") as f:
    fish = list(map(int, f.read().split(",")))
fish = dict(Counter(fish))

# converts fish to defaultdict, returns 0 for any values not in dict
# subtract 1 from timer, resets and reproduces, deletes fish on -1
for _ in range(256):
    fish = defaultdict(int, {(k - 1): v for k, v in fish.items()})
    fish[8], fish[6] = fish[8] + fish[-1], fish[6] + fish[-1]
    if -1 in fish.keys():
        del fish[-1]

print(sum(fish.values()))
