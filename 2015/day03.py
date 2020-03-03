input = open('2015/inputs/day03.txt').read()

def part1(s, count):
    directions = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}
    pos = [[0, 0] for _ in range(count)]
    houses = {(0, 0)}

    for i, c in enumerate(input):
        santa = i % count
        pos[santa][0] += directions[c][0]
        pos[santa][1] += directions[c][1]
        houses.add((pos[santa][0], pos[santa][1]))
    return len(houses)

print(part1(input, 1))
print(part1(input, 2))
