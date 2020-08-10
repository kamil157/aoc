from hashlib import md5

input = 'ffykfhsq'

def hash(index):
    s = input + str(index)
    return md5(s.encode()).hexdigest()

def part1(s):
    password = ''
    index = 0
    while len(password) < 8:
        h = hash(index)
        if h[:5] == '00000':
            password += h[5]
        index += 1
    return password

def part2(s):
    password = ['*' for _ in range(8)]
    index = 0
    while '*' in password:
        h = hash(index)
        # if (index % 30000 == 0):
            # print(''.join(password), hash, end='\r')
        try:
            if h[:5] == '00000' and password[int(h[5])] == '*':
                password[int(h[5])] = h[6]
        except:
            pass
        index += 1
    return ''.join(password)

print(part1(input))
print(part2(input))
