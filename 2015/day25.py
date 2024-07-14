from parse import parse

with open('2015/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip()


def part1():
    r, c = parse(
        "To continue, please consult the code grid in the manual.  Enter the code at row {:d}, column {:d}.", lines)

    code = 20151125
    n = sum(range(c + 1)) + sum(range(c, c + r - 1))

    for _ in range(1, n):
        code *= 252533
        code %= 33554393
    return code


print(part1())
