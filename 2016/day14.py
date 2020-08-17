import re
from hashlib import md5
from collections import deque

input = 'ngcjuoqr'
# input = 'abc'

def hash(s, i):
    return md5((s + str(i)).encode()).hexdigest()

def part1(s):
    i = 0
    keys = {}

    while len(keys) < 64:
        h = hash(s, i)
        
        if m := re.search(r'(.)\1\1', h):
            for n in range(1, 1001): # TODO cache
                nextHash = hash(s, i + n)

                if re.search(m.group(1) * 5, nextHash):
                    # print(h, nextHash, m.group(1), i, i + n)
                    keys[i] = nextHash
        
        i += 1

    return sorted(keys.keys())[-1]

print(part1(input))
