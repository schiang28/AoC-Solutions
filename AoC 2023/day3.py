import re

with open("day3input.txt") as f:
    file = f.read().splitlines()

total, total1 = 0, 0
for r in range(len(file)):
    digits, temps = re.findall('\d+', file[r]), file[r]
    for digit in digits:
        part, start = False, temps.index(digit)
        temps = temps[:start] + 'X'*len(digit) + temps[start+len(digit):]
        for delta in [(0, -1), (1, -1), (-1, -1)]:
            dr, dc = r + delta[0], start + delta[1]
            if 0<=dr<len(file) and 0<=dc<len(file[r]) and file[dr][dc] not in '1234567890.':
                part = True
                break
        for i in range(start, start+len(digit)):
            for delta in [(-1,0), (1,0)]:
                dr = r + delta[0]
                if 0<=dr<len(file) and file[dr][i] not in '1234567890.':
                    part = True
                    break
        for delta in [(0, 1), (1, 1), (-1, 1)]:
            dr, dc = r + delta[0], start + len(digit)
            if 0<=dr<len(file) and 0<=dc<len(file[r]) and file[dr][dc] not in '1234567890.':
                part = True
                break
        if part: total += int(digit)

    for c in range(len(file[r])):
        if file[r][c] == '*':
            gears = []
            for d in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                dr, dc = r+d[0], c+d[1]
                if 0<=dr<len(file) and 0<=dc<len(file[r]) and file[dr][dc].isdigit():
                    extracts, gear = file[dr], file[dr][dc]
                    for i in range(dc+1, len(extracts)):
                        if extracts[i].isdigit(): gear += extracts[i]
                        else: break
                    for i in range(dc-1, -1, -1):
                        if extracts[i].isdigit(): gear = extracts[i] + gear
                        else: break
                    gears.append(int(gear))

            temp = list(set(gears))
            if len(temp) == 2: total1 += temp[0] * temp[1]


print(total, total1)