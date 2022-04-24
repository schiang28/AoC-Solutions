from itertools import groupby

with open("day4input.txt") as f:
    file = f.read().splitlines()

# parsing file
numbers = list(map(int, file[0].split(",")))
del file[0]
boards = [list(g) for k, g in groupby(file, key=bool) if k]
for board in range(len(boards)):
    for row in range(len(boards[board])):
        boards[board][row] = boards[board][row].split()


def bingo(board):
    for row in board:
        if row.count("1000") == len(row):
            return True
    for i in range(len(board[0])):
        column = [x[i] for x in board]
        if column.count("1000") == len(column):
            return True
    return False


def cancel(board):
    for row in range(len(board)):
        board[row] = ["-1" for x in board[row]]
    return board


winning = []

for i in numbers:
    for board in range(len(boards)):
        for row in range(len(boards[board])):
            boards[board][row] = [
                "1000" if x == str(i) else x for x in boards[board][row]
            ]
    for winner in range(len(boards)):
        if bingo(boards[winner]):
            unmarked = 0
            for row in boards[winner]:
                for num in row:
                    if num != "1000":
                        unmarked += int(num)
            winning.append(unmarked * i)
            boards[winner] = cancel(boards[winner])

# list 'winning' is the order in which the boards win
print(winning[0], winning[-1])
