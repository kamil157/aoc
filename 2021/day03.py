from collections import Counter

input = open('2021/inputs/day03.txt').read().splitlines()

def part1(s):
    gamma = epsilon = ''
    for i in range(len(s[0])):
        c = Counter()
        for n in s:
            c[n[i]] += 1
        gamma += c.most_common()[0][0]
        epsilon += c.most_common()[-1][0]
    
    return int(gamma, 2) * int(epsilon, 2)

def helper(s, criteria):
    generator = set(s)
    
    i = 0
    while len(generator) > 1:
        gamma = criteria(Counter(n[i] for n in generator))

        next = set()
        for n in generator:
            if n[i] == gamma:
                next.add(n)

        generator = next
        i += 1
    return int(list(generator)[0], 2)

def part2(s):
    return helper(s, lambda c: '1' if c['1'] >= c['0'] else '0') *  helper(s, lambda c: '1' if c['1'] < c['0'] else '0')

print(part1(input))  # 4103154
print(part2(input))  # 4245351
