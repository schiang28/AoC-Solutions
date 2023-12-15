with open('day15input.txt') as f:
    file = f.read().splitlines()[0].split(",")
boxes, total = {}, 0

for string in file:
    symbol, num, val = string.split('=')[0].split('-')[0], string.split('=')[1] if '=' in string else '', 0
    for char in symbol:
        val += ord(char)
        val *= 17
        val %= 256
    
    if "=" in string:
        if val in boxes.keys():
            present = False
            for i in range(len(boxes[val])):
                if boxes[val][i][0] == symbol: index1, present = i, True
            if present: boxes[val][index1] = (symbol, num)
            else: boxes[val].append((symbol, num))
        else: boxes[val] = [(symbol, num)]
    else:
        remove = False
        if val not in boxes.keys(): boxes[val] = []
        for i in range(len(boxes[val])):
            if boxes[val][i][0] == symbol: index, remove = i, True
        if remove: boxes[val].pop(index)

for k,v in boxes.items():
    for i in range(len(v)):
        power = (k+1) * (i+1) * int(v[i][1])
        total += power

print(total)