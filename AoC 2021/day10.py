from statistics import median

with open("day10input.txt") as f:
    file = f.read().splitlines()

score = dict(zip(")]}>", [3, 57, 1197, 25137]))
addscore = dict(zip("([{<", [1, 2, 3, 4]))
reverse = dict(zip("{(<[", "})>]"))
pt1, pt2 = 0, []

for line in file:
    letters, corrupted = [], False
    for l in line:
        if l in "{[<(":
            letters.append(l)
        else:
            if l != reverse[letters[-1]]:
                pt1 += score[l]
                corrupted = True
                break
            del letters[-1]
    if not corrupted:
        addend = "".join(letters)[::-1]
        temp = 0
        for char in addend:
            temp *= 5
            temp += addscore[char]
        pt2.append(temp)

print(pt1)
print(median(pt2))
