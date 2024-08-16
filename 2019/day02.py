with open('2019/inputs/day02.txt') as f:
    input_raw = f.read()
input_ints = [int(n) for n in input_raw.split(',')]


def intcode(l):
    i = 0
    opcode = l[i]
    while opcode != 99:
        a = l[l[i + 1]]
        b = l[l[i + 2]]
        address = l[i + 3]
        i += 4
        if opcode == 1:
            l[address] = a + b
        elif opcode == 2:
            l[address] = a * b
        elif opcode == 99:
            break
        else:
            print(i, a, b, opcode)
            assert False
        opcode = l[i]

    return l


assert intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
assert intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
assert intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
assert intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

input_ints[1] = 12
input_ints[2] = 2
print(intcode(input_ints)[0])


#########################

def find_input(n):
    for i in range(100):
        for j in range(100):
            input_ints = [int(n) for n in input_raw.split(',')]
            input_ints[1] = i
            input_ints[2] = j
            result = intcode(input_ints)[0]
            if result == n:
                return 100 * i + j


print(find_input(19690720))
