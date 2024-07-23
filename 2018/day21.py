with open('2018/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def run(r, instr):
    opcode = instr[0]
    a, b, c = [int(n) for n in instr[1:]]
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


def part2():
    program = lines[1:]
    ip = int(lines[0].split()[1])

    r = [0, 0, 0, 0, 0, 0, 0]
    pc = 0
    seen = set()
    result = 0

    while 0 <= pc < len(program):
        r[ip] = pc

        if pc == 28:
            if not result:
                print(r[1])
            if r[1] in seen:
                return result
            result = r[1]
            seen.add(r[1])
        instr = program[pc].split()
        run(r, instr)

        pc = r[ip] + 1


print(part2())
