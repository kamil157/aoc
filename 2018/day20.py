from collections import defaultdict
from math import inf


with open('2018/inputs/day20.txt', encoding="utf-8") as f:
    regex = f.read().strip()[1:-1]


def part2():
    pos = 0
    dirs = {"N": -1j, "E": 1, "W": -1, "S": 1j}

    distances = {}
    dist = 0
    stack = []
    for c in regex:
        if c == "(":
            stack.append((pos, dist))
        elif c == ")":
            pos, dist = stack.pop()
        elif c == "|":
            pos, dist = stack[-1]
        else:
            pos += dirs[c]
            dist += 1
            distances[pos] = min(distances.get(pos, inf), dist)

    return max(distances.values()), len([n for n in distances.values() if n >= 1000])


# def part2():
#     pos = 0
#     dirs = {"N": -1j, "E": 1, "W": -1, "S": 1j}

#     g = defaultdict(list)
#     pos = 0
#     dirs = {"N": -1j, "E": 1, "W": -1, "S": 1j}

#     stack = []
#     for c in regex:
#         if c in "NEWS":
#             g[pos].append(pos + dirs[c])
#             g[pos + dirs[c]].append(pos)
#             pos += dirs[c]
#         elif c == "(":
#             stack.append(pos)
#         elif c == ")":
#             pos = stack.pop()
#         elif c == "|":
#             pos = stack[-1]

#     q = [(0, set())]
#     longest = 0
#     distances = {}
#     while q:
#         pos, path = q.pop(0)
#         longest = max(longest, len(path))
#         distances[pos] = min(distances.get(pos, inf), len(path))

#         for u in g[pos]:
#             if u not in path:
#                 q.append((u, path | set([pos])))

#     return longest, len([n for n in distances.values() if n >= 1000])


print(part2())
