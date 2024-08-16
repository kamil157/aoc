from itertools import *

with open('2019/inputs/day16.txt') as f:
    input = f.read()


def fft(s, phases):
    digits = [int(d) for d in s]
    pattern = [0, 1, 0, -1]

    for _ in range(phases):
        new_digits = []
        for i in range(len(digits)):
            pattern_for_digit = list(chain.from_iterable(
                [repeat(pattern[j], i + 1) for j in range(len(pattern))]))
            factors = list(islice(chain.from_iterable(
                repeat(pattern_for_digit)), 1, len(s) + 1))
            product = sum(digits[j] * factors[j] for j in range(len(digits)))
            new_digits.append(abs(product) % 10)
        digits = new_digits
    return ''.join([str(d) for d in digits])[:8]


assert fft("12345678", 4) == "01029498"
assert fft("80871224585914546619083218645595", 100) == "24176176"
assert fft("19617804207202209144916044189917", 100) == "73745418"
assert fft("69317163492948606335995924319873", 100) == "52432133"
print(fft(input, 100))  # 10189359


def real_signal(s):
    offset = int(s[:7])
    signal = s * 10000

    digits = [int(d) for d in signal[offset:]]
    for _ in range(100):
        total = 0
        for i, d in reversed(list(enumerate(digits))):
            total += d
            digits[i] = total % 10
    return ''.join([str(d) for d in digits])[:8]


assert real_signal("03036732577212944063491565474664") == "84462026"
assert real_signal("02935109699940807407585447034323") == "78725270"
assert real_signal("03081770884921959731165446850517") == "53553731"
print(real_signal(input))  # 80722126
