input = open('2016/inputs/day02.txt').read()

keypad1 = {
    (0, 0): '1',
    (1, 0): '2',
    (2, 0): '3',
    (0, 1): '4',
    (1, 1): '5',
    (2, 1): '6',
    (0, 2): '7',
    (1, 2): '8',
    (2, 2): '9',
}
pos1 = [1, 1]

keypad2 = {
    (2, 0): '1',
    (1, 1): '2',
    (2, 1): '3',
    (3, 1): '4',
    (0, 2): '5',
    (1, 2): '6',
    (2, 2): '7',
    (3, 2): '8',
    (4, 2): '9',
    (1, 3): 'A',
    (2, 3): 'B',
    (3, 3): 'C',
    (2, 4): 'D',
}
pos2 = [0, 2]

def part1(s, keypad, pos):
    directions = { 'L': [-1, 0], 'R': [1, 0], 'U': [0, -1], 'D': [0, 1] }
    result = ''
    for line in s.split():
        for dir in line:
            x = directions[dir][0] + pos[0]
            y = directions[dir][1] + pos[1]
            if (x, y) in keypad:
                pos = [x, y]
                
        result += keypad[tuple(pos)]

    return result

print(part1(input, keypad1, pos1))
print(part1(input, keypad2, pos2))
