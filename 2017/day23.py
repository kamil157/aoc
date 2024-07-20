from collections import defaultdict
from math import sqrt


with open('2017/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    def value(x):
        try:
            return int(x)
        except ValueError:
            return r[x]

    r = defaultdict(int)
    pc = 0
    count = 0
    while 0 <= pc < len(lines):
        instr = lines[pc].split()
        next_pc = pc + 1

        match instr[0]:
            case "set":
                r[instr[1]] = value(instr[2])
            case "sub":
                r[instr[1]] -= value(instr[2])
            case "mul":
                r[instr[1]] *= value(instr[2])
                count += 1
            case "jnz":
                if value(instr[1]) != 0:
                    next_pc = pc + value(instr[2])

        pc = next_pc
    return count


print(part1())


def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def part2():
    def value(x):
        try:
            return int(x)
        except ValueError:
            return r[x]

    r = defaultdict(int)
    r["a"] = 1
    pc = 0
    while 0 <= pc < len(lines):
        instr = lines[pc].split()
        next_pc = pc + 1

        match instr[0]:
            case "set":
                r[instr[1]] = value(instr[2])
            case "sub":
                r[instr[1]] -= value(instr[2])
            case "mul":
                r[instr[1]] *= value(instr[2])
            case "jnz":
                if value(instr[2]) == -13:
                    if not is_prime(r["b"]):
                        r["f"] = 0
                elif value(instr[1]) != 0 and value(instr[2]) != -8:
                    next_pc = pc + value(instr[2])

        pc = next_pc
    return r["h"]


print(part2())
