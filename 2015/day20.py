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
            return i


print(part1(input))


def part2():
    best = input
    presents = collections.defaultdict(int)
    for elf in range(input // 11):
        for i in range(1, 51):
            presents[elf * i] += 11 * elf
            if presents[elf * i] >= input and elf * i < best:
                best = elf * i

    return best


print(part2())
