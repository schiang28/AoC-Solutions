with open("day3input.txt") as f:
    file = f.read().splitlines()

s = ""
for i in range(len(file[0])):
    pos = [x[i] for x in file]  # list comp of every char at position i in file
    if pos.count("1") > pos.count("0"):
        s += "1"
    else:
        s += "0"

gamma = int(s, 2)
epsilon = int("".join(["1" if i == "0" else "0" for i in s]), 2)
print(gamma * epsilon)


def part2(file, q, w):
    for i in range(len(s)):
        if len(file) > 1:
            pos = [x[i] for x in file]
            if pos.count("1") >= pos.count("0"):
                file = [char for char in file if char[i] == q]
            else:
                file = [char for char in file if char[i] == w]
        else:
            break

    return int(file[0], 2)


oxyfile, co2file = file.copy(), file.copy()
oxygen_rating = part2(oxyfile, "1", "0")  # keeps the max
co2_rating = part2(co2file, "0", "1")  # keeps the min
print(oxygen_rating * co2_rating)  # PART 2
