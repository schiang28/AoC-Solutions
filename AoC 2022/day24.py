with open("day24input.txt") as f:
    file = f.read().splitlines()
blizzard, xbound, ybound, walls = [], len(file[0]) - 2, len(file) - 2, set()
move = {"^": (0, -1), ">": (1, 0), "<": (-1, 0), "v": (0, 1)}

for r in range(len(file)):
    for c in range(len(file[r])):
        if file[r][c] in '^><v':
            blizzard.append((c, r, move[file[r][c]]))
        if file[r][c] == "#":
            walls.add((c,r))
    
def get_next_state(time):
    squares = walls.copy()
    for x,y,(dx,dy) in blizzard:
        nx, ny = x-1+dx*time, y-1+dy*time
        squares.add((1+nx%xbound, 1+ny%ybound))
    return squares

def nexts(square, blocked):
    s = []
    x,y = square
    ls = list(move.values())
    ls.append((0,0))
    for d in ls:
        if (nx:=x+d[0],ny:=y+d[1]) not in blocked: 
            s.append((nx,ny))
    return s

def get_min_time(pos, goal, stime):
    Q, T = set(), [(stime, pos)]
    while T:
        time, square = T.pop(0)
        time += 1
        for i in nexts(square, get_next_state(time%(xbound*ybound))):
            if (time, i) not in Q:
                if i == goal:
                    return time
                Q.add((time, i))
                T.append((time, i))


ans = get_min_time(ans := (1,0), (xbound, ybound+1), 0)
print(ans)
trip2 = get_min_time((xbound, ybound+1), (1,0), ans)
print(get_min_time((1,0), (xbound, ybound+1), trip2))