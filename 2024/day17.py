with open('2024/inputs/day17.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def combo(r, operand):
    if operand in [0, 1, 2, 3]:
        return operand
    if operand == 4:
        return r["a"]
    if operand == 5:
        return r["b"]
    if operand == 6:
        return r["c"]


def part1():
    r = {}
    r["a"] = int(lines[0].split(": ")[1])
    r["b"] = int(lines[1].split(": ")[1])
    r["c"] = int(lines[2].split(": ")[1])

    pc = 0
    out = []

    program = [int(n) for n in lines[4].split(": ")[1].split(",")]

    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]
        if opcode == 0:  # adv
            r["a"] //= (2**combo(r, operand))
        elif opcode == 1:  # bxl
            r["b"] ^= operand
        elif opcode == 2:  # bst
            r["b"] = combo(r, operand) % 8
        elif opcode == 3:  # jnz
            if r["a"] != 0:
                pc = operand - 2
        elif opcode == 4:  # bxc
            r["b"] = r["b"] ^ r["c"]
        elif opcode == 5:  # out
            out.append(combo(r, operand) % 8)
        elif opcode == 6:  # bdv
            r["b"] = r["a"] // (2**combo(r, operand))
        elif opcode == 7:  # bsr
            r["c"] = r["a"] // (2**combo(r, operand))
        pc += 2

    return ",".join(str(n) for n in out)


print(part1())
