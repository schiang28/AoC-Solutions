with open('/Users/sophiechiang/Documents/Python/Advent of Code/input.txt') as f:
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

# print(whole)

size = 120
cube_ls = []
for x in range(0, size, 3):
    for y in range(0, size, 3):
        for z in range(0, size, 3):
            cube = (x, y, z)
            cube_ls.append(cube)

centre = []
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
    if s % 2 == 0:
        centre.append((cube_ls[i][0]+1, cube_ls[i][1]+1, cube_ls[i][2]+1))

for i in range(len(centre)):
    ax, ay, az = centre[i][0], centre[i][1], centre[i][2]
    ls.append(whole[az][ay][ax])

binary = ''.join(ls)
splitted = [binary[i:i+8] for i in range(0, len(binary), 8)]
print(splitted)

for i in range(len(splitted)):
    splitted[i] = chr(int(splitted[i], 2))

print(''.join(splitted))
