import re
import json

input = open('2015/inputs/day12.txt').read()

def part1(s):
    numbers = re.findall(r'-?\d+', s)
    return sum(int(n) for n in numbers)

def count(obj):
    if isinstance(obj, int):
        return obj

    if isinstance(obj, dict):
        if 'red' in obj.values():
            return 0
        return sum(map(count, obj.values()))

    if isinstance(obj, list):
        return sum(map(count, obj))

    return 0    

def part2(s):
    return count(json.loads(s))
    
print(part1(input))
print(part2(input))