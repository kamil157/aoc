with open('2023/inputs/day01.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    result = 0
    for line in lines:
        digits = [c for c in line if c.isdigit()]
        result += int(digits[0] + digits[-1])
    return result


print(part1())


def part2():
    words = {"one": 1, "two": 2, "three": 3, "four": 4,
             "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    result = 0
    for line in lines:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for length in range(3, 6):
                if line[i:i+length] in words:
                    digits.append(str(words[line[i:i+length]]))

        result += int(digits[0] + digits[-1])
    return result


print(part2())
