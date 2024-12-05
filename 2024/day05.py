from collections import defaultdict

with open('2024/inputs/day05.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def correct(g, pages):
    for i, page in enumerate(pages):
        if not all(p in g[page] for p in pages[i + 1:]):
            return False
    return True


def solve():
    part1 = part2 = 0
    g = defaultdict(list)
    for line in lines:
        if "|" in line:
            left, right = map(int, line.split("|"))
            g[left].append(right)
        elif "," in line:
            pages = list(map(int, line.split(",")))
            if correct(g, pages):
                part1 += pages[len(pages) // 2]
            else:
                def key(page):
                    return len(set(g[page]).intersection(pages))
                reordered = sorted(pages, key=key, reverse=True)
                part2 += reordered[len(pages) // 2]

    return part1, part2


print(solve())
