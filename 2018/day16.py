with open('2018/inputs/day16.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n\n')


def run(registers, instr, opcode):
    r = registers[:]
    _, a, b, c = instr
    match opcode:
        case "addr":
            r[c] = r[a] + r[b]
        case "addi":
            r[c] = r[a] + b
        case "mulr":
            r[c] = r[a] * r[b]
        case "muli":
            r[c] = r[a] * b
        case "banr":
            r[c] = r[a] & r[b]
        case "bani":
            r[c] = r[a] & b
        case "borr":
            r[c] = r[a] | r[b]
        case "bori":
            r[c] = r[a] | b
        case "setr":
            r[c] = r[a]
        case "seti":
            r[c] = a
        case "gtir":
            r[c] = 1 if a > r[b] else 0
        case "gtri":
            r[c] = 1 if r[a] > b else 0
        case "gtrr":
            r[c] = 1 if r[a] > r[b] else 0
        case "eqir":
            r[c] = 1 if a == r[b] else 0
        case "eqri":
            r[c] = 1 if r[a] == b else 0
        case "eqrr":
            r[c] = 1 if r[a] == r[b] else 0
    return r


def part2():
    names = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori",
             "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
    part1 = 0
    opcodes = {n: set(names) for n in range(len(names))}
    for line in lines[:-2]:
        # parse
        before, instr, after = line.splitlines()
        before = eval(before[8:])
        instr = [int(n) for n in instr.split()]
        after = eval(after[8:])

        # try each opcode
        possible = []
        for op in names:
            if run(before, instr, op) == after:
                possible.append(op)
        if len(possible) >= 3:
            part1 += 1
        opcode = instr[0]
        opcodes[opcode] &= set(possible)

    # deduce opcodes
    definite = {}
    while len(definite) < len(names):
        for op, possible in opcodes.items():
            possible -= set(definite.values())
            if len(possible) == 1:
                definite[op] = list(possible)[0]

    # run program
    program = lines[-1].splitlines()
    r = [0, 0, 0, 0]
    for instr in program:
        instr = [int(n) for n in instr.split()]
        r = run(r, instr, definite[instr[0]])
    return part1, r[0]


print(part2())
