from collections import Counter
import re
import string

input = open('2016/inputs/day04.txt').read()

def rotate(s, n):
    shift = n % len(string.ascii_lowercase)
    inp = string.ascii_lowercase
    out = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    table = str.maketrans(inp, out)
    return s.translate(table)

def part1(s):
    lines = re.findall(r'([-a-z]+)-(\d+)\[(\w+)\]', input)
    total = 0
    for encrypted, sector, expected in lines:
        name = encrypted.replace('-', '')
        counts = sorted(Counter(name).items(), key=lambda v: (-v[1], v[0]))
        checksum = ''.join(c for c, _ in counts[:5])

        if checksum == expected:
            total += int(sector)
            decrypted = rotate(encrypted, int(sector))

            if 'north' in decrypted:
                north_pole = int(sector)

    return total, north_pole

print(part1(input))
