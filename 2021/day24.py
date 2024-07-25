with open('2021/inputs/day24.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def base26(n):
    result = ""
    while n > 0:
        result = chr(ord("a") + n % 26) + result
        n //= 26
    return result


def part1():
    program = [line.split() for line in lines]

    def monad(number):
        r = {"w": 0, "x": 0, "y": 0, "z": 0}

        def value(x):
            try:
                return int(x)
            except ValueError:
                return r[x]

        inputs = str(number)
        index = 0

        for instr in program:
            a = instr[1]
            if instr[0] != "inp":
                b = instr[2]
            match instr[0]:
                case "inp":
                    print(r, base26(r["z"]))
                    r[a] = int(inputs[index])
                    index += 1
                case "add":
                    r[a] += value(b)
                case "mul":
                    r[a] *= value(b)
                case "div":
                    r[a] = int(r[a] / value(b))
                case "mod":
                    r[a] %= value(b)
                case "eql":
                    r[a] = 1 if value(a) == value(b) else 0

        print(r, base26(r["z"]))
        return r["z"] == 0

    return monad(99893999291967), monad(34171911181211)


print(part1())
