monkeys = {0: [54, 98, 50, 94, 69, 62, 53, 85], 1: [71, 55, 82], 2: [77, 73, 86, 72, 87], 3:[97, 91], 4: [78, 97, 51, 85, 66, 63, 62], 5: [88], 6: [87, 57, 63, 86, 87, 53], 7: [73, 59, 82, 65]}
moves = {0: lambda x : x*13, 1: lambda x:x+2, 2:lambda x: x+8, 3:lambda x: x+1, 4: lambda x:x*17, 5: lambda x:x+3, 6: lambda x: x*x, 7: lambda x: x+6}
inspect = {i:0 for i in range(len(monkeys))}
prod = 2*3*5*7*11*13*17*19

for _ in range(10000):
    for i in range(len(monkeys)):
        for item in range(len(monkeys[i])):
            old = monkeys[i].pop(0)
            new = moves[i](old)
            if i==0:
                if new % 3 == 0:
                    monkeys[2].append(new%prod)
                else:
                    monkeys[1].append(new%prod)
            elif i==1:
                if new % 13 == 0:
                    monkeys[7].append(new%prod)
                else:
                    monkeys[2].append(new%prod)
            elif i==2:
                if new % 19 == 0:
                    monkeys[4].append(new%prod)
                else:
                    monkeys[7].append(new%prod)
            elif i==3:
                if new % 17 == 0:
                    monkeys[6].append(new%prod)
                else:
                    monkeys[5].append(new%prod)
            elif i==4:
                if new % 5 ==0:
                    monkeys[6].append(new%prod)
                else:
                    monkeys[3].append(new%prod)
            elif i==5:
                if new %7==0:
                    monkeys[1].append(new%prod)
                else:
                    monkeys[0].append(new%prod)
            elif i==6:
                if new % 11==0:
                    monkeys[5].append(new%prod)
                else:
                    monkeys[0].append(new%prod)
            else:
                if new %2==0:
                    monkeys[4].append(new%prod)
                else:
                    monkeys[3].append(new%prod)
            inspect[i] += 1

s = sorted(inspect.values())
print(s[-1]*s[-2])