from statistics import median

with open("day7input.txt") as f:
    file = list(map(int, f.read().split(",")))

# median of nunbers will have the cheapest outcome
print(sum(abs(i - int(median(file))) for i in file))
# sum of range of difference between i and j, brute force
print(min([sum((abs(i - j) + 1) * ((abs(j - i)) / 2) for j in file) for i in file]))
