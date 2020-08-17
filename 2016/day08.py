import re

input = open('2016/inputs/day08.txt').readlines()

def print_screen(screen):
    for line in screen:
        print(' '.join(line))

def transpose(screen):
    return list(map(list, zip(*screen)))

def rotate_row(screen, y, by):
    screen[y] = screen[y][-by:] + screen[y][:-by]

def part1(s):
    screen = [[' ' for _ in range(50)] for _ in range(6)]

    for line in s:
        if m := re.search(r'rect (\d+)x(\d+)', line):
            w = int(m.group(1))
            h = int(m.group(2))
            for x in range(w):
                for y in range(h):
                    screen[y][x] = '#'

        elif m := re.search(r'rotate row y=(\d+) by (\d+)', line):
            y = int(m.group(1))
            by = int(m.group(2))
            rotate_row(screen, y, by)

        elif m := re.search(r'rotate column x=(\d+) by (\d+)', line):
            x = int(m.group(1))
            by = int(m.group(2))
            screen = transpose(screen)
            rotate_row(screen, x, by)
            screen = transpose(screen)

    print_screen(screen)      
    return sum(line.count('#') for line in screen)


print(part1(input))
