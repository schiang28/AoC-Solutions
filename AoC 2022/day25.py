with open("day25input.txt") as f:
    file = f.read().splitlines()
total, snafu, num = 0, [], {-2: '=', -1: '-'}

for i in file:
    temp = 0
    for j in range(len(i)):
        if i[j] == "=":
            mul = -2
        elif i[j] == "-":
            mul = -1
        else:
            mul = int(i[j])
        temp += (mul * (5 ** (len(i) - j - 1)))
    total += temp

print(total)

while total > 0:
    total, res = divmod(total, 5)
    if res == 3:
        total += 1
        res = -2
    elif res == 4:
        total += 1
        res = -1
    snafu.append(res)

ans = ""
for i in reversed(snafu):
    if i >= 0:
        ans += str(i)
    else:
        ans += str(num[i])

print(ans)
