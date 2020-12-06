from collections import Counter

input = open('2020/inputs/day06.txt').read()

def part1(s):
    groups = [g.replace('\n', '') for g in s.split('\n\n')]
    return sum(len(set(group)) for group in groups)
        
def part2(s):
    total = 0
    groups = [g.split('\n') for g in s.split('\n\n')]
    for group in groups:
        c = Counter()

        for line in group:
            c += Counter(line)

        for q in c.values():
            if q == len(group):
                total += 1
                
    return total
        
print(part1(input))
print(part2(input))
