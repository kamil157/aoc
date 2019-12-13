from queue import Queue


def split_opcode(full_opcode):
    digits = [int(n) for n in str(full_opcode).zfill(5)]
    modes = digits[:3]
    opcode = 10 * digits[3] + digits[4]
    return modes, opcode


def get(l, n, mode, base):
    if mode == 0:
        return l[l[n]]
    elif mode == 1:
        return l[n]
    elif mode == 2:
        return l[base + l[n]]
    else:
        assert False


def get_address(l, n, mode, base):
    if mode == 0:
        return l[n]
    elif mode == 1:
        return n
    elif mode == 2:
        return base + l[n]
    else:
        assert False


class Intcode:
    def __init__(self, s):
        self.memory = [int(n) for n in s.split(',')]
        for _ in range(1000):
            self.memory.append(0)
        self.program_counters = [0, 0]
        self.inputs = Queue()

    def input(self, user_input):
        self.inputs.put(user_input)

    def run(self):
        pc = self.program_counters[0]
        base = self.program_counters[1]
        l = self.memory

        while True:
            next_opcode = l[pc]
            # print('opcode', next_opcode)
            modes, opcode = split_opcode(next_opcode)

            # print(opcode)

            if opcode == 1:  # ADD
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                assert modes[0] != 1
                address = get_address(l, pc + 3, modes[0], base)
                pc += 4
                l[address] = a + b
            elif opcode == 2:  # MUL
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                assert modes[0] != 1
                address = get_address(l, pc + 3, modes[0], base)
                pc += 4
                l[address] = a * b
            elif opcode == 3:  # INPUT
                address = get_address(l, pc + 1, modes[2], base)
                pc += 2
                l[address] = self.inputs.get()
                # print(self.inputs.qsize())
            elif opcode == 4:  # OUTPUT
                output = get(l, pc + 1, modes[2], base)
                pc += 2
                # print(output)
                self.program_counters[0] = pc
                self.program_counters[1] = base
                return output
            elif opcode == 5:  # JUMP IF NOT 0
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                if a != 0:
                    pc = b
                else:
                    pc += 3
            elif opcode == 6:  # JUMP IF 0
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                if a == 0:
                    pc = b
                else:
                    pc += 3
            elif opcode == 7:  # LESS THAN
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                address = get_address(l, pc + 3, modes[0], base)
                assert modes[0] != 1
                if a < b:
                    l[address] = 1
                else:
                    l[address] = 0
                pc += 4
            elif opcode == 8:  # EQUAL
                a = get(l, pc + 1, modes[2], base)
                b = get(l, pc + 2, modes[1], base)
                address = get_address(l, pc + 3, modes[0], base)
                assert modes[0] != 1
                if a == b:
                    l[address] = 1
                else:
                    l[address] = 0
                pc += 4
            elif opcode == 9:  # BASE
                a = get(l, pc + 1, modes[2], base)
                base += a
                pc += 2
            elif opcode == 99:
                print('halt')
                break
            else:
                print(opcode)
                assert False

        return 'halt'
