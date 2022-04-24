with open("input.txt") as f:
    file = f.read()

print(file.count("(") - file.count(")"))
floor = 0
for i in range(len(file)):
    if file[i] == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(i)
