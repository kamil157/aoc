from re import findall

input = open('2015/inputs/day16.txt').read()

def is_value_ok1(ticker, compound, value):
    return ticker[compound] == value

def is_value_ok2(ticker, compound, value):
    if compound == 'trees' or compound == 'cats':
        return value > ticker[compound]
    if compound == 'pomeranians' or compound == 'goldfish':
        return value < ticker[compound]
    return is_value_ok1(ticker, compound, value)

def is_aunt_ok(compounds, ticker, is_value_ok):
    return all(is_value_ok(ticker, compound, value) for compound, value in compounds.items())

def part1(s, is_value_ok):
    ticker = { 'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1 }

    aunts_data = findall(r'Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)', s)
    aunts = { n: { k1: int(v1), k2: int(v2), k3: int(v3) } for n, k1, v1, k2, v2, k3, v3 in aunts_data }

    return next(aunt for aunt, compounds in aunts.items() if is_aunt_ok(compounds, ticker, is_value_ok))

print(part1(input, is_value_ok1))
print(part1(input, is_value_ok2))