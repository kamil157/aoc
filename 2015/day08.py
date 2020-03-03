def part1():
    with open('day08.txt') as f:
        total = 0
        for line in f.readlines():
            line = line.strip()
            decoded_string = bytes(line, "utf-8").decode("unicode_escape")
            total += len(line) - (len(decoded_string) - 2)

    return total


def part2():
    with open('day08.txt') as f:
        total = 0
        for line in f.readlines():
            line = line.strip()
            total += 2 + line.count('"') + line.count('\\')

    return total


print(part1())
print(part2())
