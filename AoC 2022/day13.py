from itertools import groupby

with open("day13input.txt") as f:
    file = [list(g) for k, g in groupby(f.read().splitlines(), key=bool) if k]
packets = [[[2]], [[6]]]
[packets.extend([eval(i[0]), eval(i[1])]) for i in file]

def compare(left, right):
    for i in range(max(len(left), len(right))):
        if i < len(left) and i < len(right):
            if isinstance(left[i], int) and isinstance(right[i], int):
                if left[i] < right[i]:
                    return True
                if right[i] < left[i]:
                    return False
            elif isinstance(left[i], int) and isinstance(right[i], list):
                state = compare([left[i]], right[i])
                if state:
                    return True
                if state == False:
                    return False
            elif isinstance(left[i], list) and isinstance(right[i], int):
                state = compare(left[i], [right[i]])
                if state:
                    return True
                if state == False:
                    return False
            else:
                state = compare(left[i], right[i])
                if state:
                    return True
                if state == False:
                    return False
        else:
            if i >= len(left):
                return True
            else:
                return False

def bubble_sort(packets):
    swapped = False
    for n in range(len(packets)-1, 0, -1):
        for i in range(n):
            if compare(packets[i], packets[i + 1]) == False:
                swapped = True
                packets[i], packets[i + 1] = packets[i + 1], packets[i]
        if not swapped:
            return

print(sum([i + 1 for i in range(len(file)) if compare(eval(file[i][0]), eval(file[i][1]))]))
bubble_sort(packets)
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))