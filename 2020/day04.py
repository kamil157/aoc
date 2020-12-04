import re

input = open('2020/inputs/day04.txt').read()

def get_passports(s):
    result = []
    passports = [p.replace('\n', ' ').split() for p in s.split('\n\n')]
    for passport in passports:
        d = {pair.split(':')[0]: pair.split(':')[1] for pair in passport}
        result.append(d)
    return result

def has_fields(passport):
    fields = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    return fields.issubset(passport.keys())

def part1(s):
    return sum(1 for passport in get_passports(s) if has_fields(passport))

def part2(s):
    count = 0
    
    for passport in get_passports(s):
        if not has_fields(passport):
            continue

        if not 1920 <= int(passport['byr']) <= 2002:
            continue
        
        if not 2010 <= int(passport['iyr']) <= 2020:
            continue
        
        if not 2020 <= int(passport['eyr']) <= 2030:
            continue

        if passport['hgt'][-2:] != 'cm' and passport['hgt'][-2:] != 'in':
            continue

        if passport['hgt'][-2:] == 'cm':
            if not 150 <= int(passport['hgt'][:-2]) <= 193:
                continue

        if passport['hgt'][-2:] == 'in':
            if not 59 <= int(passport['hgt'][:-2]) <= 76:
                continue

        if not re.search('^#[0-9a-f]{6}$', passport['hcl']):
            continue

        if not re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl']):
            continue
        
        if not re.search('^[0-9]{9}$', passport['pid']):
            continue
        
        count +=1 

    return count

print(part1(input))
print(part2(input))
