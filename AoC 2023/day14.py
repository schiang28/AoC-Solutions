with open('day14input.txt') as f:
    file = [list(i) for i in f.read().splitlines()]

for cycle in range(120):
    total = 0
    # tilt north
    for col in range(len(file[0])):
        loads = [file[i][col] for i in range(len(file))]
        poles = [-1] + [i for i in range(len(loads)) if loads[i] == "#"] + [len(file)]
        for i in range(len(poles)-1):
            rocks = 0
            for j in range(poles[i]+1, poles[i+1]):
                if loads[j] == "O":
                    if file[poles[i]+1+rocks][col] != "O": file[poles[i]+1+rocks][col], file[j][col] = "O", "."
                    rocks += 1

    # tilt west
    for row in range(len(file)):
        poles = [-1] + [i for i in range(len(file[0])) if file[row][i] == "#"] + [len(file[0])]
        for i in range(len(poles)-1):
            rocks = 0
            for j in range(poles[i]+1, poles[i+1]):
                if file[row][j] == "O":
                    if file[row][poles[i]+1+rocks] != "O": file[row][poles[i]+1+rocks], file[row][j] = "O", "."
                    rocks += 1

    # tile south
    for col in range(len(file[0])):
        loads = [file[i][col] for i in range(len(file))]
        poles = [-1] + [i for i in range(len(loads)) if loads[i] == "#"] + [len(file)]
        for i in range(len(poles)-1):
            rocks = 0
            for j in range(poles[i+1]-1, poles[i], -1):
                if loads[j] == "O":
                    if file[poles[i+1]-1-rocks][col] != "O": file[poles[i+1]-1-rocks][col], file[j][col] = "O", "."
                    rocks += 1

    # tile east
    for row in range(len(file)):
        poles = [-1] + [i for i in range(len(file[0])) if file[row][i] == "#"] + [len(file[0])]
        for i in range(len(poles)-1):
            rocks = 0
            for j in range(poles[i+1]-1, poles[i], -1):
                if file[row][j] == "O":
                    if file[row][poles[i+1]-1-rocks] != "O": file[row][poles[i+1]-1-rocks], file[row][j] = "O", "."
                    rocks += 1

    for i in range(len(file)):
        for j in range(len(file)):
            if file[i][j] == "O": total += (len(file)-i)
    print(total, cycle+1)

# cycles between 11 values after approx 120 cycles, support at 98th cycle is 106689 which is answer