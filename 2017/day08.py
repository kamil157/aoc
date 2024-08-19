from collections import defaultdict
from operator import add, eq, ge, gt, le, lt, ne, sub


with open('2017/inputs/day08.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    r = defaultdict(int)
    part2 = 0
    for line in lines:
        left, right = line.split(" if ")

        lvar, lop, lval = left.split()
        lval = int(lval)
        lmap = {"inc": add, "dec": sub}

        rvar, rop, rval = right.split()
        rval = int(rval)
        rmap = {">": gt, "<": lt, ">=": ge, "<=": le, "==": eq, "!=": ne}

        if rmap[rop](r[rvar], rval):
            r[lvar] = lmap[lop](r[lvar], lval)
            part2 = max(part2, r[lvar])

    return max(r.values()), part2


print(part1())
