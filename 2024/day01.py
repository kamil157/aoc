with open('2024/inputs/day01.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve():
    list_left = sorted(int(line.split()[0]) for line in lines)
    list_right = sorted(int(line.split()[1]) for line in lines)

    lists = zip(list_left, list_right)

    part1 = part2 = 0
    for l, r in lists:
        part1 += abs(l - r)
        part2 += l * list_right.count(l)

    return part1, part2


print(solve())
