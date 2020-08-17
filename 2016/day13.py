from collections import deque

input = 1362

def part1(s):
    pos = (1, 1)
    goal = (31, 39)
    visited = set()
    visited.add(pos)
    dist = { pos: 0 }
    q = deque()
    q.append(pos)
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    reachable = 1

    while pos != goal:
        pos = q.popleft()
        if pos not in visited and dist[pos] <= 50:
            reachable += 1
        visited.add(pos)
        for d in directions:
            x, y = pos[0] + d[0], pos[1] + d[1]
            if x < 0 or y < 0 or (x, y) in visited:
                continue
            n = x*x + 3*x + 2*x*y + y + y*y + s
            isWall = bin(n).count("1") % 2 == 1
            if isWall:
                continue
            dist[(x, y)] = dist[pos] + 1
            q.append((x, y))

    return dist[pos], reachable

print(part1(input))
