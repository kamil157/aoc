import re

input = open('2016/inputs/day07.txt').readlines()

def isTLS(ip):
    abba = re.search(r'(\w)(\w)\2\1', ip)
    inBrackets = re.search(r'\[\w*(\w)(\w)\2\1\w*]', ip)
    return abba and not inBrackets and abba.group(1) != abba.group(2)

def part1(s):
    return sum(1 for line in s if isTLS(line))

def isSSL(ip):
    inside = set()
    outside = set()
    inBrackets = False
    
    for i in range(len(ip) - 2):
        if ip[i] == '[':
            inBrackets = True
        elif ip[i] == ']':
            inBrackets = False
        window = ip[i:i + 3]
        
        if window[0] == window[2] and window[0] != window[1]:
            if inBrackets:
                inside.add(window)
            else:
                outside.add(window)

    for s in inside:
        if s[1] + s[0] + s[1] in outside:
            return True
    
    return False

def part2(s):
    return sum(1 for line in s if isSSL(line))

print(part1(input))
print(part2(input))

