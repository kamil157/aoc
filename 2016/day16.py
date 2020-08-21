input = '11101000110010100'

def get_data(a, disk_size):
    while len(a) < disk_size:
        a += '0' + ''.join('0' if c == '1' else '1' for c in a[::-1])
    return a[:disk_size]

def part1(s, disk_size):
    data = get_data(s, disk_size)
    
    while True:
        checksum = ''
        for i in range(0, len(data), 2):
            checksum += '1' if data[i] == data[i + 1] else '0'
        data = checksum

        if len(checksum) % 2 != 0:
            break

    return checksum

print(part1(input, 272))
print(part1(input, 35651584))
