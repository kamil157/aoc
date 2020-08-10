from copy import deepcopy

input = open('2016/inputs/day01.txt').read()

def part1(s):
    pos = [0, 0]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    facingIdx = 0
    visited = set()
    first = None

    for line in input.split(', '):
        dir = line[0]
        if dir == 'L':
            facingIdx -= 1
        else:
            facingIdx += 1
        facingIdx %= len(directions)
        
        dist = int(line[1:])
        for _ in range(dist):
            pos[0] += directions[facingIdx][0]
            pos[1] += directions[facingIdx][1]
            if tuple(pos) in visited and first is None:
                first = deepcopy(pos)
            visited.add(tuple(pos))

    return pos[0] + pos[1], first[0] + first[1]

print(part1(input))
