num = [12,20,0,6,1,17,7]

#num = numbers.split(',')
#duplicates = ['12', '20','0','6','1','17']
turn = len(num)
current = num[-1]
seen = {v: k+1 for k, v in enumerate(num)}

while turn < 30000000:
    if current not in seen:
        seen[current] = turn
        current = 0
        #num.append('0')
        #duplicates.append(num[turn-1])
    else:
        '''ls = []
        for a in range(0, len(num)):
            if num[a] == num[turn-1]:
                ls.append(int(a))
        age = ls[-1] - ls[-2]
        num.append(str(age))'''
        prev = current
        current = turn - seen[prev]
        seen[prev] = turn
    turn += 1

print(current)