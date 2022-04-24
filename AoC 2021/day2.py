with open("day2input.txt") as f:
    file = f.read().splitlines()

x1, y1, x2, y2, aim = 0, 0, 0, 0, 0

for i in file:
    direction, unit = i.split()
    unit = int(unit)
    if direction == "forward":
        x1 += unit
        x2 += unit
        y2 += unit * aim
    elif direction == "down":
        y1 += unit
        aim += unit
    elif direction == "up":
        y1 -= unit
        aim -= unit

print(x1 * y1)  # PART 1
print(x2 * y2)  # PART 2
