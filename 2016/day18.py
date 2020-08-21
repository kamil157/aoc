input = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'

safe = '.'
trap = '^'

def next_row(row):
    next = ''
    for i in range(len(row)):
        left = row[i - 1] if i > 0 else safe
        right = row[i + 1] if i < len(row) - 1 else safe
        next += trap if left != right else safe
    return next

def part1(s, rows):
    row = s
    safe_count = 0
    for _ in range(rows):
        safe_count += row.count(safe)
        row = next_row(row)

    return safe_count

print(part1(input, 40))
print(part1(input, 400000))
