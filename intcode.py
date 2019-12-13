from collections import deque


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
        self.memory.extend([0] * 1000)
        self.pc = 0
        self.base = 0
        self.inputs = deque()

    def input(self, user_input):
        self.inputs.append(user_input)

    def run(self):
        while True:
            next_opcode = self.memory[self.pc]
            # print('opcode', next_opcode)
            modes, opcode = split_opcode(next_opcode)

            # print(opcode)

            if opcode == 1:  # ADD
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                assert modes[0] != 1
                address = get_address(self.memory, self.pc + 3, modes[0], self.base)
                self.pc += 4
                self.memory[address] = a + b
            elif opcode == 2:  # MUL
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                assert modes[0] != 1
                address = get_address(self.memory, self.pc + 3, modes[0], self.base)
                self.pc += 4
                self.memory[address] = a * b
            elif opcode == 3:  # INPUT
                address = get_address(self.memory, self.pc + 1, modes[2], self.base)
                self.pc += 2
                self.memory[address] = self.inputs.popleft()
                # print(self.inputs.qsize())
            elif opcode == 4:  # OUTPUT
                output = get(self.memory, self.pc + 1, modes[2], self.base)
                self.pc += 2
                # print(output)
                return output
            elif opcode == 5:  # JUMP IF NOT 0
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                if a != 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 6:  # JUMP IF 0
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                if a == 0:
                    self.pc = b
                else:
                    self.pc += 3
            elif opcode == 7:  # LESS THAN
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                address = get_address(self.memory, self.pc + 3, modes[0], self.base)
                assert modes[0] != 1
                if a < b:
                    self.memory[address] = 1
                else:
                    self.memory[address] = 0
                self.pc += 4
            elif opcode == 8:  # EQUAL
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                b = get(self.memory, self.pc + 2, modes[1], self.base)
                address = get_address(self.memory, self.pc + 3, modes[0], self.base)
                assert modes[0] != 1
                if a == b:
                    self.memory[address] = 1
                else:
                    self.memory[address] = 0
                self.pc += 4
            elif opcode == 9:  # BASE
                a = get(self.memory, self.pc + 1, modes[2], self.base)
                self.base += a
                self.pc += 2
            elif opcode == 99:
                print('halt')
                break
            else:
                print(opcode)
                assert False

        return 'halt'
