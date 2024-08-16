from intcode import Intcode

with open('2019/inputs/day05.txt') as f:
    input_raw = f.read()


def intcode(s, input):
    i = Intcode(s)
    i.input(input)

    while True:
        try:
            output = i.run()
        except StopIteration:
            return output


if __name__ == "__main__":
    print(intcode(input_raw, 1))  # 9938601
    print(intcode(input_raw, 5))  # 4283952
