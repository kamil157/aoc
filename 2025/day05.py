with open('2025/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    ranges = []
    fresh = 0
    for line in lines:
        if "-" in line:
            ranges.append(tuple(int(n) for n in line.split("-")))
        elif line:
            n = int(line)
            for low, high in ranges:
                if low <= n <= high:
                    fresh += 1
                    break
    return fresh

def part2():
    ranges = []
    fresh = 0
    for line in lines:
        if "-" in line:
            _range = tuple(int(n) for n in line.split("-"))
            ranges.append(_range)

    ranges = sorted(ranges)
    current = ranges[0]
    for nxt in ranges[1:]:
        if current[1] >= nxt[0]:
            current = current[0], max(current[1], nxt[1])
        else:
            fresh += current[1] - current[0] + 1
            current = nxt

    return fresh + current[1] - current[0] + 1

        
print(part1())
print(part2())
