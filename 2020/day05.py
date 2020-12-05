input = open('2020/inputs/day05.txt').readlines()

def binary(s, lo, hi, lo_char, hi_char):
    for c in s:
        if c == lo_char:
            hi = (hi + lo) // 2
        elif c == hi_char:
            lo = (hi + lo) // 2 + 1

    assert lo == hi
    return lo

def seat_id(s):
    row = binary(s[:7], 0, 127, 'F', 'B')
    col = binary(s[7:10], 0, 7, 'L', 'R')
    return row * 8 + col

def part1(s):
    return max(seat_id(line) for line in s)
        
def part2(s):
    all_seats = set(range(8 * 128))
    taken_seats = set(seat_id(line) for line in s)
    empty_seats = all_seats - taken_seats
    for seat in empty_seats:
        if seat - 1 in taken_seats and seat + 1 in taken_seats:
            return seat

print(part1(input))
print(part2(input))
