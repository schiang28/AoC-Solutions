with open("day8input.txt") as f:
    file = f.read().splitlines()
file = [[j.split() for j in i] for i in [i.split(" | ") for i in file]]

print(len(sum([[i for i in j[1] if len(i) in [2, 4, 3, 7]] for j in file], [])))

total = 0
for i in range(len(file)):
    letters = {}
    for j in file[i][0]:
        if len(j) == 2:
            letters[1] = j
        if len(j) == 4:
            letters[4] = j
        if len(j) == 3:
            letters[7] = j
        if len(j) == 7:
            letters[8] = j
    for j in file[i][0]:
        if len(j) == 5:
            # if all the letters in 1 are also used in j, and j has 5 letters, it has to be 3
            if len([ch for ch in letters[1] if ch in j]) == 2:
                letters[3] = j
            else:
                if len([ch for ch in letters[4] if ch in j]) == 2:
                    letters[2] = j
                else:
                    letters[5] = j
        if len(j) == 6:
            if len([ch for ch in letters[4] if ch in j]) == 4:
                letters[9] = j
            else:
                if len([ch for ch in letters[1] if ch in j]) == 2:
                    letters[0] = j
                else:
                    letters[6] = j

    code = ""
    # searched key by value, sorted value first
    for j in file[i][1]:
        for k, v in letters.items():
            if sorted(list(j)) == sorted(list(v)):
                code += str(k)
    total += int(code)

print(total)
