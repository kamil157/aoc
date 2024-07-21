with open('2020/inputs/day21.txt', encoding="utf-8") as f:
    lines = f.read().strip().split('\n')


def parse():
    parsed_lines = []
    for line in lines:
        ingredients, allergens = line.split(" (contains ")
        ingredients = ingredients.split()
        allergens = allergens[:-1].replace(",", "").split()
        parsed_lines.append((ingredients, allergens))
    return parsed_lines


def mapping_from_input(parsed_lines):
    all_ingredients = set()
    all_allergens = set()

    for ingredients, allergens in parsed_lines:
        all_ingredients |= set(ingredients)
        all_allergens |= set(allergens)
    d = {a: set(all_ingredients) for a in all_allergens}

    for ingredients, allergens in parsed_lines:
        for a in allergens:
            d[a] &= set(ingredients)

    return d


def part1(parsed_lines, allergic_ingredients):
    total = 0
    for ingredients, _ in parsed_lines:
        for ingredient in ingredients:
            if ingredient not in allergic_ingredients:
                total += 1
    return total


def part2(allergic_ingredients, d):
    definite = []
    used = set()
    while len(definite) < len(allergic_ingredients):
        for a, i in d.items():
            i -= used
            if len(i) == 1:
                definite.append((a, list(i)[0]))
                used.add(list(i)[0])

    return ",".join(m[1] for m in sorted(definite))


def solve():
    parsed_lines = parse()
    d = mapping_from_input(parsed_lines)

    allergic_ingredients = set()
    for ingredients in d.values():
        allergic_ingredients |= ingredients

    return part1(parsed_lines, allergic_ingredients), part2(allergic_ingredients, d)


print(solve())
