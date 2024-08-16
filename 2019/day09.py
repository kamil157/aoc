from intcode import Intcode

with open('2019/inputs/day09.txt') as f:
    input_raw = f.read()

input_ints = [int(n) for n in input_raw.split(',')]


def run(s, inp):
    intcode = Intcode(s)
    intcode.input(inp)
    while True:
        try:
            print(intcode.run())
        except StopIteration:
            return


if __name__ == "__main__":
    run('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99', 0)
    run('1102,34915192,34915192,7,4,7,99,0', 0)
    run('104,1125899906842624,99', 0)
    run(input_raw, 1)  # 2316632620
    run(input_raw, 2)  # 78869
