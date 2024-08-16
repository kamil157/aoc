low = 245318
high = 765747


def is_password(n, part2):
    digits = [int(d) for d in str(n)]
    if len(digits) != 6:
        return False

    # two adjacent digits are the same
    same_digits = False
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            if part2:
                if i - 1 >= 0 and digits[i - 1] == digits[i]:
                    continue
                if i + 2 < len(digits) and digits[i + 2] == digits[i]:
                    continue
            same_digits = True

    if not same_digits:
        return False

    # digits never decrease
    never_decrease = True
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            never_decrease = False

    return never_decrease


print(sum([is_password(n, False) for n in range(low, high)]))
print(sum([is_password(n, True) for n in range(low, high)]))
