with open('2017/inputs/day12.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part2():
    g = {}
    for line in lines:
        left, right = line.split(" <-> ")
        g[int(left)] = [int(n) for n in right.split(", ")]

    visited = set()

    def dfs(node):
        if node in visited:
            return 0
        visited.add(node)
        return 1 + sum(dfs(n) for n in g[node])

    groups = [dfs(n) for n in g if n not in visited]
    return groups[0], len(groups)


print(part2())
