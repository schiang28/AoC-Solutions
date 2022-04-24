import random

with open('/Users/sophiechiang/Documents/Python/Advent of Code/tinput.txt') as f:
    n = f.read().splitlines()

whole = []
xyz = []
j = 0
while j < len(n):
    if n[j] != '':
        n[j] = [char for char in n[j]]
        xyz.append(n[j])
        j += 1
    else:
        whole.append(xyz)
        xyz = []
        j += 2

print(whole)

'''size = 9
cube_ls = []

for x in range(0, size, 3):
    for y in range(0, size, 3):
        for z in range(0, size, 3):
            cube = (x, y, z)
            cube_ls.append(cube)

stream = '0110100101110100'
choice = [(0, 0, 0,), (0, 0, 3), (0, 0, 6), (0, 3, 0), (0, 3, 3), (0, 3, 6), (0, 6, 0),
          (0, 6, 3), (0, 6, 6), (3, 0, 0), (3, 0, 3), (3, 0, 6), (3, 3, 0), (6, 0, 0), (6, 3, 0), (6, 6, 6)]


data = []
centre = []
for i in range(len(choice)):
    data.append(stream[i])
    centre.append((choice[i][0]+1, choice[i][1]+1, choice[i][2]+1))

# print(centre)
# print(data)

for i in range(len(centre)):
    dx, dy, dz = centre[i][0], centre[i][1], centre[i][2]
    whole[dz][dy][dx] = data[i]

ls = []
for i in range(len(cube_ls)):
    s = 0
    c = cube_ls[i]
    for x in range(3):
        for y in range(3):
            for z in range(3):
                co = (c[0]+x, c[1]+y, c[2]+z)
                if whole[co[2]][co[1]][co[0]] == '1':
                    s += 1
    if c in choice and s % 2 == 1:
        if whole[c[2]][c[1]][c[0]] == '1':
            whole[c[2]][c[1]][c[0]] = '0'
        else:
            whole[c[2]][c[1]][c[0]] = '1'
    if c not in choice and s % 2 == 0:
        if whole[c[2]][c[1]][c[0]] == '1':
            whole[c[2]][c[1]][c[0]] = '0'
        else:
            whole[c[2]][c[1]][c[0]] = '1'

'''for i in whole:
    for j in i:
        print(''.join(j))
    print("")
    print("")

centre = []
for i in range(len(cube_ls)):
    s = 0
    c = cube_ls[i]
    for x in range(3):
        for y in range(3):
            for z in range(3):
                co = (c[0]+x, c[1]+y, c[2]+z)
                if whole[co[2]][co[1]][co[0]] == '1':
                    s += 1
    if s % 2 == 0:
        #print((cube_ls[i][0]+1, cube_ls[i][1]+1, cube_ls[i][2]+1))
        centre.append((cube_ls[i][0]+1, cube_ls[i][1]+1, cube_ls[i][2]+1))

# print(centre)
ls = []
for i in range(len(centre)):
    ax, ay, az = centre[i][0], centre[i][1], centre[i][2]
    ls.append(whole[az][ay][ax])

binary = ''.join(ls)
print(binary)
n = 8
splitted = [binary[i:i+n] for i in range(0, len(binary), n)]
for i in range(len(splitted)):
    splitted[i] = chr(int(splitted[i], 2))
print(''.join(splitted))
