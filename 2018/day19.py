with open('2018/inputs/day19.txt', encoding="utf-8") as f:
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


def sum_divisors(number):
    r0 = 0
    for n in range(1, number + 1):
        if number % n == 0:
            r0 += n
    return r0


def part1(r0):
    program = lines[1:]
    ip = int(lines[0].split()[1])
    r = [r0, 0, 0, 0, 0, 0]
    pc = 0

    while 0 <= pc < len(program):
        r[ip] = pc

        instr = program[pc].split()
        if program[pc] == "addr 3 0 3" and r0 == 0:
            return sum_divisors(r[2])
        if program[pc] == "seti 0 0 0":
            return sum_divisors(r[2])
        run(r, instr)

        pc = r[ip] + 1

    return r[0]


print(part1(0))
print(part1(1))
