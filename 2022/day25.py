with open('2022/inputs/day25.txt', encoding="utf-8") as f:
    lines = f.read().split('\n')

values = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
inverse = {v: k for k, v in values.items()}


def to_decimal(snafu):
    return sum(5 ** i * values[d] for i, d in enumerate(snafu[::-1]))


def to_snafu(decimal):
    snafu = ""
    while decimal:
        digit = (decimal + 2) % 5 - 2
        if digit < 0:
            decimal += 5
        decimal //= 5
        snafu += inverse[digit]
    return snafu[::-1]


def solve():
    return to_snafu(sum(to_decimal(snafu) for snafu in lines))


print(solve())
