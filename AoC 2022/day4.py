with open("day4input.txt") as f:
    file = [i.split(",") for i in f.read().splitlines()]

t1, t2 = 0, 0
for i in file:
    n1, n2 = int(i[0].split("-")[0]), int(i[0].split("-")[1])
    n3, n4 = int(i[1].split("-")[0]), int(i[1].split("-")[1])
    if (n1 <= n3 and n2 >= n4) or (n3 <= n1 and n4 >= n2):
        t1 += 1
    r1, r2 = range(n1, n2 + 1), range(n3, n4 + 1)
    if len(set(r1).intersection(r2)) > 0:
        t2 += 1

print(t1)
print(t2)
