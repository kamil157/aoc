import itertools

input = "3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99"


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


def intcode(s, user_inputs):
    l = [int(n) for n in s.split(',')]

    i = 0
    input_i = 0

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
            l[address] = user_inputs[input_i]
            input_i += 1
        elif opcode == 4:
            address = l[i + 1]
            i += 2
            output = l[address]
            # print(output)
            return output
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


def thrusters(s):
    perm = itertools.permutations(range(5))
    best = 0

    for p in perm:
        phase = p[0]
        inout = 0

        for i in range(1, 5):
            # print(a, b)
            inout = intcode(s, [phase, inout])
            phase = p[i]

        inout = intcode(s, [phase, inout])

        # print(a, b, best)
        best = max(best, inout)
    # print(best)
    return best


assert thrusters('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0') == 43210
assert thrusters('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0') == 54321
assert thrusters(
    '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0') == 65210

print(thrusters(input))
