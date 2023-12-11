with open("day9input.txt") as f:
    file = [list(map(int, i.split())) for i in f.read().splitlines()]

def next_val(seq):
    if all(i == 0 for i in seq): return 0
    new_seq = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    return seq[-1] + next_val(new_seq)

total = [next_val(seq[::-1]) for seq in file] # seq for p1, seq[::-1 for p2]
print(sum(total))