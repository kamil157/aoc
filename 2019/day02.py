input_raw = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,10,23,2,10,23,27,1,27,6,31,1,13,31,35,1,13,35,39,1,39,10,43,2,43,13,47,1,47,9,51,2,51,13,55,1,5,55,59,2,59,9,63,1,13,63,67,2,13,67,71,1,71,5,75,2,75,13,79,1,79,6,83,1,83,5,87,2,87,6,91,1,5,91,95,1,95,13,99,2,99,6,103,1,5,103,107,1,107,9,111,2,6,111,115,1,5,115,119,1,119,2,123,1,6,123,0,99,2,14,0,0"
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
