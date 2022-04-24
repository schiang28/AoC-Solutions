with open("input.txt") as f:
    file = f.read()
x, y = 0, 0
m = {(0, 0): 1}
for instructions in range(0, len(file), 2):
    if file[instructions] == "^":
        y += 1
    elif file[instructions] == ">":
        x += 1
    elif file[instructions] == "<":
        x -= 1
    else:
        y -= 1
    if (x, y) in m.keys():
        m[(x, y)] += 1
    else:
        m[(x, y)] = 1

x, y = 0, 0
for instructions in range(1, len(file), 2):
    if file[instructions] == "^":
        y += 1
    elif file[instructions] == ">":
        x += 1
    elif file[instructions] == "<":
        x -= 1
    else:
        y -= 1
    if (x, y) in m.keys():
        m[(x, y)] += 1
    else:
        m[(x, y)] = 1


# print(m)
print(len(m.keys()))