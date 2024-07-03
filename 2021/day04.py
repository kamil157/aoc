with open('2021/inputs/day04.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def bingo(called, board):
    def line_win(b, i):
        return all(b[i][j] in called for j in range(size))

    size = len(board)
    return any(line_win(board, i) or line_win(list(zip(*board)), i) for i in range(size))


def score(called, board):
    return sum(n for row in board for n in row if n not in called)


def part1(index):
    nums = [int(n) for n in lines[0].split(",")]
    boards = [[[int(n) for n in line.split()]
               for line in board.split('\n')] for board in lines[1:]]

    wins = []
    called = set()
    for n in nums:
        called.add(n)
        for board in boards:
            if bingo(called, board):
                wins.append(n * score(called, board))
                boards.remove(board)

    return wins[index]


print(part1(0))
print(part1(-1))
