with open("day3input.txt") as f:
    bags = f.read().splitlines()

priority = "-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
t1, t2 = 0, 0

for compt in bags:
    b1, b2 = compt[: (len(compt) // 2)], compt[len(compt) // 2 :]  # splits compartment
    common = list(set(b1) & set(b2))[0]  # finds intersection -> converts set to list
    t1 += priority.index(common)
print(t1)

for compt in range(0, len(bags), 3):
    b1, b2, b3 = bags[compt], bags[compt + 1], bags[compt + 2]
    common = list(set(b1) & set(b2) & set(b3))[0]
    t2 += priority.index(common)

print(t2)
