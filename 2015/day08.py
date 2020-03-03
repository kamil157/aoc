def part1():
    return sum(len(s) - (len(bytes(s, "utf-8").decode("unicode_escape")) - 2) for s in open('2015/inputs/day08.txt'))

def part2():
    return sum(2 + s.count('"') + s.count('\\') for s in open('2015/inputs/day08.txt'))

print(part1())
print(part2())
