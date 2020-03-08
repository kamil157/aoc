from collections import defaultdict
from re import findall
from itertools import permutations

input = open('2015/inputs/day13.txt').read()

def make_graph(s):
    edges = findall(r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).', s)

    graph = defaultdict(dict)
    for u, sign, n, v in edges:
        graph[u][v] = - int(n) if sign == 'lose' else int(n)

    return graph

def happiness(graph, p):
    happiness = 0
    for i in range(len(p)):
        happiness += graph[p[i]][p[(i + 1) % len(p)]]
        happiness += graph[p[(i + 1) % len(p)]][p[i]]

    return happiness

def find_best_seating(graph):
    return max(happiness(graph, seating) for seating in permutations(graph.keys()))

def part1(s):
    return find_best_seating(make_graph(s))

def part2(s):
    graph = make_graph(s)

    for name in set(graph.keys()):
        graph[name]['Kamil'] = 0
        graph['Kamil'][name] = 0

    return find_best_seating(graph)

print(part1(input))
print(part2(input))