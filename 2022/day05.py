import re

with open('2022/inputs/day05.txt') as f:
    lines = f.read().split('\n')


def move_boxes1(stacks, count, src, dst):
    for i in range(count):
        stacks[dst].insert(0, stacks[src].pop(0))


def move_boxes2(stacks, count, src, dst):
    x = stacks[src][:count]
    stacks[src] = stacks[src][count:]
    x.extend(stacks[dst])
    stacks[dst] = x


def part1(move_boxes):
    boxes = []
    moves = []
    for line in lines:
        if line.startswith('move'):
            moves.append(line)
        elif line.startswith(' 1'):
            count = max(map(int, line.split()))
        else:
            boxes.append(line)

    stacks = [[] for i in range(count)]
    for line in boxes:
        for i in range(count):
            try:
                box = line[4 * i + 1]
            except IndexError:
                box = ' '
            if box != ' ':
                stacks[i].append(box)

    for move in moves:
        groups = re.search(r'move (\d+) from (\d+) to (\d+)', move)
        count, src, dst = int(groups.group(1)), int(groups.group(2)) - 1, int(groups.group(3)) - 1
        move_boxes(stacks, count, src, dst)

    return ''.join(s[0] for s in stacks)


print(part1(move_boxes1))
print(part1(move_boxes2))
