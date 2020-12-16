from collections import defaultdict

input = open('2020/inputs/day15.txt').read()

def part1(s, nth):
    previous = defaultdict(list)
    numbers = [int(n) for n in s.split(',')]

    for turn, n in enumerate(numbers):
        previous[n].append(turn + 1)

    for turn in range(len(numbers), nth):
        if len(previous[n]) > 1:
            n = turn - previous[n][-2]
        else:
            n = 0        

        previous[n].append(turn + 1)
        
    return n

print(part1(input, 2020))
print(part1(input, 30000000))
