input = open('2020/inputs/day08.txt').readlines()

def part1(s):
    visited = set()
    pc = 0
    acc = 0
    while pc not in visited and pc < len(s):
        instruction = s[pc]
        visited.add(pc)

        op, val = instruction.strip().split()

        if op == 'nop':
            pc += 1
        elif op == 'acc':
            acc += int(val)
            pc += 1
        elif op == 'jmp':
            pc += int(val)
        else:
            assert False

    return acc, pc

def part2(s):
    for i in range(len(s)):
        s1 = s.copy()
        s1[i] = s[i].replace('nop', 'jmp')
        s1[i] = s[i].replace('jmp', 'nop')
        acc, pc = part1(s1)
        if pc == len(s1):
            return acc

print(part1(input)[0])
print(part2(input))