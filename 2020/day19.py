import re

input = open('2020/inputs/day19.txt').read()

def part1(s, part2):
    rules, messages = s.split('\n\n')

    d = {}
    for rule in rules.splitlines():
        n, r = rule.strip().split(':')
        d[int(n)] = r

    if part2:
        d[8] = '42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42'
        d[11] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31'
    
    for _ in range(len(d) - 1):
        for k, v in d.items():
            if not re.search(r'\d+', v):
                for n, rule in d.items():
                    d[n] = re.sub(fr'(?<!\d){k}(?!\d)', f"({v})", rule)
                del d[k]
                break                


    regex = d[0].replace('"', '').replace(' ', '')
    regex = f'^{regex}$'

    return len([message for message in messages.splitlines() if re.search(regex, message)])



print(part1(input, False))
print(part1(input, True))
