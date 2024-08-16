import collections
import copy
from intcode import Intcode

with open('2019/inputs/day15.txt') as f:
    input = f.read()


def repair(s):
    intcode = Intcode(s)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    x = y = 0
    length = 0
    visited = set()
    visited.add((x, y))
    map = {(0, 0): 'D'}
    q = collections.deque()
    for command in [1, 2, 3, 4]:
        dir = directions[command - 1]
        q.append((x + dir[0], y + dir[1], command,
                 length + 1, copy.deepcopy(intcode)))

    while q:
        x, y, command, length, intcode = q.popleft()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        intcode.input(command)
        status = intcode.run()

        if status == 0:
            map[x, y] = '#'
            continue
        elif status == 1:
            map[x, y] = '.'
            for command in [1, 2, 3, 4]:
                dir = directions[command - 1]
                q.append((x + dir[0], y + dir[1], command,
                         length + 1, copy.deepcopy(intcode)))

        elif status == 2:
            map[(x, y)] = '.'
            oxygen = length, x, y
        else:
            assert False

    return oxygen, map


def draw_map(d):
    min_x = min(pos[0] for pos in d.keys())
    max_x = max(pos[0] for pos in d.keys())
    min_y = min(pos[1] for pos in d.keys())
    max_y = max(pos[1] for pos in d.keys())
    map = [['?'] * (max_x - min_x + 1) for y in range(max_y - min_y + 1)]

    for (x, y), tile in d.items():
        map[y - min_y][x - min_x] = tile
    for row in map:
        print(''.join(row))


def oxygen(s):
    oxygen, d = repair(s)
    print(oxygen[0])  # part 1
    time = 0
    q = collections.deque()
    q.append((oxygen[1], oxygen[2], time))

    while q:
        x, y, next_time = q.popleft()
        if d[x, y] != '.':
            continue

        time = next_time
        d[x, y] = 'O'

        for dir in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            q.append((x + dir[0], y + dir[1], time + 1))

    # draw_map(d)
    return time


print(oxygen(input))
