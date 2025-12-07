with open('2025/inputs/day02.txt', encoding="utf-8") as f:
    lines = f.read().splitlines()


def part1():
    result = 0
    for ids in lines[0].split(","):
        ids = ids.split("-")
        start, end = int(ids[0]), int(ids[1])
        for i in range(start, end + 1):
            s = str(i)
            if s[:len(s)//2] == s[len(s)//2:]:
                result += i
    return result

def part2():
    result = 0
    for ids in lines[0].split(","):
        ids = ids.split("-")
        start, end = int(ids[0]), int(ids[1])
        for i in range(start, end + 1):
            s = str(i)
            for j in range(1, len(s) // 2 + 1):
                substrings = set()
                cur = 0
                while cur < len(s):
                    substrings.add(s[cur:cur+j])
                    cur += j
                if len(substrings) == 1:
                    result += i
                    break
    return result


print(part1())
print(part2())
