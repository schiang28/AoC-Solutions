with open("day2input.txt") as f:
    file = f.read().splitlines()

# hard-coded solution

total = 0
for game in file:
    if game[-1] == "X":
        total += 1
        if game[0] == "A":
            total += 3
        elif game[0] == "C":
            total += 6
    elif game[-1] == "Y":
        total += 2
        if game[0] == "B":
            total += 3
        elif game[0] == "A":
            total += 6
    else:
        total += 3
        if game[0] == "B":
            total += 6
        elif game[0] == "C":
            total += 3
print(total)

total = 0
for game in file:
    if game[-1] == "X":
        if game[0] == "A":
            total += 3
        elif game[0] == "B":
            total += 1
        else:
            total += 2
    elif game[-1] == "Y":
        total += 3
        if game[0] == "B":
            total += 2
        elif game[0] == "A":
            total += 1
        else:
            total += 3
    else:
        total += 6
        if game[0] == "A":
            total += 2
        elif game[0] == "B":
            total += 3
        else:
            total += 1
print(total)
