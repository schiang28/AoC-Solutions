with open("day2input.txt") as f:
    file = [i.split("; ") for i in f.read().splitlines()]
    for i in range(len(file)):
        for j in range(len(file[i])):
            file[i][j] = file[i][j].split(" ")

def valid1(game):
    for rnd in game:
        if rnd[0] == 'Game': ide, start = int(rnd[1][:-1]), 2
        else: start = 0
        for i in range(start, len(rnd), 2):
            current = int(rnd[i])
            if 'blue' in rnd[i+1] and current > 14:
                return 0
            if 'red' in rnd[i+1] and current > 12:
                return 0
            if 'green' in rnd[i+1] and current > 13:
                return 0
    return ide

def valid2(game):
    maxr, maxb, maxg = 0,0,0
    for rnd in game:
        if rnd[0] == 'Game': start = 2
        else: start = 0
        for i in range(start, len(rnd), 2):
            current = int(rnd[i])
            if 'blue' in rnd[i+1]:
                maxb = max(maxb, current)
            if 'red' in rnd[i+1]:
                maxr = max(maxr, current)
            if 'green' in rnd[i+1]:
                maxg = max(maxg, current)
    return maxb * maxr * maxg

total = sum([valid2(game) for game in file])
print(total)