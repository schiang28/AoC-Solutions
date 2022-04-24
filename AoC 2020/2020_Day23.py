cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]

c = cups[0]
for i in range(100):
    pick = []

    pick.append(cups[(cups.index(c)+1) % len(cups)])
    pick.append(cups[(cups.index(c)+2) % len(cups)])
    pick.append(cups[(cups.index(c)+3) % len(cups)])
    for j in pick:
        cups.remove(j)

    d = cups[cups.index(c)] - 1
    valid = False
    while not valid:
        if d not in pick and d != 0:
            valid = True
        else:
            d -= 1
            if d < 0:
                d = max(cups)
    des = cups.index(d)
    cups.insert(des+1, pick[0])
    cups.insert(des+2, pick[1])
    cups.insert(des+3, pick[2])
    c = cups[(cups.index(c) + 1) % len(cups)]

print(cups)
