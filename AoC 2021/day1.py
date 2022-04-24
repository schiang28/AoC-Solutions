with open("day1input.txt") as f:
    file = list(map(int, f.read().splitlines()))

total = file[2] + file[1] + file[0]
c = 0

# PART 1
for i in range(1, len(file)):
    if file[i] > file[i - 1]:
        c += 1

print(c)

# PART 2
c = 0
for i in range(3, len(file)):
    ans = file[i] + file[i - 1] + file[i - 2]
    if ans > total:
        c += 1
    total = ans

print(c)
