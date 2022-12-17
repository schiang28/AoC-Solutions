with open("day17input.txt") as f:
    file = f.read().splitlines()[0]
rocks, height, count, cycle = set(), 0, 0, {}
shapes = [[(3,0), (4,0), (5,0), (6,0)], [(3,1), (4,1), (5,1), (4,0), (4,2)], [(3,0), (4,0), (5,0), (5,1), (5,2)], [(3,0), (3,1), (3,2), (3,3)], [(3,0), (3,1), (4,0), (4,1)]]

def clear(r):
    if any(i[0] > 7 for i in r) or any(i[0] < 1 for i in r) or any(i in rocks for i in r) or any(i[1] <= 0 for i in r):
        return False
    return True

def right(r):
    return [(i[0] + 1, i[1]) for i in r]

def left(r):
    return [(i[0] - 1, i[1]) for i in r]

def down(r):
    return [(i[0], i[1] - 1) for i in r]


for r in range(1000000000000):
    rock = [(i[0], i[1] + height + 4) for i in shapes[r % 5]]

    state = r % 5, count % len(file)
    if state in cycle:
        if 1000000000000 - r % cycle[state][0] - r == 0:
            print(height + (cycle[state][1] - height) * (1000000000000 - r // cycle[state][0] - r))
            break
    else:
        cycle[state] = r, height

    while True:
        jet = file[count % len(file)]
        if jet == ">":
            if clear(right(rock)):
                rock = right(rock)
        else:
            if clear(left(rock)):
                rock = left(rock)
        count += 1

        if clear(down(rock)):
            rock = down(rock)
        else:
            rocks.update(rock)
            height = max(height, max([i[1] for i in rock]))
            break