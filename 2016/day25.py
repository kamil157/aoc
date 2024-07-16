from itertools import count


with open('2016/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1():
    for a in count():
        registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}
        instructions = [line.split() for line in lines]
        pc = 0
        out = []
        expected = 0

        def value(n):
            if n in registers:
                return registers[n]
            return int(n)

        while len(out) < 40:
            l = instructions[pc]

            if l[0] == "cpy":
                registers[l[2]] = value(l[1])
            elif l[0] == "inc":
                registers[l[1]] += 1
            elif l[0] == "dec":
                registers[l[1]] -= 1
            elif l[0] == "jnz":
                if value(l[1]) != 0:
                    pc += value(l[2])
                    continue
            elif l[0] == "out":
                if value(l[1]) != expected:
                    break
                out.append(value(l[1]))
                expected = 1 if expected == 0 else 0

            pc += 1

        if len(out) == 40:
            return a

    return out


print(part1())
