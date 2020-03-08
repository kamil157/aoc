from itertools import combinations

input = open('2015/inputs/day17.txt').read()

def part1(s):
    containers = [int(n) for n in input.split()]

    chosen = (c for length in range(len(containers)) 
                for c in combinations(containers, length))
    return sum(1 for p in chosen if sum(p) == 150)

def part2(s):
    containers = [int(n) for n in input.split()]
    
    for i in range(len(containers)):
        if (count := sum(1 for c in combinations(containers, i) if sum(c) == 150)) > 0:
            return count

print(part1(input))
print(part2(input))