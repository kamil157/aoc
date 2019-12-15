from collections import deque


def split_opcode(full_opcode):
    digits = [int(n) for n in str(full_opcode).zfill(5)]
    modes = digits[:3]
    opcode = 10 * digits[3] + digits[4]
    return modes, opcode


class Intcode:
    def __init__(self, s):
        self.memory = [int(n) for n in s.split(',')]
        self.memory.extend([0] * 1000)
        self.pc = 0
        self.base = 0
        self.inputs = deque()

    def get_address(self, mode):
        n = self.pc
        self.pc += 1
        if mode == 0:
            return self.memory[n]
        elif mode == 1:
            return n
        elif mode == 2:
            return self.base + self.memory[n]
        else:
            assert False

    def input(self, user_input):
        self.inputs.append(user_input)

    def replace_input(self, user_input):
        self.inputs.clear()
        self.inputs.append(user_input)

    def run(self):
        while True:
            next_opcode = self.memory[self.get_address(1)]
            # print(next_opcode)
            modes, opcode = split_opcode(next_opcode)

            # print(opcode)

            if opcode == 1:  # ADD
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                assert modes[0] != 1
                address = self.get_address(modes[0])
                self.memory[address] = a + b
            elif opcode == 2:  # MUL
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                assert modes[0] != 1
                address = self.get_address(modes[0])
                self.memory[address] = a * b
            elif opcode == 3:  # INPUT
                address = self.get_address(modes[2])
                self.memory[address] = self.inputs.popleft()
            elif opcode == 4:  # OUTPUT
                output = self.memory[self.get_address(modes[2])]
                # print(output)
                return output
            elif opcode == 5:  # JUMP IF NOT 0
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                if a != 0:
                    self.pc = b
            elif opcode == 6:  # JUMP IF 0
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                if a == 0:
                    self.pc = b
            elif opcode == 7:  # LESS THAN
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                address = self.get_address(modes[0])
                assert modes[0] != 1
                if a < b:
                    self.memory[address] = 1
                else:
                    self.memory[address] = 0
            elif opcode == 8:  # EQUAL
                a = self.memory[self.get_address(modes[2])]
                b = self.memory[self.get_address(modes[1])]
                address = self.get_address(modes[0])
                assert modes[0] != 1
                if a == b:
                    self.memory[address] = 1
                else:
                    self.memory[address] = 0
            elif opcode == 9:  # BASE
                a = self.memory[self.get_address(modes[2])]
                self.base += a
            elif opcode == 99:  # HALT
                raise StopIteration
            else:
                print(opcode)
                assert False