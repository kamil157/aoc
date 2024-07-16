with open('2016/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1(c):
    registers = {'a': 0, 'b': 0, 'c': c, 'd': 0}
    instructions = [line.split() for line in lines]

    def value(n):
        if n in registers:
            return registers[n]
        return int(n)

    pc = 0
    while pc < len(instructions):
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
        pc += 1

    return registers['a']


print(part1(0))
print(part1(1))
