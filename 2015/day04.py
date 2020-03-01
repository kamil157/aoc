from hashlib import md5
from itertools import count

input = "bgvyzdsv"

def hash(s, i):
    return md5((s + str(i)).encode()).hexdigest()

def part1(s, digits):
    return(next(i for i in count() if hash(s, i)[:digits] == '0' * digits))

print(part1(input, 5))
print(part1(input, 6))