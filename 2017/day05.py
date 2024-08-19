with open('2017/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def solve(part2):
    offsets = list(lines)
    pos = 0
    result = 0
    while pos < len(offsets):
        jump = int(offsets[pos])
        if part2 and jump >= 3:
            offsets[pos] = jump - 1
        else:
            offsets[pos] = jump + 1
        pos += jump
        result += 1
    return result


print(solve(False))
print(solve(True))
