from functools import reduce
from operator import xor


def knot(l, skip, start, lengths):
    for length in lengths:
        l[:length] = l[:length][::-1]
        move = (length + skip) % len(l)
        start = (start - move) % len(l)
        l = l[move:] + l[:move]
        skip += 1
    return l, skip, start


def knot_hash(key):
    lengths = [ord(n) for n in key] + [17, 31, 73, 47, 23]
    l = list(range(256))
    start = 0
    skip = 0
    for _ in range(64):
        l, skip, start = knot(l, skip, start, lengths)

    sparse = l[start:] + l[:start]
    dense = [reduce(xor, sparse[16*i:16*(i+1)]) for i in range(16)]
    return "".join(f"{n:02x}" for n in dense)


def squares():
    result = []
    for i in range(128):
        h = knot_hash("amgozmfv" + "-" + str(i))
        b = f"{int(h, 16):0128b}"
        result.append([int(d) for d in b])
    return result


def part1():
    return sum(line.count(1) for line in squares())


print(part1())


def part2():
    g = {x+y*1j: n for y, line in enumerate(squares())
         for x, n in enumerate(line)}

    def dfs(node):
        if node in visited:
            return 1
        visited.add(node)

        for d in [1, -1, 1j, -1j]:
            if g.get(node + d, 0) == 1:
                dfs(node + d)

    visited = set()
    groups = 0
    for n, square in g.items():
        if n not in visited and square == 1:
            groups += 1
            dfs(n)
    return groups


print(part2())
