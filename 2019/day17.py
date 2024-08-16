from intcode import Intcode

with open('2019/inputs/day17.txt') as f:
    input = f.read()


def alignment(s):
    intcode = Intcode(s)
    map = []
    while True:
        try:
            line = []
            while True:
                output = intcode.run()
                if output == 10:
                    break
                line.append(chr(output))
        except StopIteration:
            break
        if line:
            map.append(line)

    result = 0
    for y, line in enumerate(map):
        for x, pixel in enumerate(line):
            if pixel != '#':
                continue
            neighbors = 0
            if x - 1 > 0 and line[x - 1] == '#':
                neighbors += 1
            if x + 1 < len(line) and line[x + 1] == '#':
                neighbors += 1
            if y - 1 > 0 and map[y - 1][x] == '#':
                neighbors += 1
            if y + 1 < len(map) and map[y + 1][x] == '#':
                neighbors += 1
            if neighbors >= 3:
                map[y][x] = 'O'
                result += y * x

    # for line in map:
    #     print(''.join(line))

    return result


def send_command(intcode, command):
    assert len(command) <= 20
    for c in command:
        intcode.input(ord(c))
    intcode.input(ord('\n'))


def walk(s):
    # m = map(s)
    intcode = Intcode(s)
    intcode.memory[0] = 2

    send_command(intcode, "A,B,A,C,B,C,B,C,A,C")  # main
    send_command(intcode, "L,10,R,12,R,12")  # A
    send_command(intcode, "R,6,R,10,L,10")  # B
    send_command(intcode, "R,10,L,10,L,12,R,6")  # C
    send_command(intcode, "n")  # video

    map = []
    while True:
        try:
            line = []
            while True:
                output = intcode.run()
                if output > 255:
                    return output
                if output == ord('\n'):
                    break
                line.append(chr(output))
        except StopIteration:
            break
        if line:
            map.append(line)

    for line in map:
        print(''.join(line))


print(alignment(input))  # 3888
print(walk(input))  # 927809
