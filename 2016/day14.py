import re
from hashlib import md5

input = 'ngcjuoqr'

def hash(s, i):
    return md5((s + str(i)).encode()).hexdigest()

def hash2017(s, i):
    h = s + str(i)
    for _ in range(2017):
        h = md5(h.encode()).hexdigest()
    return h

def part1(s, f):
    i = 0
    keys = {}
    hashes = [f(s, i) for i in range(25000)]

    while len(keys) < 64:
        h = hashes[i]
        
        if m := re.search(r'(.)\1\1', h):
            for n in range(1, 1001):
                nextHash = hashes[i + n]

                if re.search(m.group(1) * 5, nextHash):
                    keys[i] = nextHash
        
        i += 1

    return sorted(keys.keys())[-1]

print(part1(input, hash))
print(part1(input, hash2017))
