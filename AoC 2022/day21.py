with open("day21input.txt") as f:
    file = {i.split(": ")[0]:i.split(": ")[1] for i in f.read().splitlines()}
temp = file['root']
file['root'] = temp[:5] + "-" + temp[6:]

def yell(m):
    if file[m].isdigit():
        return int(file[m])
    o1, o2, o3 = file[m].split(" ")
    if o2 == "+":
        return yell(o1) + yell(o3)
    if o2 == "-":
        return yell(o1) - yell(o3)
    if o2 == "*":
        return yell(o1) * yell(o3)
    if o2 == "/":
        return yell(o1) / yell(o3)

for i in range(1000000, 10000000):
    if i % 10000 == 0:
        print(i)
    file['humn'] = str(i)
    if yell("root") == 0:
        print(i)
