from functools import cache


with open('2024/inputs/day19.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


@cache
def dfs(pattern):
    return sum(dfs(pattern[len(towel):]) for towel in lines[0].split(", ") if pattern.startswith(towel)) if pattern else 1


def solve():
    return sum(dfs(pattern) != 0 for pattern in lines[1].splitlines()), sum(dfs(pattern) for pattern in lines[1].splitlines())


print(solve())
