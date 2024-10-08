from re import findall
from itertools import permutations
from collections import defaultdict

input = open('2015/inputs/day09.txt').read()

def part1(s, f):
    edges = findall(r'(\w+) to (\w+) = (\d+)', s)

    distances = defaultdict(dict)
    for u, v, d in edges:
        distances[u][v] = int(d)
        distances[v][u] = int(d)

    return f((sum(distances[route[i]][route[i + 1]] 
            for i in range(len(route) - 1))) 
            for route in permutations(distances.keys()))

print(part1(input, min))
print(part1(input, max))
