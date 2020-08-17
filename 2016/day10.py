import re
from collections import defaultdict

input = open('2016/inputs/day10.txt').read()

def part1(s):
    lines = s.split('\n')
    i = 0

    bots = defaultdict(list)
    output = {}
    while lines:
        executed = False

        if m := re.search(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', lines[i]):
            bot = int(m.group(1))
            lowType = m.group(2)
            lowId = int(m.group(3))
            highType = m.group(4)
            highId = int(m.group(5))
            if len(bots[bot]) == 2:
                if sorted(bots[bot]) == [17, 61]:
                    result = bot
                lowValue = sorted(bots[bot])[0]
                highValue = sorted(bots[bot])[1]
                if lowType == 'bot':
                    bots[lowId].append(lowValue)
                else:
                    output[lowId] = lowValue
                if highType == 'bot':
                    bots[highId].append(highValue)
                else:
                    output[highId] = highValue 
                del bots[bot]
                executed = True

        elif m := re.search(r'value (\d+) goes to bot (\d+)', lines[i]):
            value = int(m.group(1))
            bot = int(m.group(2))
            bots[bot].append(value)
            executed = True
        
        if executed:
            del lines[i]
            i = 0
        else:
            i += 1

    return result, output[0] * output[1] * output[2]

print(part1(input))
