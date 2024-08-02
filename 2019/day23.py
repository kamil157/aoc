from intcode import Intcode
from collections import deque

with open('2019/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read()


def solve():
    intcodes = [Intcode(lines) for _ in range(50)]
    packets = [deque() for _ in range(50)]
    nat = None
    part1 = None
    part2 = set()

    for i in range(50):
        intcodes[i].input(i)

    while True:
        idle = True
        for i in range(50):
            intcode = intcodes[i]
            dest = intcode.run(1000)
            if dest is not None:
                idle = False
                x = intcode.run()
                y = intcode.run()
                if dest == 255:
                    if not part1:
                        part1 = y
                    nat = (x, y)
                else:
                    packets[dest].append((x, y))
                # print(i, dest, x, y)

            if packets[i]:
                x, y = packets[i].popleft()
                intcodes[i].input(x)
                intcodes[i].input(y)
                idle = False
            else:
                intcodes[i].input(-1)
                intcodes[i].input(-1)

        if idle:
            x, y = nat
            if y in part2:
                return part1, y
            intcodes[0].input(x)
            intcodes[0].input(y)
            part2.add(y)
            nat = None


print(solve())
