def part1():
    t = 440231
    recipes = [3, 7]
    first = 0
    second = 1

    while True:
        recipe = recipes[first] + recipes[second]
        if recipe >= 10:
            recipes.append(recipe // 10)
        recipes.append(recipe % 10)
        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)

        if len(recipes) - 10 > t:
            return "".join(map(str, recipes[t:t + 10]))


print(part1())


def part2():
    t = "440231"
    digits = [int(d) for d in t]
    recipes = [3, 7]
    first = 0
    second = 1

    while True:
        recipe = recipes[first] + recipes[second]
        if recipe >= 10:
            recipes.append(recipe // 10)
        if digits == recipes[-len(t):]:
            return len(recipes) - len(t)

        recipes.append(recipe % 10)
        if digits == recipes[-len(t):]:
            return len(recipes) - len(t)

        first = (first + recipes[first] + 1) % len(recipes)
        second = (second + recipes[second] + 1) % len(recipes)


print(part2())
