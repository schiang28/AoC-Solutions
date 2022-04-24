import re
coordinates = '''
F8
N2
F32
F17
E4
N4
R90
S2
R90
E3
L90
N5
E2
N2
W5
F78
L180
F19
R90
S1
E2
L180
E1
S5
E4
F62
R180
F16
S2
F8
R180
S1
L90
E4
R90
S3
E5
R180
F87
N2
E2
R90
N2
F2
R90
N5
W4
L90
F42
N1
F93
F87
E2
S4
F73
L270
S2
W3
F48
W5
L180
N1
F53
R90
S2
R90
N2
E2
S5
W3
R90
E2
R90
W1
L180
F29
W1
F56
R90
F34
F74
S1
R90
L90
W4
L90
W5
L90
W1
L90
N5
E2
S2
F58
N5
L90
S4
L90
R270
W4
S4
E3
R180
S4
W3
R90
F36
R90
W1
F73
S4
E1
L90
S4
W5
L90
F20
W3
L180
E3
S1
R90
S5
W3
L90
E5
W2
F21
N4
F83
W4
F48
W3
F4
L90
N5
R270
E1
S5
L180
F44
W5
R180
S3
F30
N5
F87
L90
F69
S5
E1
R90
E2
S3
F40
W4
F97
W5
F20
L180
N5
L90
E5
N3
L90
F13
N2
F38
S5
F27
E5
L180
F59
N3
F2
R90
N2
R90
F56
L90
N4
R90
F12
F34
N3
F93
L270
W3
F74
W4
R90
E2
L180
W3
F12
N5
W1
F98
E4
R180
S1
W5
R90
F96
N2
L90
F36
S1
F3
W3
F100
N5
R90
F33
W3
N5
E3
R90
F33
N5
E2
N1
L90
F84
L270
E1
F28
R180
W3
L90
S2
F88
L90
W2
N1
F3
R90
F56
N1
N4
L90
R90
F97
E5
N4
F38
N1
R90
W1
F60
W3
N1
F59
E1
N3
E3
L180
N1
F53
S1
E2
R90
E2
F6
R180
F36
R180
W2
F81
R90
E4
R90
F97
L90
W1
S1
E5
L180
F34
R180
F64
E2
R180
W3
S5
L90
E4
F12
F58
W3
N3
F77
N4
F32
R90
N2
E4
L90
S5
E1
N5
F44
R90
F5
E4
R90
N5
E4
R180
W3
L90
N1
F1
S3
E5
R180
S3
F86
S5
F61
W3
R270
W5
R90
F26
R180
F92
S5
L90
E5
N5
F82
R90
F22
R90
F23
S1
F42
N4
F76
E1
S1
W3
S2
L90
F19
E4
F41
E2
N2
L90
F34
S4
F20
W3
F18
S1
R90
N3
F38
W3
R90
W4
R90
E2
R90
F10
L90
N4
F94
S1
W3
R180
W5
F74
R90
S4
L180
S3
F74
N5
S4
L90
F34
S2
E5
N5
F28
L90
E1
F31
N1
L90
L90
W2
N5
R90
F1
N5
F48
W2
F50
N2
F62
S4
L90
W5
N1
F12
W3
R90
R90
F75
N5
F69
E3
F19
N2
F77
E1
N4
R180
E3
N2
L90
N1
W1
S4
F85
W1
R90
F74
E5
F73
E4
S3
W4
S5
L90
F49
S5
E5
F5
W2
F58
R90
W5
F53
S4
F86
N2
F88
E5
F59
E1
F56
W2
N4
W4
R180
F16
F25
R180
N3
F4
W4
S4
F98
E5
L90
W4
S1
E2
R90
F96
L270
E1
N1
F55
S1
F10
R90
W2
L90
N5
R90
N4
E4
L90
F52
S3
F43
E2
R90
S3
R90
N4
E1
N4
F15
E3
R270
L180
N2
F43
L90
W2
F19
L90
S5
F58
E4
S4
L90
W1
F9
N4
F38
S5
L90
W1
F39
W5
F83
L180
F99
L90
E3
S2
R90
N3
F35
N1
N3
L90
N4
W5
F26
R270
N2
F7
N1
F16
S4
L90
S5
L180
F5
W1
F32
S2
N3
F82
N4
R90
F27
R180
F20
S1
E3
L90
W3
F23
L180
N3
F34
W1
N3
S2
F80
E5
F65
L90
E5
N1
F80
R90
W3
L90
N1
L180
S1
F65
E3
S1
W3
F89
S1
F24
E5
F85
W1
F87
S1
R90
S4
F3
S3
F23
N4
L90
N5
R90
N2
R90
S2
W4
S2
F95
L90
F52
W1
N5
L90
N4
S3
E3
R90
N2
E1
R180
W4
F82
L180
E5
L90
E4
F65
W5
R90
W5
N5
L180
N4
F22
W3
S4
F60
R90
E5
N3
F32
S2
F80
R90
F18
S3
L90
F90
E3
L90
N3
E5
F79
N5
W4
S5
F100
N1
E3
S3
F49
R180
S3
E2
F1
W1
F5
R180
S5
W3
S3
F67
R270
N3
W3
N1
W3
F37
L90
N3
L90
F68
N3
W4
W2
F26
N3
L90
W3
S2
F7
W3
E3
L270
F64
R90
E4
R90
W3
N1
W1
F98
R270
W5
F45
R90
F49
E4
S2
F58
F56
W3
F57
E3
S5
R180
E3
F82
F57
S3
W2
R90
E2
R90
F95
W4
F85
E3
N3
R90
E5
F31
R90
F20
R90
N5
E3
S4
R180
W1
N5
F72
L90
E3
F46
R180
F18
E3
F48
S2
F84
W3
F88
F44
S2
E4
F77
L90
N4
L90
E2
F22
E5
L90
F79
W1
R90
F41
R180
F54'''

coordinates = coordinates.split()

wx = 10
wy = 1

x = 0
y = 0
'''ls = ["n", "e", "s", "w"]
d = ls[1]'''

# green is part 1

for i in coordinates:
    direct = i[0]
    num = int(i[1:])
    if direct == "F":
        '''if d == "n":
            y += num*wy
        elif d == "e":
            x += num*wx
        elif d == "s":
            y -= num*wy
        else:
            x -= num*wx'''
        y += num*wy
        x += num*wx
    elif direct == "N":
        wy += num
    elif direct == "E":
        wx += num
    elif direct == "S":
        wy -= num
    elif direct == "W":
        wx -= num
    elif direct == "L":
        degree = int(num / 90)
        '''if d == "w":
            d = ls[3-degree]
        elif d == "n":
            d = ls[0-degree]
        elif d == "e":
            d = ls[1-degree]
        else:
            d = ls[2-degree]'''
        for j in range(0, degree):
            wx, wy = -wy, wx
    else:
        degree = int(num / 90)
        '''if d == "w":
            d = ls[(3+degree) % 4]
        elif d == "n":
            d = ls[0+degree]
        elif d == "e":
            d = ls[(1+degree) % 4]
        else:
            d = ls[(2+degree) % 4]'''
        for j in range(0, degree):
            wx, wy = wy, -wx
    print(x, y)

print(abs(x)+abs(y))
