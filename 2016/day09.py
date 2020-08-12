import re

input = open('2016/inputs/day09.txt').read()

def length(s, f):
    return len(s)

def decompress(s, f):
    i = 0
    count = 0

    while i < len(s):
        if s[i] == '(':
            m = re.search(r'\((\d+)x(\d+)\)', s[i:])
            chars = int(m.group(1))
            repeat = int(m.group(2))
            
            i += len(m.group(0))
            count += repeat * f(s[i:i + chars], f)
            i += chars
        else:
            i += 1
            count += 1
            
    return count

print(decompress(input, length))
print(decompress(input, decompress))
