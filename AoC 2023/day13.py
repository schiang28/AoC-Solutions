from itertools import groupby

with open('day13input.txt') as f:
    file = [list(g) for k, g in groupby(f.read().splitlines(), key=bool) if k]
refc, refr, count, refc2, refr2 = {}, {}, 1, [], []

for t in file:
    found = False
    possc = [col for col in range(len(t[0])-1) if [i[col] for i in t] == [i[col+1] for i in t]]

    for c in possc:
        valid, diff = True, 1
        while True:
            if 0<=c-diff<len(t[0]) and 0<=c+1+diff<len(t[0]):
                if [i[c-diff] for i in t] != [i[c+1+diff] for i in t]:
                    valid = False
                    break
            else: break
            diff += 1
        if valid: refc[count], refr[count], found = c+1, 0, True

    if not found:
        possr = [row for row in range(len(t)-1) if t[row] == t[row+1]]

        for r in possr:
            valid, diff = True, 1
            while True:
                if 0<=r-diff<len(t) and 0<=r+1+diff<len(t):
                    if t[r-diff] != t[r+1+diff]:
                        valid = False
                        break
                else: break
                diff += 1
            if valid: refr[count], refc[count] = r+1, 0
    count+=1

print(sum([i for i in refc.values()]) + sum([i*100 for i in refr.values()]))

count = 1
for t in file:
    foundalt = False
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == "#": t[i] = t[i][:j] + "." + t[i][j+1:]
            else: t[i] = t[i][:j] + "#" + t[i][j+1:]

            found = False
            possc = [col for col in range(len(t[0])-1) if [i[col] for i in t] == [i[col+1] for i in t] and refc[count] != (col+1)]

            for c in possc:
                valid, diff = True, 1
                while True:
                    if 0<=c-diff<len(t[0]) and 0<=c+1+diff<len(t[0]):
                        if [i[c-diff] for i in t] != [i[c+1+diff] for i in t]:
                            valid = False
                            break
                    else: break
                    diff += 1
                if valid:
                    found, foundalt = True, True
                    refc2.append(c+1)

            if not found:
                possr = [row for row in range(len(t)-1) if t[row] == t[row+1] and refr[count] != (row+1)]

                for r in possr:
                    valid, diff = True, 1
                    while True:
                        if 0<=r-diff<len(t) and 0<=r+1+diff<len(t):
                            if t[r-diff] != t[r+1+diff]:
                                valid = False
                                break
                        else: break
                        diff += 1
                    if valid:
                        foundalt = True
                        refr2.append(r+1)
            
            if t[i][j] == "#": t[i] = t[i][:j] + "." + t[i][j+1:]
            else: t[i] = t[i][:j] + "#" + t[i][j+1:]

            if foundalt: break
        if foundalt: break
        
    count+=1


total = sum([i for i in refc2]) + sum([i*100 for i in refr2])
print(total)