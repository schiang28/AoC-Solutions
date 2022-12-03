import re
from itertools import combinations
from math import sqrt
from collections import Counter
from itertools import groupby

with open("dayxinput.txt") as f:
    # list of integers
    file = list(map(int, f.read().splitlines()))
    # list of strings
    file = f.read().splitlines()

# splits list on empty entries
file = ["jeff", "ham", "boat", "", "my", "name", "hello", "", "hello", "world"]
# groups by whitespace
file = [list(g) for k, g in groupby(file, key=bool) if k]
# groups by white space then turns to integer, only if one int on line
file = [list(map(int, g)) for k, g in groupby(file, key=bool) if k]


# if multiple things separated by space on one line, created 3d array
file = [[i.split() for i in j] for j in file]
file = [[list(map(int, i.split())) for i in j] for j in file]

# removes all empty entries in a list
print([x for x in file if x])

# groupby unique elements(string)
[k for k, g in groupby("AAAABBBCCDAABBB")]  # --> ['A', 'B', 'C', 'D', 'A', 'B']
[
    list(g) for k, g in groupby("AAAABBBCCD")
]  # --> [['A', 'A', 'A', 'A'], ['B', 'B', 'B'], ['C', 'C'], ['D']]

# convert binary to denary
x = "10110"
print(int(x, 2))
x = "{0:b}".format(37)  # convert int to binary

