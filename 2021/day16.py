from math import prod


with open('2021/inputs/day16.txt', encoding="utf-8") as f:
    lines = f.read().strip()

hex_to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}


class parser():
    def __init__(self, binary):
        self.ptr = 0
        self.binary = binary
        self.versions = 0

    def read(self, length):
        result = self.binary[self.ptr:self.ptr + length]
        self.ptr += length
        return result

    def read_int(self, length):
        return int(self.read(length), base=2)

    def subpackets(self):
        values = []
        if self.read(1) == "0":
            length = self.read_int(15)
            subpackets_len = 0
            while subpackets_len < length:
                sub_len, value = self.packet()
                subpackets_len += sub_len
                values.append(value)
        else:
            count = self.read_int(11)
            for _ in range(count):
                values.append(self.packet()[1])
        return values

    def packet(self):
        start = self.ptr
        self.versions += self.read_int(3)
        type_id = self.read_int(3)

        if type_id == 4:
            literal = ""
            while self.read(1) == "1":
                literal += self.read(4)
            literal += self.read(4)
            result = int(literal, base=2)
        else:
            values = self.subpackets()
            match type_id:
                case 0:
                    result = sum(values)
                case 1:
                    result = prod(values)
                case 2:
                    result = min(values)
                case 3:
                    result = max(values)
                case 5:
                    result = int(values[0] > values[1])
                case 6:
                    result = int(values[0] < values[1])
                case 7:
                    result = int(values[0] == values[1])

        return self.ptr - start, result


def part1():
    binary = "".join(hex_to_bin[c] for c in lines)
    p = parser(binary)
    p.packet()
    return p.versions


print(part1())


def part2():
    binary = "".join(hex_to_bin[c] for c in lines)
    return parser(binary).packet()[1]


print(part2())
