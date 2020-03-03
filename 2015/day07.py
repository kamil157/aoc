from re import findall

input = open('2015/inputs/day07.txt').read()


def part1(s):
    gates = findall(r'(\w+) (AND|LSHIFT|OR|RSHIFT) (\w+) -> (\w+)', s)
    nots = findall(r'NOT (\w+) -> (\w+)', s)
    direct = findall(r'\n(\w+) -> (\w+)', s)

    for _ in range(10):
        for a, result in direct:
            print(f'{a} -> {result}')

        for a, result in nots:
            print(f'NOT {a} -> {result}')

        for a, opcode, b, result in gates:
            print(f'{a} {opcode} {b} -> {result}')

print(part1(input))