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


def intcode(memory, program_counters, user_inputs, prev, amp_id):
    i = program_counters[amp_id]
    input_i = 0

    while True:
        next_opcode = memory[i]
        # print('op', next_opcode)
        modes, opcode = split_opcode(next_opcode)

        # print('op', opcode)

        if opcode == 1:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            assert modes[0] == 0
            address = memory[i + 3]
            i += 4
            memory[address] = a + b
        elif opcode == 2:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            assert modes[0] == 0
            address = memory[i + 3]
            i += 4
            memory[address] = a * b
            assert a * b < 100000000000
        elif opcode == 3:
            address = memory[i + 1]
            i += 2
            # print('input =', user_inputs[input_i])
            memory[address] = user_inputs[input_i]
            input_i += 1
        elif opcode == 4:
            address = memory[i + 1]
            i += 2
            output = memory[address]
            # print(output)
            program_counters[amp_id] = i
            return output, opcode
        elif opcode == 5:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            if a != 0:
                i = b
            else:
                i += 3
        elif opcode == 6:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            if a == 0:
                i = b
            else:
                i += 3
        elif opcode == 7:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            address = memory[i + 3]
            assert modes[0] == 0
            if a < b:
                memory[address] = 1
            else:
                memory[address] = 0
            i += 4
        elif opcode == 8:
            a = get(memory, i + 1, modes[2])
            b = get(memory, i + 2, modes[1])
            address = memory[i + 3]
            assert modes[0] == 0
            if a == b:
                memory[address] = 1
            else:
                memory[address] = 0
            i += 4

        elif opcode == 99:
            # print('halt')
            break
        else:
            print(opcode)
            assert False

    return prev, opcode


def thrusters(s):
    perm = itertools.permutations(range(5, 10))
    best = 0

    for p in perm:
        memory = [[int(n) for n in s.split(',')] for _ in range(5)]
        program_counters = [0] * 5

        signal = 0
        i = 0

        while True:
            # print(signal)
            phase = p[i % 5]
            signal, opcode = intcode(memory[i % 5], program_counters, [phase, signal] if i < 5 else [signal], signal, i % 5)
            # print(i, memory[i % 5])
            if opcode == 99:
                # print(signal)
                best = max(best, signal)
                break
            i += 1

        # print(a, b, best)
    # print(best)
    return best


assert thrusters('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5') == 139629729
assert thrusters(
    '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10') == 18216

print(thrusters(input))
