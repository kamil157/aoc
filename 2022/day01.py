input = open('2022/inputs/day01.txt').readlines()


def get_elves(s):
    elves = []
    calories = 0
    for line in s:
        num = line.strip()
        if num == "":
            elves.append(calories)
            calories = 0
            continue
        calories += int(num)
    return elves


def part1(s):
    return max(get_elves(s))


def part2(s):
    return sum(sorted(get_elves(s), reverse=True)[:3])


print(part1(input))
print(part2(input))
