with open("day8input.txt") as f:
    file = [list(map(int, i)) for i in f.read().splitlines()]

visible, scores = 0, []

for r in range(len(file)):
    for c in range(len(file[r])):
        score = 1
        if r == 0 or r == (len(file) - 1) or c == 0 or c == (len(file[r]) - 1):
            visible += 1
        else:
            s1 = [file[d][c] for d in range(r + 1, len(file))]
            s2 = [file[d][c] for d in range(0, r)]
            s3 = [file[r][d] for d in range(c + 1, len(file[r]))]
            s4 = [file[r][d] for d in range(0, c)]
            for sides in [s1, s2, s3, s4]:
                if all(i < file[r][c] for i in sides):
                    visible += 1
                    break

            for trees in [s1, s2[::-1], s3, s4[::-1]]:
                temp = 0
                for t in trees:
                    temp += 1
                    if t >= file[r][c]:
                        break
                score *= temp
            scores.append(score)

print(visible)
print(max(scores))
