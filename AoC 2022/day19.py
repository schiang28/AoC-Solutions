import re
from time import time
s = time()

with open("day19input.txt") as f:
    file, total = [list(map(int, re.findall(r"\d+", i))) for i in f.read().splitlines()], 1

def get_max_geode(nextr, r1, r2, r3, r4, m1, m2, m3, m4, time):
        global maxgeode
        if nextr == 0 and r1 >= maxore: # ore
            return
        if nextr == 1 and r2 >= ob2: # clay
            return
        if nextr == 2 and (r3 >= g2 or r2 == 0): # obsidian
            return
        if nextr == 3 and r3 == 0: # geode
            return

        while time > 0:
            if nextr == 0 and m1 >= o1:
                for i in range(4): # creating ore robot
                    get_max_geode(i, r1+1, r2, r3, r4, m1-o1+r1, m2+r2, m3+r3, m4+r4, time-1)
                return
            elif nextr == 1 and m1 >= c1:
                for i in range(4): # creating clay robot
                    get_max_geode(i, r1, r2+1, r3, r4, m1-c1+r1, m2+r2, m3+r3, m4+r4, time-1)
                return
            elif nextr == 2 and m1 >= ob1 and m2 >= ob2:
                for i in range(4): # creating obsidian robot
                    get_max_geode(i, r1, r2, r3+1, r4, m1-ob1+r1, m2-ob2+r2, m3+r3, m4+r4, time-1)
                return
            elif nextr == 3 and m1 >= g1 and m3 >= g2:
                for i in range(4): # creating geo robot
                    get_max_geode(i, r1, r2, r3, r4+1, m1-g1+r1, m2+r2, m3-g2+r3, m4+r4, time-1)
                return
            m1, m2, m3, m4, time = m1+r1, m2+r2, m3+r3, m4+r4, time-1
        maxgeode = max(maxgeode, m4)

for blueprint in file[:3]:
    bpid, o1, c1, ob1, ob2, g1, g2 = blueprint
    maxore, maxgeode = max(o1, c1, ob1, g1), 0
    for i in range(4):
        get_max_geode(i, 1, 0, 0, 0, 0, 0, 0, 0, 32)
    total *= maxgeode

print(total)
print(time()-s)