import math

with open("day4input.txt") as f:
    file = [i.split(" | ") for i in f.read().splitlines()]
cards = [[set(map(int, i[0].split()[2:])), set(map(int, i[1].split()))] for i in file]
winning = [card[0].intersection(card[1]) for card in cards]

total = [math.floor(2**(len(winning[card])-1)) for card in range(len(cards))]
print(sum(total))

copies, points = [1] * len(cards), [0] * len(cards)
for game in range(len(cards)):
    while copies[game] > 0:
        for i in range(1, len(winning[game])+1): copies[game+i] += 1
        points[game] += 1
        copies[game] -= 1
print(sum(points))