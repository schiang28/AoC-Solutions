from itertools import permutations

numbers = '''
71
30
134
33
51
115
122
38
61
103
21
12
44
129
29
89
54
83
96
91
133
102
99
52
144
82
22
68
7
15
93
125
14
92
1
146
67
132
114
59
72
107
34
119
136
60
20
53
8
46
55
26
126
77
65
78
13
108
142
27
75
110
90
35
143
86
116
79
48
113
101
2
123
58
19
76
16
66
135
64
28
9
6
100
124
47
109
23
139
145
5
45
106
41'''

ls = [0]
num = numbers.split()
for x in num:
    ls.append(int(x))

built_in = max(ls) + 3
ls.sort()
ls.append(built_in)
print(ls)

count1 = 0
count3 = 0
for i in range(0, len(ls)-1):
    dif = ls[i+1]-ls[i]
    if dif == 1:
        count1 += 1
    elif dif == 3:
        count3 += 1

print("part 1", count1 * count3)

d = {}


def function(i):
    if i == len(ls) - 1:
        return 1
    if i in d:
        return d[i]
    ans = 0
    for j in range(i+1, len(ls)):
        if ls[j] - ls[i] <= 3:
            ans += function(j)
    d[i] = ans
    return ans


print("part 2", function(0))
print(d)
