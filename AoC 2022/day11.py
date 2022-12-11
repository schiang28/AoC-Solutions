monkeys = {0: [54, 98, 50, 94, 69, 62, 53, 85], 1: [71, 55, 82], 2: [77, 73, 86, 72, 87], 3:[97, 91], 4: [78, 97, 51, 85, 66, 63, 62], 5: [88], 6: [87, 57, 63, 86, 87, 53], 7: [73, 59, 82, 65]}
moves = {0: lambda x:x*13, 1: lambda x:x+2, 2:lambda x:x+8, 3:lambda x:x+1, 4: lambda x:x*17, 5: lambda x:x+3, 6: lambda x:x*x, 7: lambda x:x+6}
rules = {0: (3,2,1), 1: (13,7,2), 2:(19,4,7), 3:(17,6,5), 4:(5,6,3), 5:(7,1,0), 6:(11,5,0), 7:(2,4,3)}
inspect, prod = {i:0 for i in range(len(monkeys))}, 2*3*5*7*11*13*17*19

for _ in range(10000):
    for i in range(len(monkeys)):
        for item in range(len(monkeys[i])):
            new = moves[i](monkeys[i].pop(0))
            if new % rules[i][0] == 0:
                monkeys[rules[i][1]].append(new%prod)
            else:
                monkeys[rules[i][2]].append(new%prod)
            inspect[i] += 1

print(sorted(inspect.values())[-1]*sorted(inspect.values())[-2])