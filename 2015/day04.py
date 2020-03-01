from hashlib import md5

input = "bgvyzdsv"

def part1(s, count):
    i = 0
    while True:
        hash = md5((s + str(i)).encode()).hexdigest()
        if hash[:count] == '0' * count:
            return i
        i += 1

print(part1(input, 5))
print(part1(input, 6))