
with open('2022/inputs/day10.txt') as f:
    lines = f.read().strip().split('\n')


def run_program():
    x = 1
    cycle = 1
    values = {cycle: x}

    for line in lines:
        if line == "noop":
            cycle += 1
            values[cycle] = x
        if line[:4] == "addx":
            cycle += 1
            values[cycle] = x
            x += int(line[5:])
            cycle += 1
            values[cycle] = x
    return values


def part1():
    total = 0
    values = run_program()

    for cycle in [20, 60, 100, 140, 180, 220]:
        total += values[cycle] * cycle
    return total


print(part1())


def part2():
    values = run_program()

    for y in range(6):
        line = ""
        for x in range(40):
            if values[y * 40 + x + 1] in [x - 1, x, x + 1]:
                line += "##"
            else:
                line += ".."
        print(line)


print(part2())
