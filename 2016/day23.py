with open('2016/inputs/day23.txt', encoding="utf-8") as f:
    lines = f.read().strip().split("\n")


def part1(eggs):
    registers = {'a': eggs, 'b': 0, 'c': 0, 'd': 0}
    instructions = [line.split() for line in lines]
    pc = 0

    def value(n):
        if n in registers:
            return registers[n]
        return int(n)

    while pc < len(instructions):
        l = instructions[pc]

        if l[0] == "cpy":
            registers[l[2]] = value(l[1])
        elif l[0] == "inc":
            registers[l[1]] += 1
        elif l[0] == "dec":
            registers[l[1]] -= 1
        elif l[0] == "jnz":
            if value(l[2]) < 0:
                loop = instructions[pc + value(l[2]):pc + 1]
                if loop == [['cpy', 'b', 'c'], ['inc', 'a'], ['dec', 'c'], ['jnz', 'c', '-2'], ['dec', 'd'], ['jnz', 'd', '-5']]:
                    registers["a"] += registers["b"] * registers["d"]
                    pc += 1
                    continue
            if value(l[1]) != 0:
                pc += value(l[2])
                continue
        elif l[0] == "tgl":
            index = pc + value(l[1])
            if 0 <= index < len(instructions):
                instr = instructions[index]
                if len(instr) == 2:
                    toggled = "dec" if instr[0] == "inc" else "inc"
                elif len(instr) == 3:
                    toggled = "cpy" if instr[0] == "jnz" else "cpy"
                instructions[index][0] = toggled

        pc += 1

    return registers['a']


print(part1(7))
print(part1(12))
