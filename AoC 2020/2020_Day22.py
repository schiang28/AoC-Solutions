cards = '''Player 1:
27
29
30
44
50
5
33
47
34
38
36
4
2
18
24
16
32
21
17
9
3
22
41
31
23

Player 2:
25
1
15
46
6
13
20
12
10
14
19
37
40
26
43
11
48
45
49
28
35
7
42
39
8'''


cards = cards.split('Player ')
cards.pop(0)

player1 = cards[0].split()
player2 = cards[1].split()

del player1[0]
del player2[0]

seen = set()
while len(player1) > 0 and len(player2) > 0:
    t = (tuple(player1), tuple(player2))
    if t in seen:
        break
    seen.add(t)
    c1, c2 = int(player1[0]), int(player2[0])
    if c1 > c2:
        player1.append(str(c1))
        player1.append(str(c2))
        del player1[0]
        del player2[0]
    else:
        player2.append(str(c2))
        player2.append(str(c1))
        del player2[0]
        del player1[0]

print(player1)
print(player2)

total = 0
for i in range(1, len(player1)+1):
    total += int(player1[-i]) * i
print(total)