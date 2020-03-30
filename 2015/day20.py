import itertools
import collections
from math import prod

input = 36000000

def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1

    if n > 1:
        yield n

def get_divisors(n):
    pf = prime_factors(n)

    pf_with_multiplicity = collections.Counter(pf)

    powers = [
        [factor ** i for i in range(count + 1)]
        for factor, count in pf_with_multiplicity.items()
    ]

    for prime_power_combo in itertools.product(*powers):
        yield prod(prime_power_combo)

def part1(n):
    for i in itertools.count():
        presents = 10 * sum(get_divisors(i))
        if presents >= n:
            print(i, presents)
            return i

elf_count = 5000

def part2(n):
    presents = [0] * elf_count
    for elf in range(1, elf_count):
        delivered = 0
        for house in range(1, len(presents)):
            if delivered == 50:
                break
            if house % elf == 0:
                delivered += 1
                presents[house] += 11 * elf
                if presents[house] >= n:
                    print(house, presents[house])


    for i, p in enumerate(presents):
        if p >= n:
            print(i, p)
            return i

# print(part1(input))
print(part2(50000))