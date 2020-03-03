input = '1113122113'

def part1(s, iterations):
    for _ in range(iterations):
        s1 = ''
        current_digit = s[0]
        current_len = 1
        for d in s[1:]:
            if d == current_digit:
                current_len += 1
            else:
                s1 += str(current_len) + current_digit
                current_digit = d
                current_len = 1

        s = s1 + str(current_len) + current_digit
    return len(s)

print(part1(input, 40))
print(part1(input, 50))