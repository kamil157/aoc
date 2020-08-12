from collections import Counter

input = open('2016/inputs/day06.txt').read()

def part1(s, frequency):
    transposed = zip(*s.split())
    return ''.join(Counter(pos).most_common()[frequency][0] for pos in transposed)

print(part1(input, 0))
print(part1(input, -1))

