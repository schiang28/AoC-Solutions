with open("day5input.txt") as f:
    file = [i.split(" ") for i in f.read().splitlines()]
steps = [list(map(int, (i[1], i[3], i[5]))) for i in file]

stacks = {
    1: "SLW",
    2: "JTNQ",
    3: "SCHFJ",
    4: "TRMWNGB",
    5: "TRLSDHQB",
    6: "MJBVFHRL",
    7: "DWRNJM",
    8: "BZTFHNDJ",
    9: "HLQNBFT",
}

for step in steps:
    n1, n2, n3, temp = step[0], step[1], step[2], ""
    for _ in range(n1):
        temp += stacks[n2][-1]
        stacks[n2] = stacks[n2][:-1]
    temp = temp[::-1]  # <- delete for part 1
    stacks[n3] += temp

for k, v in stacks.items():
    print(v[-1], end="")
