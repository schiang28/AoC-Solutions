with open("day20input.txt") as f:
    file = f.read().splitlines()
alg, inp = file[0], file[2:]
deltas = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1))
# only works for input not sample, infinitely surrounding symbols alternates between # and . due to first char of alg

for n in range(50):
    sy = "." if n % 2 == 0 else "#"
    inp.insert(0, sy * len(inp[0]))
    inp.append(sy * len(inp[0]))
    inp = [sy + i + sy for i in inp]
    inpcopy = [list(i) for i in inp.copy()]

    for r in range(len(inpcopy)):
        for c in range(len(inpcopy[r])):
            binstr = ""
            for d in deltas:
                rr, cc = r + d[0], c + d[1]
                if not (0 <= rr < len(inpcopy)) or not (0 <= cc < len(inpcopy[0])):
                    binstr += sy
                else:
                    binstr += inp[rr][cc]
            inpcopy[r][c] = alg[int(binstr.replace("#", "1").replace(".", "0"), 2)]

    inp = ["".join(i) for i in inpcopy]

print(sum([i.count("#") for i in inp]))