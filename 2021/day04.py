input = open('2021/inputs/day04.txt').read().split('\n\n')

def part1(s):
    nums = s[0]
    print(nums)

    boards = s[1:]

    for board in boards:
        print(board, end='\n\n')


    boards = [[[int(n) for n in line.split()] for line in board.split('\n')] for board in boards ]
    for board in boards:
        print(board, end='\n')


print(part1(input))
