with open('day18input.txt') as f:
    file = [i.split() for i in f.read().splitlines()]
pos, area = 0, 1

for face, n, col in file:
    n = int(col[2:-2], 16)
    if col[-2] == "0":
        pos += n
        area += n/2
    elif col[-2] == "3": area += (-n*pos + n/2)        
    elif col[-2] == "2":
        pos -= n
        area += n/2
    else: area += (n*pos + n/2)

print(area)