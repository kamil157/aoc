from itertools import permutations
from parse import parse, search

with open('2016/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1(initial):
    password = list(initial)
    for line in lines:
        if m := parse("swap position {:d} with position {:d}", line):
            password[m[0]], password[m[1]] = password[m[1]], password[m[0]]
        elif m := parse("swap letter {} with letter {}", line):
            a = password.index(m[0])
            b = password.index(m[1])
            password[a], password[b] = password[b], password[a]
        elif m := search("rotate {} {:d} step", line):
            offset = m[1] if m[0] == "left" else -m[1]
            password = password[offset:] + password[:offset]
        elif m := parse("rotate based on position of letter {}", line):
            index = password.index(m[0])
            offset = 1 + index
            offset += 1 if index >= 4 else 0
            offset %= len(password)
            password = password[-offset:] + password[:-offset]
        elif m := parse("reverse positions {:d} through {:d}", line):
            password[m[0]:m[1] + 1] = password[m[0]:m[1] + 1][::-1]
        elif m := parse("move position {:d} to position {:d}", line):
            c = password.pop(m[0])
            password.insert(m[1], c)
    return "".join(password)


print(part1("abcdefgh"))


def part2():
    for password in permutations("abcdefgh"):
        if part1(password) == "fbgdceah":
            return "".join(password)


print(part2())
