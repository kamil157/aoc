import re

input = open('2020/inputs/day13.txt').readlines()

def part1(s):
    start = int(s[0].strip())
    buses = [int(id) for id in s[1].split(',') if id != 'x']

    time = start
    while True:
        for bus in buses:
            if time % bus == 0:
                return (time - start) * bus
        time += 1

def part2(s):
    buses = [int(id) for id in s[1].split(',') if id != 'x']
    requirements = s[1].strip().split(',')

    t = 0
    step = 1
    for bus in (buses):        
        idx = requirements.index(str(bus))
        while t % bus != -idx % bus:
            t += step
        step *= bus        

    return t

print(part1(input))
print(part2(input))
