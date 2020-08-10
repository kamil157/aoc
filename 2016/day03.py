input = open('2016/inputs/day03.txt').readlines()

def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def count_real(triangles):
    return sum(1 for a, b, c in triangles if is_triangle(a, b, c))

def part1(s):
    triangles = [[int(n) for n in line.split()] for line in input]
    return count_real(triangles)

def part2(s):
    triangle_edges = [[int(n) for n in line.split()] for line in input]

    triangles = []
    for i in range(0, len(triangle_edges), 3):
        for j in range(3):
            triangles.append([triangle_edges[i][j], triangle_edges[i + 1][j], triangle_edges[i + 2][j]])

    return count_real(triangles)


print(part1(input))
print(part2(input))