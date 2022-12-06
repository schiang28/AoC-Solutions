with open("day6input.txt") as f:
    file = f.read().splitlines()[0]

n = 14
for char in range(n - 1, len(file)):
    if len(set([file[char - i] for i in range(n)])) == n:
        print(char + 1)
        break
