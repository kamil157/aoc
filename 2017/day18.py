from collections import defaultdict


with open('2017/inputs/day18.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    def value(x):
        if x in r:
            return r[x]
        return int(x)

    sound = ""

    r = defaultdict(int)
    pc = 0
    while True:
        instr = lines[pc].split()
        next_pc = pc + 1

        match instr[0]:
            case "snd":
                sound = r[instr[1]]
            case "set":
                r[instr[1]] = value(instr[2])
            case "add":
                r[instr[1]] += value(instr[2])
            case "mul":
                r[instr[1]] *= value(instr[2])
            case "mod":
                r[instr[1]] %= value(instr[2])
            case "rcv":
                if r[instr[1]] != 0:
                    return sound
            case "jgz":
                if r[instr[1]] > 0:
                    next_pc = pc + value(instr[2])

        pc = next_pc


print(part1())


class Program:
    def __init__(self, pid):
        self.messages = []
        self.program = None
        self.pid = pid
        self.counter = 0

    def main(self):
        def value(x):
            if x in r:
                return r[x]
            return int(x)

        r = defaultdict(int)
        r["p"] = self.pid
        pc = 0
        while 0 <= pc < len(lines):
            instr = lines[pc].split()
            next_pc = pc + 1

            match instr[0]:
                case "snd":
                    self.counter += 1
                    self.program.messages.append(value(instr[1]))
                case "set":
                    r[instr[1]] = value(instr[2])
                case "add":
                    r[instr[1]] += value(instr[2])
                case "mul":
                    r[instr[1]] *= value(instr[2])
                case "mod":
                    r[instr[1]] %= value(instr[2])
                case "rcv":
                    if not self.messages:
                        yield
                    r[instr[1]] = self.messages.pop(0)
                case "jgz":
                    if value(instr[1]) > 0:
                        next_pc = pc + value(instr[2])

            pc = next_pc

    def connect(self, program):
        self.program = program


def part2():
    p0 = Program(0)
    p1 = Program(1)
    p0.connect(p1)
    p1.connect(p0)
    p0g = p0.main()
    p1g = p1.main()
    next(p0g)
    next(p1g)
    while p0.messages or p1.messages:
        if p0.messages:
            next(p0g)
        if p1.messages:
            next(p1g)
    return p1.counter


print(part2())
