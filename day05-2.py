input_raw = "3,225,1,225,6,6,1100,1,238,225,104,0,1,191,196,224,1001,224,-85,224,4,224,1002,223,8,223,1001,224,4,224,1,223,224,223,1101,45,50,225,1102,61,82,225,101,44,39,224,101,-105,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,102,14,187,224,101,-784,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,1001,184,31,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,91,18,225,2,35,110,224,101,-810,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,76,71,224,1001,224,-147,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,7,16,225,1102,71,76,224,101,-5396,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1101,72,87,225,1101,56,77,225,1102,70,31,225,1102,29,15,225,1002,158,14,224,1001,224,-224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1007,226,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,8,226,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,107,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,404,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,1007,677,677,224,102,2,223,223,1006,224,464,1001,223,1,223,107,226,226,224,1002,223,2,223,1005,224,479,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,524,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,554,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,569,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,599,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,614,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,629,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226"
input_ints = [int(n) for n in input_raw.split(',')]


def split_opcode(full_opcode):
    digits = [int(n) for n in str(full_opcode).zfill(5)]
    modes = digits[:3]
    opcode = 10 * digits[3] + digits[4]
    return modes, opcode


def get(l, n, mode):
    if mode == 0:
        return l[l[n]]
    else:
        return l[n]


def intcode(l, user_input):
    i = 0

    while True:
        next_opcode = l[i]
        # print(next_opcode)
        modes, opcode = split_opcode(next_opcode)

        # print(opcode)

        if opcode == 1:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            assert modes[0] == 0
            address = l[i + 3]
            i += 4
            l[address] = a + b
        elif opcode == 2:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            assert modes[0] == 0
            address = l[i + 3]
            i += 4
            l[address] = a * b
        elif opcode == 3:
            address = l[i + 1]
            i += 2
            l[address] = user_input
        elif opcode == 4:
            address = l[i + 1]
            i += 2
            output = l[address]
            print(output)
        elif opcode == 5:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            if a != 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            address = l[i + 3]
            assert modes[0] == 0
            if a < b:
                l[address] = 1
            else:
                l[address] = 0
            i += 4
        elif opcode == 8:
            a = get(l, i + 1, modes[2])
            b = get(l, i + 2, modes[1])
            address = l[i + 3]
            assert modes[0] == 0
            if a == b:
                l[address] = 1
            else:
                l[address] = 0
            i += 4

        elif opcode == 99:
            break
        else:
            print(opcode)
            assert False

    return l


intcode(input_ints, 5)
