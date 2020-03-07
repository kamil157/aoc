import re

input = "hxbxwxba"

def string_to_ints(s):
    return [ord(c) for c in s]

def increment(s):
    def increment_char(l, i):
        l[i] += 1
        if l[i] > ord('z'):
            l[i] = ord('a')
            return False
        return True

    l = string_to_ints(s)
    for i in range(-1, -len(s), -1):
        if increment_char(l, i):
            return ''.join([chr(c) for c in l])

    raise Exception

def straight(s):
    l = string_to_ints(s)
    return any(l[i] + 1 == l[i + 1] and l[i] + 2 == l[i + 2] for i in range(len(l) - 2))

def part1(s):
    valid = False
    while not valid:
        s = increment(s)
        confusing = re.search('[iol]', s)
        pairs = re.search(r'([a-z])\1.*([a-z])\2', s)
        valid = straight(s) and not confusing and pairs

    return s

print(part1(input))
print(part1(part1(input)))