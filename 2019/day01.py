with open('2019/inputs/day01.txt') as f:
    input = f.read()


def fuel(n):
    return n // 3 - 2


assert fuel(12) == 2
assert fuel(14) == 2
assert fuel(1969) == 654
assert fuel(100756) == 33583

print(sum(fuel(int(n)) for n in input.split()))

#####################


def total_fuel(n):
    total = 0
    f = fuel(n)
    while f > 0:
        total += f
        f = fuel(f)
    return total


assert total_fuel(14) == 2
assert total_fuel(1969) == 966
assert total_fuel(100756) == 50346

print(sum(total_fuel(int(n)) for n in input.split()))
