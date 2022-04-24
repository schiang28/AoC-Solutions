from itertools import product

d, rolls, s, p, turn, universe = 1, 0, [0, 0], [6, 8], 0, {}

while True:
    turn %= 2
    p[turn] = (p[turn] + (3 * d + 3) - 1) % 10 + 1
    rolls += 3
    s[turn] += p[turn]
    d += 3
    if s[turn] >= 1000:
        break
    turn += 1

print(rolls * min(s))


def roll(p1, p2, s1=0, s2=0):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in universe:
        return universe[(p1, p2, s1, s2)]
    ans = (0, 0)
    for a, b, c in product([1, 2, 3], [1, 2, 3], [1, 2, 3]):
        np1 = (a + b + c + p1) % 10
        ns1 = s1 + np1 + 1
        ns2, ns1 = roll(p2, np1, s2, ns1)
        ans = (ans[0] + ns1, ans[1] + ns2)
    universe[(p1, p2, s1, s2)] = ans
    return ans


print(max(roll(5, 7)))