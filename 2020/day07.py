import re
from collections import defaultdict, deque

input = open('2020/inputs/day07.txt').readlines()

def graph(s): 
    graph = {}
    g_reversed = defaultdict(list)
    for line in s:
        left, right = line.split('bags contain')
        left_bag = re.search(r'(\w+ \w+)', left).group(1)
        right_bags = re.findall(r'(\w+ \w+) bag', right)
        right_bags_count = re.findall(r'(\d+) (\w+ \w+) bag', right)
        
        graph[left_bag] = right_bags_count
        for bag in right_bags:
            g_reversed[bag].append(left_bag)
    
    return g_reversed, graph

def part1(s):
    g_reversed = graph(s)[0]   

    visited = set()
    q = deque(['shiny gold'])
    while q:
        node = q.popleft()
        visited.add(node)
        for neighbor in g_reversed[node]:
            q.append(neighbor)

    return len(visited) - 1

def part2(s):
    g = graph(s)[1]    

    count = 0
    q = deque([('1', 'shiny gold')])
    while q:
        node = q.popleft()
        count += int(node[0])
        for neighbor in g[node[1]]:
            q.append((int(node[0]) * int(neighbor[0]), neighbor[1]))

    return count - 1

print(part1(input))
print(part2(input))
