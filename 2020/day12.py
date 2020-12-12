import re

input = open('2020/inputs/day12.txt').readlines()

def part1(s):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    facing = 0
    pos_x, pos_y = 0, 0
    for line in s:
        m = re.search(r'(\w)(\d+)', line)
        action, value = m[1], int(m[2])
        
        if action == 'N':
            pos_y -= value
        elif action == 'S':
            pos_y += value
        elif action == 'E':
            pos_x += value
        elif action == 'W':
            pos_x -= value
        elif action == 'F': 
            pos_x += value * directions[facing][0]
            pos_y += value * directions[facing][1]
        elif action == 'L':
            facing += value // 90
            facing %= 4
        elif action == 'R':
            facing -= value // 90
            facing %= 4

    return abs(pos_x) + abs(pos_y)

def part2(s):
    pos_x, pos_y = 0, 0
    way_x, way_y = 10, -1
    for line in s:
        m = re.search(r'(\w)(\d+)', line)
        action, value = m[1], int(m[2])
        
        if action == 'N':
            way_y -= value
        elif action == 'S':
            way_y += value
        elif action == 'E':
            way_x += value
        elif action == 'W':
            way_x -= value
        elif action == 'F': 
            pos_x += value * way_x
            pos_y += value * way_y
        elif action == 'L':
            for _ in range(value // 90):
                way_x, way_y = way_y, -way_x
        elif action == 'R':
            for _ in range(value // 90):
                way_x, way_y = -way_y, way_x

    return abs(pos_x) + abs(pos_y)

print(part1(input))
print(part2(input))
