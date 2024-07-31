from parse import parse
with open('2018/inputs/day17.txt', encoding="utf-8") as f:
    lines = f.read().strip().splitlines()


def part1():
    g = {}
    for line in lines:
        if nums := parse("x={:d}, y={:d}..{:d}", line):
            (x, y1, y2) = nums
            for y in range(y1, y2+1):
                g[x+y*1j] = "#"
        elif nums := parse("y={:d}, x={:d}..{:d}", line):
            (y, x1, x2) = nums
            for x in range(x1, x2+1):
                g[x+y*1j] = "#"

    source = 500

    top = min(int(n.imag) for n in g)
    bottom = max(int(n.imag) for n in g)

    def go_down(pos):
        while g.get(pos + 1j, ".") in ".|":
            pos += 1j
            if int(pos.imag) >= top:
                g[pos] = "|"
            if int(pos.imag) >= bottom:
                return

        left = pos
        while g.get(left + 1j, ".") in "#~" and g.get(left - 1, ".") in ".|":
            left -= 1
            g[left] = "|"

        if g.get(left + 1j, ".") in ".|":
            go_down(left)

        right = pos
        while g.get(right + 1j, ".") in "#~" and g.get(right + 1, ".") in ".|":
            right += 1
            g[right] = "|"

        if g.get(right + 1j, ".") in ".|":
            go_down(right)

        if g.get(left + 1j, ".") in "#~" and g.get(right + 1j, ".") in "#~":
            lowest = left
            while g.get(lowest, ".") in ".|":
                g[lowest] = "~"
                go_down(lowest)
                lowest += 1

        if len([tile for tile in g.values() if tile in "|~"]) >= 30809:
            print(len([tile for tile in g.values() if tile in "|~"]))
        if len([tile for tile in g.values() if tile in "|~"]) % 30809 == 0:
            with open('2018/inputs/day17a.txt', "w", encoding="utf-8") as f:
                for y in range(2000):
                    line = ""
                    for x in range(400, 700):
                        line += g.get(x+y*1j, ".")
                    f.write(line + '\n')
                exit()

    for i in range(100):
        go_down(source)
        print(i)

    with open('2018/inputs/day17a.txt', "w", encoding="utf-8") as f:
        for y in range(2000):
            line = ""
            for x in range(400, 700):
                line += g.get(x+y*1j, ".")
            f.write(line + '\n')
    return len([tile for tile in g.values() if tile in "|~"])


print(part1())
