low = 245318
high = 765747


def is_password(n):
    digits = [int(d) for d in str(n)]
    if len(digits) != 6:
        return False

    # print(digits)

    # two adjacent digits are the same
    same_digits = False
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            same_digits = True

    if not same_digits:
        return False

    # digits never decrease
    never_decrease = True
    for i in range(len(digits) - 1):
        if digits[i] > digits[i + 1]:
            never_decrease = False

    if not never_decrease:
        return False

    # print(n)
    return True


assert is_password(111111)
assert is_password(223450) is False
assert is_password(123789) is False


print(sum([is_password(n) for n in range(low, high)]))
