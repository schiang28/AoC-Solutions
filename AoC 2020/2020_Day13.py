time = 1000495
numbers = '''
19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,521,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,523,x,x,x,x,x,37,x,x,x,x,x,x,13'''

depart = numbers.split(",")
differences = []
d1 = []

# PART 1
for i in range(0, len(depart)):
    x = 0
    while x < time:
        if depart[i] != "x":
            x += int(depart[i])
        else:
            break
    diff = x - time
    if diff >= 0:
        differences.append(int(diff)*int(depart[i]))
        d1.append(diff)

s = d1.index(min(d1))
print("p1", differences[s])

# PART 2
depart = [*map(int, numbers.replace('x', '1').split(','))]
print(depart)

time, p = 0, 1
for i, b in enumerate(depart):
    print(i, b)
    while (time+i) % b:
        time += p
    p *= b

print("p2", time)
