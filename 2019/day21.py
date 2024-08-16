from intcode import Intcode

with open('2019/inputs/day21.txt', encoding="utf-8") as f:
    input = f.read()


def send_command(intcode, command):
    assert len(command) <= 20
    for c in command:
        intcode.input(ord(c))
    intcode.input(ord('\n'))


def spring(s, commands):
    intcode = Intcode(s)

    for command in commands:
        send_command(intcode, command)

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


print(spring(input,
             [
                 "NOT A J",
                 "NOT B T",
                 "OR T J",
                 "NOT C T",
                 "OR T J",
                 "AND D J",
                 "WALK"
             ]))

print(spring(input,
             [
                 "NOT A J",
                 "NOT B T",
                 "OR T J",
                 "NOT C T",
                 "OR T J",
                 "AND D J",

                 "NOT E T",
                 "NOT T T",
                 "OR H T",
                 "AND T J",
                 "RUN"
             ]))
