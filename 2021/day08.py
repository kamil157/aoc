from collections import defaultdict
from itertools import permutations, product


with open('2021/inputs/day08.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def part1():
    return sum(len(digit) in [2, 3, 4, 7] for line in lines for digit in line.split(" | ")[1].split())


print(part1())


def valid(segment_mixed):
    segments_orig = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }
    segments_orig = {v: k for k, v in segments_orig.items()}

    def normalize(segments):
        reverse = defaultdict(list)
        for s, d in segments.items():
            for c in s:
                reverse[c].append(d)
        return sorted(map(sorted, reverse.values()))

    return normalize(segments_orig) == normalize(segment_mixed)


def part2():
    result = 0

    lengths = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    lengths_dict = defaultdict(list)
    for d, l in enumerate(lengths):
        lengths_dict[l].append(d)

    for line in lines:
        input, output = line.split(" | ")

        mappings = [permutations(digits) for digits in lengths_dict.values()]
        for mapping in product(*mappings):
            segment_map = {}
            for digits in mapping:
                segments = ["".join(sorted(digit)) for digit in input.split() if len(
                    digit) == lengths[digits[0]]]
                for i, digit in enumerate(digits):
                    segment_map[segments[i]] = digit

            if valid(segment_map):
                value = ""
                for segments in output.split():
                    value += str(segment_map["".join(sorted(segments))])
                result += int(value)

    return result


print(part2())
