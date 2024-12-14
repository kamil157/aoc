from re import search
import z3

with open('2024/inputs/day13.txt', encoding="utf-8") as f:
    lines = f.read().split('\n\n')


def solve(offset):
    total = 0
    for line in lines:
        m = search(r"Button A:\s*X\+(\d+), Y\+(\d+)", line)
        ax = int(m.group(1))
        ay = int(m.group(2))

        m = search(r"Button B:\s*X\+(\d+), Y\+(\d+)", line)
        bx = int(m.group(1))
        by = int(m.group(2))

        m = search(r"Prize:\s*X=(\d+), Y=(\d+)", line)
        px = int(m.group(1)) + offset
        py = int(m.group(2)) + offset

        o = z3.Optimize()
        a = z3.Int("a")
        b = z3.Int("b")
        o.add(a * ax + b * bx == px)
        o.add(a * ay + b * by == py)
        if o.check() == z3.sat:
            total += o.model().eval(3 * a + b).as_long()

    return total


print(solve(0))
print(solve(10000000000000))
