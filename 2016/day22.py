with open('2016/inputs/day22.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1():
    fs = [line.replace("T", "").split() for line in lines[2:]]
    return sum(int(a[2]) != 0 and (int(a[2]) <= int(b[3])) for a in fs for b in fs)


print(part1())


def part2():
    fs = [line.replace("T", "").split() for line in lines[2:]]

    steps = 0
    w = 36
    h = 30
    empty_x = 35
    empty_y = 27
    g_x = w - 1
    g_y = 0

    # move _ to G
    while empty_x > 1:
        empty_x -= 1
        steps += 1
    while empty_y > 0:
        empty_y -= 1
        steps += 1
    while empty_x < w - 2:
        empty_x += 1
        steps += 1

    # swap G to O
    while empty_x > 0:
        g_x -= 1
        empty_x += 1
        steps += 1
        empty_y += 1
        steps += 1
        empty_x -= 1
        steps += 1
        empty_x -= 1
        steps += 1
        empty_y -= 1
        steps += 1
    g_x -= 1
    empty_x += 1
    steps += 1

    for y in range(h):
        line = ""
        for x in range(w):
            if int(fs[x * h + y][4][:-1]) > 90:
                line += "#"
            elif x == empty_x and y == empty_y:
                line += "_"
            elif x == g_x and y == g_y:
                line += "G"
            elif x == 0 and y == 0:
                line += "O"
            else:
                line += "."
        print(line)

    return steps


print(part2())
