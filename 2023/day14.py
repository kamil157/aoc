with open('2023/inputs/day14.txt') as f:
    lines = f.read().strip().split('\n')


def move_line(line):
    return '#'.join(''.join(sorted(part, reverse=True)) for part in line.split("#"))


def move(lines):
    return [move_line(line) for line in lines]


def transpose(lines):
    return [''.join(row) for row in zip(*lines)]


def total_load(lines):
    return sum((len(lines) - i) * line.count('O') for i, line in enumerate(lines))


def part1(lines):
    return total_load(transpose(move(transpose(lines))))


print(part1(lines))


def spin(lines):
    lines = transpose(move(transpose(lines)))
    lines = move(lines)
    lines = transpose(move(transpose(lines[::-1])))[::-1]
    lines = [line[::-1] for line in move(line[::-1] for line in lines)]
    return lines


def part2(lines):
    results = {}
    loads = []
    i = 0
    while True:
        lines = spin(lines)
        load = total_load(lines)
        if "".join(lines) in results:
            length = i - results["".join(lines)]
            return loads[(1000000000 - i) % length - length - 1 + i]
        results["".join(lines)] = i
        loads.append(load)
        i += 1


print(part2(lines))
