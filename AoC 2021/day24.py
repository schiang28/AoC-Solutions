from collections import defaultdict

with open("day24input.txt") as f:
    file = [i.split() for i in f.read().splitlines()]

# first tried to implement the ALU quite literally by checking each line, first element etc...obviously it was too slow
# then had a look at the input and found that each 'block' of how each digit was dealt with was very similar
# each block basically repeated with some instructions simply having different values, all registers being modified etc was the same
# translated the instructions to python but it was still way too slow
# thought about and attempted using z3 and failed
# had another look at the input and find how z was like popping and pushing from a stack
# stack had to be empty at the end for z to be 0
# condition for x had to be met in every loop for number of pops and pushes to be the same
# therefore u can then find how pairs of digits in the model number related to each other
# e.g 4th digit had to equal 5th digit; for the largest model these 2 digits would be 9
# working out largest and smallest model number was therefore trivial from here
# well at least i could use my code to check the worked out answer :/

code = 99999999999999

while True:
    var = defaultdict(int, {"w": 0, "x": 0, "y": 0, "z": 0})
    count = 0
    for instruct in file:
        if len(instruct) == 2:
            var[instruct[1]] = int(str(code)[count])
            count += 1
        elif instruct[0] == "add":
            if instruct[2].isdigit() or instruct[2][0] == "-":
                var[instruct[1]] += int(instruct[2])
            else:
                var[instruct[1]] += var[instruct[2]]
        elif instruct[0] == "mul":
            if instruct[2].isdigit() or instruct[2][0] == "-":
                var[instruct[1]] *= int(instruct[2])
            else:
                var[instruct[1]] *= var[instruct[2]]
        elif instruct[0] == "div":
            if instruct[2].isdigit() or instruct[2][0] == "-":
                temp = var[instruct[1]] // int(instruct[2])
                var[instruct[1]] = temp
                # var[instruct[1]] = trunc(temp)
            else:
                temp = var[instruct[1]] // var[instruct[2]]
                var[instruct[1]] = temp
                # var[instruct[1]] = trunc(temp)
        elif instruct[0] == "mod":
            if instruct[2].isdigit() or instruct[2][0] == "-":
                var[instruct[1]] %= int(instruct[2])
            else:
                var[instruct[1]] %= var[instruct[2]]
        else:
            if instruct[2].isdigit() or instruct[2][0] == "-":
                if var[instruct[1]] == int(instruct[2]):
                    var[instruct[1]] = 1
                else:
                    var[instruct[1]] = 0
            else:
                if var[instruct[1]] == var[instruct[2]]:
                    var[instruct[1]] = 1
                else:
                    var[instruct[1]] = 0

    if var["z"] == 0:
        print(code)
        break
    code -= 1
    while "0" in str(code):
        code -= 1


a = [1, 1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 26, 26, 26]
b = [15, 10, 12, 10, 14, -11, 10, -16, -9, 11, -8, -8, -10, -9]
c = [13, 16, 2, 8, 11, 6, 12, 2, 2, 15, 1, 10, 14, 10]

while True:
    x, y, z = 0, 0, 0
    for i in range(len(str(code))):
        w = int(str(code)[i])
        x = z % 26 + b[i]
        z = z // a[i]
        x = 1 if x != w else 0
        y = 25 * x + 1
        z *= y  # y will be 26 or 1
        y = 0
        y += w
        y += c[i]
        y *= x
        z += y
    if z == 0:
        print(code)
        break
    code -= 1
    while "0" in str(code):
        code -= 1


"""
a = [1, 1, 1, 1, 1, 26, 1, 26, 26, 1, 26, 26, 26, 26]
b = [15, 10, 12, 10, 14, -11, 10, -16, -9, 11, -8, -8, -10, -9]
c = [13, 16, 2, 8, 11, 6, 12, 2, 2, 15, 1, 10, 14, 10]

want z to end up 0
therefore stack has to be empty
all conditions have to be met in loop

push code[0]+13
push code[1]+16
push code[2]+2
push code[3]+8
push code[4]+11
code[5]-11
push code[6]+12
code[7]-16
code[8]-9
push code[9]+15
code[10]-8
code[11]-8
code[12]-10
code[13]-9


code[5] = code[4]
code[7] = code[6]-4
code[8] = code[3]-1
code[10] = code[9]+7
code[11] = code[2]-6
code[12] = code[1]+6
code[13] = code[0]+4


largest = 53999995829399
smalleset = 11721151118175
"""
