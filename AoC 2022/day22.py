with open("day22input.txt") as f:
    file = f.read().splitlines()
plane, ins, direction = file[:-2], file[-1], "RDLU"
x, y, dire = plane[0].index("."), 0, direction[0]
size = 50

moves, temp = [], ""
for i in ins:
    if i == "L" or i == "R":
        moves.append(temp)
        moves.append(i)
        temp = ""
    else:
        temp += i
moves.append(temp)

for i in moves:
    if i == "L":
        dire = direction[(direction.index(dire) - 1) % 4]
    elif i == "R":
        dire = direction[(direction.index(dire) + 1) % 4]
    else:
        lx, ly = len(plane[y].strip()), len(''.join([i[x] for i in plane if x < len(i)]).strip())
        if dire == "R":
            dx, dy = 1, 0
        elif dire == "D":
            dx, dy = 0, 1
        elif dire == "L":
            dx, dy = -1,0
        else:
            dx, dy = 0,-1

        for _ in range(int(i)):
            tempd = dire
            tempx = x + dx
            if tempx >= len(plane[y]):
                # tempx -= lx
                if 0<=y<=size-1:
                    tempy = size*3-1-y
                    tempx = size*2-1
                    tempd = "L"
                elif size<=y<=size*2-1:
                    tempy = size-1
                    tempx = y
                    tempd = "U"
                elif size*2<=y<=size*3-1:
                    tempx = size*3-1
                    tempy = size*3-1-y
                else:
                    pass
            elif tempx < (len(plane[y])-lx):
                tempx %= lx
            tempy = y + dy

            lengthy = len(''.join([i[x] for i in plane if x < len(i)]).rstrip())
            if tempy >= lengthy:
                tempy -= ly
            elif tempy < (lengthy-ly):
                tempy = lengthy - 1

            if plane[tempy][tempx] == "#":
                break
            else:
                dire = tempd
                x, y = tempx, tempy

p = {"R": 0, "D": 1, "L":2, "U":3}
password = 1000*(y+1)+4*(x+1)+p[dire]
print(password)