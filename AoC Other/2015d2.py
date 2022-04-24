with open("input.txt") as f:
    file = f.read().splitlines()
file = [list(map(int, i.split("x"))) for i in file]

total = 0
ribbon = 0
for i in file:
    extra = min(i[0] * i[1], i[0] * i[2], i[1] * i[2])
    sa = 2 * i[0] * i[1] + 2 * i[0] * i[2] + 2 * i[1] * i[2] + extra
    total += sa
    ribbon += i[0] * i[1] * i[2] + sorted(i)[0] * 2 + sorted(i)[1] * 2

print(total)
print(ribbon)