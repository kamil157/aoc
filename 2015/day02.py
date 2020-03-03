input = open('2015/inputs/day02.txt').readlines()

def process(s, f):
    total = 0
    for line in s:
        l, w, h, = [int(n) for n in line.split('x')]
        total += f(l, w, h)
    return total

def part1(s):
    def paper(l, w, h):
        sides = [l * w, w * h, h * l]
        return 2 * sum(sides) + min(sides)
    return process(s, paper)

def part2(s):
    def ribbon(l, w, h):
        half_perimeters = [l + w, w + h, h + l]
        return 2 * min(half_perimeters) + l * w * h
    return process(s, ribbon)

print(part1(input))
print(part2(input))
