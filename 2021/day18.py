from functools import reduce
from itertools import permutations


with open('2021/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def magnitude(n):
    if isinstance(n, int):
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])


def addleft(n, v):
    if v is None:
        return n
    if isinstance(n, int):
        return n + v
    return [addleft(n[0], v), n[1]]


def addright(n, v):
    if v is None:
        return n
    if isinstance(n, int):
        return n + v
    return [n[0], addright(n[1], v)]


def explode(n, level=0):
    if isinstance(n, int):
        return False, None, n, None
    a, b = n
    if level == 4:
        return True, a, 0, b
    changed, left, a, right = explode(a, level + 1)
    if changed:
        return True, left, [a, addleft(b, right)], None
    changed, left, b, right = explode(b, level + 1)
    if changed:
        return True, None, [addright(a, left), b], right
    return False, None, n, None


def split(n):
    if isinstance(n, int):
        if n >= 10:
            return True, [n // 2, n - n // 2]
        return False, n
    else:
        changed, n[0] = split(n[0])
        if changed:
            return True, n
        changed, n[1] = split(n[1])
        if changed:
            return True, n
        return False, n


def add(a, b):
    n = [a, b]
    while True:
        changed, _, n, _ = explode(n)
        if changed:
            continue

        changed, n = split(n)
        if changed:
            continue
        return n


def part1():
    return magnitude(reduce(add, (eval(n) for n in lines)))


def part2():
    return max(magnitude(add(eval(a), eval(b))) for a, b in permutations(lines, 2))


print(part1())
print(part2())
