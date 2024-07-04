from functools import reduce


with open('2021/inputs/day10.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}


def analyze(line):
    stack = []
    for c in line:
        if c in "([{<":
            stack.append(c)
        else:
            if chunks[stack.pop()] != c:
                return c, stack
    return "", stack


def part1():
    points = 0
    scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
    for line in lines:
        if illegal := analyze(line)[0]:
            points += scoring[illegal]
    return points


print(part1())


def part2():
    scoring = {")": 1, "]": 2, "}": 3, ">": 4}
    scores = []
    for line in lines:
        illegal, stack = analyze(line)
        if not illegal:
            complete = [chunks[c] for c in stack[::-1]]
            scores.append(reduce(
                lambda acc, c: acc * 5 + scoring[c], complete, 0))

    return sorted(scores)[len(scores) // 2]


print(part2())
