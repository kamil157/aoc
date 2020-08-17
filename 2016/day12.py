import re

input = open('2016/inputs/day12.txt').read()

def part1(s, c):
    registers = { 'a': 0, 'b': 0, 'c': c, 'd': 0 }
    instructions = s.split('\n')
    i = 0

    while i < len(instructions):
        line = instructions[i]

        if m := re.search(r'cpy (-?\d+|[a-d]) ([a-d])', line):
            x = m.group(1)
            y = m.group(2)
            registers[y] = registers[x] if x in registers else int(x)
        
        elif m := re.search(r'(inc|dec) ([a-d])', line):
            op = m.group(1)
            x = m.group(2)
            registers[x] += 1 if op == 'inc' else -1

        elif m := re.search(r'jnz (-?\d+|[a-d]) (-?\d+)', line):
            x = m.group(1)
            y = int(m.group(2))
            if registers[x] if x in registers else int(x) != 0:
                i += y
                continue
        
        i += 1           

    return registers['a']

print(part1(input, 0))
print(part1(input, 1))
