from collections import defaultdict

input_raw = """3,8,1005,8,299,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,0,10,4,10,1002,8,1,29,1,1007,14,10,2,1106,8,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,58,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,80,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,103,1,5,6,10,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,101,0,8,128,1,106,18,10,1,7,20,10,1006,0,72,1006,0,31,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,1002,8,1,164,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,186,1,1007,8,10,1006,0,98,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,216,2,102,8,10,1,1008,18,10,1,1108,8,10,1006,0,68,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1001,8,0,253,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,274,1,1105,7,10,101,1,9,9,1007,9,1060,10,1005,10,15,99,109,621,104,0,104,1,21102,936995738520,1,1,21102,316,1,0,1106,0,420,21101,0,936995824276,1,21102,1,327,0,1106,0,420,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,248129784923,1,1,21102,1,374,0,1105,1,420,21102,29015149735,1,1,21101,385,0,0,1106,0,420,3,10,104,0,104,0,3,10,104,0,104,0,21101,983925826304,0,1,21101,0,408,0,1105,1,420,21102,825012036364,1,1,21101,0,419,0,1105,1,420,99,109,2,22101,0,-1,1,21101,0,40,2,21101,0,451,3,21102,441,1,0,1105,1,484,109,-2,2105,1,0,0,1,0,0,1,109,2,3,10,204,-1,1001,446,447,462,4,0,1001,446,1,446,108,4,446,10,1006,10,478,1101,0,0,446,109,-2,2105,1,0,0,109,4,2102,1,-1,483,1207,-3,0,10,1006,10,501,21102,0,1,-3,21201,-3,0,1,22102,1,-2,2,21102,1,1,3,21101,520,0,0,1106,0,525,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,548,2207,-4,-2,10,1006,10,548,21201,-4,0,-4,1105,1,616,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,567,0,1105,1,525,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,586,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,608,21201,-1,0,1,21102,1,608,0,106,0,483,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"""


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


def intcode(l, program_counters, user_input):
    pc = program_counters[0]
    base = 0

    while True:
        next_opcode = l[pc]
        # print(next_opcode)
        modes, opcode = split_opcode(next_opcode)

        # print(opcode)

        if opcode == 1:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            assert modes[0] != 1
            address = get_address(l, pc + 3, modes[0], base)
            pc += 4
            l[address] = a + b
        elif opcode == 2:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            assert modes[0] != 1
            address = get_address(l, pc + 3, modes[0], base)
            pc += 4
            l[address] = a * b
        elif opcode == 3:
            address = get_address(l, pc + 1, modes[2], base)
            pc += 2
            l[address] = user_input
        elif opcode == 4:
            output = get(l, pc + 1, modes[2], base)
            pc += 2
            print(output)
            program_counters[0] = pc
            return output
        elif opcode == 5:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            if a != 0:
                pc = b
            else:
                pc += 3
        elif opcode == 6:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            if a == 0:
                pc = b
            else:
                pc += 3
        elif opcode == 7:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            address = get_address(l, pc + 3, modes[0], base)
            assert modes[0] != 1
            if a < b:
                l[address] = 1
            else:
                l[address] = 0
            pc += 4
        elif opcode == 8:
            a = get(l, pc + 1, modes[2], base)
            b = get(l, pc + 2, modes[1], base)
            address = get_address(l, pc + 3, modes[0], base)
            assert modes[0] != 1
            if a == b:
                l[address] = 1
            else:
                l[address] = 0
            pc += 4
        elif opcode == 9:
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


def run(s):
    memory = [int(n) for n in s.split(',')]
    for _ in range(100000):
        memory.append(0)
    program_counters = [0]

    black, white = 0, 1
    x, y = 0, 0
    dir = 0
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    panels = defaultdict(int)
    panels[x, y] = black

    # loop
    while True:
        inp = panels[x, y]
        result = intcode(memory, program_counters, inp)
        if result == 'halt':
            break
        color = 'black' if result == black else 'white'
        panels[x, y] = result
        # print(result, color)

        result = intcode(memory, program_counters, inp)
        if result == 'halt':
            break
        turn = 'left' if result == 0 else 'right'
        # print(result, turn)

        # print('status', x, y, dir)
        dir += -1 if result == 0 else 1
        x += directions[dir % 4][0]
        y += directions[dir % 4][1]
        # print(x, y, panels)

    # print(panels)
    print(len(panels))


# run('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99', 0)
# run('1102,34915192,34915192,7,4,7,99,0', 0)
# run('104,1125899906842624,99', 0)
# run(input_raw, 1)
run(input_raw)