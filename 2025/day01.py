with open('2025/inputs/day01.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    result = 0
    pos = 50
    for line in lines:
        direction, dist = line[0], int(line[1:])
        if direction == "L":
            pos -= dist
        else:
            pos += dist
        pos %= 100
        if pos == 0:
            result += 1
    return result

def part2():
    result = 0
    pos = 50
    for line in lines:
        direction, dist = line[0], int(line[1:])
        if direction == "L":
            for _ in range(dist):
                pos -= 1
                pos %= 100
                if pos == 0:
                    result += 1
        else:
            for _ in range(dist):
                pos += 1
                pos %= 100
                if pos == 0:
                    result += 1
                
    return result


print(part1())
print(part2())
