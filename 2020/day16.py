import re
from collections import defaultdict
from math import prod

input = open('2020/inputs/day16.txt').read()

def valid_add(valid, lo, hi):
    for n in range(lo, hi + 1):
        valid.add(n)

def parse_nearby(nearby):
    return [[int(n) for n in line.split(',')] for line in nearby.split('\n')[1:]]

def parse_ranges(ranges):
    valid = set()
    range_dict = {}
    parsed_ranges = re.findall(r'([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)', ranges)
    for r in parsed_ranges:
        name, lo1, hi1, lo2, hi2 = r[0], int(r[1]), int(r[2]), int(r[3]), int(r[4])
        valid_add(valid, lo1, hi1)
        valid_add(valid, lo2, hi2)
        range_dict[name] = (range(lo1, hi1 + 1), range(lo2, hi2 + 1))

    return valid, range_dict

def part1(s):
    ranges, _, nearby = s.split('\n\n')
    valid = parse_ranges(ranges)[0]
    parsed_nearby = parse_nearby(nearby)
    invalid_fields = [n for ticket in parsed_nearby for n in ticket if n not in valid]
    return sum(invalid_fields)

def is_valid(ticket, valid):
    return all(n in valid for n in ticket)

def is_possible(field_values, range1, range2):
    return all(n in range1 or n in range2 for n in field_values)

def part2(s):
    ranges, your, nearby = s.split('\n\n')
    valid, range_dict = parse_ranges(ranges)
    your_ticket = [int(n) for n in your.split('\n')[1].split(',')]
    parsed_nearby = parse_nearby(nearby)
    valid_tickets = [ticket for ticket in parsed_nearby if is_valid(ticket, valid)]    
        
    possible_fields = defaultdict(list)
    for i in range(len(your_ticket)):
        field_values = [ticket[i] for ticket in valid_tickets]
        for name, (range1, range2) in range_dict.items():    
            if is_possible(field_values, range1, range2):
                possible_fields[i].append(name)

    fields = {}
    for idx in sorted(possible_fields, key=lambda idx: len(possible_fields[idx])):
        fields[idx] = next(name for name in possible_fields[idx] if name not in fields.values())

    return prod(your_ticket[idx] for idx, name in fields.items() if 'departure' in name)

print(part1(input))
print(part2(input))
