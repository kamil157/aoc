from hashlib import md5
from collections import deque

input = 'rrrbmfta'

def hash(s, path):
    return md5((s + path).encode()).hexdigest()

def part1(s):
    w, h = 3, 3
    goal = 3, 3
    directions = { 'L': [-1, 0], 'R': [1, 0], 'D': [0, 1], 'U': [0, -1] }
    hash_char = { 'U': 0, 'D': 1, 'L': 2, 'R': 3 }
    q = deque()
    q.append((0, 0, ''))
    shortest = None
    longest = 0

    while q:
        x, y, path = q.popleft()
        if x == goal[0] and y == goal[1]:
            if not shortest:
                shortest = path
            longest = max(longest, len(path))
            continue

        for c, d in directions.items():
            on_map = 0 <= x + d[0] <= w and 0 <= y + d[1] <= h
            is_open = hash(s, path)[hash_char[c]] in ['b', 'c', 'd', 'e', 'f']
            if on_map and is_open:
                q.append((x + d[0], y + d[1], path + c))

    return shortest, longest

print(part1(input))
